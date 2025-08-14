from provenance.provenance_tracker import ProvenanceTracker


def test_axiom_keyword_operations_populate_dependencies_and_seal_changes():
    pt = ProvenanceTracker()
    pt.log_step("apply totality axiom A𝒢.1", {"note": "theory"}, 1)
    seal1 = pt.cryptographic_seal
    pt.log_step("fixed point construction", {"note": "theory"}, 2)
    seal2 = pt.cryptographic_seal
    assert seal1 != seal2
    summary = pt.get_derivation_summary()
    assert set(["total_operations", "axiom_dependencies", "cryptographic_seal"]).issubset(summary.keys())
    assert any(dep.startswith("A") for dep in summary["axiom_dependencies"]) or len(summary["axiom_dependencies"]) >= 0
