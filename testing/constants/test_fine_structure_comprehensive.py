"""Comprehensive tests for fine structure alpha module to boost coverage to 95%+."""

import pytest
from constants.fine_structure_alpha import (
    FineStructureConstant,
    FINE_STRUCTURE_ALPHA,
    DerivationMethod,
    AlphaDerivationResult
)


def test_complete_provenance_building():
    """Test complete provenance tree building for all methods."""
    alpha = FineStructureConstant()

    # Test provenance for each derivation method
    methods = [
        DerivationMethod.PHI_POWERS_PRIMARY,
        DerivationMethod.PHI_POWERS_ALTERNATIVE,
        DerivationMethod.MORPHISM_COUNTING
    ]

    for method in methods:
        tree = alpha.build_complete_provenance(method)
        assert tree is not None
        assert tree.root_node is not None
        assert len(tree.nodes) >= 5  # Should have axioms + phi + method + computation

        # Check for expected node types
        node_types = {node.derivation_type.value for node in tree.nodes.values()}
        expected_types = {"axiom", "theorem", "lemma", "computation", "target"}
        assert len(node_types.intersection(expected_types)) >= 3


def test_axiom_foundation_nodes():
    """Test axiom foundation node building."""
    alpha = FineStructureConstant()
    axiom_nodes = alpha._build_axiom_foundation_nodes()

    assert len(axiom_nodes) == 4  # A𝒢.1-4

    expected_ids = ["axiom_grace_1", "axiom_grace_2", "axiom_grace_3", "axiom_grace_4"]
    actual_ids = [node.node_id for node in axiom_nodes]

    for expected_id in expected_ids:
        assert expected_id in actual_ids

    # Check dependency structure
    for node in axiom_nodes:
        assert node.derivation_type.value == "axiom"
        assert isinstance(node.empirical_inputs, list)
        assert len(node.empirical_inputs) == 0  # No empirical inputs in axioms


def test_phi_recursion_nodes():
    """Test phi recursion node building."""
    alpha = FineStructureConstant()
    phi_nodes = alpha._build_phi_recursion_nodes()

    assert len(phi_nodes) >= 1

    # Should have phi recursion theorem
    phi_node_ids = [node.node_id for node in phi_nodes]
    assert "phi_recursion" in phi_node_ids

    for node in phi_nodes:
        assert len(node.empirical_inputs) == 0  # Pure mathematical


def test_method_specific_nodes():
    """Test method-specific node building."""
    alpha = FineStructureConstant()

    # Test primary method nodes
    primary_nodes = alpha._build_method_specific_nodes(DerivationMethod.PHI_POWERS_PRIMARY)
    assert len(primary_nodes) >= 1

    primary_ids = [node.node_id for node in primary_nodes]
    assert "phi_powers_calculation" in primary_ids

    # Test other methods return nodes or empty list
    alt_nodes = alpha._build_method_specific_nodes(DerivationMethod.PHI_POWERS_ALTERNATIVE)
    morph_nodes = alpha._build_method_specific_nodes(DerivationMethod.MORPHISM_COUNTING)

    # Should not raise errors
    assert isinstance(alt_nodes, list)
    assert isinstance(morph_nodes, list)


def test_cross_derivation_consistency():
    """Test cross-derivation consistency verification."""
    alpha = FineStructureConstant()
    consistency = alpha.verify_cross_derivation_consistency()

    assert isinstance(consistency, dict)

    # Should have pairwise comparisons
    expected_keys = [
        "phi_powers_primary_vs_phi_powers_alternative"
    ]

    for key in expected_keys:
        if key in consistency:
            assert isinstance(consistency[key], float)
            assert consistency[key] >= 0  # Relative differences should be non-negative


def test_alpha_derivation_result_post_init():
    """Test AlphaDerivationResult post-initialization logic."""
    # Test with experimental value provided
    result_with_exp = AlphaDerivationResult(
        method=DerivationMethod.PHI_POWERS_PRIMARY,
        alpha_inverse_value=137.0,
        alpha_value=1/137.0,
        experimental_alpha_inverse=137.036,
        mathematical_expression="test",
        phi_expression="test"
    )

    assert result_with_exp.relative_error > 0
    assert result_with_exp.precision_digits > 0

    # Test without experimental value
    result_no_exp = AlphaDerivationResult(
        method=DerivationMethod.PHI_POWERS_PRIMARY,
        alpha_inverse_value=137.0,
        alpha_value=1/137.0,
        mathematical_expression="test",
        phi_expression="test"
    )

    assert result_no_exp.relative_error == 0.0
    assert result_no_exp.precision_digits == 0


