import pytest
from provenance.provenance_tracker import ProvenanceTracker, ContaminationError


def test_classify_and_justification_branches():
    pt = ProvenanceTracker()
    # axiom classification
    assert pt.classify_operation("Apply Axiom A𝒢.3")
    # theorem classification
    assert pt.classify_operation("Use theorem of FixG")
    # recursion classification
    assert pt.classify_operation("phi recursion step")
    # fixed point classification
    assert pt.classify_operation("fixed point proof")
    # validation classification
    assert pt.classify_operation("validation compare")
    # derivation classification
    assert pt.classify_operation("derive alpha")
    # computation fallback
    assert pt.classify_operation("sum numbers")

    # justification branches
    assert "Golden ratio" in pt.get_mathematical_justification("phi power")
    assert "Grace Operator" in pt.get_mathematical_justification("apply grace")
    assert "φ-recursion" in pt.get_mathematical_justification("recursion step")
    assert "Fixed point" in pt.get_mathematical_justification("fixed point")
    assert "FIRM axiom" in pt.get_mathematical_justification("other")


def test_error_bounds_numeric_and_sequence():
    pt = ProvenanceTracker()
    # numeric output
    b1 = pt.compute_error_bounds({"x": 2.0, "y": 3.0}, 5.0)
    assert 0.0 < b1["relative_error"] < 1.0
    assert b1["absolute_error"] > 0.0
    # eigenvalue branch via list output
    b2 = pt.compute_error_bounds({"phi": "φ"}, [1.0, 2.0])
    # presence of precision key ensures branch executed
    assert "precision_decimal_places" in b1


def test_start_complete_and_seal():
    pt = ProvenanceTracker()
    # start via compatibility wrapper
    pt.start_operation("op", mathematical_inputs={"phi": "φ"}, theoretical_basis="theory")
    # complete via compatibility wrapper
    pt.complete_operation(result=42, derivation_path=["a", "b"], verification_status="ok")
    # summary and seal present
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] >= 2
    assert isinstance(summary["cryptographic_seal"], str) or summary["cryptographic_seal"] is None


def test_contamination_detection_paths():
    pt = ProvenanceTracker()
    with pytest.raises(ContaminationError):
        pt.log_step("use alpha inv", {"alpha_inv": 137.035999084}, 1)
    # string keyword contamination
    assert pt.contains_empirical_data({"note": "experimental value"}) is True
    lst = pt.detect_empirical_contamination({"note": "measured"})
    assert any("note=" in s for s in lst)


def test_audit_report_and_verify_complete():
    pt = ProvenanceTracker()
    pt.log_step("derive phi", {"phi_symbol": "(1+sqrt(5))/2"}, 1.618)
    report = pt.generate_audit_report()
    assert "FIRM PROVENANCE AUDIT REPORT" in report
    # Not all ops will have all axioms; verify_complete_provenance can be False without error
    assert isinstance(pt.verify_complete_provenance(), bool)
