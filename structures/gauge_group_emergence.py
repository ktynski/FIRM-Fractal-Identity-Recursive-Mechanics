"""
Compatibility shim for gauge group emergence under the `structures` package.

Re-exports the canonical implementation from
`theory.physics.fundamental.gauge_group_emergence`.
"""

from theory.physics.fundamental.gauge_group_emergence import (
    GaugeGroup,
    SymmetryBreakingScale,
    GaugeGroupStructure,
    StandardModelGroups,
    GAUGE_GROUP_EMERGENCE,
)

__all__ = [
    "GaugeGroup",
    "SymmetryBreakingScale",
    "GaugeGroupStructure",
    "StandardModelGroups",
    "GAUGE_GROUP_EMERGENCE",
]


