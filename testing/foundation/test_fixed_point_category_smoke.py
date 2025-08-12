from foundation.categories.fixed_point_category import PHYSICAL_REALITY


def test_objects_and_morphisms_enumeration():
    # Avoid hashing dataclass with dict fields; use example accessors
    X = PHYSICAL_REALITY.example_object("X")
    assert X.name == "U1_Electromagnetic"
    space, time = PHYSICAL_REALITY.compute_spacetime_dimensionality()
    assert (space, time) == (3, 1)


def test_identity_and_composition_tokens():
    X = PHYSICAL_REALITY.example_object("X")
    Y = PHYSICAL_REALITY.example_object("Y")
    f = PHYSICAL_REALITY.example_morphism(X, Y)
    id_X = PHYSICAL_REALITY.identity(X)
    assert id_X.as_tuple()[0] == id_X.as_tuple()[2]
    composed = PHYSICAL_REALITY.compose(f, id_X)
    assert composed.as_tuple()[0] == X.name
