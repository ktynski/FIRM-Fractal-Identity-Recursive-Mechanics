#!/usr/bin/env python3
"""
Low-Dimensional Topology Generator (pure mathematics)
Trefoil-like knot schematic, Seifert circles, and Jones polynomial sample values.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_low_dimensional_topology() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Trefoil knot schematic (planar projection)
    ax1.set_title("Trefoil Knot (schematic projection)", fontsize=14, weight="bold")
    t = np.linspace(0, 2*np.pi, 400)
    x = np.sin(t) + 2*np.sin(2*t)
    y = np.cos(t) - 2*np.cos(2*t)
    ax1.plot(x, y, 'k-', lw=2)
    ax1.set_aspect('equal', adjustable='box')
    ax1.axis('off')

    # 2) Seifert circles (schematic)
    ax2.set_title("Seifert Circles (schematic)", fontsize=14, weight="bold")
    angles = np.linspace(0, 2*np.pi, 200)
    for r, c in zip([1.2, 0.9, 0.6], ['steelblue', 'tomato', 'green']):
        ax2.plot(r*np.cos(angles), r*np.sin(angles), color=c, lw=2)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # 3) Jones polynomial sample values (evaluated at t = e^{iθ}, schematic magnitude)
    ax3.set_title("Jones Polynomial |V_K(e^{iθ})| (schematic)", fontsize=14, weight="bold")
    theta = np.linspace(0, 2*np.pi, 200)
    # schematic magnitude pattern
    V_mag = 1 + 0.5*np.cos(3*theta) + 0.3*np.cos(5*theta)
    ax3.plot(theta, V_mag, lw=2)
    ax3.set_xlabel("θ")
    ax3.set_ylabel("|V_K(e^{iθ})|")
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Low-Dimensional Topology (pure mathematics)", fontsize=16, weight="bold")
    plt.tight_layout()
    out = Path("figures/outputs/low_dimensional_topology.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "low_dimensional_topology"}


if __name__ == "__main__":
    res = generate_low_dimensional_topology()
    print(f"Generated: {res['file']}")
