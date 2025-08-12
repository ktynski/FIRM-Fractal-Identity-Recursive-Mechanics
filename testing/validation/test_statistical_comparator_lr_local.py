from validation.statistical_comparator import STATISTICAL_COMPARATOR


def test_likelihood_ratio_basic():
    firm = {"obs": 1.0}
    null = {}
    data = {"obs": (1.2, 0.3)}
    res = STATISTICAL_COMPARATOR.perform_likelihood_ratio_test(firm, null, data)
    assert res.test_statistic >= 0.0 and res.degrees_of_freedom == 1

