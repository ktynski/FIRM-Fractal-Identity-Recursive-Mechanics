#!/usr/bin/env python3
"""
Ricci Flow Generator (pure mathematics)
Metric smoothing schematic and neckpinch cartoon.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_ricci_flow() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Metric smoothing: contour lines becoming rounder
    ax1.set_title("Ricci flow smoothing (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 400)
    r0 = 1 + 0.3*np.cos(3*theta)
    r1 = 1 + 0.1*np.cos(3*theta)
    ax1.plot(r0*np.cos(theta), r0*np.sin(theta), 'k-', lw=2, label='t=0')
    ax1.plot(r1*np.cos(theta), r1*np.sin(theta), 'r--', lw=2, label='t>0')
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.legend()

    # 2) Neckpinch cartoon
    ax2.set_title("Neckpinch (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 400)
    y0 = 1/(1 + x**2)
    y1 = 1/(1 + (1.5*x)**2)
    ax2.plot(x, y0, 'k-', lw=2, label='t=0')
    ax2.plot(x, y1, 'r--', lw=2, label='t>0')
    ax2.set_xlabel('x')
    ax2.set_ylabel('profile')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    fig.suptitle("Ricci Flow (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/ricci_flow.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "ricci_flow"}


if __name__ == "__main__":
    res = generate_ricci_flow()
    print(f"Generated: {res['file']}")
