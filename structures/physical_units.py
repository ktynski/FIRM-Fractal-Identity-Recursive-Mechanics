"""
Physical Units (Centralized, definitional constants only)

This module centralizes exact SI definitions to avoid ad hoc hardcoding
throughout the codebase. These are unit definitions, not empirical inputs,
and are used only in conversion/interpretation layers, never in derivations.

All constants below are defined exactly by the SI since 2019.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PhysicalUnits:
    """Centralized exact SI definitions and derived exact conversions.

    These are definitional (non-empirical) constants used only in
    unit conversion/interpretation layers, never in derivations.
    """
    # Exact SI definitions
    C_LIGHT_M_PER_S: float = 299_792_458.0                # m/s (exact)
    PLANCK_CONSTANT_J_S: float = 6.626_070_15e-34         # J s (exact)
    BOLTZMANN_CONSTANT_J_PER_K: float = 1.380_649e-23     # J/K (exact)
    ELEMENTARY_CHARGE_C: float = 1.602_176_634e-19        # C (exact)

    # Helpful derived exact conversions
    @property
    def PLANCK_CONSTANT_EV_S(self) -> float:
        """Planck constant in eV·s (exact), derived from J·s and elementary charge."""
        return self.PLANCK_CONSTANT_J_S / self.ELEMENTARY_CHARGE_C

    @property
    def BOLTZMANN_CONSTANT_EV_PER_K(self) -> float:
        """Boltzmann constant in eV/K (exact), derived from J/K and charge."""
        return self.BOLTZMANN_CONSTANT_J_PER_K / self.ELEMENTARY_CHARGE_C


# Global singleton
PHYSICAL_UNITS = PhysicalUnits()

__all__ = ["PhysicalUnits", "PHYSICAL_UNITS"]
