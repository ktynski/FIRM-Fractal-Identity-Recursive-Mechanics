import pytest
from foundation.categories.fixed_point_category import PHYSICAL_REALITY


def test_compose_non_composable_raises():
    cat = PHYSICAL_REALITY
    X = cat.example_object("X")
    Y = cat.example_object("Y")
    Z = cat.example_object("Z")
    W = cat.example_object("W")
    f = cat.example_morphism(X, Y)
    g = cat.example_morphism(Z, W)
    # f after g is not composable (W != X)
    with pytest.raises(ValueError):
        cat.compose(f, g)
