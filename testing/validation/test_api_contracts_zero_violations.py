from validation.api_contracts import run_api_contracts


def test_api_contracts_zero_or_reported_violations_shape():
    report = run_api_contracts()
    assert "violations" in report and isinstance(report["violations"], dict)
    assert "status" in report and report["status"] in ("passed", "failed")
    # Ensure each category lists violations as a list
    for lst in report["violations"].values():
        assert isinstance(lst, list)
