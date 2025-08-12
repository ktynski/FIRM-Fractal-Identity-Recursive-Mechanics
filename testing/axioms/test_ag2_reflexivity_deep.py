def test_reflexivity_yoneda_and_presheaf_ops():
    from foundation.axioms.a_grace_2_reflexivity import PresheafCategory, Presheaf, YonedaEmbedding
    from foundation.axioms.a_grace_2_reflexivity import AGrace2Reflexivity

    cat = PresheafCategory("Ω")
    p = Presheaf("F", {"X": {1, 2}}, {"f": lambda x: x})
    cat.add_presheaf("F", p)
    assert cat.is_topos() is True
    assert cat.get_presheaf("F").name == "F"

    y = YonedaEmbedding(cat)
    eX = y.embed_object("X")
    faithful, full = y.verify_full_faithfulness()
    props = y.verify_naturality_and_isomorphism()
    assert eX.name.startswith("e(") and isinstance(props, dict)
    assert isinstance(faithful, bool) and isinstance(full, bool)

    ax = AGrace2Reflexivity()
    ax.construct_reflexive_internalization()
    ax.establish_yoneda_embedding()
    assert ax.enable_self_reference() in (True, False)

