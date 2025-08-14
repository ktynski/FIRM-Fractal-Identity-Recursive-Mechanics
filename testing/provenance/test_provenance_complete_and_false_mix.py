def test_provenance_complete_then_breaks_false():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    # complete set
    for s in [
        "totality grothendieck", "reflexive yoneda", "grace stabilizing", "fixed point existence", "consciousness identity"]:
        t.log_step(s, {"n": 1.0}, 0.0)
    assert t.verify_complete_provenance() is True
    # now add an op with no deps; verification should fail afterwards
    t.log_step("misc computation", {"m": 2.0}, 0.0)
    assert t.verify_complete_provenance() is False
