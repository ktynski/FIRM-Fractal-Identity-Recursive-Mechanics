#!/usr/bin/env python3
"""
Marcinkiewicz Interpolation Generator (pure mathematics)
Weak-type endpoints and strong-type interior schematic for sublinear operator T.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_marcinkiewicz_interpolation() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("Marcinkiewicz interpolation (schematic)", fontsize=14, weight='bold')
    # endpoints (p0,q0), (p1,q1)
    p0, q0 = 1, 1
    p1, q1 = 2, 2
    ax.plot([p0, p1], [q0, q1], 'k--', lw=2, label='interpolation line')
    # weak-type at endpoints
    ax.scatter([p0, p1], [q0, q1], s=120, c=['gold','gold'], edgecolors='k', label='weak-type')
    # interior strong-type example
    p, q = 1.5, 1.5
    ax.scatter([p], [q], s=120, c='tomato', edgecolors='k', label='strong-type')
    ax.set_xlabel('1/p (schematic)')
    ax.set_ylabel('1/q (schematic)')
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.suptitle("Marcinkiewicz Interpolation (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/marcinkiewicz_interpolation.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "marcinkiewicz_interpolation"}


if __name__ == "__main__":
    res = generate_marcinkiewicz_interpolation()
    print(f"Generated: {res['file']}")
