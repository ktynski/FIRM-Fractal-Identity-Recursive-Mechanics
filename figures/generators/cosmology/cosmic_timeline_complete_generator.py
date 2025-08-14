#!/usr/bin/env python3
"""
Complete Cosmic Timeline Generator
Shows comprehensive cosmic history from Big Bang to present with φ-field evolution
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any, List, Tuple

def generate_cosmic_timeline_complete() -> Dict[str, Any]:
    """Generate complete cosmic timeline with φ-field evolution."""
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 14))
    
    # Golden ratio and cosmological parameters
    phi = (1 + np.sqrt(5)) / 2
    
    # 1. Main Cosmic Timeline
    ax1.set_title("Complete Cosmic Timeline: φ-Field Evolution from Big Bang to Present", 
                 fontsize=16, weight='bold')
    
    # Cosmic events with times, descriptions, and φ-field states
    events = [
        # (time_seconds, redshift, event, description, phi_state, color)
        (0, np.inf, "Big Bang", "Spacetime emergence", "φ-singularity", '#FF0000'),
        (1e-43, 1e30, "Planck Epoch", "Quantum gravity era", "φ-quantum foam", '#FF4444'),
        (1e-36, 1e29, "Inflation", "φ-field drives expansion", "φ-inflaton active", '#FF8800'),
        (1e-32, 1e28, "Reheating", "φ→radiation conversion", "φ-decay products", '#FFAA00'),
        (1, 1e10, "Big Bang Nucleosynthesis", "Light element synthesis", "φ-thermal equilibrium", '#AAFF00'),
        (380000, 1100, "Recombination", "First atoms form", "φ-matter coupling", '#00FF00'),
        (200e6, 20, "First Stars", "Stellar ignition", "φ-gravitational collapse", '#00FFAA'),
        (1e9, 6, "First Galaxies", "Large structure formation", "φ-dark matter halos", '#00AAFF'),
        (9e9, 0.7, "Dark Energy Dominance", "Accelerated expansion", "φ-dark energy active", '#0088FF'),
        (13.8e9, 0, "Present Day", "Current cosmic state", "φ-mature universe", '#4444FF'),
        (100e9, -0.7, "Heat Death", "Maximum entropy", "φ-equilibrium", '#8888FF'),
    ]
    
    # Extract data
    times = np.array([e[0] for e in events[:-1]])  # Exclude future
    redshifts = np.array([e[1] for e in events[:-1]])
    event_names = [e[2] for e in events[:-1]]
    descriptions = [e[3] for e in events[:-1]]
    phi_states = [e[4] for e in events[:-1]]
    colors = [e[5] for e in events[:-1]]
    
    # Main timeline
    ax1.semilogx(times, redshifts, 'k-', linewidth=3, alpha=0.7)
    
    # Plot events
    for i, (time, z, name, desc, phi_state, color) in enumerate(events[:-1]):
        # Event point
        ax1.scatter(time, z, s=200, c=color, alpha=0.8, edgecolors='black', linewidth=2, zorder=5)
        
        # Event labels with alternating positions
        y_offset = ((-1)**i) * (0.3 + 0.1*i) * np.log10(z+1)
        y_text = z + y_offset
        
        # Connection line
        ax1.plot([time, time], [z, y_text], 'k--', alpha=0.5, linewidth=1)
        
        # Text box
        ax1.annotate(f"{name}\n{desc}\nφ-state: {phi_state}", 
                    (time, y_text), xytext=(0, 20 if y_offset > 0 else -20),
                    textcoords='offset points', ha='center', va='bottom' if y_offset > 0 else 'top',
                    fontsize=9, weight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.8, edgecolor='black'))
    
    # Add cosmic epochs
    epoch_ranges = [
        (1e-43, 1e-32, "Quantum Era", '#FFE6E6'),
        (1e-32, 380000, "Radiation Dominated", '#E6F3FF'),
        (380000, 9e9, "Matter Dominated", '#E6FFE6'),
        (9e9, 13.8e9, "Dark Energy Dominated", '#F0E6FF')
    ]
    
    for t_start, t_end, epoch, color in epoch_ranges:
        ax1.axvspan(t_start, t_end, alpha=0.2, color=color, label=epoch)
    
    ax1.set_xlabel("Time Since Big Bang (seconds)", fontsize=14)
    ax1.set_ylabel("Redshift z", fontsize=14)
    ax1.set_xlim(1e-44, 2e10)
    ax1.set_ylim(-1, 1e12)
    ax1.set_yscale('log')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    
    # 2. φ-Field Evolution and Physical Parameters
    ax2.set_title("φ-Field Evolution and Key Physical Parameters", fontsize=14, weight='bold')
    
    # Time array for continuous evolution
    t_evolution = np.logspace(-43, 10, 1000)  # 10^-43 to 10^10 seconds
    
    # φ-field value evolution
    phi_field_value = np.zeros_like(t_evolution)
    
    # Different epochs with different φ-field behavior
    for i, t in enumerate(t_evolution):
        if t < 1e-36:  # Pre-inflation
            phi_field_value[i] = 10 * np.exp(-t * 1e36)  # High field value
        elif t < 1e-32:  # Inflation
            phi_field_value[i] = 5 * (1 + np.sin(np.log(t) * phi))  # Inflaton field
        elif t < 1:  # Radiation era
            phi_field_value[i] = 1 * t**(-0.25)  # Decreasing with expansion
        elif t < 380000:  # Matter formation
            phi_field_value[i] = 0.5 * (1 + 0.1 * np.sin(phi * np.log(t)))  # Oscillatory
        elif t < 9e9:  # Matter dominated
            phi_field_value[i] = 0.1 * (1 + 0.2 * np.cos(phi * np.log(t) / 10))  # Slow evolution
        else:  # Dark energy era
            phi_field_value[i] = 0.3 * np.exp((t - 9e9) / 50e9)  # Dark energy rise
    
    # Plot φ-field evolution
    ax2_field = ax2
    ax2_field.loglog(t_evolution, np.abs(phi_field_value), 'r-', linewidth=3, label='|φ-Field Value|')
    
    # Scale factor evolution a(t)
    scale_factor = np.zeros_like(t_evolution)
    for i, t in enumerate(t_evolution):
        if t < 1e-32:  # Inflation: exponential expansion
            scale_factor[i] = 1e-30 * np.exp(t * 1e32 / phi)
        elif t < 380000:  # Radiation: a ∝ √t
            scale_factor[i] = 1e-15 * np.sqrt(t)
        elif t < 9e9:  # Matter: a ∝ t^(2/3)
            scale_factor[i] = 1e-10 * t**(2/3)
        else:  # Dark energy: accelerating
            scale_factor[i] = 1e-10 * (9e9)**(2/3) * np.exp((t - 9e9) / 20e9)
    
    ax2_scale = ax2.twinx()
    ax2_scale.loglog(t_evolution, scale_factor, 'b-', linewidth=3, label='Scale Factor a(t)')
    
    # Temperature evolution
    temperature = np.zeros_like(t_evolution)
    for i, t in enumerate(t_evolution):
        if t < 1e-32:  # Very early: Planck temperature
            temperature[i] = 1e19 * (1e-43 / (t + 1e-44))**0.25
        elif t < 1:  # Radiation era: T ∝ t^(-1/2)
            temperature[i] = 1e10 / np.sqrt(t)
        elif t < 380000:  # Before recombination
            temperature[i] = 3000 * (380000 / t)**0.5
        else:  # After recombination: CMB temperature
            temperature[i] = 2.7 * (1 + redshifts[np.argmin(np.abs(times - t))])
    
    ax2_temp = ax2.twinx()
    ax2_temp.spines['right'].set_position(('outward', 60))
    ax2_temp.loglog(t_evolution, temperature, 'orange', linewidth=3, label='Temperature (K)')
    
    # Mark key transitions
    transition_times = [1e-36, 1e-32, 1, 380000, 9e9]
    transition_names = ['Inflation\nStart', 'Inflation\nEnd', 'BBN', 'Recomb.', 'Dark Energy']
    
    for t_trans, name in zip(transition_times, transition_names):
        if t_trans <= 1e10:
            ax2.axvline(t_trans, color='gray', linestyle=':', alpha=0.7)
            ax2.text(t_trans, 1e-2, name, rotation=90, va='bottom', ha='right', 
                    fontsize=8, alpha=0.8)
    
    # Labels and formatting
    ax2_field.set_xlabel("Time Since Big Bang (seconds)", fontsize=12)
    ax2_field.set_ylabel("φ-Field Value", color='red', fontsize=12)
    ax2_scale.set_ylabel("Scale Factor a(t)", color='blue', fontsize=12)
    ax2_temp.set_ylabel("Temperature (K)", color='orange', fontsize=12)
    
    ax2_field.tick_params(axis='y', labelcolor='red')
    ax2_scale.tick_params(axis='y', labelcolor='blue')
    ax2_temp.tick_params(axis='y', labelcolor='orange')
    
    ax2_field.grid(True, alpha=0.3)
    ax2_field.set_xlim(1e-43, 2e10)
    
    # Add legends
    ax2_field.legend(loc='upper left')
    ax2_scale.legend(loc='upper center')
    ax2_temp.legend(loc='upper right')
    
    # Overall figure formatting
    plt.tight_layout()
    
    # Add φ-field insights
    fig.text(0.02, 0.02, 
            "φ-Field drives all major cosmic transitions: inflation, dark matter clustering, dark energy acceleration",
            ha='left', va='bottom', fontsize=12, style='italic', weight='bold')
    
    # Save figure
    output_path = Path("figures/outputs/cosmic_timeline_complete.png")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    return {
        "file": str(output_path),
        "category": "cosmology", 
        "title": "Complete Cosmic Timeline: φ-Field Evolution",
        "description": "Comprehensive cosmic history from Big Bang to present showing φ-field evolution through all epochs",
        "cosmic_events": len(events) - 1,  # Exclude future event
        "time_span": "13.8 billion years",
        "epochs_covered": len(epoch_ranges),
        "phi_field_transitions": len(transition_times),
        "provenance": "phi_field_cosmic_evolution"
    }

if __name__ == "__main__":
    result = generate_cosmic_timeline_complete()
    print(f"Generated: {result['file']}")
    print(f"Cosmic events: {result['cosmic_events']}")
    print(f"Time span: {result['time_span']}")
    print(f"Epochs: {result['epochs_covered']}")
    print(f"φ-transitions: {result['phi_field_transitions']}")
