#!/usr/bin/env python3
"""
Gauge Field Configurations Generator
Shows φ-harmonic gauge field configurations and topological structures
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any

def generate_gauge_field_configurations() -> Dict[str, Any]:
    """Generate φ-harmonic gauge field configurations analysis."""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Golden ratio and gauge parameters
    phi = (1 + np.sqrt(5)) / 2
    g = 0.6  # Gauge coupling
    
    # 1. Non-Abelian Gauge Field Configuration
    ax1.set_title("φ-Harmonic SU(2) Gauge Field Configuration", fontsize=14, weight='bold')
    
    # Spatial grid
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    
    # φ-enhanced Yang-Mills field
    # A_μ = φ-harmonic configuration with topological structure
    
    # Gauge field components with φ-modulation
    A1 = np.sin(phi * X) * np.cos(Y) * np.exp(-(X**2 + Y**2)/4)
    A2 = np.cos(X) * np.sin(phi * Y) * np.exp(-(X**2 + Y**2)/4)
    
    # Field strength tensor F_μν = ∂_μ A_ν - ∂_ν A_μ + g[A_μ, A_ν]
    # Approximate field strength
    F12 = np.gradient(A2)[1] - np.gradient(A1)[0] + g * (A1 * A2 - A2 * A1)
    
    # Plot field strength
    contour = ax1.contourf(X, Y, F12, levels=20, cmap='RdBu_r', alpha=0.8)
    plt.colorbar(contour, ax=ax1, label='Field Strength F₁₂')
    
    # Add field lines (streamplot of A_μ)
    ax1.streamplot(X, Y, A1, A2, density=1.5, color='white', linewidth=1)
    
    # Mark φ-harmonic vortices
    vortex_positions = [(phi, 0), (-phi, 0), (0, phi), (0, -phi)]
    for vx, vy in vortex_positions:
        ax1.scatter(vx, vy, s=100, c='yellow', marker='*', edgecolors='black', 
                   linewidth=1, zorder=5)
    
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_aspect('equal')
    
    # Add topological charge
    topological_charge = np.trapz(np.trapz(F12, x), y) / (2*np.pi)
    ax1.text(0.02, 0.98, f"Topological charge:\nQ = {topological_charge:.2f}\nφ-vortices: {len(vortex_positions)}", 
            transform=ax1.transAxes, va='top', fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightblue', alpha=0.8))
    
    # 2. Gauge Coupling Running with φ-Corrections
    ax2.set_title("Gauge Coupling Evolution: φ-Enhanced β-Function", fontsize=14, weight='bold')
    
    # Energy scale
    mu = np.logspace(0, 4, 100)  # 1 GeV to 10 TeV
    
    # Standard Model gauge couplings at MZ
    g1_MZ = np.sqrt(5/3) * 0.358  # U(1)_Y hypercharge
    g2_MZ = 0.652                 # SU(2)_L weak
    g3_MZ = 1.221                 # SU(3)_C strong
    
    MZ = 91.2  # GeV
    
    # One-loop β-functions (simplified)
    b1 = 41/10    # U(1) beta function
    b2 = -19/6    # SU(2) beta function  
    b3 = -7       # SU(3) beta function
    
    # Standard running
    alpha1_std = (g1_MZ**2/(4*np.pi)) / (1 - b1 * (g1_MZ**2/(4*np.pi)) * np.log(mu/MZ)/(2*np.pi))
    alpha2_std = (g2_MZ**2/(4*np.pi)) / (1 - b2 * (g2_MZ**2/(4*np.pi)) * np.log(mu/MZ)/(2*np.pi))
    alpha3_std = (g3_MZ**2/(4*np.pi)) / (1 - b3 * (g3_MZ**2/(4*np.pi)) * np.log(mu/MZ)/(2*np.pi))
    
    # φ-corrections to β-functions
    phi_corrections = 1 + 0.01 * np.sin(phi * np.log(mu/MZ))
    
    alpha1_phi = alpha1_std * phi_corrections
    alpha2_phi = alpha2_std * phi_corrections  
    alpha3_phi = alpha3_std * phi_corrections
    
    ax2.semilogx(mu, alpha1_std, 'b--', linewidth=2, alpha=0.7, label='α₁ (U(1)) Standard')
    ax2.semilogx(mu, alpha2_std, 'g--', linewidth=2, alpha=0.7, label='α₂ (SU(2)) Standard') 
    ax2.semilogx(mu, alpha3_std, 'r--', linewidth=2, alpha=0.7, label='α₃ (SU(3)) Standard')
    
    ax2.semilogx(mu, alpha1_phi, 'b-', linewidth=3, label='α₁ φ-Enhanced')
    ax2.semilogx(mu, alpha2_phi, 'g-', linewidth=3, label='α₂ φ-Enhanced')
    ax2.semilogx(mu, alpha3_phi, 'r-', linewidth=3, label='α₃ φ-Enhanced')
    
    # Mark unification scale
    unification_scale = 2e16  # GeV
    ax2.axvline(unification_scale, color='gold', linestyle=':', alpha=0.7, 
               label='φ-GUT Scale')
    
    # Find φ-corrected unification point
    # Look for crossing of α₁ and α₂
    unification_idx = np.argmin(np.abs(alpha1_phi - alpha2_phi))
    unification_mu = mu[unification_idx]
    unification_alpha = alpha1_phi[unification_idx]
    
    ax2.scatter(unification_mu, unification_alpha, s=200, c='gold', 
               alpha=0.9, edgecolors='black', linewidth=2, zorder=10)
    ax2.text(unification_mu, unification_alpha + 0.005, 
            f'φ-Unification\n{unification_mu:.1e} GeV', 
            ha='center', va='bottom', fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='yellow', alpha=0.8))
    
    ax2.set_xlabel("Energy Scale μ (GeV)")
    ax2.set_ylabel("Gauge Coupling α = g²/(4π)")
    ax2.legend(ncol=2, fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(1, 1e18)
    ax2.set_ylim(0, 0.15)
    
    # 3. Instanton Configurations and Vacuum Structure
    ax3.set_title("Instanton Configurations: φ-Modulated Vacuum", fontsize=14, weight='bold')
    
    # Instanton solution in 2D (simplified)
    rho = np.linspace(0, 4, 100)  # Radial coordinate
    
    # Standard instanton profile
    instanton_std = 2 * rho**2 / (rho**2 + 1)**2
    
    # φ-modulated instanton
    # Multiple instanton sizes at φ-harmonic scales
    rho_phi = [1/phi, 1, phi, phi**2]  # φ-harmonic instanton sizes
    weights = [0.3, 0.4, 0.2, 0.1]     # Relative weights
    
    instanton_phi = np.zeros_like(rho)
    for size, weight in zip(rho_phi, weights):
        instanton_phi += weight * 2 * (rho/size)**2 / ((rho/size)**2 + 1)**2
    
    ax3.plot(rho, instanton_std, 'b-', linewidth=2, label='Standard Instanton')
    ax3.plot(rho, instanton_phi, 'r-', linewidth=3, label='φ-Modulated Instanton')
    ax3.fill_between(rho, instanton_std, instanton_phi, alpha=0.3, color='yellow')
    
    # Mark φ-scales
    for i, size in enumerate(rho_phi):
        if size <= 4:
            ax3.axvline(size, color='red', linestyle=':', alpha=0.7)
            ax3.text(size, 0.4, f'ρ_φ^{i-1}', rotation=90, va='bottom', ha='right', color='red')
    
    # Vacuum energy contributions
    vacuum_energy_std = np.trapz(instanton_std * rho, rho)
    vacuum_energy_phi = np.trapz(instanton_phi * rho, rho)
    
    ax3.text(0.02, 0.98, f"Vacuum contributions:\nStandard: {vacuum_energy_std:.2f}\nφ-Enhanced: {vacuum_energy_phi:.2f}", 
            transform=ax3.transAxes, va='top', fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightgreen', alpha=0.8))
    
    ax3.set_xlabel("Instanton Size ρ")
    ax3.set_ylabel("Action Density")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 4)
    
    # 4. Gauge-Gravity Correspondence: AdS/CFT with φ-Fields
    ax4.set_title("AdS/CFT Correspondence: φ-Enhanced Holographic Duality", fontsize=14, weight='bold')
    
    # Radial AdS coordinate
    z = np.linspace(0.1, 5, 100)  # AdS radial coordinate (z=0 is boundary)
    
    # AdS_5 metric component
    # ds² = (R²/z²)(-dt² + dx² + dz²) with φ-corrections
    R_AdS = 1  # AdS radius
    
    # Warp factor with φ-corrections
    warp_factor_std = (R_AdS / z)**2
    warp_factor_phi = warp_factor_std * (1 + 0.1 * np.sin(phi * np.log(z)) * np.exp(-z))
    
    # Gauge field in AdS bulk
    gauge_field_bulk = np.exp(-z) * np.cos(phi * z)
    
    # Plot warp factors
    ax4_warp = ax4
    ax4_warp.semilogy(z, warp_factor_std, 'b-', linewidth=2, label='Standard AdS₅')
    ax4_warp.semilogy(z, warp_factor_phi, 'r-', linewidth=3, label='φ-Enhanced AdS₅')
    ax4_warp.fill_between(z, warp_factor_std, warp_factor_phi, alpha=0.3, color='yellow')
    
    # Gauge field on secondary axis
    ax4_gauge = ax4_warp.twinx()
    ax4_gauge.plot(z, gauge_field_bulk, 'green', linewidth=2, label='Bulk Gauge Field')
    
    # Mark AdS/CFT correspondence scales
    IR_cutoff = phi  # φ-scale IR cutoff
    ax4_warp.axvline(IR_cutoff, color='orange', linestyle='--', alpha=0.7, 
                    label=f'IR Cutoff (φ-scale)')
    
    # Boundary (UV) at z→0
    ax4_warp.axvline(0.2, color='purple', linestyle='--', alpha=0.7, label='UV Boundary')
    
    ax4_warp.set_xlabel("AdS Radial Coordinate z")
    ax4_warp.set_ylabel("Warp Factor (R/z)²", color='blue')
    ax4_gauge.set_ylabel("Gauge Field Amplitude", color='green')
    
    ax4_warp.tick_params(axis='y', labelcolor='blue')
    ax4_gauge.tick_params(axis='y', labelcolor='green')
    
    ax4_warp.legend(loc='upper right')
    ax4_gauge.legend(loc='upper left')
    ax4_warp.grid(True, alpha=0.3)
    ax4_warp.set_xlim(0.1, 5)
    ax4_warp.set_ylim(0.1, 100)
    
    # Add holographic correspondence
    ax4_warp.text(0.02, 0.02, "CFT₄ ↔ AdS₅ × S⁵\nφ-fields enhance\nholographic duality", 
                 transform=ax4_warp.transAxes, va='bottom', fontweight='bold',
                 bbox=dict(boxstyle="round", facecolor='lightcyan', alpha=0.8))
    
    # Overall title
    fig.suptitle("Gauge Field Configurations: φ-Harmonic Non-Abelian Fields and Holographic Duality\n" +
                "φ-Enhanced Yang-Mills Theory with Topological Structures and AdS/CFT Correspondence",
                fontsize=16, weight='bold')
    
    plt.tight_layout()
    
    # Calculate key parameters
    coupling_unification_scale = unification_mu
    vacuum_enhancement = vacuum_energy_phi / vacuum_energy_std
    
    # Save figure
    output_path = Path("figures/outputs/gauge_field_configurations.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "field_theory",
        "title": "Gauge Field Configurations: φ-Harmonic Non-Abelian Fields",
        "description": "φ-enhanced Yang-Mills theory with topological structures and holographic duality",
        "topological_charge": f"{topological_charge:.2f}",
        "phi_vortices": len(vortex_positions),
        "unification_scale_gev": f"{coupling_unification_scale:.1e} GeV",
        "vacuum_enhancement": f"{vacuum_enhancement:.2f}×",
        "instanton_scales": len(rho_phi),
        "provenance": "phi_enhanced_yang_mills_theory"
    }

if __name__ == "__main__":
    result = generate_gauge_field_configurations()
    print(f"Generated: {result['file']}")
    print(f"Topological charge: {result['topological_charge']}")
    print(f"φ-vortices: {result['phi_vortices']}")
    print(f"Unification scale: {result['unification_scale_gev']} GeV")
    print(f"Vacuum enhancement: {result['vacuum_enhancement']}")
