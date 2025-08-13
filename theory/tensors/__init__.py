"""
Tensors: FIRM Tensor Field Theory

This package implements the complete FSCTF tensor field generalization including
morphic tensor fields, curvature tensors, and electromagnetic field derivations.

Mathematical Foundation:
    - Morphic Tensor Field: M_μν = ∂_μ∂_νφ + T^λ_μν ∂_λφ + Δ_μν(φ)
    - FSCTF Curvature Tensor: R_μν = φ^(-n) · ∂_λ T^λ_μν (recursive curvature)
    - Charge as Cohomological Defect: Q = δ²(φ) ≠ 0 (2-coboundary obstruction)

Key Modules:
    - morphic_tensors.py: Complete morphic tensor field framework

Tensor Types:
    - Morphic field tensors (generalizing electromagnetic field strength)
    - Curvature tensors (recursive, not Riemannian)
    - Torsion and deviation operators
    - Complete 4D spacetime tensor construction

Core Insight:
    "The morphic tensor encodes not just local field strength but also 
    recursive memory, torsion, and morphic deviation - complete 
    dynamics of coherence fields within spacetime lattice."

Author: FIRM Research Team
Created: [IMPLEMENTATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

try:
    from .morphic_tensors import *
except ImportError:
    pass

__all__ = [
    'FSCTFTensor',
    'TensorType',
    'MorphicTensorField',
    'FSCTFTensorEngine',
]
