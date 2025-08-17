#!/usr/bin/env python3
"""
Team 2 Utils Finalization: Implementation Loop
Target: utils/implementation_loop.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from utils.implementation_loop import ImplementationLoop, LoopStatus, LoopStep, ContaminationError

class TestImplementationLoopFinalization:
    """
    Finalization tests for the implementation loop module.
    """

    def setup_method(self):
        """Set up the test environment."""
        self.loop = ImplementationLoop()

    def test_initialization(self):
        """Verify the loop initializes correctly."""
        assert self.loop.current_step is None
        assert len(self.loop.loop_history) == 0

    @patch('utils.implementation_loop.ImplementationLoop._execute_single_atomic_step')
    @patch('utils.implementation_loop.ImplementationLoop._capture_provenance')
    @patch('utils.implementation_loop.ImplementationLoop._test_ex_nihilo_integrity')
    def test_execute_implementation_loop_success(self, mock_test, mock_provenance, mock_execute):
        """Test the full implementation loop with a successful execution."""
        mock_execute.return_value = "result"
        mock_provenance.return_value = {"provenance": "data"}
        
        step_info = {"operation": "test_op"}
        result = self.loop.execute_implementation_loop(step_info)

        assert result["result"] == "result"
        assert result["next_step_ready"] is True
        assert len(self.loop.loop_history) == 1
        assert self.loop.loop_history[0].status == LoopStatus.COMPLETED

    @patch('utils.implementation_loop.ANTI_CONTAMINATION.scan_for_contamination', side_effect=ContaminationError("Contaminated"))
    def test_execute_implementation_loop_contamination(self, mock_scan):
        """Test the implementation loop when contamination is detected."""
        step_info = {"operation": "test_op"}
        with pytest.raises(ContaminationError):
            self.loop.execute_implementation_loop(step_info)
        
        assert len(self.loop.loop_history) == 1
        assert self.loop.loop_history[0].status == LoopStatus.CONTAMINATED

    def test_perform_mathematical_operation(self):
        """Test the internal mathematical operation performer."""
        result_phi = self.loop._perform_mathematical_operation("phi_op", {})
        assert result_phi > 1.6

        result_grace = self.loop._perform_mathematical_operation("grace_op", {})
        assert result_grace > 1.6

    def test_get_loop_summary(self):
        """Test the loop summary generation."""
        # Manually add a history record for testing
        mock_result = MagicMock()
        mock_result.status = LoopStatus.COMPLETED
        mock_result.contamination_detected = False
        self.loop.loop_history.append(mock_result)
        
        summary = self.loop.get_loop_summary()
        assert summary["total_steps"] == 1
        assert summary["success_rate"] == 1.0
