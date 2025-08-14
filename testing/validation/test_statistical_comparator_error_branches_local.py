from validation.statistical_comparator import STATISTICAL_COMPARATOR


def test_comparator_handles_empty_inputs_and_reports():
    # Exercise safe branches returning dicts without raising
    res = STATISTICAL_COMPARATOR.comprehensive_validation_analysis()
    assert isinstance(res, dict)
    # Global analysis gracefully handles empty results
    ga = STATISTICAL_COMPARATOR._perform_global_analysis([])
    assert isinstance(ga, dict) and "error" in ga
