#!/usr/bin/env python3
"""
Team 2 Validation Mastery: Independent Verification
Target: validation/independent_verification.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.independent_verification import (
    EnvironmentSnapshot,
    verify_fine_structure,
    verify_mass_spectrum_summary,
    verify_ex_nihilo_pipeline,
    run_independent_verification
)

class TestIndependentVerificationMastery:
    """
    Mastery tests for the independent verification module.
    """

    @patch('platform.python_version', return_value='3.12.7 (main, Oct 30 2024, 17:52:10) [Clang 13.1.6 (clang-1316.0.21.2.5)]')
    @patch('platform.platform', return_value='macOS')
    def test_environment_snapshot(self, mock_platform, mock_version):
        """Test the environment snapshot creation."""
        snapshot = EnvironmentSnapshot.capture()
        assert snapshot.python_version == '3.12.7 (main, Oct 30 2024, 17:52:10) [Clang 13.1.6 (clang-1316.0.21.2.5)]'
        assert snapshot.platform == 'macOS'
        assert snapshot.timestamp_utc is not None

    @patch('validation.independent_verification.FineStructureAlpha')
    def test_verify_fine_structure(self, MockFineStructureAlpha):
        """Test the fine structure constant verification."""
        mock_alpha = MagicMock()
        mock_alpha.derive_alpha_inverse.return_value.value = 137.036
        MockFineStructureAlpha.return_value = mock_alpha

        result = verify_fine_structure()
        assert result['quantity'] == 'alpha_inverse'
        assert result['value'] == 137.036
        assert 'hash' in result

    @patch('validation.independent_verification.ParticleSpectrumAlgorithms')
    def test_verify_mass_spectrum_summary(self, MockParticleSpectrum):
        """Test the mass spectrum summary verification."""
        mock_spectrum = MagicMock()
        mock_spectrum.derive_complete_particle_spectrum.return_value = {"electron": 0.511}
        MockParticleSpectrum.return_value = mock_spectrum

        summary = verify_mass_spectrum_summary()
        assert "electron" in summary['spectrum_compact']
        assert summary['spectrum_compact']['electron'] == 0.511
        assert 'hash' in summary

    @patch('validation.independent_verification.EX_NIHILO_PIPELINE')
    def test_verify_ex_nihilo_pipeline(self, MockPipeline):
        """Test the Ex Nihilo pipeline verification."""
        mock_result = MagicMock()
        mock_result.verify_complete_integrity.return_value = True
        mock_result.total_stages_completed = 5
        mock_result.pipeline_successful = True
        mock_result.final_universe_parameters = {}
        mock_result.cmb_predictions = {}
        MockPipeline.execute_complete_pipeline.return_value = mock_result
        
        summary = verify_ex_nihilo_pipeline()
        assert summary['pipeline_successful'] is True
        assert summary['cryptographic_integrity'] is True
        assert 'hash' in summary

    @patch('validation.independent_verification.verify_ex_nihilo_pipeline')
    @patch('validation.independent_verification.verify_mass_spectrum_summary')
    @patch('validation.independent_verification.verify_fine_structure')
    def test_run_independent_verification(self, mock_fine, mock_mass, mock_ex):
        """Test the main independent verification runner."""
        mock_fine.return_value = {'hash': 'hash_alpha'}
        mock_mass.return_value = {'hash': 'hash_mass'}
        mock_ex.return_value = {'hash': 'hash_ex'}

        report = run_independent_verification(canonical_hashes=None)
        
        assert report['overall_status'] == 'passed'
        assert 'alpha_inverse' in report['results']
        
        # Test with canonical hashes
        canonical = {
            'alpha_inverse': 'hash_alpha',
            'mass_spectrum': 'hash_mass_mismatch',
            'ex_nihilo_pipeline': 'hash_ex'
        }
        report_mismatch = run_independent_verification(canonical_hashes=canonical)
        assert report_mismatch['overall_status'] == 'mismatch'
        assert report_mismatch['comparisons']['mass_spectrum']['match'] is False
