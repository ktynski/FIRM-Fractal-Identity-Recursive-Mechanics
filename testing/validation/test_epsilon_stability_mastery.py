#!/usr/bin/env python3
"""
Team 2 Validation Mastery: Epsilon Stability
Target: validation/epsilon_stability.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import json

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.epsilon_stability import (
    log_base_phi,
    load_candidate_l0_values,
    compute_epsilons_from_l0,
    S_epsilon,
    evaluate_candidates
)

class TestEpsilonStabilityMastery:
    """
    Mastery tests for the epsilon stability module.
    """

    def test_log_base_phi(self):
        """Test the log_base_phi function."""
        import math
        phi = (1 + math.sqrt(5)) / 2
        assert abs(log_base_phi(phi**2) - 2.0) < 1e-9
        assert abs(log_base_phi(1) - 0.0) < 1e-9

    @patch('validation.epsilon_stability.REGISTRY_PATH')
    def test_load_candidate_l0_values(self, mock_registry_path):
        """Test loading candidate l0 values from the registry."""
        mock_registry_data = {
            "pred1": {
                "prediction_type": "phi_geometric_candidates_complete",
                "predicted_values": {
                    "candidate_series": [
                        {"l0": 220.0},
                        {"l0": 356.0}
                    ]
                }
            }
        }
        mock_registry_path.exists.return_value = True
        mock_registry_path.read_text.return_value = json.dumps(mock_registry_data)
        
        l0_values = load_candidate_l0_values()
        assert l0_values == [220.0, 356.0]

    def test_compute_epsilons_from_l0(self):
        """Test computing epsilon values from l0."""
        l0_values = [220.0]
        pairs = compute_epsilons_from_l0(l0_values)
        assert len(pairs) == 1
        l0, epsilon = pairs[0]
        assert l0 == 220.0
        # Expected value of epsilon for l0=220.0
        assert abs(epsilon - (-1.4096)) < 1e-4

    @patch('validation.epsilon_stability.delta_kappa', return_value=1e-5)
    @patch('validation.epsilon_stability.delta_G', return_value=1e-8)
    @patch('validation.epsilon_stability.delta_C', return_value=0.1)
    def test_S_epsilon(self, mock_delta_C, mock_delta_G, mock_delta_kappa):
        """Test the S_epsilon stability functional."""
        result = S_epsilon(epsilon=0.0)
        assert "S" in result
        assert result["S"] > 0
        assert result["delta_kappa"] == 1e-5

    @patch('validation.epsilon_stability.load_candidate_l0_values')
    @patch('validation.epsilon_stability.S_epsilon')
    def test_evaluate_candidates(self, mock_S_epsilon, mock_load_l0):
        """Test the evaluation of candidates."""
        mock_load_l0.return_value = [220.0, 356.0]
        
        # Mock S_epsilon to return different values for different epsilons
        def S_side_effect(epsilon):
            if abs(epsilon - (-1.4096)) < 1e-4: # Corresponds to l0=220.0
                return {"S": 10.0, "epsilon": epsilon, "l0": 220.0}
            else: # Corresponds to l0=356.0
                return {"S": 5.0, "epsilon": epsilon, "l0": 356.0}

        mock_S_epsilon.side_effect = S_side_effect
        
        results = evaluate_candidates()
        
        assert len(results) == 2
        # Check that the results are sorted by S value
        assert results[0]["S"] == 5.0
        assert results[0]["l0"] == 356.0
        assert results[1]["S"] == 10.0
        assert results[1]["l0"] == 220.0
