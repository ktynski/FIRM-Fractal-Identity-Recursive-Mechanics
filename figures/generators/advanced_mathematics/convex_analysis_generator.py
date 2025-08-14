#!/usr/bin/env python3
"""
Convex Analysis Generator (pure mathematics)
Epigraph, convex/strongly-convex functions, and subgradient schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_convex_analysis() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Convex vs strongly convex
    ax1.set_title("Convex vs strongly convex", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 400)
    f = np.abs(x) + 0.2
    g = 0.5*x**2 + 0.1
    ax1.plot(x, f, lw=2, label='convex')
    ax1.plot(x, g, lw=2, label='strongly convex')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2) Epigraph epi(f)
    ax2.set_title("Epigraph epi(f)", fontsize=14, weight='bold')
    X, Y = np.meshgrid(np.linspace(-2,2,200), np.linspace(0,3,200))
    F = np.abs(X) + 0.2
    region = Y >= F
    ax2.imshow(region.astype(float), extent=[-2,2,0,3], origin='lower', cmap='Blues', alpha=0.6, aspect='auto')
    ax2.plot(x, f, 'k-', lw=2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True, alpha=0.3)

    # 3) Subgradient at x0
    ax3.set_title("Subgradient ∂f(x₀)", fontsize=14, weight='bold')
    x0 = 0.5
    f0 = np.abs(x0) + 0.2
    ax3.plot(x, f, 'k-', lw=2)
    # subgradient slope s ∈ [-1,1] for |x| at 0; here at 0.5 slope = sign = 1
    s = np.sign(x0)
    tangent = f0 + s*(x - x0)
    ax3.plot(x, tangent, 'r--', lw=2)
    ax3.scatter([x0],[f0], s=80, c='tomato')
    ax3.set_xlabel('x')
    ax3.set_ylabel('f(x)')
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Convex Analysis (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/convex_analysis.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "convex_analysis"}


if __name__ == "__main__":
    res = generate_convex_analysis()
    print(f"Generated: {res['file']}")
