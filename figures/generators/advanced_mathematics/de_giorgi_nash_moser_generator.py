#!/usr/bin/env python3
"""
De Giorgi–Nash–Moser Regularity Generator (pure mathematics)
Oscillation decay and Harnack inequality schematic for solutions of elliptic PDE.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_de_giorgi_nash_moser() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Oscillation decay in nested balls
    ax1.set_title("Oscillation decay (schematic)", fontsize=14, weight='bold')
    k = np.arange(0, 6)
    osc = 1.0*(0.6)**k
    ax1.semilogy(k, osc, 'o-', lw=2)
    ax1.set_xlabel('scale k')
    ax1.set_ylabel('osc_{B_{r_k}} u')
    ax1.grid(True, which='both', alpha=0.3)

    # 2) Harnack inequality schematic: sup ≤ C inf on a ball
    ax2.set_title("Harnack inequality (schematic)", fontsize=14, weight='bold')
    radii = np.linspace(0.2, 1.0, 6)
    sup_vals = 1.0 + 0.1*(1-radii)
    inf_vals = 0.8 - 0.1*(1-radii)
    ax2.plot(radii, sup_vals, 'r-', lw=2, label='sup')
    ax2.plot(radii, inf_vals, 'b-', lw=2, label='inf')
    ax2.set_xlabel('radius')
    ax2.set_ylabel('value')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("De Giorgi–Nash–Moser Regularity (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/de_giorgi_nash_moser.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "de_giorgi_nash_moser"}


if __name__ == "__main__":
    res = generate_de_giorgi_nash_moser()
    print(f"Generated: {res['file']}")
