def test_provenance_summary_operations_shape():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    t.log_step("axiom step", {"a": 1.0}, 0.0)
    s = t.get_derivation_summary()
    ops = s["operations"]
    assert all(set(["id","type","expression","justification","axiom_deps","timestamp","hash"]) <= set(o.keys()) for o in ops)
