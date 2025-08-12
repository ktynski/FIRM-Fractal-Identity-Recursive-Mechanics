from __future__ import annotations

import pytest

import provenance.provenance_tracker as pt
from provenance.provenance_tracker import ProvenanceTracker, OperationType, ContaminationError


def test_is_empirical_value_string_keywords():
    tracker = ProvenanceTracker()
    assert tracker.is_empirical_value("Experimental data point") is True
    assert tracker.is_empirical_value("observed trend") is True
    assert tracker.is_empirical_value("pure theory") is False


def test_detect_empirical_contamination_report():
    tracker = ProvenanceTracker()
    items = tracker.detect_empirical_contamination({
        "alpha_inv": 137.035999084,  # forbidden numeric
        "note": "measured"
    })
    assert any("alpha_inv" in s for s in items)
    assert any("note" in s for s in items)


def test_classify_operation_all_branches():
    tracker = ProvenanceTracker()
    assert tracker.classify_operation("Apply AXIOM A𝒢.1") == OperationType.AXIOM_APPLICATION
    assert tracker.classify_operation("use theorem of phi") == OperationType.THEOREM_USE
    assert tracker.classify_operation("phi recursion step") == OperationType.RECURSION
    assert tracker.classify_operation("fixed point computation") == OperationType.FIXED_POINT
    assert tracker.classify_operation("validation compare") == OperationType.VALIDATION
    assert tracker.classify_operation("derive structure") == OperationType.DERIVATION
    assert tracker.classify_operation("misc operation") == OperationType.COMPUTATION


def test_compute_error_bounds_sequences_and_precision_fallback(monkeypatch):
    tracker = ProvenanceTracker()
    # Force precision framework fallback path
    monkeypatch.setattr(pt, "PRECISION_FRAMEWORK", None, raising=False)
    # Use list output to trigger sequence branch
    tracker.log_step("sequence output", {"phi": 1.6, "n": 3}, [1.0, 2.0, 3.0])
    last = tracker.derivation_chain[-1]
    assert isinstance(last.error_bounds, dict)
    assert "relative_error" in last.error_bounds


def test_get_mathematical_justification_else_branch():
    tracker = ProvenanceTracker()
    tracker.log_step("generic operation", {"x": 1}, 1)
    just = tracker.derivation_chain[-1].mathematical_justification
    assert isinstance(just, str) and len(just) > 0
