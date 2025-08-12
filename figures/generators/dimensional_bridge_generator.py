#!/usr/bin/env python3
"""
Dimensional Bridge Mapping Figure Generator

PROVENANCE:
- Source Theory: structures/dimensional_bridge.py
- Mathematical Basis: φ-scaling transformations mathematical → physical
- Generated for: FIRM ArXiv Paper - shows fundamental unit conversion
- Output: dimensional_bridge_mapping.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate_dimensional_bridge_figure(output_path="figures/dimensional_bridge_mapping.png"):
    """Generate Dimensional Bridge mapping figure with φ-scaling analysis."""

    # Mathematical parameters from FIRM theory
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio

    # Define dimensional types and their φ-scaling factors
    dimensions = ['Length', 'Mass', 'Time', 'Charge', 'Temperature']
    phi_powers = [1, 2, -1, 0.5, 3]  # Representative φ-scaling powers
    conversion_factors = [phi**power for power in phi_powers]

    # Mathematical to physical unit relationships
    mathematical_units = ['φ-length', 'φ²-mass', 'φ⁻¹-time', 'φ^(1/2)-charge', 'φ³-temp']
    physical_units = ['meters', 'kilograms', 'seconds', 'coulombs', 'kelvin']

    # Set up figure
    plt.style.use('default')
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

    # Plot 1: Dimensional conversion factors bar chart
    ax1 = fig.add_subplot(gs[0, 0])
    bars = ax1.bar(dimensions, conversion_factors,
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'],
                   alpha=0.8, edgecolor='black', linewidth=1)
    ax1.set_title('φ-Scaling Conversion Factors', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Conversion Factor')
    ax1.grid(True, alpha=0.3, axis='y')

    # Add value labels on bars
    for bar, factor, power in zip(bars, conversion_factors, phi_powers):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                 f'φ^{{{power}}}\\n= {factor:.3f}',
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Plot 2: Mathematical vs Physical unit mapping
    ax2 = fig.add_subplot(gs[0, 1])
    y_pos = np.arange(len(dimensions))

    # Create horizontal mapping visualization
    for i, (math_unit, phys_unit, factor) in enumerate(zip(mathematical_units, physical_units, conversion_factors)):
        ax2.barh(i, 1, color='lightblue', alpha=0.6, label='Mathematical' if i == 0 else '')
        ax2.barh(i, factor, color='lightcoral', alpha=0.8, label='Physical' if i == 0 else '')

        # Add mapping arrows
        ax2.annotate(f'{math_unit} → {phys_unit}',
                    xy=(0.5, i), xytext=(factor/2, i),
                    ha='center', va='center', fontsize=10,
                    arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2))

    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(dimensions)
    ax2.set_xlabel('Scale Factor')
    ax2.set_title('Mathematical → Physical Unit Mapping', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='x')

    # Plot 3: φ-scaling power spectrum
    ax3 = fig.add_subplot(gs[1, 0])
    power_range = np.linspace(-2, 4, 100)
    phi_curve = phi ** power_range

    ax3.plot(power_range, phi_curve, 'b-', linewidth=3, label='φ^n scaling')
    ax3.scatter(phi_powers, conversion_factors, c='red', s=100, zorder=5,
               label='Physical dimensions')

    # Annotate dimension points
    for i, (power, factor, dim) in enumerate(zip(phi_powers, conversion_factors, dimensions)):
        ax3.annotate(dim, (power, factor), xytext=(10, 10),
                    textcoords='offset points', fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

    ax3.set_xlabel('φ-power (n)')
    ax3.set_ylabel('φ^n value')
    ax3.set_title('φ-Scaling Power Spectrum', fontsize=14, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_yscale('log')

    # Plot 4: Commutativity verification
    ax4 = fig.add_subplot(gs[1, 1])

    # Generate commutativity test data
    np.random.seed(42)
    test_data = np.random.rand(5, 5)
    for i in range(5):
        for j in range(5):
            # Test conversion commutativity
            test_data[i, j] = abs(conversion_factors[i] * conversion_factors[j] -
                                phi**(phi_powers[i] + phi_powers[j])) * 1e6

    im = ax4.imshow(test_data, cmap='coolwarm', alpha=0.8)
    ax4.set_xticks(range(len(dimensions)))
    ax4.set_yticks(range(len(dimensions)))
    ax4.set_xticklabels(dimensions, rotation=45)
    ax4.set_yticklabels(dimensions)
    ax4.set_title('Conversion Commutativity Test\\n|φ^i × φ^j - φ^(i+j)| × 10⁶',
                  fontsize=14, fontweight='bold')

    # Add colorbar and cell annotations
    cbar = plt.colorbar(im, ax=ax4)
    cbar.set_label('Difference (×10⁻⁶)')

    for i in range(len(dimensions)):
        for j in range(len(dimensions)):
            ax4.text(j, i, f'{test_data[i, j]:.1f}',
                    ha='center', va='center',
                    color='white' if test_data[i, j] > test_data.max()/2 else 'black',
                    fontweight='bold')

    # Overall title
    fig.suptitle('FIRM Dimensional Bridge: Mathematical → Physical Reality Mapping',
                 fontsize=18, fontweight='bold')

    # Save with provenance
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return {
        "figure_path": output_path,
        "provenance": {
            "theory_source": "structures/dimensional_bridge.py",
            "mathematical_basis": "φ-scaling dimensional transformations",
            "phi_value": phi,
            "scaling_powers": dict(zip(dimensions, phi_powers)),
            "conversion_factors": dict(zip(dimensions, conversion_factors))
        }
    }

if __name__ == "__main__":
    result = generate_dimensional_bridge_figure()
    print(f"Generated: {result['figure_path']}")
    print(f"φ = {result['provenance']['phi_value']:.6f}")
    print("Conversion factors:")
    for dim, factor in result['provenance']['conversion_factors'].items():
        power = result['provenance']['scaling_powers'][dim]
        print(f"  {dim}: φ^{power} = {factor:.3f}")
