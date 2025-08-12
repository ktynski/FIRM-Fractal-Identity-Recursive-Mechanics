from foundation.operators.phi_recursion import PHI_RECURSION
from foundation.operators.grace_operator import GRACE_OPERATOR


def test_phi_properties_true():
    props = PHI_RECURSION.verify_phi_properties()
    assert isinstance(props, dict)
    assert all(bool(v) for v in props.values())


def test_grace_contraction_property():
    assert bool(GRACE_OPERATOR.verify_contraction_property())
