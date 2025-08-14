#!/usr/bin/env python3
"""
Harmonic Analysis on Groups Generator (pure mathematics)
SU(2) characters and orthogonality (schematic), Peter–Weyl flavor.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_harmonic_analysis_groups() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) SU(2) characters: χ_j(θ) = sin((2j+1)θ/2)/sin(θ/2)
    ax1.set_title("SU(2) characters χ_j(θ)", fontsize=14, weight="bold")
    theta = np.linspace(1e-3, np.pi, 400)
    js = [0, 0.5, 1, 1.5, 2]
    for j in js:
        chi = np.sin((2*j + 1)*theta/2) / np.sin(theta/2)
        ax1.plot(theta, chi, label=f"j={j}")
    ax1.set_xlabel("θ ∈ [0, π]")
    ax1.set_ylabel("χ_j(θ)")
    ax1.grid(True, alpha=0.3)
    ax1.legend(ncol=2)

    # 2) Orthogonality (numeric inner product over [0, π] with weight sin^2(θ/2))
    ax2.set_title("Approx. orthogonality ∫ χ_i χ_j w(θ) dθ", fontsize=14, weight="bold")
    w = (np.sin(theta/2))**2
    mat = np.zeros((len(js), len(js)))
    for a, ja in enumerate(js):
        chi_a = np.sin((2*ja + 1)*theta/2) / np.sin(theta/2)
        for b, jb in enumerate(js):
            chi_b = np.sin((2*jb + 1)*theta/2) / np.sin(theta/2)
            mat[a, b] = np.trapz(chi_a * chi_b * w, theta)
    im = ax2.imshow(mat, cmap='coolwarm', origin='lower')
    for i in range(len(js)):
        for j in range(len(js)):
            ax2.text(j, i, f"{mat[i,j]:.1f}", ha='center', va='center', fontsize=9)
    ax2.set_xticks(range(len(js)))
    ax2.set_yticks(range(len(js)))
    ax2.set_xticklabels([f"j={j}" for j in js])
    ax2.set_yticklabels([f"j={j}" for j in js])
    plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)

    fig.suptitle("Harmonic Analysis on Groups (pure mathematics)", fontsize=16, weight="bold")
    plt.tight_layout()
    out = Path("figures/outputs/harmonic_analysis_groups.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "harmonic_analysis_groups"}


if __name__ == "__main__":
    res = generate_harmonic_analysis_groups()
    print(f"Generated: {res['file']}")
