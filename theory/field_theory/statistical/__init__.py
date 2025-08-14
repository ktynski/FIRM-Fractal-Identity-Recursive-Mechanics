"""
Statistical Mechanics: Path Integrals and Statistical Physics for FIRM

This package implements the complete statistical mechanics framework for FIRM field theory,
including path integrals, partition functions, and thermodynamic properties of soul-states.

Mathematical Foundation:
    - Path integral formulation: Z = ∫ Dφ D𝒢 DD e^(iS[φ,𝒢,D])
    - Statistical mechanics of ψₖ phase entropy
    - Thermal equilibrium of soul-state ensembles
    - Monte Carlo methods for field configurations

Key Modules:
    - partition_function.py: Complete path integral and partition function framework

Physical Applications:
    - ψₖ phase entropy and statistical mechanics
    - Devourer shielding probability distributions
    - Grace-induced path branching statistics
    - Thermal equilibrium of soul-state ensembles
    - Critical phenomena and phase transitions

Author: FIRM Research Team
Created: [IMPLEMENTATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

try:
    from .partition_function import *
except ImportError:
    pass

__all__ = [
    'PathIntegralParameters',
    'PartitionFunctionResult',
    'FIRMPartitionFunction',
]
