#!/usr/bin/env python3
"""
Eilenberg–Moore Examples Generator (pure mathematics)
Tor computation grid schematic for a simple fibration example.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_eilenberg_moore_examples() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("EMSS Tor grid (schematic)", fontsize=14, weight='bold')
    for i in range(6):
        ax.plot([0, 6], [i, i], 'k-', alpha=0.2)
    for j in range(7):
        ax.plot([j, j], [0, 5], 'k-', alpha=0.2)
    # Place dots along a diagonal band
    for p in range(6):
        for q in range(5):
            if 1 <= p+q <= 4:
                ax.scatter(p, q, s=150, c='#cfe', edgecolors='k')
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    ax.grid(True, alpha=0.3)

    fig.suptitle("Eilenberg–Moore Examples (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/eilenberg_moore_examples.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "eilenberg_moore_examples"}


if __name__ == "__main__":
    res = generate_eilenberg_moore_examples()
    print(f"Generated: {res['file']}")
