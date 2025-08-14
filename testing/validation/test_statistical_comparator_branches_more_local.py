from validation.statistical_comparator import STATISTICAL_COMPARATOR, StatisticalResult, StatisticalTest, HypothesisType


def test_statistical_report_with_override_and_multiple_corrections():
    # Craft two synthetic results to exercise global analysis and report paths
    r1 = StatisticalResult(
        test_name="t1", theoretical_value=1.0, experimental_value=1.0, experimental_uncertainty=1.0,
        test_statistic=0.0, p_value=0.5, confidence_interval=(0.0, 2.0),
        statistical_significance=0.0, degrees_of_freedom=1,
        test_type=StatisticalTest.CHI_SQUARED, hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=1.0,
    )
    r2 = StatisticalResult(
        test_name="t2", theoretical_value=2.0, experimental_value=0.0, experimental_uncertainty=1.0,
        test_statistic=4.0, p_value=0.045, confidence_interval=(0.0, 4.0),
        statistical_significance=2.0, degrees_of_freedom=1,
        test_type=StatisticalTest.CHI_SQUARED, hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=10.0,
    )
    report = STATISTICAL_COMPARATOR.generate_statistical_report(results_override=[r1, r2])
    assert isinstance(report, str) and "FIRM Statistical Validation Report" in report
    # Ensure multiple-comparisons summary present
    assert "Holm adjusted p" in report and "Benjamini–Hochberg" in report
