from foundation.operators.phi_recursion import PHI_VALUE


def test_phi_value_precision_and_iteration_foundation():
    assert abs(PHI_VALUE - 1.61803398875) < 1e-6
    x = 1.0
    for _ in range(20):
        x = 1.0 + 1.0 / x
    assert abs(x - PHI_VALUE) < 1e-6

from foundation.operators.phi_recursion import PHI_RECURSION, PHI_VALUE


def test_verify_phi_properties_all_true():
    props = PHI_RECURSION.verify_phi_properties()
    assert isinstance(props, dict)
    assert all(bool(v) for v in props.values())


def test_compute_phi_iterative_close_to_theoretical():
    approx = PHI_RECURSION.compute_phi_iterative(precision=1e-12, max_iterations=200)
    assert abs(approx - PHI_VALUE) < 1e-10
