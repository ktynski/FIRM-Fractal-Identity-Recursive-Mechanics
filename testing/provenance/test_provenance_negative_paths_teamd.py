import pytest
from provenance.derivation_tree import DerivationNode, ProvenanceTree, DerivationType


def test_provenance_missing_dependency_raises():
    ax = DerivationNode(
        node_id="A",
        mathematical_expression="Axiom A",
        derivation_type=DerivationType.AXIOM,
    )
    bad = DerivationNode(
        node_id="B",
        mathematical_expression="Depends on missing",
        derivation_type=DerivationType.THEOREM,
        dependencies=["NONEXISTENT"],
    )
    tree = ProvenanceTree(ax)
    tree.add_node(bad)
    with pytest.raises(ValueError):
        tree._topological_sort()


def test_provenance_cycle_detection_raises():
    a = DerivationNode("A", "A", derivation_type=DerivationType.THEOREM, dependencies=["C"])  # type: ignore[arg-type]
    b = DerivationNode("B", "B", derivation_type=DerivationType.THEOREM, dependencies=["A"])  # type: ignore[arg-type]
    c = DerivationNode("C", "C", derivation_type=DerivationType.THEOREM, dependencies=["B"])  # type: ignore[arg-type]
    tree = ProvenanceTree(a)
    tree.add_node(b)
    tree.add_node(c)
    with pytest.raises(ValueError):
        tree._topological_sort()
