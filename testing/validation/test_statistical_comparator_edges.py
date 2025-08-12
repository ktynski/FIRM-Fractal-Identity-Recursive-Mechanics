import numpy as np
from validation.statistical_comparator import StatisticalComparator, StatisticalTest


def test_generate_report_with_empty_results_path():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    # Force use of override with empty list
    report = comp.generate_statistical_report(results_override=[])
    assert "Statistical analysis error" not in report


def test_likelihood_ratio_dof_zero_path():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    # Same param counts -> dof = 0 -> p_value = 1.0
    firm = {"x": 0.0}
    null = {"x": 0.0}
    data = {"x": (0.0, 1.0)}
    res = comp.perform_likelihood_ratio_test(firm, null, data)
    assert res.test_type == StatisticalTest.LIKELIHOOD_RATIO
    assert res.degrees_of_freedom == 0
    assert res.p_value == 1.0
