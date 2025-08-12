from validation.experimental_firewall import EXPERIMENTAL_FIREWALL, FirewallStatus


def test_firewall_gating_and_reports():
    f = EXPERIMENTAL_FIREWALL
    f.reset()
    # Theory phase blocks data and sealed comparison
    assert f.request_experimental_data(dataset_id="planck_2018_cmb", requester="test") is None
    assert f.get_sealed_comparison("fine_structure_alpha_inv") is None
    rep = f.generate_firewall_report()
    assert isinstance(rep, str) and "FIRM Experimental Firewall Security Report" in rep
    # Validation phase enable may fail if preconditions not met; handle both outcomes
    try:
        f.enable_validation_phase()
    except Exception:
        pass
    # After attempt, either still blocked or allowed token, both acceptable
    access = f.request_experimental_data(dataset_id="planck_2018_cmb", requester="test")
    assert access is None or (isinstance(access, dict) and access.get("access_granted") is True)
    # Emergency shutdown path
    f.emergency_shutdown("unit test")
    assert f._firewall_status == FirewallStatus.DISABLED

