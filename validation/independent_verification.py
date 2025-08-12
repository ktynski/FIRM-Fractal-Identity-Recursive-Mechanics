from __future__ import annotations

"""
Independent Verification Runner

Re-executes key derivations in a clean Python context, computes cryptographic
hashes of the outputs, and emits a machine-readable JSON report including an
environment snapshot. Designed for peer-review reproducibility checks.

Scope:
  - Fine structure constant (pure-math derivation path only)
  - Mass spectrum summary (pure-math path)
  - Ex Nihilo pipeline (end-to-end) with seals/proofs summary

No empirical values are used during derivation; comparison is outside this runner.
"""

import json
import hashlib
import platform
import sys
import os
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

# Imports from the codebase
try:
    from constants.fine_structure_alpha import FineStructureAlpha  # canonical name
except Exception:  # pragma: no cover - compatibility path
    from constants.fine_structure_alpha import FineStructureConstant as FineStructureAlpha
from constants.mass_ratios import ParticleSpectrumAlgorithms
from cosmology.ex_nihilo_pipeline import EX_NIHILO_PIPELINE, CosmogenesisResult


@dataclass
class EnvironmentSnapshot:
    python_version: str
    platform: str
    machine: str
    processor: str
    implementation: str
    executable: str
    cwd: str
    env_user: Optional[str]
    env_path_hash: str
    timestamp_utc: str

    @staticmethod
    def capture() -> "EnvironmentSnapshot":
        env_path_hash = hashlib.sha256(os.environ.get("PATH", "").encode()).hexdigest()
        return EnvironmentSnapshot(
            python_version=sys.version.replace("\n", " "),
            platform=platform.platform(),
            machine=platform.machine(),
            processor=platform.processor(),
            implementation=platform.python_implementation(),
            executable=sys.executable,
            cwd=os.getcwd(),
            env_user=os.environ.get("USER") or os.environ.get("USERNAME"),
            env_path_hash=env_path_hash,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
        )


def _sha256_of_obj(obj: Any) -> str:
    """Stable JSON dump + SHA-256 to fingerprint any JSON-serializable object."""
    try:
        data = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    except TypeError:
        data = str(obj).encode()
    return hashlib.sha256(data).hexdigest()


def _safe_float(x: Any) -> float:
    """Convert to float, returning NaN on failure (no exceptions raised)."""
    try:
        return float(x)
    except Exception:
        return float("nan")


def verify_fine_structure() -> Dict[str, Any]:
    """Compute theory-only α⁻¹ and include method/provenance where available."""
    alpha = FineStructureAlpha()
    # Expect the implementation to provide a primary derivation method; we
    # avoid any experimental comparison here by design (pure math only).
    result_map: Dict[str, Any] = {}
    try:
        # Prefer a structured derivation API if present; else fall back to value getter
        if hasattr(alpha, "derive_alpha_inverse"):
            derived = alpha.derive_alpha_inverse()
            value = _safe_float(getattr(derived, "value", derived))
            provenance = getattr(derived, "provenance", None)
        elif hasattr(alpha, "derive_primary_phi_expression"):
            derived = alpha.derive_primary_phi_expression()
            value = _safe_float(getattr(derived, "alpha_inverse_value", float("nan")))
            provenance = getattr(derived, "phi_expression", None)
        elif hasattr(alpha, "alpha_inverse_pure"):
            value = _safe_float(alpha.alpha_inverse_pure())
            provenance = None
        else:
            # Fallback to a common attribute pattern
            value = _safe_float(getattr(alpha, "alpha_inverse", float("nan")))
            provenance = None
        result_map = {
            "quantity": "alpha_inverse",
            "value": value,
            "provenance": provenance,
            "method": (
                "derive_alpha_inverse" if hasattr(alpha, "derive_alpha_inverse")
                else "derive_primary_phi_expression" if hasattr(alpha, "derive_primary_phi_expression")
                else "alpha_inverse_pure"
            ),
        }
    except Exception as e:
        result_map = {
            "quantity": "alpha_inverse",
            "error": f"{type(e).__name__}: {e}",
        }
    result_map["hash"] = _sha256_of_obj(result_map)
    return result_map


