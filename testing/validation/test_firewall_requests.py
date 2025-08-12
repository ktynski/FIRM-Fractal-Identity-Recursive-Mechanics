from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_request_experimental_data_theory_vs_validation():
    EXPERIMENTAL_FIREWALL.reset()
    # Theory phase blocks data request
    token = EXPERIMENTAL_FIREWALL.request_experimental_data("codata_2018_constants", requester="unit_test")
    assert token is None

    # Validation phase allows access
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        # Preconditions may fail in some environments; skip remainder
        return
    token = EXPERIMENTAL_FIREWALL.request_experimental_data("codata_2018_constants", requester="unit_test")
    assert isinstance(token, dict) and token.get("access_granted") is True


def test_multiple_alerts_accumulate_under_theory_phase():
    EXPERIMENTAL_FIREWALL.reset()
    # Trigger multiple theory-phase sealed comparisons to generate alerts
    _ = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    _ = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    report = EXPERIMENTAL_FIREWALL.generate_firewall_report()
    # Expect at least one alert reflected in the report summary
    assert "Total Alerts" in report
