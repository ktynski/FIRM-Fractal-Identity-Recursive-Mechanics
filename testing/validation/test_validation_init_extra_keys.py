def test_validate_all_firm_predictions_keyset():
    from validation import validate_all_firm_predictions
    res = validate_all_firm_predictions()
    # Expect several standard keys present even if values vary
    expected = [
        "comparator_enabled",
        "analysis_nonempty",
        "phi_value_range",
        "precision_framework_operational",
        "provenance_acyclicity_proxy",
        "grace_operator_contraction",
    ]
    for k in expected:
        assert k in res
