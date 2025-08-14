def test_provenance_summary_fields_and_complete():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    # cover both with-deps and no-deps ops
    t.log_step("totality grothendieck", {"a": 1.0}, 0.0)
    t.log_step("misc", {"b": 2.0}, 0.0)
    s = t.get_derivation_summary()
    assert isinstance(s, dict)
    assert "total_operations" in s and "operations" in s and isinstance(s["operations"], list)
