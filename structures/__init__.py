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

# Local registry for discovered/constructed physical structures
_STRUCTURE_REGISTRY: Dict[str, Any] = {}

def register_physical_structure(name: str, obj: Any) -> None:
    """Register a named physical structure instance for discovery and provenance.

    Args:
        name: Canonical structure name (e.g., "spacetime", "gauge_groups").
        obj: The structure instance to register.
    """
    _STRUCTURE_REGISTRY[name] = obj

def get_physical_structure(name: str) -> Any:
    """Retrieve a registered physical structure by name."""
    return _STRUCTURE_REGISTRY.get(name)

# Re-export primary classes and singleton instances
from .dimensional_bridge import DIMENSIONAL_BRIDGE, DimensionalBridge
from .gauge_group_emergence import (
    GAUGE_GROUP_EMERGENCE,
    StandardModelGroups,
    GaugeGroup,
    SymmetryBreakingScale,
    GaugeGroupStructure,
)
from .particle_spectrum import (
    PARTICLE_SPECTRUM,
    CompleteSpectrum,
    ParticleType,
    FermionType,
    Generation,
    QuantumNumbers,
    ParticleSpecification,
)
from .spacetime_dimensions import (
    SPACETIME_STRUCTURE,
    SpacetimeDimensionality,
    SpacetimeSignature,
    DimensionalStability,
    SpacetimeDimension,
    SpacetimeStructure,
)

__all__ = [
    # Registry utilities
    'register_physical_structure',
    'get_physical_structure',

    # Dimensional bridge
    'DIMENSIONAL_BRIDGE',
    'DimensionalBridge',

    # Gauge group emergence
    'GAUGE_GROUP_EMERGENCE',
    'StandardModelGroups',
    'GaugeGroup',
    'SymmetryBreakingScale',
    'GaugeGroupStructure',

    # Particle spectrum
    'PARTICLE_SPECTRUM',
    'CompleteSpectrum',
    'ParticleType',
    'FermionType',
    'Generation',
    'QuantumNumbers',
    'ParticleSpecification',

    # Spacetime dimensionality
    'SPACETIME_STRUCTURE',
    'SpacetimeDimensionality',
    'SpacetimeSignature',
    'DimensionalStability',
    'SpacetimeDimension',
    'SpacetimeStructure',
]