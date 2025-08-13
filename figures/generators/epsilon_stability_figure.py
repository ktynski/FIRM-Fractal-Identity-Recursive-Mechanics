"""
Generate ε-stability scan figure from theory-only S(ε).

Outputs:
  - arxiv_paper/FIRM_FINAL_SUBMISSION/figures/epsilon_stability_scan.png

No empirical inputs are used.
"""

from __future__ import annotations

import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from validation.epsilon_stability import S_epsilon


def generate_epsilon_stability_scan(
    eps_min: float = -2.0,
    eps_max: float = 0.0,
    step: float = 0.002,
    out_path: Path | None = None,
) -> Path:
    E = np.arange(eps_min, eps_max + 1e-12, step, dtype=float)
    Svals = []
    for e in E:
        d = S_epsilon(float(e))
        Svals.append(d["S"])
    Svals = np.asarray(Svals, dtype=float)

    if out_path is None:
        out_path = Path("arxiv_paper/FIRM_FINAL_SUBMISSION/figures/epsilon_stability_scan.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8.0, 3.5))
    plt.plot(E, Svals, "-", lw=1.2, color="#1f77b4")
    plt.xlabel(r"$\varepsilon$")
    plt.ylabel(r"$S(\varepsilon)$")
    plt.title("Theory-only ε-stability landscape: S(ε)")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()
    return out_path


if __name__ == "__main__":
    p = generate_epsilon_stability_scan()
    print(f"Saved: {p}")


