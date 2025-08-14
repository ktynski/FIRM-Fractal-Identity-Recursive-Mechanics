import numpy as np

from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_global_analysis_and_report_paths():
    comp = StatisticalComparator()
    comp.enable_validation_mode()

    # Build two results (one chi-squared, one Bayesian) to drive global paths
    r1 = comp.perform_chi_squared_test(theoretical=1.0, experimental=1.1, uncertainty=0.2, test_name="t1")
    r2 = comp.perform_bayesian_comparison(theoretical=2.0, experimental=1.9, uncertainty=0.3, test_name="t2")

    ga = comp._perform_global_analysis([r1, r2])
    assert "global_chi_squared" in ga and "global_p_value" in ga
    assert "global_bayes_factor" in ga

    # Generate report (exercises lazy analysis path too)
    report = comp.generate_statistical_report()
    assert "FIRM Statistical Validation Report" in report
