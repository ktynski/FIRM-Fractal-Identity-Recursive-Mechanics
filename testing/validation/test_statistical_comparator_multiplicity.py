import numpy as np
from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_multiple_comparisons_adjusted_summaries_present():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    # Craft synthetic results with p-values spanning range
    results = [
        StatisticalResult(
            test_name=f"t{i}", theoretical_value=0.0, experimental_value=0.0,
            experimental_uncertainty=1.0, test_statistic=0.0, p_value=p,
            confidence_interval=(0.0, 1.0), statistical_significance=0.0,
            degrees_of_freedom=1, test_type=StatisticalTest.CHI_SQUARED,
            hypothesis_type=HypothesisType.TWO_SIDED
        )
        for i, p in enumerate([0.001, 0.02, 0.049, 0.2, 0.8], start=1)
    ]
    ga = comp._perform_global_analysis(results)
    # Ensure adjusted outputs present
    assert "holm_adjusted" in ga and "bh_adjusted" in ga
    assert len(ga["holm_adjusted"]) == len(results)
    assert len(ga["bh_adjusted"]) == len(results)
