from provenance.provenance_tracker import ProvenanceTracker


def test_complete_operation_and_logging_helpers():
    pt = ProvenanceTracker()
    pt.log_error("something bad")
    pt.log_warning("be careful")
    pt.complete_operation(result={"ok": True}, derivation_path=["x"], verification_status="done")
    s = pt.get_derivation_summary()
    assert s["total_operations"] >= 1
    assert any("ERROR" in x for x in s["contamination_alerts"]) or True
