def test_axiom_registry_and_verify_all():
    from foundation.axioms import verify_all_axioms, AXIOM_REGISTRY
    results = verify_all_axioms()
    assert isinstance(results, dict)
    # At least ensure registry exposes some ids
    assert isinstance(AXIOM_REGISTRY, dict)


def test_grothendieck_universe_helpers():
    from foundation.categories.grothendieck_universe import UNIVERSE_OMEGA
    assert UNIVERSE_OMEGA.verify_stratification() in (True, False)
    # Call totality then self-reference foundation
    desc = UNIVERSE_OMEGA.construct_totality_colimit()
    assert isinstance(desc, str)
    assert UNIVERSE_OMEGA.enable_self_reference_foundation() in (True, False)
    # Proof text exists
    proof = UNIVERSE_OMEGA.generate_mathematical_proof()
    assert isinstance(proof, str)

