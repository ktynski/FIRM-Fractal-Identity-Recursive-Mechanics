from foundation.axioms import verify_all_axioms, AXIOM_REGISTRY, AxiomStatus


def test_verify_all_axioms_registry_and_statuses():
    results = verify_all_axioms()
    assert isinstance(results, dict)
    # If registry has entries, verify keys match ids and statuses are valid
    if AXIOM_REGISTRY:
        for ax_id in AXIOM_REGISTRY.keys():
            assert ax_id in results
            assert results[ax_id].status in (
                AxiomStatus.COMPLETE, AxiomStatus.CONSISTENT, AxiomStatus.INDEPENDENT, AxiomStatus.FAILED
            )
