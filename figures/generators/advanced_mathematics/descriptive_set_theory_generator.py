#!/usr/bin/env python3
"""
Descriptive Set Theory Generator (pure mathematics)
Borel hierarchy schematic and analytic/co-analytic sets in Polish spaces.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_descriptive_set_theory() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Borel hierarchy Σ^0_n / Π^0_n schematic
    ax1.set_title("Borel hierarchy (schematic)", fontsize=14, weight='bold')
    levels = ["Σ^0_1 (open)", "Π^0_1 (closed)", "Σ^0_2", "Π^0_2", "⋯"]
    for i, lv in enumerate(levels):
        ax1.text(0.1, 0.9 - i*0.18, lv, fontsize=12, bbox=dict(boxstyle='round', fc='#eef'))
    ax1.axis('off')

    # 2) Analytic/co-analytic sets: projection schematic in Polish space
    ax2.set_title("Analytic (Σ^1_1) via projection", fontsize=14, weight='bold')
    # product X×Y and projection π_X
    ax2.add_patch(plt.Rectangle((0.1, 0.1), 0.6, 0.6, fc='#f8f8ff', ec='k'))
    ax2.text(0.4, 0.75, 'X × Y', ha='center')
    # subset A ⊂ X×Y
    ax2.add_patch(plt.Rectangle((0.2, 0.2), 0.3, 0.4, fc='#cde', ec='k'))
    ax2.text(0.35, 0.45, 'A', ha='center')
    # projection arrow
    ax2.annotate('', xy=(0.85, 0.4), xytext=(0.7, 0.4), arrowprops=dict(arrowstyle='->', lw=2))
    ax2.text(0.77, 0.42, r"π_X(A)", ha='center')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    fig.suptitle("Descriptive Set Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/descriptive_set_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "descriptive_set_theory"}


if __name__ == "__main__":
    res = generate_descriptive_set_theory()
    print(f"Generated: {res['file']}")
