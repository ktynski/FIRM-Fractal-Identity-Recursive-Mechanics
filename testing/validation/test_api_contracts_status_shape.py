def test_api_contracts_status_and_shape():
    from validation.api_contracts import run_api_contracts
    report = run_api_contracts()
    assert set(report.keys()) == {"violations", "total_violations", "by_category", "status"}
    assert isinstance(report["violations"], dict)
    assert isinstance(report["by_category"], dict)
    assert report["status"] in ("passed", "failed")
    assert report["total_violations"] >= 0

