#!/usr/bin/env python3
"""
Sheaf Cohomology Spectral Sequences Generator (pure mathematics)
Leray spectral sequence and Cech-to-derived spectral sequence schematics.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_sheaf_cohomology_spectral_sequence() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Leray spectral sequence E2^{p,q} = H^p(Y, R^q f_* F) ⇒ H^{p+q}(X,F)
    ax1.set_title("Leray spectral sequence (schematic)", fontsize=14, weight='bold')
    pmax, qmax = 5, 4
    for p in range(pmax):
        for q in range(qmax):
            if (p,q) in [(0,0),(1,0),(0,1),(2,0),(1,1)]:
                ax1.scatter(p, q, s=200, c='tomato', edgecolors='k')
                ax1.text(p, q, f"{p},{q}", ha='center', va='center', fontsize=9)
    ax1.set_xlim(-0.5, pmax-0.5)
    ax1.set_ylim(-0.5, qmax-0.5)
    ax1.set_xlabel('p')
    ax1.set_ylabel('q')
    ax1.grid(True, alpha=0.3)

    # 2) Cech-to-derived spectral sequence schematic
    ax2.set_title("Cech-to-derived spectral sequence (schematic)", fontsize=14, weight='bold')
    for i in range(4):
        ax2.plot([0, 4], [i, i], 'k-', alpha=0.2)
    for j in range(5):
        ax2.plot([j, j], [0, 3], 'k-', alpha=0.2)
    for p in range(4):
        for q in range(3):
            if (p+q) % 2 == 0:
                ax2.scatter(p, q, s=150, c='gold', edgecolors='k')
    ax2.set_xlim(-0.5, 3.5)
    ax2.set_ylim(-0.5, 2.5)
    ax2.set_xlabel('p')
    ax2.set_ylabel('q')
    ax2.grid(True, alpha=0.3)

    # 3) Convergence schematic
    ax3.set_title("Convergence to H^{p+q}(X, F)", fontsize=14, weight='bold')
    s = np.linspace(0, 1, 200)
    ax3.plot(s, np.sqrt(s), lw=2, label='E_r')
    ax3.plot(s, s**0.2, lw=2, label='E_∞')
    ax3.legend()
    ax3.set_xlabel('pages r')
    ax3.set_ylabel('stability (schematic)')
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Sheaf Cohomology Spectral Sequences (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/sheaf_cohomology_spectral_sequence.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "sheaf_cohomology_spectral_sequence"}


if __name__ == "__main__":
    res = generate_sheaf_cohomology_spectral_sequence()
    print(f"Generated: {res['file']}")
