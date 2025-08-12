from foundation.axioms import verify_all_axioms, AXIOM_REGISTRY


def test_verify_all_axioms_emits_results_for_registered():
    res = verify_all_axioms()
    # Should produce a mapping or an empty dict if imports fail; in our env we expect entries
    assert isinstance(res, dict)
    # If registry has entries, verify keys in result
    if AXIOM_REGISTRY:
        for k in AXIOM_REGISTRY.keys():
            assert k in res

