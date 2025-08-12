import pytest

from provenance.provenance_tracker import ProvenanceTracker, ContaminationError


def test_contains_empirical_numeric_forbidden_and_string_keyword():
    pt = ProvenanceTracker()
    assert pt.contains_empirical_data({"c": 299792458}) is True
    assert pt.is_empirical_value("experimental setup") is True


def test_detect_empirical_contamination_lists_matches():
    pt = ProvenanceTracker()
    out = pt.detect_empirical_contamination({"c": 299792458, "note": "observed"})
    assert any("Speed of light" in s or "observed" in s for s in out)


def test_log_step_contamination_raises():
    pt = ProvenanceTracker()
    with pytest.raises(ContaminationError):
        pt.log_step("compute c", {"c": 299792458}, 1.0)


def test_compat_wrappers_start_complete_and_summary():
    pt = ProvenanceTracker()
    # Start/complete wrappers should add steps without contamination
    pt.start_operation("compat_start", mathematical_inputs={"x": 1}, theoretical_basis="axiom")
    pt.complete_operation(result=42, derivation_path=["a", "b"], verification_status="ok")
    # Summary should reflect operations and cryptographic seal present
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] >= 2
    assert isinstance(summary.get("cryptographic_seal"), str)

