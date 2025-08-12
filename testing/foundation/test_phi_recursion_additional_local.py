import math
from pytest import approx
from foundation.operators.phi_recursion import PHI_RECURSION, ConvergenceStatus


def test_phi_recursion_basic_paths_and_powers():
    # recursion function and convergence iteration
    assert abs(PHI_RECURSION.recursion_function(1.0) - 2.0) < 1e-12
    steps = list(PHI_RECURSION.iterate_recursion(1.0, max_iterations=50))
    assert len(steps) >= 1 and steps[-1].status in {ConvergenceStatus.CONVERGED, ConvergenceStatus.CONVERGING}
    # iterative compute
    val = PHI_RECURSION.compute_phi_iterative(precision=1e-10, max_iterations=200)
    assert abs(val - PHI_RECURSION.theoretical_phi) < 1e-9
    # power via precompute/LRU/exp path
    assert PHI_RECURSION.compute_phi_power(2) == approx((PHI_RECURSION.theoretical_phi ** 2), rel=1e-12)
    big = PHI_RECURSION.compute_phi_power(100)
    assert math.isfinite(big)

