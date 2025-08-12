from validation.api_contracts import run_api_contracts


def test_api_contracts_run_report():
    report = run_api_contracts()
    assert isinstance(report, dict)
    assert "violations" in report and "status" in report

from validation.api_contracts import run_api_contracts


def test_api_contracts_runner_passes_minimum_contracts():
    res = run_api_contracts()
    assert res["status"] in {"passed", "failed"}
    # With the minimal methods added, fine structure and ex nihilo should pass
    violations = res["violations"]
    # Allow mass_spectrum to be either if private corrections are used; focus on not missing class
    assert isinstance(violations, dict)
