import validation


def test_validate_all_firm_predictions_meta_flags(monkeypatch):
    res = validation.validate_all_firm_predictions()
    # Meta items should exist with validation_status field
    for key in (
        "firewall_active",
        "sealed_datasets_intact",
        "comparator_enabled",
        "analysis_nonempty",
        "precision_framework_operational",
        "phi_recursion_convergence",
        "grace_operator_contraction",
    ):
        assert key in res and hasattr(res[key], "validation_status")

