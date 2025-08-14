#!/usr/bin/env python3
"""
Harmonic Measure Generator (pure mathematics)
Boundary arcs probability schematic and Poisson kernel flavor.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_harmonic_measure() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Harmonic measure of boundary arcs from interior point
    ax1.set_title("Harmonic measure of arcs (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 400)
    ax1.plot(np.cos(theta), np.sin(theta), 'k-', lw=2)
    z0 = np.array([0.2, 0.1])
    ax1.scatter([z0[0]],[z0[1]], s=60, c='red')
    ax1.text(z0[0]+0.05, z0[1], 'z0', color='red')
    # arcs
    arc1 = theta[(theta>=0) & (theta<=np.pi/3)]
    arc2 = theta[(theta>=np.pi/3) & (theta<=2*np.pi/3)]
    ax1.plot(np.cos(arc1), np.sin(arc1), lw=6, alpha=0.4, color='gold')
    ax1.plot(np.cos(arc2), np.sin(arc2), lw=6, alpha=0.4, color='steelblue')
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 2) Poisson kernel evaluated at boundary angles
    ax2.set_title("Poisson kernel P_r(θ) (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(-np.pi, np.pi, 400)
    r = 0.5
    P = (1 - r**2) / (1 - 2*r*np.cos(theta) + r**2)
    ax2.plot(theta, P, lw=2)
    ax2.set_xlabel('θ')
    ax2.set_ylabel('P_r(θ)')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Harmonic Measure (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/harmonic_measure.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "harmonic_measure"}


if __name__ == "__main__":
    res = generate_harmonic_measure()
    print(f"Generated: {res['file']}")
