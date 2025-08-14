import json
import subprocess
import sys
from collections import Counter, defaultdict
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


def test_no_duplicate_definitions(tmp_path: Path) -> None:
    """Fail if any module defines the same function or class name more than once."""
    report = run_codebase_mapper(tmp_path / "codebase_map.json")
    modules = report.get("modules", [])

    duplicates = []
    for m in modules:
        mod_path = m.get("path", "")
        if not keep_module(mod_path):
            continue

        fn_names = [fn.get("name") for fn in m.get("functions", []) if fn.get("name")]
        cls_names = [cls.get("name") for cls in m.get("classes", []) if cls.get("name")]

        fn_counts = Counter(fn_names)
        cls_counts = Counter(cls_names)

        for name, count in fn_counts.items():
            if count > 1:
                duplicates.append((mod_path, "function", name, count))
        for name, count in cls_counts.items():
            if count > 1:
                duplicates.append((mod_path, "class", name, count))

    if duplicates:
        sample = "\n".join(f"{mod} :: {kind} {name!r} defined {count} times" for mod, kind, name, count in duplicates[:20])
        raise AssertionError("Duplicate symbol definitions detected:\n" + sample)
