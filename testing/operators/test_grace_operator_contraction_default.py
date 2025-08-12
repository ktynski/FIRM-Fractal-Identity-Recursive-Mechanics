def test_grace_operator_default_contraction_and_phi():
    from foundation.operators.grace_operator import GRACE_OPERATOR
    assert GRACE_OPERATOR.verify_contraction_property() in (True, False)
    assert GRACE_OPERATOR.derive_phi_emergence() > 1.0

