#!/usr/bin/env python3
"""
Riemann Surfaces and Teichmüller Theory Generator (pure mathematics)
Fundamental polygon, periods, and moduli/Teichmüller schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_riemann_surfaces_teichmueller() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Genus 2 fundamental polygon (octagon with edge identifications)
    ax1.set_title("Genus 2 Fundamental Polygon (schematic)", fontsize=14, weight='bold')
    angles = np.linspace(0, 2*np.pi, 9)[:-1]
    R = 1.0
    xs = R*np.cos(angles)
    ys = R*np.sin(angles)
    ax1.plot(np.r_[xs, xs[0]], np.r_[ys, ys[0]], lw=2)
    for i, (x, y) in enumerate(zip(xs, ys)):
        ax1.text(x*1.1, y*1.1, chr(65+i), fontsize=9)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 2) Period matrix schematic (symmetric with positive definite imaginary part)
    ax2.set_title("Period Matrix Ω (schematic)", fontsize=14, weight='bold')
    n = 2
    real = np.array([[0.2, 0.05], [0.05, 0.3]])
    imag = np.array([[1.1, 0.2], [0.2, 0.9]])
    mat = real + 1j*imag
    im = ax2.imshow(np.imag(mat), cmap='viridis', vmin=0, vmax=1.2)
    for i in range(n):
        for j in range(n):
            ax2.text(j, i, f"{np.imag(mat)[i,j]:.2f}", ha='center', va='center', color='w', fontsize=10)
    ax2.set_xticks(range(n))
    ax2.set_yticks(range(n))
    ax2.set_xlabel("columns")
    ax2.set_ylabel("rows")
    plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04, label='Im Ω')

    # 3) Teichmüller/Moduli schematic: dimension 3g-3 for g≥2
    ax3.set_title("Moduli Dimension dim M_g = 3g-3 (g≥2)", fontsize=14, weight='bold')
    g = np.arange(2, 9)
    dim = 3*g - 3
    ax3.plot(g, dim, 'o-', lw=2)
    ax3.set_xlabel('genus g')
    ax3.set_ylabel('dim M_g')
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Riemann Surfaces and Teichmüller Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/riemann_surfaces_teichmueller.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "riemann_surfaces_teichmueller"}


if __name__ == "__main__":
    res = generate_riemann_surfaces_teichmueller()
    print(f"Generated: {res['file']}")
