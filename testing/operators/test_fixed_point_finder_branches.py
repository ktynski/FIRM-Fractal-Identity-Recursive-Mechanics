import math

from foundation.operators.fixed_point_finder import FIXED_POINT_SOLVER, SearchStrategy


def test_numeric_iteration_converges_and_nonconverges():
    # Converging map
    f = lambda x: 0.5 * (x + 1.0)
    val = FIXED_POINT_SOLVER.find_fixed_point(f=f, initial_guess=0.0, tolerance=1e-9, max_iterations=100)
    assert isinstance(val, float)

    # Non-converging map should raise within limited iterations
    g = lambda x: x + 1.0
    try:
        FIXED_POINT_SOLVER.find_fixed_point(f=g, initial_guess=0.0, tolerance=1e-30, max_iterations=5)
        assert False, "Expected non-convergence error"
    except ValueError:
        pass


def test_distance_metrics_for_sequences_and_dicts():
    d = FIXED_POINT_SOLVER._compute_distance
    assert d([1, 2], [1, 3, 0]) > 0
    assert d({"a": 1}, {"a": 1, "b": 2}) > 0
    assert d(1.0, 1.0) == 0.0


def test_enumeration_and_analysis_paths():
    sols = FIXED_POINT_SOLVER.enumerate_all_fixed_points(search_domain_size=3, strategy=SearchStrategy.SYSTEMATIC_GRID)
    # Analysis for a known solution id if any
    for s in sols[:1]:
        analysis = FIXED_POINT_SOLVER.analyze_convergence_properties(s.solution_id)
        assert analysis.banach_conditions_met is True
        rep = FIXED_POINT_SOLVER.generate_fixed_point_report()
        assert "FIRM Fixed Point Analysis Report" in rep
