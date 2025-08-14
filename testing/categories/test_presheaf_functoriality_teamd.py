from foundation.categories.presheaf_category import PresheafStructure, PresheafType


def test_presheaf_functoriality_identity_and_composition():
    # Build a tiny presheaf with identity and two synthetic morphisms f_1, f_2
    def id_action(x):
        return x

    def f_1(x):
        return f"F1(∘ {x})"

    def f_2(x):
        return f"F2(∘ {x})"

    P = PresheafStructure(
        name="Tiny",
        presheaf_type=PresheafType.NON_REPRESENTABLE,
        object_mapping={"X": {"•"}},
        morphism_mapping={
            "id_X": id_action,
            "f_1": f_1,
            "f_2": f_2,
        },
    )

    assert P.verify_functoriality() is True
