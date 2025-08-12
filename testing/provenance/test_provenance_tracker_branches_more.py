from provenance.provenance_tracker import ProvenanceTracker, OperationType


def test_classify_operation_all_branches():
    pt = ProvenanceTracker()
    assert pt.classify_operation("Apply Axiom A𝒢.1") is OperationType.AXIOM_APPLICATION
    assert pt.classify_operation("Use Theorem 1") is OperationType.THEOREM_USE
    assert pt.classify_operation("φ-recursion step") is OperationType.RECURSION
    assert pt.classify_operation("Fixed point calculation") is OperationType.FIXED_POINT
    assert pt.classify_operation("validation compare model") is OperationType.VALIDATION
    assert pt.classify_operation("derive mixing angle") is OperationType.DERIVATION
    assert pt.classify_operation("matrix multiply") is OperationType.COMPUTATION


def test_justification_and_axiom_extraction_branches():
    pt = ProvenanceTracker()
    # justification
    assert "Golden ratio" in pt.get_mathematical_justification("phi power")
    assert "Grace Operator" in pt.get_mathematical_justification("grace contraction")
    assert "φ-recursion" in pt.get_mathematical_justification("recursion kernel")
    assert "Fixed point" in pt.get_mathematical_justification("fixed point map")
    assert "Mathematical operation" in pt.get_mathematical_justification("other op")

    # axiom extraction
    deps = pt.extract_axiom_dependencies("totality reflexive grace fixed point consciousness")
    for ax in ("A𝒢.1", "A𝒢.2", "A𝒢.3", "A𝒢.4", "AΨ.1"):
        assert ax in deps

