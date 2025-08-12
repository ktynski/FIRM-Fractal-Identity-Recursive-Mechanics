#!/usr/bin/env python3
"""
φ-Recursion Rate Verification Figure Generator

PROVENANCE:
- Source Theory: foundation/operators/phi_recursion.py
- Mathematical Basis: Exponential convergence rate -2 ln φ verification
- Generated for: FIRM ArXiv Paper - validates φ-recursive scaling foundation
- Output: phi_recursion_rate_verification.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate_phi_recursion_rate_figure(output_path="figures/phi_recursion_rate_verification.png"):
    """Generate φ-recursion rate verification figure with mathematical validation."""

    # Mathematical parameters from FIRM theory
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    expected_slope = -2 * np.log(phi)  # Theoretical convergence rate

    # Simulate φ-recursion: x_{n+1} = 1 + 1/x_n
    def phi_recursion_step(x):
        return 1 + 1/x if x != 0 else 1

    # Generate convergence data
    initial_value = 1.7
    max_iterations = 80
    values = [initial_value]
    current = initial_value

    for i in range(max_iterations):
        current = phi_recursion_step(current)
        values.append(current)

    # Calculate errors from φ
    errors = np.array([abs(v - phi) for v in values[1:]])
    n = np.arange(len(errors))

    # Filter out zero errors and fit slope
    valid_errors = errors[errors > 1e-15]
    valid_n = n[:len(valid_errors)]

    measured_slope = 0
    if len(valid_n) > 4:
        half_point = len(valid_n) // 2
        log_errors = np.log(valid_errors)
        coeffs = np.polyfit(valid_n[half_point:], log_errors[half_point:], 1)
        measured_slope = coeffs[0]

    # Set up figure
    plt.style.use('default')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Error convergence (log scale)
    if len(valid_errors) > 0:
        ax1.semilogy(valid_n, valid_errors, marker='o', linestyle='-',
                     color='#2E8B57', linewidth=2, markersize=4, alpha=0.8,
                     label='φ-recursion error')
    ax1.set_title('φ-Recursion Error Convergence', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Iteration n')
    ax1.set_ylabel('|xₙ - φ|')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Plot 2: Slope verification
    if len(valid_n) > 4:
        log_errors = np.log(valid_errors)
        ax2.plot(valid_n, log_errors, 'o', alpha=0.7, color='#4682B4',
                 markersize=4, label='log error')
        half_point = len(valid_n) // 2
        ax2.plot(valid_n[half_point:], np.polyval(coeffs, valid_n[half_point:]),
                 'r--', linewidth=2, label=f'fit slope = {measured_slope:.3f}')

    ax2.axhline(0, color='black', linewidth=0.5, alpha=0.5)
    ax2.set_title(f'Expected slope ≈ {expected_slope:.3f} = -2 ln φ',
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('Iteration n')
    ax2.set_ylabel('ln |error|')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Add parameter box
    textstr = f'φ = {phi:.6f}\\n-2 ln φ = {expected_slope:.3f}\\nMeasured slope = {measured_slope:.3f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax2.text(0.05, 0.95, textstr, transform=ax2.transAxes, fontsize=10,
             verticalalignment='top', bbox=props)

    # Overall title
    fig.suptitle('φ-Recursion Rate Verification: Exponential Convergence Analysis',
                 fontsize=16, fontweight='bold')
    fig.tight_layout()

    # Save with provenance
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return {
        "figure_path": output_path,
        "provenance": {
            "theory_source": "foundation/operators/phi_recursion.py",
            "mathematical_basis": "Exponential convergence rate -2 ln φ",
            "phi_value": phi,
            "expected_slope": expected_slope,
            "measured_slope": measured_slope,
            "slope_difference": abs(measured_slope - expected_slope)
        }
    }

if __name__ == "__main__":
    result = generate_phi_recursion_rate_figure()
    print(f"Generated: {result['figure_path']}")
    print(f"φ = {result['provenance']['phi_value']:.6f}")
    print(f"Theoretical slope: {result['provenance']['expected_slope']:.6f}")
    print(f"Measured slope: {result['provenance']['measured_slope']:.6f}")
    print(f"Difference: {result['provenance']['slope_difference']:.6f}")
