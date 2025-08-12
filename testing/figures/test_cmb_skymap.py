import os
from pathlib import Path

from figures.cmb_skymap import CMBSkymapGenerator


def test_theory_only_cmb_skymap_generates_png(tmp_path):
    gen = CMBSkymapGenerator(lmax=8, n_lat=48, n_lon=96)
    # Redirect output to temp dir
    gen.output_dir = Path(tmp_path)
    result = gen.generate_skymap()
    out = result.get("file")
    assert out, "No output path returned"
    assert Path(out).exists(), "Skymap PNG not created"
    # File size sanity (non-empty image)
    assert Path(out).stat().st_size > 5_000, "Skymap PNG too small or empty"

