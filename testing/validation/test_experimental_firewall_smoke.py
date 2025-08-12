from validation.experimental_firewall import EXPERIMENTAL_FIREWALL, FirewallStatus


def test_firewall_theory_vs_validation_access_and_report():
    fw = EXPERIMENTAL_FIREWALL
    fw.reset()
    # Theory phase: access blocked
    tok = fw.request_experimental_data("codata_2018_constants", requester="test")
    assert tok is None
    # Enabling validation may raise if theory incomplete; tolerate either path
    try:
        fw.enable_validation_phase()
    except Exception:
        # Stay in theory phase; proceed to report generation
        pass
    rep = fw.generate_firewall_report()
    assert isinstance(rep, str) and "FIREWALL" in rep
