#!/usr/bin/env python3
"""
Codebase mapper: Walks a Python repository and extracts a structured map of
modules, classes, functions, signatures, docstrings, imports, inheritance,
and variables. Outputs JSON (authoritative) and optional Markdown summary.

Strictly uses standard library only. Robust to parse errors (continues and records).
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import traceback
from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List, Optional, Tuple, Union

import ast


def now_iso() -> str:
    """Return current UTC timestamp in ISO-8601 format with timezone.

    Returns:
        ISO8601 string, e.g. '2025-01-01T00:00:00+00:00'.
    """
    return _dt.datetime.now(_dt.timezone.utc).isoformat()


def safe_read_text(path: str) -> Optional[str]:
    """Safely read a text file as UTF-8.

    Args:
        path: Absolute or relative filesystem path.

    Returns:
        File contents as string, or None if any I/O error occurs.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


def expr_to_str(node: Optional[ast.AST]) -> Optional[str]:
    """Best-effort string representation of an AST expression node.

    Args:
        node: AST node to stringify.

    Returns:
        String form via ast.unparse/ast.dump, or None if input is None.
    """
    if node is None:
        return None
    try:
        # Python 3.9+
        return ast.unparse(node)  # type: ignore[attr-defined]
    except Exception:
        try:
            return ast.get_source_segment("", node) or ast.dump(node)
        except Exception:
            return ast.dump(node)


def name_from_base(node: ast.expr) -> str:
    """Extract a readable class base name from an AST expr.

    Handles dotted attributes and falls back to ast.unparse/ast.dump.
    """
    try:
        return ast.unparse(node)  # type: ignore[attr-defined]
    except Exception:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            parts: List[str] = []
            cur: Optional[ast.AST] = node
            while isinstance(cur, ast.Attribute):
                parts.append(cur.attr)
                cur = cur.value  # type: ignore[assignment]
            if isinstance(cur, ast.Name):
                parts.append(cur.id)
            parts.reverse()
            return ".".join(parts) if parts else ast.dump(node)
        return ast.dump(node)


def decorator_to_str(dec: ast.expr) -> str:
    """Return readable string for a decorator expression."""
    return expr_to_str(dec) or "<unknown>"


def default_value_to_str(node: Optional[ast.expr]) -> Optional[str]:
    """Return readable string for a default value expression (or None)."""
    return expr_to_str(node)


def get_arg(arg: ast.arg) -> Dict[str, Any]:
    """Convert ast.arg to a serializable dict with name and annotation."""
    return {
        "name": arg.arg,
        "annotation": expr_to_str(arg.annotation),
    }


