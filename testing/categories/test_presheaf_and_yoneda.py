from foundation.categories.presheaf_category import PresheafStructure, PresheafType, PresheafCategory


def test_presheaf_functoriality_symbolic_composition():
    # Construct a minimal presheaf with identity and two synthetic morphisms
    presheaf = PresheafStructure(
        name="TestPresheaf",
        presheaf_type=PresheafType.NON_REPRESENTABLE,
        object_mapping={"A": {"x", "y"}},
        morphism_mapping={
            "id_A": (lambda z: z),
            "f_0": (lambda z: f"({z} ∘ f_0)"),
            "f_1": (lambda z: f"({z} ∘ f_1)"),
        },
    )

    assert presheaf.verify_functoriality() is True


def test_yoneda_embedding_representable_properties():
    C = PresheafCategory("Ω")
    embedded = C.yoneda_embed_object("X")
    assert embedded.hom_functor.presheaf_type == PresheafType.REPRESENTABLE
    assert embedded.hom_functor.representing_object == "X"
    assert embedded.hom_functor.verify_functoriality() is True


def test_yoneda_naturality_and_isomorphism_flags():
    C = PresheafCategory("Ω")
    verification = C.verify_yoneda_full_faithfulness()
    assert verification["faithfulness"] is True
    assert verification["fullness"] is True
    assert verification["naturality"] is True
    assert verification["isomorphism"] is True


def test_presheaf_category_rejects_non_functorial_presheaf():
    C = PresheafCategory("Ω")
    bad = PresheafStructure(
        name="BadPresheaf",
        presheaf_type=PresheafType.NON_REPRESENTABLE,
        object_mapping={"A": {"x"}},
        morphism_mapping={
            "id_A": (lambda z: f"bad_{z}"),  # violates identity law
        },
    )
    assert bad.verify_functoriality() is False
    import pytest
    with pytest.raises(ValueError):
        C.add_presheaf(bad)


def test_construct_topos_and_prepare_for_grace_operator():
    C = PresheafCategory("Ω")
    # Build topos and embed one object to satisfy readiness conditions
    topos = C.construct_topos_structure()
    assert all(topos.values())
    C.yoneda_embed_object("Q")
    assert C.prepare_for_grace_operator() is True
