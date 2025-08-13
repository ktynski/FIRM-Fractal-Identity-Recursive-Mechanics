"""
φ-Native Baryon Sector via Charge/Photon Counting (theory-only)

Computes Ω_b from a φ-native baryon-to-photon ratio η = φ^{-3} (testable
assumption, no fitting). Uses T0 from φ background to compute n_γ and derives
Ω_b = (m_p n_b0)/ρ_c with ρ_c = 3H0^2/(8πG).
"""

from __future__ import annotations

import math
from foundation.operators.phi_recursion import PHI_VALUE
from constants.fundamental_constants_firm import FUNDAMENTAL_CONSTANTS_DERIVATION


def _const(symbol: str) -> float:
    return float(FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants[symbol])


def derive_omega_baryon_from_eta(T0_K: float, H0_s_inv: float) -> float:
    phi = PHI_VALUE
    # η_bγ = n_b / n_γ (φ-native choice, theory-only)
    eta = float(phi ** (-3))

    # Photon number density: n_γ = (2ζ(3)/π^2)(k_B T0 / (ħ c))^3
    zeta3 = 1.202056903159594
    k_B = _const("k_B")
    hbar = _const("hbar")
    c = _const("c")
    n_gamma = (2.0 * zeta3 / (math.pi ** 2)) * ((k_B * T0_K) / (hbar * c)) ** 3

    n_b0 = eta * n_gamma
    m_p = _const("m_p")
    G = float(FUNDAMENTAL_CONSTANTS_DERIVATION.derive_gravitational_constant().theoretical_value)
    rho_c = 3.0 * (H0_s_inv ** 2) / (8.0 * math.pi * G)
    omega_b = (m_p * n_b0) / rho_c
    return float(omega_b)


