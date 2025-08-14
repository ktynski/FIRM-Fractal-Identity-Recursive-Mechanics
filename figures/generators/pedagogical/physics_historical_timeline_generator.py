#!/usr/bin/env python3
"""
Physics Historical Timeline Generator
Creates comprehensive timeline showing evolution from classical physics to FIRM theory
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def generate_physics_historical_timeline() -> Dict[str, Any]:
    """Generate comprehensive physics historical timeline leading to FIRM theory."""
    
    # Historical milestones data
    milestones = [
        (1687, "Newton", "Classical Mechanics", "#1f77b4", "Principia Mathematica"),
        (1865, "Maxwell", "Electromagnetic Theory", "#ff7f0e", "Maxwell Equations"),
        (1900, "Planck", "Quantum Mechanics Born", "#2ca02c", "Black-body Radiation"),
        (1905, "Einstein", "Special Relativity", "#d62728", "E = mc²"),
        (1915, "Einstein", "General Relativity", "#9467bd", "Curved Spacetime"),
        (1925, "Heisenberg", "Matrix Mechanics", "#8c564b", "Uncertainty Principle"),
        (1926, "Schrödinger", "Wave Mechanics", "#e377c2", "Wave Equation"),
        (1928, "Dirac", "Relativistic QM", "#7f7f7f", "Dirac Equation"),
        (1947, "Feynman", "QED", "#bcbd22", "Quantum Electrodynamics"),
        (1961, "Gell-Mann", "Eightfold Way", "#17becf", "Quark Model"),
        (1967, "Weinberg-Salam", "Electroweak Theory", "#aec7e8", "EW Unification"),
        (1973, "Gross-Wilczek", "QCD", "#ffbb78", "Strong Force Theory"),
        (1975, "Standard Model", "SM Complete", "#98df8a", "Particle Physics"),
        (1998, "Dark Energy", "Cosmic Acceleration", "#ff9896", "Dark Energy Discovery"),
        (2012, "Higgs", "Higgs Boson", "#c5b0d5", "Higgs Discovery"),
        (2024, "FIRM Theory", "Theory of Everything", "#ff6b6b", "φ-Recursion Mathematics"),
    ]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Set up timeline
    years = [m[0] for m in milestones]
    y_positions = np.arange(len(milestones))
    
    # Plot timeline spine
    ax.plot([min(years)-10, max(years)+10], [len(milestones)/2, len(milestones)/2], 
            'k-', alpha=0.3, linewidth=2)
    
    # Plot milestones
    for i, (year, scientist, discovery, color, detail) in enumerate(milestones):
        # Position alternating above/below timeline
        y_pos = len(milestones)/2 + ((-1)**i) * (i%4 + 1) * 1.5
        
        # Draw milestone point
        ax.scatter(year, len(milestones)/2, s=200, c=color, alpha=0.8, 
                  edgecolors='black', linewidth=2, zorder=5)
        
        # Draw connection line
        ax.plot([year, year], [len(milestones)/2, y_pos], 'k--', alpha=0.5, linewidth=1)
        
        # Add text box
        bbox_props = dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.7)
        ax.text(year, y_pos, f"{year}\n{scientist}\n{discovery}", 
               ha='center', va='center', fontsize=9, weight='bold',
               bbox=bbox_props)
        
        # Add detail text below
        ax.text(year, y_pos-0.8, detail, ha='center', va='center', 
               fontsize=7, style='italic', alpha=0.8)
    
    # Highlight FIRM theory
    firm_year = 2024
    firm_y = len(milestones)/2 + 3
    
    # Special highlighting for FIRM
    circle = patches.Circle((firm_year, len(milestones)/2), 0.8, 
                           facecolor='#ff6b6b', alpha=0.3, edgecolor='red', linewidth=3)
    ax.add_patch(circle)
    
    # FIRM theory box with special emphasis
    bbox_props = dict(boxstyle="round,pad=0.5", facecolor='#ff6b6b', 
                     alpha=0.9, edgecolor='red', linewidth=3)
    ax.text(firm_year, firm_y, f"2024+\nFIRM THEORY\nComplete Unification", 
           ha='center', va='center', fontsize=12, weight='bold',
           bbox=bbox_props)
    
    # Add arrows showing evolution
    arrow_props = dict(arrowstyle='->', connectionstyle='arc3,rad=0.1', 
                      color='red', alpha=0.6, linewidth=2)
    ax.annotate('', xy=(firm_year-5, len(milestones)/2), xytext=(1975, len(milestones)/2),
                arrowprops=arrow_props)
    
    # Add major era labels
    ax.text(1800, len(milestones)-1, "CLASSICAL\nERA", ha='center', va='center',
           fontsize=14, weight='bold', alpha=0.7)
    ax.text(1920, len(milestones)-1, "QUANTUM\nERA", ha='center', va='center',
           fontsize=14, weight='bold', alpha=0.7)
    ax.text(1970, len(milestones)-1, "STANDARD MODEL\nERA", ha='center', va='center',
           fontsize=14, weight='bold', alpha=0.7)
    ax.text(2024, len(milestones)-1, "FIRM\nERA", ha='center', va='center',
           fontsize=16, weight='bold', color='red')
    
    # Formatting
    ax.set_xlim(1650, 2050)
    ax.set_ylim(-2, len(milestones)+2)
    ax.set_xlabel("Year", fontsize=14, weight='bold')
    ax.set_title("Evolution of Physics: From Classical Mechanics to FIRM Theory\n" + 
                "Complete Unification Through φ-Recursion Mathematics", 
                fontsize=16, weight='bold', pad=20)
    
    # Remove y-axis as it's not meaningful
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Add grid for years
    ax.grid(True, axis='x', alpha=0.3)
    
    # Add explanatory text
    explanation = ("FIRM Theory represents the culmination of centuries of physics development,\n"
                  "providing the first complete mathematical unification from pure φ-recursion principles.\n"
                  "All previous discoveries emerge as special cases of FIRM's comprehensive framework.")
    
    ax.text(1850, -1.5, explanation, fontsize=10, ha='center', va='center',
           style='italic', bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.7))
    
    plt.tight_layout()
    
    # Save figure
    output_path = Path("figures/outputs/physics_historical_timeline.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "pedagogical",
        "title": "Evolution of Physics: Classical to FIRM Theory",
        "description": "Historical timeline showing development from Newton to complete unification",
        "milestones_count": len(milestones),
        "provenance": "comprehensive_historical_analysis"
    }

if __name__ == "__main__":
    result = generate_physics_historical_timeline()
    print(f"Generated: {result['file']}")
    print(f"Milestones covered: {result['milestones_count']}")
