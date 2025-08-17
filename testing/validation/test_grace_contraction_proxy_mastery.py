#!/usr/bin/env python3
"""
Team 2 Validation Mastery: Grace Contraction Proxy
Target: validation/grace_contraction_proxy.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.grace_contraction_proxy import compute_contraction_residual

class TestGraceContractionProxyMastery:
    """
    Mastery tests for the grace contraction proxy module.
    """

    def test_compute_contraction_residual_zero(self):
        """Test the contraction residual computation with a value of k that should yield zero residual."""
        import math
        phi = (1 + 5**0.5) / 2
        k_value = 12 + 1/phi # This is the theoretical fixed point
        rho, delta_g = compute_contraction_residual(k_value)
        assert abs(delta_g) < 1e-2

    def test_compute_contraction_residual_nonzero(self):
        """Test the contraction residual computation with a value of k that should yield non-zero residual."""
        k_value = 10.0
        rho, delta_g = compute_contraction_residual(k_value)
        assert abs(delta_g) > 1e-9

    def test_rho_value(self):
        """Test that the rho value is computed correctly."""
        k_value = 12.0
        rho, delta_g = compute_contraction_residual(k_value)
        # Based on the formula in the function
        import math
        phi = (1 + 5**0.5) / 2
        expected_rho = math.sin(2 * math.pi * k_value)
        assert abs(rho - expected_rho) < 1e-9
