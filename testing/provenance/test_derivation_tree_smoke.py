from provenance.derivation_tree import DerivationNode, DerivationType, ProvenanceTree


def test_derivation_tree_basic_properties():
    a = DerivationNode("a", "1", derivation_type=DerivationType.AXIOM)
    b = DerivationNode("b", "a->b", dependencies=["a"], derivation_type=DerivationType.THEOREM)
    c = DerivationNode("c", "b->c", dependencies=["b"], derivation_type=DerivationType.TARGET)
    tree = ProvenanceTree(root_node=a)
    tree.add_node(b)
    tree.add_node(c)
    topo = tree._topological_sort()
    assert topo[0] == "a"
    assert topo[-1] == "c"
    depth = tree._compute_max_depth()
    assert depth >= 2
