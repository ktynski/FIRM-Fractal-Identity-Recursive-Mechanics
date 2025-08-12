from foundation.categories.fixed_point_category import PHYSICAL_REALITY


def test_spacetime_dims():
    space, time = PHYSICAL_REALITY.compute_spacetime_dimensionality()
    assert (space, time) == (3, 1)
