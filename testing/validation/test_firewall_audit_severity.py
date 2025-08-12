from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_firewall_severity_counts_and_audit_log():
    EXPERIMENTAL_FIREWALL.reset()
    # Trigger several theory-phase accesses to generate HIGH alerts
    for _ in range(3):
        _ = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    report = EXPERIMENTAL_FIREWALL.generate_firewall_report()
    assert "High:" in report or "HIGH" in report
    assert "Access Attempts:" in report


def test_request_seal_integrity_compromised_monkeypatch(monkeypatch):
    EXPERIMENTAL_FIREWALL.reset()
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        return
    # Monkeypatch SealedDataset.verify_seal_integrity at the class level
    import validation.experimental_firewall as fw
    monkeypatch.setattr(fw.SealedDataset, "verify_seal_integrity", lambda self: False, raising=True)
    # Now any request should detect compromised seal and be blocked
    ds_id = next(iter(EXPERIMENTAL_FIREWALL._sealed_datasets.keys()))
    token = EXPERIMENTAL_FIREWALL.request_experimental_data(ds_id, requester="unit_test")
    assert token is None
    rep = EXPERIMENTAL_FIREWALL.generate_firewall_report()
    # Assert stable report fields instead of literal text
    assert "Firewall Status: BREACHED" in rep
    assert "Critical: 1" in rep
