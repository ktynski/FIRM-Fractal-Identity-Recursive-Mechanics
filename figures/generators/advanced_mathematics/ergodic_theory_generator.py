#!/usr/bin/env python3
"""
Ergodic Theory Generator (pure mathematics)
Measure-preserving maps, mixing schematic, and correlation decay.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_ergodic_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Measure-preserving map on unit square: (x,y) -> (x+y mod 1, x)
    ax1.set_title("Measure-Preserving Map (Arnold cat-like, schematic)", fontsize=14, weight='bold')
    rng = np.random.default_rng(0)
    pts = rng.random((1000, 2))
    for _ in range(3):
        x, y = pts[:,0], pts[:,1]
        pts = np.column_stack((((x + y) % 1.0), x))
    ax1.scatter(pts[:,0], pts[:,1], s=4, alpha=0.5)
    ax1.set_xlim(0,1)
    ax1.set_ylim(0,1)
    ax1.set_aspect('equal')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    # 2) Mixing schematic: overlap of sets under T^n
    ax2.set_title("Mixing: μ(A ∩ T^{-n}B) → μ(A)μ(B)", fontsize=14, weight='bold')
    n = np.arange(0, 40)
    overlap = 0.25 + 0.5*np.exp(-n/10.0)
    ax2.plot(n, overlap, lw=2)
    ax2.axhline(0.25, color='k', linestyle='--', alpha=0.6, label='μ(A)μ(B)')
    ax2.set_xlabel('n')
    ax2.set_ylabel('overlap')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # 3) Correlation decay for observable f
    ax3.set_title("Correlation Decay C_f(n)", fontsize=14, weight='bold')
    n = np.arange(0, 50)
    corr = np.exp(-n/12.0) * np.cos(0.4*n)
    ax3.plot(n, corr, 'o-', lw=2)
    ax3.set_xlabel('n')
    ax3.set_ylabel('C_f(n)')
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Ergodic Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/ergodic_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "ergodic_theory"}


if __name__ == "__main__":
    res = generate_ergodic_theory()
    print(f"Generated: {res['file']}")
