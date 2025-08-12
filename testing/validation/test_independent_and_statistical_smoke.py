from validation.independent_verification import run_independent_verification
from validation.statistical_comparator import StatisticalComparator


def test_independent_verification_runs():
    report = run_independent_verification()
    assert isinstance(report, dict)
    assert report.get("overall_status") in ("recorded", "passed", "mismatch")
    assert "results" in report and isinstance(report["results"], dict)


def test_statistical_comparator_enable_and_report():
    sc = StatisticalComparator()
    sc.enable_validation_mode()
    # Minimal Bayesian comparison using synthetic values (no empirical data)
    res = sc.perform_bayesian_comparison(theoretical=1.0, experimental=1.0, uncertainty=0.1, test_name="synthetic")
    assert res.test_type.name == "BAYESIAN_FACTOR"
    # Generate a small report from provided results
    txt = sc.generate_statistical_report([res])
    assert isinstance(txt, str) and "Statistical Validation Report" in txt
