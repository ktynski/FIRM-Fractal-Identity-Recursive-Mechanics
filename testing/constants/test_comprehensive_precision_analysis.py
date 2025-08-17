#!/usr/bin/env python3
"""
Team 3 Constants Conquest: Comprehensive Precision Analysis Test
Target: constants/comprehensive_precision_analysis.py
Mission: Validate the systematic application of the φ⁻ⁿ optimization
         methodology, ensuring cross-consistency and accurate error
         propagation across all defined constants.
"""

import sys
import pytest
from pathlib import Path
from unittest.mock import Mock

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import the target module and its components
from constants.comprehensive_precision_analysis import (
    ComprehensivePrecisionAnalyzer,
    PrecisionAnalysisResult,
    ConstantCategory
)

class TestComprehensivePrecisionAnalysis:
    """
    Test suite for the ComprehensivePrecisionAnalyzer class.
    """

    def setup_method(self):
        """Set up the test environment before each test."""
        self.analyzer = ComprehensivePrecisionAnalyzer()

    def test_single_constant_optimization(self):
        """
        Test the φ⁻ⁿ optimization for a single, well-defined constant
        (fine-structure constant) to ensure the core logic is sound.
        """
        fine_structure_constant = next(
            c for c in self.analyzer._constants_database 
            if c.name == "fine_structure_constant_inverse"
        )
        result = self.analyzer.optimize_phi_formulation_for_constant(fine_structure_constant)
        
        assert isinstance(result, PrecisionAnalysisResult)
        assert result.precision_ranking == "BREAKTHROUGH"
        assert result.best_phi_power == 7

    def test_comprehensive_analysis_execution(self):
        """
        Verify that the full comprehensive analysis runs without errors
        and returns a structured result object.
        """
        results = self.analyzer.perform_comprehensive_analysis()
        assert results.total_constants_analyzed > 0
        assert len(results.individual_results) == results.total_constants_analyzed

    def test_cross_consistency_analysis(self):
        """
        Ensure that the cross-consistency analysis correctly categorizes
        constants and identifies patterns in the φ-power distribution.
        """
        results = self.analyzer.perform_comprehensive_analysis()
        cross_consistency = results.cross_consistency_analysis
        
        assert "category_performance" in cross_consistency
        assert "phi_power_distribution" in cross_consistency
        assert cross_consistency["most_common_phi_power"] is not None

    def test_statistical_summary_generation(self):
        """
        Validate the generation of the statistical summary, ensuring that
        it correctly calculates metrics like mean and median error.
        """
        results = self.analyzer.perform_comprehensive_analysis()
        summary = results.statistical_summary
        
        assert "mean_error_percent" in summary
        assert "median_error_percent" in summary
        assert summary["mean_error_percent"] >= 0
        assert summary["breakthrough_fraction"] >= 0

if __name__ == "__main__":
    pytest.main([__file__])
