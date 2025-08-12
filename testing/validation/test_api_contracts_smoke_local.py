from validation.api_contracts import run_api_contracts


def test_api_contracts_runs_and_reports_shape():
    result = run_api_contracts()
    assert "violations" in result and isinstance(result["violations"], dict)
    assert "total_violations" in result and isinstance(result["total_violations"], int)
    assert "status" in result and result["status"] in ("passed", "failed")
