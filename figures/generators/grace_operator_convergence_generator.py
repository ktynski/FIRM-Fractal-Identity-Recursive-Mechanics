#!/usr/bin/env python3
"""
Grace Operator Fixed Point Convergence Figure Generator

PROVENANCE:
- Source Theory: foundation/operators/grace_operator.py
- Mathematical Basis: Banach fixed-point theorem convergence analysis
- Generated for: FIRM ArXiv Paper - demonstrates φ-contraction mapping
- Output: grace_operator_fixed_point_convergence.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate_grace_operator_convergence_figure(output_path="figures/grace_operator_fixed_point_convergence.png"):
    """Generate Grace Operator fixed point convergence figure with full provenance."""

    # Mathematical parameters from FIRM theory
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    contraction_ratio = 1 / phi  # Grace Operator contraction ratio

    # Set up figure
    plt.style.use('default')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Convergence analysis for multiple initial conditions
    seeds = [1.0, 2.0, 0.5, -1.0]
    max_iter = 40

    for seed in seeds:
        current = seed
        values = []
        errors = []
        prev = current

        # Grace Operator iteration: x_{n+1} = 1 + (1/φ)(x_n - 1)
        for k in range(1, max_iter + 1):
            current = 1.0 + contraction_ratio * (current - 1.0)
            values.append(current)
            err = abs(current - prev)
            errors.append(err)
            prev = current

        # Plot trajectories and errors
        ax1.plot(values, label=f'x₀={seed}', linewidth=2)
        ax2.semilogy(errors, label=f'x₀={seed}', linewidth=2)

    # Add φ reference line
    ax1.axhline(phi, color='red', linestyle='--', alpha=0.7, label='φ ≈ 1.618')

    # Format axes
    ax1.set_title('Grace Operator Iteration Trajectories', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Value')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.set_title('Convergence Error |xₖ - xₖ₋₁|', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Error (log)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Overall title
    fig.suptitle('FIRM Grace Operator Fixed Point Convergence', fontsize=16, fontweight='bold')
    fig.tight_layout()

    # Save with provenance
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return {
        "figure_path": output_path,
        "provenance": {
            "theory_source": "foundation/operators/grace_operator.py",
            "mathematical_basis": "Banach fixed-point theorem",
            "phi_value": phi,
            "contraction_ratio": contraction_ratio,
            "convergence_rate": f"O(φ^(-n)) ≈ O(0.618^n)"
        }
    }

if __name__ == "__main__":
    result = generate_grace_operator_convergence_figure()
    print(f"Generated: {result['figure_path']}")
    print(f"φ = {result['provenance']['phi_value']:.6f}")
    print(f"Convergence: {result['provenance']['convergence_rate']}")
