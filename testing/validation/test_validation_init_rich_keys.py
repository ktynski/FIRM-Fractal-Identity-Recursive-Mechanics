def test_validation_init_rich_key_presence():
    from validation import validate_all_firm_predictions
    r = validate_all_firm_predictions()
    keys = [
        "independent_verification_report",
        "banach_conditions",
        "spacetime_dimensionality",
        "axiom_system_valid",
        "cmb_outputs_present",
    ]
    for k in keys:
        assert k in r

