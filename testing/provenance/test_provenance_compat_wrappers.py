def test_provenance_compat_wrappers_and_summary(monkeypatch):
    from provenance.provenance_tracker import ProvenanceTracker
    t = ProvenanceTracker()
    # start + complete wrappers
    t.start_operation("compute_alpha", mathematical_inputs={"n": 1}, theoretical_basis="phi-math")
    t.complete_operation(result={"alpha_inv": 100}, derivation_path=["step1"], verification_status="ok")
    # error and derivation wrappers
    t.log_error("minor issue")
    seal = t.record_derivation("derive_phi", inputs={"k": 2}, outputs={"phi": 1.618}, mathematical_steps=["golden"], contamination_check=False)
    assert isinstance(seal, str)
    summary = t.get_derivation_summary()
    assert summary["total_operations"] >= 3
    assert isinstance(summary["cryptographic_seal"], str) or summary["cryptographic_seal"] is None

def test_provenance_empirical_detection_and_precision_fallback(monkeypatch):
    from provenance.provenance_tracker import ProvenanceTracker
    import provenance.provenance_tracker as mod
    t = ProvenanceTracker()
    # string keyword empirical
    assert t.contains_empirical_data({"note": "experimental setup"}) is True
    cont = t.detect_empirical_contamination({"note": "observed value"})
    assert isinstance(cont, list)
    # precision framework None path
    monkeypatch.setattr(mod, "PRECISION_FRAMEWORK", None, raising=False)
    b = t.compute_error_bounds({"a": 1.0}, 2.0)
    assert set(b.keys()) >= {"relative_error", "absolute_error", "precision_decimal_places"}
