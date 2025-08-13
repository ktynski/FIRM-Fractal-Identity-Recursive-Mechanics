"""
Fundamental Physics: Core Theoretical Physics from Mathematical Foundation

This package implements fundamental physics derivations from FIRM's mathematical foundation,
including gauge group emergence, spacetime dimensions, and fundamental interactions.

Mathematical Foundation:
    - Derives from: foundation/ (pure mathematics)
    - Implements: Core theoretical physics principles
    - Enables: All physics applications and observable predictions

Key Modules:
    - gauge_group_emergence.py: Standard Model gauge group emergence from φ-symmetries
    - spacetime_dimensions.py: (3+1)D spacetime emergence from Grace Operator
    - yukawa_couplings.py: Fundamental interaction couplings

Core Theoretical Results:
    - U(1)×SU(2)×SU(3) gauge group emergence from E₈ → SO(10) → SU(5) cascade
    - (3+1)D spacetime as unique stable eigenvalue configuration
    - All fundamental coupling constants from φ-mathematics

Separation of Concerns:
    - foundation/: Pure mathematics
    - theory/physics/fundamental/: Core theoretical physics ← This package
    - theory/physics/forces/: Specific force implementations
    - theory/physics/gravity/: Gravity and spacetime dynamics
    - structures/: Bridge to observables

Author: FIRM Research Team
Created: [REORGANIZATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

try:
    from .gauge_group_emergence import *
    from .spacetime_dimensions import *
    from .yukawa_couplings import *
except ImportError:
    pass

__all__ = [
    'GaugeGroup',
    'GaugeGroupStructure',
    'GAUGE_GROUP_EMERGENCE',
    'SpacetimeDimensions',
    'YukawaCouplings',
]
