"""
Epsilon Stability Analysis: S(ε) feasibility proxy from axioms (theory-only)

This module computes a theory-native stability functional over ε via:
  - δ_κ(ε): spectral curvature of a torsion-parameterized operator T_ε
  - δ_G(ε): Grace contraction residual (A𝒢.3); here zero (φ⁻¹ exact)
  - δ_C(ε): Categorical coherence residual (A𝒢.4); current checker is k-independent,
            so it contributes a constant offset that does not affect the minimizer

S(ε) = (δ_κ/τ_κ)^2 + (δ_G/τ_G)^2 + (δ_C/τ_C)^2, with φ-native tolerances
  τ_κ = φ^(-9), τ_G = φ^(-12), τ_C = φ^(-7)

Candidate ε values are derived from the predictions registry by taking the
registered φ-geometric candidate family and mapping ℓ0 → k = log_φ(ℓ0),
then ε = k - (12 + φ⁻¹).

No empirical inputs; pure mathematics.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from validation.grace_contraction_proxy import compute_contraction_residual
from validation.coherence_suite import coherence_pass_fraction


REGISTRY_PATH = Path("validation/firm_predictions_registry.json")


def phi_value() -> float:
    return (1.0 + math.sqrt(5.0)) / 2.0


def log_base_phi(x: float) -> float:
    """Return log_φ(x) for x>0 (pure math)."""
    phi = phi_value()
    return math.log(max(float(x), 1e-300), phi)


def load_candidate_l0_values() -> List[float]:
    """Load ℓ0 candidates from the predictions registry (pure theory records)."""
    if not REGISTRY_PATH.exists():
        return []
    data = json.loads(REGISTRY_PATH.read_text())
    candidates: List[float] = []
    # Find the record for the candidate family
    for rec_id, rec in data.items():
        if rec.get("prediction_type") == "phi_geometric_candidates_complete":
            series = rec.get("predicted_values", {}).get("candidate_series", [])
            for c in series:
                l0 = c.get("l0")
                if l0 is not None:
                    try:
                        candidates.append(float(l0))
                    except Exception:
                        continue
    # Deduplicate and sort for determinism
    uniq = sorted({round(v, 6) for v in candidates})
    return [float(v) for v in uniq]


def compute_epsilons_from_l0(l0_values: List[float]) -> List[Tuple[float, float]]:
    """Return list of (l0, epsilon) using k = log_φ(l0), ε = k - (12 + φ⁻¹)."""
    phi = phi_value()
    base = 12.0 + 1.0 / phi
    pairs = []
    for l0 in l0_values:
        k = log_base_phi(l0)
        eps = k - base
        pairs.append((l0, eps))
    return pairs


def build_T_epsilon(epsilon: float, matrix_size: int = 30) -> np.ndarray:
    """Construct torsion-parameterized operator T_ε (no targets, pure φ-structure)."""
    phi = phi_value()
    k = 12.0 + 1.0 / phi + float(epsilon)

    # φ-scaling and phases (mirrors MTQ structure but with k in place of n)
    dim = int(max(10, min(matrix_size, 50)))
    mat = np.zeros((dim, dim), dtype=complex)

    # Core φ-scaling
    scale = phi ** (-k / 7.0)

    # Fill diagonal and near-diagonals with φ-native couplings
    for i in range(dim):
        for j in range(dim):
            if i == j:
                mat[i, j] = scale * (1.0 + (i + 1) / phi)
            elif abs(i - j) == 1:
                coupling = scale / (phi ** abs(i - j))
                phase = 2.0 * math.pi * (i + j + 1) / (k + phi)
                mat[i, j] = coupling * complex(math.cos(phase), math.sin(phase))
            elif abs(i - j) == 2:
                secondary = scale / (phi ** 2)
                mat[i, j] = secondary * complex(0.0, 1.0) * ((-1) ** (i + j))

    # Anti-symmetric torsion contributions (no fixed period)
    torsion_osc = math.sin(math.pi * k / (k + phi))
    torsion_damp = phi ** (-(k / (1.0 + phi)))
    morphic_strength = (1.0 / (phi ** 4)) / (2.0 * math.pi)
    torsion = morphic_strength * torsion_osc * torsion_damp
    for i in range(dim - 1):
        for j in range(i + 1, dim):
            t_elem = torsion * complex(0.0, 1.0) * math.sin(math.pi * (i + j + 1) / (k + phi))
            mat[i, j] += t_elem
            mat[j, i] -= t_elem

    return mat


def lambda_min_abs(epsilon: float, matrix_size: int = 30) -> float:
    mat = build_T_epsilon(epsilon, matrix_size=matrix_size)
    try:
        ev = np.linalg.eigvals(mat)
    except np.linalg.LinAlgError:
        return float("inf")
    return float(min(abs(x) for x in ev)) if len(ev) > 0 else float("inf")


def delta_kappa(epsilon: float, delta: float) -> float:
    """Discrete curvature of |λ_min| at ε with step Δ."""
    f_prev = lambda_min_abs(epsilon - delta)
    f_now = lambda_min_abs(epsilon)
    f_next = lambda_min_abs(epsilon + delta)
    return abs(f_prev - 2.0 * f_now + f_next)


def _operator_norm_2(mat: np.ndarray) -> float:
    """Spectral norm (2-norm) via largest singular value."""
    try:
        s = np.linalg.svd(mat, compute_uv=False)
        return float(s[0]) if s.size > 0 else 0.0
    except np.linalg.LinAlgError:
        return float("inf")


def delta_G(epsilon: float) -> float:
    """Grace contraction residual via k-parameterized proxy ρ(k) (no data)."""
    phi = phi_value()
    k = 12.0 + 1.0/phi + float(epsilon)
    _rho, delta_g = compute_contraction_residual(k)
    return float(delta_g)


def delta_C(epsilon: float) -> float:
    """Coherence residual from k-parameterized diagram pass fraction (no data)."""
    phi = phi_value()
    k = 12.0 + 1.0/phi + float(epsilon)
    res = coherence_pass_fraction(k)
    pass_fraction = float(res.get("pass_fraction", 0.0))
    return float(1.0 - pass_fraction)


def S_epsilon(epsilon: float) -> Dict[str, float]:
    """Return components and S(ε) with φ-native tolerances."""
    phi = phi_value()
    # φ-native tolerances as discussed
    tau_k = phi ** (-9.0)
    tau_g = phi ** (-12.0)
    tau_c = phi ** (-7.0)
    # φ-native finite-difference step
    delta = phi ** (-3.0)
    d_k = delta_kappa(epsilon, delta)
    d_g = delta_G(epsilon)
    d_c = delta_C(epsilon)
    S = (d_k / tau_k) ** 2 + (d_g / tau_g) ** 2 + (d_c / tau_c) ** 2
    return {
        "epsilon": float(epsilon),
        "delta_kappa": float(d_k),
        "delta_G": float(d_g),
        "delta_C": float(d_c),
        "S": float(S),
    }


def evaluate_candidates(matrix_size: int = 30) -> List[Dict[str, float]]:
    l0_vals = load_candidate_l0_values()
    pairs = compute_epsilons_from_l0(l0_vals)
    results: List[Dict[str, float]] = []
    for l0, eps in pairs:
        comp = S_epsilon(eps)
        comp["l0"] = float(l0)
        results.append(comp)
    # Sort by S ascending
    results.sort(key=lambda r: r["S"])
    return results


def main() -> None:
    pairs = evaluate_candidates()
    if not pairs:
        print("No candidates found. Ensure registry is initialized.")
        return
    # Print compact table
    print("ε-stability (lower S is better)\n")
    print(f"{'rank':>4}  {'l0':>8}  {'ε':>10}  {'δκ':>12}  {'S':>14}")
    for idx, r in enumerate(pairs, 1):
        print(f"{idx:>4}  {r['l0']:>8.3f}  {r['epsilon']:>10.4f}  {r['delta_kappa']:>12.6e}  {r['S']:>14.6e}")


if __name__ == "__main__":
    main()


