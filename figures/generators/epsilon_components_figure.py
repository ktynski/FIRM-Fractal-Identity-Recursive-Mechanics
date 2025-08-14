"""
Generate multi-panel ε-stability figure: S(ε), δκ(ε), δG(ε), δC(ε).

Outputs:
  - arxiv_paper/FIRM_FINAL_SUBMISSION/figures/epsilon_components_scan.png

Theory-only (no empirical inputs).
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
try:
    from validation.epsilon_stability import S_epsilon
except ImportError:
    # Fallback epsilon stability function
    def S_epsilon(epsilon_components):
        return sum(abs(c) for c in epsilon_components)


def generate_epsilon_components_scan(
    eps_min: float = -2.0,
    eps_max: float = 1.0,
    step: float = 0.005,
    out_path: Path | None = None,
) -> Path:
    E = np.arange(eps_min, eps_max + 1e-12, step, dtype=float)
    S_vals, dk_vals, dg_vals, dc_vals = [], [], [], []
    for e in E:
        comp = S_epsilon(float(e))
        S_vals.append(comp["S"]) ; dk_vals.append(comp["delta_kappa"]) ; dg_vals.append(comp["delta_G"]) ; dc_vals.append(comp["delta_C"]) \

    S_vals = np.asarray(S_vals, dtype=float)
    dk_vals = np.asarray(dk_vals, dtype=float)
    dg_vals = np.asarray(dg_vals, dtype=float)
    dc_vals = np.asarray(dc_vals, dtype=float)

    fig, axs = plt.subplots(2, 2, figsize=(10, 6), constrained_layout=True)
    ax = axs[0, 0]
    ax.plot(E, S_vals, lw=1.0)
    ax.set_title("S(ε)") ; ax.set_xlabel("ε") ; ax.set_ylabel("S")
    ax.grid(True, alpha=0.3)

    ax = axs[0, 1]
    ax.plot(E, dk_vals, lw=1.0, color="#1f77b4")
    ax.set_title("δκ(ε)") ; ax.set_xlabel("ε") ; ax.set_ylabel("δκ")
    ax.grid(True, alpha=0.3)

    ax = axs[1, 0]
    ax.plot(E, dg_vals, lw=1.0, color="#d62728")
    ax.set_title("δG(ε)") ; ax.set_xlabel("ε") ; ax.set_ylabel("δG")
    ax.grid(True, alpha=0.3)

    ax = axs[1, 1]
    ax.plot(E, dc_vals, lw=1.0, color="#2ca02c")
    ax.set_title("δC(ε)") ; ax.set_xlabel("ε") ; ax.set_ylabel("δC")
    ax.grid(True, alpha=0.3)

    if out_path is None:
        out_path = Path("arxiv_paper/FIRM_FINAL_SUBMISSION/figures/epsilon_components_scan.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    p = generate_epsilon_components_scan()
    print(str(p))

