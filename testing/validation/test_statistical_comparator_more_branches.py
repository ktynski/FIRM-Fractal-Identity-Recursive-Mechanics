from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_report_with_stored_results_path():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    r = StatisticalResult(
        test_name="t0_chi_squared", theoretical_value=0.0, experimental_value=0.0,
        experimental_uncertainty=1.0, test_statistic=0.0, p_value=1.0,
        confidence_interval=(0.0, 1.0), statistical_significance=0.0,
        degrees_of_freedom=1, test_type=StatisticalTest.CHI_SQUARED,
        hypothesis_type=HypothesisType.TWO_SIDED
    )
    # Store results and generate report without override
    comp._statistical_results = [r]
    rep = comp.generate_statistical_report()
    assert "INDIVIDUAL TEST RESULTS" in rep
