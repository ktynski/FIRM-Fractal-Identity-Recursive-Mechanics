#!/usr/bin/env python3
"""
Inflation Evolution Timeline Figure Generator

PROVENANCE:
- Source Theory: cosmology/inflation_theory.py
- Mathematical Basis: φ-field driven cosmic inflation dynamics
- Generated for: FIRM ArXiv Paper - complete inflation timeline analysis
- Output: inflation_evolution.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate_inflation_evolution_figure(output_path="figures/inflation_evolution.png"):
    """Generate comprehensive inflation evolution timeline figure."""

    # Mathematical parameters from FIRM theory
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio

    # Time evolution parameters (in e-folds)
    time = np.linspace(0, 60, 1000)
    dt = time[1] - time[0]

    # φ-driven inflation field evolution
    phi_field_initial = phi * 2.5  # Initial field value
    phi_field = phi_field_initial * np.exp(-time/20)  # Slow roll evolution

    # Inflation potential V(φ) = (1/2)m²φ²(1 - φ/φ₀)
    m_planck = 1.0  # In Planck units
    V0 = 0.5 * m_planck**2
    phi_0 = phi_field_initial
    inflation_potential = V0 * (phi_field**2) * (1 - phi_field/phi_0)

    # Hubble parameter H = √(V/3M_p²)
    hubble_parameter = np.sqrt(np.maximum(inflation_potential / 3, 1e-10))

    # Scale factor a(t) = exp(∫H dt)
    integrated_hubble = np.cumsum(hubble_parameter) * dt
    scale_factor = np.exp(integrated_hubble)

    # Slow-roll parameters
    dphi_dt = np.gradient(phi_field)
    d2phi_dt2 = np.gradient(dphi_dt)
    epsilon = dphi_dt**2 / (2 * hubble_parameter**2)
    eta = -d2phi_dt2 / (3 * hubble_parameter * dphi_dt + 1e-10)

    # Set up comprehensive figure
    plt.style.use('default')
    fig = plt.figure(figsize=(20, 15))
    gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)

    # Plot 1: φ-field evolution
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(time, phi_field, color='#E74C3C', linewidth=3, label='φ-inflation field')
    ax1.axhline(phi_field_initial * 0.1, color='black', linestyle='--', alpha=0.6, label='End of inflation')
    ax1.set_xlabel('e-folds N')
    ax1.set_ylabel('φ(N)')
    ax1.set_title('φ-Field Evolution', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Inflation potential
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(time, inflation_potential, color='#8E44AD', linewidth=3, label='V(φ)')
    ax2.set_xlabel('e-folds N')
    ax2.set_ylabel('V(φ) (Planck units)')
    ax2.set_title('Inflation Potential Evolution', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')

    # Plot 3: Hubble parameter
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.plot(time, hubble_parameter, color='#3498DB', linewidth=3, label='H(N)')
    ax3.set_xlabel('e-folds N')
    ax3.set_ylabel('H (Planck units)')
    ax3.set_title('Hubble Parameter Evolution', fontsize=14, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_yscale('log')

    # Plot 4: Scale factor
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.semilogy(time, scale_factor, color='#27AE60', linewidth=3, label='a(N)')
    ax4.set_xlabel('e-folds N')
    ax4.set_ylabel('Scale Factor a(N)')
    ax4.set_title('Cosmic Scale Factor', fontsize=14, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Plot 5: Slow-roll parameters
    ax5 = fig.add_subplot(gs[1, 1])
    epsilon_filtered = np.clip(epsilon, 1e-10, 1)
    eta_filtered = np.clip(eta, -10, 10)

    ax5.semilogy(time, epsilon_filtered, color='#F39C12', linewidth=3, label='ε')
    ax5_twin = ax5.twinx()
    ax5_twin.plot(time, eta_filtered, color='#E67E22', linewidth=3, label='η')
    ax5.axhline(1, color='red', linestyle='--', alpha=0.6, label='ε = 1 (end inflation)')
    ax5.set_xlabel('e-folds N')
    ax5.set_ylabel('ε (slow-roll)', color='#F39C12')
    ax5_twin.set_ylabel('η (slow-roll)', color='#E67E22')
    ax5.set_title('Slow-Roll Parameters', fontsize=14, fontweight='bold')
    ax5.legend(loc='upper left')
    ax5_twin.legend(loc='upper right')
    ax5.grid(True, alpha=0.3)

    # Plot 6: φ-potential shape in field space
    ax6 = fig.add_subplot(gs[1, 2])
    field_range = np.linspace(0.1, phi_field_initial * 1.2, 200)
    potential_shape = V0 * (field_range**2) * (1 - field_range/phi_0)
    ax6.plot(field_range, potential_shape, color='#9B59B6', linewidth=3, label='V(φ)')
    ax6.scatter(phi_field[::50], inflation_potential[::50], c=time[::50],
               s=30, cmap='viridis', zorder=5, label='Evolution path')
    ax6.set_xlabel('φ-field value')
    ax6.set_ylabel('Potential V(φ)')
    ax6.set_title('φ-Potential Landscape', fontsize=14, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)

    # Plot 7: Timeline of cosmic phases
    ax7 = fig.add_subplot(gs[2, :])

    # Define phase transitions
    phase_times = [0, 20, 40, 60]
    phase_labels = ['Pre-inflation\\nφ >> φ_c', 'Slow Roll\\nInflation', 'End Inflation\\nφ ~ φ_c', 'Reheating\\nφ → 0']
    phase_colors = ['#E74C3C', '#F39C12', '#27AE60', '#3498DB']

    # Create phase timeline
    for i, (start, end, label, color) in enumerate(zip(phase_times[:-1], phase_times[1:], phase_labels[:-1], phase_colors[:-1])):
        ax7.barh(0, end-start, left=start, height=0.3, color=color, alpha=0.7,
                 edgecolor='black', linewidth=1)
        ax7.text((start+end)/2, 0, label, ha='center', va='center',
                 fontsize=11, fontweight='bold', color='white')

    # Add final phase
    ax7.barh(0, 10, left=phase_times[-2], height=0.3, color=phase_colors[-1], alpha=0.7,
             edgecolor='black', linewidth=1)
    ax7.text(phase_times[-2]+5, 0, phase_labels[-1], ha='center', va='center',
             fontsize=11, fontweight='bold', color='white')

    # Add cosmic events
    event_times = [15, 35, 50]
    event_labels = ['CMB\\nDecoupling', 'BBN\\nNucleosynthesis', 'Structure\\nFormation']
    for t, label in zip(event_times, event_labels):
        ax7.axvline(t, color='red', linestyle='--', alpha=0.8, linewidth=2)
        ax7.text(t, 0.5, label, ha='center', va='bottom', fontsize=10,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.8))

    ax7.set_xlim(0, 70)
    ax7.set_ylim(-0.5, 1)
    ax7.set_xlabel('e-folds N')
    ax7.set_title('φ-Driven Cosmic Evolution Timeline', fontsize=14, fontweight='bold')
    ax7.grid(True, alpha=0.3, axis='x')
    ax7.set_yticks([])

    # Add overall title and parameter box
    fig.suptitle('FIRM φ-Field Cosmic Inflation: Complete Evolution Timeline',
                 fontsize=20, fontweight='bold')

    # Parameter information box
    param_text = f'φ = {phi:.6f}\\nV₀ = {V0} M_p⁴\\nφ₀ = {phi_0:.2f} M_p\\nTotal e-folds: ~60'
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.8)
    fig.text(0.02, 0.98, param_text, transform=fig.transFigure, fontsize=12,
             verticalalignment='top', bbox=props)

    # Save with provenance
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return {
        "figure_path": output_path,
        "provenance": {
            "theory_source": "cosmology/inflation_theory.py",
            "mathematical_basis": "φ-field driven cosmic inflation dynamics",
            "phi_value": phi,
            "initial_field": phi_field_initial,
            "total_efolds": 60,
            "scale_factor_expansion": scale_factor[-1]/scale_factor[0]
        }
    }

if __name__ == "__main__":
    result = generate_inflation_evolution_figure()
    print(f"Generated: {result['figure_path']}")
    print(f"φ = {result['provenance']['phi_value']:.6f}")
    print(f"Initial field: {result['provenance']['initial_field']:.3f} M_p")
    print(f"Scale expansion: {result['provenance']['scale_factor_expansion']:.2e}")
