#!/usr/bin/env python3
"""
Distribution Theory Generator (pure mathematics)
Test functions, Dirac delta, and convolution smoothing schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_distribution_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Test functions φ ∈ C_c^∞(ℝ)
    ax1.set_title(r"Test function φ ∈ C_c^∞(ℝ)", fontsize=14, weight='bold')
    x = np.linspace(-3, 3, 400)
    phi = np.exp(-1/(1 - (x/2)**2))
    phi[np.abs(x) >= 2] = 0
    ax1.plot(x, phi, lw=2)
    ax1.set_xlabel('x')
    ax1.set_ylabel('φ(x)')
    ax1.grid(True, alpha=0.3)

    # 2) Dirac delta action ⟨δ, φ⟩ = φ(0)
    ax2.set_title(r"Dirac δ: ⟨δ, φ⟩ = φ(0)", fontsize=14, weight='bold')
    ax2.stem([0], [1], linefmt='k-', markerfmt='ko', basefmt='k-')
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(0, 1.2)
    ax2.grid(True, alpha=0.3)

    # 3) Convolution smoothing f*ρ_ε
    ax3.set_title(r"Convolution smoothing f * ρ_ε", fontsize=14, weight='bold')
    f = np.sign(x)
    rho = np.exp(-x**2/0.2)
    rho /= np.trapz(rho, x)
    conv = np.convolve(f, rho, mode='same')
    conv /= np.max(np.abs(conv))
    ax3.plot(x, f, 'k--', lw=1, label='f')
    ax3.plot(x, conv, 'r-', lw=2, label='f*ρ_ε')
    ax3.set_xlabel('x')
    ax3.set_ylabel('value')
    ax3.grid(True, alpha=0.3)
    ax3.legend()

    fig.suptitle("Distribution Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/distribution_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "distribution_theory"}


if __name__ == "__main__":
    res = generate_distribution_theory()
    print(f"Generated: {res['file']}")
