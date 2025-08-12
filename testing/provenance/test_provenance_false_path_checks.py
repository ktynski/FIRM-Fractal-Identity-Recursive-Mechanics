def test_provenance_incomplete_false_path():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    # log steps missing some axioms and one with no dependency keywords
    t.log_step("totality axiom", {"x": 1.0}, 0.0)   # A𝒢.1
    t.log_step("computation with no axiom tag", {"y": 2.0}, 0.0)  # no deps
    assert t.verify_complete_provenance() is False

