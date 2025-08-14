from validation.independent_verification import run_independent_verification


def test_independent_verification_basic_report_shape():
    report = run_independent_verification()
    assert isinstance(report, dict)
    assert "environment" in report and isinstance(report["environment"], dict)
    assert "results" in report and isinstance(report["results"], dict)
    # Ensure alpha and mass keys exist and contain a stable hash
    assert "alpha_inverse" in report["results"]
    assert "mass_spectrum" in report["results"]
    assert "hash" in report["results"]["alpha_inverse"]
    assert "hash" in report["results"]["mass_spectrum"]