def verify_mass_spectrum_summary() -> Dict[str, Any]:
    """Compute compact mass spectrum summary using available algorithms."""
    algo = ParticleSpectrumAlgorithms()
    summary: Dict[str, Any] = {}
    try:
        # If there is a structured API, use it; otherwise compute a compact summary
        if hasattr(algo, "derive_complete_particle_spectrum"):
            spectrum = algo.derive_complete_particle_spectrum()  # expected: Dict[str, ParticleMass]
            # Normalize to plain mapping: {name: mass_value}
            compact: Dict[str, float] = {}
            for name, obj in (spectrum or {}).items():
                mass_val = getattr(obj, "mass", None) or getattr(obj, "value", None) or obj
                compact[name] = _safe_float(mass_val)
            # Provide stable ordering for hashing determinism
            compact_ordered = {k: compact[k] for k in sorted(compact.keys())}
            summary = {"spectrum_compact": compact_ordered, "source": "derive_complete_particle_spectrum"}
        else:
            # Minimal deterministic probe: derive some base corrections used
            compact = {
                "qcd_correction": _safe_float(getattr(algo, "_compute_qcd_correction", lambda: float("nan"))()),
                "ew_correction": _safe_float(getattr(algo, "_compute_electroweak_correction", lambda: float("nan"))()),
            }
            summary = {"spectrum_compact": compact, "source": "corrections_only"}
    except Exception as e:
        summary = {"error": f"{type(e).__name__}: {e}"}
    summary["hash"] = _sha256_of_obj(summary)
    return summary


def verify_ex_nihilo_pipeline() -> Dict[str, Any]:
    """Execute pipeline and return integrity-focused summary (no payload bloat)."""
    try:
        result: CosmogenesisResult = EX_NIHILO_PIPELINE.execute_complete_pipeline()
        # Summarize critical integrity signals without large payloads
        seals_ok = result.verify_complete_integrity()
        stage_count = result.total_stages_completed
        pipeline_ok = bool(result.pipeline_successful)
        proof_count = len(getattr(result, "executable_proofs", []))
        audit_len = len(getattr(result, "cryptographic_audit_trail", []))
        summary = {
            "pipeline_successful": pipeline_ok,
            "stages_completed": stage_count,
            "cryptographic_integrity": seals_ok,
            "executable_proofs": proof_count,
            "audit_trail_length": audit_len,
            "final_params_hash": _sha256_of_obj(result.final_universe_parameters),
            "cmb_predictions_hash": _sha256_of_obj(result.cmb_predictions),
        }
    except Exception as e:
        summary = {"error": f"{type(e).__name__}: {e}"}
    summary["hash"] = _sha256_of_obj(summary)
    return summary


def run_independent_verification(canonical_hashes: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Run independent verification workflow. If canonical_hashes is provided,
    compare computed hashes; otherwise emit a report suitable for registering
    as canonical (peer review baseline).
    """
    env = EnvironmentSnapshot.capture()

    alpha_res = verify_fine_structure()
    mass_res = verify_mass_spectrum_summary()
    en_res = verify_ex_nihilo_pipeline()

    results = {
        "alpha_inverse": alpha_res,
        "mass_spectrum": mass_res,
        "ex_nihilo_pipeline": en_res,
    }

    overall_ok = True
    comparisons: Dict[str, Any] = {}

    if canonical_hashes:
        for key, res in results.items():
            got = res.get("hash")
            want = canonical_hashes.get(key)
            match = (got == want) if want else False
            comparisons[key] = {"expected": want, "actual": got, "match": match}
            overall_ok = overall_ok and match

    report = {
        "environment": asdict(env),
        "results": results,
        "comparisons": comparisons or None,
        "overall_status": "passed" if overall_ok else "mismatch" if canonical_hashes else "recorded",
        "report_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "quantities": list(results.keys()),
            "hashes": {k: results[k].get("hash") for k in results},
        },
    }
    return report


def main() -> None:
    # CLI entry: print JSON to stdout
    report = run_independent_verification()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()