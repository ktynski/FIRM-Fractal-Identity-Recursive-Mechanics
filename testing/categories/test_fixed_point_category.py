from foundation.categories.fixed_point_category import FixedPointCategory, PHYSICAL_REALITY


def test_spacetime_dimensionality_counts():
    # Use the singleton which constructs spacetime fixed point on init
    d_space, d_time = PHYSICAL_REALITY.compute_spacetime_dimensionality()
    # Expect 3 spatial and 1 time dimension (from oscillatory pair)
    assert d_space == 3
    assert d_time == 1


def test_gauge_group_enumeration_nonempty():
    cat = FixedPointCategory()
    mapping = cat.enumerate_gauge_groups()
    # Should include at least EM, weak, strong entries
    assert any("electromagnetic" in k for k in mapping.keys())
    assert any("weak" in k for k in mapping.keys())
    assert any("strong" in k for k in mapping.keys())
