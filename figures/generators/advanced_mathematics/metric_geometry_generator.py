#!/usr/bin/env python3
"""
Metric Geometry Generator (pure mathematics)
Metric balls, Gromov–Hausdorff distance schematic, and geodesic property.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_metric_geometry() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Metric balls in a space (schematic)
    ax1.set_title("Metric balls B(x,r) (schematic)", fontsize=14, weight='bold')
    centers = np.array([[0,0], [1.5,0.5], [-1.0,1.0]])
    radii = [1.0, 0.8, 0.6]
    theta = np.linspace(0, 2*np.pi, 200)
    for c, r in zip(centers, radii):
        ax1.plot(c[0] + r*np.cos(theta), c[1] + r*np.sin(theta), lw=2)
        ax1.scatter([c[0]], [c[1]], s=50, c='k')
        ax1.text(c[0], c[1]-0.1, f"r={r}", ha='center')
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 3)
    ax1.set_ylim(-1.5, 2.5)
    ax1.grid(True, alpha=0.3)

    # 2) Gromov–Hausdorff distance schematic: embed two spaces into a common Z
    ax2.set_title("Gromov–Hausdorff distance (schematic)", fontsize=14, weight='bold')
    # Two finite metric spaces represented by point clouds
    A = np.array([[0,0],[1,0],[0.5,0.8]])
    B = np.array([[2.5,0.2],[3.5,0.2],[3.0,1.0]])
    ax2.scatter(A[:,0], A[:,1], s=80, c='steelblue', label='A', edgecolors='k')
    ax2.scatter(B[:,0], B[:,1], s=80, c='tomato', label='B', edgecolors='k')
    # matching lines
    for i in range(min(len(A), len(B))):
        ax2.plot([A[i,0], B[i,0]], [A[i,1], B[i,1]], 'k--', alpha=0.5)
    ax2.set_aspect('equal')
    ax2.set_xlim(-0.5, 4.5)
    ax2.set_ylim(-0.5, 1.6)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # 3) Geodesic property: shortest paths inside space
    ax3.set_title("Geodesic space: shortest paths exist", fontsize=14, weight='bold')
    P = np.array([0, 0])
    Q = np.array([3, 1.2])
    ax3.scatter([P[0], Q[0]], [P[1], Q[1]], s=80, c=['blue','red'])
    ax3.text(P[0], P[1]-0.1, 'P', ha='center')
    ax3.text(Q[0], Q[1]+0.05, 'Q', ha='center')
    # geodesic line
    t = np.linspace(0, 1, 100)
    G = P*(1-t)[:,None] + Q*t[:,None]
    ax3.plot(G[:,0], G[:,1], 'k-', lw=2)
    ax3.set_aspect('equal')
    ax3.set_xlim(-0.5, 3.5)
    ax3.set_ylim(-0.5, 1.8)
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Metric Geometry (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/metric_geometry.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "metric_geometry"}


if __name__ == "__main__":
    res = generate_metric_geometry()
    print(f"Generated: {res['file']}")
