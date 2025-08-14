#!/usr/bin/env python3
"""
Random Matrix Theory Generator (pure mathematics)
Wigner matrix eigenvalue histogram vs semicircle law.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def semicircle_pdf(x):
    return (1/(2*np.pi)) * np.sqrt(np.maximum(0, 4 - x**2))


def generate_random_matrix_theory() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Wigner matrix eigenvalues
    ax1.set_title("Wigner eigenvalues (schematic)", fontsize=14, weight='bold')
    rng = np.random.default_rng(5)
    n = 200
    M = rng.standard_normal((n, n))
    W = (M + M.T) / (2*np.sqrt(n))
    eigvals = np.linalg.eigvalsh(W)
    ax1.hist(eigvals, bins=40, density=True, alpha=0.7, color='steelblue')
    x = np.linspace(-2.2, 2.2, 400)
    ax1.plot(x, semicircle_pdf(x), 'k--', lw=2, label='semicircle')
    ax1.legend()
    ax1.set_xlabel('λ')
    ax1.set_ylabel('density')
    ax1.grid(True, alpha=0.3)

    # 2) Empirical CDF vs semicircle CDF (schematic) using sorted eigenvalues
    ax2.set_title("Empirical CDF vs semicircle (schematic)", fontsize=14, weight='bold')
    xs = np.sort(eigvals)
    ecdf = np.arange(1, len(xs)+1) / len(xs)
    ax2.plot(xs, ecdf, lw=2, label='Empirical CDF')
    # semicircle cdf via numerical integral (coarse)
    xx = np.linspace(-2, 2, 300)
    pdf = semicircle_pdf(xx)
    cdf = np.cumsum(pdf) * (xx[1]-xx[0])
    cdf = cdf / cdf[-1]
    ax2.plot(xx, cdf, 'k--', lw=2, label='Semicircle CDF')
    ax2.legend()
    ax2.set_xlabel('λ')
    ax2.set_ylabel('CDF')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("Random Matrix Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/random_matrix_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "random_matrix_theory"}


if __name__ == "__main__":
    res = generate_random_matrix_theory()
    print(f"Generated: {res['file']}")
