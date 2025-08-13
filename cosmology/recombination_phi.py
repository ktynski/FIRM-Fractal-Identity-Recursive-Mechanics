"""
φ-Native Recombination (theory-only)

Defines the recombination redshift z_rec and width purely from φ-native
background, avoiding empirical targets. We use a symmetry threshold on the
baryon loading parameter R(z) = 3ρ_b/(4ρ_γ). Recombination is taken to occur
when R(z_rec) crosses a φ-native equilibrium break: R(z_rec) = φ^{-1}.

This is a concrete, testable theoretical choice (no fitting). Width is set by
Δz/ (1+z_rec) = φ^{-3} as a conservative φ-damping scale.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Dict

from foundation.operators.phi_recursion import PHI_VALUE


@dataclass(frozen=True)
class RecombinationResult:
    z_rec: float
    width_delta_z: float
    phi_threshold: float
    provenance: Dict[str, str]


def compute_recombination_from_phi_threshold(omega_baryon: float, omega_gamma: float) -> RecombinationResult:
    """
    Solve for z_rec from R(z) = (3/4) (Ω_b/Ω_γ) (1/(1+z)) with threshold R(z_rec) = φ^{-1}.
    ⇒ 1 + z_rec = (3/4)(Ω_b/Ω_γ) φ.

    Width is set by Δz = (1+z_rec) φ^{-3} (φ-damping scale for transition).
    """
    phi = PHI_VALUE
    ratio = (3.0 / 4.0) * (float(omega_baryon) / max(float(omega_gamma), 1e-30)) * float(phi)
    z_rec = max(ratio - 1.0, 0.0)
    width = (1.0 + z_rec) * (phi ** (-3))
    return RecombinationResult(
        z_rec=float(z_rec),
        width_delta_z=float(width),
        phi_threshold=float(phi ** (-1)),
        provenance={
            "R(z)": "(3/4)(Ω_b/Ω_γ)/(1+z)",
            "threshold": "R(z_rec) = φ^{-1}",
            "solution": "1+z_rec = (3/4)(Ω_b/Ω_γ) φ",
            "width": "Δz = (1+z_rec) φ^{-3}",
        },
    )


