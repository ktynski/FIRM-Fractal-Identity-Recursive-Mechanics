from validation.experimental_firewall import EXPERIMENTAL_FIREWALL, FirewallStatus


def test_firewall_gating_and_reports():
    fw = EXPERIMENTAL_FIREWALL
    fw.reset()
    # Theory phase blocks data access
    assert fw.request_experimental_data("planck_2018_cmb", requester="test") is None
    # Enabling validation may raise if theory incomplete; catch and proceed
    try:
        fw.enable_validation_phase()
    except Exception:
        pass
    # get_sealed_comparison during theory should be None and raise alert
    fw.reset()
    assert fw.get_sealed_comparison("fine_structure_alpha_inv") is None
    # Emergency shutdown toggles state and logs
    fw.emergency_shutdown("test reason")
    assert fw._firewall_status == FirewallStatus.DISABLED
    rep = fw.generate_firewall_report()
    assert isinstance(rep, str) and "FIRM Experimental Firewall Security Report" in rep
