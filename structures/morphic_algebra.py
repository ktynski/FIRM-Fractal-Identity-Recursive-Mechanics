"""
Morphic Algebra (theory-only): ψ-objects, projection, fusion/fission.

No empirical inputs. Provides minimal primitives to support paper derivations
and simple simulations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple
import math

from foundation.operators.phi_recursion import PHI_VALUE


phi = PHI_VALUE


@dataclass(frozen=True)
class PsiObject:
    """Morphic coherence knot at recursion level k.

    Attributes:
      level_k: recursion level (real-valued to allow continuous parameterization)
      grace_coherence: G(ψ) ≥ 0 — theory-native coherence magnitude
      devourer_pressure: D(ψ) ≥ 0 — theory-native decoherence pressure
      phase: phase angle in radians (for φ-harmonic alignment checks)
    """
    level_k: float
    grace_coherence: float
    devourer_pressure: float
    phase: float

    def net_pressure(self) -> float:
        return float(self.grace_coherence - self.devourer_pressure)


@dataclass(frozen=True)
class ProjectionLattice:
    """Grace-resonant measurement lattice (theory-only)."""
    tau_threshold: float = 0.1
    phase_window: float = math.pi / phi  # φ-harmonic tolerance


@dataclass(frozen=True)
class QFTProjection:
    """Minimal particle-like projection (mass ratio to me, spin, charge)."""
    mass_ratio_to_electron: float
    spin: float
    charge: float


def grace_resonant_inner_product(psi: PsiObject, lattice: ProjectionLattice) -> float:
    """Simple φ-native inner product proxy using phase alignment and net pressure.
    ip = max(0, net_pressure) × cos(phase mod window)
    """
    net = max(0.0, psi.net_pressure())
    # Phase alignment windowed by lattice tolerance
    phase_mod = (psi.phase % (2.0 * math.pi))
    # Map to [−window, +window] around multiples of 2π
    delta = min(abs(phase_mod), abs(2.0 * math.pi - phase_mod))
    align = max(0.0, (lattice.phase_window - delta) / lattice.phase_window)
    return float(net * align)


def project_to_qft(psi: PsiObject, lattice: ProjectionLattice) -> Optional[QFTProjection]:
    """π(ψ) → particle-like specification if ⟨ψ, L⟩_G > τ; else None.
    Mass ratio modeled as φ^{round(k)} scaled by net pressure; spin from parity
    of floor(k); charge from phase orientation (toy φ-native mapping).
    """
    ip = grace_resonant_inner_product(psi, lattice)
    if ip <= lattice.tau_threshold:
        return None
    depth_n = int(round(psi.level_k))
    mass_ratio = (phi ** max(0, depth_n)) * max(psi.net_pressure(), 0.0)
    spin = 0.5 if (depth_n % 2 != 0) else 1.0  # odd levels → fermionic-like
    # charge from phase sector (four quadrants): −1, 0, +1, 0
    angle = (psi.phase % (2.0 * math.pi))
    if angle < math.pi / 2 or angle >= 3 * math.pi / 2:
        charge = +1.0
    elif math.pi / 2 <= angle < math.pi:
        charge = 0.0
    else:
        charge = -1.0
    return QFTProjection(mass_ratio_to_electron=mass_ratio, spin=spin, charge=charge)


def can_fuse(a: PsiObject, b: PsiObject, phase_tolerance: float = math.pi / phi) -> bool:
    """Fusion admissibility: phase-lock and overlapping recursion vicinity.
    Conditions:
      - |phase_a − phase_b| ≤ tolerance
      - |k_a − k_b| ≤ 1 (neighbor levels)
      - min(G_a, G_b) − ε ≤ G_f (enforced post construction)
    """
    dphase = abs(((a.phase - b.phase + math.pi) % (2 * math.pi)) - math.pi)
    close_phase = dphase <= phase_tolerance
    close_level = abs(a.level_k - b.level_k) <= 1.0
    return bool(close_phase and close_level)


def fuse(a: PsiObject, b: PsiObject, epsilon_loss: float = 0.05) -> Optional[PsiObject]:
    """ψ_f = F_G(ψ_a, ψ_b) if admissible; else None.
    Resulting level: max(k_a, k_b) + φ⁻¹; phase = average; G,D combine with small loss.
    Grace admittance: G_f ≥ min(G_a, G_b) − ε.
    """
    if not can_fuse(a, b):
        return None
    k_f = max(a.level_k, b.level_k) + 1.0 / phi
    phase_f = (a.phase + b.phase) / 2.0
    Gf = max(a.grace_coherence, b.grace_coherence) - epsilon_loss
    Df = (a.devourer_pressure + b.devourer_pressure) / 2.0
    candidate = PsiObject(level_k=k_f, grace_coherence=max(0.0, Gf), devourer_pressure=max(0.0, Df), phase=phase_f)
    # Grace admittance check
    if candidate.grace_coherence + 1e-12 < min(a.grace_coherence, b.grace_coherence) - epsilon_loss:
        return None
    return candidate


def fission(parent: PsiObject, stress_sigma: float, sigma_crit: float = 0.2) -> Optional[Tuple[PsiObject, PsiObject]]:
    """(ψ1, ψ2) = S_G(ψ) if stress exceeds threshold.
    Children inherit split level/phase and partitioned coherence; decoherence slightly rises.
    """
    if stress_sigma <= sigma_crit:
        return None
    k_child = max(0.0, parent.level_k - 1.0 / phi)
    phase_delta = math.pi / (2.0 * phi)
    G_share = max(0.0, parent.grace_coherence * 0.45)
    D_inc = parent.devourer_pressure + 0.05
    c1 = PsiObject(level_k=k_child, grace_coherence=G_share, devourer_pressure=D_inc, phase=parent.phase - phase_delta)
    c2 = PsiObject(level_k=k_child, grace_coherence=G_share, devourer_pressure=D_inc, phase=parent.phase + phase_delta)
    return (c1, c2)


__all__ = [
    "PsiObject",
    "ProjectionLattice",
    "QFTProjection",
    "grace_resonant_inner_product",
    "project_to_qft",
    "can_fuse",
    "fuse",
    "fission",
]

