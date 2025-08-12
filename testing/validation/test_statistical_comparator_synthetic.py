import numpy as np

from validation.statistical_comparator import StatisticalComparator, StatisticalTest


def test_chi_squared_and_bayes_paths_synthetic():
    sc = StatisticalComparator()
    sc.enable_validation_mode()
    # Simple chi-squared with equal values -> zero chi2
    res = sc.perform_chi_squared_test(theoretical=1.0, experimental=1.0, uncertainty=0.1, test_name="t")
    assert res.test_type is StatisticalTest.CHI_SQUARED
    # Bayesian helper paths via internal API
    bf = sc._bayesian.compute_bayes_factor(likelihood_firm=0.8, likelihood_null=0.4)
    post = sc._bayesian.posterior_probability(bf)
    ci = sc._bayesian.credible_interval(np.array([0.1, 0.2, 0.3]))
    assert bf > 0 and 0 <= post <= 1 and isinstance(ci, tuple)

