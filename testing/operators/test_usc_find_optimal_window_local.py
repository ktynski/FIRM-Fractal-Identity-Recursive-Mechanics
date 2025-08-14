from foundation.operators.unified_stability_criterion import USC_FRAMEWORK


def test_usc_find_optimal_in_expected_window():
    n_opt = USC_FRAMEWORK.find_optimal_stability_n()
    assert 100 <= n_opt <= 129
