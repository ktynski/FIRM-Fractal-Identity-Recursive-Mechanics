from provenance.provenance_tracker import ProvenanceTracker, OperationType


def test_classify_operation_and_justifications_and_axioms():
    pt = ProvenanceTracker()
    assert pt.classify_operation("apply axiom A𝒢.3") == OperationType.AXIOM_APPLICATION
    assert pt.classify_operation("use theorem lemma") == OperationType.THEOREM_USE
    assert pt.classify_operation("phi recursion") in (OperationType.RECURSION, OperationType.DERIVATION)
    assert pt.classify_operation("fixed point iteration") == OperationType.FIXED_POINT
    assert pt.classify_operation("validation compare") == OperationType.VALIDATION
    assert pt.classify_operation("derive something") == OperationType.DERIVATION
    j = pt.get_mathematical_justification("grace operator application")
    assert "Grace Operator" in j
    deps = pt.extract_axiom_dependencies("totality reflexive grace fixed point consciousness")
    # Should include all referenced axioms
    for ax in ("A𝒢.1", "A𝒢.2", "A𝒢.3", "A𝒢.4", "AΨ.1"):
        assert ax in deps
