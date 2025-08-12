import os
import json
import tempfile

from utils import codebase_mapper as cbm


def test_generate_markdown_and_dot_and_cli_defaults(tmp_path):
    # Create a tiny temp tree with a python file
    root = tmp_path / "proj"
    root.mkdir()
    py = root / "a.py"
    py.write_text("""\n\nimport math\n\nclass A:\n    def f(self):\n        return 1\n\n""")

    # Run main against the temp root with outputs in temp dir
    json_path = root / "out.json"
    md_path = root / "out.md"
    dot_path = root / "out.dot"
    rc = cbm.main([
        "--root", str(root),
        "--output-json", str(json_path),
        "--output-md", str(md_path),
        "--output-dot", str(dot_path),
    ])
    assert rc == 0
    assert json_path.exists() and md_path.exists() and dot_path.exists()

    # Validate JSON shape
    data = json.loads(json_path.read_text())
    assert set(["generated_at", "root", "summary", "modules", "tree_ascii", "import_edges"]).issubset(data.keys())
    md = md_path.read_text()
    assert "# Codebase Map" in md and "## Modules" in md
    dot = dot_path.read_text()
    assert "digraph imports" in dot

