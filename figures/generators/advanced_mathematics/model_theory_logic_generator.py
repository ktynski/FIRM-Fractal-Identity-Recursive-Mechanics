#!/usr/bin/env python3
"""
Model Theory and Logic Generator (pure mathematics)
Structures, elementary embeddings, type spaces, and compactness schematic.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, Any


def generate_model_theory_logic() -> Dict[str, Any]:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # 1) Language/signature and structures
    ax1.set_title("Language Σ and Structures 𝔐, 𝔑", fontsize=14, weight="bold")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.axis('off')
    ax1.text(2, 6.5, r"Σ = (\mathcal{F},\mathcal{R},\mathcal{C})", fontsize=12, weight='bold',
             bbox=dict(boxstyle='round', fc='#eef', ec='#99f'))
    # Structures M,N
    ax1.text(2, 4.5, r"\mathfrak{M} |= T", fontsize=12, bbox=dict(boxstyle='round', fc='#efe'))
    ax1.text(8, 4.5, r"\mathfrak{N} |= T", fontsize=12, bbox=dict(boxstyle='round', fc='#efe'))
    ax1.annotate('', xy=(7.2, 4.5), xytext=(2.8, 4.5),
                 arrowprops=dict(arrowstyle='->', lw=2, color='purple'))
    ax1.text(5, 4.9, r"elementary\ embedding\  \mathfrak{M} \preccurlyeq \mathfrak{N}",
             ha='center', fontsize=10, color='purple', weight='bold')
    # Diagrams
    ax1.text(2, 3, r"Diag(\mathfrak{M})", fontsize=10)
    ax1.text(8, 3, r"Diag(\mathfrak{N})", fontsize=10)

    # 2) Types space S_n(M)
    ax2.set_title(r"Type Space: S_n(\mathfrak{M})", fontsize=14, weight='bold')
    theta = np.linspace(0, 2*np.pi, 200)
    for r in [1.0, 1.3, 1.6]:
        ax2.plot(r*np.cos(theta), r*np.sin(theta), alpha=0.4)
    # Sample types as points on circles
    rng = np.random.default_rng(7)
    pts = np.column_stack([
        rng.uniform(0.5, 1.5, size=30)*np.cos(rng.uniform(0, 2*np.pi, size=30)),
        rng.uniform(0.5, 1.5, size=30)*np.sin(rng.uniform(0, 2*np.pi, size=30)),
    ])
    ax2.scatter(pts[:,0], pts[:,1], s=30, c='tomato', alpha=0.8, edgecolors='k', linewidths=0.3)
    ax2.text(0, 0, r"S_n(\mathfrak{M})", ha='center', va='center', fontsize=12, weight='bold')
    ax2.set_aspect('equal')
    ax2.axis('off')

    # 3) Compactness theorem schematic
    ax3.set_title("Compactness Theorem (schematic)", fontsize=14, weight='bold')
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 6)
    ax3.axis('off')
    # Infinite set of sentences Γ and finite subsets Γ_0
    ax3.text(2, 4.5, r"\Gamma = \{\varphi_i\}_{i\in I}", bbox=dict(boxstyle='round', fc='#ffe'))
    for i, x in enumerate([4, 6, 8]):
        ax3.text(x, 3 + 0.6*np.sin(i), r"\Gamma_0^{}", bbox=dict(boxstyle='round', fc='#ffd'))
        ax3.annotate('', xy=(x-0.4, 3+0.6*np.sin(i)), xytext=(2.6, 4.4),
                     arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    ax3.text(5, 1.5, r"If every finite \Gamma_0 is satisfiable \Rightarrow \Gamma\ is satisfiable",
             ha='center', fontsize=11, weight='bold', color='green')

    # 4) Stability/NIP schematic chart
    ax4.set_title("Stability / NIP landscape (schematic)", fontsize=14, weight='bold')
    classes = ["Stable", "Simple", "NIP", "O-minimal"]
    vals = [4, 3, 2, 1]
    ax4.barh(classes, vals, color=['#88c', '#aac', '#caa', '#aca'])
    ax4.set_xlabel("tameness (schematic scale)")
    ax4.grid(True, axis='x', alpha=0.3)

    fig.suptitle("Model Theory and Logic (pure mathematics)", fontsize=16, weight='bold')
    plt.tight_layout()
    out = Path("figures/outputs/model_theory_logic.png")
    fig.savefig(out, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return {"file": str(out), "category": "advanced_mathematics", "topic": "model_theory_logic"}


if __name__ == "__main__":
    res = generate_model_theory_logic()
    print(f"Generated: {res['file']}")
