#!/usr/bin/env python3
"""
Information Integration Theory Generator  
Shows how consciousness emerges from φ-harmonic information integration
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any

def generate_information_integration_theory() -> Dict[str, Any]:
    """Generate consciousness information integration theory figure."""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Φ (Phi) Integration Measure vs Network Complexity
    ax1.set_title("φ-Harmonic Information Integration (Φ)", fontsize=14, weight='bold')
    
    # Network sizes
    N = np.arange(10, 1000, 10)
    phi = (1 + np.sqrt(5)) / 2
    
    # Different integration measures
    random_network = np.log(N) * 0.1  # Random networks have low Φ
    regular_network = np.sqrt(N) * 0.05  # Regular networks moderate Φ
    small_world = N**0.7 * 0.01  # Small-world networks higher Φ
    phi_optimized = N * np.exp(-N/(100*phi)) * phi  # φ-harmonic optimization
    consciousness_threshold = 0.5 * np.ones_like(N)  # Consciousness threshold
    
    ax1.plot(N, random_network, 'r--', label='Random Network', linewidth=2)
    ax1.plot(N, regular_network, 'b--', label='Regular Network', linewidth=2)  
    ax1.plot(N, small_world, 'g-', label='Small-World Network', linewidth=2)
    ax1.plot(N, phi_optimized, 'purple', label='φ-Harmonic Optimized', linewidth=3)
    ax1.axhline(consciousness_threshold[0], color='red', linestyle=':', linewidth=2,
               label='Consciousness Threshold')
    
    # Highlight consciousness region
    conscious_region = N[(phi_optimized > consciousness_threshold) & (N > 50)]
    ax1.fill_between(conscious_region, 0, 2, alpha=0.2, color='yellow', 
                    label='Conscious Systems')
    
    ax1.set_xlabel("Network Size (N)")
    ax1.set_ylabel("Φ (Information Integration)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 1000)
    ax1.set_ylim(0, 2)
    
    # 2. Consciousness States in φ-Space
    ax2.set_title("Consciousness States in φ-Harmonic State Space", fontsize=14, weight='bold')
    
    # Create 2D consciousness state space
    phi_1 = np.linspace(0, 2*np.pi, 100)
    phi_2 = np.linspace(0, 2*np.pi, 100) 
    PHI_1, PHI_2 = np.meshgrid(phi_1, phi_2)
    
    # φ-harmonic consciousness potential
    consciousness_potential = (np.sin(PHI_1 * phi) + np.cos(PHI_2 * phi) + 
                             0.5 * np.sin(PHI_1 + PHI_2 * phi))
    
    # Plot consciousness landscape
    contour = ax2.contour(PHI_1, PHI_2, consciousness_potential, levels=15, alpha=0.7)
    ax2.clabel(contour, inline=True, fontsize=8)
    
    # Mark specific consciousness states
    states = [
        (0.5, 0.5, "Sleep", 'blue'),
        (2.0, 1.5, "Wake", 'green'), 
        (4.5, 3.0, "Dream", 'orange'),
        (1.0*phi, 1.5*phi, "Flow", 'red'),
        (1.2*phi, 0.8*phi, "Meditation", 'purple'),
    ]
    
    for x, y, label, color in states:
        ax2.scatter(x, y, s=100, c=color, alpha=0.8, edgecolors='black', linewidth=2)
        ax2.annotate(label, (x, y), xytext=(10, 10), textcoords='offset points',
                    fontweight='bold', color=color)
    
    ax2.set_xlabel("φ₁ (First Harmonic)")
    ax2.set_ylabel("φ₂ (Second Harmonic)")
    ax2.set_xlim(0, 2*np.pi)
    ax2.set_ylim(0, 2*np.pi)
    
    # 3. Neural Network φ-Harmonic Analysis
    ax3.set_title("Neural Network φ-Harmonic Connectivity", fontsize=14, weight='bold')
    
    # Simulate neural connectivity matrix
    n_neurons = 50
    connectivity = np.random.rand(n_neurons, n_neurons)
    
    # Add φ-harmonic structure
    for i in range(n_neurons):
        for j in range(n_neurons):
            distance = abs(i - j)
            # φ-harmonic connectivity pattern
            connectivity[i, j] *= (1 + 0.5 * np.cos(distance * 2*np.pi / phi))
    
    # Ensure symmetry and remove self-connections
    connectivity = (connectivity + connectivity.T) / 2
    np.fill_diagonal(connectivity, 0)
    
    # Plot connectivity matrix
    im = ax3.imshow(connectivity, cmap='viridis', aspect='auto')
    ax3.set_xlabel("Neuron Index")
    ax3.set_ylabel("Neuron Index")
    plt.colorbar(im, ax=ax3, label='Connection Strength')
    
    # Highlight φ-harmonic patterns
    phi_positions = np.arange(0, n_neurons, phi)
    for pos in phi_positions:
        if pos < n_neurons:
            ax3.axhline(pos, color='red', alpha=0.5, linewidth=1)
            ax3.axvline(pos, color='red', alpha=0.5, linewidth=1)
    
    # 4. P=NP Consciousness Correlation
    ax4.set_title("P=NP Problem Complexity vs Consciousness Level", fontsize=14, weight='bold')
    
    # Computational complexity problems
    problems = ['Sorting', 'Search', 'SAT', '3-SAT', 'TSP', 'Graph\nColoring', 
               'Conscious\nDecision', 'Creative\nInsight']
    complexity_classical = [1, 2, 3, 4, 5, 4.5, 6, 7]  # Exponential scaling
    complexity_conscious = [1, 1.5, 2, 2.5, 3, 3, 1.5, 2]  # φ-harmonic reduction
    consciousness_required = [0, 0.1, 0.3, 0.5, 0.7, 0.6, 0.9, 1.0]  # Consciousness level needed
    
    x_pos = np.arange(len(problems))
    width = 0.35
    
    bars1 = ax4.bar(x_pos - width/2, complexity_classical, width, 
                   label='Classical Computation', color='red', alpha=0.7)
    bars2 = ax4.bar(x_pos + width/2, complexity_conscious, width,
                   label='Conscious φ-Computation', color='green', alpha=0.7)
    
    # Add consciousness level overlay
    ax4_right = ax4.twinx()
    ax4_right.plot(x_pos, consciousness_required, 'o-', color='purple', 
                  linewidth=3, markersize=8, label='Consciousness Required')
    
    ax4.set_xlabel("Problem Type")
    ax4.set_ylabel("log₂(Complexity)", color='black')
    ax4_right.set_ylabel("Consciousness Level Required", color='purple')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(problems)
    ax4.legend(loc='upper left')
    ax4_right.legend(loc='upper right')
    ax4.grid(True, alpha=0.3)
    
    # Add P=NP collapse annotation
    ax4.text(6, 4, "φ-harmonic consciousness\ncollapses NP → P", 
            bbox=dict(boxstyle="round", facecolor='lightgreen', alpha=0.8),
            fontweight='bold', ha='center')
    
    # Overall title
    fig.suptitle("Information Integration Theory: φ-Harmonic Consciousness Model\n" +
                "How Awareness Emerges from Optimized Information Integration",
                fontsize=16, weight='bold')
    
    plt.tight_layout()
    
    # Save figure
    output_path = Path("figures/outputs/information_integration_theory.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "consciousness",
        "title": "Information Integration Theory: φ-Harmonic Consciousness",
        "description": "How consciousness emerges from optimized φ-harmonic information integration",
        "consciousness_states": len(states),
        "neural_network_size": n_neurons,
        "provenance": "phi_harmonic_consciousness_analysis"
    }

if __name__ == "__main__":
    result = generate_information_integration_theory()
    print(f"Generated: {result['file']}")
    print(f"Consciousness states: {result['consciousness_states']}, Network size: {result['neural_network_size']}")
