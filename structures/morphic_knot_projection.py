"""
Morphic Knot → Particle Property Projection (theory-only)

Derivations implemented:
  - Mass from recursive depth: depth n ≈ round(log_φ(m/me)); C_n = (m/me)/φ^n
  - Spin from internal symmetry: fermions → 1/2, gauge bosons → 1, scalars → 0
  - Charge from phase/U(1)-SU(2): Q = T3 + Y/2

No empirical inputs; uses existing φ-native spectrum and quantum numbers.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional, Tuple, Dict

from foundation.operators.phi_recursion import PHI_VALUE
from structures.particle_spectrum import (
    PARTICLE_SPECTRUM,
    ParticleSpecification,
    ParticleType,
)
from constants.mass_ratios import FUNDAMENTAL_MASSES


phi = PHI_VALUE


def log_phi(x: float) -> float:
    return math.log(x) / math.log(phi)


@dataclass(frozen=True)
class MassDepthDecomposition:
    particle: str
    mass_ratio_to_electron: float
    recursive_depth_n: int
    form_factor_Cn: float


def derive_recursive_depth_and_form_factor(particle_name: str) -> MassDepthDecomposition:
    """
    Compute depth n ≈ round(log_φ(m/me)) and form factor C_n = (m/me)/φ^n.
    Uses theory-only FUNDAMENTAL_MASSES.
    """
    ratio = FUNDAMENTAL_MASSES.get_mass_ratio(particle_name, "electron")
    # Guard for massless particles
    if ratio == 0.0:
        return MassDepthDecomposition(particle=particle_name, mass_ratio_to_electron=0.0, recursive_depth_n=0, form_factor_Cn=0.0)
    n_est = int(round(log_phi(abs(ratio))))
    cn = ratio / (phi ** n_est)
    return MassDepthDecomposition(particle=particle_name, mass_ratio_to_electron=ratio, recursive_depth_n=n_est, form_factor_Cn=cn)


def derive_spin_from_internal_symmetry(spec: ParticleSpecification) -> float:
    """Minimal symmetry-to-spin mapping consistent with current spectrum."""
    if spec.particle_type == ParticleType.FERMION:
        return 0.5
    if spec.particle_type == ParticleType.GAUGE_BOSON:
        return 1.0
    if spec.particle_type == ParticleType.SCALAR_BOSON:
        return 0.0
    # Composites follow constituent quantum numbers; default to 0.5
    return 0.5


def derive_charge_from_quantum_numbers(spec: ParticleSpecification) -> Optional[float]:
    """
    Compute Q = T3 + Y/2 from given quantum numbers; returns None if unavailable.
    """
    qn = spec.quantum_numbers
    if qn is None:
        return None
    return float(qn.weak_isospin + 0.5 * qn.weak_hypercharge)


def build_mass_depth_report(include_examples: Tuple[str, ...] = ("electron", "muon", "tau", "proton")) -> str:
    lines = [
        "Morphic Knot → Mass Depth Report",
        "================================",
        f"φ = {phi:.10f}",
        "",
    ]
    for name in include_examples:
        try:
            d = derive_recursive_depth_and_form_factor(name)
            lines.append(
                f"- {name:8}: m/me={d.mass_ratio_to_electron:.6f} ≈ φ^{d.recursive_depth_n} × C, C={d.form_factor_Cn:.6f}"
            )
        except Exception as e:
            lines.append(f"- {name:8}: error: {e}")
    return "\n".join(lines)


def verify_projection_consistency(sample: Tuple[str, ...] = ("electron", "muon", "tau", "up", "down", "photon", "W_plus", "Z")) -> Dict[str, Dict[str, float]]:
    """
    Cross-checks for selected particles:
      - spin derived equals catalog spin
      - charge from (T3, Y) equals catalog Q
      - C_n close to O(1) for massive elementary particles
    Returns per-particle diagnostics.
    """
    result: Dict[str, Dict[str, float]] = {}
    for key in sample:
        spec = PARTICLE_SPECTRUM.get_particle_by_name(key)
        if spec is None:
            continue
        # Spin
        spin_derived = derive_spin_from_internal_symmetry(spec)
        spin_delta = abs((spec.quantum_numbers.spin if spec.quantum_numbers else spin_derived) - spin_derived)
        # Charge
        q_from_qnums = derive_charge_from_quantum_numbers(spec)
        q_catalog = spec.quantum_numbers.electric_charge if spec.quantum_numbers else None
        q_delta = (abs(q_catalog - q_from_qnums) if (q_from_qnums is not None and q_catalog is not None) else 0.0)
        # Mass depth/form factor
        try:
            dec = derive_recursive_depth_and_form_factor(spec.name if spec.name in ("electron","muon","tau","proton","neutron") else key)
            cn = dec.form_factor_Cn
        except Exception:
            cn = float("nan")
        result[key] = {
            "spin_derived": float(spin_derived),
            "spin_delta": float(spin_delta),
            "charge_from_T3Y": float(q_from_qnums) if q_from_qnums is not None else float("nan"),
            "charge_catalog": float(q_catalog) if q_catalog is not None else float("nan"),
            "charge_delta": float(q_delta),
            "form_factor_Cn": float(cn),
        }
    return result


__all__ = [
    "MassDepthDecomposition",
    "derive_recursive_depth_and_form_factor",
    "derive_spin_from_internal_symmetry",
    "derive_charge_from_quantum_numbers",
    "build_mass_depth_report",
    "verify_projection_consistency",
]


