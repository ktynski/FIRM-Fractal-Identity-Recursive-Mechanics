from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_firewall_report_contains_expected_sections():
    EXPERIMENTAL_FIREWALL.reset()
    # Trigger a theory-phase sealed comparison to create an alert
    _ = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    report = EXPERIMENTAL_FIREWALL.generate_firewall_report()
    assert "FIRM Experimental Firewall Security Report" in report
    assert "Firewall Status" in report
    assert "CONTAMINATION MONITORING" in report
    assert "SEALED DATASETS" in report
    assert "AUDIT LOG" in report
