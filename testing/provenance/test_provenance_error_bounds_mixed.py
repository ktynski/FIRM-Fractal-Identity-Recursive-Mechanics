def test_compute_error_bounds_mixed_inputs():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    b = t.compute_error_bounds({"a": 0.0, "b": 1e-12, "c": "phi"}, 0.0)
    assert set(b.keys()) >= {"relative_error", "absolute_error"}
