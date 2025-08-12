from validation import validate_all_firm_predictions


def test_validate_all_firm_predictions_smoke():
    results = validate_all_firm_predictions()
    assert isinstance(results, dict)
    # Check presence of some known keys that the aggregator populates
    assert "comparator_enabled" in results
    assert "phi_recursion_convergence" in results
    assert "banach_conditions" in results
