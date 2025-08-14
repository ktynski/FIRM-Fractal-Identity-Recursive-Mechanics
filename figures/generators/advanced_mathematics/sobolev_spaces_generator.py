#!/usr/bin/env python3
"""
Sobolev Spaces Generator (pure mathematics)
Sobolev norms, embeddings diagram, and Poincaré inequality schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_sobolev_spaces() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Sobolev norms ||u||_{H^k}^2 = Σ_{|α|≤k} ||∂^α u||_2^2 (schematic)
    ax1.set_title(r"Sobolev norm ||u||_{H^k} (schematic)", fontsize=14, weight='bold')
    x = np.linspace(0, 2*np.pi, 400)
    u = np.sin(x) + 0.5*np.sin(3*x)
    du = np.gradient(u, x)
    d2u = np.gradient(du, x)
    H1 = np.trapz(u**2 + du**2, x)
    H2 = np.trapz(u**2 + du**2 + d2u**2, x)
    ax1.plot(x, u, lw=2, label='u')
    ax1.plot(x, du, lw=1, label="u'")
    ax1.plot(x, d2u, lw=1, label="u''")
    ax1.text(0.05, 0.9, f"||u||_{H1}^2≈{H1:.2f}\n||u||_{H2}^2≈{H2:.2f}", transform=ax1.transAxes,
             bbox=dict(boxstyle='round', fc='#ffd'))
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) Sobolev embeddings (schematic arrows)
    ax2.set_title("Sobolev embeddings (schematic)", fontsize=14, weight='bold')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8)
    ax2.axis('off')
    nodes = [(2,6,'H¹(Ω)'), (8,6,'L^{p}(Ω)'), (5,3,'C^{0,α}(Ω)')]
    for x0, y0, label in nodes:
        ax2.text(x0, y0, label, ha='center', va='center', bbox=dict(boxstyle='round', fc='#eef'))
    ax2.annotate('', xy=(7.6, 6), xytext=(2.4, 6), arrowprops=dict(arrowstyle='->', lw=2))
    ax2.text(5, 6.3, 'Rellich/Kondrachov', ha='center')
    ax2.annotate('', xy=(5, 3.4), xytext=(2, 5.6), arrowprops=dict(arrowstyle='->', lw=2))
    ax2.text(3.7, 4.7, 'Morrey', ha='center')

    # 3) Poincaré inequality schematic ‖u‖_{L²} ≤ C ‖∇u‖_{L²}
    ax3.set_title("Poincaré inequality (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 1, 200)
    u = t*(1-t)
    ax3.plot(t, u, lw=2)
    ax3.text(0.6, 0.18, r"‖u‖_{L²} ≤ C‖∇u‖_{L²}", fontsize=12)
    ax3.set_xlabel('x')
    ax3.set_ylabel('u(x)')
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Sobolev Spaces (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/sobolev_spaces.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "sobolev_spaces"}


if __name__ == "__main__":
    res = generate_sobolev_spaces()
    print(f"Generated: {res['file']}")
