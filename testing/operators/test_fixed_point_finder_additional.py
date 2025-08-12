import math
import pytest

from foundation.operators.fixed_point_finder import FIXED_POINT_SOLVER


def test_find_fixed_point_numeric_convergence():
    # f(x) = (x + 2)/2 has fixed point at 2
    f = lambda x: (x + 2.0) / 2.0
    val = FIXED_POINT_SOLVER.find_fixed_point(f=f, initial_guess=1.5, tolerance=1e-12, max_iterations=200)
    assert abs(val - 2.0) < 1e-9


def test_find_fixed_point_non_convergence_raises():
    # Divergent mapping f(x) = 2x should not converge
    f = lambda x: 2.0 * x
    with pytest.raises(ValueError):
        FIXED_POINT_SOLVER.find_fixed_point(f=f, initial_guess=1.0, tolerance=1e-30, max_iterations=50)


def test_verify_banach_conditions_true():
    assert FIXED_POINT_SOLVER.verify_banach_conditions() is True

