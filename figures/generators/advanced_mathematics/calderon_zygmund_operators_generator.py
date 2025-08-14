#!/usr/bin/env python3
"""
Calderón–Zygmund Operators Generator (pure mathematics)
Singular kernel schematic and L^p boundedness bars.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_calderon_zygmund_operators() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Kernel K(x) ~ 1/x (Hilbert transform schematic)
    ax1.set_title("Singular kernel K(x) ~ 1/x (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-3, 3, 600)
    K = 1/(x + 1e-6)
    ax1.plot(x, K, 'k-', lw=1)
    ax1.axvline(0, color='r', linestyle='--', lw=2, label='singularity')
    ax1.set_xlabel('x')
    ax1.set_ylabel('K(x)')
    ax1.set_ylim(-10, 10)
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) L^p boundedness schematic
    ax2.set_title("L^p boundedness (schematic)", fontsize=14, weight='bold')
    p = np.array([1.1, 1.5, 2.0, 3.0, 4.0])
    bound = np.array([2.0, 1.5, 1.2, 1.4, 1.8])
    ax2.bar([str(v) for v in p], bound, color='#cfe')
    ax2.set_xlabel('p')
    ax2.set_ylabel('||T||_{L^p→L^p} (schematic)')
    ax2.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Calderón–Zygmund Operators (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/calderon_zygmund_operators.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "calderon_zygmund_operators"}


if __name__ == "__main__":
    res = generate_calderon_zygmund_operators()
    print(f"Generated: {res['file']}")
