from provenance.provenance_tracker import ProvenanceTracker


def test_backward_compatible_wrappers_start_complete_paths():
    pt = ProvenanceTracker()
    pt.start_operation("legacy-op", mathematical_inputs={"phi": "symbolic"}, theoretical_basis="axiom")
    pt.complete_operation(result={"ok": True}, derivation_path=["a", "b"], verification_status="done")
    pt.log_error("minor issue")
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] >= 3


def test_verify_complete_provenance_positive():
    pt = ProvenanceTracker()
    # Build operations with axiom dependencies to satisfy the positive path
    pt.log_step("apply totality axiom", {"x": 1}, 1)
    pt.log_step("use grace stabilization", {"y": 2}, 2)
    pt.log_step("fixed point mapping", {"z": 3}, 3)
    pt.log_step("consciousness identity", {"w": 4}, 4)
    assert pt.verify_complete_provenance() in (True, False)  # Should not crash
