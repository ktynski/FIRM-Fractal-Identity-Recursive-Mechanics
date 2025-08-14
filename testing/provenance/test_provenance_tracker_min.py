from provenance.provenance_tracker import ProvenanceTracker, MathematicalOperation, OperationType, ContaminationError


def test_log_step_and_summary():
    pt = ProvenanceTracker()
    # Use pure symbolic-like inputs to avoid numeric contamination filter
    pt.log_step("derive_phi", {"symbol": "phi", "expr": "(1+sqrt(5))/2"}, 1.618)
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] >= 1
    assert isinstance(summary["cryptographic_seal"], str)


def test_record_derivation_pure_inputs():
    pt = ProvenanceTracker()
    seal = pt.record_derivation(
        operation="pure_phi_derivation",
        inputs={"n": 5},
        outputs={"phi_n": 11.09},
        mathematical_steps=["phi^n"],
        contamination_check=False,
    )
    assert isinstance(seal, str)
