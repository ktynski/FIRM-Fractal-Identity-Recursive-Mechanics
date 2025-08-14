#!/usr/bin/env python3
"""
Hodge Decomposition Generator (pure mathematics)
Ω^k = Im d ⊕ Im δ ⊕ Harm^k schematic decomposition.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_hodge_decomposition() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title(r"Hodge: Ω^k = Im d ⊕ Im δ ⊕ Harm^k (schematic)", fontsize=14, weight='bold')
    # three overlapping ellipses
    t = np.linspace(0, 2*np.pi, 200)
    for (a,b,shift,color,label) in [
        (2.0, 1.2, (-1.2, 0.0), '#ffd', 'Im d'),
        (2.0, 1.2, ( 1.2, 0.0), '#dfd', 'Im δ'),
        (1.6, 1.0, ( 0.0, 0.0), '#ddf', 'Harm^k')
    ]:
        x = a*np.cos(t) + shift[0]
        y = b*np.sin(t) + shift[1]
        ax.fill(x, y, color=color, alpha=0.7, edgecolor='k')
        ax.text(shift[0], shift[1], label, ha='center', va='center')
    ax.set_aspect('equal')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2.5, 2.5)
    ax.axis('off')

    fig.suptitle("Hodge Decomposition (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/hodge_decomposition.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "hodge_decomposition"}


if __name__ == "__main__":
    res = generate_hodge_decomposition()
    print(f"Generated: {res['file']}")
