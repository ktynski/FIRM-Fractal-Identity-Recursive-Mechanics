from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_generate_report_with_override_and_exception_fallback(monkeypatch):
    comp = StatisticalComparator()
    comp.enable_validation_mode()

    # Force comprehensive_validation_analysis to raise to take exception branch
    def boom():
        raise RuntimeError("boom")

    monkeypatch.setattr(comp, "comprehensive_validation_analysis", boom, raising=True)

    # Provide an override list with two results to exercise BH/Holm summaries
    r1 = StatisticalResult(
        test_name="a_chi_squared", theoretical_value=1.0, experimental_value=1.0,
        experimental_uncertainty=1.0, test_statistic=0.0, p_value=1.0,
        confidence_interval=(0.0, 1.0), statistical_significance=0.0,
        degrees_of_freedom=1, test_type=StatisticalTest.CHI_SQUARED,
        hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=1.0,
    )
    r2 = StatisticalResult(
        test_name="b_likelihood", theoretical_value=0.0, experimental_value=1.0,
        experimental_uncertainty=1.0, test_statistic=0.0, p_value=0.2,
        confidence_interval=(0.0, 1.0), statistical_significance=1.0,
        degrees_of_freedom=1, test_type=StatisticalTest.LIKELIHOOD_RATIO,
        hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=0.0,  # triggers non-positive guard in evidence_strength
    )

    rep = comp.generate_statistical_report(results_override=[r1, r2])
    assert "GLOBAL ANALYSIS:" in rep
    # evidence strings should be computable without errors
    assert "strong_against" in rep or "decisive" in rep or "substantial" in rep
