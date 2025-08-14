#!/usr/bin/env python3
"""
Littlewood–Paley Theory Generator (pure mathematics)
Dyadic frequency pieces and square function schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_littlewood_paley() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Dyadic frequency bumps
    ax1.set_title("Dyadic frequency pieces (schematic)", fontsize=14, weight='bold')
    xi = np.linspace(0, 10, 1000)
    def bump(center, width):
        return np.exp(-((xi-center)**2)/(2*width**2))
    for j, (c, w) in enumerate([(0.5,0.4),(1,0.5),(2,0.6),(4,0.8),(8,1.0)]):
        ax1.plot(xi, bump(c, w), lw=2, label=f'Δ_{j}')
    ax1.set_xlabel('frequency |xi|')
    ax1.set_ylabel('amplitude')
    ax1.grid(True, alpha=0.3)
    ax1.legend(ncol=2)

    # 2) Square function S(f) = (Σ |Δ_j f|^2)^{1/2} (schematic)
    ax2.set_title("Square function S(f) (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-3, 3, 600)
    parts = [np.exp(-(x-j/2.0)**2) for j in range(-2,3)]
    S = np.sqrt(np.sum([p**2 for p in parts], axis=0))
    ax2.plot(x, S, lw=2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('S(f)(x)')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Littlewood–Paley Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/littlewood_paley.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "littlewood_paley"}


if __name__ == "__main__":
    res = generate_littlewood_paley()
    print(f"Generated: {res['file']}")
