from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_generate_statistical_report_zero_results_path():
    sc = StatisticalComparator()
    sc.enable_validation_mode()
    # Force no stored results
    report = sc.generate_statistical_report(results_override=[])
    assert "FIRM Statistical Validation Report" in report
    assert "No statistical tests available" in report


def test_summarize_results_small_list():
    sc = StatisticalComparator()
    res = [
        StatisticalResult(
            test_name="r1", theoretical_value=0.0, experimental_value=0.0, experimental_uncertainty=1.0,
            test_statistic=0.0, p_value=0.5, confidence_interval=(0.0, 1.0), statistical_significance=0.0,
            degrees_of_freedom=1, test_type=StatisticalTest.CHI_SQUARED, hypothesis_type=HypothesisType.TWO_SIDED
        )
    ]
    summary = sc._summarize_results(res)
    assert "num_results" in summary and summary["num_results"] == 1
