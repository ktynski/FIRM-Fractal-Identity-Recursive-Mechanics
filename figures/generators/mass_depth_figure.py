"""
Generate C_n (form factor) vs depth n for selected particles from theory.

Outputs:
  - arxiv_paper/FIRM_FINAL_SUBMISSION/figures/mass_depth_cn.png
  - CSV: figures/outputs/mass_depth_cn.csv
"""

from __future__ import annotations

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from structures.morphic_knot_projection import derive_recursive_depth_and_form_factor


DEFAULT_PARTICLES = (
    "electron", "muon", "tau", "up", "down", "charm", "strange", "bottom", "top", "proton", "neutron",
)


def generate_mass_depth_cn(
    particles = DEFAULT_PARTICLES,
    out_png: Path | None = None,
    out_csv: Path | None = None,
) -> tuple[Path, Path]:
    rows = []
    for name in particles:
        try:
            d = derive_recursive_depth_and_form_factor(name)
            rows.append((name, d.recursive_depth_n, d.form_factor_Cn, d.mass_ratio_to_electron))
        except Exception:
            continue

    # Save CSV
    if out_csv is None:
        out_csv = Path("figures/outputs/mass_depth_cn.csv")
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["particle", "depth_n", "C_n", "m_over_me"])
        w.writerows(rows)

    # Plot
    names = [r[0] for r in rows]
    nvals = np.array([r[1] for r in rows], dtype=float)
    cvals = np.array([r[2] for r in rows], dtype=float)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.scatter(nvals, cvals, s=40)
    for x, y, label in zip(nvals, cvals, names):
        ax.annotate(label, (x, y), textcoords="offset points", xytext=(4, 2), fontsize=8)
    ax.set_xlabel("recursive depth n ≈ round(log_φ(m/me))")
    ax.set_ylabel("form factor C_n")
    ax.set_title("Morphic-knot mass projection: C_n vs depth")
    ax.grid(True, alpha=0.3)

    if out_png is None:
        out_png = Path("arxiv_paper/FIRM_FINAL_SUBMISSION/figures/mass_depth_cn.png")
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=200)
    plt.close(fig)
    return out_png, out_csv


if __name__ == "__main__":
    p_png, p_csv = generate_mass_depth_cn()
    print(str(p_png))
    print(str(p_csv))

