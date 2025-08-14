#!/usr/bin/env python3
"""
Aperiodic Tilings Generator (pure mathematics)
Penrose-like rhomb tiling patch schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def rhomb(ax, center, angle, long_diag=1.0, short_diag=0.618, color='gold'):
    a = long_diag/2
    b = short_diag/2
    # vertices of rhomb centered at origin, then rotate and translate
    verts = np.array([[ a, 0], [0,  b], [-a, 0], [0, -b]])
    R = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    verts = (verts @ R.T) + np.array(center)
    ax.fill(verts[:,0], verts[:,1], color=color, alpha=0.8, edgecolor='k')


def generate_aperiodic_tilings() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_title("Aperiodic Tilings (Penrose-like patch)", fontsize=14, weight='bold')

    rng = np.random.default_rng(3)
    centers = rng.uniform(-2, 2, size=(40, 2))
    for c in centers:
        ang = rng.uniform(0, np.pi)
        col = '#f7d560' if rng.random() < 0.5 else '#c0d8f0'
        rhomb(ax, c, ang, color=col)

    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axis('off')

    fig.suptitle("Aperiodic Tilings (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/aperiodic_tilings.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "aperiodic_tilings"}


if __name__ == "__main__":
    res = generate_aperiodic_tilings()
    print(f"Generated: {res['file']}")
