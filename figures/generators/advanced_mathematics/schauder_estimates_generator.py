#!/usr/bin/env python3
"""
Schauder Estimates Generator (pure mathematics)
C^{k,α} norms and elliptic operator regularity schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_schauder_estimates() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Hölder seminorm [u]_{C^{0,α}}
    ax1.set_title(r"Hölder seminorm [u]_{C^{0,α}} (schematic)", fontsize=14, weight='bold')
    x = np.linspace(0, 1, 200)
    alpha = 0.6
    u = x**alpha
    ax1.plot(x, u, lw=2)
    ax1.text(0.6, 0.6**alpha, r"[u]_{C^{0,α}} = sup_{x\ne y} |u(x)-u(y)|/|x-y|^α", fontsize=10)
    ax1.set_xlabel('x')
    ax1.set_ylabel('u(x)')
    ax1.grid(True, alpha=0.3)

    # 2) Elliptic regularity schematic: ||u||_{C^{2,α}} ≤ C(||Lu||_{C^{0,α}} + ||u||_{C^0})
    ax2.set_title(r"Schauder: ||u||_{C^{2,α}} ≤ C(||Lu||_{C^{0,α}} + ||u||_{C^0})", fontsize=14, weight='bold')
    norms = ['||u||_{C^0}', '||Lu||_{C^{0,α}}', '||u||_{C^{2,α}}']
    vals = [1.0, 0.6, 1.8]
    ax2.bar(norms, vals, color=['#cfe', '#ecf', '#fec'])
    ax2.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Schauder Estimates (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/schauder_estimates.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "schauder_estimates"}


if __name__ == "__main__":
    res = generate_schauder_estimates()
    print(f"Generated: {res['file']}")
