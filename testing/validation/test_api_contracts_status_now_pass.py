def test_api_contracts_status_field_is_string():
    from validation.api_contracts import run_api_contracts
    report = run_api_contracts()
    assert report["status"] in ("passed", "failed")
    assert isinstance(report["by_category"], dict)

