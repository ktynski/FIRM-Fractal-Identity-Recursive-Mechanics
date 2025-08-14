#!/usr/bin/env python3
"""
Minimal Surfaces Generator (pure mathematics)
Catenoid/Enneper-like schematics and mean curvature ~ 0 illustration.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_minimal_surfaces() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Catenoid-like level sets (schematic in 2D projection)
    ax1.set_title("Catenoid level sets (schematic)", fontsize=14, weight='bold')
    r = np.linspace(0.1, 2.0, 6)
    theta = np.linspace(0, 2*np.pi, 400)
    for a in r:
        x = a*np.cos(theta)
        y = a*np.sin(theta)
        ax1.plot(x, y, lw=2, alpha=0.7)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2.2, 2.2)
    ax1.set_ylim(-2.2, 2.2)
    ax1.grid(True, alpha=0.3)

    # 2) Mean curvature schematic H ~ 0 along surface
    ax2.set_title("Mean curvature ~ 0 (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 200)
    y = 0.2*np.sin(2*np.pi*x) / (1 + x**2)
    H = 0.02*np.sin(6*np.pi*x)  # small oscillation around 0
    ax2.plot(x, y, 'k-', lw=2, label='profile')
    ax2.plot(x, H, 'r--', lw=2, label='H(x)')
    ax2.axhline(0, color='gray', linestyle=':')
    ax2.set_xlabel('x')
    ax2.set_ylabel('value')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Minimal Surfaces (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/minimal_surfaces.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "minimal_surfaces"}


if __name__ == "__main__":
    res = generate_minimal_surfaces()
    print(f"Generated: {res['file']}")
