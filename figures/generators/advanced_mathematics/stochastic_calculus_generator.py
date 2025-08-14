#!/usr/bin/env python3
"""
Stochastic Calculus Generator (pure mathematics)
Brownian motion sample paths and Ito vs Stratonovich drift schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def brownian(n=1000, dt=0.001, seed=0):
    rng = np.random.default_rng(seed)
    dW = np.sqrt(dt) * rng.standard_normal(size=n)
    W = np.cumsum(dW)
    t = np.linspace(0, n*dt, n)
    return t, W


def generate_stochastic_calculus() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Brownian motion sample paths
    ax1.set_title("Brownian motion sample paths", fontsize=14, weight='bold')
    for s in [0, 1, 2]:
        t, W = brownian(n=2000, dt=0.001, seed=s)
        ax1.plot(t, W, lw=1)
    ax1.set_xlabel('t')
    ax1.set_ylabel('W_t')
    ax1.grid(True, alpha=0.3)

    # 2) Ito vs Stratonovich schematic drift comparison
    ax2.set_title("Itô vs Stratonovich (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 1, 200)
    ito = 0.3*t
    strat = 0.3*t + 0.5*0.2*t  # schematic correction term
    ax2.plot(t, ito, lw=2, label='Itô drift')
    ax2.plot(t, strat, lw=2, label='Stratonovich drift')
    ax2.set_xlabel('t')
    ax2.set_ylabel('drift')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Stochastic Calculus (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/stochastic_calculus.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "stochastic_calculus"}


if __name__ == "__main__":
    res = generate_stochastic_calculus()
    print(f"Generated: {res['file']}")
