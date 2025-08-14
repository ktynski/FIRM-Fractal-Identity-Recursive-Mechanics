def test_identity_framework_generation_and_predictions():
    from foundation.axioms.a_psi_1_identity import IDENTITY_AXIOM
    from foundation.categories.fixed_point_category import PHYSICAL_REALITY

    # Generate full framework text
    text = IDENTITY_AXIOM.generate_consciousness_framework()
    assert isinstance(text, str) and "FIRM Consciousness Integration Framework" in text

    # Verify predictions dictionary shape via operator
    X = PHYSICAL_REALITY.example_object("X")
    qm = IDENTITY_AXIOM._psi_operator.derive_quantum_measurement("conscious", X)
    assert isinstance(qm.outcome_probabilities, dict) and len(qm.outcome_probabilities) >= 1
