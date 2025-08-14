#!/usr/bin/env python3
"""
Geometric Group Theory Generator (pure mathematics)
Cayley graph (truncated), hyperbolic disk schematic, and growth function.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_geometric_group_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Cayley graph of F_2 = <a,b> (depth=3)
    ax1.set_title("Cayley Graph of F_2 (depth=3, schematic)", fontsize=14, weight="bold")
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-0.5, 3.5)
    ax1.axis('off')
    nodes = {(0,0): 'e'}
    edges = []
    directions = [(1,0,'a'), (-1,0,'a^{-1}'), (0,1,'b'), (0,-1,'b^{-1}')]
    frontier = [(0,0)]
    for depth in range(1, 4):
        new_frontier = []
        for (x,y) in frontier:
            for dx, dy, lab in directions:
                nx, ny = x + dx, y + dy
                if (nx,ny) not in nodes:
                    nodes[(nx,ny)] = lab
                    edges.append(((x,y), (nx,ny), lab))
                    new_frontier.append((nx,ny))
        frontier = new_frontier
    for (x,y), label in nodes.items():
        ax1.scatter(x, y, s=60, c='k')
        ax1.text(x+0.1, y+0.1, label, fontsize=8)
    for (x1,y1), (x2,y2), lab in edges:
        ax1.plot([x1,x2],[y1,y2], 'gray', lw=1)

    # 2) Hyperbolic disk (Poincaré) schematic with boundary ∂G
    ax2.set_title("Hyperbolic Disk (schematic) and Boundary ∂G", fontsize=14, weight="bold")
    circle = plt.Circle((0,0), 1.0, fill=False, color='k', lw=2)
    ax2.add_patch(circle)
    # geodesic arcs (schematic)
    for ang in np.linspace(0, np.pi, 6):
        x = np.linspace(-0.9, 0.9, 200)
        y = 0.3*np.cos(5*x + ang)
        ax2.plot(x, y, alpha=0.4, color='steelblue')
    ax2.text(0, 1.05, r"∂G (Gromov boundary)", ha='center', va='bottom', fontsize=11)
    ax2.set_aspect('equal')
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.2, 1.2)
    ax2.axis('off')

    # 3) Growth function: exponential growth of F_2
    ax3.set_title("Growth of F_2: |B(n)| ~ c·λ^n (schematic)", fontsize=14, weight="bold")
    n = np.arange(0, 10)
    growth = 2*(3**n)  # schematic exponential growth
    ax3.semilogy(n, growth, 'o-', lw=2)
    ax3.set_xlabel("radius n")
    ax3.set_ylabel("|B(n)| (log scale)")
    ax3.grid(True, which='both', alpha=0.3)

    fig.suptitle("Geometric Group Theory (pure mathematics)", fontsize=16, weight="bold")
    plt.tight_layout()
    out = Path("figures/outputs/geometric_group_theory.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "geometric_group_theory"}


if __name__ == "__main__":
    res = generate_geometric_group_theory()
    print(f"Generated: {res['file']}")
