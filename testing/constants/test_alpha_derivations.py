from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA


def test_alpha_primary_and_alternative_derivations():
    r1 = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
    r2 = FINE_STRUCTURE_ALPHA.derive_alternative_phi_expression()
    # Expect result objects with numeric alpha_inverse_value and no empirical inputs
    v1 = getattr(r1, "alpha_inverse_value", None)
    v2 = getattr(r2, "alpha_inverse_value", None)
    assert isinstance(v1, (int, float))
    assert isinstance(v2, (int, float))
    assert getattr(r1, "empirical_inputs", []) == []
    assert getattr(r2, "empirical_inputs", []) == []
