#!/usr/bin/env python3
"""
Spectral Zeta Functions Generator (pure mathematics)
Riemann zeta schematic, eigenvalue zeta, and heat trace asymptotics.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_spectral_zeta_functions() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Riemann zeta: critical strip schematic
    ax1.set_title("Riemann zeta ζ(s) critical strip (schematic)", fontsize=14, weight='bold')
    ax1.set_xlim(-1, 3)
    ax1.set_ylim(-20, 20)
    ax1.axvspan(0, 1, color='#f0f8ff')
    ax1.axvline(0.5, color='red', linestyle='--', lw=2, label='Re(s)=1/2')
    t = np.linspace(0, 20, 8)
    y = np.r_[t, -t]
    x = np.full_like(y, 0.5)
    ax1.scatter(x, y, c='k', s=20, label='nontrivial zeros (schematic)')
    ax1.set_xlabel('Re(s)')
    ax1.set_ylabel('Im(s)')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='lower right')

    # 2) Eigenvalue zeta ζ_A(s) = Σ λ_k^{-s} for a model spectrum λ_k ~ k^2
    ax2.set_title(r"Eigenvalue zeta ζ_A(s) for λ_k≈k² (schematic)", fontsize=14, weight='bold')
    s_vals = np.linspace(0.6, 3.0, 200)
    K = 500
    k = np.arange(1, K+1)
    lam = k**2
    zeta_A = np.array([np.sum(lam**(-s)) for s in s_vals])
    ax2.plot(s_vals, zeta_A, lw=2)
    ax2.set_xlabel('s')
    ax2.set_ylabel('ζ_A(s)')
    ax2.grid(True, alpha=0.3)

    # 3) Heat trace asymptotics Tr(e^{-tA}) ~ (4πt)^{-n/2} Σ a_j t^j
    ax3.set_title("Heat trace asymptotics (schematic)", fontsize=14, weight='bold')
    tt = np.logspace(-3, 0, 200)
    n = 2
    a0, a1, a2 = 1.0, 0.2, 0.05
    heat = (4*np.pi*tt)**(-n/2) * (a0 + a1*tt + a2*tt**2)
    ax3.loglog(tt, heat, lw=2)
    ax3.set_xlabel('t')
    ax3.set_ylabel('Tr(e^{-tA})')
    ax3.grid(True, which='both', alpha=0.3)

    fig.suptitle("Spectral Zeta Functions (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/spectral_zeta_functions.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "spectral_zeta_functions"}


if __name__ == "__main__":
    res = generate_spectral_zeta_functions()
    print(f"Generated: {res['file']}")
