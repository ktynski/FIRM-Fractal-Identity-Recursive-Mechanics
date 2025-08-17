#!/usr/bin/env python3
"""
Team 2 Validation Mastery: Rigorous Statistical Analysis
Target: validation/rigorous_statistical_analysis.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import numpy as np

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.rigorous_statistical_analysis import RigorousStatisticalAnalyzer, StatisticalTest, StatisticalResult, MultipleTestingResult

class TestRigorousStatisticalAnalysisMastery:
    """
    Mastery tests for the rigorous statistical analysis module.
    """

    def setup_method(self):
        """Set up the test environment."""
        self.analyzer = RigorousStatisticalAnalyzer()

    def test_initialization(self):
        """Verify the analyzer initializes correctly."""
        assert self.analyzer._phi is not None
        assert 'fine_structure_inv' in self.analyzer._experimental_constants
        assert 'fine_structure_inv' in self.analyzer._firm_predictions

    def test_analyze_fine_structure_significance(self):
        """Test the analysis of the fine structure constant significance."""
        result = self.analyzer.analyze_fine_structure_significance()
        assert isinstance(result, StatisticalResult)
        assert result.p_value < 0.05
        assert result.effect_size > 1.0

    @patch('numpy.random.uniform')
    def test_monte_carlo_null_hypothesis_test(self, mock_uniform):
        """Test the Monte Carlo null hypothesis test."""
        # Mock random uniform to control the outcome
        mock_uniform.return_value = self.analyzer._firm_predictions['fine_structure_inv']
        result = self.analyzer.monte_carlo_null_hypothesis_test(n_simulations=10)
        assert result['null_hypothesis_p_value'] == 1.0 # All randoms are perfect matches

    def test_multiple_testing_correction_analysis(self):
        """Test the multiple testing correction analysis."""
        result = self.analyzer.multiple_testing_correction_analysis()
        assert isinstance(result, MultipleTestingResult)
        assert result.total_tests > 0
        assert result.significant_before_correction >= result.significant_after_bonferroni

    def test_selection_bias_quantification(self):
        """Test the selection bias quantification."""
        result = self.analyzer.selection_bias_quantification()
        assert 'systematic_phi_exploration' in result
        assert result['systematic_phi_exploration']['best_phi_power'] == -7

    def test_power_analysis_precision_requirements(self):
        """Test the power analysis for precision requirements."""
        result = self.analyzer.power_analysis_precision_requirements()
        assert 'fine_structure_power_analysis' in result
        assert result['current_statistical_power'] > 0.8
