#!/usr/bin/env python3
"""
Algebraic K-Theory Examples Generator (pure mathematics)
K0 and K1 for simple rings (schematic values and maps).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_algebraic_k_theory_examples() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("K0 and K1 examples (schematic)", fontsize=14, weight='bold')
    labels = ['K0(ℤ)','K1(ℤ)','K0(ℂ)','K1(ℂ)']
    vals = [1, 2, 1, 1]
    ax.bar(labels, vals, color=['#eef','#cfe','#def','#bdf'])
    ax.set_ylabel('rank/size (schematic)')
    ax.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Algebraic K-Theory Examples (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/algebraic_k_theory_examples.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "algebraic_k_theory_examples"}


if __name__ == "__main__":
    res = generate_algebraic_k_theory_examples()
    print(f"Generated: {res['file']}")
