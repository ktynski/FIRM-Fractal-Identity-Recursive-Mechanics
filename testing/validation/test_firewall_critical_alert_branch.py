def test_firewall_report_critical_alert(monkeypatch):
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW
    # Force validation phase
    FW.reset()
    monkeypatch.setattr(FW, "_theory_phase_active", False, raising=False)
    monkeypatch.setattr(FW, "_validation_phase_active", True, raising=False)
    # Inject a dataset with bad seal to trigger critical alert on access
    class BadSeal:
        description = "bad"
        def verify_seal_integrity(self): return False
    FW._sealed_datasets = {"bad": BadSeal()}
    # Request to trigger alert
    _ = FW.request_experimental_data("bad", "tester")
    rep = FW.generate_firewall_report()
    assert "CRITICAL" in rep or "BREACHED" in rep

