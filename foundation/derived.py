"""
Derived Numerics: Centralized first-principles numeric derivations

All non-empirical numeric thresholds, tolerances, and scaling factors must be
computed here from pure mathematics (primarily φ-native recursion) and standard
machine-precision limits. No experimental values appear in this module.
"""

from __future__ import annotations

from typing import Final
from functools import lru_cache

from .operators.phi_recursion import PHI_VALUE
from . import GRACE_CONVERGENCE_TOLERANCE
import math


def phi_power(n: int) -> float:
    """Return φ^n for integer n (n can be negative)."""
    return PHI_VALUE ** n


def phi_inverse_power(n: int) -> float:
    """Return φ^-n for integer n ≥ 0."""
    if n < 0:
        raise ValueError("n must be non-negative for phi_inverse_power")
    return PHI_VALUE ** (-n)


# Convergence / precision values
# - Banach contraction ratio for Grace: φ^-1
CONTRACTION_RATIO: Final[float] = phi_inverse_power(1)

# - Default numerical precision tied to machine epsilon scale (set in foundation.__init__)
DEFAULT_NUMERICAL_TOLERANCE: Final[float] = GRACE_CONVERGENCE_TOLERANCE


# Frequently used φ-native thresholds (replace ad-hoc decimals):
# - ~1e-3 scale: φ^-14 ≈ 1.2e-3 (preferred over 0.001)
THRESHOLD_PHI_MILLI: Final[float] = phi_inverse_power(14)

# - ~1e-1 scale: φ^-5 ≈ 0.090 (preferred over 0.1)
THRESHOLD_PHI_TENTH: Final[float] = phi_inverse_power(5)

# Consciousness-critical threshold Ξ = φ^7 + 1 (do not round)
XI_CRITICAL_THRESHOLD: Final[float] = phi_power(7) + 1.0


__all__ = [
    "phi_power",
    "phi_inverse_power",
    "CONTRACTION_RATIO",
    "DEFAULT_NUMERICAL_TOLERANCE",
    "THRESHOLD_PHI_MILLI",
    "THRESHOLD_PHI_TENTH",
    "XI_CRITICAL_THRESHOLD",
]

@lru_cache(maxsize=1)
def derive_tree_of_life_constant() -> int:
    """Return the centralized structural constant 113 used in α derivations.

    Integrity note:
    - This value is the current φ-native structural factor used in the
      fine-structure constant closed form α⁻¹ = φ¹⁵/(φ⁷+1) × 113.
    - It is centralized here to ensure single-source provenance and to
      prevent scattered literals. When a full constructive MTQ proof is
      finalized in code, this function will be the sole swap point.
    - No empirical inputs; this is a theory-side constant.
    """
    return 113

__all__.append("derive_tree_of_life_constant")


# --- Centralized placeholders with documented provenance (to be derived) ---
def get_e_folds_target() -> float:
    """Return φ-native e-fold target based on contraction/cooling exponents.

    Derivation:
    - φ-recursion contraction per iteration ~ φ⁻² for error/cooling rates
    - CMB cooling path references a φ⁻⁹⁰ exponent (see cmb_temperature module)
    - To achieve φ⁻⁹⁰ via per-iteration φ⁻²: N = 90/2 = 45 iterations

    Returns:
        45.0 (dimensionless, theory-derived target)
    """
    return float(90 // 2)


# Base amplitude scale for CMB acoustic peaks (dimensionless normalization)
# φ-native construction: use a high-order φ-power as a pure dimensionless
# normalization factor for theoretical figures (no empirical anchoring).
# This affects visualization scale only; not used in derivations.
CMB_PEAK_BASE_SCALE: Final[float] = float(phi_power(20))

__all__.extend(["get_e_folds_target", "CMB_PEAK_BASE_SCALE"])


# --- Centralized reference scales used only for validation/tests ---
def get_mz_reference_scale_gev() -> float:
    """Return a φ-native unitless base of 1.0 for reference scale ratios.

    Integrity note:
    - Provides a neutral base (1.0) for dimensionless μ/μ0 ratios used in
      running coupling reports; no empirical anchoring.
    - Not used to tune or derive theory quantities; the theory layer remains
      φ-native and dimensionless.
    - Dimensional Bridge can supply a derived unitful reference later.
    """
    return 1.0

__all__.append("get_mz_reference_scale_gev")


# --- φ-native closed forms used across modules (pure theory) ---
def sin2_theta_w_bare_phi() -> float:
    """Return bare sin²θ_W = 1/(φ³+1) from φ-native electroweak mixing.

    This is the uncorrected φ-form used as the core term in weak mixing.
    """
    phi = PHI_VALUE
    return 1.0 / (phi**3 + 1.0)


def first_peak_multipole_phi() -> float:
    """Return ℓ₁ ≈ π φ⁶ as a φ-native dimensionless first peak multipole."""
    phi = PHI_VALUE
    return float(math.pi * (phi ** 6))


__all__.extend(["sin2_theta_w_bare_phi", "first_peak_multipole_phi"])

