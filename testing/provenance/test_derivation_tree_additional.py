from provenance.derivation_tree import (
    DerivationNode,
    DerivationType,
    ProvenanceTree,
    PROVENANCE_VALIDATOR,
)


def test_derivation_tree_detects_cycle_and_reports_invalid_structure():
    ax = DerivationNode(
        node_id="A",
        mathematical_expression="A𝒢.1",
        derivation_type=DerivationType.AXIOM,
    )
    n1 = DerivationNode(
        node_id="N1",
        mathematical_expression="T1",
        derivation_type=DerivationType.THEOREM,
        dependencies=["A", "N2"],  # forward ref to form a cycle with N2
    )
    n2 = DerivationNode(
        node_id="N2",
        mathematical_expression="T2",
        derivation_type=DerivationType.THEOREM,
        dependencies=["N1"],
    )

    tree = ProvenanceTree(ax, "Target")
    tree.add_node(n1)
    tree.add_node(n2)

    results = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert results["structure_valid"] is False  # cycle makes topo sort fail


def test_derivation_tree_complete_provenance_happy_path():
    ax = DerivationNode(
        node_id="A",
        mathematical_expression="A𝒢.2",
        derivation_type=DerivationType.AXIOM,
    )
    d1 = DerivationNode(
        node_id="D1",
        mathematical_expression="Def1",
        derivation_type=DerivationType.DEFINITION,
        dependencies=["A"],
    )
    t1 = DerivationNode(
        node_id="T1",
        mathematical_expression="Thm1",
        derivation_type=DerivationType.THEOREM,
        dependencies=["D1"],
    )

    tree = ProvenanceTree(ax, "Target")
    tree.add_node(d1)
    tree.add_node(t1)

    results = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert results["structure_valid"] is True
    assert results["provenance_complete"] is True
    assert results["axiom_foundation_valid"] is True

from provenance.derivation_tree import DerivationNode, DerivationType, ProvenanceTree


def test_build_and_trace_derivation_tree():
    # Axioms
    ax1 = DerivationNode(node_id="A1", mathematical_expression="A𝒢.1", derivation_type=DerivationType.AXIOM)
    ax2 = DerivationNode(node_id="A2", mathematical_expression="A𝒢.2", derivation_type=DerivationType.AXIOM)

    # Intermediate theorem depends on A1
    th1 = DerivationNode(node_id="T1", mathematical_expression="Theorem 1", derivation_type=DerivationType.THEOREM, dependencies=["A1"])

    # Target depends on theorem and A2
    target = DerivationNode(
        node_id="R1",
        mathematical_expression="Result",
        derivation_type=DerivationType.TARGET,
        dependencies=["T1", "A2"],
    )

    tree = ProvenanceTree(root_node=ax1, nodes={})
    tree.add_node(ax2)
    tree.add_node(th1)
    tree.add_node(target)

    # Tracing
    paths = tree.trace_to_axioms("R1")
    assert paths and all(path[-1] in ("A1", "A2") for path in paths)

    # Complete provenance
    assert tree.verify_complete_provenance() is True

    # No contamination expected
    assert tree.detect_contamination() == []
