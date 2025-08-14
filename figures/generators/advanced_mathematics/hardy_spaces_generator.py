#!/usr/bin/env python3
"""
Hardy Spaces Generator (pure mathematics)
Boundary values on unit circle, Poisson integral, and H^p nesting.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_hardy_spaces() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Unit circle and boundary function f(e^{iθ})
    ax1.set_title("Boundary data on unit circle", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 400)
    z = np.exp(1j*theta)
    f = 1 + 0.6*np.cos(3*theta)
    ax1.plot(np.real(z), np.imag(z), 'k-', lw=2)
    ax1.scatter(np.real(z), np.imag(z), c=f, cmap='viridis', s=4)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 2) Poisson integral radial reconstruction P_r * f
    ax2.set_title("Poisson integral P_r*f (schematic)", fontsize=14, weight='bold')
    r = np.linspace(0.1, 0.95, 6)
    for rv in r:
        g = 1 + 0.6*(rv**3)*np.cos(3*theta)
        ax2.plot(theta, g, lw=1.5)
    ax2.set_xlabel('θ')
    ax2.set_ylabel('P_r*f')
    ax2.grid(True, alpha=0.3)

    # 3) H^p nesting H^p ⊂ H^q for p ≤ q
    ax3.set_title("H^p nesting (schematic)", fontsize=14, weight='bold')
    p_vals = np.array([1, 2, 3, 4])
    vals = p_vals  # schematic sizes
    ax3.bar(p_vals, vals)
    ax3.set_xlabel('p')
    ax3.set_ylabel('size (schematic)')
    ax3.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Hardy Spaces (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/hardy_spaces.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "hardy_spaces"}


if __name__ == "__main__":
    res = generate_hardy_spaces()
    print(f"Generated: {res['file']}")
