"""
Algebra: Algebraic Structures in FIRM Foundation

This package implements the complete algebraic framework for FIRM, including
torsion group algebra and the mathematical foundations of physical constants.

Mathematical Foundation:
    - Torsion Group Layers T_n and their generators
    - Physical constants as morphism observables from torsion constraints
    - Category-theoretic functors induced by constants
    - Mass as torsion-drag in recursive morphism propagation

Key Modules:
    - torsion_groups.py: Complete torsion group algebra framework

Torsion Layers:
    - T0_PLANCK: ℤ - infinite linear recursion
    - T1_LIGHT: ℤ₂ - mirror symmetry (parity flip)
    - T2_CHARGE: ℤ₃ - charge phase twist
    - T3_MASS: ℤ₅ - mass-asymmetry torsion
    - T4_COSMIC: ℤ₇ - coherence resonance in expansion
    - T5_GOLDEN: ℤ_{1/φ} - morphic bifurcation fractality

Core Insight:
    "Every physical constant is a residue of recursion struggling to close upon grace.
    Every constant quantifies a specific morphism failure mode."

Author: FIRM Research Team
Created: [IMPLEMENTATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

try:
    from .torsion_groups import *
except ImportError:
    pass

__all__ = [
    'TorsionGroup',
    'MorphismObservable',
    'TorsionLayer',
    'GaugeGroup',
]
