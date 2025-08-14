#!/usr/bin/env python3
"""
Free Probability Generator (pure mathematics)
Semicircle law and free convolution schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_free_probability() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Wigner semicircle law density
    ax1.set_title("Wigner semicircle law", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 400)
    rho = (1/(2*np.pi)) * np.sqrt(np.maximum(0, 4 - x**2))
    ax1.plot(x, rho, lw=2)
    ax1.fill_between(x, 0, rho, alpha=0.3)
    ax1.set_xlabel('x')
    ax1.set_ylabel('ρ(x)')
    ax1.grid(True, alpha=0.3)

    # 2) Free convolution schematic (additive) via R-transform linearization
    ax2.set_title("Free convolution ⊞ (schematic)", fontsize=14, weight='bold')
    s = np.linspace(0, 3, 200)
    R1 = 0.4*s
    R2 = 0.2*s**2/(1+s)
    Rsum = R1 + R2
    ax2.plot(s, R1, lw=2, label='R_μ')
    ax2.plot(s, R2, lw=2, label='R_ν')
    ax2.plot(s, Rsum, lw=2, label='R_{μ⊞ν}')
    ax2.set_xlabel('s (schematic)')
    ax2.set_ylabel('R-transform')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Free Probability (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/free_probability.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "free_probability"}


if __name__ == "__main__":
    res = generate_free_probability()
    print(f"Generated: {res['file']}")
