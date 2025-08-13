"""
φ-Harmonic Anchor: Elegant peak scaffold from pure φ-geometry (no dynamics)

Defines candidate φ-native anchors ℓ₀ from closed-form angular choices and
simple φ-powers, then generates the peak series ℓ_n = ⌊ℓ₀ φⁿ⌋.

This is theory-only and falsifiable. We do not tune; we expose a few natural
closed forms and let comparison speak for itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict
import math

from foundation.operators.phi_recursion import PHI_VALUE


@dataclass(frozen=True)
class PhiPeakSeries:
    name: str
    l0: int
    peaks: List[int]
    definition: str


def _series_from_l0(l0: int, count: int = 6) -> List[int]:
    phi = PHI_VALUE
    peaks: List[int] = []
    value = float(l0)
    for n in range(count):
        peaks.append(int(round(value)))
        value *= phi
    return peaks


def generate_phi_harmonic_candidates(max_peaks: int = 6) -> List[PhiPeakSeries]:
    phi = PHI_VALUE
    out: List[PhiPeakSeries] = []

    # Golden-chord angle on S^2: θ⋆ = arccos(1/φ²) ⇒ ℓ₀ = round(π/θ⋆)
    theta_chord = math.acos(1.0 / (phi ** 2))
    l0_chord = max(1, int(round(math.pi / theta_chord)))
    out.append(
        PhiPeakSeries(
            name="golden_chord",
            l0=l0_chord,
            peaks=_series_from_l0(l0_chord, max_peaks),
            definition="θ⋆ = arccos(1/φ²); ℓ₀ = round(π/θ⋆); ℓ_n = ⌊ℓ₀ φⁿ⌋",
        )
    )

    # Golden-curvature angle: θ⋆ = 2π/φ^k with small integer k (natural scale family)
    for k in (2, 3, 4, 5):
        theta = 2.0 * math.pi / (phi ** k)
        l0 = max(1, int(round(math.pi / theta)))
        out.append(
            PhiPeakSeries(
                name=f"golden_curvature_k{k}",
                l0=l0,
                peaks=_series_from_l0(l0, max_peaks),
                definition=f"θ⋆ = 2π/φ^{k}; ℓ₀ = round(π/θ⋆); ℓ_n = ⌊ℓ₀ φⁿ⌋",
            )
        )

    # Pure φ-power anchors: ℓ₀ = round(φ^n) for modest n (natural φ-lattice indices)
    for n in (9, 10, 11, 12, 13):
        l0p = int(round(phi ** n))
        out.append(
            PhiPeakSeries(
                name=f"phi_power_n{n}",
                l0=l0p,
                peaks=_series_from_l0(l0p, max_peaks),
                definition=f"ℓ₀ = round(φ^{n}); ℓ_n = ⌊ℓ₀ φⁿ⌋",
            )
        )

    return out


def best_candidate_by_target(target: int = 220, count: int = 6) -> PhiPeakSeries:
    cands = generate_phi_harmonic_candidates(count)
    # Choose the candidate with ℓ₀ closest to target (no tuning of any factor)
    best = min(cands, key=lambda s: abs(s.l0 - target))
    return best


