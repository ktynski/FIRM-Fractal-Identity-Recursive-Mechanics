from foundation.categories.fixed_point_category import PHYSICAL_REALITY


def test_category_ops_compose_identity():
    cat = PHYSICAL_REALITY
    X = cat.example_object("X")
    Y = cat.example_object("Y")
    f = cat.example_morphism(X, Y)
    idY = cat.identity(Y)
    # is_composable and compose
    assert cat.is_composable(idY, f) is True
    comp = cat.compose(idY, f)
    assert comp.as_tuple()[0] == X.name and comp.as_tuple()[2] == Y.name
    # objects() and morphisms() return sets
    assert isinstance(cat.objects(), set)
    assert isinstance(cat.morphisms(), set)
