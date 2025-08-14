#!/usr/bin/env python3
"""
Optimal Transport Generator (pure mathematics)
Wasserstein-2 geodesic between 1D densities (schematic).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_optimal_transport() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(12, 5))

    x = np.linspace(-3, 3, 400)
    mu = np.exp(-(x+1.0)**2)
    mu /= np.trapz(mu, x)
    nu = np.exp(-(x-1.0)**2/0.5)
    nu /= np.trapz(nu, x)

    # Displacement interpolation ρ_t = ((1-t)Id + tT)_# μ (schematic as convex combo)
    ts = [0.0, 0.25, 0.5, 0.75, 1.0]
    for t in ts:
        rho_t = (1-t)*mu + t*nu  # schematic; true W2 uses monotone transport
        ax.plot(x, rho_t, lw=2, alpha=0.7)
    ax.legend([f"t={t:.2f}" for t in ts])
    ax.set_xlabel('x')
    ax.set_ylabel('density')
    ax.grid(True, alpha=0.3)
    ax.set_title("Optimal Transport: Wasserstein geodesic (schematic)")

    fig.suptitle("Optimal Transport (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/optimal_transport.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "optimal_transport"}


if __name__ == "__main__":
    res = generate_optimal_transport()
    print(f"Generated: {res['file']}")
