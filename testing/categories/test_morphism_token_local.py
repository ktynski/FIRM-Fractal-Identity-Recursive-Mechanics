from foundation.categories.fixed_point_category import PHYSICAL_REALITY


def test_morphism_token_and_composition_laws():
    X = PHYSICAL_REALITY.example_object("X")
    Y = PHYSICAL_REALITY.example_object("Y")
    Z = PHYSICAL_REALITY.example_object("Z")

    id_X = PHYSICAL_REALITY.identity(X)
    f = PHYSICAL_REALITY.example_morphism(X, Y)
    g = PHYSICAL_REALITY.example_morphism(Y, Z)

    # typed tokens
    assert hasattr(f, "source_name") and hasattr(f, "target_name")

    # composability and composition
    assert PHYSICAL_REALITY.is_composable(g, f) is True
    fog = PHYSICAL_REALITY.compose(g, f)
    assert fog.source_name == X.name and fog.target_name == Z.name

    # identity laws: id_X ∘ f = f and f ∘ id_Y = f where defined
    assert PHYSICAL_REALITY.compose(f, id_X).target_name == f.target_name
    id_Y = PHYSICAL_REALITY.identity(Y)
    assert PHYSICAL_REALITY.compose(id_Y, f).source_name == f.source_name
