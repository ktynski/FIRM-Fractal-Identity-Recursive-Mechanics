#!/usr/bin/env python3
"""
Amenability and Følner Sets Generator (pure mathematics)
Følner sets in groups and boundary/volume ratio schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_amenability_folner() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Følner sets in Z^2 lattice
    ax1.set_title("Følner sets in ℤ² (schematic)", fontsize=14, weight='bold')
    xs = np.arange(-6, 7)
    ys = np.arange(-6, 7)
    for x in xs:
        ax1.plot([x, x], [ys.min(), ys.max()], 'k-', alpha=0.1)
    for y in ys:
        ax1.plot([xs.min(), xs.max()], [y, y], 'k-', alpha=0.1)
    # square Følner sets
    for r, col in [(2, 'gold'), (4, 'tomato')]:
        ax1.add_patch(plt.Rectangle((-r, -r), 2*r, 2*r, fill=True, alpha=0.3, color=col, ec='k'))
    ax1.set_aspect('equal')
    ax1.set_xlim(-7, 7)
    ax1.set_ylim(-7, 7)
    ax1.grid(False)

    # 2) Boundary/volume ratio vs size
    ax2.set_title("Boundary/volume ratio (schematic)", fontsize=14, weight='bold')
    R = np.arange(1, 20)
    ratio = (8*R) / ((2*R)**2)
    ax2.plot(R, ratio, 'o-', lw=2)
    ax2.set_xlabel('size R')
    ax2.set_ylabel('|∂F_R|/|F_R|')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Amenability and Følner Sets (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/amenability_folner.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "amenability_folner"}


if __name__ == "__main__":
    res = generate_amenability_folner()
    print(f"Generated: {res['file']}")
