"""
Generate potential wells V(φ, G) slices for various recursion depths d.

Outputs:
  - arxiv_paper/FIRM_FINAL_SUBMISSION/figures/recursive_potential_wells.png
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from theory.fsctf_lagrangian import FSCTFParams, V_recursive


def generate_recursive_potential_wells(
    phi_min: float = -2.5,
    phi_max: float = 2.5,
    n: int = 600,
    G_val: float = 1.0,
    depths = (2.0, 3.0, 4.0),
    out_path: Path | None = None,
) -> Path:
    xs = np.linspace(phi_min, phi_max, n)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    for d in depths:
        params = FSCTFParams(depth_d=d, R_max=10)
        V = np.array([V_recursive(x, G_val, params) for x in xs], dtype=float)
        ax.plot(xs, V, lw=1.2, label=f"d={d}")
    ax.axhline(0.0, color="#999", lw=0.6)
    ax.set_xlabel("φ")
    ax.set_ylabel("V(φ, G)")
    ax.set_title("Recursive potential wells for various depths d")
    ax.grid(True, alpha=0.3)
    ax.legend(frameon=False)
    if out_path is None:
        out_path = Path("arxiv_paper/FIRM_FINAL_SUBMISSION/figures/recursive_potential_wells.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    p = generate_recursive_potential_wells()
    print(str(p))


