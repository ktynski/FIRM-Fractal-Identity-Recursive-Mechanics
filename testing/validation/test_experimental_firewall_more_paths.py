def test_firewall_request_data_success_path(monkeypatch):
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW
    FW.reset()
    # Force validation phase active for success path
    monkeypatch.setattr(FW, "_theory_phase_active", False, raising=False)
    monkeypatch.setattr(FW, "_validation_phase_active", True, raising=False)
    res = FW.request_experimental_data("codata_2018_constants", "tester")
    assert isinstance(res, dict) and res.get("access_granted") is True

def test_firewall_verify_contamination_free_derivation_true_false():
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW
    FW.reset()
    assert FW.verify_contamination_free_derivation(["pure math", "axiom step"]) is True
    # Include empirical marker to force False
    bad = ["use codata_2018_constants entry"]
    assert FW.verify_contamination_free_derivation(bad) is False
