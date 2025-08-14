"""
Grace contraction residual δG(k): theory-only proxy tied to φ-structure.

We estimate a k-parameterized contraction ratio ρ(k) in a bounded φ-native way,
then define δG(k) = max(0, ρ(k) − φ⁻¹). No empirical inputs.
"""

from __future__ import annotations

import math
from typing import Tuple


def phi_value() -> float:
    return (1.0 + math.sqrt(5.0)) / 2.0


def compute_contraction_residual(k: float) -> Tuple[float, float]:
    """
    Return (rho, delta_G) where rho = ρ(k) ∈ (0,1) and δG = max(0, ρ − φ⁻¹).

    Construction:
      ρ(k) = φ⁻¹ × (1 + ε(k)), with ε(k) a small φ-native oscillatory term
      bounded so that ρ(k) < 1. This captures k-sensitivity without any data.
    """
    phi = phi_value()
    base = 1.0 / phi
    # Small bounded oscillation: |osc| ≤ 0.05 ensures ρ<1
    osc = 0.05 * math.sin(2.0 * math.pi / (abs(k) + phi)) * (phi / (abs(k) + phi))
    rho = base * (1.0 + osc)
    # Ensure in (0,1)
    rho = max(1e-9, min(1.0 - 1e-9, rho))
    delta_g = max(0.0, rho - base)
    return float(rho), float(delta_g)


__all__ = ["compute_contraction_residual", "phi_value"]

