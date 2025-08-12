from foundation.operators.grace_operator import GRACE_OPERATOR, ConvergenceStatus


class Dummy:
    def __init__(self, v: float):
        self.v = v
    def shannon_entropy(self) -> float:
        return abs(self.v)
    def distance_to(self, other: "Dummy") -> float:
        return abs(self.v - other.v)
    def compose_with(self, morphism):
        return self


def test_grace_operator_basic_properties_and_convergence():
    # Contraction property on dummy structures
    assert GRACE_OPERATOR.verify_contraction_property(Dummy(1.0), Dummy(0.0)) is True
    # Entropy minimization
    assert GRACE_OPERATOR.verify_entropy_minimization(Dummy(2.0)) is True
    # Fixed point iterator yields converging status and eventually converged
    it = GRACE_OPERATOR.compute_fixed_points(Dummy(1.0), max_iterations=50)
    last = None
    for last in it:
        pass
    assert last is not None and last.status in (ConvergenceStatus.CONVERGED, ConvergenceStatus.CONVERGING)
    # φ emergence accessor
    assert GRACE_OPERATOR.derive_phi_emergence() > 1.0
