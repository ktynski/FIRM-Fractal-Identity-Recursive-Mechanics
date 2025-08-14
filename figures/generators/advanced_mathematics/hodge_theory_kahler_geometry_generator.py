#!/usr/bin/env python3
"""
Hodge Theory and Kähler Geometry Generator (pure mathematics)
Hodge diamond and Lefschetz decomposition schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_hodge_theory_kahler_geometry() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Hodge diamond for a K3 surface (example values)
    ax1.set_title("Hodge Diamond (K3 example)", fontsize=14, weight='bold')
    # rows of diamond
    rows = [[1], [0,0], [1,20,1], [0,0], [1]]
    y = 4
    for r, row in enumerate(rows):
        x0 = (4 - len(row)) / 2
        for i, val in enumerate(row):
            ax1.text(x0 + i, y - r, str(val), ha='center', va='center', fontsize=14, bbox=dict(boxstyle='round', fc='#eef'))
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-0.5, 4.5)
    ax1.axis('off')

    # 2) Hard Lefschetz schematic
    ax2.set_title("Hard Lefschetz (schematic)", fontsize=14, weight='bold')
    degrees = np.arange(0, 5)
    dims = [1, 0, 22, 0, 1]
    ax2.plot(degrees, dims, 'o-', lw=2)
    for d, v in zip(degrees, dims):
        ax2.text(d, v + 0.5, f"H^{d}", ha='center')
    ax2.set_xlabel('degree')
    ax2.set_ylabel('dim H^d')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Hodge Theory and Kähler Geometry (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/hodge_theory_kahler_geometry.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "hodge_theory_kahler_geometry"}


if __name__ == "__main__":
    res = generate_hodge_theory_kahler_geometry()
    print(f"Generated: {res['file']}")
