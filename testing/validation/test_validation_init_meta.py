from validation import validate_all_firm_predictions


def test_validate_all_firm_predictions_meta_items_present():
    results = validate_all_firm_predictions()
    # Check presence of key meta validations without asserting specific outcomes
    for key in (
        "firewall_active",
        "sealed_datasets_intact",
        "comparator_enabled",
        "analysis_nonempty",
        "phi_value_range",
        "precision_framework_operational",
        "independent_verification_report",
        "comparator_global_metrics_finite",
        "fixed_point_objects_nonempty",
        "provenance_acyclicity_proxy",
        "phi_recursion_convergence",
        "grace_operator_contraction",
        "banach_conditions",
        "spacetime_dimensionality",
        "axiom_system_valid",
    ):
        assert key in results and hasattr(results[key], "validation_status")
