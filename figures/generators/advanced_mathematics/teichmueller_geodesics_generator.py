#!/usr/bin/env python3
"""
Teichmüller Geodesics Generator (pure mathematics)
Stretch maps schematic and quadratic differential trajectories.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_teichmueller_geodesics() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Stretch map schematic on unit square
    ax1.set_title("Teichmüller stretch maps (schematic)", fontsize=14, weight='bold')
    # original grid
    for x in np.linspace(0, 1, 6):
        ax1.plot([x, x], [0, 1], 'k-', alpha=0.3)
    for y in np.linspace(0, 1, 6):
        ax1.plot([0, 1], [y, y], 'k-', alpha=0.3)
    # stretched grid
    k = 1.8
    for x in np.linspace(0, 1, 6):
        ax1.plot([1.1 + k*(x-0.5), 1.1 + k*(x-0.5)], [0, 1], 'r-', alpha=0.6)
    for y in np.linspace(0, 1, 6):
        ax1.plot([1.1 - 0.5, 1.1 + 0.5], [y, y], 'r-', alpha=0.6)
    ax1.set_aspect('equal')
    ax1.set_xlim(-0.2, 2.0)
    ax1.set_ylim(-0.1, 1.1)
    ax1.axis('off')

    # 2) Quadratic differential horizontal trajectories (schematic)
    ax2.set_title("Quadratic differential trajectories", fontsize=14, weight='bold')
    t = np.linspace(0, 2*np.pi, 400)
    for a in [0.6, 0.8, 1.0]:
        ax2.plot(a*np.cos(t), a*np.sin(t), lw=2)
    ax2.set_aspect('equal')
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.2, 1.2)
    ax2.axis('off')

    fig.suptitle("Teichmüller Geodesics (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/teichmueller_geodesics.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "teichmueller_geodesics"}


if __name__ == "__main__":
    res = generate_teichmueller_geodesics()
    print(f"Generated: {res['file']}")
