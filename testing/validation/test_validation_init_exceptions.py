def test_validation_init_precision_and_iv_exceptions(monkeypatch):
    import validation
    import validation.independent_verification as iv
    import utils.precision_framework as pf

    # Force compute_with_precision to raise to enter exception path
    def boom(*a, **k):
        raise RuntimeError("boom")
    monkeypatch.setattr(pf.PRECISION_FRAMEWORK, "compute_with_precision", boom, raising=True)

    # Patch run_independent_verification to raise
    def boom_iv():
        raise RuntimeError("iv")
    monkeypatch.setattr(iv, "run_independent_verification", boom_iv, raising=True)

    res = validation.validate_all_firm_predictions()
    assert isinstance(res, dict)
    assert "precision_framework_operational" in res

def test_validation_init_sealed_count_zero(monkeypatch):
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW
    from validation import validate_all_firm_predictions
    FW.reset()
    # Empty sealed datasets
    monkeypatch.setattr(FW, "_sealed_datasets", {}, raising=False)
    r = validate_all_firm_predictions()
    assert "firewall_sealed_count_nonzero" in r
