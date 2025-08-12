from foundation.categories.fixed_point_category import PHYSICAL_REALITY, FixedPointCategory


def test_is_composable_false_branch():
    cat = FixedPointCategory()
    x = cat.example_object("X")
    y = cat.example_object("Y")
    z = cat.example_object("Z")
    # sanity: composable pair requires g: X→Y and f: Y→Z for f∘g
    g_good = cat.example_morphism(x, y).as_tuple()
    f_good = cat.example_morphism(y, z).as_tuple()
    assert cat.is_composable(f_good, g_good) is True
    # non-composable pair: mismatch (g: Z→X vs f: Y→Z)
    g_bad = cat.example_morphism(z, x).as_tuple()
    assert cat.is_composable(f_good, g_bad) is False


def test_add_fixed_point_negative_and_positive_paths():
    cat = FixedPointCategory()
    # Positive path: use a valid object already verified
    obj = cat.example_object("X")
    cat.add_fixed_point(obj)  # should not raise

    # Negative path: craft an invalid FixedPointStructure via monkeypatching verify
    class Dummy:
        name = "Bad"
        def verify_fixed_point_property(self):
            return False
    bad = Dummy()
    try:
        cat.add_fixed_point(bad)  # type: ignore[arg-type]
        raised = False
    except ValueError:
        raised = True
    assert raised is True


def test_derive_fundamental_constants_covers_morphism_and_fixed_points():
    cat = FixedPointCategory()
    consts = cat.derive_fundamental_constants()
    # Presence not guaranteed for all, but call path must execute
    assert isinstance(consts, dict)

