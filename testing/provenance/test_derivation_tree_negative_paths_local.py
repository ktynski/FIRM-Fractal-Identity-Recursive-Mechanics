import pytest
from provenance.derivation_tree import DerivationNode, DerivationType, ProvenanceTree


def test_topological_sort_detects_cycle_and_missing_dep():
    a = DerivationNode(node_id="A", mathematical_expression="axiom", derivation_type=DerivationType.AXIOM)
    b = DerivationNode(node_id="B", mathematical_expression="uses A", dependencies=["A"])
    c = DerivationNode(node_id="C", mathematical_expression="uses D", dependencies=["D"])  # missing dep
    tree = ProvenanceTree(root_node=a)
    tree.add_node(b)
    tree.add_node(c)
    with pytest.raises(ValueError):
        tree._topological_sort()
    # Create a cycle explicitly with two nodes X<->Y
    x = DerivationNode(node_id="X", mathematical_expression="depends on Y", dependencies=["Y"])
    y = DerivationNode(node_id="Y", mathematical_expression="depends on X", dependencies=["X"])
    tree2 = ProvenanceTree(root_node=a)
    tree2.add_node(x)
    tree2.add_node(y)
    with pytest.raises(ValueError):
        tree2._topological_sort()

