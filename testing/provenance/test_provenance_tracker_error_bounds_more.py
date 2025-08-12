import math

from provenance.provenance_tracker import ProvenanceTracker


def test_error_bounds_scalar_nonzero():
    pt = ProvenanceTracker()
    bounds = pt.compute_error_bounds({"a": 10.0, "b": 5.0}, 2.0)
    assert set(["relative_error", "absolute_error"]).issubset(bounds.keys())
    assert bounds["relative_error"] > 0
    assert bounds["absolute_error"] > 0


def test_error_bounds_scalar_zero():
    pt = ProvenanceTracker()
    bounds = pt.compute_error_bounds({"a": 10.0, "b": 5.0}, 0.0)
    assert set(["relative_error", "absolute_error"]).issubset(bounds.keys())
    assert bounds["relative_error"] > 0
    assert bounds["absolute_error"] > 0


def test_error_bounds_sequence_output_and_determinism():
    pt = ProvenanceTracker()
    out = (1.0, 2.0, 3.0)
    bounds_1 = pt.compute_error_bounds({"phi": 1.618, "n": 3}, out)
    bounds_2 = pt.compute_error_bounds({"phi": 1.618, "n": 3}, out)
    assert set(["relative_error", "absolute_error"]).issubset(bounds_1.keys())
    assert bounds_1 == bounds_2

