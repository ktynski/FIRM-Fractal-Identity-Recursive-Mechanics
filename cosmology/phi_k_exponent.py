"""
φ-Exponent Decomposition for ℓ₀ ≈ 220

Compute k = log_φ(ℓ₀) and decompose as k = 12 + φ^{-1} + ε.
This provides a clean numerical bridge between a φ-power anchor and the
mythic/structural reading (12 shells + grace surplus + torsion ε).
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from foundation.operators.phi_recursion import PHI_VALUE


@dataclass(frozen=True)
class PhiExponentDecomposition:
    l0: float
    k: float
    base: int
    grace_surplus: float
    epsilon: float


def decompose_k_for_l0(l0: float = 220.0) -> PhiExponentDecomposition:
    phi = PHI_VALUE
    # k = log_φ(l0)
    k = math.log(l0, phi)
    base = 12
    grace = 1.0 / phi
    epsilon = k - (base + grace)
    return PhiExponentDecomposition(
        l0=float(l0), k=float(k), base=base, grace_surplus=float(grace), epsilon=float(epsilon)
    )

