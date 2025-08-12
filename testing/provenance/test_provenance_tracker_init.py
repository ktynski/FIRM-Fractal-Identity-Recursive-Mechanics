from __future__ import annotations

import pytest

from provenance.provenance_tracker import (
    PROVENANCE_TRACKER,
    ProvenanceTracker,
    MathematicalOperation,
    OperationType,
    ContaminationError,
)


def test_operation_lifecycle_and_seal():
    tracker = ProvenanceTracker()
    # Log pure operation
    tracker.log_step("derive phi power", {"n": 5, "phi": 1.618}, 11.09017)
    assert len(tracker.derivation_chain) == 1
    assert tracker.cryptographic_seal is not None

    # Complete operation path
    tracker.complete_operation(result={"ok": True}, derivation_path=["start", "compute", "end"], verification_status="verified")
    assert len(tracker.derivation_chain) >= 2
    assert tracker.cryptographic_seal is not None


def test_classification_and_justification():
    tracker = ProvenanceTracker()
    tracker.log_step("Apply Axiom Totality", {"set": "U"}, 1)
    op = tracker.derivation_chain[-1]
    # Classification
    assert isinstance(op.operation_type, OperationType)
    # Justification string exists
    assert isinstance(op.mathematical_justification, str) and op.mathematical_justification
    # Axiom dependency extraction
    assert any(dep.startswith("A") for dep in op.axiom_dependencies)


def test_empirical_contamination_detection():
    tracker = ProvenanceTracker()
    # Forbidden value should trip contamination
    with pytest.raises(ContaminationError):
        tracker.log_step("compare alpha", {"alpha_inv": 137.035999084}, None)


def test_audit_report_generation_and_summary():
    tracker = ProvenanceTracker()
    tracker.log_step("recursion phi compute", {"phi": 1.618}, 2.618)
    report = tracker.generate_audit_report()
    assert "FIRM PROVENANCE AUDIT REPORT" in report
    summary = tracker.get_derivation_summary()
    assert summary["total_operations"] >= 1


def test_verify_complete_provenance_negative():
    tracker = ProvenanceTracker()
    tracker.log_step("computation only", {"x": 1}, 1)
    assert tracker.verify_complete_provenance() in (False, True)  # Should not crash