#!/usr/bin/env python3
"""
Random Walks and Poisson Boundary Generator (pure mathematics)
Simple random walk on group and Poisson boundary schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_random_walks_poisson_boundary() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Simple random walk path on ℤ^2 (schematic)
    ax1.set_title("Random walk on ℤ² (schematic)", fontsize=14, weight='bold')
    rng = np.random.default_rng(1)
    steps = rng.integers(low=0, high=4, size=400)
    moves = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}
    pos = np.zeros((401,2), dtype=int)
    for i, s in enumerate(steps, start=1):
        pos[i] = pos[i-1] + moves[int(s)]
    ax1.plot(pos[:,0], pos[:,1], 'k-', lw=1)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)

    # 2) Poisson boundary schematic
    ax2.set_title("Poisson boundary (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 400)
    ax2.plot(np.cos(theta), np.sin(theta), 'k-', lw=2)
    ax2.text(0, 0, 'G', ha='center')
    ax2.text(1.1, 0, '∂P G', ha='left')
    ax2.set_aspect('equal')
    ax2.axis('off')

    fig.suptitle("Random Walks and Poisson Boundary (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/random_walks_poisson_boundary.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "random_walks_poisson_boundary"}


if __name__ == "__main__":
    res = generate_random_walks_poisson_boundary()
    print(f"Generated: {res['file']}")
