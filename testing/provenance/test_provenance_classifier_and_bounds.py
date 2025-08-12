def test_classifier_justification_dependencies_and_bounds():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    # Classify different operation strings
    assert t.classify_operation("axiom_application:A𝒢.1").name == "AXIOM_APPLICATION"
    assert t.classify_operation("theorem:lemma").name == "THEOREM_USE"
    assert t.classify_operation("phi recursion step").name in ("RECURSION", "DERIVATION")
    assert t.classify_operation("fixed point compute").name == "FIXED_POINT"
    assert t.classify_operation("validation compare").name == "VALIDATION"
    assert t.classify_operation("derive something").name == "DERIVATION"
    assert t.classify_operation("compute").name == "COMPUTATION"

    # Justifications
    assert isinstance(t.get_mathematical_justification("phi power"), str)
    assert isinstance(t.get_mathematical_justification("grace op"), str)
    assert isinstance(t.get_mathematical_justification("fixed point"), str)

    # Dependencies extraction
    deps = t.extract_axiom_dependencies("totality reflexive grace fixed point consciousness")
    assert set(deps) >= {"A𝒢.1", "A𝒢.2", "A𝒢.3", "A𝒢.4", "AΨ.1"}

    # Error bounds numeric
    b_num = t.compute_error_bounds({"a": 2.0}, 3.0)
    assert set(b_num.keys()) >= {"relative_error", "absolute_error"}
    # Error bounds sequence
    b_seq = t.compute_error_bounds({"a": 1.0}, [1.0, 2.0])
    assert set(b_seq.keys()) >= {"relative_error", "absolute_error"}

    # log_verification path
    t.log_verification("unit", theoretical=1.0, observed=1.0, error=0.0, verified=True)
    assert len(t.derivation_chain) >= 1

