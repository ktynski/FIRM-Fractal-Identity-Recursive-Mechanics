#!/usr/bin/env python3
"""
Symplectic Geometry Generator (pure mathematics)
ω-level sets, moment map image, and Hamiltonian flow schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_symplectic_geometry() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) ω = dx ∧ dy level sets (visualize scalar curl of a canonical symplectic vector field)
    ax1.set_title(r"Symplectic form ω on ℝ² (schematic)", fontsize=14, weight='bold')
    x = np.linspace(-2, 2, 200)
    y = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(x, y)
    # Canonical rotation field (Hamiltonian for H = (x^2 + y^2)/2):
    U = -Y  # x' = -∂H/∂y
    V = X   # y' =  ∂H/∂x
    # Scalar curl in 2D: ∂V/∂x - ∂U/∂y
    dV_dy, dV_dx = np.gradient(V, y, x)
    dU_dy, dU_dx = np.gradient(U, y, x)
    curl = dV_dx - dU_dy  # shape (len(y), len(x))
    im = ax1.imshow(curl, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', cmap='coolwarm')
    plt.colorbar(im, ax=ax1, label='∂V/∂x − ∂U/∂y (scalar curl)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    # 2) Moment map image for S¹ action on S² (schematic: height function)
    ax2.set_title("Moment Map μ: S² → ℝ (height)", fontsize=14, weight='bold')
    phi = np.linspace(0, np.pi, 100)
    mu = np.cos(phi)
    ax2.plot(phi, mu, lw=2)
    ax2.set_xlabel('φ (colatitude)')
    ax2.set_ylabel('μ')
    ax2.grid(True, alpha=0.3)

    # 3) Hamiltonian flow lines for H = (x² + y²)/2
    ax3.set_title("Hamiltonian Flow for H = (x² + y²)/2", fontsize=14, weight='bold')
    r = np.linspace(0.2, 1.8, 5)
    t = np.linspace(0, 2*np.pi, 400)
    for R in r:
        ax3.plot(R*np.cos(t), R*np.sin(t), lw=2)
    ax3.set_aspect('equal')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Symplectic Geometry (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/symplectic_geometry.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "symplectic_geometry"}


if __name__ == "__main__":
    res = generate_symplectic_geometry()
    print(f"Generated: {res['file']}")
