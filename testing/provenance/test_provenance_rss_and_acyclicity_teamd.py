from provenance.derivation_tree import (
    DerivationNode,
    ProvenanceTree,
    DerivationType,
    ProvenanceValidator,
)


def test_provenance_rss_error_and_acyclicity():
    # Build minimal tree: Axiom -> Theorem -> Target
    ax = DerivationNode(
        node_id="A",
        mathematical_expression="Axiom A",
        derivation_type=DerivationType.AXIOM,
        numerical_value=None,
    )
    th = DerivationNode(
        node_id="T",
        mathematical_expression="Theorem from A",
        derivation_type=DerivationType.THEOREM,
        dependencies=["A"],
        numerical_value=1.0,
        error_bounds={"relative_error": 1e-6},
    )
    tg = DerivationNode(
        node_id="G",
        mathematical_expression="Target from T",
        derivation_type=DerivationType.TARGET,
        dependencies=["T"],
        numerical_value=2.0,
    )

    tree = ProvenanceTree(ax)
    tree.add_node(th)
    tree.add_node(tg)

    # Error propagation uses RSS; here should equal dependency relative error on G
    errs = tree.compute_error_propagation()
    assert "G" in errs
    assert abs(errs["G"]["relative_error"] - 1e-6) < 1e-12
    assert errs["G"]["absolute_error"] == abs(2.0 * 1e-6)

    # Structure valid and acyclic
    validator = ProvenanceValidator(strict_mode=True)
    res = validator.validate_tree(tree)
    assert res["structure_valid"] is True
    assert res["provenance_complete"] is True
    assert res["contamination_free"] is True
