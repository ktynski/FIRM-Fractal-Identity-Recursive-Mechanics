from foundation.categories.fixed_point_category import FixedPointCategory


def test_compose_and_identity_tokens():
    cat = FixedPointCategory()
    x = cat.example_object("X")
    y = cat.example_object("Y")
    z = cat.example_object("Z")

    g = cat.example_morphism(x, y)  # g: X→Y
    f = cat.example_morphism(y, z)  # f: Y→Z

    h = cat.compose(f.as_tuple(), g.as_tuple())  # f∘g: X→Z
    assert h.as_tuple() == (x.name, "→", z.name)

    id_x = cat.identity(x)
    assert id_x.as_tuple() == (x.name, "→", x.name)
