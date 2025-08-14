#!/usr/bin/env python3
"""
o-minimality Generator (pure mathematics)
Definable sets in ℝ and cell decomposition schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_o_minimality() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Definable subsets of ℝ: finite unions of points and intervals
    ax1.set_title("Definable sets in ℝ (o-minimal)", fontsize=14, weight='bold')
    ax1.set_xlim(-2, 8)
    ax1.set_ylim(-1, 1)
    ax1.get_yaxis().set_visible(False)
    # intervals
    ax1.hlines(0.3, 0, 2, colors='steelblue', lw=6)
    ax1.hlines(0.3, 3, 5, colors='steelblue', lw=6)
    # points
    for p in [0, 1.5, 2.0, 3.0, 5.0, 6.5]:
        ax1.plot(p, -0.3, 'o', color='tomato')
    ax1.grid(True, axis='x', alpha=0.3)

    # 2) Definable subsets of ℝ² (finite unions of cells)
    ax2.set_title("Definable sets in ℝ² (cells)", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 200)
    y1 = np.sin(x)
    y2 = np.sin(x) + 1.0
    ax2.fill_between(x, y1, y2, color='lightgreen', alpha=0.7, label='cell')
    ax2.plot(x, y1, 'k-')
    ax2.plot(x, y2, 'k-')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # 3) Cell decomposition schematic
    ax3.set_title("Cell decomposition (schematic)", fontsize=14, weight='bold')
    for vx in [-1.5, -0.5, 0.5, 1.5]:
        ax3.axvline(vx, color='#ccc')
    for vy in [-1.0, 0.0, 1.0]:
        ax3.axhline(vy, color='#eee')
    # highlight some cells
    rects = [(-1.5, -1.0, 1.0, 1.0), (0.5, 0.0, 1.0, 1.0), (-0.5, 0.0, 1.0, 1.0)]
    for (x0, y0, w, h) in rects:
        ax3.add_patch(plt.Rectangle((x0, y0), w, h, fill=True, alpha=0.3, color='gold', ec='k'))
    ax3.set_xlim(-2, 2)
    ax3.set_ylim(-1.5, 1.5)
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.grid(False)

    fig.suptitle("o-minimality (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/o_minimality.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "o_minimality"}


if __name__ == "__main__":
    res = generate_o_minimality()
    print(f"Generated: {res['file']}")
