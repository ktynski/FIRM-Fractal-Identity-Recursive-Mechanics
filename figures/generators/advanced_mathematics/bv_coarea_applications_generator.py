#!/usr/bin/env python3
"""
BV Coarea Applications Generator (pure mathematics)
Length of level sets and total variation relation schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_bv_coarea_applications() -> Dict[str, Any]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 1) Level sets length vs t
    ax1.set_title("Level set length vs t (schematic)", fontsize=14, weight='bold')
    t = np.linspace(0, 1, 200)
    length = 1 + 0.5*np.sin(2*np.pi*t) + 0.3*t
    ax1.plot(t, length, lw=2)
    ax1.set_xlabel('t')
    ax1.set_ylabel('H^{n-1}({u=t})')
    ax1.grid(True, alpha=0.3)

    # 2) Coarea relation TV(u) = ∫ length({u=t}) dt (schematic area under curve)
    ax2.set_title("Coarea formula (schematic)", fontsize=14, weight='bold')
    ax2.plot(t, length, lw=2)
    ax2.fill_between(t, 0, length, color='gold', alpha=0.4)
    ax2.text(0.5, np.max(length)*0.5, r"TV(u) = ∫ H^{n-1}({u=t}) dt", ha='center')
    ax2.set_xlabel('t')
    ax2.set_ylabel('length')
    ax2.grid(True, alpha=0.3)

    fig.suptitle("BV Coarea Applications (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/bv_coarea_applications.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "bv_coarea_applications"}


if __name__ == "__main__":
    res = generate_bv_coarea_applications()
    print(f"Generated: {res['file']}")
