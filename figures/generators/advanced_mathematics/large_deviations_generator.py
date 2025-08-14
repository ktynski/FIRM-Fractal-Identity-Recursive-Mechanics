#!/usr/bin/env python3
"""
Large Deviations Generator (pure mathematics)
Rate function I(x) and tail probability schematic via Cramér's theorem.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_large_deviations() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Rate function I(x) = sup_{θ}(θx - Λ(θ)) (schematic convex function)
    ax1.set_title("Rate function I(x) (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 400)
    I = 0.5*(x-0.2)**2 + 0.05*np.abs(x)
    ax1.plot(x, I, lw=2)
    ax1.set_xlabel('x')
    ax1.set_ylabel('I(x)')
    ax1.grid(True, alpha=0.3)

    # 2) Tail probability P(S_n/n ≥ a) ~ e^{-n I(a)} (schematic)
    ax2.set_title("Tail probability decay (schematic)", fontsize=14, weight='bold')
    n = np.array([10, 20, 50, 100, 200])
    a = 0.8
    Ia = 0.5*(a-0.2)**2 + 0.05*np.abs(a)
    tail = np.exp(-n * Ia)
    ax2.semilogy(n, tail, 'o-', lw=2)
    ax2.set_xlabel('n')
    ax2.set_ylabel('P(S_n/n ≥ a)')
    ax2.grid(True, which='both', alpha=0.3)

    fig.suptitle("Large Deviations (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/large_deviations.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "large_deviations"}


if __name__ == "__main__":
    res = generate_large_deviations()
    print(f"Generated: {res['file']}")
