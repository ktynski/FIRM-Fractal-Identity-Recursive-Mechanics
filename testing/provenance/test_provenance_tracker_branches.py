import math
import pytest
from provenance.provenance_tracker import ProvenanceTracker, ContaminationError


def test_contains_empirical_data_detection():
    pt = ProvenanceTracker()
    # Use a forbidden constant exactly to trigger detection
    inputs = {"alpha_inv": 137.035999084}
    assert pt.contains_empirical_data(inputs) is True
    contamination = pt.detect_empirical_contamination(inputs)
    assert any("alpha_inv" in s for s in contamination)


def test_log_step_error_bounds_numeric_and_phi_branch():
    pt = ProvenanceTracker()
    # Avoid numeric contamination by passing symbolic-like inputs
    pt.log_step("derive_phi", {"phi_symbol": "(1+sqrt(5))/2"}, 2.0)
    op = pt.derivation_chain[-1]
    assert isinstance(op.error_bounds, dict)
    assert "relative_error" in op.error_bounds and "absolute_error" in op.error_bounds


def test_start_and_complete_operation_wrappers():
    pt = ProvenanceTracker()
    # Start and complete wrappers (compatibility API)
    pt.start_operation("test_operation", mathematical_inputs={"x": 1}, theoretical_basis="phi")
    pt.complete_operation(result=42, derivation_path=["a", "b"], verification_status="ok")
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] >= 2
    assert isinstance(summary["cryptographic_seal"], str)
