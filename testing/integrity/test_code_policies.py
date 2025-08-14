import json
import os
import re
import subprocess
import sys
from pathlib import Path


def run_codebase_mapper(tmp_json: Path) -> dict:
    # Repo root is two levels up from this test file (testing/integrity/..)
    repo_root = Path(__file__).resolve().parents[2]
    mapper = repo_root / "utils" / "codebase_mapper.py"
    cmd = [sys.executable, str(mapper), "--root", str(repo_root), "--output-json", str(tmp_json)]
    subprocess.run(cmd, check=True, capture_output=True)
    with open(tmp_json, "r", encoding="utf-8") as f:
        return json.load(f)


def is_public_name(name: str) -> bool:
    if not isinstance(name, str):
        return False
    if name.startswith("test_"):
        return False
    if name.startswith("_"):
        return False
    if name.startswith("__") and name.endswith("__"):
        return False
    return True


def keep_module(mod: str) -> bool:
    return not (mod.startswith("testing/"))


def test_public_docstring_policy(tmp_path: Path) -> None:
    """Non-regression policy: no new missing public docstrings beyond baseline.

    Baseline is taken from codebase_missing_docstrings_public.json if present.
    The test fails only if current missing set minus baseline is non-empty.
    """
    report = run_codebase_mapper(tmp_path / "codebase_map.json")
    modules = report.get("modules", [])

    current_missing = {"functions": set(), "classes": set(), "methods": set()}

    for m in modules:
        mod_path = m.get("path", "")
        if not keep_module(mod_path):
            continue
        for fn in m.get("functions", []):
            if is_public_name(fn.get("name", "")) and not fn.get("docstring"):
                current_missing["functions"].add((mod_path, fn.get("name")))
        for cls in m.get("classes", []):
            if is_public_name(cls.get("name", "")) and not cls.get("docstring"):
                current_missing["classes"].add((mod_path, cls.get("name")))
            for meth in cls.get("methods", []):
                if is_public_name(meth.get("name", "")) and not meth.get("docstring"):
                    current_missing["methods"].add((mod_path, f"{cls.get('name')}::{meth.get('name')}"))

    # Load baseline if available
    repo_root = Path(__file__).resolve().parents[2]
    baseline_path = repo_root / "codebase_missing_docstrings_public.json"
    baseline_missing = {"functions": set(), "classes": set(), "methods": set()}
    if baseline_path.exists():
        with open(baseline_path, "r", encoding="utf-8") as f:
            baseline = json.load(f)
        for k in ("functions", "classes", "methods"):
            for item in baseline.get(k, []):
                if k == "methods":
                    baseline_missing[k].add((item["module"], f"{item['class']}::{item['name']}"))
                else:
                    baseline_missing[k].add((item["module"], item["name"]))

    regressions = []
    for k in ("functions", "classes", "methods"):
        new_missing = current_missing[k] - baseline_missing[k]
        for mod, name in sorted(new_missing)[:20]:
            regressions.append(f"{k}: {mod} :: {name}")

    if regressions:
        raise AssertionError(
            "New missing public docstrings detected (beyond baseline):\n" + "\n".join(regressions)
        )


def _looks_like_number(s: str) -> bool:
    return bool(re.match(r"^-?\d*\.?\d+([eE][+-]?\d+)?$", s or ""))


def test_no_hardcoded_constants_outside_centralized_module(tmp_path: Path) -> None:
    """Non-regression policy: no new module-level numeric constants beyond baseline.

    Baseline is taken from hardcoded_constants_analysis.json if present.
    The test fails only if new occurrences appear beyond baseline.
    """
    report = run_codebase_mapper(tmp_path / "codebase_map.json")
    modules = report.get("modules", [])

    current = set()
    for m in modules:
        mod = m.get("path", "")
        if not keep_module(mod):
            continue
        if mod == "foundation/derived.py":
            continue
        for var in m.get("variables", {}).get("module_variables", []):
            name = var.get("name")
            value = var.get("value")
            if value is None:
                continue
            if _looks_like_number(str(value)):
                try:
                    f = float(value)
                except Exception:
                    continue
                allowed = {0.0, 1.0, 2.0, 0.5, 1e-12, 1e-15}
                if f in allowed:
                    continue
                current.add((mod, name, str(value)))

    # Load baseline if exists
    repo_root = Path(__file__).resolve().parents[2]
    baseline_path = repo_root / "hardcoded_constants_analysis.json"
    baseline = set()
    if baseline_path.exists():
        with open(baseline_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for it in data.get("all_constants", []):
            baseline.add((it.get("module", ""), it.get("variable", ""), str(it.get("value", ""))))

    regressions = sorted(current - baseline)[:20]
    if regressions:
        sample = "\n".join(f"{mod} :: {name} = {val}" for mod, name, val in regressions)
        raise AssertionError(
            "New hardcoded numeric constants found outside foundation/derived.py (beyond baseline):\n" + sample
        )
