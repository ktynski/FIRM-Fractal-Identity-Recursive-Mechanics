#!/usr/bin/env python3
"""
Sobolev Sharp Embeddings Generator (pure mathematics)
Critical exponent p* and borderline cases schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_sobolev_sharp_embeddings() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title(r"Sharp embedding: W^{1,p}(ℝ^n) → L^{p*}(ℝ^n), p* = np/(n-p)", fontsize=14, weight='bold')
    p = np.linspace(1.1, 3.0, 200)
    n = 3.0
    pstar = n*p/(n-p)
    ax.plot(p, pstar, lw=2)
    ax.axvline(3, color='r', linestyle='--', label='p=n (borderline)')
    ax.set_xlabel('p')
    ax.set_ylabel('p*')
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.suptitle("Sobolev Sharp Embeddings (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/sobolev_sharp_embeddings.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "sobolev_sharp_embeddings"}


if __name__ == "__main__":
    res = generate_sobolev_sharp_embeddings()
    print(f"Generated: {res['file']}")
