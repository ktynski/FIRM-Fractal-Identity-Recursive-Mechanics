#!/usr/bin/env python3
"""
CAT(0) Geometry Generator (pure mathematics)
Geodesic triangle thinness schematic and convexity properties.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_cat0_geometry() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Triangle thinness (comparison with Euclidean)
    ax1.set_title("CAT(0) triangle thinness (schematic)", fontsize=14, weight='bold')
    A = np.array([0, 0])
    B = np.array([3, 0.3])
    C = np.array([1.2, 2.0])
    for P, Q in [(A,B), (B,C), (C,A)]:
        ax1.plot([P[0], Q[0]], [P[1], Q[1]], 'k-', lw=2)
    # thin geodesic "shortcut" inside triangle
    t = np.linspace(0, 1, 100)
    P1 = A*(1-t)[:,None] + C*t[:,None]
    P2 = A*(1-t)[:,None] + B*t[:,None]
    mid1 = 0.5*(P1 + P2) - np.array([0, 0.1])
    ax1.plot(mid1[:,0], mid1[:,1], 'r--', lw=2, label='thinness')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) Convexity of distance function d(·,·) in CAT(0)
    ax2.set_title("Convexity of distance along geodesics", fontsize=14, weight='bold')
    s = np.linspace(0, 1, 200)
    d = 1 + 0.2*(s-0.5)**2  # convex profile schematic
    ax2.plot(s, d, lw=2)
    ax2.set_xlabel('geodesic parameter s')
    ax2.set_ylabel('distance d')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("CAT(0) Geometry (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/cat0_geometry.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "cat0_geometry"}


if __name__ == "__main__":
    res = generate_cat0_geometry()
    print(f"Generated: {res['file']}")
