def test_provenance_tracker_true_path_minimal_axiom_chain():
    from provenance.provenance_tracker import ProvenanceTracker
    tracker = ProvenanceTracker()
    # log two axiom-tagged operations with trivial numeric inputs
    tracker.log_step("axiom_application:A𝒢.1", {"x": 1.0}, {"ok": True})
    tracker.log_step("axiom_application:A𝒢.2", {"y": 2.0}, {"ok": True})
    # ensure chain recorded and cryptographic seal produced
    assert len(tracker.derivation_chain) >= 2
    assert tracker.cryptographic_seal is not None

