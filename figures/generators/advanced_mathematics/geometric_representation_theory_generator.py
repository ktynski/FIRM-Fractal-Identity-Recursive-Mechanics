#!/usr/bin/env python3
"""
Geometric Representation Theory Generator (pure mathematics)
Generates visualizations for flag variety cells, perverse sheaves, and character data.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_geometric_representation_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Flag variety (Bruhat cells for SL(3)): draw a small grid with highlighted cells
    ax1.set_title("Flag Variety (SL(3)): Bruhat Cells", fontsize=14, weight="bold")
    n = 3
    grid = np.zeros((n, n))
    # highlight a pattern representing closure relations (schematic)
    grid[0, 0] = 3
    grid[0, 1] = 2
    grid[1, 0] = 2
    grid[1, 1] = 1
    im = ax1.imshow(grid, cmap="YlGnBu", origin="lower")
    for i in range(n):
        for j in range(n):
            ax1.text(j, i, f"w{i}{j}", ha="center", va="center", fontsize=10)
    plt.colorbar(im, ax=ax1, fraction=0.046, pad=0.04, label="cell dimension (schematic)")
    ax1.set_xticks(range(n))
    ax1.set_yticks(range(n))
    ax1.set_xlabel("column")
    ax1.set_ylabel("row")

    # 2) Perverse sheaves: simple objects dimensions (schematic bar chart)
    ax2.set_title("Perverse Sheaves on Flag Variety (schematic dims)", fontsize=14, weight="bold")
    simples = ["IC(w00)", "IC(w01)", "IC(w10)", "IC(w11)"]
    dims = [5, 3, 3, 2]
    ax2.bar(np.arange(len(simples)) - 0.15, dims, width=0.3, label="dim H^*", color="steelblue")
    ax2.bar(np.arange(len(simples)) + 0.15, [d//2+1 for d in dims], width=0.3, label="support rank", color="tomato")
    for i, d in enumerate(dims):
        ax2.text(i-0.15, d+0.1, str(d), ha="center", va="bottom", fontweight="bold")
    ax2.set_xticks(range(len(simples)))
    ax2.set_xticklabels(simples, rotation=20)
    ax2.set_ylabel("value")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # 3) Characters on a compact torus (weight lattice sampling)
    ax3.set_title("Characters on a Torus: χ_λ(e^{iθ})", fontsize=14, weight="bold")
    theta = np.linspace(0, 2*np.pi, 400)
    weights = [1, 2, 3]
    for w in weights:
        chi = np.cos(w * theta)  # schematic character
        ax3.plot(theta, chi, label=f"λ={w}")
    ax3.set_xlabel("θ")
    ax3.set_ylabel("χ_λ")
    ax3.set_xlim(0, 2*np.pi)
    ax3.grid(True, alpha=0.3)
    ax3.legend()

    # 4) D-modules functor diagram (schematic arrows)
    ax4.set_title("D-Modules (schematic): pushforward/pullback functors", fontsize=14, weight="bold")
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 6)
    ax4.axis("off")
    pts = [(2, 4, "(X, D_X)"), (8, 4, "(Y, D_Y)"), (5, 1.5, "f: X→Y")]
    for x, y, label in pts:
        ax4.text(x, y, label, ha="center", va="center", bbox=dict(boxstyle="round", fc="#f0f0f0"))
    # arrows for f_*, f^!, f^*, f_!
    ax4.annotate("", xy=(7.5, 4), xytext=(2.5, 4), arrowprops=dict(arrowstyle="->", lw=2, color="blue"))
    ax4.text(5, 4.3, r"f_*", ha="center", va="bottom", color="blue", fontweight="bold")
    ax4.annotate("", xy=(2.5, 3.7), xytext=(7.5, 3.7), arrowprops=dict(arrowstyle="->", lw=2, color="crimson"))
    ax4.text(5, 3.4, r"f^*", ha="center", va="top", color="crimson", fontweight="bold")
    ax4.annotate("", xy=(7.2, 3.5), xytext=(5, 1.8), arrowprops=dict(arrowstyle="->", lw=2, color="green"))
    ax4.text(6.2, 2.7, r"f_!", ha="center", va="center", color="green", fontweight="bold")
    ax4.annotate("", xy=(2.8, 3.5), xytext=(5, 1.8), arrowprops=dict(arrowstyle="->", lw=2, color="purple"))
    ax4.text(3.8, 2.7, r"f^!", ha="center", va="center", color="purple", fontweight="bold")

    fig.suptitle("Geometric Representation Theory (pure mathematics)", fontsize=16, weight="bold")
    plt.tight_layout()
    out = Path("figures/outputs/geometric_representation_theory.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "geometric_representation_theory"}


if __name__ == "__main__":
    res = generate_geometric_representation_theory()
    print(f"Generated: {res['file']}")
