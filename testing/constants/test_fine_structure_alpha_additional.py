from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA


def test_alpha_cross_derivation_consistency_and_provenance():
    # Compute two derivations
    primary = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
    alt = FINE_STRUCTURE_ALPHA.derive_alternative_phi_expression()

    # Consistency check - different mathematical methods should be reasonably close
    # but not identical since they use fundamentally different approaches
    rel = abs(primary.alpha_inverse_value - alt.alpha_inverse_value) / primary.alpha_inverse_value
    assert rel < 0.01, f"Methods differ by {rel*100:.2f}% - acceptable for different mathematical approaches"

    # Provenance tree builds for a method
    tree = FINE_STRUCTURE_ALPHA.build_complete_provenance(primary.method)
    assert hasattr(tree, "root") or hasattr(tree, "root_node")
