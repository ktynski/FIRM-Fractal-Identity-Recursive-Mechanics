#!/usr/bin/env python3
"""
Stein Interpolation Generator (pure mathematics)
Analytic family T_z on strip and norm bound schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_stein_interpolation() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Complex strip 0 ≤ Re z ≤ 1 with boundary lines
    ax1.set_title("Analytic family T_z on strip (schematic)", fontsize=14, weight='bold')
    ax1.set_xlim(-0.2, 1.2)
    ax1.set_ylim(-3, 3)
    ax1.axvline(0, color='k')
    ax1.axvline(1, color='k')
    ax1.fill_betweenx(np.linspace(-3,3,2), 0, 1, color='#eef')
    ax1.text(0.02, 2.5, 'Re z = 0', fontsize=11)
    ax1.text(0.82, 2.5, 'Re z = 1', fontsize=11)
    ax1.set_xlabel('Re z')
    ax1.set_ylabel('Im z')
    ax1.grid(True, alpha=0.3)

    # 2) Norm bound ||T_theta||_{p->q} ≤ M0^{1-theta} M1^{theta}
    ax2.set_title("Interpolation bound (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 1, 100)
    M0, M1 = 2.0, 0.8
    bound = (M0**(1-theta)) * (M1**theta)
    ax2.plot(theta, bound, lw=2)
    ax2.set_xlabel('theta')
    ax2.set_ylabel('norm bound')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Stein Interpolation (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/stein_interpolation.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "stein_interpolation"}


if __name__ == "__main__":
    res = generate_stein_interpolation()
    print(f"Generated: {res['file']}")
