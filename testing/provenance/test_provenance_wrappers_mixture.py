def test_provenance_backward_compatibility_mixture():
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    # use legacy start/complete wrappers
    t.start_operation("opA", mathematical_inputs={"x": 1}, theoretical_basis="math")
    t.complete_operation(result={"r": 1}, derivation_path=["a"], verification_status="ok")
    # Test backward compatibility with record_derivation wrapper
    seal = t.record_derivation("deriveA", inputs={"a": 1}, outputs={"b": 2}, mathematical_steps=["s1"], contamination_check=False)
    assert isinstance(seal, str) or seal == ""
    # summary should include operations
    s = t.get_derivation_summary()
    assert s["total_operations"] >= 2
