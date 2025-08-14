#!/usr/bin/env python3
"""
Geometric Langlands Generator (pure mathematics)
Hecke eigensheaves schematic, local systems, and correspondence diagram.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_geometric_langlands() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Moduli stack Bun_G(X) schematic
    ax1.set_title(r"Bun_G(X) and Loc_{G^\vee}(X) (schematic)", fontsize=14, weight='bold')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.axis('off')
    ax1.text(2.5, 6, r"Bun_G(X)", bbox=dict(boxstyle='round', fc='#eef'))
    ax1.text(7.5, 6, r"Loc_{G^\vee}(X)", bbox=dict(boxstyle='round', fc='#efe'))
    # arrows
    ax1.annotate('', xy=(7.0, 6), xytext=(3.0, 6), arrowprops=dict(arrowstyle='->', lw=2, color='purple'))
    ax1.text(5, 6.3, r"Geometric Langlands correspondence", ha='center', color='purple', weight='bold')

    # 2) Hecke operator action on D-modules
    ax2.set_title(r"Hecke Operators H_x on D(Bun_G)", fontsize=14, weight='bold')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8)
    ax2.axis('off')
    # objects and arrows
    ax2.text(2, 5.5, r"\mathcal{F}", bbox=dict(boxstyle='round', fc='#f0f0f0'))
    ax2.text(8, 5.5, r"H_x(\mathcal{F})", bbox=dict(boxstyle='round', fc='#f0f0f0'))
    ax2.annotate('', xy=(7.6, 5.5), xytext=(2.4, 5.5), arrowprops=dict(arrowstyle='->', lw=2))
    # eigen-sheaf condition
    ax2.text(5, 3, r"Hecke eigensheaf: H_x(\mathcal{F}) \cong E_x \otimes \mathcal{F}", ha='center',
             bbox=dict(boxstyle='round', fc='#ffd'))

    # 3) Local-to-global picture (spectral side)
    ax3.set_title(r"Local systems E: \pi_1(X) \to G^\vee (spectral side)", fontsize=14, weight='bold')
    t = np.linspace(0, 2*np.pi, 200)
    ax3.plot(np.cos(t), np.sin(t), 'k-', lw=2)
    for ang in np.linspace(0, 2*np.pi, 7, endpoint=False):
        ax3.arrow(0, 0, 0.8*np.cos(ang), 0.8*np.sin(ang), head_width=0.05, lw=2, color='steelblue')
    ax3.text(0, 0, r"\pi_1(X)", ha='center', va='center', bbox=dict(boxstyle='round', fc='#eef'))
    ax3.text(1.1, 0, r"G^\vee", ha='left', va='center')
    ax3.set_aspect('equal')
    ax3.axis('off')

    fig.suptitle("Geometric Langlands (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/geometric_langlands.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "geometric_langlands"}


if __name__ == "__main__":
    res = generate_geometric_langlands()
    print(f"Generated: {res['file']}")
