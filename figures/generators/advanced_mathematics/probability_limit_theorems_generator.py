#!/usr/bin/env python3
"""
Probability Limit Theorems Generator (pure mathematics)
Law of Large Numbers and Central Limit Theorem convergence (schematic) without SciPy dependency.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def normal_pdf(x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2)


def generate_probability_limit_theorems() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) LLN: sample mean convergence to μ
    ax1.set_title("LLN: sample mean → μ", fontsize=14, weight='bold')
    n = np.arange(1, 201)
    rng = np.random.default_rng(0)
    X = rng.exponential(scale=1.0, size=200)
    sample_mean = np.cumsum(X)/n
    ax1.plot(n, sample_mean, lw=2)
    ax1.axhline(1.0, color='k', linestyle='--', label='μ=1')
    ax1.set_xlabel('n')
    ax1.set_ylabel('sample mean')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2) CLT: normalized sums converge to N(0,1)
    ax2.set_title("CLT: normalized sums → N(0,1)", fontsize=14, weight='bold')
    x = np.linspace(-4, 4, 400)
    for m in [1, 2, 5, 10, 30]:
        Y = rng.standard_exponential(size=10000) - 1  # mean 0, var 1
        # block sums of size m, normalized by sqrt(m)
        blocks = Y[: (len(Y) // m) * m].reshape(-1, m)
        S = blocks.mean(axis=1) * np.sqrt(m)
        density, bins = np.histogram(S, bins=100, range=(-4,4), density=True)
        centers = 0.5*(bins[1:] + bins[:-1])
        ax2.plot(centers, density, alpha=0.6, lw=1, label=f'm={m}')
    ax2.plot(x, normal_pdf(x), 'k--', lw=2, label='N(0,1)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('density')
    ax2.grid(True, alpha=0.3)
    ax2.legend(ncol=2)

    fig.suptitle("Probability Limit Theorems (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/probability_limit_theorems.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "probability_limit_theorems"}


if __name__ == "__main__":
    res = generate_probability_limit_theorems()
    print(f"Generated: {res['file']}")
