from provenance.derivation_tree import DerivationNode, DerivationType, ProvenanceTree, PROVENANCE_VALIDATOR


def test_provenance_tree_basic_paths_and_report():
    ax = DerivationNode(
        node_id="A1",
        mathematical_expression="Axiom: A𝒢.1",
        derivation_type=DerivationType.AXIOM,
        justification="Foundational axiom",
    )
    b = DerivationNode(
        node_id="B1",
        mathematical_expression="Definition from A1",
        derivation_type=DerivationType.DEFINITION,
        dependencies=["A1"],
    )
    c = DerivationNode(
        node_id="C1",
        mathematical_expression="Theorem using B1",
        derivation_type=DerivationType.THEOREM,
        dependencies=["B1"],
        numerical_value=1.0,
    )
    tree = ProvenanceTree(root_node=ax)
    tree.add_node(b)
    tree.add_node(c)
    # Paths should trace to axioms
    paths = tree.trace_to_axioms("C1")
    assert paths and paths[0][-1] == "A1"
    # Validator basic checks
    res = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert res["structure_valid"] and res["provenance_complete"] and res["axiom_foundation_valid"]
    # Report shape
    report = tree.generate_audit_report()
    assert isinstance(report, dict) and "audit_metadata" in report and "integrity_verification" in report
