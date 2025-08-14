#!/usr/bin/env python3
"""
Algebraic Number Theory: Class Field Theory (schematic)
Ideal class group, Minkowski region, and splitting of primes.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_algebraic_number_theory_class_field() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Class group as quotient lattice schematic Z^2 / L
    ax1.set_title("Ideal Class Group (schematic quotient)", fontsize=14, weight='bold')
    x = np.linspace(-3, 3, 13)
    y = np.linspace(-3, 3, 13)
    for xv in x:
        ax1.plot([xv, xv], [y.min(), y.max()], color='#ddd')
    for yv in y:
        ax1.plot([x.min(), x.max()], [yv, yv], color='#ddd')
    # fundamental domain
    rect = plt.Rectangle((-1, -0.5), 2, 1, fill=True, color='gold', alpha=0.3, ec='k')
    ax1.add_patch(rect)
    ax1.text(0, 0, 'FD', ha='center', va='center', fontsize=12, weight='bold')
    ax1.set_aspect('equal')
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.grid(False)

    # 2) Minkowski region for discriminant D (ellipse schematic)
    ax2.set_title("Minkowski Region (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 2*np.pi, 300)
    a, b = 2.0, 1.2
    ax2.plot(a*np.cos(t), b*np.sin(t), lw=2)
    ax2.set_aspect('equal')
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-1.8, 1.8)
    ax2.grid(True, alpha=0.3)

    # 3) Splitting of primes in a quadratic field K = Q(√d)
    ax3.set_title("Prime Splitting in K = Q(√d) (schematic)", fontsize=14, weight='bold')
    primes = np.array([2,3,5,7,11,13,17,19,23,29])
    # -1 (inert), 0 (ramified), +1 (split)
    leg = np.array([0, -1, 1, -1, 1, 1, -1, 1, -1, 1])
    colors = ['tomato' if s<0 else ('gold' if s==0 else 'seagreen') for s in leg]
    ax3.bar(primes, leg+1.1, color=colors)
    ax3.set_xticks(primes)
    ax3.set_yticks([0,1,2])
    ax3.set_yticklabels(['inert', 'ramified', 'split'])
    ax3.set_xlabel('p')
    ax3.set_ylabel('behavior')
    ax3.grid(True, axis='y', alpha=0.3)

    fig.suptitle("Algebraic Number Theory: Class Field Theory (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/algebraic_number_theory_class_field.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "algebraic_number_theory_class_field"}


if __name__ == "__main__":
    res = generate_algebraic_number_theory_class_field()
    print(f"Generated: {res['file']}")
