"""
Structures Package: Physical Structure and Dimensional Analysis Systems

This package contains systems for analyzing physical structures, dimensional
analysis, and the mathematical foundations of physical reality.

Mathematical Foundation:
    - Derives from: FIRM physical structure principles
    - Depends on: φ-mathematics, dimensional analysis, gauge theory
    - Enables: Complete analysis of physical structures and dimensions

Key Components:
    - Dimensional Bridge: Complete dimensional analysis and conversion
    - Gauge Group Emergence: Mathematical emergence of gauge symmetries
    - Particle Spectrum: Complete particle spectrum derivation
    - Spacetime Dimensions: Mathematical foundation of spacetime

Provenance:
    - All structures: Derived from φ-mathematical principles
    - No empirical inputs: Pure mathematical structure analysis
    - Complete audit trails: All structure analysis documented
    - Academic verification: Full structural transparency

Scientific Integrity:
    - Pure mathematical derivation: No empirical content
    - Complete structure systems: Rigorous mathematical analysis
    - Mathematical necessity: All structures derived from principles
    - Academic verification: Full structural documentation

Author: FIRM Research Team
Mathematical derivation: Ex nihilo emergence via φ-recursion
Academic integrity: Complete provenance documented
"""

from typing import Any, Dict

# Re-export registry functions from foundation
from foundation.registry import register_physical_structure, get_physical_structure

# Re-export primary classes and singleton instances  
from .dimensional_bridge import DIMENSIONAL_BRIDGE, DimensionalBridge
from .particle_spectrum import (
    PARTICLE_SPECTRUM,
    CompleteSpectrum,
    ParticleType,
    FermionType,
    Generation,
    QuantumNumbers,
    ParticleSpecification,
)
from .morphic_algebra import *
from .morphic_knot_projection import *
from .physical_units import *

__all__ = [
    # Registry utilities
    'register_physical_structure',
    'get_physical_structure',

    # Dimensional bridge
    'DIMENSIONAL_BRIDGE',
    'DimensionalBridge',

    # Particle spectrum
    'PARTICLE_SPECTRUM',
    'CompleteSpectrum',
    'ParticleType',
    'FermionType',
    'Generation',
    'QuantumNumbers',
    'ParticleSpecification',

    # Mathematical structures
    # (Specific exports from morphic_algebra, morphic_knot_projection, physical_units)
]