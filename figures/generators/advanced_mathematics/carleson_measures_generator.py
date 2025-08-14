#!/usr/bin/env python3
"""
Carleson Measures Generator (pure mathematics)
Carleson boxes and measure condition schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_carleson_measures() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Carleson box over boundary interval I
    ax1.set_title("Carleson box T(I) (schematic)", fontsize=14, weight='bold')
    ax1.add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.6, fc='#eef', ec='k'))
    ax1.add_patch(plt.Rectangle((0.2, 0.1), 0.4, 0.3, fc='#cdf', ec='k'))
    ax1.text(0.4, 0.3, 'T(I)', ha='center')
    ax1.text(0.3, 0.05, 'I', ha='center')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')

    # 2) Carleson measure condition μ(T(I)) ≤ C|I|
    ax2.set_title(r"Carleson: μ(T(I)) ≤ C |I| (schematic)", fontsize=14, weight='bold')
    I_length = np.linspace(0.05, 0.5, 20)
    mu = 2.0*I_length  # schematic with C=2
    ax2.plot(I_length, mu, 'o-', lw=2)
    ax2.set_xlabel('|I|')
    ax2.set_ylabel('μ(T(I))')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Carleson Measures (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/carleson_measures.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "carleson_measures"}


if __name__ == "__main__":
    res = generate_carleson_measures()
    print(f"Generated: {res['file']}")
