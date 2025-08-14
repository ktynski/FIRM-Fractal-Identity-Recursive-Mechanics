from foundation.operators.unified_stability_criterion import USC_FRAMEWORK


def test_generate_usc_report_contains_headings_and_values():
    rep = USC_FRAMEWORK.generate_usc_report()
    assert isinstance(rep, str)
    assert "UNIFIED STABILITY CRITERION (USC) REPORT" in rep
    assert "Optimal n:" in rep
    # Hermiticity check and local stability sanity
    assert USC_FRAMEWORK.verify_phi_hermitian(113)
    results = USC_FRAMEWORK.compute_stability_analysis(range(112, 115))
    assert any(r.stability_type in {r.stability_type.OPTIMAL, r.stability_type.STABLE} for r in results)
