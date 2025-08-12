import json
import subprocess
import sys
from pathlib import Path


def test_codebase_mapper_cli_smoke(tmp_path: Path):
    repo_root = Path(__file__).resolve().parents[2]
    mapper = repo_root / "utils" / "codebase_mapper.py"
    out = tmp_path / "map.json"
    cmd = [sys.executable, str(mapper), "--root", str(repo_root), "--output-json", str(out)]
    subprocess.run(cmd, check=True, capture_output=True)
    data = json.loads(out.read_text())
    assert isinstance(data, dict)
    assert "modules" in data and isinstance(data["modules"], list)
