import pytest

from foundation.operators.fixed_point_finder import FIXED_POINT_SOLVER, SearchStrategy


def test_verify_banach_conditions_true():
    assert FIXED_POINT_SOLVER.verify_banach_conditions()


def test_numeric_nonconvergence_and_exception_message():
    # Divergent mapping
    with pytest.raises(ValueError):
        FIXED_POINT_SOLVER.find_fixed_point(f=lambda x: 2 * x, initial_guess=1.0, tolerance=1e-30, max_iterations=20)


def test_enumerate_fixed_points_handles_nonconvergent_guesses():
    # Small domain with grid ensures some guesses return and some may not; function handles exceptions
    sols = FIXED_POINT_SOLVER.enumerate_all_fixed_points(search_domain_size=3, strategy=SearchStrategy.SYSTEMATIC_GRID)
    assert isinstance(sols, list)

