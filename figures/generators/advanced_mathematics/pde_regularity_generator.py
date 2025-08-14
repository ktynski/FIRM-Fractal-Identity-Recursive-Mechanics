#!/usr/bin/env python3
"""
PDE Regularity Generator (pure mathematics)
Elliptic interior regularity and Hölder continuity schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_pde_regularity() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Elliptic interior regularity (schematic domain with subdomain)
    ax1.set_title("Elliptic interior regularity (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 400)
    R = 1.5
    ax1.plot(R*np.cos(theta), R*np.sin(theta), 'k-', lw=2)
    ax1.fill(1.0*np.cos(theta), 1.0*np.sin(theta), color='lightblue', alpha=0.6)
    ax1.text(0,0, r"u ∈ C^∞(Ω')", ha='center', va='center', fontsize=12)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.axis('off')

    # 2) Hölder continuity profile schematic
    ax2.set_title("Hölder continuity u ∈ C^{0,α}", fontsize=14, weight='bold')
    x = np.linspace(0, 1, 200)
    alpha = 0.7
    u = x**alpha
    ax2.plot(x, u, lw=2)
    ax2.text(0.6, 0.6**alpha, r"|u(x)-u(y)| ≤ C|x-y|^α", fontsize=12)
    ax2.set_xlabel('x')
    ax2.set_ylabel('u(x)')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("PDE Regularity (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/pde_regularity.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "pde_regularity"}


if __name__ == "__main__":
    res = generate_pde_regularity()
    print(f"Generated: {res['file']}")
