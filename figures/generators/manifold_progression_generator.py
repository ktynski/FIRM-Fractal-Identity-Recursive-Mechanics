"""
Generator for manifold progression diagram.

This script generates a visualization of the FIRM manifold progression theory,
showing the four key manifolds (Torus → Möbius Strip → Klein Bottle → φ-Klein Recursive)
with their topological properties and transitions.

The diagram is saved as 'manifold_progression_diagram.png' and includes:
- 3D visualizations of each manifold
- Topological invariants (fundamental group, Euler characteristic)
- Transition operators between manifolds
- Cosmogenesis phase mapping

Author: FIRM Research Team
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

# Constants
PHI = (1 + np.sqrt(5)) / 2
PHI_INV = 1 / PHI

# Color scheme
COLORS = {
    'torus': '#3498db',       # Blue
    'mobius': '#e74c3c',      # Red
    'klein': '#9b59b6',       # Purple
    'phi_klein': '#f1c40f',   # Yellow
    'background': '#f8f9fa',  # Light gray
    'text': '#2c3e50',        # Dark blue/gray
    'arrow': '#27ae60',       # Green
}

def generate_torus(ax):
    """Generate a torus visualization on the given 3D axis."""
    # Torus parameters
    R, r = 2, 0.5  # Major and minor radii
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, 2 * np.pi, 50)
    u, v = np.meshgrid(u, v)

    # Torus parametric equations
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)

    # Plot surface
    ax.plot_surface(x, y, z, color=COLORS['torus'], alpha=0.8, edgecolor='k', linewidth=0.2)
    ax.set_title("Torus $T^2 = S^1 \\times S^1$", fontsize=12)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

def generate_mobius_strip(ax):
    """Generate a Möbius strip visualization on the given 3D axis."""
    # Möbius strip parameters
    R = 2  # Major radius
    w = 1  # Width
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-w/2, w/2, 10)
    u, v = np.meshgrid(u, v)

    # Möbius strip parametric equations
    x = (R + v * np.cos(u/2)) * np.cos(u)
    y = (R + v * np.cos(u/2)) * np.sin(u)
    z = v * np.sin(u/2)

    # Plot surface
    ax.plot_surface(x, y, z, color=COLORS['mobius'], alpha=0.8, edgecolor='k', linewidth=0.2)
    ax.set_title("Möbius Strip $M$", fontsize=12)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

def generate_klein_bottle(ax):
    """Generate a Klein bottle visualization on the given 3D axis."""
    # Klein bottle parameters (immersed in 3D)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)

    # Klein bottle parametric equations (immersion in 3D)
    r = 1.5
    x = (r + np.cos(u/2) * np.sin(v) - np.sin(u/2) * np.sin(2*v)) * np.cos(u)
    y = (r + np.cos(u/2) * np.sin(v) - np.sin(u/2) * np.sin(2*v)) * np.sin(u)
    z = np.sin(u/2) * np.sin(v) + np.cos(u/2) * np.sin(2*v)

    # Plot surface
    ax.plot_surface(x, y, z, color=COLORS['klein'], alpha=0.8, edgecolor='k', linewidth=0.2)
    ax.set_title("Klein Bottle $K$", fontsize=12)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

def generate_phi_klein_recursive(ax):
    """Generate a φ-Klein recursive manifold visualization."""
    # Simplified representation: multiple Klein bottles at different scales
    generate_klein_bottle(ax)  # Base Klein bottle

    # Add a scaled down version
    r_scaled = 0.618  # φ⁻¹
    ax.text(0, 0, 2.5, "$\\Phi(K) = \\bigcup_{n=0}^{\\infty} \\phi^{-n}(K)$",
            fontsize=10, ha='center', color=COLORS['text'])
    ax.set_title("$\\phi$-Klein Recursive Manifold $\\Phi(K)$", fontsize=12)

def generate_manifold_progression_diagram():
    """Generate the complete manifold progression diagram."""
    # Create figure
    fig = plt.figure(figsize=(16, 9))
    fig.suptitle("FIRM Manifold Progression", fontsize=20)

    # Create 3D subplots for each manifold
    ax1 = fig.add_subplot(2, 4, 1, projection='3d')
    generate_torus(ax1)

    ax2 = fig.add_subplot(2, 4, 2, projection='3d')
    generate_mobius_strip(ax2)

    ax3 = fig.add_subplot(2, 4, 3, projection='3d')
    generate_klein_bottle(ax3)

    ax4 = fig.add_subplot(2, 4, 4, projection='3d')
    generate_phi_klein_recursive(ax4)

    # Add manifold properties in text boxes
    props1 = fig.add_subplot(2, 4, 5)
    props1.text(0.5, 0.5, "$\\pi_1(T^2) = \\mathbb{Z} \\times \\mathbb{Z}$\n$\\chi(T^2) = 0$\nOrientable: Yes\nGenus: 1",
               ha='center', va='center', fontsize=10)
    props1.set_title("Torus Properties", fontsize=10)
    props1.axis('off')

    props2 = fig.add_subplot(2, 4, 6)
    props2.text(0.5, 0.5, "$\\pi_1(M) = \\mathbb{Z}$\n$\\chi(M) = 0$\nOrientable: No\nBoundary: $S^1$",
               ha='center', va='center', fontsize=10)
    props2.set_title("Möbius Properties", fontsize=10)
    props2.axis('off')

    props3 = fig.add_subplot(2, 4, 7)
    props3.text(0.5, 0.5, "$\\pi_1(K) = \\langle a,b | aba^{-1}b \\rangle$\n$\\chi(K) = 0$\nOrientable: No\nSelf-intersecting: Yes",
               ha='center', va='center', fontsize=10)
    props3.set_title("Klein Bottle Properties", fontsize=10)
    props3.axis('off')

    props4 = fig.add_subplot(2, 4, 8)
    props4.text(0.5, 0.5, "Recursive structure\n$\\phi$-scaling\nFractal dimension\nInfinite genus",
               ha='center', va='center', fontsize=10)
    props4.set_title("$\\phi$-Klein Properties", fontsize=10)
    props4.axis('off')

    # Add arrows between manifolds
    fig.text(0.28, 0.6, "$\\to$", fontsize=24, ha='center')
    fig.text(0.28, 0.52, "Dimensional\nBridge", fontsize=8, ha='center')

    fig.text(0.53, 0.6, "$\\to$", fontsize=24, ha='center')
    fig.text(0.53, 0.52, "Boundary\nClosure", fontsize=8, ha='center')

    fig.text(0.78, 0.6, "$\\to$", fontsize=24, ha='center')
    fig.text(0.78, 0.52, "$\\phi$-Recursion", fontsize=8, ha='center')

    # Add cosmogenesis phase mapping
    fig.text(0.5, 0.1, "Cosmogenesis Phase Mapping: Phase 1-2 (Torus) → Phase 3-4 (Möbius) → Phase 5-6 (Klein) → Phase 7-8 ($\\phi$-Klein)",
            ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

    # Save figure
    output_path = 'figures/manifold_progression_diagram.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved manifold progression diagram to {output_path}")

    # Copy to arxiv paper directory
    arxiv_path = 'arxiv_paper/FIRM_FINAL_SUBMISSION/figures/manifold_progression_diagram.png'
    if not os.path.exists(os.path.dirname(arxiv_path)):
        os.makedirs(os.path.dirname(arxiv_path))
    plt.savefig(arxiv_path, dpi=300, bbox_inches='tight')
    print(f"Copied to {arxiv_path}")

    plt.close(fig)
    return output_path

if __name__ == "__main__":
    generate_manifold_progression_diagram()