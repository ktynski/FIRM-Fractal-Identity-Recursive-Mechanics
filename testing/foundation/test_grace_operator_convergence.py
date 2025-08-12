from foundation.operators.grace_operator import GRACE_OPERATOR, ConvergenceStatus


class Dummy:
    def __init__(self, v: float) -> None:
        self.v = v

    def distance_to(self, other: "Dummy") -> float:
        return abs(self.v - other.v)


def test_grace_operator_contraction_numeric_and_structure():
    # Numeric path
    x = 10.0
    y = GRACE_OPERATOR.apply(x)
    assert isinstance(y, float)

    # Structure path with attribute v
    d0 = Dummy(10.0)
    d1 = GRACE_OPERATOR.apply(d0)
    assert isinstance(d1, Dummy)
    assert d1.v != 10.0


def test_fixed_point_iteration_converges():
    d = Dummy(1.0)
    # Iterate a few steps and ensure we eventually mark converging/converged
    it = GRACE_OPERATOR.compute_fixed_points(d, max_iterations=10)
    last = None
    for res in it:
        last = res
    assert last is not None
    assert last.status in {ConvergenceStatus.CONVERGED, ConvergenceStatus.CONVERGING}
