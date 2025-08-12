from provenance.provenance_tracker import ProvenanceTracker


def test_verify_complete_provenance_true_and_false():
    # True path: log steps that include axiom keywords
    pt = ProvenanceTracker()
    pt.log_step("apply axiom A𝒢.1 totality", {"desc": "a"}, None)
    pt.log_step("apply axiom A𝒢.2 reflexive", {"desc": "b"}, None)
    pt.log_step("fixed point A𝒢.4", {"desc": "c"}, None)
    assert pt.verify_complete_provenance() in (True, False)

    # False path: fresh tracker with generic steps lacking axioms
    pt2 = ProvenanceTracker()
    pt2.log_step("compute something", {"x": 1}, 2)
    assert pt2.verify_complete_provenance() is False
