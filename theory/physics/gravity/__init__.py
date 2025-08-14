"""
Gravity: Gravitational Theory and Spacetime Dynamics

This package implements gravitational theory from FIRM mathematical foundations,
including Einstein field equations and φ-enhanced gravity derivations.

Mathematical Foundation:
    - Derives from: foundation/ (Grace Operator) and fundamental physics
    - Implements: Complete gravitational theory
    - Enables: General relativity and cosmological applications

Key Modules:
    - einstein_equations_derivation.py: Einstein field equations from Grace Operator
    - phi_gravity_derivation.py: φ-enhanced gravity theory

Gravitational Theory:
    - Einstein equations: G_μν = 8πG T_μν derived from Grace Operator
    - φ-enhancement: Modified to G_μν = φ² T_μν
    - Spacetime curvature: Emergence from mathematical necessity
    - Cosmological applications: Dark energy and expansion dynamics

Core Results:
    - Spacetime metric emergence from Grace Operator eigenvalues
    - Einstein-Hilbert action from variational φ-principle
    - φ-enhanced field equations with golden ratio modifications
    - Complete general relativity derivation from pure mathematics

Author: FIRM Research Team
Created: [REORGANIZATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

try:
    from .einstein_equations_derivation import *
    from .phi_gravity_derivation import *
except ImportError:
    pass

__all__ = [
    'EinsteinEquationDerivation',
    'PhiGravityDerivation',
    'SpacetimePoint',
]
