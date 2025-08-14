import pytest
from foundation.operators.phi_recursion import PhiRecursion


def test_compute_phi_power_negative_and_cache_paths():
    pr = PhiRecursion()
    v_neg = pr.compute_phi_power(-3)
    assert v_neg > 0.0
    # call again to exercise LRU cache path
    v_neg2 = pr.compute_phi_power(-3)
    assert v_neg2 == v_neg


def test_verify_phi_properties_and_continued_fraction():
    pr = PhiRecursion()
    props = pr.verify_phi_properties()
    assert all(isinstance(v, bool) for v in props.values())
    # private helper acceptable in tests for coverage
    approx = pr._compute_continued_fraction_approximation(terms=5)
    assert approx > 1.0


def test_iterate_recursion_invalid_initial_value_raises():
    pr = PhiRecursion()
    with pytest.raises(ValueError):
        list(pr.iterate_recursion(initial_value=0.0))
