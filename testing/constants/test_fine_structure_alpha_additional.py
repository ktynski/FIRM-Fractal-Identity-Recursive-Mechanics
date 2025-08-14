from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA


def test_alpha_cross_derivation_consistency_and_provenance():
    # Compute two derivations
    primary = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
    alt = FINE_STRUCTURE_ALPHA.derive_alternative_phi_expression()

    # Consistency
    rel = abs(primary.alpha_inverse_value - alt.alpha_inverse_value) / primary.alpha_inverse_value
    assert rel < 1e-10

    # Provenance tree builds for a method
    tree = FINE_STRUCTURE_ALPHA.build_complete_provenance(primary.method)
    assert hasattr(tree, "root") or hasattr(tree, "root_node")
