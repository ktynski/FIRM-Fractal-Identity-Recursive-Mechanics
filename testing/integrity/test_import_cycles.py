import json
import subprocess
import sys
from collections import defaultdict, deque
from pathlib import Path


def run_codebase_mapper(tmp_json: Path) -> dict:
    repo_root = Path(__file__).resolve().parents[2]
    mapper = repo_root / "utils" / "codebase_mapper.py"
    cmd = [sys.executable, str(mapper), "--root", str(repo_root), "--output-json", str(tmp_json)]
    subprocess.run(cmd, check=True, capture_output=True)
    with open(tmp_json, "r", encoding="utf-8") as f:
        return json.load(f)


def keep_module(mod: str) -> bool:
    # Ignore tests themselves
    return not (mod.startswith("testing/"))


def path_to_dotted(rel_path: str) -> str:
    if rel_path.endswith("/__init__.py"):
        return rel_path[: -len("/__init__.py")].replace("/", ".")
    if rel_path.endswith(".py"):
        return rel_path[: -3].replace("/", ".")
    return rel_path.replace("/", ".")


def resolve_relative(current_mod: str, target: str) -> str:
    # target like '..x.y' or '.z'; current_mod like 'a.b.c'
    if not target or target[0] != '.':
        return target
    # count leading dots
    i = 0
    while i < len(target) and target[i] == '.':
        i += 1
    levels_up = i
    remainder = target[i:]
    parts = current_mod.split('.')
    if levels_up > len(parts):
        # too many ups; fallback to remainder only
        base = []
    else:
        base = parts[: len(parts) - levels_up]
    return ".".join([*base, remainder] if remainder else base)


def build_graph(modules):
    dotted_to_path = {}
    for m in modules:
        p = m.get("path", "")
        dotted_to_path[path_to_dotted(p)] = p

    graph = defaultdict(set)
    for m in modules:
        src_path = m.get("path", "")
        if not keep_module(src_path):
            continue
        src_dotted = path_to_dotted(src_path)
        # direct imports
        for imp in m.get("imports", {}).get("imports", []):
            target = imp.split(" as ")[0].strip()
            if target in dotted_to_path:
                graph[src_path].add(dotted_to_path[target])
        # from-imports (absolute or relative)
        for frm in m.get("imports", {}).get("from_imports", []):
            mod = frm.get("module", "")
            if not mod:
                continue
            target = resolve_relative(src_dotted, mod)
            if target in dotted_to_path:
                graph[src_path].add(dotted_to_path[target])
    return graph


def find_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node, path):
        visited.add(node)
        stack.add(node)
        for nei in graph.get(node, set()):
            if nei not in visited:
                cyc = dfs(nei, path + [nei])
                if cyc:
                    return cyc
            elif nei in stack:
                # Found a back edge; reconstruct a simple cycle
                if nei in path:
                    i = path.index(nei)
                    return path[i:] + [nei]
                return [nei, node, nei]
        stack.remove(node)
        return None

    for n in list(graph.keys()):
        if n not in visited:
            cyc = dfs(n, [n])
            if cyc:
                return cyc
    return None


def test_no_import_cycles(tmp_path: Path) -> None:
    report = run_codebase_mapper(tmp_path / "codebase_map.json")
    modules = report.get("modules", [])
    graph = build_graph(modules)
    cycle = find_cycle(graph)
    if cycle:
        # Whitelist known acceptable cycles pending refactor
        allowed_nodes = {
            "provenance/provenance_tracker.py",
            "utils/precision_framework.py",
            "utils/implementation_loop.py",
        }
        if set(cycle).issubset(allowed_nodes):
            return
        raise AssertionError("Import cycle detected: " + " -> ".join(cycle))

