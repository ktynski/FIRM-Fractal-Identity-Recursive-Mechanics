"""Test missing branches in api_contracts.py to boost coverage."""

import pytest
from unittest.mock import Mock, patch
from validation.api_contracts import (
    check_fine_structure_contract,
    check_mass_spectrum_contract,
    check_ex_nihilo_contract,
    run_api_contracts
)

def test_fine_structure_missing_class():
    """Test fine structure contract when FineStructureConstant class is missing."""
    with patch('validation.api_contracts.fine_alpha') as mock_alpha:
        # Remove the class to trigger missing violation
        delattr(mock_alpha, 'FineStructureConstant') if hasattr(mock_alpha, 'FineStructureConstant') else None
        mock_alpha.FineStructureConstant = None
        del mock_alpha.FineStructureConstant

        violations = check_fine_structure_contract()

        assert len(violations) >= 1
        assert any('missing' in v.reason for v in violations)

def test_fine_structure_missing_methods():
    """Test fine structure contract when required methods are missing."""
    with patch('validation.api_contracts.fine_alpha') as mock_alpha:
        # Create mock class without required methods
        mock_class = Mock()
        mock_instance = Mock()
        mock_instance.derive_alpha_inverse = None
        mock_instance.alpha_inverse_pure = None
        mock_instance.derive_alternative_phi_expression = None
        mock_instance.build_complete_provenance = None

        # Remove methods to make them non-callable
        del mock_instance.derive_alpha_inverse
        del mock_instance.alpha_inverse_pure
        del mock_instance.derive_alternative_phi_expression
        del mock_instance.build_complete_provenance

        mock_class.return_value = mock_instance
        mock_alpha.FineStructureConstant = mock_class

        violations = check_fine_structure_contract()

        # Should have violations for missing methods
        assert len(violations) >= 2
        assert any('missing_method' in v.reason for v in violations)

def test_mass_spectrum_missing_class():
    """Test mass spectrum contract when ParticleSpectrumAlgorithms class is missing."""
    with patch('validation.api_contracts.mass_ratios') as mock_mass:
        del mock_mass.ParticleSpectrumAlgorithms

        violations = check_mass_spectrum_contract()

        assert len(violations) >= 1
        assert any('missing' in v.reason for v in violations)

def test_ex_nihilo_missing_singleton():
    """Test ex nihilo contract when EX_NIHILO_PIPELINE is missing."""
    with patch('validation.api_contracts.en_pipeline') as mock_pipeline:
        del mock_pipeline.EX_NIHILO_PIPELINE

        violations = check_ex_nihilo_contract()

        assert len(violations) >= 1
        assert any('missing' in v.reason for v in violations)

def test_run_api_contracts_phi_value_missing():
    """Test run_api_contracts when PHI_VALUE is missing."""
    with patch('validation.api_contracts.phi_mod') as mock_phi:
        del mock_phi.PHI_VALUE

        result = run_api_contracts()

        assert result['status'] == 'failed'
        assert result['total_violations'] > 0
        violations = result['violations']['centralized_constants']
        assert len(violations) >= 1

def test_run_api_contracts_phi_value_out_of_range():
    """Test run_api_contracts when PHI_VALUE is out of range."""
    with patch('validation.api_contracts.phi_mod') as mock_phi:
        mock_phi.PHI_VALUE = 3.0  # Out of (1,2) range

        result = run_api_contracts()

        violations = result['violations']['centralized_constants']
        assert any('range' in v['reason'] for v in violations)

def test_run_api_contracts_phi_value_non_numeric():
    """Test run_api_contracts when PHI_VALUE is non-numeric."""
    with patch('validation.api_contracts.phi_mod') as mock_phi:
        mock_phi.PHI_VALUE = "not_a_number"

        result = run_api_contracts()

        violations = result['violations']['centralized_constants']
        assert any('type' in v['reason'] for v in violations)

def test_run_api_contracts_precision_framework_missing():
    """Test run_api_contracts when PRECISION_FRAMEWORK is missing."""
    with patch('validation.api_contracts.precision_mod') as mock_precision:
        del mock_precision.PRECISION_FRAMEWORK

        result = run_api_contracts()

        violations = result['violations']['centralized_constants']
        assert any('missing' in v['reason'] for v in violations)