def get_function_signature(node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> Dict[str, Any]:
    """Extract a structured signature from a function/async function AST.

    Args:
        node: FunctionDef or AsyncFunctionDef node.

    Returns:
        Dict with positional_only, keyword_only, vararg/kwarg names and
        annotations, defaults, and return annotation.
    """
    args = node.args

    posonly = [get_arg(a) for a in getattr(args, "posonlyargs", [])]
    regular = [get_arg(a) for a in args.args]
    kwonly = [get_arg(a) for a in args.kwonlyargs]

    defaults = [default_value_to_str(d) for d in args.defaults]
    kw_defaults = [default_value_to_str(d) for d in args.kw_defaults]

    vararg = args.vararg.arg if args.vararg else None
    vararg_annotation = expr_to_str(args.vararg.annotation) if args.vararg else None

    kwarg = args.kwarg.arg if args.kwarg else None
    kwarg_annotation = expr_to_str(args.kwarg.annotation) if args.kwarg else None

    # Align defaults with the last N of (posonly+regular)
    positional_params = posonly + regular
    num_with_defaults = len(defaults)
    positional_defaults: List[Optional[str]] = [None] * (len(positional_params) - num_with_defaults) + defaults

    for i, default in enumerate(positional_defaults):
        if default is not None:
            positional_params[i]["default"] = default

    for i, default in enumerate(kw_defaults):
        if default is not None and i < len(kwonly):
            kwonly[i]["default"] = default

    return {
        "positional_only": positional_params,
        "keyword_only": kwonly,
        "vararg": vararg,
        "vararg_annotation": vararg_annotation,
        "kwarg": kwarg,
        "kwarg_annotation": kwarg_annotation,
        "returns": expr_to_str(node.returns),
    }


def extract_imports(tree: ast.AST) -> Dict[str, Any]:
    """Collect all import and from-import statements in a module AST.

    Returns:
        Dict with keys 'imports' (List[str]) and 'from_imports' (List[dict]).
    """
    imports: List[str] = []
    from_imports: List[Dict[str, Any]] = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for alias in n.names:
                if alias.asname:
                    imports.append(f"{alias.name} as {alias.asname}")
                else:
                    imports.append(alias.name)
        elif isinstance(n, ast.ImportFrom):
            mod = n.module or ""
            names: List[str] = []
            for alias in n.names:
                if alias.asname:
                    names.append(f"{alias.name} as {alias.asname}")
                else:
                    names.append(alias.name)
            from_imports.append({
                "module": ("." * n.level) + mod,
                "names": names,
            })
    return {"imports": imports, "from_imports": from_imports}


def extract_variables(tree: ast.AST) -> Dict[str, List[Dict[str, Any]]]:
    """Collect top-level module variables (Assign/AnnAssign simple names).

    Returns:
        Dict with key 'module_variables' listing name, annotation, and value.
    """
    module_vars: List[Dict[str, Any]] = []
    for n in tree.body if isinstance(tree, ast.Module) else []:  # type: ignore[attr-defined]
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            module_vars.append({
                "name": n.target.id,
                "annotation": expr_to_str(n.annotation),
                "value": expr_to_str(n.value),
            })
        elif isinstance(n, ast.Assign):
            # Collect only simple Name targets
            value_str = expr_to_str(n.value)
            for tgt in n.targets:
                if isinstance(tgt, ast.Name):
                    module_vars.append({
                        "name": tgt.id,
                        "annotation": None,
                        "value": value_str,
                    })
    return {"module_variables": module_vars}


def extract_class(node: ast.ClassDef) -> Dict[str, Any]:
    """Extract class metadata: bases, decorators, docstring, methods, variables."""
    bases = [name_from_base(b) for b in node.bases]
    decorators = [decorator_to_str(d) for d in node.decorator_list]
    doc = ast.get_docstring(node)

    methods: List[Dict[str, Any]] = []
    properties: List[str] = []
    class_variables: List[Dict[str, Any]] = []

    for n in node.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            sig = get_function_signature(n)
            m_entry = {
                "name": n.name,
                "async": isinstance(n, ast.AsyncFunctionDef),
                "decorators": [decorator_to_str(d) for d in n.decorator_list],
                "signature": sig,
                "docstring": ast.get_docstring(n),
            }
            methods.append(m_entry)
            # Track properties by decorator names
            if any(getattr(d, "id", None) == "property" or (isinstance(d, ast.Attribute) and getattr(d, "attr", "") == "setter") for d in n.decorator_list):
                properties.append(n.name)
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            class_variables.append({
                "name": n.target.id,
                "annotation": expr_to_str(n.annotation),
                "value": expr_to_str(n.value),
            })
        elif isinstance(n, ast.Assign):
            value_str = expr_to_str(n.value)
            for tgt in n.targets:
                if isinstance(tgt, ast.Name):
                    class_variables.append({
                        "name": tgt.id,
                        "annotation": None,
                        "value": value_str,
                    })

    return {
        "name": node.name,
        "bases": bases,
        "decorators": decorators,
        "docstring": doc,
        "methods": methods,
        "properties": properties,
        "class_variables": class_variables,
    }


def extract_function(node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> Dict[str, Any]:
    """Extract function metadata: name, async, decorators, signature, docstring."""
    sig = get_function_signature(node)
    return {
        "name": node.name,
        "async": isinstance(node, ast.AsyncFunctionDef),
        "decorators": [decorator_to_str(d) for d in node.decorator_list],
        "signature": sig,
        "docstring": ast.get_docstring(node),
    }


def analyze_module(py_path: str, rel_path: str) -> Dict[str, Any]:
    """Analyze a Python file into a serializable module report.

    Args:
        py_path: Absolute path to the Python file.
        rel_path: Path relative to repo root (for identification).

    Returns:
        Dict containing module docstring, classes, functions, imports,
        variables, and parse errors (if any).
    """
    src = safe_read_text(py_path)
    if src is None:
        return {
            "path": rel_path,
            "docstring": None,
            "classes": [],
            "functions": [],
            "imports": {"imports": [], "from_imports": []},
            "variables": {"module_variables": []},
            "errors": ["Unable to read file"],
        }

    try:
        tree = ast.parse(src, filename=py_path)
    except Exception as e:
        return {
            "path": rel_path,
            "docstring": None,
            "classes": [],
            "functions": [],
            "imports": {"imports": [], "from_imports": []},
            "variables": {"module_variables": []},
            "errors": [f"ParseError: {e.__class__.__name__}: {e}"],
        }

    module_doc = ast.get_docstring(tree)
    imports = extract_imports(tree)
    variables = extract_variables(tree)

    classes: List[Dict[str, Any]] = []
    functions: List[Dict[str, Any]] = []

    for n in tree.body if isinstance(tree, ast.Module) else []:  # type: ignore[attr-defined]
        if isinstance(n, ast.ClassDef):
            classes.append(extract_class(n))
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(extract_function(n))

    return {
        "path": rel_path,
        "docstring": module_doc,
        "classes": classes,
        "functions": functions,
        "imports": imports,
        "variables": variables,
        "errors": [],
    }


def is_python_file(path: str) -> bool:
    """Return True if filename looks like a Python source file."""
    return path.endswith(".py") and not os.path.basename(path).startswith(".")


def should_skip_dir(dir_name: str) -> bool:
    """Directory skip policy for traversal (caches, VCS, virtualenvs, etc.)."""
    skip = {
        ".git",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".venv",
        "env",
        "venv",
        "node_modules",
        "htmlcov",
    }
    return dir_name in skip


def build_dir_tree(root: str) -> Dict[str, Any]:
    """Build a nested dict of the directory tree rooted at 'root'.

    Returns:
        Mapping of subdirectories and a special '__files__' list per node.
    """
    tree: Dict[str, Any] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        # In-place filter of directories
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        rel = os.path.relpath(dirpath, root)
        node = tree
        if rel != ".":
            for part in rel.split(os.sep):
                node = node.setdefault(part, {})
        node["__files__"] = sorted([f for f in filenames if not f.startswith(".")])
    return tree


def tree_to_ascii(tree: Dict[str, Any], prefix: str = "") -> str:
    """Render a directory tree dict (from build_dir_tree) as ASCII lines."""
    lines: List[str] = []

    def walk(node: Dict[str, Any], pre: str, is_root: bool = False) -> None:
        files = node.get("__files__", [])
        entries = [k for k in node.keys() if k != "__files__"]
        entries.sort()
        for idx, name in enumerate(entries):
            last = idx == len(entries) - 1 and not files
            connector = "└── " if last else "├── "
            lines.append(f"{pre}{connector}{name}/")
            child = node[name]
            new_pre = f"{pre}{'    ' if last else '│   '}"
            walk(child, new_pre)
        for i, f in enumerate(files):
            last = i == len(files) - 1
            connector = "└── " if last else "├── "
            lines.append(f"{pre}{connector}{f}")

    walk(tree, prefix, True)
    return "\n".join(lines)


def generate_markdown(report: Dict[str, Any]) -> str:
    """Generate a human-readable Markdown summary of the codebase report."""
    lines: List[str] = []
    lines.append(f"# Codebase Map\n")
    lines.append(f"Generated at: {report.get('generated_at', '')} UTC\n")
    lines.append("")

    summary = report.get("summary", {})
    lines.append("## Summary\n")
    for k in ("num_files", "num_modules", "num_classes", "num_functions"):
        if k in summary:
            lines.append(f"- {k}: {summary[k]}")
    lines.append("")

    lines.append("## Directory Tree\n")
    lines.append("````")
    lines.append(report.get("tree_ascii", ""))
    lines.append("````\n")

    lines.append("## Modules\n")
    for mod in report.get("modules", []):
        lines.append(f"### {mod['path']}")
        if mod.get("docstring"):
            lines.append("- Module docstring:")
            lines.append("```")
            lines.append(mod["docstring"] or "")
            lines.append("```")
        imp = mod.get("imports", {})
        imports = imp.get("imports", [])
        from_imports = imp.get("from_imports", [])
        if imports or from_imports:
            lines.append("- Imports:")
            for i in imports:
                lines.append(f"  - import {i}")
            for fi in from_imports:
                names = ", ".join(fi.get("names", []))
                lines.append(f"  - from {fi.get('module', '')} import {names}")
        if mod.get("variables", {}).get("module_variables"):
            lines.append("- Module variables:")
            for v in mod["variables"]["module_variables"]:
                ann = f": {v['annotation']}" if v.get("annotation") else ""
                val = f" = {v['value']}" if v.get("value") else ""
                lines.append(f"  - {v['name']}{ann}{val}")
        if mod.get("classes"):
            lines.append("- Classes:")
            for cls in mod["classes"]:
                bases = f"({', '.join(cls.get('bases', []))})" if cls.get("bases") else ""
                lines.append(f"  - {cls['name']}{bases}")
                if cls.get("docstring"):
                    lines.append("    - Docstring:")
                    lines.append("    ```")
                    lines.append(cls["docstring"] or "")
                    lines.append("    ```")
                if cls.get("methods"):
                    lines.append("    - Methods:")
                    for m in cls["methods"]:
                        ret = m.get("signature", {}).get("returns")
                        ret_str = f" -> {ret}" if ret else ""
                        lines.append(f"      - {m['name']}{ret_str}")
                if cls.get("class_variables"):
                    lines.append("    - Class variables:")
                    for v in cls["class_variables"]:
                        ann = f": {v['annotation']}" if v.get("annotation") else ""
                        val = f" = {v['value']}" if v.get("value") else ""
                        lines.append(f"      - {v['name']}{ann}{val}")
        if mod.get("functions"):
            lines.append("- Functions:")
            for fn in mod["functions"]:
                ret = fn.get("signature", {}).get("returns")
                ret_str = f" -> {ret}" if ret else ""
                lines.append(f"  - {fn['name']}{ret_str}")
        if mod.get("errors"):
            lines.append("- Errors:")
            for e in mod["errors"]:
                lines.append(f"  - {e}")
        lines.append("")
    return "\n".join(lines)


def compute_import_edges(modules: List[Dict[str, Any]]) -> List[Tuple[str, str]]:
    """Compute directed import edges (module path -> imported module string)."""
    edges: List[Tuple[str, str]] = []
    # Map import strings roughly to relative paths (best effort)
    # We do not resolve fully; we just keep module strings as nodes.
    for m in modules:
        src = m["path"]
        imp = m.get("imports", {})
        for name in imp.get("imports", []):
            tgt = name.split(" as ")[0].strip()
            edges.append((src, tgt))
        for fi in imp.get("from_imports", []):
            module = fi.get("module", "")
            if module:
                edges.append((src, module))
    return edges


def generate_dot(edges: List[Tuple[str, str]]) -> str:
    """Generate Graphviz DOT content for a list of import edges."""
    lines = ["digraph imports {"]
    lines.append("  rankdir=LR;")
    for src, tgt in edges:
        # Escape quotes
        s = src.replace("\"", "'")
        t = tgt.replace("\"", "'")
        lines.append(f'  "{s}" -> "{t}";')
    lines.append("}")
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entrypoint.

    Options:
        --root: directory to scan
        --output-json/--output-md/--output-dot: artifact destinations
        --follow-symlinks: os.walk followlinks flag

    Returns:
        Process exit code (0 on success).
    """
    parser = argparse.ArgumentParser(description="Map a Python codebase to JSON and Markdown.")
    parser.add_argument("--root", type=str, default=os.getcwd(), help="Root directory to scan")
    parser.add_argument("--output-json", type=str, default=None, help="Path to write JSON report")
    parser.add_argument("--output-md", type=str, default=None, help="Path to write Markdown summary")
    parser.add_argument("--output-dot", type=str, default=None, help="Path to write Graphviz DOT of imports")
    parser.add_argument("--follow-symlinks", action="store_true", help="Follow symlinks during traversal")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"error: root not a directory: {root}", file=sys.stderr)
        return 2

    modules: List[Dict[str, Any]] = []
    num_classes = 0
    num_functions = 0

    for dirpath, dirnames, filenames in os.walk(root, followlinks=args.follow_symlinks):
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        for fname in filenames:
            if not is_python_file(fname):
                continue
            abs_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(abs_path, root)
            mod = analyze_module(abs_path, rel_path)
            modules.append(mod)
            num_classes += len(mod.get("classes", []))
            num_functions += len(mod.get("functions", []))

    dir_tree = build_dir_tree(root)
    tree_ascii = tree_to_ascii(dir_tree)

    report: Dict[str, Any] = {
        "generated_at": now_iso(),
        "root": root,
        "summary": {
            "num_files": sum(1 for _ in (f for _, _, fs in os.walk(root) for f in fs if is_python_file(f))),
            "num_modules": len(modules),
            "num_classes": num_classes,
            "num_functions": num_functions,
        },
        "modules": modules,
        "tree_ascii": tree_ascii,
    }

    # Import graph
    edges = compute_import_edges(modules)
    report["import_edges"] = edges

    # Output paths defaults
    if args.output_json is None:
        args.output_json = os.path.join(root, "codebase_map.json")
    if args.output_md is None:
        args.output_md = os.path.join(root, "codebase_map.md")

    # Write JSON
    try:
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"wrote JSON: {args.output_json}")
    except Exception as e:
        print(f"error writing JSON: {e}", file=sys.stderr)
        return 3

    # Write Markdown
    try:
        md = generate_markdown(report)
        with open(args.output_md, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"wrote Markdown: {args.output_md}")
    except Exception as e:
        print(f"error writing Markdown: {e}", file=sys.stderr)
        # Continue; JSON is authoritative

    # Write DOT if requested
    if args.output_dot:
        try:
            dot = generate_dot(edges)
            with open(args.output_dot, "w", encoding="utf-8") as f:
                f.write(dot)
            print(f"wrote DOT: {args.output_dot}")
        except Exception as e:
            print(f"error writing DOT: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

