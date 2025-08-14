from validation.statistical_comparator import StatisticalComparator, StatisticalTest


def test_likelihood_ratio_nonnegative_and_types():
    sc = StatisticalComparator()
    sc.enable_validation_mode()
    data = {"x": (1.0, 0.2), "y": (2.0, 0.3)}
    firm = {"x": 1.1, "y": 1.9}
    null = {"x": 1.0, "y": 2.0}
    res = sc.perform_likelihood_ratio_test(firm, null, data)
    assert res.test_type is StatisticalTest.LIKELIHOOD_RATIO
    assert res.test_statistic >= 0.0
