#!/usr/bin/env python3
"""
Fractional Sobolev and Besov Spaces Generator (pure mathematics)
Gagliardo seminorm schematic and Besov smoothness bars.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_fractional_sobolev_besov() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Gagliardo seminorm [u]_{W^{s,p}} schematic
    ax1.set_title(r"Gagliardo seminorm [u]_{W^{s,p}} (schematic)", fontsize=14, weight='bold')
    x = np.linspace(0, 1, 300)
    u = x**0.3
    # plot u and a shifted copy to visualize |u(x)-u(y)|/|x-y|^{s}
    y = x.copy()
    s = 0.4
    ax1.plot(x, u, lw=2)
    ax1.text(0.6, 0.6**0.3, r"∬ |u(x)-u(y)|^p/|x-y|^{sp+n} dx dy", fontsize=10)
    ax1.set_xlabel('x')
    ax1.set_ylabel('u(x)')
    ax1.grid(True, alpha=0.3)

    # 2) Besov smoothness bars B^{s}_{p,q}
    ax2.set_title(r"Besov smoothness B^{s}_{p,q} (schematic)", fontsize=14, weight='bold')
    labels = [r"B^{0.2}_{2,2}", r"B^{0.4}_{2,2}", r"B^{0.6}_{2,2}", r"B^{0.8}_{2,2}"]
    vals = [0.5, 1.0, 1.5, 2.0]
    ax2.bar(labels, vals, color=['#eef','#def','#cfe','#bdf'])
    ax2.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Fractional Sobolev and Besov Spaces (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/fractional_sobolev_besov.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "fractional_sobolev_besov"}


if __name__ == "__main__":
    res = generate_fractional_sobolev_besov()
    print(f"Generated: {res['file']}")
