#!/usr/bin/env python3
"""
Complex Analysis and SCV Generator (pure mathematics)
Conformal maps, Cauchy-Riemann heatmap, and contour integral visualization.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_complex_analysis_scv() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Conformal map: Möbius map (z-1)/(z+1)
    ax1.set_title("Conformal Map: w = (z-1)/(z+1)", fontsize=14, weight="bold")
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    W = (Z - 1) / (Z + 1 + 1e-6)  # avoid division by 0
    ax1.contour(np.real(W), np.imag(W), np.real(W), levels=10, colors='blue', alpha=0.4)
    ax1.contour(np.real(W), np.imag(W), np.imag(W), levels=10, colors='red', alpha=0.4)
    ax1.set_xlabel("Re w")
    ax1.set_ylabel("Im w")
    ax1.grid(True, alpha=0.3)

    # 2) Cauchy-Riemann equations heatmap for f(x+iy) = x^2 - y^2 + i(2xy)
    ax2.set_title("Cauchy-Riemann residual heatmap", fontsize=14, weight="bold")
    u = X**2 - Y**2
    v = 2*X*Y
    ux, uy = np.gradient(u, x, y)
    vx, vy = np.gradient(v, x, y)
    cr_residual = np.abs(ux - vy) + np.abs(uy + vx)
    im = ax2.imshow(cr_residual, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', cmap='magma')
    plt.colorbar(im, ax=ax2, label='|CR residual|')
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")

    # 3) Contour integral path around unit circle for f(z)=1/(z-0.5)
    ax3.set_title("Contour Integral on |z|=1: f(z)=1/(z-0.5)", fontsize=14, weight="bold")
    t = np.linspace(0, 2*np.pi, 300)
    zc = np.exp(1j*t)
    ax3.plot(np.real(zc), np.imag(zc), 'k-', lw=2)
    ax3.scatter([0.5], [0], c='red', s=80, label='pole at 0.5')
    ax3.set_aspect('equal')
    ax3.set_xlabel("Re z")
    ax3.set_ylabel("Im z")
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4) Several complex variables: polydisk boundary sampling
    ax4.set_title("SCV: Polydisk samples in C^2", fontsize=14, weight="bold")
    angles = np.linspace(0, 2*np.pi, 36)
    z1 = np.exp(1j*angles)
    z2 = np.exp(1j*(angles + 0.4))
    ax4.scatter(np.real(z1), np.real(z2), c=angles, cmap='viridis')
    ax4.set_xlabel("Re z1 on S^1")
    ax4.set_ylabel("Re z2 on S^1")
    ax4.grid(True, alpha=0.3)

    fig.suptitle("Complex Analysis and Several Complex Variables (pure mathematics)", fontsize=16, weight="bold")
    plt.tight_layout()
    out = Path("figures/outputs/complex_analysis_scv.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "complex_analysis_scv"}


if __name__ == "__main__":
    res = generate_complex_analysis_scv()
    print(f"Generated: {res['file']}")
