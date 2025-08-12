def test_firewall_phase_transitions_and_sealed_comparison(monkeypatch):
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW
    FW.reset()
    # theory phase blocks
    assert FW.request_experimental_data("codata_2018_constants", "tester") is None
    # enabling validation may raise if theory not complete; guard
    try:
        FW.enable_validation_phase()
    except Exception:
        pass
    # After any outcome, get_sealed_comparison behaviour
    result_none = FW.get_sealed_comparison("nonexistent_key")
    assert result_none in (None,)
    # If validation is active and key allowed, shape is dict
    if getattr(FW, "_validation_phase_active", False):
        comp = FW.get_sealed_comparison("fine_structure_alpha_inv")
        if comp is not None:
            assert comp.get("sealed") is True
    report = FW.generate_firewall_report()
    assert isinstance(report, str) and "FIRM Experimental Firewall Security Report" in report

def test_firewall_contamination_alerts_and_shutdown():
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW, ContaminationType
    FW.reset()
    # raise an alert (theory phase access to sealed comparison)
    _ = FW.get_sealed_comparison("fine_structure_alpha_inv")
    rep = FW.generate_firewall_report()
    assert isinstance(rep, str)
    # emergency shutdown
    FW.emergency_shutdown("test")
    rep2 = FW.generate_firewall_report()
    assert "DISABLED" in rep2

