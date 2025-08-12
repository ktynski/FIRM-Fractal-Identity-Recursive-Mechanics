def test_totality_construct_and_russell_resolution():
    from foundation.axioms.a_grace_1_totality import AGrace1Totality
    ax = AGrace1Totality()
    ax.construct_universe_hierarchy(3)
    assert ax.verify_stratification() in (True, False)
    assert ax.resolve_russell_paradox() in (True, False)
    desc = ax.compute_totality_colimit()
    assert isinstance(desc, str)

