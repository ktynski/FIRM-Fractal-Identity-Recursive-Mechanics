from foundation.operators.unified_stability_criterion import USC_FRAMEWORK


def test_usc_analyze_connection_fields():
    conn = USC_FRAMEWORK.analyze_connection_to_physics(113)
    for k in ("stability_condition", "stability_measure", "eigenvalue_minimum", "psi_operator_value", "phi_connection", "structural_stability"):
        assert k in conn

