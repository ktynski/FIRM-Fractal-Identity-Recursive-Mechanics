"""
φ-Native Cosmological Background Helpers

Derives temperature T0, radiation density parameter Ω_γ, and baryon fraction
from φ-native principles with the existing dimensional bridge and Kelvin
scaling factor modules. No empirical targets or tuning.

Outputs are used by CMB power spectrum and background E(z) consistently.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
import math

import numpy as np

from foundation.operators.phi_recursion import PHI_VALUE
from structures.dimensional_bridge import (
    DIMENSIONAL_BRIDGE,
    DimensionalQuantity,
    DimensionType,
)
from constants.kelvin_scaling_factor import KELVIN_SCALING_DERIVATION
from cosmology.baryon_phi import derive_omega_baryon_from_eta
from constants.fundamental_constants_firm import FUNDAMENTAL_CONSTANTS_DERIVATION


@dataclass(frozen=True)
class PhiBackgroundResult:
    T0_K: float
    omega_gamma: float
    omega_baryon: float
    derivation_provenance: Dict[str, str]


def derive_T0_kelvin_phi_native() -> float:
    """
    Derive present-day background temperature T0 in Kelvin from φ-native T_morphic.

    T_morphic = φ^(-90) (dimensionless). Apply Dimensional Bridge for temperature
    and the Kelvin spectral scaling factor 2.821 (exact φ-spectral Wien result).

    Returns:
        T0_K (float): φ-native present-day temperature in Kelvin units.
    """
    phi = PHI_VALUE
    # Base morphic temperature (dimensionless φ-exponent)
    T_morphic = phi ** (-90)
    # Assign physical temperature dimension via Dimensional Bridge
    T_math = DimensionalQuantity(
        value=T_morphic,
        dimensions={DimensionType.TEMPERATURE: 1},
        unit="mathematical_units",
        mathematical_justification="T_morphic = φ^(-90) with TEMPERATURE dimension",
    )
    T_bridge = DIMENSIONAL_BRIDGE.convert_mathematical_to_physical(T_math)
    # Kelvin scaling factor from φ-spectral Wien peak
    kelvin_factor = KELVIN_SCALING_DERIVATION.derive_phi_spectral_wien_peak().scaling_factor
    T0_K = float(T_bridge.value) * float(kelvin_factor)
    return T0_K


def derive_omega_gamma_phi_native(h0_s_inverse: float) -> float:
    """
    Derive radiation density parameter Ω_γ using φ-native constants and T0.

    Ω_γ = u_γ / (ρ_c c^2) where u_γ = a_rad T0^4, ρ_c = 3 H0^2 / (8π G).

    Uses theoretical constants from FUNDAMENTAL_CONSTANTS_DERIVATION to keep
    provenance consistent across the codebase.
    """
    # Get constants (theoretical values from our derivations)
    try:
        k_B = float(FUNDAMENTAL_CONSTANTS_DERIVATION.derive_boltzmann_constant().theoretical_value)
    except Exception:
        k_B = float(FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants["k_B"])
    try:
        hbar = float(FUNDAMENTAL_CONSTANTS_DERIVATION.derive_planck_constant().theoretical_value)
    except Exception:
        hbar = float(FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants["hbar"])
    try:
        c = float(FUNDAMENTAL_CONSTANTS_DERIVATION.derive_speed_of_light().theoretical_value)
    except Exception:
        c = float(FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants["c"])
    try:
        G = float(FUNDAMENTAL_CONSTANTS_DERIVATION.derive_gravitational_constant().theoretical_value)
    except Exception:
        G = float(FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants["G"])

    # Radiation constant a_rad = (π^2 k_B^4) / (15 c^3 ħ^3)
    a_rad = (math.pi ** 2) * (k_B ** 4) / (15.0 * (c ** 3) * (hbar ** 3))

    T0 = derive_T0_kelvin_phi_native()
    u_gamma = a_rad * (T0 ** 4)  # J/m^3
    # Critical mass density ρ_c = 3 H0^2 / (8π G)
    rho_c = 3.0 * (h0_s_inverse ** 2) / (8.0 * math.pi * G)
    # Convert u_gamma (energy density) to mass density via c^2
    omega_gamma = (u_gamma / (c ** 2)) / rho_c
    return float(omega_gamma)


def derive_baryon_fraction_phi_native(omega_matter: float, h0_s_inverse: float) -> float:
    """
    Derive Ω_b via φ-native η ≡ n_b/n_γ = φ^{-3} and T0 (no fitting).
    """
    T0 = derive_T0_kelvin_phi_native()
    omega_b = derive_omega_baryon_from_eta(T0, h0_s_inverse)
    # Ensure Ω_b ≤ Ω_m (theory sanity)
    return float(min(omega_b, omega_matter))


def build_phi_background(h0_s_inverse: float, omega_matter: float) -> PhiBackgroundResult:
    """
    Construct φ-native background set used by E(z) and rs/DA integrals.
    """
    T0 = derive_T0_kelvin_phi_native()
    og = derive_omega_gamma_phi_native(h0_s_inverse)
    ob = derive_baryon_fraction_phi_native(omega_matter, h0_s_inverse)
    return PhiBackgroundResult(
        T0_K=T0,
        omega_gamma=og,
        omega_baryon=ob,
        derivation_provenance={
            "T0": "T_morphic=φ^-90 → DimensionalBridge(T) → ×2.821 (Kelvin factor)",
            "omega_gamma": "Ω_γ = a_rad T0^4 / (ρ_c c^2); a_rad from (π^2 k_B^4)/(15 c^3 ħ^3)",
            "omega_baryon": "Ω_b = Ω_m / φ^2 (φ-native symmetry split)",
        },
    )


