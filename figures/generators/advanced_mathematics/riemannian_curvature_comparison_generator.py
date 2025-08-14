#!/usr/bin/env python3
"""
Riemannian Curvature Comparison Generator (pure mathematics)
Toponogov triangle comparison and Bishop–Gromov volume comparison schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_riemannian_curvature_comparison() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Toponogov triangle comparison (schematic)
    ax1.set_title("Toponogov triangle comparison (schematic)", fontsize=14, weight='bold')
    A = np.array([0, 0])
    B = np.array([2.5, 0.2])
    C = np.array([1.0, 1.6])
    for P, Q in [(A,B), (B,C), (C,A)]:
        ax1.plot([P[0], Q[0]], [P[1], Q[1]], 'k-', lw=2)
    # comparison triangle in model space (Euclidean)
    Bp = np.array([2.5, 0])
    Cp = np.array([1.0, 1.6])
    for P, Q in [(A,Bp), (Bp,Cp), (Cp,A)]:
        ax1.plot([P[0], Q[0]], [P[1], Q[1]], 'r--', lw=2)
    ax1.set_aspect('equal')
    ax1.set_xlim(-0.5, 3.2)
    ax1.set_ylim(-0.2, 2.2)
    ax1.grid(True, alpha=0.3)

    # 2) Bishop–Gromov volume comparison (schematic)
    ax2.set_title("Bishop–Gromov volume comparison (schematic)", fontsize=14, weight='bold')
    r = np.linspace(0.1, 3.0, 200)
    vol_M = r**2 * np.exp(-0.1*r)  # schematic
    vol_mod = r**2  # model space
    ax2.plot(r, vol_M/vol_M[-1], lw=2, label='Vol_M(B_r)/Vol_M(B_R)')
    ax2.plot(r, vol_mod/vol_mod[-1], 'r--', lw=2, label='model')
    ax2.set_xlabel('r')
    ax2.set_ylabel('normalized volume')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Riemannian Curvature Comparison (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/riemannian_curvature_comparison.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "riemannian_curvature_comparison"}


if __name__ == "__main__":
    res = generate_riemannian_curvature_comparison()
    print(f"Generated: {res['file']}")
