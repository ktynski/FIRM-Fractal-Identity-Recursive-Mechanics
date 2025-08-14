def test_validation_init_expected_boolean_flags():
    from validation import validate_all_firm_predictions
    r = validate_all_firm_predictions()
    # Ensure key booleans exist regardless of values
    for key in [
        "fixed_point_objects_nonempty",
        "comparator_global_metrics_finite",
        "gauge_groups_enumerated",
        "expected_gauge_groups_present",
        "fixed_point_count_minimum",
    ]:
        assert key in r
