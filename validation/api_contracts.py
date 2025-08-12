from __future__ import annotations

"""
API Contracts Checker

Defines and enforces interface contracts for core subsystems to ensure
peer-review-grade API stability and clarity. Contracts are minimal and
focus on required methods and return shapes only.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple
import inspect

# Targets
import constants.fine_structure_alpha as fine_alpha
import constants.mass_ratios as mass_ratios
import cosmology.ex_nihilo_pipeline as en_pipeline
import foundation.operators.phi_recursion as phi_mod
import utils.precision_framework as precision_mod


@dataclass
class ContractViolation:
    target: str
    reason: str
    detail: str


def _has_callable(obj: Any, name: str) -> bool:
    """Return True if object has a callable attribute with given name."""
    return hasattr(obj, name) and callable(getattr(obj, name))


def check_fine_structure_contract() -> List[ContractViolation]:
    """Validate fine structure module exposes minimal expected APIs.

    Returns list of violations (empty if contract is satisfied).
    """
    violations: List[ContractViolation] = []
    # Class must exist (canonical name)
    if hasattr(fine_alpha, "FineStructureConstant"):
        cls = fine_alpha.FineStructureConstant
    else:
        violations.append(ContractViolation(
            "constants.fine_structure_alpha.FineStructureConstant",
            "missing",
            "class not found"
        ))
        return violations
    inst = cls()

    # required: some derivation or pure getter
    if not (_has_callable(inst, "derive_alpha_inverse") or _has_callable(inst, "alpha_inverse_pure")):
        violations.append(ContractViolation("FineStructureAlpha", "missing_method", "derive_alpha_inverse() or alpha_inverse_pure() required"))

    # Optional but recommended: alternative derivation path and provenance builder
    if not _has_callable(inst, "derive_alternative_phi_expression"):
        violations.append(ContractViolation("FineStructureAlpha", "recommended_method", "derive_alternative_phi_expression() recommended for cross-check"))
    if not _has_callable(inst, "build_complete_provenance"):
        violations.append(ContractViolation("FineStructureAlpha", "recommended_method", "build_complete_provenance(method) recommended"))

    return violations


def check_mass_spectrum_contract() -> List[ContractViolation]:
    """Validate mass spectrum module exposes expected classes/methods."""
    violations: List[ContractViolation] = []
    if not hasattr(mass_ratios, "ParticleSpectrumAlgorithms"):
        violations.append(ContractViolation("constants.mass_ratios.ParticleSpectrumAlgorithms", "missing", "class not found"))
        return violations

    cls = mass_ratios.ParticleSpectrumAlgorithms
    inst = cls()

    # required: derivation entrypoint or clear correction APIs
    if not (_has_callable(inst, "derive_complete_particle_spectrum") or
            (_has_callable(inst, "_compute_qcd_correction") and _has_callable(inst, "_compute_electroweak_correction"))):
        violations.append(ContractViolation(
            "ParticleSpectrumAlgorithms", "missing_method",
            "derive_complete_particle_spectrum() or both _compute_qcd_correction()/_compute_electroweak_correction() required"
        ))

    # Recommend presence of get_mass_ratio API if spectrum derivation is not present
    if not _has_callable(inst, "get_mass_ratio"):
        violations.append(ContractViolation(
            "ParticleSpectrumAlgorithms", "recommended_method",
            "get_mass_ratio(a, b) recommended for downstream checks"
        ))

    return violations


def check_ex_nihilo_contract() -> List[ContractViolation]:
    """Validate ex nihilo pipeline singleton and its primary methods."""
    violations: List[ContractViolation] = []
    if not hasattr(en_pipeline, "EX_NIHILO_PIPELINE"):
        violations.append(ContractViolation("cosmology.ex_nihilo_pipeline.EX_NIHILO_PIPELINE", "missing", "singleton not found"))
        return violations

    pipe = en_pipeline.EX_NIHILO_PIPELINE

    if not _has_callable(pipe, "execute_complete_pipeline"):
        violations.append(ContractViolation("EX_NIHILO_PIPELINE", "missing_method", "execute_complete_pipeline() required"))
    # Recommend integrity verification hook
    if not _has_callable(pipe, "execute_stage"):
        violations.append(ContractViolation("EX_NIHILO_PIPELINE", "recommended_method", "execute_stage(name) recommended"))

    return violations


def run_api_contracts() -> Dict[str, Any]:
    """Run all API contract checks and return a machine-readable report."""
    violations_phi: List[ContractViolation] = []
    # Centralized constants must exist
    if not hasattr(phi_mod, "PHI_VALUE"):
        violations_phi.append(ContractViolation("foundation.operators.phi_recursion.PHI_VALUE", "missing", "constant not found"))
    else:
        try:
            phi_val = float(getattr(phi_mod, "PHI_VALUE"))
            if not (1.0 < phi_val < 2.0):
                violations_phi.append(ContractViolation("PHI_VALUE", "range", "φ must be in (1,2)"))
        except Exception as e:
            violations_phi.append(ContractViolation("PHI_VALUE", "type", f"non-numeric: {e}"))
    if not hasattr(precision_mod, "PRECISION_FRAMEWORK"):
        violations_phi.append(ContractViolation("utils.precision_framework.PRECISION_FRAMEWORK", "missing", "precision framework not found"))
    else:
        pf = getattr(precision_mod, "PRECISION_FRAMEWORK")
        if not hasattr(pf, "compute_with_precision"):
            violations_phi.append(ContractViolation("PRECISION_FRAMEWORK", "missing_method", "compute_with_precision() required"))

    all_violations: Dict[str, List[ContractViolation]] = {
        "fine_structure": check_fine_structure_contract(),
        "mass_spectrum": check_mass_spectrum_contract(),
        "ex_nihilo": check_ex_nihilo_contract(),
        "centralized_constants": violations_phi,
    }
    total = sum(len(v) for v in all_violations.values())
    summary = {k: len(v) for k, v in all_violations.items()}
    return {
        "violations": {
            k: [vi.__dict__ for vi in v] for k, v in all_violations.items()
        },
        "total_violations": total,
        "by_category": summary,
        "status": "passed" if total == 0 else "failed",
    }


def main() -> None:
    """CLI entrypoint: print JSON report for API contract checks."""
    import json
    print(json.dumps(run_api_contracts(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()