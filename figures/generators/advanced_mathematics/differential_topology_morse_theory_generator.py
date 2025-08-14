#!/usr/bin/env python3
"""
Differential Topology: Morse Theory (pure mathematics)
Morse function critical points, gradient flow lines, and handle schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_differential_topology_morse_theory() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Morse function on sphere: f(θ,φ) = cos θ
    ax1.set_title("Morse function on S²: f(θ)=cos θ", fontsize=14, weight='bold')
    theta = np.linspace(0, np.pi, 200)
    f = np.cos(theta)
    ax1.plot(theta, f, lw=2)
    ax1.scatter([0, np.pi], [1, -1], c=['green','red'], s=80)
    ax1.text(0, 1.02, 'max', color='green', ha='center')
    ax1.text(np.pi, -1.08, 'min', color='red', ha='center')
    ax1.set_xlabel('θ')
    ax1.set_ylabel('f(θ)')
    ax1.grid(True, alpha=0.3)

    # 2) Gradient flow lines on sphere projection (schematic)
    ax2.set_title("Gradient flow lines (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 2*np.pi, 200)
    for r in [0.2, 0.5, 0.8]:
        ax2.plot(r*np.cos(t), r*np.sin(t), 'k-', alpha=0.3)
    for ang in np.linspace(0, np.pi, 6):
        ax2.arrow(0, 0, 0.8*np.cos(ang), 0.8*np.sin(ang), head_width=0.03, alpha=0.6)
        ax2.arrow(0, 0, 0.8*np.cos(-ang), 0.8*np.sin(-ang), head_width=0.03, alpha=0.6)
    ax2.set_aspect('equal')
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.axis('off')

    # 3) Handle attachment schematic
    ax3.set_title("Handle decomposition (schematic)", fontsize=14, weight='bold')
    ax3.add_patch(plt.Rectangle((0.5, 0.5), 1.5, 0.6, color='lightblue', alpha=0.7))
    ax3.add_patch(plt.Rectangle((2.2, 0.5), 1.5, 0.6, color='lightgreen', alpha=0.7))
    ax3.add_patch(plt.Rectangle((3.9, 0.5), 1.5, 0.6, color='salmon', alpha=0.7))
    ax3.text(1.25, 0.85, '0-handle', ha='center')
    ax3.text(2.95, 0.85, '1-handle', ha='center')
    ax3.text(4.65, 0.85, '2-handle', ha='center')
    ax3.set_xlim(0, 6)
    ax3.set_ylim(0, 2)
    ax3.axis('off')

    fig.suptitle("Differential Topology: Morse Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/differential_topology_morse_theory.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "differential_topology_morse_theory"}


if __name__ == "__main__":
    res = generate_differential_topology_morse_theory()
    print(f"Generated: {res['file']}")
