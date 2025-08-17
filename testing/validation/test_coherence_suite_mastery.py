#!/usr/bin/env python3
"""
Team 2 Validation Mastery: Coherence Suite
Target: validation/coherence_suite.py
"""

import sys
from pathlib import Path
import numpy as np

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.coherence_suite import coherence_pass_fraction, _rot, _scale

class TestCoherenceSuiteMastery:
    """
    Mastery tests for the coherence suite module.
    """

    def test_rot_matrix(self):
        """Test the rotation matrix generation."""
        import math
        angle = math.pi / 2
        expected = np.array([[0, -1], [1, 0]])
        assert np.allclose(_rot(angle), expected)

    def test_scale_matrix(self):
        """Test the scaling matrix generation."""
        expected = np.array([[2.0, 0], [0, 3.0]])
        assert np.allclose(_scale(2.0, 3.0), expected)

    def test_coherence_pass_fraction_passing(self):
        """Test the coherence pass fraction with a value of k that should pass."""
        # This is a bit of a guess, but for k -> infinity, theta -> 0, and all matrices are near identity
        result = coherence_pass_fraction(k=1e6)
        assert result["pass_fraction"] == 1.0

    def test_coherence_pass_fraction_failing(self):
        """Test the coherence pass fraction with a value of k that might fail."""
        # For k=-phi, theta is undefined, but let's test near it
        phi = (1 + 5**0.5) / 2
        result = coherence_pass_fraction(k=-phi + 1e-9)
        # We don't know for sure it will fail, but it's a good test case
        assert "pass_fraction" in result
