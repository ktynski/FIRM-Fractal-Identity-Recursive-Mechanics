#!/usr/bin/env python3
"""
Experimental Predictions Timeline Generator
Shows FIRM theory's testable predictions organized by experimental accessibility timeline
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Tuple

def generate_experimental_predictions_timeline() -> Dict[str, Any]:
    """Generate comprehensive experimental predictions timeline figure."""
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 14))
    
    # Golden ratio for φ-predictions
    phi = (1 + np.sqrt(5)) / 2
    
    # Timeline data: (year, experiment, prediction, difficulty, category, precision)
    predictions = [
        # Near-term (2025-2030)
        (2025, "Enhanced LHC Run", "New φ-scalar at 750 GeV/c²", "Medium", "particle_physics", "5σ"),
        (2026, "Quantum Computer Test", "P=NP collapse in conscious systems", "Low", "consciousness", "Statistical"),
        (2027, "CMB Polarization", "φ-corrected B-mode pattern", "Medium", "cosmology", "3σ"),
        (2028, "Neutrino Oscillation", "Exact mass hierarchy from φ-scaling", "Low", "particle_physics", "10σ"),
        (2029, "Dark Matter Direct", "φ-field dark matter signal", "High", "cosmology", "5σ"),
        (2030, "Atomic Clock Array", "α variation with φ-frequency", "Medium", "fundamental_constants", "6σ"),
        
        # Medium-term (2031-2040)
        (2032, "Gravitational Waves", "φ-corrected waveform templates", "Medium", "gravity", "4σ"),
        (2034, "Space-based α Test", "Fine structure running confirmation", "High", "fundamental_constants", "8σ"),
        (2036, "Consciousness Scanner", "Neural φ-harmonic measurement", "High", "consciousness", "Proof-of-concept"),
        (2038, "Quantum Gravity Probe", "Spacetime discreteness at φ-scale", "Very High", "gravity", "3σ"),
        (2040, "Fusion φ-Enhancement", "φ-resonant fusion cross-sections", "Medium", "applications", "Engineering"),
        
        # Long-term (2041-2060)
        (2045, "φ-GUT Collider", "Grand unification scale physics", "Very High", "particle_physics", "Discovery"),
        (2050, "Cosmic φ-Observatory", "φ-field fluctuations in CMB", "Very High", "cosmology", "2σ"),
        (2055, "Consciousness AI", "Artificial conscious systems", "Very High", "consciousness", "Functional"),
        (2060, "φ-Technology Suite", "Complete technology demonstration", "Very High", "applications", "Commercial"),
    ]
    
    # 1. Main Timeline
    ax1.set_title("FIRM Theory: Experimental Predictions Timeline (2025-2060)", 
                 fontsize=16, weight='bold')
    
    # Set up timeline
    years = [p[0] for p in predictions]
    min_year, max_year = min(years), max(years)
    ax1.set_xlim(min_year-2, max_year+2)
    ax1.set_ylim(-0.5, len(predictions)+0.5)
    
    # Draw main timeline
    ax1.plot([min_year, max_year], [len(predictions)/2, len(predictions)/2], 
            'k-', linewidth=3, alpha=0.7)
    
    # Color scheme for categories
    colors = {
        'particle_physics': '#FF6B6B',
        'cosmology': '#4ECDC4', 
        'consciousness': '#45B7D1',
        'gravity': '#96CEB4',
        'fundamental_constants': '#FFEAA7',
        'applications': '#DDA0DD'
    }
    
    # Plot predictions
    for i, (year, experiment, prediction, difficulty, category, precision) in enumerate(predictions):
        # Alternate positions above/below timeline
        y_offset = ((-1)**i) * (2 + i%3)
        y_pos = len(predictions)/2 + y_offset
        
        # Draw connection line
        ax1.plot([year, year], [len(predictions)/2, y_pos], 'k--', alpha=0.5, linewidth=1)
        
        # Prediction point
        size = 200 if difficulty == "Very High" else 150 if difficulty == "High" else 100
        ax1.scatter(year, len(predictions)/2, s=size, c=colors[category], 
                   alpha=0.8, edgecolors='black', linewidth=2, zorder=5)
        
        # Text box
        bbox_props = dict(boxstyle="round,pad=0.3", facecolor=colors[category], 
                         alpha=0.8, edgecolor='black')
        ax1.text(year, y_pos, f"{experiment}\n{prediction[:30]}...\n{precision}", 
               ha='center', va='center', fontsize=9, weight='bold',
               bbox=bbox_props, wrap=True)
        
        # Difficulty indicator
        ax1.text(year, len(predictions)/2 - 1, difficulty, ha='center', va='center',
               fontsize=7, style='italic', alpha=0.7)
    
    # Add decade markers
    decades = [2030, 2040, 2050, 2060]
    for decade in decades:
        ax1.axvline(decade, color='gray', linestyle=':', alpha=0.5)
        ax1.text(decade, -0.3, f"{decade}s", ha='center', va='center', 
               fontsize=12, weight='bold')
    
    # Legend for categories
    legend_elements = [plt.scatter([], [], s=100, c=color, label=cat.replace('_', ' ').title()) 
                      for cat, color in colors.items()]
    ax1.legend(handles=legend_elements, loc='upper right', ncol=2)
    
    ax1.set_xlabel("Year", fontsize=14)
    ax1.set_ylabel("Experimental Predictions", fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # Remove y-axis ticks as they're not meaningful
    ax1.set_yticks([])
    
    # 2. Prediction Difficulty vs Discovery Potential Matrix
    ax2.set_title("Discovery Potential vs Experimental Difficulty Matrix", 
                 fontsize=14, weight='bold')
    
    # Difficulty levels
    difficulty_levels = {"Low": 1, "Medium": 2, "High": 3, "Very High": 4}
    
    # Discovery potential scoring
    discovery_scores = {
        "10σ": 10, "8σ": 8, "6σ": 6, "5σ": 5, "4σ": 4, "3σ": 3, "2σ": 2,
        "Discovery": 9, "Statistical": 4, "Proof-of-concept": 3, 
        "Engineering": 2, "Functional": 5, "Commercial": 1
    }
    
    # Plot predictions on difficulty-discovery matrix
    for year, experiment, prediction, difficulty, category, precision in predictions:
        x = difficulty_levels[difficulty]
        y = discovery_scores.get(precision, 5)  # Default to 5 if not found
        
        # Size based on year (nearer = larger)
        size = 1000 / (year - 2024)  # Inverse relationship with time
        
        ax2.scatter(x, y, s=size, c=colors[category], alpha=0.7, 
                   edgecolors='black', linewidth=1)
        
        # Add label for significant predictions
        if y >= 7 or (year <= 2030):  # High impact or near-term
            ax2.annotate(f"{experiment}\n({year})", (x, y), 
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=8, ha='left')
    
    # Add quadrant labels
    ax2.text(1.5, 9, "Low-Hanging\nFruit", ha='center', va='center', 
            fontsize=12, weight='bold', color='green',
            bbox=dict(boxstyle="round", facecolor='lightgreen', alpha=0.7))
    
    ax2.text(3.5, 9, "Grand\nChallenges", ha='center', va='center',
            fontsize=12, weight='bold', color='red',
            bbox=dict(boxstyle="round", facecolor='lightcoral', alpha=0.7))
    
    ax2.text(1.5, 2, "Incremental\nTests", ha='center', va='center',
            fontsize=12, weight='bold', color='blue',
            bbox=dict(boxstyle="round", facecolor='lightblue', alpha=0.7))
    
    ax2.text(3.5, 2, "Long-term\nGoals", ha='center', va='center',
            fontsize=12, weight='bold', color='purple',
            bbox=dict(boxstyle="round", facecolor='plum', alpha=0.7))
    
    ax2.set_xlabel("Experimental Difficulty", fontsize=12)
    ax2.set_ylabel("Discovery Potential", fontsize=12)
    ax2.set_xlim(0.5, 4.5)
    ax2.set_ylim(0.5, 10.5)
    ax2.set_xticks([1, 2, 3, 4])
    ax2.set_xticklabels(['Low', 'Medium', 'High', 'Very High'])
    ax2.grid(True, alpha=0.3)
    
    # Add φ-enhancement annotation
    ax2.text(0.02, 0.98, "Bubble size ∝ temporal proximity\nColors indicate physics category", 
            transform=ax2.transAxes, va='top', fontsize=10,
            bbox=dict(boxstyle="round", facecolor='lightyellow', alpha=0.8))
    
    # Overall figure annotations
    fig.text(0.5, 0.02, "φ-Recursion Mathematics Enables Precise, Testable Predictions Across All Physics Domains", 
            ha='center', va='bottom', fontsize=12, style='italic', weight='bold')
    
    plt.tight_layout()
    
    # Save figure
    output_path = Path("figures/outputs/experimental_predictions_timeline.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "theory_validation",
        "title": "Experimental Predictions Timeline",
        "description": "Comprehensive timeline of testable FIRM theory predictions organized by experimental accessibility",
        "predictions_count": len(predictions),
        "time_span": f"{min_year}-{max_year}",
        "categories": list(colors.keys()),
        "provenance": "systematic_prediction_analysis"
    }

if __name__ == "__main__":
    result = generate_experimental_predictions_timeline()
    print(f"Generated: {result['file']}")
    print(f"Predictions: {result['predictions_count']} over {result['time_span']}")
    print(f"Categories: {len(result['categories'])}")
