#!/usr/bin/env python3
"""
Hardy–Littlewood Maximal Inequality Generator (pure mathematics)
Maximal function M f and weak-(1,1) schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def maximal_function_1d(x: np.ndarray, f: np.ndarray, radii: np.ndarray) -> np.ndarray:
    M = np.zeros_like(f)
    n = len(x)
    for i in range(n):
        vals = []
        for r in radii:
            # interval [x[i]-r, x[i]+r]
            left = x[i] - r
            right = x[i] + r
            mask = (x >= left) & (x <= right)
            if np.any(mask):
                vals.append(np.max(np.abs(f[mask])))
        M[i] = max(vals) if vals else np.abs(f[i])
    return M


def generate_hardy_littlewood_maximal() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) f and M f (schematic)
    ax1.set_title("Maximal function M f (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-3, 3, 600)
    f = np.sin(2*x) * np.exp(-0.2*x**2)
    radii = np.linspace(0.05, 0.6, 12)
    M = maximal_function_1d(x, f, radii)
    ax1.plot(x, f, 'k-', lw=2, label='f')
    ax1.plot(x, M, 'r--', lw=2, label='M f')
    ax1.set_xlabel('x')
    ax1.set_ylabel('value')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) Weak-(1,1) schematic: λ vs measure{|Mf|>λ}
    ax2.set_title("Weak-(1,1) bound (schematic)", fontsize=14, weight='bold')
    lam = np.linspace(0.1, 1.5, 50)
    # schematic  C||f||_1 / λ behavior
    L1 = np.trapz(np.abs(f), x)
    C = 3.0
    measure = C*L1/lam
    ax2.loglog(lam, measure, 'o-', lw=2)
    ax2.set_xlabel('λ')
    ax2.set_ylabel('measure{|Mf|>λ}')
    ax2.grid(True, which='both', alpha=0.3)

    fig.suptitle("Hardy–Littlewood Maximal Inequality (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/hardy_littlewood_maximal.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "hardy_littlewood_maximal"}


if __name__ == "__main__":
    res = generate_hardy_littlewood_maximal()
    print(f"Generated: {res['file']}")
