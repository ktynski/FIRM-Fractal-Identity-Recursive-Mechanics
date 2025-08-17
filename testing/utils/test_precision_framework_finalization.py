#!/usr/bin/env python3
"""
Team 2 Utils Finalization: Precision Framework
Target: utils/precision_framework.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import decimal
import pytest

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from utils.precision_framework import PrecisionFramework, PrecisionType, ErrorAnalysis, compute_with_precision, propagate_errors

class TestPrecisionFrameworkFinalization:
    """
    Finalization tests for the precision framework module.
    """

    def setup_method(self):
        """Set up the test environment."""
        self.framework = PrecisionFramework()

    def test_initialization(self):
        """Verify the framework initializes correctly."""
        assert self.framework.precision_requirements is not None
        assert "phi_power" in self.framework.precision_requirements

    def test_compute_with_precision_phi_power(self):
        """Test the compute_with_precision method with a phi_power operation."""
        result, error_analysis = self.framework.compute_with_precision("phi_power", 2)
        assert isinstance(result, decimal.Decimal)
        assert isinstance(error_analysis, ErrorAnalysis)
        assert result > 2.0 # phi^2 is approx 2.618

    def test_compute_with_precision_grace_operator(self):
        """Test the compute_with_precision method with a grace_operator operation."""
        result, error_analysis = self.framework.compute_with_precision("grace_operator", 1.0)
        assert isinstance(result, decimal.Decimal)
        # Should converge to phi
        assert abs(result - self.framework.high_precision_constants["phi"]) < 1e-50

    def test_propagate_errors_addition(self):
        """Test the error propagation for addition."""
        error = self.framework.propagate_errors("addition", [(1.0, 0.1), (2.0, 0.2)])
        import math
        assert abs(error - math.sqrt(0.1**2 + 0.2**2)) < 1e-9

    def test_convenience_functions(self):
        """Test the convenience functions."""
        with patch('utils.precision_framework.PRECISION_FRAMEWORK') as mock_framework:
            compute_with_precision("test_op", 1, 2)
            mock_framework.compute_with_precision.assert_called_once_with("test_op", 1, 2)
            
            propagate_errors("test_prop", [])
            mock_framework.propagate_errors.assert_called_once_with("test_prop", [])
