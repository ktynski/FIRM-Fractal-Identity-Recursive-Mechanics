#!/usr/bin/env python3
"""
Operator Algebras Generator (pure mathematics)
Spectra heatmap, C*-algebra norms, and von Neumann factors schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_operator_algebras() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Spectrum of a normal operator (schematic): eigenvalue cloud
    ax1.set_title("Spectral Set σ(T) (schematic)", fontsize=14, weight='bold')
    rng = np.random.default_rng(42)
    pts = 0.6*rng.standard_normal((200, 2))
    ax1.scatter(pts[:,0], pts[:,1], s=12, c=np.hypot(pts[:,0], pts[:,1]), cmap='plasma', alpha=0.8)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.2)
    ax1.set_xlabel('Re λ')
    ax1.set_ylabel('Im λ')

    # 2) C*-norm vs operator norm (schematic curves)
    ax2.set_title("Norms: ||·|| and C*-identity ||T*T|| = ||T||²", fontsize=14, weight='bold')
    t = np.linspace(0, 2, 200)
    op_norm = np.sqrt(t)
    cstar_norm = t
    ax2.plot(t, op_norm, label='||T||', lw=2)
    ax2.plot(t, cstar_norm, label='||T*T||', lw=2)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlabel('t (schematic)')

    # 3) Von Neumann factors types (I, II, III)
    ax3.set_title("Von Neumann Factors (schematic)", fontsize=14, weight='bold')
    classes = ['Type I', 'Type II₁', 'Type II_∞', 'Type III']
    vals = [3, 4, 2, 1]
    ax3.bar(classes, vals, color=['#8cc', '#c8c', '#cc8', '#8c8'])
    ax3.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Operator Algebras (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/operator_algebras.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "operator_algebras"}


if __name__ == "__main__":
    res = generate_operator_algebras()
    print(f"Generated: {res['file']}")
