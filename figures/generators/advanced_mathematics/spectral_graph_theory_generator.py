#!/usr/bin/env python3
"""
Spectral Graph Theory Generator (pure mathematics)
Graph Laplacian spectrum and Fiedler vector visualization (schematic).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_spectral_graph_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Graph (schematic small connected graph)
    ax1.set_title("Graph G (schematic)", fontsize=14, weight='bold')
    pos = np.array([[0,0], [1,0.2], [2,0], [0.5,1], [1.5,1]])
    edges = [(0,1),(1,2),(0,3),(1,3),(1,4),(2,4),(3,4)]
    for (i,j) in edges:
        ax1.plot([pos[i,0], pos[j,0]], [pos[i,1], pos[j,1]], 'k-', lw=2)
    ax1.scatter(pos[:,0], pos[:,1], s=120, c='steelblue', edgecolors='k')
    for i,(x,y) in enumerate(pos):
        ax1.text(x, y+0.08, f"v{i}", ha='center')
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 2) Laplacian spectrum
    ax2.set_title("Laplacian Spectrum σ(L)", fontsize=14, weight='bold')
    n = len(pos)
    A = np.zeros((n,n))
    for i,j in edges:
        A[i,j] = A[j,i] = 1
    D = np.diag(A.sum(axis=1))
    L = D - A
    eigvals, eigvecs = np.linalg.eigh(L)
    ax2.bar(np.arange(n), eigvals, color='tomato')
    for i,lam in enumerate(eigvals):
        ax2.text(i, lam+0.05, f"{lam:.2f}", ha='center', fontsize=9)
    ax2.set_xlabel('index')
    ax2.set_ylabel('eigenvalue')
    ax2.grid(True, axis='y', alpha=0.3)

    # 3) Fiedler vector on nodes (2nd smallest eigenvector)
    ax3.set_title("Fiedler Vector (embedding color)", fontsize=14, weight='bold')
    fiedler = eigvecs[:, 1]
    rng = np.ptp(fiedler) + 1e-9
    norm = (fiedler - fiedler.min()) / rng
    ax3.scatter(pos[:,0], pos[:,1], s=200, c=norm, cmap='coolwarm', edgecolors='k')
    for i,(x,y) in enumerate(pos):
        ax3.text(x, y+0.08, f"{fiedler[i]:.2f}", ha='center')
    ax3.set_aspect('equal')
    ax3.axis('off')

    fig.suptitle("Spectral Graph Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/spectral_graph_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "spectral_graph_theory", "eigenvalues": eigvals.tolist()}


if __name__ == "__main__":
    res = generate_spectral_graph_theory()
    print(f"Generated: {res['file']}")
