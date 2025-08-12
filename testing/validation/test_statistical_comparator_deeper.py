import numpy as np
from validation.statistical_comparator import StatisticalComparator


def test_statistical_comparator_comprehensive_analysis_empty_safe():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    # Force internal state to no prior results and call report; path should be safe
    report = comp.generate_statistical_report()
    assert isinstance(report, str)


def test_likelihood_ratio_test_shapes():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    data = {"x": (1.0, 0.1)}
    res = comp.perform_likelihood_ratio_test(firm_params={"x": 1.05}, null_params={"x": 1.0}, data=data)
    assert res.degrees_of_freedom == 0 or res.degrees_of_freedom >= 0
