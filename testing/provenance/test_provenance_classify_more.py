def test_classify_operation_additional_strings():
    from provenance.provenance_tracker import ProvenanceTracker, OperationType
    t = ProvenanceTracker()
    assert t.classify_operation("lemma application").name == OperationType.THEOREM_USE.name
    assert t.classify_operation("φ recursion identity").name in (OperationType.RECURSION.name, OperationType.DERIVATION.name)
    assert t.classify_operation("fixed POINT iteration").name == OperationType.FIXED_POINT.name
    assert t.classify_operation("validation compare stats").name == OperationType.VALIDATION.name
    assert t.classify_operation("derive alpha").name == OperationType.DERIVATION.name
