from foundation.operators.phi_recursion import PhiRecursion, ConvergenceStatus


def test_phi_recursion_converges_and_proof():
    pr = PhiRecursion(precision=8)
    steps = list(pr.iterate_recursion(initial_value=1.0, max_iterations=200))
    assert steps[-1].status in (ConvergenceStatus.CONVERGED, ConvergenceStatus.CONVERGING)
    res = pr.prove_convergence()
    assert res.convergence_verified is True
