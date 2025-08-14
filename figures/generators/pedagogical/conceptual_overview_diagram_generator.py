#!/usr/bin/env python3
"""
FIRM Theory Conceptual Overview Diagram Generator
Creates comprehensive big-picture visualization of how FIRM theory unifies all physics
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np
from pathlib import Path
from typing import Dict, Any

def generate_conceptual_overview_diagram() -> Dict[str, Any]:
    """Generate comprehensive FIRM theory conceptual overview."""
    
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Central φ-recursion core
    core_circle = patches.Circle((8, 6), 1.5, facecolor='#ff6b6b', alpha=0.8, 
                                edgecolor='darkred', linewidth=3)
    ax.add_patch(core_circle)
    ax.text(8, 6, "φ-RECURSION\nMATHEMATICS\n\nGrace Operator\nFixed Points", 
           ha='center', va='center', fontsize=12, weight='bold', color='white')
    
    # Major physics domains emerging from core - better aligned grid
    domains = [
        # (x, y, width, height, title, color, details)
        (3.5, 9.5, 2.8, 1.4, "PARTICLE PHYSICS", "#2ca02c", "Quarks, Leptons, Bosons\nSM Parameters\nMasses & Couplings"),
        (12.5, 9.5, 2.8, 1.4, "COSMOLOGY", "#1f77b4", "CMB, BAO, SNe\nDark Matter/Energy\nInflation, BBN"),
        (3.5, 7.5, 2.8, 1.4, "MATHEMATICS", "#8c564b", "Category Theory\nTopos Structure\nAxiomatic Foundation"),
        (12.5, 7.5, 2.8, 1.4, "SPACETIME", "#e377c2", "Einstein Equations\nMetric Emergence\nGravitational Waves"),
        (3.5, 4.5, 2.8, 1.4, "CONSCIOUSNESS", "#9467bd", "P=NP Correlation\nNeural φ-Harmonics\nInformation Integration"),
        (12.5, 4.5, 2.8, 1.4, "FIELD THEORY", "#ff7f0e", "Gauge Fields\nSymmetry Breaking\nLagrangian Dynamics"),
    ]
    
    # Draw domain boxes and connections
    for x, y, w, h, title, color, details in domains:
        # Domain box
        box = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.1",
                            facecolor=color, alpha=0.7, edgecolor='black', linewidth=2)
        ax.add_patch(box)
        
        # Title and details
        ax.text(x, y+0.3, title, ha='center', va='center', fontsize=11, 
               weight='bold', color='white')
        ax.text(x, y-0.3, details, ha='center', va='center', fontsize=9, 
               color='white', style='italic')
        
        # Connection to core
        connection = ConnectionPatch((x, y), (8, 6), "data", "data",
                                   arrowstyle="->", shrinkA=50, shrinkB=75,
                                   mutation_scale=20, fc=color, alpha=0.6, linewidth=2)
        ax.add_artist(connection)
    
    # Add mathematical foundation layers - better spaced and aligned
    foundation_layers = [
        (8, 0.6, "AXIOM LAYER: A_Grace, A_Ψ, A_Psi", "#34495e"),
        (8, 1.2, "TOPOS LAYER: Grothendieck Universes", "#2c3e50"),
        (8, 1.8, "CATEGORY LAYER: Fixed Point Categories", "#1a252f"),
    ]
    
    for x, y, text, color in foundation_layers:
        box = FancyBboxPatch((x-4.5, y-0.25), 9, 0.5, boxstyle="round,pad=0.05",
                            facecolor=color, alpha=0.9, edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=10, 
               color='white', weight='bold')
    
    # Add emergence arrows - centered and evenly spaced
    emergence_levels = [
        (8, 3, "MATHEMATICAL EMERGENCE", 11),
        (8, 5.5, "PHYSICAL EMERGENCE", 11),
        (8, 8.5, "PHENOMENOLOGICAL EMERGENCE", 11),
        (8, 10.5, "OBSERVATIONAL PREDICTIONS", 11),
    ]
    
    for x, y, text, fontsize in emergence_levels:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
               weight='bold', alpha=0.8, 
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.3))
    
    # Add validation cycle - better aligned corners
    validation_points = [
        (14.5, 8.5, "EXPERIMENTAL\nVERIFICATION"),
        (14.5, 3.5, "THEORETICAL\nVALIDATION"),
        (1.5, 3.5, "MATHEMATICAL\nPROOFS"),
        (1.5, 8.5, "OBSERVATIONAL\nTESTS"),
    ]
    
    for i, (x, y, text) in enumerate(validation_points):
        circle = patches.Circle((x, y), 0.9, facecolor='lightblue', alpha=0.7, 
                               edgecolor='blue', linewidth=2.5)
        ax.add_patch(circle)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, weight='bold',
                bbox=dict(boxstyle="round,pad=0.1", facecolor='white', alpha=0.8))
        
        # Connect validation cycle with better arrows
        next_i = (i + 1) % len(validation_points)
        next_x, next_y, _ = validation_points[next_i]
        arrow = ConnectionPatch((x, y), (next_x, next_y), "data", "data",
                               arrowstyle="->", shrinkA=45, shrinkB=45,
                               mutation_scale=18, fc='blue', alpha=0.7, linewidth=2)
        ax.add_artist(arrow)
    
    # Add predictions and implications
    predictions = [
        (8, 11, "FIRM PREDICTIONS & IMPLICATIONS", 14, 'red'),
        (4, 11.5, "• All physical constants derived\n• Dark matter/energy explained\n• Consciousness quantified", 10, 'darkred'),
        (12, 11.5, "• Quantum gravity unified\n• Information paradoxes resolved\n• Technological applications", 10, 'darkred'),
    ]
    
    for x, y, text, fontsize, color in predictions:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
               weight='bold', color=color)
    
    # Title and subtitle
    ax.text(8, 12.5, "FIRM THEORY: COMPLETE CONCEPTUAL OVERVIEW", 
           ha='center', va='center', fontsize=18, weight='bold')
    ax.text(8, 12, "Unification of All Physics Through φ-Recursion Mathematics", 
           ha='center', va='center', fontsize=14, style='italic', alpha=0.8)
    
    # Add φ symbols for decoration
    phi_positions = [(1, 11), (15, 11), (1, 1), (15, 1)]
    for x, y in phi_positions:
        ax.text(x, y, "φ", ha='center', va='center', fontsize=24, 
               color='gold', weight='bold', alpha=0.7)
    
    # Formatting
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 13)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    # Save figure
    output_path = Path("../../canonical_outputs/conceptual_overview_diagram.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "pedagogical", 
        "title": "FIRM Theory Complete Conceptual Overview",
        "description": "Big picture visualization of how φ-recursion unifies all physics",
        "domains_covered": len(domains),
        "provenance": "comprehensive_conceptual_synthesis"
    }

if __name__ == "__main__":
    result = generate_conceptual_overview_diagram()
    print(f"Generated: {result['file']}")
    print(f"Physics domains: {result['domains_covered']}")
