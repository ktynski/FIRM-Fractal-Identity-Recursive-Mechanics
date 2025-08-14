from foundation.categories.fixed_point_category import FixedPointCategory


def test_enumerate_gauge_groups_expected_keys():
    cat = FixedPointCategory()
    groups = cat.enumerate_gauge_groups()
    # Expect at least the SM groups
    assert any("electromagnetic" in k for k in groups.keys())
    assert any("weak" in k for k in groups.keys())
    assert any("strong" in k for k in groups.keys())


def test_verify_realizability_returns_booleans():
    cat = FixedPointCategory()
    res = cat.verify_physical_realizability()
    assert isinstance(res, dict)
    for v in res.values():
        assert isinstance(v, bool)
