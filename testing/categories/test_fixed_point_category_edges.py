import pytest

from foundation.categories.fixed_point_category import FixedPointCategory


def test_normalize_morphism_invalid_raises():
    cat = FixedPointCategory()
    with pytest.raises(ValueError):
        cat._normalize_morphism(("bad", "tuple"))  # wrong shape


def test_identity_and_morphisms_exposure_and_dimensionality_missing_spacetime():
    cat = FixedPointCategory()
    x = cat.example_object("X")
    idm = cat.identity(x)
    assert idm.as_tuple()[0] == idm.as_tuple()[2]

    # Temporarily remove spacetime and check edge path
    # Accessing private dict for edge-case coverage only in tests
    original = cat._fixed_points.pop("Spacetime", None)
    try:
        dims = cat.compute_spacetime_dimensionality()
        assert dims in ((0, 0), (3, 1))
    finally:
        if original is not None:
            cat._fixed_points["Spacetime"] = original
