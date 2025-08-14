#!/usr/bin/env python3
"""
Calculus of Variations Generator (pure mathematics)
Euler–Lagrange comparison of paths and minimal energy curve (schematic).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_calculus_of_variations() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Compare two paths between endpoints and their energies
    ax1.set_title("Path energy comparison", fontsize=14, weight='bold')
    x = np.linspace(0, 1, 200)
    y1 = x  # straight line
    y2 = x + 0.2*np.sin(2*np.pi*x)
    ax1.plot(x, y1, 'k-', lw=2, label='γ₁: straight')
    ax1.plot(x, y2, 'r--', lw=2, label='γ₂: wavy')
    # energy proxy E = ∫ (1 + |y'|^2) dx
    E1 = np.trapz(1 + np.gradient(y1, x)**2, x)
    E2 = np.trapz(1 + np.gradient(y2, x)**2, x)
    ax1.text(0.05, 0.9, f"E(γ₁)≈{E1:.3f}\nE(γ₂)≈{E2:.3f}", transform=ax1.transAxes,
             bbox=dict(boxstyle='round', fc='#ffd'))
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) Euler–Lagrange minimal curve for L = (1/2)|y'|² with fixed endpoints is straight line
    ax2.set_title("Euler–Lagrange minimal curve (schematic)", fontsize=14, weight='bold')
    ax2.plot(x, y1, 'k-', lw=2)
    ax2.scatter([0,1], [0,1], s=60, c='blue')
    ax2.text(0, 0, 'A', ha='right', va='top')
    ax2.text(1, 1, 'B', ha='left', va='bottom')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Calculus of Variations (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/calculus_of_variations.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "calculus_of_variations"}


if __name__ == "__main__":
    res = generate_calculus_of_variations()
    print(f"Generated: {res['file']}")
