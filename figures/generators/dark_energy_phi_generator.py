#!/usr/bin/env python3
"""
Dark Energy φ-Scaling vs ΛCDM Comparison Figure Generator

PROVENANCE:
- Source Theory: cosmology/dark_energy_phi.py
- Mathematical Basis: φ-scaling dark energy model vs standard ΛCDM
- Generated for: FIRM ArXiv Paper - testable cosmological predictions
- Output: dark_energy_phi_scaling.png
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate_dark_energy_phi_figure(output_path="figures/dark_energy_phi_scaling.png"):
    """Generate comprehensive dark energy φ-scaling vs ΛCDM comparison figure."""

    # Mathematical parameters from FIRM theory
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio

    # Cosmological parameters
    H0 = 70  # km/s/Mpc (Hubble constant)
    Omega_m = 0.3  # Matter density parameter
    Omega_Lambda = 0.7  # Dark energy density parameter (ΛCDM)
    Omega_r = 8e-5  # Radiation density parameter

    # Redshift range
    z = np.linspace(0, 5, 200)
    a = 1 / (1 + z)  # Scale factor

    # ΛCDM model
    rho_m_LCDM = Omega_m * a**(-3)
    rho_r_LCDM = Omega_r * a**(-4)
    rho_DE_LCDM = Omega_Lambda * np.ones_like(a)  # Constant
    H_LCDM = H0 * np.sqrt(rho_m_LCDM + rho_r_LCDM + rho_DE_LCDM)
    w_LCDM = -np.ones_like(z)  # Constant w = -1

    # φ-scaling dark energy model
    w_phi = -1 + (phi - 1) / phi * a**2  # φ-dependent equation of state
    rho_DE_phi = Omega_Lambda * a**(-3 * (1 + w_phi))
    # Handle numerical issues
    rho_DE_phi = np.abs(rho_DE_phi)
    rho_DE_phi = np.clip(rho_DE_phi, 1e-10, 1e10)

    H_phi = H0 * np.sqrt(rho_m_LCDM + rho_r_LCDM + rho_DE_phi)

    # Luminosity distance calculations
    def integrate_E(z_vals, H_vals):
        dz = z_vals[1] - z_vals[0]
        E_inv = 1 / (H_vals / H0)
        return np.cumsum(E_inv) * dz

    # Comoving distances
    D_c_LCDM = integrate_E(z, H_LCDM)
    D_c_phi = integrate_E(z, H_phi)

    # Luminosity distances
    D_L_LCDM = (1 + z) * D_c_LCDM
    D_L_phi = (1 + z) * D_c_phi

    # Distance modulus
    mu_LCDM = 5 * np.log10(D_L_LCDM) + 25  # +25 for Mpc units
    mu_phi = 5 * np.log10(D_L_phi) + 25

    # Set up comprehensive comparison figure
    plt.style.use('default')
    fig = plt.figure(figsize=(20, 15))
    gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)

    # Plot 1: Dark energy density evolution
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.semilogy(z, rho_DE_LCDM, color='#E74C3C', linewidth=3, label='ΛCDM (constant)', linestyle='--')
    ax1.semilogy(z, rho_DE_phi, color='#8E44AD', linewidth=3, label='φ-scaling DE')
    ax1.set_xlabel('Redshift z')
    ax1.set_ylabel('Dark Energy Density (normalized)')
    ax1.set_title('Dark Energy Evolution', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Equation of state evolution
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(z, w_LCDM, color='#E74C3C', linewidth=3, label='ΛCDM (w = -1)', linestyle='--')
    ax2.plot(z, w_phi, color='#8E44AD', linewidth=3, label='φ-scaling (w variable)')
    ax2.axhline(-1, color='black', linestyle=':', alpha=0.5, label='Cosmological constant')
    ax2.set_xlabel('Redshift z')
    ax2.set_ylabel('Equation of State w')
    ax2.set_title('Dark Energy Equation of State', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(-1.5, -0.5)

    # Plot 3: Hubble parameter evolution
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.plot(z, H_LCDM, color='#E74C3C', linewidth=3, label='ΛCDM', linestyle='--')
    ax3.plot(z, H_phi, color='#8E44AD', linewidth=3, label='φ-scaling')
    ax3.set_xlabel('Redshift z')
    ax3.set_ylabel('H(z) (km/s/Mpc)')
    ax3.set_title('Hubble Parameter Evolution', fontsize=14, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Plot 4: Energy density components
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.semilogy(z, rho_m_LCDM, color='#27AE60', linewidth=3, label='Matter')
    ax4.semilogy(z, rho_r_LCDM, color='#F39C12', linewidth=3, label='Radiation')
    ax4.semilogy(z, rho_DE_LCDM, color='#E74C3C', linewidth=3, label='Dark Energy (ΛCDM)', linestyle='--')
    ax4.semilogy(z, rho_DE_phi, color='#8E44AD', linewidth=3, label='Dark Energy (φ)')
    ax4.set_xlabel('Redshift z')
    ax4.set_ylabel('Energy Density (normalized)')
    ax4.set_title('Cosmic Energy Components', fontsize=14, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Plot 5: Luminosity distance comparison
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.plot(z[:100], D_L_LCDM[:100], color='#E74C3C', linewidth=3, label='ΛCDM', linestyle='--')
    ax5.plot(z[:100], D_L_phi[:100], color='#8E44AD', linewidth=3, label='φ-scaling')
    ax5.set_xlabel('Redshift z')
    ax5.set_ylabel('Luminosity Distance D_L(z)')
    ax5.set_title('Luminosity Distance Comparison', fontsize=14, fontweight='bold')
    ax5.legend()
    ax5.grid(True, alpha=0.3)

    # Plot 6: Distance modulus difference
    ax6 = fig.add_subplot(gs[1, 2])
    delta_mu = mu_phi[:100] - mu_LCDM[:100]
    ax6.plot(z[:100], delta_mu, color='#9B59B6', linewidth=3, label='Δμ = μ_φ - μ_ΛCDM')
    ax6.axhline(0, color='black', linestyle=':', alpha=0.5)
    ax6.set_xlabel('Redshift z')
    ax6.set_ylabel('Distance Modulus Difference')
    ax6.set_title('Observational Difference', fontsize=14, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)

    # Plot 7: φ-scaling parameter sensitivity
    ax7 = fig.add_subplot(gs[2, :])

    # Show different φ-scaling behaviors
    phi_variations = [phi, phi*1.1, phi*0.9]
    phi_labels = [f'φ = {p:.3f}' for p in phi_variations]
    colors = ['#8E44AD', '#E67E22', '#3498DB']

    for i, (phi_var, label, color) in enumerate(zip(phi_variations, phi_labels, colors)):
        w_var = -1 + (phi_var - 1) / phi_var * a**2
        rho_DE_var = Omega_Lambda * a**(-3 * (1 + w_var))
        rho_DE_var = np.abs(rho_DE_var)
        rho_DE_var = np.clip(rho_DE_var, 1e-10, 1e10)

        ax7.semilogy(z, rho_DE_var, color=color, linewidth=3, label=label,
                    alpha=0.8 if i == 0 else 0.6)

    ax7.semilogy(z, rho_DE_LCDM, color='#E74C3C', linewidth=3,
                 label='ΛCDM (constant)', linestyle='--', alpha=0.8)

    ax7.set_xlabel('Redshift z')
    ax7.set_ylabel('Dark Energy Density (normalized)')
    ax7.set_title('φ-Parameter Sensitivity Analysis', fontsize=14, fontweight='bold')
    ax7.legend(ncol=2)
    ax7.grid(True, alpha=0.3)

    # Add overall title and parameter boxes
    fig.suptitle('FIRM φ-Scaling Dark Energy vs Standard ΛCDM Model',
                 fontsize=20, fontweight='bold')

    # FIRM model parameters box
    param_text = f'FIRM φ-Model Parameters:\\nφ = {phi:.6f}\\nw(z) = -1 + (φ-1)/φ × a²\\nΩ_m = {Omega_m}\\nΩ_Λ = {Omega_Lambda}\\nH₀ = {H0} km/s/Mpc'
    props = dict(boxstyle='round', facecolor='lightgreen', alpha=0.8)
    fig.text(0.02, 0.98, param_text, transform=fig.transFigure, fontsize=12,
             verticalalignment='top', bbox=props)

    # Observational constraints box
    obs_text = 'Key Observational Tests:\\n• Supernovae distance-redshift\\n• BAO scale evolution\\n• CMB angular diameter distance\\n• Growth of structure'
    props2 = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
    fig.text(0.78, 0.98, obs_text, transform=fig.transFigure, fontsize=12,
             verticalalignment='top', bbox=props2)

    # Save with provenance
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return {
        "figure_path": output_path,
        "provenance": {
            "theory_source": "cosmology/dark_energy_phi.py",
            "mathematical_basis": "φ-scaling dark energy model vs ΛCDM",
            "phi_value": phi,
            "equation_of_state_z0": w_phi[0],
            "phi_scaling_parameter": phi - 1,
            "observational_tests": ["supernovae", "BAO", "CMB", "structure_growth"]
        }
    }

if __name__ == "__main__":
    result = generate_dark_energy_phi_figure()
    print(f"Generated: {result['figure_path']}")
    print(f"φ = {result['provenance']['phi_value']:.6f}")
    print(f"φ-1 = {result['provenance']['phi_scaling_parameter']:.6f} (scaling parameter)")
    print(f"w(z=0) = {result['provenance']['equation_of_state_z0']:.3f}")
