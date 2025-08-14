from foundation.operators.fixed_point_finder import BanachFixedPointSolver, SearchStrategy


def test_fixed_point_solver_basic_paths():
    solver = BanachFixedPointSolver(precision=1e-6)
    assert 0.0 < solver.contraction_ratio < 1.0
    assert solver.verify_banach_conditions() is True
    # Strategy enumeration smoke
    for strat in (SearchStrategy.SYSTEMATIC_GRID, SearchStrategy.RANDOM_SAMPLING):
        # Use enumerate_all_fixed_points with a small domain for speed
        res = solver.enumerate_all_fixed_points(search_domain_size=10, strategy=strat)
        assert isinstance(res, list)
        # If any solutions found, check one for shape
        if res:
            sol = res[0]
            assert hasattr(sol, "fixed_point_type") and hasattr(sol, "iteration_count")
