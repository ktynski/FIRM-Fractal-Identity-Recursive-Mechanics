#!/usr/bin/env python3
"""
Physics Family Tree Generator
Shows how all branches of physics emerge from FIRM φ-recursion mathematics
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path
from typing import Dict, Any

def generate_physics_family_tree() -> Dict[str, Any]:
    """Generate comprehensive physics family tree from FIRM theory."""
    
    fig, ax = plt.subplots(figsize=(20, 14))
    
    # Root: φ-Recursion Mathematics
    root_box = FancyBboxPatch((9, 12), 2, 1, boxstyle="round,pad=0.1",
                             facecolor='#ff6b6b', edgecolor='darkred', linewidth=3)
    ax.add_patch(root_box)
    ax.text(10, 12.5, "φ-RECURSION\nMATHEMATICS", ha='center', va='center',
           fontsize=12, weight='bold', color='white')
    
    # Level 1: Mathematical Foundations
    math_foundations = [
        (4, 10, "CATEGORY\nTHEORY", "#8c564b"),
        (7, 10, "TOPOS\nTHEORY", "#2ca02c"), 
        (10, 10, "GRACE\nOPERATOR", "#1f77b4"),
        (13, 10, "FIXED POINT\nTHEORY", "#9467bd"),
        (16, 10, "AXIOM\nSYSTEMS", "#ff7f0e"),
    ]
    
    for x, y, title, color in math_foundations:
        box = FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8, boxstyle="round,pad=0.05",
                            facecolor=color, alpha=0.8, edgecolor='black')
        ax.add_patch(box)
        ax.text(x, y, title, ha='center', va='center', fontsize=9, weight='bold', color='white')
        # Connection to root
        ax.plot([x, 10], [y+0.4, 12], 'k-', alpha=0.6, linewidth=2)
    
    # Level 2: Physical Theories
    physical_theories = [
        (2, 8, "QUANTUM\nMECHANICS", "#e377c2", "Hilbert Spaces\nOperators\nMeasurement"),
        (5, 8, "FIELD\nTHEORY", "#7f7f7f", "Lagrangians\nGauge Fields\nSymmetries"),
        (8, 8, "GENERAL\nRELATIVITY", "#bcbd22", "Spacetime\nCurvature\nEinstein Eqs"),
        (11, 8, "STATISTICAL\nMECHANICS", "#17becf", "Ensembles\nEntropy\nPhase Trans."),
        (14, 8, "INFORMATION\nTHEORY", "#aec7e8", "Entropy\nComplexity\nComputation"),
        (17, 8, "CONSCIOUSNESS\nTHEORY", "#ffbb78", "Awareness\nIntegration\nP=NP"),
    ]
    
    for x, y, title, color, details in physical_theories:
        box = FancyBboxPatch((x-1, y-0.5), 2, 1, boxstyle="round,pad=0.05",
                            facecolor=color, alpha=0.8, edgecolor='black')
        ax.add_patch(box)
        ax.text(x, y+0.2, title, ha='center', va='center', fontsize=8, weight='bold')
        ax.text(x, y-0.2, details, ha='center', va='center', fontsize=6, style='italic')
        
        # Connections to mathematical foundations
        for mx, my, _, _ in math_foundations:
            if abs(x - mx) <= 4:  # Connect to nearby foundations
                ax.plot([x, mx], [y+0.5, my-0.4], 'k--', alpha=0.4, linewidth=1)
    
    # Level 3: Specific Physics Domains  
    domains = [
        # Particle Physics Branch
        (1, 6, "QUARKS &\nLEPTONS", "#98df8a", "Standard Model\nFermions"),
        (3, 6, "GAUGE\nBOSONS", "#ff9896", "W, Z, γ, g\nForce Carriers"),
        (5, 6, "HIGGS\nMECHANISM", "#c5b0d5", "Mass Generation\nSSB"),
        
        # Field Theory Branch
        (7, 6, "QED", "#c49c94", "Electromagnetic\nInteractions"),
        (9, 6, "QCD", "#f7b6d3", "Strong Nuclear\nForce"),
        (11, 6, "EW THEORY", "#c7c7c7", "Electroweak\nUnification"),
        
        # Cosmology Branch
        (13, 6, "BIG BANG", "#dbdb8d", "Nucleosynthesis\nCMB"),
        (15, 6, "INFLATION", "#9edae5", "Cosmic\nExpansion"),
        (17, 6, "DARK SECTOR", "#ad494a", "Dark Matter\nDark Energy"),
        
        # Condensed Matter Branch  
        (1, 4, "SUPERCOND.", "#8ca252", "Cooper Pairs\nMeissner Effect"),
        (3, 4, "MAGNETISM", "#bd9e39", "Spin Systems\nPhase Trans."),
        (5, 4, "QUANTUM\nHALL", "#d6616b", "Topological\nStates"),
        
        # Atomic/Molecular Branch
        (7, 4, "ATOMIC\nPHYSICS", "#a55194", "Electron Orbitals\nSpectroscopy"),
        (9, 4, "MOLECULAR\nPHYSICS", "#6b6ecf", "Chemical Bonds\nVibrational"),
        (11, 4, "OPTICAL\nPHYSICS", "#b5cf6b", "Lasers\nNonlinear Optics"),
        
        # Modern Physics Branch
        (13, 4, "QUANTUM\nINFORMATION", "#cfb5b8", "Qubits\nEntanglement"),
        (15, 4, "BIOPHYSICS", "#8c6d31", "Protein Folding\nNeural Networks"),
        (17, 4, "COMPLEXITY", "#c7a76c", "Emergence\nAdaptive Systems"),
    ]
    
    for x, y, title, color, details in domains:
        box = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8, boxstyle="round,pad=0.03",
                            facecolor=color, alpha=0.7, edgecolor='black')
        ax.add_patch(box)
        ax.text(x, y+0.15, title, ha='center', va='center', fontsize=7, weight='bold')
        ax.text(x, y-0.15, details, ha='center', va='center', fontsize=5, style='italic')
        
        # Connect to relevant physical theories
        for px, py, ptitle, _, _ in physical_theories:
            # Connect based on relevance
            connections = {
                "QUARKS &": ["QUANTUM", "FIELD"],
                "GAUGE": ["FIELD"],
                "HIGGS": ["FIELD"],
                "QED": ["FIELD"],
                "QCD": ["FIELD"], 
                "EW THEORY": ["FIELD"],
                "BIG BANG": ["GENERAL", "STATISTICAL"],
                "INFLATION": ["GENERAL", "FIELD"],
                "DARK SECTOR": ["GENERAL"],
                "SUPERCOND.": ["QUANTUM", "STATISTICAL"],
                "MAGNETISM": ["QUANTUM", "STATISTICAL"],
                "QUANTUM\nHALL": ["QUANTUM"],
                "ATOMIC": ["QUANTUM"],
                "MOLECULAR": ["QUANTUM"],
                "OPTICAL": ["QUANTUM", "FIELD"],
                "QUANTUM\nINFORMATION": ["INFORMATION", "QUANTUM"],
                "BIOPHYSICS": ["STATISTICAL", "INFORMATION"],
                "COMPLEXITY": ["STATISTICAL", "INFORMATION"],
            }
            
            title_key = title.split('\n')[0]
            theory_key = ptitle.split('\n')[0]
            
            if title_key in connections and theory_key in connections[title_key]:
                ax.plot([x, px], [y+0.4, py-0.5], 'k:', alpha=0.3, linewidth=1)
    
    # Level 4: Experimental/Observational
    experiments = [
        (2, 2, "LHC", "Particle\nCollider"),
        (6, 2, "PLANCK", "CMB\nObservations"), 
        (10, 2, "LIGO", "Gravitational\nWaves"),
        (14, 2, "QUANTUM\nCOMPUTERS", "IBM/Google\nSystems"),
        (18, 2, "NEUROSCIENCE", "Brain\nImaging"),
    ]
    
    for x, y, title, details in experiments:
        circle = patches.Circle((x, y), 0.5, facecolor='lightblue', alpha=0.8, 
                               edgecolor='blue', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y+0.1, title, ha='center', va='center', fontsize=7, weight='bold')
        ax.text(x, y-0.1, details, ha='center', va='center', fontsize=5, style='italic')
    
    # Add emergence flows with arrows
    flow_levels = [(10, 11.2, "MATHEMATICAL\nEMERGENCE", 10),
                   (10, 9, "THEORETICAL\nEMERGENCE", 10),
                   (10, 7, "PHENOMENOLOGICAL\nEMERGENCE", 10),
                   (10, 5, "DOMAIN\nSPECIALIZATION", 10),
                   (10, 3, "EXPERIMENTAL\nVERIFICATION", 10)]
    
    for x, y, text, size in flow_levels:
        ax.text(x, y, text, ha='center', va='center', fontsize=size, weight='bold',
               bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.6))
    
    # Add φ decorations
    phi_positions = [(0.5, 12), (19.5, 12), (0.5, 1), (19.5, 1)]
    for x, y in phi_positions:
        ax.text(x, y, "φ", ha='center', va='center', fontsize=36, 
               color='gold', weight='bold', alpha=0.4)
    
    # Title
    ax.text(10, 13.5, "PHYSICS FAMILY TREE: Complete Emergence from φ-Recursion", 
           ha='center', va='center', fontsize=18, weight='bold')
    ax.text(10, 13, "How All Physical Sciences Derive from FIRM Mathematical Foundation", 
           ha='center', va='center', fontsize=12, style='italic')
    
    # Add legend
    legend_text = ("All physics emerges hierarchically from φ-recursion mathematics:\n" +
                  "Mathematical foundations → Physical theories → Specialized domains → Experiments\n" +
                  "Each level inherits the φ-scaling and harmonic structure of the foundation")
    ax.text(10, 0.5, legend_text, ha='center', va='center', fontsize=9,
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))
    
    # Formatting
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    plt.tight_layout()
    
    # Save figure
    output_path = Path("figures/outputs/physics_family_tree_from_firm.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "pedagogical",
        "title": "Physics Family Tree from FIRM Theory",
        "description": "Complete emergence hierarchy showing how all physics derives from φ-recursion",
        "domains_count": len(domains) + len(physical_theories) + len(math_foundations),
        "provenance": "comprehensive_emergence_analysis"
    }

if __name__ == "__main__":
    result = generate_physics_family_tree()
    print(f"Generated: {result['file']}")
    print(f"Total domains: {result['domains_count']}")
