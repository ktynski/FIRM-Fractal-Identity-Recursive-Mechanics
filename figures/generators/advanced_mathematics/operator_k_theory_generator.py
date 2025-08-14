#!/usr/bin/env python3
"""
Operator K-Theory Generator (pure mathematics)
Bott periodicity schematic and index map diagram.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_operator_k_theory() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Bott periodicity schematic K^*(X) ≅ K^{*+2}(X)
    ax1.set_title("Bott periodicity (schematic)", fontsize=14, weight='bold')
    degrees = np.arange(0, 8)
    vals = (np.sin(degrees*np.pi/2) != 0).astype(int)
    ax1.stem(degrees, vals)
    ax1.set_xlabel('degree n')
    ax1.set_ylabel('nontrivial? (schematic)')
    ax1.grid(True, alpha=0.3)

    # 2) Index map diagram ind: K_0(A) → ℤ (schematic)
    ax2.set_title("Index map (schematic)", fontsize=14, weight='bold')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 6)
    ax2.axis('off')
    ax2.text(2, 3, r"K_0(A)", bbox=dict(boxstyle='round', fc='#eef'))
    ax2.text(8, 3, r"ℤ", bbox=dict(boxstyle='round', fc='#efe'))
    ax2.annotate('', xy=(7.2, 3), xytext=(2.8, 3), arrowprops=dict(arrowstyle='->', lw=2))
    ax2.text(5, 3.3, 'index', ha='center')

    fig.suptitle("Operator K-Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/operator_k_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "operator_k_theory"}


if __name__ == "__main__":
    res = generate_operator_k_theory()
    print(f"Generated: {res['file']}")
