#!/usr/bin/env python3
"""
Hodge Theory on Graphs Generator (pure mathematics)
Graph Laplacians on 0- and 1-forms and Hodge decomposition schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_hodge_theory_on_graphs() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Graph
    ax1.set_title("Graph G (schematic)", fontsize=14, weight='bold')
    pos = np.array([[0,0], [1,0.2], [2,0], [0.5,1], [1.5,1]])
    edges = [(0,1),(1,2),(0,3),(1,3),(1,4),(2,4),(3,4)]
    for (i,j) in edges:
        ax1.plot([pos[i,0], pos[j,0]], [pos[i,1], pos[j,1]], 'k-', lw=2)
    ax1.scatter(pos[:,0], pos[:,1], s=120, c='steelblue', edgecolors='k')
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 2) 0- and 1-form Laplacians (schematic spectra)
    ax2.set_title("Spectra of Δ_0 and Δ_1 (schematic)", fontsize=14, weight='bold')
    lam0 = [0.0, 0.8, 1.2, 1.7, 2.4]
    lam1 = [0.1, 0.9, 1.5, 2.2, 2.9]
    ax2.stem(range(len(lam0)), lam0, linefmt='b-', markerfmt='bo', basefmt=' ')  # Δ0
    ax2.stem(range(len(lam1)), lam1, linefmt='r-', markerfmt='ro', basefmt=' ')
    ax2.set_xlabel('index')
    ax2.set_ylabel('eigenvalue')
    ax2.grid(True, alpha=0.3)

    # 3) Hodge decomposition on graph: C^1 = Im d ⊕ Im δ ⊕ Harm^1
    ax3.set_title("Graph Hodge: C^1 = Im d ⊕ Im δ ⊕ Harm^1 (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 2*np.pi, 200)
    for (a,b,shift,color,label) in [
        (2.0, 1.0, (-1.2, 0.0), '#ffd', 'Im d'),
        (2.0, 1.0, ( 1.2, 0.0), '#dfd', 'Im δ'),
        (1.6, 0.8, ( 0.0, 0.0), '#ddf', 'Harm^1')
    ]:
        x = a*np.cos(t) + shift[0]
        y = b*np.sin(t) + shift[1]
        ax3.fill(x, y, color=color, alpha=0.7, edgecolor='k')
        ax3.text(shift[0], shift[1], label, ha='center', va='center')
    ax3.set_aspect('equal')
    ax3.set_xlim(-4, 4)
    ax3.set_ylim(-2.5, 2.5)
    ax3.axis('off')

    fig.suptitle("Hodge Theory on Graphs (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/hodge_theory_on_graphs.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "hodge_theory_on_graphs"}


if __name__ == "__main__":
    res = generate_hodge_theory_on_graphs()
    print(f"Generated: {res['file']}")
