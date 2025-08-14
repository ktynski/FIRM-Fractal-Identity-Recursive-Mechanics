#!/usr/bin/env python3
"""
Morse–Bott Theory Generator (pure mathematics)
Critical manifold schematic and Hessian on normal directions.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_morse_bott_theory() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) f(x,y) = x^2 with critical manifold {x=0}
    ax1.set_title("Morse–Bott: f(x,y)=x^2 (critical manifold x=0)", fontsize=14, weight='bold')
    y = np.linspace(-2, 2, 200)
    x0 = np.zeros_like(y)
    ax1.plot(x0, y, 'r-', lw=3, label='critical manifold')
    for x in [-1.5, -1.0, 1.0, 1.5]:
        ax1.plot([x]*len(y), y, 'k:', alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2) Hessian in normal directions (schematic positive-definite)
    ax2.set_title("Hessian on normals (schematic)", fontsize=14, weight='bold')
    lambdas = [1, 1, 1]
    ax2.bar(['λ1','λ2','λ3'], lambdas, color='#dfd')
    ax2.set_ylim(0, 1.5)
    ax2.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Morse–Bott Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/morse_bott_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "morse_bott_theory"}


if __name__ == "__main__":
    res = generate_morse_bott_theory()
    print(f"Generated: {res['file']}")
