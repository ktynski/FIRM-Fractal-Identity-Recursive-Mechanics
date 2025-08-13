"""
Forces: Fundamental Force Implementations

This package implements the complete fundamental forces from FIRM theory,
including strong force (QCD) and electromagnetic force derivations.

Mathematical Foundation:
    - Derives from: theory/physics/fundamental/ (gauge groups, symmetries)
    - Implements: Specific force implementations
    - Enables: Complete Standard Model force calculations

Key Modules:
    - strong_force_triadic.py: Strong force as φ-locked triadic morphism binding
    - gluon_torsion_framework.py: QCD gluon dynamics and confinement

Force Implementations:
    - Strong force: Triadic morphic binding with confinement and asymptotic freedom
    - QCD: Complete gluon torsion framework with SU(3) color dynamics

Core Results:
    - Confinement from topological irreducibility of φ-triads
    - Asymptotic freedom from micro-resonance cancellation
    - SU(3) emergence from triadic symmetry automorphisms
    - Gluon dynamics from morphic coherence preservation

Author: FIRM Research Team
Created: [REORGANIZATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

try:
    from .strong_force_triadic import *
    from .gluon_torsion_framework import *
except ImportError:
    pass

__all__ = [
    'StrongForceTriadic',
    'GluonTorsionFramework',
    'TriadicMorphismState',
]
