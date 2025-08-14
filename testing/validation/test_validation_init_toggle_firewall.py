def test_validation_init_with_firewall_toggle(monkeypatch):
    from validation import validate_all_firm_predictions
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL as FW
    FW.reset()
    # Enable validation phase if possible; ignore errors
    try:
        FW.enable_validation_phase()
    except Exception:
        pass
    r = validate_all_firm_predictions()
    assert isinstance(r, dict)
