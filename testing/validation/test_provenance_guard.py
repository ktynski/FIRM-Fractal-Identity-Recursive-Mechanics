import pytest
from validation.provenance_guard import ProvenanceGuard, ProofObject, ProvenanceGuardError


def test_registry_loads():
    guard = ProvenanceGuard()
    assert guard.is_quarantined("omega_lambda_correction_1.108")


def test_fail_without_proof():
    guard = ProvenanceGuard()
    with pytest.raises(ProvenanceGuardError) as exc:
        guard.require_proof("omega_lambda_correction_1.108", None)
    assert "Quarantined item" in str(exc.value)


def test_accept_valid_proof():
    guard = ProvenanceGuard()
    proof = ProofObject(
        id="thm-omega-lambda-φ-vacuum-001",
        theorem="Vacuum φ-ζ regularized sum yields multiplier C with regulator-independence",
        derivation_tree_hash="abcd1234ef567890",
        regulator="zeta",
        convergence_proof="Abel-Plana bound with ε<1e-5",
        error_bound="< 1e-5"
    )
    guard.require_proof("omega_lambda_correction_1.108", proof)
    assert "omega_lambda_correction_1.108" in guard.approved


def test_non_quarantined_key_noop():
    guard = ProvenanceGuard()
    # Using a random key not in registry should not raise
    guard.require_proof("nonexistent_key", None)