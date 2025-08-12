from provenance.provenance_tracker import ProvenanceTracker, OperationType


def test_classify_justify_and_extract_axioms():
    pt = ProvenanceTracker()
    # Classification coverage
    assert pt.classify_operation("apply axiom A𝒢.1") == OperationType.AXIOM_APPLICATION
    assert pt.classify_operation("use theorem lemma") == OperationType.THEOREM_USE
    assert pt.classify_operation("φ recursion") == OperationType.RECURSION
    assert pt.classify_operation("fixed point iteration") == OperationType.FIXED_POINT
    assert pt.classify_operation("validation compare") == OperationType.VALIDATION
    assert pt.classify_operation("derive foo") == OperationType.DERIVATION
    assert pt.classify_operation("compute") == OperationType.COMPUTATION

    # Justification mapping
    j1 = pt.get_mathematical_justification("phi structure")
    j2 = pt.get_mathematical_justification("grace operator")
    j3 = pt.get_mathematical_justification("recursion path")
    j4 = pt.get_mathematical_justification("fixed point")
    j5 = pt.get_mathematical_justification("misc")
    assert all(isinstance(x, str) and len(x) > 0 for x in (j1, j2, j3, j4, j5))

    # Axiom extraction
    deps = pt.extract_axiom_dependencies("totality reflexive grace fixed point consciousness")
    assert set(deps).issuperset({"A𝒢.1", "A𝒢.2", "A𝒢.3", "A𝒢.4", "AΨ.1"})


def test_compute_error_bounds_variants():
    pt = ProvenanceTracker()
    # Numeric output case
    b1 = pt.compute_error_bounds({"a": 10.0, "b": 5.0}, 2.0)
    assert set(["relative_error", "absolute_error"]).issubset(b1.keys())
    # List/tuple output triggers eigenvalue path
    b2 = pt.compute_error_bounds({"phi": 1.618, "n": 3}, (1.0, 2.0))
    assert set(["relative_error", "absolute_error"]).issubset(b2.keys())
