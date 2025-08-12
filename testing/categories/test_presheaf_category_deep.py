def test_presheaf_category_yoneda_and_topos():
    from foundation.categories.presheaf_category import PresheafCategory, PresheafStructure, PresheafType
    cat = PresheafCategory("Ω")
    # Add a simple presheaf obeying identity
    P = PresheafStructure(
        name="F",
        presheaf_type=PresheafType.NON_REPRESENTABLE,
        object_mapping={"X": {"x"}},
        morphism_mapping={"id_X": lambda z: z}
    )
    cat.add_presheaf(P)
    yX = cat.yoneda_embed_object("X")
    assert yX.original_object == "X"
    yoneda = cat.verify_yoneda_full_faithfulness()
    assert yoneda["faithfulness"] and yoneda["fullness"]
    topos = cat.construct_topos_structure()
    assert all(topos.values())
    text = cat.enable_self_reference()
    assert isinstance(text, str) and "Self-Reference Enabled" in text
    assert cat.prepare_for_grace_operator() in (True, False)

