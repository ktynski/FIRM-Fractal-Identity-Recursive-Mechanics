#!/usr/bin/env python3
"""
Percolation Critical Probability Generator (pure mathematics)
Bond percolation on ℤ² schematic and cluster size vs p.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_percolation_critical_probability() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Bond percolation on ℤ² with p
    ax1.set_title("Bond percolation on ℤ² (schematic)", fontsize=14, weight='bold')
    rng = np.random.default_rng(0)
    grid = 6
    p = 0.45
    for i in range(grid+1):
        ax1.plot([0, grid], [i, i], 'k-', alpha=0.2)
        ax1.plot([i, i], [0, grid], 'k-', alpha=0.2)
    for i in range(grid):
        for j in range(grid+1):
            if rng.random() < p:
                ax1.plot([i, i+1], [j, j], 'b-', lw=2)
    for i in range(grid+1):
        for j in range(grid):
            if rng.random() < p:
                ax1.plot([i, i], [j, j+1], 'b-', lw=2)
    ax1.set_aspect('equal')
    ax1.set_xlim(0, grid)
    ax1.set_ylim(0, grid)
    ax1.axis('off')

    # 2) Cluster size vs p (schematic phase transition near p_c≈0.5)
    ax2.set_title("Cluster size vs p (schematic)", fontsize=14, weight='bold')
    pvals = np.linspace(0.3, 0.7, 50)
    size = 1/(0.51 - pvals + 1e-3)
    size[pvals<0.51] = 1/(0.51 - pvals[pvals<0.51] + 1e-3)
    size[pvals>=0.51] = 50  # diverging schematic
    ax2.plot(pvals, size, 'o-', lw=2)
    ax2.axvline(0.5, color='r', linestyle='--', label='p_c~0.5 (schematic)')
    ax2.set_xlabel('p')
    ax2.set_ylabel('expected cluster size')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Percolation Critical Probability (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/percolation_critical_probability.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "percolation_critical_probability"}


if __name__ == "__main__":
    res = generate_percolation_critical_probability()
    print(f"Generated: {res['file']}")
