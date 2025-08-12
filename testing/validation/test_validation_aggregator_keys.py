from validation import validate_all_firm_predictions


def test_validation_aggregator_core_keys_present():
    res = validate_all_firm_predictions()
    assert isinstance(res, dict)
    # Core keys expected regardless of environment specifics
    for key in (
        "comparator_enabled",
        "analysis_nonempty",
        "phi_recursion_convergence",
        "banach_conditions",
        "grace_operator_contraction",
    ):
        assert key in res
