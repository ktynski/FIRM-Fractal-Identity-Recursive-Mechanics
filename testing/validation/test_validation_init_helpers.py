def test_validate_all_firm_predictions_shape():
    from validation import validate_all_firm_predictions
    results = validate_all_firm_predictions()
    assert isinstance(results, dict)
    # Expect some keys to exist from meta-validations
    assert "comparator_enabled" in results
    assert hasattr(results["comparator_enabled"], "validation_status")

def test_validation_cli_main_runs(monkeypatch):
    import validation
    # Intercept sys.exit
    import sys
    called = {"code": None}
    def fake_exit(code):
        called["code"] = code
    monkeypatch.setattr(sys, "exit", fake_exit, raising=False)
    validation.main()
    assert called["code"] in (0, 1)
