#!/usr/bin/env python3
"""
Lott–Sturm–Villani Curvature Generator (pure mathematics)
CD(K,N) displacement convexity schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_lott_sturm_villani_curvature() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("CD(K,N) displacement convexity (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 1, 200)
    U0 = 1 + 0.5*(1-t)
    U1 = 1 + 0.5*t
    convex = np.maximum(U0, U1) - 0.1*t*(1-t)  # convex below linear interpolation
    ax.plot(t, U0, lw=2, label='U(ρ_0)')
    ax.plot(t, U1, lw=2, label='U(ρ_1)')
    ax.plot(t, convex, 'k--', lw=2, label='U(ρ_t) convex')
    ax.set_xlabel('t along W2-geodesic')
    ax.set_ylabel('U(ρ_t)')
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.suptitle("Lott–Sturm–Villani Curvature (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/lott_sturm_villani_curvature.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "lott_sturm_villani_curvature"}


if __name__ == "__main__":
    res = generate_lott_sturm_villani_curvature()
    print(f"Generated: {res['file']}")
