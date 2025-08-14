#!/usr/bin/env python3
"""
BV Functions Generator (pure mathematics)
Jump set, total variation schematic, and perimeter of sets.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_bv_functions() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) BV function with jump (schematic)
    ax1.set_title("BV function with jump (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 400)
    u = np.where(x < 0.3, 0.2 + 0.3*x, 1.0 + 0.1*np.sin(5*(x-0.3)))
    ax1.plot(x, u, lw=2)
    ax1.axvline(0.3, color='r', linestyle='--', alpha=0.6)
    ax1.set_xlabel('x')
    ax1.set_ylabel('u(x)')
    ax1.grid(True, alpha=0.3)

    # 2) Total variation TV(u) as integral of |Du|
    ax2.set_title("Total variation TV(u) (schematic)", fontsize=14, weight='bold')
    du = np.abs(np.gradient(u, x))
    tv = np.trapz(du, x)
    ax2.plot(x, du, lw=2)
    ax2.text(-1.8, np.max(du)*0.8, f"TV≈{tv:.2f}")
    ax2.set_xlabel('x')
    ax2.set_ylabel('|Du|')
    ax2.grid(True, alpha=0.3)

    # 3) Perimeter of set E: P(E) = |Dχ_E| (schematic)
    ax3.set_title("Perimeter P(E) (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 200)
    r = 1.0 + 0.2*np.cos(3*theta)
    ax3.plot(r*np.cos(theta), r*np.sin(theta), 'k-', lw=2)
    ax3.set_aspect('equal')
    ax3.set_xlim(-1.5, 1.5)
    ax3.set_ylim(-1.5, 1.5)
    ax3.axis('off')

    fig.suptitle("BV Functions and Perimeters (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/bv_functions.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "bv_functions"}


if __name__ == "__main__":
    res = generate_bv_functions()
    print(f"Generated: {res['file']}")
