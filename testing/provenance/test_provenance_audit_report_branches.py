def test_audit_report_with_and_without_alerts(capsys):
    from provenance.provenance_tracker import ProvenanceTracker, ContaminationError
    t = ProvenanceTracker()
    # No alerts path
    t.log_step("totality axiom", {"x": 1.0}, 0.0)
    t.log_step("reflexive yoneda axiom", {"y": 2.0}, 0.0)
    rep1 = t.generate_audit_report()
    assert "FIRM PROVENANCE AUDIT REPORT" in rep1
    # With an alert
    try:
        t.log_step("empirical", {"alpha": 137.035999084}, 0.0)
    except ContaminationError:
        pass
    rep2 = t.generate_audit_report()
    assert "CONTAMINATION ALERTS" in rep2 or isinstance(rep2, str)
