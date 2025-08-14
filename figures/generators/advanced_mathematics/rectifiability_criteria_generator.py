#!/usr/bin/env python3
"""
Rectifiability Criteria Generator (pure mathematics)
Approximate tangent measure schematic and criteria bars.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_rectifiability_criteria() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Approximate tangent measure schematic
    ax1.set_title("Approximate tangent measure (schematic)", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 200)
    curve = np.column_stack([np.cos(theta) + 0.2*np.cos(5*theta), np.sin(theta)])
    ax1.plot(curve[:,0], curve[:,1], 'k-', lw=2)
    x0 = np.array([1.0, 0.0])
    ax1.scatter([x0[0]],[x0[1]], s=80, c='red')
    ax1.plot([x0[0]-0.5, x0[0]+0.5], [x0[1], x0[1]], 'r--', lw=2)
    ax1.set_aspect('equal')
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-1.5, 1.5)
    ax1.axis('off')

    # 2) Criteria bars (e.g., β-numbers, tangent measures, densities)
    ax2.set_title("Rectifiability criteria (schematic)", fontsize=14, weight='bold')
    labels = ['β-numbers', 'tangent measures', 'densities']
    vals = [1.0, 0.8, 1.2]
    ax2.bar(labels, vals, color=['#eef','#cfe','#bdf'])
    ax2.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Rectifiability Criteria (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/rectifiability_criteria.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "rectifiability_criteria"}


if __name__ == "__main__":
    res = generate_rectifiability_criteria()
    print(f"Generated: {res['file']}")
