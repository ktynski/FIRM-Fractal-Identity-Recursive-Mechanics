from provenance.provenance_tracker import ProvenanceTracker


def test_error_bounds_visible_in_summary_and_report():
    pt = ProvenanceTracker()
    pt.log_step("phi power", {"phi": 1.618}, 2.0)
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] >= 1
    # Ensure last operation included error bounds
    last = pt.derivation_chain[-1]
    assert last.error_bounds is not None
    assert set(["relative_error", "absolute_error"]).issubset(last.error_bounds.keys())
    report = pt.generate_audit_report()
    assert "FIRM PROVENANCE AUDIT REPORT" in report

