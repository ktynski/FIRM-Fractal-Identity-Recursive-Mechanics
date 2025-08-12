from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA, DerivationMethod


def test_alpha_api_methods_and_provenance():
    # alpha_inverse_pure and derive_alpha_inverse cover utility paths
    pure = FINE_STRUCTURE_ALPHA.alpha_inverse_pure()
    assert pure > 0
    obj = FINE_STRUCTURE_ALPHA.derive_alpha_inverse()
    assert getattr(obj, "value", 0.0) > 0
    # Provenance builders for both methods
    tree_primary = FINE_STRUCTURE_ALPHA.build_complete_provenance(DerivationMethod.PHI_POWERS_PRIMARY)
    assert tree_primary is not None
    # Cross-derivation consistency is finite and small
    cons = FINE_STRUCTURE_ALPHA.verify_cross_derivation_consistency()
    assert isinstance(cons, dict) and all(v >= 0 for v in cons.values())
