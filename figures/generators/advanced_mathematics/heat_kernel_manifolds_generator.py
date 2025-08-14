#!/usr/bin/env python3
"""
Heat Kernel on Manifolds Generator (pure mathematics)
Gaussian bounds p_t(x,y) ~ (4πt)^{-n/2} exp(-d(x,y)^2/4t).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_heat_kernel_manifolds() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("Heat kernel Gaussian bounds (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-3, 3, 400)
    for t in [0.05, 0.1, 0.2, 0.5, 1.0]:
        p = (4*np.pi*t)**(-0.5) * np.exp(-x**2/(4*t))
        ax.plot(x, p, lw=2, label=f't={t}')
    ax.set_xlabel('distance d(x,y)')
    ax.set_ylabel('p_t(x,y)')
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.suptitle("Heat Kernel on Manifolds (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/heat_kernel_manifolds.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "heat_kernel_manifolds"}


if __name__ == "__main__":
    res = generate_heat_kernel_manifolds()
    print(f"Generated: {res['file']}")
