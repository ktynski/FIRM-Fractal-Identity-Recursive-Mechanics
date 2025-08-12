from foundation.operators.phi_recursion import PhiRecursion, ConvergenceStatus


def test_iterate_and_prove_convergence_edges():
    pr = PhiRecursion(precision=10)
    # iterate from a small positive value
    steps = list(pr.iterate_recursion(initial_value=0.5, max_iterations=100))
    assert steps[-1].status in (ConvergenceStatus.CONVERGING, ConvergenceStatus.CONVERGED)
    # prove convergence API returns coherent result
    res = pr.prove_convergence(initial_value=1.0)
    assert isinstance(res.final_phi_value, float)
    assert res.convergence_steps >= 1
    assert res.theoretical_phi == pr.theoretical_phi

