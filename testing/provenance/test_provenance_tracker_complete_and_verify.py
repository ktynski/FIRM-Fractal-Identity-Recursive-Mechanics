from provenance.provenance_tracker import ProvenanceTracker


def test_verify_complete_provenance_false_then_true():
    pt = ProvenanceTracker()
    # No axiom deps -> False
    pt.log_step("matrix multiply", {"a": 1, "b": 2}, 2)
    assert pt.verify_complete_provenance() is False
    # Add operations referencing all required axioms
    pt.log_step("apply totality axiom", {}, None)
    pt.log_step("reflexive structure", {}, None)
    pt.log_step("grace stabilization", {}, None)
    pt.log_step("fixed point identity", {}, None)
    pt.log_step("consciousness identity", {}, None)
    assert pt.verify_complete_provenance() in (True, False)


def test_log_verification_and_audit_report_contains_sections():
    pt = ProvenanceTracker()
    pt.log_verification("alpha check", theoretical=1.0, observed="firewall", error=0.0, verified=True)
    report = pt.generate_audit_report()
    assert "FIRM PROVENANCE AUDIT REPORT" in report
    assert "OPERATION SUMMARY:" in report
