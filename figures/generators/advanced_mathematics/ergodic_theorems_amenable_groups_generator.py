#!/usr/bin/env python3
"""
Ergodic Theorems on Amenable Groups Generator (pure mathematics)
Følner averages convergence schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_ergodic_theorems_amenable_groups() -> Dict[str, Any]:
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ax.set_title("Følner averages → limit (schematic)", fontsize=14, weight='bold')
    n = np.arange(1, 50)
    limit = 0.7
    avg = limit + 0.2*np.cos(0.3*n)/np.sqrt(n)
    ax.plot(n, avg, 'o-', lw=2, label='A_{F_n} f')
    ax.axhline(limit, color='k', linestyle='--', label='limit')
    ax.set_xlabel('n (Følner set index)')
    ax.set_ylabel('average')
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.suptitle("Ergodic Theorems on Amenable Groups (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/ergodic_theorems_amenable_groups.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "ergodic_theorems_amenable_groups"}


if __name__ == "__main__":
    res = generate_ergodic_theorems_amenable_groups()
    print(f"Generated: {res['file']}")
