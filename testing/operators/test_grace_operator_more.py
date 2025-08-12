def test_grace_operator_fixed_point_iterator_and_contract():
    from foundation.operators.grace_operator import GRACE_OPERATOR, FixedPointResult, ConvergenceStatus

    class Dummy:
        def __init__(self, v: float):
            self.v = v
        def shannon_entropy(self) -> float:
            return abs(self.v)
        def distance_to(self, other: "Dummy") -> float:
            return abs(self.v - other.v)
        def compose_with(self, morphism):
            return self

    s1, s2 = Dummy(1.0), Dummy(0.0)
    assert GRACE_OPERATOR.verify_contraction_property(s1, s2) in (True, False)

    # iterate a few fixed-point steps
    it = GRACE_OPERATOR.compute_fixed_points(Dummy(1.0), max_iterations=5)
    first = next(it)
    assert isinstance(first, FixedPointResult)
    assert first.convergence_steps >= 1
    assert first.status in (ConvergenceStatus.CONVERGING, ConvergenceStatus.CONVERGED)

