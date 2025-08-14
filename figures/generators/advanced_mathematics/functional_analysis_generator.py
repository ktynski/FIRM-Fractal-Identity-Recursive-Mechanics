#!/usr/bin/env python3
"""
Functional Analysis Generator (pure mathematics)
Banach unit balls and Hahn–Banach separation schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_functional_analysis() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Unit balls in ℓ^p for p=1,2,∞ (2D sections)
    ax1.set_title("Unit balls in ℓ^p (2D)", fontsize=14, weight='bold')
    t = np.linspace(0, 2*np.pi, 400)
    # p=2 circle
    x2, y2 = np.cos(t), np.sin(t)
    ax1.plot(x2, y2, 'b-', label='p=2')
    # p=1 diamond
    x1 = np.sign(np.cos(t)) * (np.abs(np.cos(t)))
    y1 = np.sign(np.sin(t)) * (1 - np.abs(x1))
    ax1.plot(x1, y1, 'g-', label='p=1')
    # p=∞ square
    ax1.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], 'r-', label='p=∞')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) Normed space linear functionals (level sets)
    ax2.set_title("Linear functionals level sets", fontsize=14, weight='bold')
    x = np.linspace(-1.5, 1.5, 200)
    y = np.linspace(-1.5, 1.5, 200)
    X, Y = np.meshgrid(x, y)
    f = X + 0.5*Y
    cs = ax2.contour(X, Y, f, levels=np.linspace(-2, 2, 11), cmap='viridis')
    ax2.clabel(cs, inline=True, fontsize=8)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)

    # 3) Hahn–Banach separation schematic
    ax3.set_title("Hahn–Banach separation (schematic)", fontsize=14, weight='bold')
    cloud = np.random.default_rng(1).normal(size=(100, 2)) * [0.6, 0.2] + [0.0, -0.4]
    ax3.scatter(cloud[:,0], cloud[:,1], s=20, alpha=0.6)
    # separating line y = 0.3x
    xv = np.linspace(-1.5, 1.5, 50)
    ax3.plot(xv, 0.3*xv, 'k--', lw=2)
    ax3.text(1.0, 0.3*1.0+0.05, '⟨f,·⟩=c', fontsize=10)
    ax3.set_aspect('equal')
    ax3.set_xlim(-1.8, 1.8)
    ax3.set_ylim(-1.5, 1.5)
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Functional Analysis (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/functional_analysis.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "functional_analysis"}


if __name__ == "__main__":
    res = generate_functional_analysis()
    print(f"Generated: {res['file']}")
