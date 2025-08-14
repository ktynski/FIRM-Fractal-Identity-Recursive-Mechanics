#!/usr/bin/env python3
"""
de Rham Cohomology Generator (pure mathematics)
Closed/exact forms, Stokes theorem schematic, and H^k_{dR}(M).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_de_rham_cohomology() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Closed vs exact forms (schematic arrows)
    ax1.set_title("Closed vs Exact (schematic)", fontsize=14, weight='bold')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.axis('off')
    ax1.text(2, 6, r"Ω^{k-1}(M)", bbox=dict(boxstyle='round', fc='#eef'))
    ax1.text(5, 6, r"Ω^{k}(M)", bbox=dict(boxstyle='round', fc='#eef'))
    ax1.text(8, 6, r"Ω^{k+1}(M)", bbox=dict(boxstyle='round', fc='#eef'))
    ax1.annotate('', xy=(4.6, 6), xytext=(2.4, 6), arrowprops=dict(arrowstyle='->', lw=2))
    ax1.text(3.5, 6.3, 'd', ha='center')
    ax1.annotate('', xy=(7.6, 6), xytext=(5.4, 6), arrowprops=dict(arrowstyle='->', lw=2))
    ax1.text(6.5, 6.3, 'd', ha='center')
    ax1.text(5, 4, r"closed: dω=0; exact: ω=dη", ha='center')

    # 2) Stokes theorem schematic ∫_{∂M} ω = ∫_M dω
    ax2.set_title("Stokes theorem (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 200)
    R = 1.2
    ax2.plot(R*np.cos(theta), R*np.sin(theta), 'k-', lw=2)
    ax2.arrow(1.2*np.cos(np.pi/4), 1.2*np.sin(np.pi/4), -0.2, 0.0, head_width=0.05)
    ax2.text(0, 0, r"∫_M dω", ha='center')
    ax2.text(1.4, 0.0, r"∫_{∂M} ω", ha='center')
    ax2.set_aspect('equal')
    ax2.axis('off')

    # 3) H^k_{dR}(M) dimensions for torus T^2
    ax3.set_title(r"H^k_{dR}(T^2)", fontsize=14, weight='bold')
    ks = [0,1,2]
    dims = [1,2,1]
    ax3.bar(ks, dims, color='tomato')
    for k, v in zip(ks, dims):
        ax3.text(k, v+0.05, f"{v}", ha='center')
    ax3.set_xlabel('k')
    ax3.set_ylabel('dim H^k')
    ax3.grid(True, axis='y', alpha=0.3)

    fig.suptitle("de Rham Cohomology (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/de_rham_cohomology.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "de_rham_cohomology"}


if __name__ == "__main__":
    res = generate_de_rham_cohomology()
    print(f"Generated: {res['file']}")
