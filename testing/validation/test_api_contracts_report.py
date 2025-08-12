from validation.api_contracts import run_api_contracts


def test_api_contracts_returns_structured_report():
    report = run_api_contracts()
    assert isinstance(report, dict)
    assert "violations" in report and "total_violations" in report and "by_category" in report
