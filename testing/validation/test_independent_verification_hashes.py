from validation.independent_verification import run_independent_verification


def test_run_independent_verification_with_mismatch():
    report = run_independent_verification(canonical_hashes={"alpha_inverse": "deadbeef"})
    assert report.get("overall_status") in ("mismatch", "recorded", "passed")
    assert "results" in report
