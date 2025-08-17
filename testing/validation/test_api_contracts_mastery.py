#!/usr/bin/env python3
"""
Team 2 Validation Mastery: API Contracts
Target: validation/api_contracts.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.api_contracts import (
    check_fine_structure_contract,
    check_mass_spectrum_contract,
    check_ex_nihilo_contract,
    run_api_contracts
)

class TestApiContractsMastery:
    """
    Mastery tests for the API contracts module.
    """

    @patch('validation.api_contracts.fine_alpha')
    def test_check_fine_structure_contract_valid(self, mock_fine_alpha):
        """Test the fine structure contract with a valid module."""
        mock_fine_alpha.FineStructureConstant.return_value.derive_alpha_inverse.return_value = 137.0
        violations = check_fine_structure_contract()
        assert len(violations) == 0

    @patch('validation.api_contracts.fine_alpha')
    def test_check_fine_structure_contract_invalid(self, mock_fine_alpha):
        """Test the fine structure contract with an invalid module."""
        del mock_fine_alpha.FineStructureConstant
        violations = check_fine_structure_contract()
        assert len(violations) > 0
        assert "missing" in violations[0].reason

    @patch('validation.api_contracts.mass_ratios')
    def test_check_mass_spectrum_contract_valid(self, mock_mass_ratios):
        """Test the mass spectrum contract with a valid module."""
        mock_mass_ratios.ParticleSpectrumAlgorithms.return_value.derive_complete_particle_spectrum.return_value = {}
        violations = check_mass_spectrum_contract()
        assert len(violations) == 0

    @patch('validation.api_contracts.en_pipeline')
    def test_check_ex_nihilo_contract_valid(self, mock_en_pipeline):
        """Test the ex nihilo contract with a valid module."""
        mock_en_pipeline.EX_NIHILO_PIPELINE.execute_complete_pipeline.return_value = {}
        violations = check_ex_nihilo_contract()
        assert len(violations) == 0

    @patch('validation.api_contracts.check_fine_structure_contract', return_value=[])
    @patch('validation.api_contracts.check_mass_spectrum_contract', return_value=[])
    @patch('validation.api_contracts.check_ex_nihilo_contract', return_value=[])
    @patch('validation.api_contracts.phi_mod')
    @patch('validation.api_contracts.precision_mod')
    def test_run_api_contracts_all_passing(self, mock_precision_mod, mock_phi_mod, mock_ex_nihilo, mock_mass_spectrum, mock_fine_structure):
        """Test the main runner function with all contracts passing."""
        mock_phi_mod.PHI_VALUE = 1.618
        mock_precision_mod.PRECISION_FRAMEWORK.compute_with_precision.return_value = 1.0
        report = run_api_contracts()
        assert report["status"] == "passed"
        assert report["total_violations"] == 0
