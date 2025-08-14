def test_error_bounds_on_tuple_output():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    b = t.compute_error_bounds({"a": 1.0, "b": 2.0}, (1.0, 2.0))
    assert set(b.keys()) >= {"relative_error", "absolute_error"}
