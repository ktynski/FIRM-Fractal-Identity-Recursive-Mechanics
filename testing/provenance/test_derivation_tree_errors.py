import pytest

from provenance.derivation_tree import DerivationNode, DerivationType, ProvenanceTree


def test_topological_sort_missing_dependency_raises():
    root = DerivationNode(node_id="R", mathematical_expression="target", derivation_type=DerivationType.TARGET, dependencies=["X"])
    tree = ProvenanceTree(root_node=root, target_result="T")
    with pytest.raises(ValueError):
        tree._topological_sort()


def test_cycle_detection_in_depth_computation():
    # Build two nodes with cyclic dependency
    a = DerivationNode(node_id="A", mathematical_expression="A", derivation_type=DerivationType.THEOREM, dependencies=["B"])
    b = DerivationNode(node_id="B", mathematical_expression="B", derivation_type=DerivationType.THEOREM, dependencies=["A"])
    tree = ProvenanceTree(root_node=a, target_result="T")
    tree.add_node(b)
    with pytest.raises(ValueError):
        tree._compute_max_depth()
