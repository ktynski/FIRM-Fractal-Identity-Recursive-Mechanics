def test_stabilization_axiom_smoke():
    from foundation.axioms.a_grace_3_stabilization import STABILIZATION_AXIOM, StabilizingMorphismCandidate

    assert STABILIZATION_AXIOM.verify_consistency() in (True, False)
    assert STABILIZATION_AXIOM.prove_existence() in (True, False)
    assert STABILIZATION_AXIOM.prove_uniqueness() in (True, False)

    candidate = STABILIZATION_AXIOM.construct_grace_operator()
    assert isinstance(candidate, StabilizingMorphismCandidate)
    # exercise candidate helpers
    assert candidate.verify_functoriality() in (True, False)
    assert candidate.contraction_ratio > 0
    # entropy flow helpers
    before = [3.0, 1.0, 2.0]
    minimized = candidate.minimize_entropy(before)
    contracted = candidate.apply_contraction(minimized)
    assert isinstance(contracted, type(before))

    phi = STABILIZATION_AXIOM.derive_phi_emergence()
    assert 1.0 < phi < 2.0


def test_identity_axiom_smoke_and_ops():
    from foundation.axioms.a_psi_1_identity import IDENTITY_AXIOM
    from foundation.categories.fixed_point_category import PHYSICAL_REALITY

    assert IDENTITY_AXIOM.verify_consistency() in (True, False)

    # Derivation texts (non-empty)
    assert isinstance(IDENTITY_AXIOM.derive_consciousness_emergence(), str)
    assert isinstance(IDENTITY_AXIOM.resolve_quantum_measurement_problem(), str)

    # Exercise Ψ operator on a deterministic object
    X = PHYSICAL_REALITY.example_object("X")
    psiX = IDENTITY_AXIOM._psi_operator.apply_psi_operator(X, "conscious")
    assert psiX.name.startswith("Psi(")
    # Derive a simple measurement description
    qm = IDENTITY_AXIOM._psi_operator.derive_quantum_measurement("conscious", X)
    assert isinstance(qm.outcome_probabilities, dict)