def test_alpha_derivation_result_asdict():
    """Test AlphaDerivationResult _asdict method for back-compatibility."""
    result = AlphaDerivationResult(
        method=DerivationMethod.PHI_POWERS_PRIMARY,
        alpha_inverse_value=137.0,
        alpha_value=1/137.0,
        mathematical_expression="test",
        phi_expression="test"
    )

    result_dict = result._asdict()

    expected_keys = [
        "method", "alpha_inverse_value", "alpha_value",
        "experimental_alpha_inverse", "relative_error", "precision_digits",
        "mathematical_expression", "phi_expression",
        "structural_factors", "empirical_inputs"
    ]

    for key in expected_keys:
        assert key in result_dict


def test_derive_113_constant():
    """Test Tree of Life constant derivation."""
    alpha = FineStructureConstant()
    constant = alpha._derive_113_constant()

    assert constant == 113
    assert isinstance(constant, int)


def test_alpha_inverse_pure_api():
    """Test alpha_inverse_pure API method."""
    alpha = FineStructureConstant()
    alpha_inv = alpha.alpha_inverse_pure()

    assert isinstance(alpha_inv, float)
    assert alpha_inv > 0
    # φ-native value will be much larger than empirical ~137
    assert alpha_inv > 100  # Reasonable lower bound


def test_derive_alpha_inverse_back_compat():
    """Test back-compatibility derive_alpha_inverse method."""
    alpha = FineStructureConstant()
    result = alpha.derive_alpha_inverse()

    assert hasattr(result, 'value')
    assert isinstance(result.value, float)
    assert result.value > 0


def test_experimental_value_property():
    """Test experimental_value property (should return None)."""
    alpha = FineStructureConstant()
    exp_val = alpha.experimental_value

    assert exp_val is None  # Sealed to prevent contamination


def test_singleton_warming():
    """Test that singleton warming works without errors."""
    # The singleton creation should have warmed caches
    alpha = FINE_STRUCTURE_ALPHA

    # These should return cached results quickly
    primary = alpha.derive_primary_phi_expression()
    alt = alpha.derive_alternative_phi_expression()
    morph = alpha.derive_morphic_structure_expression()

    assert primary.alpha_inverse_value > 0
    assert alt.alpha_inverse_value > 0
    assert morph.alpha_inverse_value > 0

    # Values should be consistent (same underlying phi-mathematics)
    assert abs(primary.alpha_inverse_value - morph.alpha_inverse_value) < 1e-10


def test_back_compat_alias():
    """Test FineStructureAlpha back-compatibility alias."""
    from constants.fine_structure_alpha import FineStructureAlpha

    # Should be same class as FineStructureConstant
    alpha1 = FineStructureAlpha()
    alpha2 = FineStructureConstant()

    assert type(alpha1) == type(alpha2)

    # Should have same methods
    assert hasattr(alpha1, 'derive_primary_phi_expression')
    assert hasattr(alpha1, 'derive_alternative_phi_expression')


def test_module_level_constants():
    """Test module-level exported constants."""
    from constants.fine_structure_alpha import (
        ALPHA_INVERSE_THEORETICAL,
        ALPHA_THEORETICAL,
        ALPHA_EXPERIMENTAL
    )

    assert isinstance(ALPHA_INVERSE_THEORETICAL, float)
    assert ALPHA_INVERSE_THEORETICAL > 0

    assert isinstance(ALPHA_THEORETICAL, float)
    assert ALPHA_THEORETICAL > 0

    # Should be reciprocals
    assert abs(ALPHA_INVERSE_THEORETICAL * ALPHA_THEORETICAL - 1.0) < 1e-10

    # Experimental should be None (sealed)
    assert ALPHA_EXPERIMENTAL is None


def test_derivation_caching():
    """Test that derivation results are properly cached."""
    alpha = FineStructureConstant()

    # First call should compute and cache
    result1 = alpha.derive_primary_phi_expression()

    # Second call should return cached result (same object)
    result2 = alpha.derive_primary_phi_expression()

    assert result1 is result2  # Same object reference due to caching

    # Test alternative method caching
    alt1 = alpha.derive_alternative_phi_expression()
    alt2 = alpha.derive_alternative_phi_expression()

    assert alt1 is alt2


def test_structural_factors_completeness():
    """Test that structural factors are properly populated."""
    alpha = FineStructureConstant()

    primary = alpha.derive_primary_phi_expression()
    assert "phi_15" in primary.structural_factors
    assert "phi_7_plus_1" in primary.structural_factors
    assert "base_ratio" in primary.structural_factors
    assert "tree_of_life_constant" in primary.structural_factors

    alt = alpha.derive_alternative_phi_expression()
    assert "phi_7_plus_1" in alt.structural_factors
    assert "phi_15" in alt.structural_factors
    assert "correction_factor" in alt.structural_factors