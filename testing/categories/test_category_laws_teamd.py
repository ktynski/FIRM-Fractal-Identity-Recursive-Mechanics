from foundation.categories.fixed_point_category import FixedPointCategory


def test_fixed_point_category_identity_and_associativity():
    cat = FixedPointCategory()

    # Deterministic example objects
    X = cat.example_object("X")
    Y = cat.example_object("Y")
    Z = cat.example_object("Z")

    # Identity laws: id ∘ f = f and f ∘ id = f (by token equality)
    f = cat.example_morphism(X, Y)
    id_X = cat.identity(X)
    id_Y = cat.identity(Y)

    left = cat.compose(f, id_X)  # f ∘ id_X
    right = cat.compose(id_Y, f)  # id_Y ∘ f

    assert left.as_tuple() == f.as_tuple()
    assert right.as_tuple() == f.as_tuple()

    # Associativity: h ∘ (g ∘ f) == (h ∘ g) ∘ f
    g = cat.example_morphism(Y, Z)
    h = cat.example_morphism(Z, Z)  # endomorphism on Z for composability

    inner = cat.compose(g, f)
    left_assoc = cat.compose(h, inner)

    outer = cat.compose(h, g)
    right_assoc = cat.compose(outer, f)

    assert left_assoc.as_tuple() == right_assoc.as_tuple()
