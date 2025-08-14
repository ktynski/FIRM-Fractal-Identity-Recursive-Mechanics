#!/usr/bin/env python3
"""
Isoperimetric Inequality Generator (pure mathematics)
Area vs perimeter comparison; circle is optimal schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_isoperimetric_inequality() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Shapes with same perimeter; circle maximizes area (schematic)
    ax1.set_title("Isoperimetric optimality (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 400)
    circle_x = np.cos(theta)
    circle_y = np.sin(theta)
    ax1.plot(circle_x, circle_y, 'k-', lw=2, label='circle')
    r = 1
    star = (1 + 0.3*np.cos(5*theta))
    ax1.plot(star*np.cos(theta), star*np.sin(theta), 'r--', lw=2, label='wavy curve')
    ax1.set_aspect('equal')
    ax1.legend()
    ax1.axis('off')

    # 2) Area vs perimeter curve (schematic)
    ax2.set_title("Area vs perimeter (schematic)", fontsize=14, weight='bold')
    P = np.linspace(2, 8, 100)
    A_circle = (P**2)/(4*np.pi)
    A_other = 0.9*A_circle
    ax2.plot(P, A_circle, lw=2, label='circle bound')
    ax2.plot(P, A_other, 'r--', lw=2, label='non-optimal shapes')
    ax2.set_xlabel('Perimeter P')
    ax2.set_ylabel('Area A')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Isoperimetric Inequality (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/isoperimetric_inequality.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "isoperimetric_inequality"}


if __name__ == "__main__":
    res = generate_isoperimetric_inequality()
    print(f"Generated: {res['file']}")
