import pytest
from foundation.categories.fixed_point_category import (
    FixedPointCategory,
    GraceEquivariantMorphism,
)


def test_grace_equivariant_morphism_commutes_and_compose_error():
    cat = FixedPointCategory()
    X = cat.example_object("X")
    Y = cat.example_object("Y")
    Z = cat.example_object("Z")

    # Callable morphism that maps presheaf to itself (proxy)
    def f_presheaf(p):
        return p

    morph = GraceEquivariantMorphism(source=X, target=Y, morphism_data=f_presheaf)
    assert morph.verify_grace_equivariance() is True

    # Compose error on mismatched tokens
    f = cat.example_morphism(X, Y)
    g = cat.example_morphism(Z, Y)
    with pytest.raises(ValueError):
        cat.compose(f, g)

