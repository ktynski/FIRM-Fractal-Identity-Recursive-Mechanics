from provenance.derivation_tree import (
    DerivationNode,
    DerivationType,
    ProvenanceTree,
    PROVENANCE_VALIDATOR,
)


def test_validator_detects_missing_dependency_and_cycle():
    # Root axiom
    ax = DerivationNode(node_id="A", mathematical_expression="A", derivation_type=DerivationType.AXIOM)
    tree = ProvenanceTree(root_node=ax)

    # Node with missing dependency
    b = DerivationNode(node_id="B", mathematical_expression="B", derivation_type=DerivationType.COMPUTATION, dependencies=["MISSING"])
    tree.add_node(b)

    res = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert res["structure_valid"] is False or res["mathematical_consistency"] is False


def test_validator_passes_simple_acyclic_tree():
    a = DerivationNode(node_id="A", mathematical_expression="A", derivation_type=DerivationType.AXIOM)
    tree = ProvenanceTree(root_node=a)
    b = DerivationNode(node_id="B", mathematical_expression="B", derivation_type=DerivationType.COMPUTATION, dependencies=["A"])
    c = DerivationNode(node_id="C", mathematical_expression="C", derivation_type=DerivationType.THEOREM, dependencies=["B"])
    tree.add_node(b)
    tree.add_node(c)

    res = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert all(res.values())
