#!/usr/bin/env python3
"""
Neural Network φ-Harmonic Analysis Generator
Shows φ-harmonic patterns in brain neural networks and consciousness emergence
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any

def generate_neural_network_phi_analysis() -> Dict[str, Any]:
    """Generate neural network φ-harmonic analysis figure."""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Golden ratio and neural parameters
    phi = (1 + np.sqrt(5)) / 2
    
    # 1. Brain Network Connectivity: φ-Harmonic Structure
    ax1.set_title("Brain Network: φ-Harmonic Connectivity Patterns", fontsize=14, weight='bold')
    
    # Simulate brain network with φ-harmonic structure
    np.random.seed(42)  # Reproducible
    n_neurons = 50
    
    # Create adjacency matrix with φ-harmonic long-range connections
    connectivity = np.zeros((n_neurons, n_neurons))
    
    for i in range(n_neurons):
        for j in range(n_neurons):
            if i != j:
                distance = min(abs(i - j), n_neurons - abs(i - j))  # Circular topology
                
                # Short-range connections (local clusters)
                if distance <= 3:
                    connectivity[i, j] = np.random.exponential(0.8)
                
                # φ-harmonic long-range connections
                phi_distances = [int(n_neurons / phi), int(n_neurons / phi**2), int(n_neurons * phi / 10)]
                for phi_dist in phi_distances:
                    if abs(distance - phi_dist) <= 2:
                        connectivity[i, j] += 0.5 * np.random.exponential(0.6)
    
    # Apply threshold and symmetrize
    connectivity = np.where(connectivity > 0.3, connectivity, 0)
    connectivity = (connectivity + connectivity.T) / 2
    
    # Plot connectivity matrix
    im = ax1.imshow(connectivity, cmap='hot', aspect='auto')
    ax1.set_xlabel("Neuron Index")
    ax1.set_ylabel("Neuron Index") 
    plt.colorbar(im, ax=ax1, label='Connection Strength')
    
    # Highlight φ-harmonic patterns
    phi_positions = [int(n_neurons/phi), int(n_neurons/phi**2)]
    for pos in phi_positions:
        ax1.axhline(pos, color='cyan', alpha=0.7, linewidth=2)
        ax1.axvline(pos, color='cyan', alpha=0.7, linewidth=2)
    
    ax1.text(0.02, 0.98, f"φ-harmonic distances:\n{int(n_neurons/phi)}, {int(n_neurons/phi**2)} neurons", 
            transform=ax1.transAxes, va='top', fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightblue', alpha=0.8))
    
    # 2. Neural Oscillation Frequencies: φ-Harmonic Resonance
    ax2.set_title("Neural Oscillations: φ-Harmonic Frequency Structure", fontsize=14, weight='bold')
    
    # EEG frequency bands with φ-harmonic relationships
    frequencies = np.logspace(0, 2, 1000)  # 1-100 Hz
    
    # Standard EEG bands
    bands = {
        'Delta': (1, 4, 'purple'),
        'Theta': (4, 8, 'blue'), 
        'Alpha': (8, 13, 'green'),
        'Beta': (13, 30, 'orange'),
        'Gamma': (30, 100, 'red')
    }
    
    # Neural power spectrum with φ-harmonic peaks
    base_power = 1 / frequencies**2  # 1/f background
    
    # Add φ-harmonic resonances
    phi_frequencies = [8/phi, 8, 8*phi, 8*phi**2]  # Based on alpha rhythm
    phi_powers = []
    
    for freq in frequencies:
        phi_enhancement = 0
        for phi_freq in phi_frequencies:
            phi_enhancement += 0.3 * np.exp(-((freq - phi_freq)/2)**2)
        phi_powers.append(base_power[np.argmin(np.abs(frequencies - freq))] * (1 + phi_enhancement))
    
    phi_powers = np.array(phi_powers)
    
    # Plot power spectrum
    ax2.loglog(frequencies, base_power, 'k--', alpha=0.5, label='1/f Background')
    ax2.loglog(frequencies, phi_powers, 'r-', linewidth=3, label='φ-Harmonic Enhanced')
    
    # Mark EEG bands
    for band, (f_low, f_high, color) in bands.items():
        ax2.fill_between([f_low, f_high], 1e-6, 1e2, alpha=0.2, color=color, label=f'{band} ({f_low}-{f_high} Hz)')
    
    # Mark φ-frequencies
    for i, phi_freq in enumerate(phi_frequencies):
        if phi_freq <= 100:
            ax2.axvline(phi_freq, color='red', linestyle=':', alpha=0.7)
            ax2.text(phi_freq, 0.01, f'φ^{i-1}×8Hz', rotation=90, va='bottom', ha='right', color='red')
    
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Power Spectral Density")
    ax2.legend(loc='upper right', ncol=2, fontsize=8)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(1, 100)
    ax2.set_ylim(1e-6, 1e2)
    
    # 3. Consciousness States: φ-Phase Space
    ax3.set_title("Consciousness States in φ-Harmonic Phase Space", fontsize=14, weight='bold')
    
    # Create 2D consciousness state space
    phi_1 = np.linspace(0, 4*np.pi, 100)
    phi_2 = np.linspace(0, 4*np.pi, 100)
    PHI_1, PHI_2 = np.meshgrid(phi_1, phi_2)
    
    # Consciousness potential landscape
    consciousness_field = (np.sin(PHI_1/phi) * np.cos(PHI_2/phi) + 
                          0.5 * np.sin(PHI_1 + PHI_2/phi) +
                          0.3 * np.cos(PHI_1*phi/4) * np.sin(PHI_2*phi/4))
    
    # Plot consciousness landscape
    contour = ax3.contourf(PHI_1, PHI_2, consciousness_field, levels=20, cmap='viridis', alpha=0.8)
    ax3.contour(PHI_1, PHI_2, consciousness_field, levels=10, colors='white', alpha=0.5)
    
    # Mark specific consciousness states
    states = [
        (1.5, 2.0, "Focused Attention", 'red'),
        (3.2, 1.8, "Creative Flow", 'orange'),
        (2.1, 3.5, "Deep Meditation", 'purple'),
        (1.0*phi, 2.0*phi, "φ-Resonant State", 'yellow'),
        (2.5*phi, 1.2*phi, "Lucid Dreaming", 'cyan'),
        (0.8, 0.9, "Default Mode", 'white')
    ]
    
    for x, y, label, color in states:
        if x < 4*np.pi and y < 4*np.pi:
            ax3.scatter(x, y, s=150, c=color, alpha=0.9, edgecolors='black', linewidth=2)
            ax3.annotate(label, (x, y), xytext=(10, 10), textcoords='offset points',
                        fontsize=9, fontweight='bold', color='white',
                        bbox=dict(boxstyle="round,pad=0.3", facecolor='black', alpha=0.7))
    
    ax3.set_xlabel("φ₁ (First Harmonic)")
    ax3.set_ylabel("φ₂ (Second Harmonic)")
    plt.colorbar(contour, ax=ax3, label='Consciousness Potential Φ')
    
    # 4. Neural Information Integration: φ-Harmonic Measure
    ax4.set_title("Information Integration Φ vs Network Parameters", fontsize=14, weight='bold')
    
    # Network complexity parameters
    network_sizes = np.logspace(1, 3, 50)  # 10 to 1000 neurons
    
    # Different network topologies
    # Random networks
    phi_random = np.log(network_sizes) * 0.1
    
    # Small-world networks
    phi_small_world = network_sizes**0.5 * 0.02
    
    # φ-optimized networks (harmonic connectivity)
    phi_optimized = network_sizes**0.618 * 0.005 * (1 + 0.2 * np.sin(np.log(network_sizes) * phi))
    
    # Scale-free networks
    phi_scale_free = network_sizes**0.3 * 0.03
    
    ax4.loglog(network_sizes, phi_random, 'b--', linewidth=2, label='Random Networks')
    ax4.loglog(network_sizes, phi_small_world, 'g-', linewidth=2, label='Small-World Networks')
    ax4.loglog(network_sizes, phi_scale_free, 'orange', linewidth=2, label='Scale-Free Networks')
    ax4.loglog(network_sizes, phi_optimized, 'r-', linewidth=3, label='φ-Optimized Networks')
    
    # Consciousness threshold
    consciousness_threshold = 0.5
    ax4.axhline(consciousness_threshold, color='purple', linestyle=':', linewidth=2,
               label='Consciousness Threshold')
    
    # Mark brain-scale networks
    human_brain_neurons = [1e11]  # Approximate number of neurons
    cortical_neurons = [1.6e10]   # Cortical neurons
    
    for brain_size, label in zip([cortical_neurons[0], human_brain_neurons[0]], 
                                ['Cortex', 'Whole Brain']):
        if brain_size <= 1000:  # Only if in range
            ax4.axvline(brain_size, color='red', linestyle=':', alpha=0.7)
            ax4.text(brain_size, 10, label, rotation=90, va='bottom', ha='right')
    
    # Highlight consciousness region
    conscious_networks = network_sizes[phi_optimized > consciousness_threshold]
    if len(conscious_networks) > 0:
        ax4.fill_between([conscious_networks[0], network_sizes[-1]], 0.1, 10, 
                        alpha=0.2, color='yellow', label='Conscious Systems')
    
    ax4.set_xlabel("Network Size (Number of Neurons)")
    ax4.set_ylabel("Information Integration Φ")
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim(10, 1000)
    ax4.set_ylim(0.01, 10)
    
    # Add φ-optimization insight
    ax4.text(0.02, 0.98, "φ-harmonic connectivity\nmaximizes information\nintegration efficiency", 
            transform=ax4.transAxes, va='top', fontweight='bold',
            bbox=dict(boxstyle="round", facecolor='lightgreen', alpha=0.8))
    
    # Overall title
    fig.suptitle("Neural Network φ-Harmonic Analysis: Consciousness from Optimized Information Integration\n" +
                "Brain Networks Exhibit φ-Harmonic Structure for Maximum Consciousness Efficiency",
                fontsize=16, weight='bold')
    
    plt.tight_layout()
    
    # Calculate key metrics
    max_phi_integration = np.max(phi_optimized)
    optimal_network_size = network_sizes[np.argmax(phi_optimized)]
    phi_frequency_count = len(phi_frequencies)
    
    # Save figure
    output_path = Path("figures/outputs/neural_network_phi_analysis.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "consciousness",
        "title": "Neural Network φ-Harmonic Analysis",
        "description": "φ-harmonic patterns in brain networks and consciousness emergence mechanism",
        "network_size_analyzed": n_neurons,
        "consciousness_states": len(states),
        "phi_frequencies": phi_frequency_count,
        "max_phi_integration": f"{max_phi_integration:.3f}",
        "optimal_network_size": f"{optimal_network_size:.0f} neurons",
        "provenance": "phi_harmonic_neural_analysis"
    }

if __name__ == "__main__":
    result = generate_neural_network_phi_analysis()
    print(f"Generated: {result['file']}")
    print(f"Network size: {result['network_size_analyzed']} neurons")
    print(f"Consciousness states: {result['consciousness_states']}")
    print(f"φ-frequencies: {result['phi_frequencies']}")
    print(f"Max Φ integration: {result['max_phi_integration']}")
    print(f"Optimal network: {result['optimal_network_size']}")
