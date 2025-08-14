from provenance.derivation_tree import (
    DerivationNode,
    ProvenanceTree,
    DerivationType,
    ProvenanceValidator,
)


def test_provenance_validator_full_result_and_default_rss():
    # Build a small tree with a numeric leaf lacking explicit error_bounds
    ax = DerivationNode(
        node_id="A",
        mathematical_expression="A",
        derivation_type=DerivationType.AXIOM,
    )
    mid = DerivationNode(
        node_id="B",
        mathematical_expression="B",
        derivation_type=DerivationType.THEOREM,
        dependencies=["A"],
        numerical_value=3.0,
    )
    leaf = DerivationNode(
        node_id="C",
        mathematical_expression="C",
        derivation_type=DerivationType.TARGET,
        dependencies=["B"],
        numerical_value=6.0,
    )

    t = ProvenanceTree(ax)
    t.add_node(mid)
    t.add_node(leaf)

    # Default φ-derived minimal bound should apply for B and propagate to C
    errs = t.compute_error_propagation()
    assert "C" in errs and errs["C"]["relative_error"] > 0.0

    v = ProvenanceValidator(strict_mode=True)
    res = v.validate_tree(t)
    assert res["structure_valid"]
    assert res["provenance_complete"]
    assert res["contamination_free"]
    assert res["axiom_foundation_valid"]
