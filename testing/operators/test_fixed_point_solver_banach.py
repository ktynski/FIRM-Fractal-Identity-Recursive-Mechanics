from foundation.operators.fixed_point_finder import FIXED_POINT_SOLVER


def test_banach_conditions_true():
    assert FIXED_POINT_SOLVER.verify_banach_conditions() is True
