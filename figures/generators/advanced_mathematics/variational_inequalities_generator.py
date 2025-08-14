#!/usr/bin/env python3
"""
Variational Inequalities Generator (pure mathematics)
VI(K,F) projection-solver schematic and monotone operator illustration.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_variational_inequalities() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) VI(K,F): find x* ∈ K s.t. ⟨F(x*), y-x*⟩ ≥ 0 ∀y∈K (schematic)
    ax1.set_title(r"VI(K,F) (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 200)
    Kx = 1.2*np.cos(theta)
    Ky = 0.6*np.sin(theta)
    ax1.fill(Kx, Ky, color='#e0f7fa', alpha=0.8, edgecolor='k')
    x_star = np.array([0.3, 0.1])
    ax1.scatter([x_star[0]], [x_star[1]], s=80, c='red')
    ax1.text(x_star[0]+0.05, x_star[1]+0.05, r"x*", color='red')
    # F(x*) arrow
    F = np.array([0.4, 0.2])
    ax1.arrow(x_star[0], x_star[1], F[0], F[1], head_width=0.05, color='purple')
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.2, 1.2)
    ax1.grid(True, alpha=0.3)

    # 2) Monotone operator schematic: ⟨F(x)-F(y), x-y⟩ ≥ 0
    ax2.set_title("Monotone operator (schematic)", fontsize=14, weight='bold')
    xs = np.linspace(-1, 1, 200)
    Fx = xs  # monotone
    ax2.plot(xs, Fx, lw=2)
    ax2.text(0.0, 0.0, r"⟨F(x)-F(y),x-y⟩≥0", fontsize=12)
    ax2.set_xlabel('x')
    ax2.set_ylabel('F(x)')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Variational Inequalities (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/variational_inequalities.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "variational_inequalities"}


if __name__ == "__main__":
    res = generate_variational_inequalities()
    print(f"Generated: {res['file']}")
