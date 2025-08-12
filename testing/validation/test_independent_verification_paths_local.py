from validation.independent_verification import run_independent_verification


def test_independent_verification_runs_and_reports():
    rep = run_independent_verification()
    assert isinstance(rep, dict) and "overall_status" in rep and "results" in rep

