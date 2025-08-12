from foundation.operators.unified_stability_criterion import USC_FRAMEWORK


def test_usc_phi_hermitian_and_threshold_derivation():
    # Check Hermiticity for representative n and threshold positivity/order
    assert USC_FRAMEWORK.verify_phi_hermitian(10)
    thr = USC_FRAMEWORK.stability_threshold
    # φ^-9 in (0,1)
    assert 0.0 < thr < 1.0


def test_usc_find_optimal_n_local_window():
    n_opt = USC_FRAMEWORK.find_optimal_stability_n()
    # Must return an int in analyzed window
    assert isinstance(n_opt, int) and 100 <= n_opt <= 129

