#!/usr/bin/env python3
"""
Dark Matter Structure Formation Generator
Shows how φ-field dark matter drives cosmic structure formation
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any

def generate_dark_matter_structure_formation() -> Dict[str, Any]:
    """Generate dark matter structure formation from φ-field dynamics."""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Golden ratio and cosmological parameters
    phi = (1 + np.sqrt(5)) / 2
    H0 = 67.4  # Hubble constant km/s/Mpc
    
    # 1. φ-Field Dark Matter Power Spectrum
    ax1.set_title("Dark Matter Power Spectrum: φ-Field vs CDM", fontsize=14, weight='bold')
    
    # Wavenumber range (h/Mpc)
    k = np.logspace(-3, 2, 100)
    
    # Standard CDM power spectrum (simplified)
    k_eq = 0.01  # Matter-radiation equality scale
    P_cdm = (k / k_eq)**(3.96) / (1 + (k / k_eq)**2)**1.32
    
    # φ-field dark matter with harmonic corrections
    # Enhanced power on φ-harmonic scales
    phi_scales = [0.1/phi, 0.1, 0.1*phi, 0.1*phi**2]  # Multiple harmonic scales
    P_phi = P_cdm.copy()
    
    for phi_scale in phi_scales:
        # Add φ-harmonic enhancements
        enhancement = 1 + 0.15 * np.exp(-((np.log(k) - np.log(phi_scale))/0.5)**2)
        P_phi *= enhancement
    
    ax1.loglog(k, P_cdm, 'b-', linewidth=2, label='Standard CDM')
    ax1.loglog(k, P_phi, 'r-', linewidth=3, label='φ-Field Dark Matter')
    ax1.fill_between(k, P_cdm, P_phi, alpha=0.3, color='yellow', label='φ-Enhancement')
    
    # Mark φ-harmonic scales
    for i, scale in enumerate(phi_scales):
        ax1.axvline(scale, color='red', linestyle=':', alpha=0.7)
        ax1.text(scale, 1e-2, f'φ^{i-1}', rotation=90, va='bottom', ha='right', color='red')
    
    ax1.set_xlabel("Wavenumber k (h/Mpc)")
    ax1.set_ylabel("Power P(k)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(1e-3, 1e2)
    ax1.set_ylim(1e-6, 1e2)
    
    # 2. Halo Mass Function Evolution
    ax2.set_title("Halo Mass Function: φ-Enhanced Structure Growth", fontsize=14, weight='bold')
    
    # Halo mass range (M_sun/h)
    M_halo = np.logspace(8, 16, 50)
    
    # Redshifts
    redshifts = [0, 1, 3, 6]
    colors = ['red', 'orange', 'green', 'blue']
    
    for z, color in zip(redshifts, colors):
        # Growth factor with φ-corrections
        D_z = 1 / (1 + z) * (1 + 0.05 * phi * np.exp(-z/2))  # φ-enhanced growth
        
        # Press-Schechter mass function with φ-corrections
        sigma_M = 0.8 * (M_halo / 1e12)**(-0.5)  # Mass variance
        nu = 1.686 / (sigma_M * D_z)  # Peak height
        
        # φ-corrected mass function
        dn_dM = 0.3 * (nu / sigma_M) * (M_halo / 1e12)**(-1) * np.exp(-nu**2/2) * (1 + 0.1/phi)
        
        ax2.loglog(M_halo, dn_dM, color=color, linewidth=2, label=f'z = {z}')
        
    ax2.set_xlabel("Halo Mass M (M☉/h)")
    ax2.set_ylabel("dn/dM (h³/Mpc³)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Add observational constraints
    ax2.fill_between([1e12, 1e14], 1e-6, 1e-2, alpha=0.2, color='gray', 
                    label='Observational Range')
    
    # 3. Structure Formation Timeline
    ax3.set_title("Cosmic Structure Timeline: φ-Field Dynamics", fontsize=14, weight='bold')
    
    # Cosmic time and redshift
    redshift_range = np.linspace(0, 10, 100)
    cosmic_time = 13.8 / (1 + redshift_range)**1.5  # Approximate age-redshift relation
    
    # Structure formation milestones
    milestones = [
        (10, "Dark matter decoupling", "φ-field becomes dominant"),
        (6, "First φ-halos form", "φ-harmonic condensation"),  
        (3, "Galaxy formation peak", "Baryons follow φ-potential"),
        (1, "Large scale structure", "φ-cosmic web emerges"),
        (0, "Present day", "Mature φ-structure")
    ]
    
    # Plot cosmic timeline
    ax3.plot(cosmic_time, redshift_range, 'k-', linewidth=2, alpha=0.7)
    
    # Add milestones
    for z_milestone, event, description in milestones:
        t_milestone = 13.8 / (1 + z_milestone)**1.5
        ax3.scatter(t_milestone, z_milestone, s=200, c='red', alpha=0.8, 
                   edgecolors='black', linewidth=2, zorder=5)
        ax3.annotate(f"{event}\n{description}", (t_milestone, z_milestone),
                    xytext=(20, 0), textcoords='offset points', 
                    fontsize=9, ha='left', va='center',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))
    
    ax3.set_xlabel("Cosmic Time (Gyr)")
    ax3.set_ylabel("Redshift z")
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 14)
    ax3.set_ylim(0, 11)
    
    # 4. φ-Field Potential Wells and Galaxy Formation
    ax4.set_title("φ-Field Potential Wells: Galaxy Formation Sites", fontsize=14, weight='bold')
    
    # Spatial coordinates (Mpc/h)
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    X, Y = np.meshgrid(x, y)
    
    # φ-field potential with multiple wells
    # Superposition of Gaussian wells at φ-harmonic separations
    phi_potential = np.zeros_like(X)
    
    # Central massive halo
    phi_potential += -5 * np.exp(-(X**2 + Y**2) / (2 * 2**2))
    
    # Satellite halos at φ-harmonic distances
    satellite_positions = [
        (4*phi, 0), (-4*phi, 0), (0, 4*phi), (0, -4*phi),  # φ-harmonic ring
        (6, 6), (-6, -6), (6, -6), (-6, 6)  # Diagonal satellites
    ]
    
    for x_sat, y_sat in satellite_positions:
        depth = -2 * np.exp(-0.5)  # Satellite depth
        phi_potential += depth * np.exp(-((X - x_sat)**2 + (Y - y_sat)**2) / (2 * 1.5**2))
    
    # Add φ-field fluctuations
    phi_potential += 0.3 * np.sin(phi * X / 2) * np.cos(phi * Y / 2) * np.exp(-(X**2 + Y**2) / 50)
    
    # Plot potential
    contour = ax4.contour(X, Y, phi_potential, levels=15, colors='blue', alpha=0.7)
    ax4.clabel(contour, inline=True, fontsize=8)
    
    # Fill deepest wells (galaxy formation sites)
    ax4.contourf(X, Y, phi_potential, levels=[-6, -4], colors=['red'], alpha=0.3)
    
    # Mark galaxy positions
    for x_sat, y_sat in [(0, 0)] + satellite_positions[:4]:  # Central + φ-ring
        ax4.scatter(x_sat, y_sat, s=100, c='gold', alpha=0.8, 
                   edgecolors='black', linewidth=1, marker='*')
    
    ax4.set_xlabel("x (Mpc/h)")
    ax4.set_ylabel("y (Mpc/h)")
    ax4.set_aspect('equal')
    ax4.grid(True, alpha=0.3)
    
    # Add φ-harmonic scale annotation
    ax4.text(0.02, 0.98, f"φ-harmonic scale:\n{4*phi:.1f} Mpc/h", 
            transform=ax4.transAxes, va='top', fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightblue', alpha=0.8))
    
    # Overall title
    fig.suptitle("Dark Matter Structure Formation: φ-Field Dynamics Drive Cosmic Web\n" +
                "φ-Harmonic Enhancements Create Preferred Scales for Galaxy Formation",
                fontsize=16, weight='bold')
    
    plt.tight_layout()
    
    # Calculate key parameters
    phi_enhancement_factor = np.max(P_phi / P_cdm)
    structure_formation_acceleration = 1 + 0.1/phi  # φ-enhanced growth
    
    # Save figure
    output_path = Path("figures/outputs/dark_matter_structure_formation.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "cosmology",
        "title": "Dark Matter Structure Formation: φ-Field Dynamics",
        "description": "How φ-field dark matter drives cosmic structure formation with harmonic enhancements",
        "phi_enhancement_factor": f"{phi_enhancement_factor:.2f}×",
        "structure_formation_acceleration": f"{structure_formation_acceleration:.3f}",
        "harmonic_scales": len(phi_scales),
        "formation_milestones": len(milestones),
        "provenance": "phi_field_structure_formation"
    }

if __name__ == "__main__":
    result = generate_dark_matter_structure_formation()
    print(f"Generated: {result['file']}")
    print(f"φ-enhancement: {result['phi_enhancement_factor']}")
    print(f"Structure acceleration: {result['structure_formation_acceleration']}")
    print(f"Harmonic scales: {result['harmonic_scales']}")
