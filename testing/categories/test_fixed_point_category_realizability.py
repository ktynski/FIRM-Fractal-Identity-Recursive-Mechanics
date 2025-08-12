from foundation.categories.fixed_point_category import FixedPointCategory


def test_verify_physical_realizability_all_objects():
    cat = FixedPointCategory()
    result = cat.verify_physical_realizability()
    assert isinstance(result, dict)
    # Should include keys for the constructed objects
    for key in ("U1_EM", "SU2_Weak", "SU3_Strong", "Spacetime"):
        assert any(key in name or name in key for name in result.keys())
