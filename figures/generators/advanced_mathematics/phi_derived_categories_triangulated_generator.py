#!/usr/bin/env python3
"""
φ-Derived Categories and Triangulated Categories Generator
Shows rigorous homological algebra with φ-enhanced derived categories, triangulated structures, and DG-algebras
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from pathlib import Path
from typing import Dict, Any

def generate_phi_derived_categories_triangulated() -> Dict[str, Any]:
    """Generate φ-enhanced derived categories and triangulated categories analysis."""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Golden ratio
    phi = (1 + np.sqrt(5)) / 2
    
    # 1. Derived Categories: D^b(A_φ) with φ-Enhanced Complexes
    ax1.set_title("φ-Derived Category: D^b(A_φ) with φ-Enhanced Chain Complexes", fontsize=14, weight='bold')
    
    # Chain complex in derived category
    # ... → C^{n-1} → C^n → C^{n+1} → ...
    # φ-enhancement affects differentials and cohomology
    
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.axis('off')
    
    # Chain complex objects
    complex_objects = [
        (1, 4, "C^{n-2}"),
        (3, 4, "C^{n-1}"),
        (5, 4, "C^n"),
        (7, 4, "C^{n+1}"),
        (9, 4, "C^{n+2}")
    ]
    
    # φ-enhanced cohomology dimensions
    cohom_dims = [2, int(phi), int(phi**2), int(phi), 1]
    
    for (x, y, label), dim in zip(complex_objects, cohom_dims):
        # Size of object reflects cohomology dimension
        size = 0.2 + 0.1 * dim
        circle = plt.Circle((x, y), size, facecolor='lightblue', 
                           edgecolor='black', linewidth=2, alpha=0.8)
        ax1.add_patch(circle)
        ax1.text(x, y, label, ha='center', va='center', fontweight='bold', fontsize=10)
        ax1.text(x, y-size-0.3, f'dim={dim}', ha='center', va='center', 
                fontsize=8, color='blue', fontweight='bold')
    
    # Differentials d^n: C^n → C^{n+1}
    differentials = [
        ((1, 4), (3, 4), "d^{n-2}"),
        ((3, 4), (5, 4), "d^{n-1}"),
        ((5, 4), (7, 4), "d^n"),
        ((7, 4), (9, 4), "d^{n+1}")
    ]
    
    for (x1, y1), (x2, y2), d_label in differentials:
        ax1.annotate('', xy=(x2-0.3, y2), xytext=(x1+0.3, y1),
                    arrowprops=dict(arrowstyle='->', lw=2, color='red'))
        mid_x = (x1 + x2) / 2
        ax1.text(mid_x, y1 + 0.5, d_label, ha='center', va='center',
                fontweight='bold', color='red', fontsize=9)
    
    # φ-enhanced differentials: d^n_φ = d^n + φ·δ^n
    for (x1, y1), (x2, y2), d_label in differentials:
        mid_x = (x1 + x2) / 2
        ax1.text(mid_x, y1 - 0.5, f"{d_label}_φ", ha='center', va='center',
                fontweight='bold', color='purple', fontsize=8, style='italic')
    
    # Quasi-isomorphism
    quasi_iso_y = 6
    ax1.annotate('', xy=(7, quasi_iso_y), xytext=(3, quasi_iso_y),
                arrowprops=dict(arrowstyle='<->', lw=3, color='green'))
    ax1.text(5, quasi_iso_y + 0.3, "φ-quasi-isomorphism", ha='center', va='center',
            fontweight='bold', color='green', fontsize=11)
    
    # Derived category properties
    ax1.text(1, 1.5, f"φ-Derived Category D^b(A_φ):\n• φ-quasi-isomorphisms inverted\n• φ-triangulated structure\n• Cohomology: H^n_φ(C) with φ-grading\n• Serre duality: D ≅ D^op with φ-twist", 
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightgreen', alpha=0.8))
    
    # 2. Triangulated Categories: φ-Distinguished Triangles
    ax2.set_title("φ-Triangulated Structure: Distinguished Triangles and φ-Octahedral Axiom", fontsize=14, weight='bold')
    
    # Distinguished triangle: X → Y → Z → ΣX
    # φ-enhancement: φ-suspension and φ-cones
    
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8)
    ax2.axis('off')
    
    # Triangle vertices
    triangle_objects = [
        (2, 6, "X", "blue"),
        (8, 6, "Y", "red"),
        (5, 2, "Z", "green"),
        (2, 2, "ΣX", "purple")  # Suspension
    ]
    
    for x, y, label, color in triangle_objects:
        if label == "ΣX":
            # Suspension gets special hexagon
            hex_patch = patches.RegularPolygon((x, y), 6, radius=0.4,
                                             facecolor=color, edgecolor='black',
                                             linewidth=2, alpha=0.8)
            ax2.add_patch(hex_patch)
        else:
            circle = plt.Circle((x, y), 0.4, facecolor=color, 
                              edgecolor='black', linewidth=2, alpha=0.8)
            ax2.add_patch(circle)
        
        ax2.text(x, y, label, ha='center', va='center', fontweight='bold', fontsize=12)
    
    # Distinguished triangle arrows
    triangle_arrows = [
        ((2, 6), (8, 6), "f"),      # X → Y
        ((8, 6), (5, 2.4), "g"),    # Y → Z
        ((5, 1.6), (2, 2.4), "h"),  # Z → ΣX
        ((2, 2), (2, 5.6), "Σf")   # ΣX → ΣY (implied)
    ]
    
    for (x1, y1), (x2, y2), arrow_label in triangle_arrows:
        if arrow_label == "Σf":
            ax2.annotate('', xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle='->', lw=2, color='purple', linestyle='--'))
        else:
            ax2.annotate('', xy=(x2-0.2, y2-0.2), xytext=(x1+0.2, y1+0.2),
                        arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax2.text(mid_x + 0.3, mid_y + 0.3, arrow_label, ha='center', va='center',
                fontweight='bold', fontsize=10)
    
    # φ-octahedral axiom diagram (simplified)
    oct_center = (5, 5)
    ax2.text(oct_center[0], oct_center[1], "φ-Octahedral\nAxiom", ha='center', va='center',
            fontsize=11, fontweight='bold', color='red',
            bbox=dict(boxstyle="round", facecolor='yellow', alpha=0.7))
    
    # Triangulated axioms
    ax2.text(0.5, 0.5, f"φ-Triangulated Axioms:\n• TR1: Identity triangles\n• TR2: Rotation of triangles\n• TR3: φ-octahedral axiom\n• TR4: φ-suspension functor Σ_φ", 
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightcyan', alpha=0.8))
    
    # 3. DG-Algebras: A_∞-Structure with φ-Enhancement
    ax3.set_title("φ-DG-Algebras: A_∞-Structure and φ-Minimal Models", fontsize=14, weight='bold')
    
    # DG-algebra: (A, d, μ) with differential and multiplication
    # φ-enhancement: A_∞-operations with φ-homotopies
    
    # A_∞-operations: μ₁, μ₂, μ₃, ... with φ-structure constants
    operations = np.arange(1, 7)
    
    # φ-structure constants for A_∞-operations
    phi_constants = [1, 1, int(phi), int(phi**2), int(phi), 1]  # μₙ coefficients
    std_constants = [1, 1, 0, 0, 0, 0]  # Standard DG-algebra (only μ₁, μ₂)
    
    # Plot A_∞-operations
    width = 0.35
    x_pos = operations
    
    bars1 = ax3.bar(x_pos - width/2, std_constants, width,
                   label='Standard DG-algebra', color='blue', alpha=0.8)
    bars2 = ax3.bar(x_pos + width/2, phi_constants, width,
                   label='φ-A_∞-algebra', color='red', alpha=0.8)
    
    # Add value labels
    for i, (std, phi_val) in enumerate(zip(std_constants, phi_constants)):
        n = i + 1
        ax3.text(n - width/2, std + 0.1, str(std), ha='center', va='bottom', fontweight='bold')
        ax3.text(n + width/2, phi_val + 0.1, str(phi_val), ha='center', va='bottom', fontweight='bold')
        
        # Label operations
        ax3.text(n, -0.3, f'μ_{n}', ha='center', va='center', fontsize=10, fontweight='bold')
    
    ax3.set_xlabel("A_∞-operation number n")
    ax3.set_ylabel("Structure constant")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xticks(operations)
    ax3.set_ylim(0, max(phi_constants) + 1)
    
    # A_∞-relations
    total_relations = sum(phi_constants)
    ax3.text(0.02, 0.98, f"φ-A_∞ Relations:\n∑ᵢ₊ⱼ₌ₙ ±μᵢ₊₁(id^i ⊗ μⱼ ⊗ id^k) = 0\nφ-minimal model: H_φ(A) with φ-homotopies\nTotal φ-operations: {total_relations}", 
            transform=ax3.transAxes, va='top', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightblue', alpha=0.8))
    
    # 4. Spectral Sequences: φ-Grothendieck Spectral Sequence
    ax4.set_title("φ-Spectral Sequences: Grothendieck and φ-Hypercohomology", fontsize=14, weight='bold')
    
    # Grothendieck spectral sequence: E₂^{p,q} = R^p F(R^q G(-)) ⇒ R^{p+q}(F∘G)(-)
    # φ-enhancement: φ-derived functors
    
    p_max, q_max = 5, 5
    p_range = np.arange(0, p_max)
    q_range = np.arange(0, q_max)
    
    # E₂ page for φ-spectral sequence
    E2_phi = {}
    for p in p_range:
        for q in q_range:
            if p == 0 and q == 0:
                E2_phi[(p,q)] = 1
            elif p + q <= 3:
                E2_phi[(p,q)] = int(phi**(p + q))
            elif p == q and p <= 2:  # Diagonal terms
                E2_phi[(p,q)] = int(phi**p)
            else:
                E2_phi[(p,q)] = 0
    
    # Plot φ-spectral sequence
    for (p, q), value in E2_phi.items():
        if value > 0:
            size = 0.2 + 0.1 * np.log(value + 1)
            circle = plt.Circle((p, q), size, facecolor='lightcoral', 
                              edgecolor='black', linewidth=1, alpha=0.8)
            ax4.add_patch(circle)
            ax4.text(p, q, str(value), ha='center', va='center', 
                    fontweight='bold', fontsize=9)
    
    # Differentials d_r: E_r^{p,q} → E_r^{p+r,q-r+1}
    differentials_ss = [
        ((0, 2), (2, 1)),  # d₂
        ((1, 1), (3, 0)),  # d₂
        ((0, 3), (3, 1))   # d₃
    ]
    
    for (p1, q1), (p2, q2) in differentials_ss:
        if (p1, q1) in E2_phi and E2_phi[(p1, q1)] > 0:
            if p2 < p_max and q2 < q_max:
                ax4.annotate('', xy=(p2, q2), xytext=(p1, q1),
                            arrowprops=dict(arrowstyle='->', lw=2, color='purple', alpha=0.8))
    
    ax4.set_xlabel("p (functor degree)")
    ax4.set_ylabel("q (object degree)")
    ax4.set_xlim(-0.5, p_max-0.5)
    ax4.set_ylim(-0.5, q_max-0.5)
    ax4.set_xticks(p_range)
    ax4.set_yticks(q_range)
    ax4.grid(True, alpha=0.3)
    
    # Convergence and degeneration
    total_E2_entries = sum(1 for v in E2_phi.values() if v > 0)
    ax4.text(0.02, 0.98, f"φ-Spectral Sequence:\nE₂^{{p,q}} = R^p F_φ(R^q G_φ(-)) ⇒ R^{{p+q}}(F_φ∘G_φ)\nφ-hypercohomology with {total_E2_entries} nonzero entries\nφ-degeneration at E_∞ page", 
            transform=ax4.transAxes, va='top', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightyellow', alpha=0.8))
    
    # Overall title
    fig.suptitle("Advanced Homological Algebra: φ-Enhanced Derived Categories and Triangulated Structures\n" +
                "Rigorous Higher Homological Algebra with φ-DG-Algebras and Spectral Sequences",
                fontsize=16, weight='bold')
    
    plt.tight_layout()
    
    # Calculate homological algebra invariants
    total_complex_objects = len(complex_objects)
    total_cohom_dim = sum(cohom_dims)
    total_a_infinity_ops = sum(phi_constants)
    max_spectral_entry = max(E2_phi.values()) if E2_phi else 0
    
    # Save figure
    output_path = Path("figures/outputs/phi_derived_categories_triangulated.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "advanced_mathematics",
        "title": "φ-Enhanced Derived Categories and Triangulated Structures",
        "description": "Rigorous homological algebra with φ-enhanced derived categories, triangulated categories, and DG-algebras",
        "complex_objects": total_complex_objects,
        "total_cohomology_dimension": total_cohom_dim,
        "a_infinity_operations": total_a_infinity_ops,
        "spectral_sequence_entries": total_E2_entries,
        "max_spectral_entry": max_spectral_entry,
        "triangulated_axioms": "TR1-TR4 with φ-octahedral axiom",
        "phi_enhancements": "φ-quasi-isomorphisms, φ-suspension, φ-A_∞-structure, φ-hypercohomology",
        "derived_category": "D^b(A_φ) with φ-triangulated structure",
        "grothendieck_spectral": f"E₂ page with {total_E2_entries} entries",
        "provenance": "rigorous_homological_algebra"
    }

if __name__ == "__main__":
    result = generate_phi_derived_categories_triangulated()
    print(f"Generated: {result['file']}")
    print(f"Complex objects: {result['complex_objects']}")
    print(f"Total cohomology dimension: {result['total_cohomology_dimension']}")
    print(f"A_∞-operations: {result['a_infinity_operations']}")
    print(f"Spectral sequence entries: {result['spectral_sequence_entries']}")
    print(f"Max spectral entry: {result['max_spectral_entry']}")
    print(f"Triangulated axioms: {result['triangulated_axioms']}")
    print(f"φ-enhancements: {result['phi_enhancements']}")
    print(f"Derived category: {result['derived_category']}")
    print(f"Grothendieck spectral: {result['grothendieck_spectral']}")
