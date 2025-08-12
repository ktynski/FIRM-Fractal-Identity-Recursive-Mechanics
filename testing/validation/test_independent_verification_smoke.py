from validation.independent_verification import run_independent_verification


def test_independent_verification_report_structure():
    report = run_independent_verification()
    assert isinstance(report, dict)
    assert "environment" in report and "results" in report and "overall_status" in report
    env = report["environment"]
    assert isinstance(env, dict) and "python_version" in env and "timestamp_utc" in env
