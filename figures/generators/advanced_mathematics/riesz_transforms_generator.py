#!/usr/bin/env python3
"""
Riesz Transforms Generator (pure mathematics)
Fourier multiplier schematic and L^p boundedness bars.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_riesz_transforms() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Multiplier m_j(ξ) = i ξ_j/|ξ|
    ax1.set_title("Riesz multiplier m(ξ) = i ξ_j/|ξ| (schematic)", fontsize=14, weight='bold')
    xi = np.linspace(-5, 5, 400)
    m = xi / (np.sqrt(xi**2 + 1e-9))
    ax1.plot(xi, m, lw=2)
    ax1.set_xlabel('ξ')
    ax1.set_ylabel('Re m(ξ) (schematic)')
    ax1.grid(True, alpha=0.3)

    # 2) L^p boundedness (schematic constant vs p)
    ax2.set_title("L^p boundedness (schematic)", fontsize=14, weight='bold')
    p = np.array([1.2, 1.5, 2.0, 3.0, 4.0])
    const = np.array([2.2, 1.6, 1.2, 1.3, 1.6])
    ax2.bar([str(v) for v in p], const, color='#cfe')
    ax2.set_xlabel('p')
    ax2.set_ylabel('||R||_{L^p→L^p} (schematic)')
    ax2.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Riesz Transforms (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/riesz_transforms.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "riesz_transforms"}


if __name__ == "__main__":
    res = generate_riesz_transforms()
    print(f"Generated: {res['file']}")
