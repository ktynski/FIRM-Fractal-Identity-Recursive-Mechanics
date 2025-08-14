import pytest

from provenance.derivation_tree import (
    DerivationNode,
    DerivationType,
    ProvenanceTree,
    PROVENANCE_VALIDATOR,
)


def _basic_tree():
    root = DerivationNode(
        node_id="root",
        mathematical_expression="target",
        derivation_type=DerivationType.TARGET,
        dependencies=["A1"],
    )
    tree = ProvenanceTree(root_node=root, target_result="R")
    tree.add_node(
        DerivationNode(
            node_id="A1",
            mathematical_expression="Axiom",
            derivation_type=DerivationType.AXIOM,
        )
    )
    return tree


def test_validator_happy_path():
    tree = _basic_tree()
    results = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert all(results.values())


def test_validator_detects_missing_dependency():
    root = DerivationNode(
        node_id="root",
        mathematical_expression="target",
        derivation_type=DerivationType.TARGET,
        dependencies=["MISSING"],
    )
    tree = ProvenanceTree(root_node=root, target_result="R")
    with pytest.raises(ValueError):
        tree._topological_sort()
    assert PROVENANCE_VALIDATOR._validate_tree_structure(tree) is False
