#!/usr/bin/env python3
"""
Geometric Group Growth Generator (pure mathematics)
Polynomial vs exponential growth and Gromov theorem schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_geometric_group_growth() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("Group growth: polynomial vs exponential (schematic)", fontsize=14, weight='bold')
    n = np.arange(1, 20)
    poly = n**3
    expo = 2**n
    ax.semilogy(n, poly, 'o-', lw=2, label='polynomial')
    ax.semilogy(n, expo, 'o-', lw=2, label='exponential')
    ax.set_xlabel('radius n')
    ax.set_ylabel('|B(n)| (log scale)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()

    fig.suptitle("Geometric Group Growth (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/geometric_group_growth.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "geometric_group_growth"}


if __name__ == "__main__":
    res = generate_geometric_group_growth()
    print(f"Generated: {res['file']}")
