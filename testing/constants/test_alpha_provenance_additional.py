from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA, DerivationMethod


def test_alpha_cache_consistency_between_derivations():
    # First calls populate cache
    p1 = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
    a1 = FINE_STRUCTURE_ALPHA.derive_alternative_phi_expression()
    # Second calls should hit cache and remain identical
    p2 = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
    a2 = FINE_STRUCTURE_ALPHA.derive_alternative_phi_expression()
    assert p1.alpha_inverse_value == p2.alpha_inverse_value
    assert a1.alpha_inverse_value == a2.alpha_inverse_value


def test_alpha_provenance_tree_builds_minimal_structure():
    tree = FINE_STRUCTURE_ALPHA.build_complete_provenance(DerivationMethod.PHI_POWERS_PRIMARY)
    # Root present and cryptographic integrity holds after insertion by ProvenanceTree
    assert tree.root_node.node_id in tree.nodes
    assert tree.nodes[tree.root_node.node_id].verify_integrity()
    # Coerced legacy constructor: target_result should be a non-empty string
    assert isinstance(tree.target_result, str) and len(tree.target_result) > 0

