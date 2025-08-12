from validation.independent_verification import run_independent_verification


def test_independent_verification_report_shape():
    report = run_independent_verification()
    assert "environment" in report and isinstance(report["environment"], dict)
    assert "results" in report and isinstance(report["results"], dict)
    assert "overall_status" in report
    # hashes present for each quantity
    for key in ("alpha_inverse", "mass_spectrum", "ex_nihilo_pipeline"):
        assert key in report["results"]
        assert "hash" in report["results"][key]
