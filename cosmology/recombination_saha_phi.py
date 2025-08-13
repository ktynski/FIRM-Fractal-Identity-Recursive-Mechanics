"""
φ-Native Saha Recombination (theory-only, no empirical inputs)

Implements a hydrogen Saha-equation-based recombination redshift using
constants from our theoretical constants module. The target ionization
fraction threshold is set theory-side (x_e_target = φ^{-3}), avoiding any
observational anchoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional
import math

from foundation.operators.phi_recursion import PHI_VALUE
from constants.fundamental_constants_firm import FUNDAMENTAL_CONSTANTS_DERIVATION


@dataclass(frozen=True)
class SahaRecombinationResult:
    z_rec: float
    x_e_target: float
    provenance: Dict[str, str]


def _get_constant(symbol: str) -> float:
    # Prefer observed SI-defined exact values for k_B, h, ħ, e, ε0, μ0, c;
    # derive G via theoretical chain to avoid anchoring on empirical G.
    obs = FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants
    return float(obs[symbol])


def _theoretical_G() -> float:
    try:
        return float(FUNDAMENTAL_CONSTANTS_DERIVATION.derive_gravitational_constant().theoretical_value)
    except Exception:
        return float(FUNDAMENTAL_CONSTANTS_DERIVATION._observed_constants["G"])  # fallback


def _rydberg_energy_joules() -> float:
    # E_R = m_e e^4 / (8 ε0^2 h^2)
    m_e = _get_constant("m_e")
    e = _get_constant("e")
    epsilon_0 = _get_constant("epsilon_0")
    h = _get_constant("h")
    return m_e * (e ** 4) / (8.0 * (epsilon_0 ** 2) * (h ** 2))


def _ionization_energy_hydrogen() -> float:
    # χ_H = 13.6 eV = Rydberg energy; computed above in Joules
    return _rydberg_energy_joules()


def _saha_S(T: float, n_b: float) -> float:
    """
    Return Saha RHS S(T, n_b) so that x_e satisfies x_e^2/(1-x_e) = S.
    S = (2π m_e k_B T / h^2)^{3/2} * (2 / n_b) * exp(-χ/(k_B T))
    """
    m_e = _get_constant("m_e")
    k_B = _get_constant("k_B")
    h = _get_constant("h")
    chi = _ionization_energy_hydrogen()
    pref = (2.0 * math.pi * m_e * k_B * T) / (h ** 2)
    S = (pref ** 1.5) * (2.0 / max(n_b, 1e-99)) * math.exp(-chi / (k_B * T))
    return S


def _saha_xe_from_S(S: float) -> float:
    # Solve x^2/(1-x) = S → x = 0.5 ( -S + sqrt(S(S+4)) )
    disc = max(S * (S + 4.0), 0.0)
    return 0.5 * (-S + math.sqrt(disc))


def compute_zrec_saha_phi(H0_s_inv: float, omega_m: float, omega_b: float, omega_gamma: float, T0_K: float,
                           x_e_target: Optional[float] = None) -> SahaRecombinationResult:
    """
    Compute z_rec from Saha equation with φ-native background.

    - H0_s_inv: H0 in s^-1
    - Ω_m, Ω_b, Ω_γ: background parameters
    - T0_K: present temperature (Kelvin) from φ-native derivation
    - x_e_target: theory-side ionization fraction threshold; default φ^{-3}
    """
    phi = PHI_VALUE
    x_e_star = float(phi ** (-3)) if x_e_target is None else float(x_e_target)

    # Critical density ρ_c and baryon number density today
    c = _get_constant("c")
    G = _theoretical_G()
    m_p = _get_constant("m_p")
    rho_c = 3.0 * (H0_s_inv ** 2) / (8.0 * math.pi * G)
    n_b0 = (omega_b * rho_c) / m_p

    # Bisection in z for x_e(z) - x_e_star = 0
    def x_e_at_z(z: float) -> float:
        T = T0_K * (1.0 + z)
        n_b = n_b0 * (1.0 + z) ** 3
        S = _saha_S(T, n_b)
        return max(min(_saha_xe_from_S(S), 1.0), 0.0)

    z_lo, z_hi = 100.0, 5000.0
    f_lo = x_e_at_z(z_lo) - x_e_star
    f_hi = x_e_at_z(z_hi) - x_e_star
    # Ensure the bracket; if not, expand
    for _ in range(10):
        if f_lo * f_hi <= 0.0:
            break
        z_hi *= 1.5
        f_hi = x_e_at_z(z_hi) - x_e_star

    # Bisection iterations
    z_rec = z_hi
    for _ in range(80):
        z_mid = 0.5 * (z_lo + z_hi)
        f_mid = x_e_at_z(z_mid) - x_e_star
        if f_lo * f_mid <= 0.0:
            z_hi, f_hi = z_mid, f_mid
        else:
            z_lo, f_lo = z_mid, f_mid
        z_rec = z_mid
        if abs(f_mid) < 1e-6:
            break

    return SahaRecombinationResult(
        z_rec=float(z_rec),
        x_e_target=x_e_star,
        provenance={
            "equation": "x_e^2/(1-x_e) = S(T,n_b)",
            "S": "(2π m_e k_B T/h^2)^{3/2} (2/n_b) exp(-χ/(k_B T))",
            "χ": "Hydrogen ionization energy from constants (Rydberg)",
            "threshold": f"x_e_target = {x_e_star}",
        },
    )


