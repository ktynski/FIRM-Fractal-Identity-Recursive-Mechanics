from provenance.provenance_tracker import ProvenanceTracker


def test_provenance_complete_true_path():
    pt = ProvenanceTracker()
    # Log steps containing all required axioms (A𝒢.1-4, AΨ.1)
    for s in (
        "apply axiom A𝒢.1 totality",
        "apply axiom A𝒢.2 reflexive yoneda",
        "apply axiom A𝒢.3 grace stabilization",
        "fixed point A𝒢.4 coherence",
        "consciousness identity AΨ.1",
    ):
        pt.log_step(s, {"desc": s}, None)
    assert pt.verify_complete_provenance() is True
    # Report should render
    txt = pt.generate_audit_report()
    assert isinstance(txt, str) and "FIRM PROVENANCE AUDIT REPORT" in txt
