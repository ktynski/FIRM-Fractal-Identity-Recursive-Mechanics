#!/usr/bin/env python3
"""
Geometric Measure Theory Generator (pure mathematics)
Hausdorff measure schematic, rectifiable sets, and coarea formula illustration.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_geometric_measure_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Hausdorff measure H^s schematic: cover by balls
    ax1.set_title(r"Hausdorff measure H^s: coverings (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 200)
    curve = np.column_stack([np.cos(theta) + 0.2*np.cos(5*theta), np.sin(theta) + 0.2*np.sin(3*theta)])
    ax1.plot(curve[:,0], curve[:,1], 'k-', lw=2)
    rng = np.random.default_rng(4)
    centers = rng.uniform(-1, 1, size=(30, 2))
    radii = rng.uniform(0.05, 0.2, size=30)
    for c, r in zip(centers, radii):
        circ_t = np.linspace(0, 2*np.pi, 60)
        ax1.plot(c[0] + r*np.cos(circ_t), c[1] + r*np.sin(circ_t), 'b-', alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.8, 1.8)
    ax1.axis('off')

    # 2) Rectifiable set: union of Lipschitz images (schematic)
    ax2.set_title("Rectifiable set (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-1.5, 1.5, 400)
    for shift, col in [(-0.6, 'tomato'), (0.0, 'gold'), (0.6, 'seagreen')]:
        y = 0.3*np.sin(4*x) + shift
        ax2.plot(x, y, color=col, lw=2)
    ax2.set_xlim(-1.8, 1.8)
    ax2.set_ylim(-1.8, 1.8)
    ax2.grid(True, alpha=0.3)

    # 3) Coarea formula illustration: level sets of f
    ax3.set_title("Coarea: ∫|∇f| = ∫ H^{n-1}(f^{-1}(t)) dt (schematic)", fontsize=14, weight='bold')
    X, Y = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-2, 2, 200))
    f = X**2 + (Y - 0.5)**2
    levels = [0.5, 1.0, 1.5, 2.0, 2.5]
    cs = ax3.contour(X, Y, f, levels=levels, colors='k', alpha=0.7)
    ax3.clabel(cs, inline=True, fontsize=8)
    ax3.set_aspect('equal')
    ax3.set_xlim(-2, 2)
    ax3.set_ylim(-2, 2)
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Geometric Measure Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/geometric_measure_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "geometric_measure_theory"}


if __name__ == "__main__":
    res = generate_geometric_measure_theory()
    print(f"Generated: {res['file']}")
