from validation.api_contracts import run_api_contracts


def test_api_contracts_run():
    report = run_api_contracts()
    assert "status" in report and report["status"] in ("passed", "failed")
    assert "violations" in report and isinstance(report["violations"], dict)
