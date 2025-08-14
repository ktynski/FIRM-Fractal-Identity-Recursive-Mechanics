import math
from foundation.operators.unified_stability_criterion import USC_FRAMEWORK


def test_phi_hermitian_across_window_and_threshold():
    for n in (100, 113, 128):
        assert USC_FRAMEWORK.verify_phi_hermitian(n)
    phi = (1 + math.sqrt(5)) / 2
    assert abs(USC_FRAMEWORK.stability_threshold - phi ** (-9)) < 1e-12
