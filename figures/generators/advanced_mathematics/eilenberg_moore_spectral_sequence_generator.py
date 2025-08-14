#!/usr/bin/env python3
"""
Eilenberg–Moore Spectral Sequence Generator (pure mathematics)
E2 page via Tor and convergence schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_eilenberg_moore_spectral_sequence() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) E2 page schematic: Tor^{A}(B,C)
    ax1.set_title(r"EMSS E₂^{p,q} = Tor^{A}_p(B,C)^q (schematic)", fontsize=14, weight='bold')
    pmax, qmax = 6, 5
    for p in range(pmax):
        for q in range(qmax):
            if p == 0 or (p+q) % 2 == 0:
                ax1.scatter(p, q, s=120, c='seagreen', edgecolors='k')
    ax1.set_xlim(-0.5, pmax-0.5)
    ax1.set_ylim(-0.5, qmax-0.5)
    ax1.set_xlabel('p')
    ax1.set_ylabel('q')
    ax1.grid(True, alpha=0.3)

    # 2) Convergence to H^*(...), schematic stabilization
    ax2.set_title("Convergence to target cohomology (schematic)", fontsize=14, weight='bold')
    s = np.linspace(0, 1, 200)
    ax2.plot(s, 1 - np.exp(-5*s), lw=2, label='stabilization')
    ax2.set_xlabel('pages r')
    ax2.set_ylabel('rank captured')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Eilenberg–Moore Spectral Sequence (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/eilenberg_moore_spectral_sequence.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "eilenberg_moore_spectral_sequence"}


if __name__ == "__main__":
    res = generate_eilenberg_moore_spectral_sequence()
    print(f"Generated: {res['file']}")
