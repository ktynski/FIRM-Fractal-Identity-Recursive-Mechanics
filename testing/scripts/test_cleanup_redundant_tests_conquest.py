#!/usr/bin/env python3
"""
Team 2 Scripts Conquest: Cleanup Redundant Tests
Target: scripts/cleanup_redundant_tests.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock, call

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.cleanup_redundant_tests import find_redundant_tests, determine_files_to_remove, cleanup_redundant_tests

class TestCleanupRedundantTestsConquest:
    """
    Comprehensive conquest tests for the cleanup redundant tests script.
    """

    @patch('os.walk')
    def test_find_redundant_tests(self, mock_walk):
        """Test finding redundant test files."""
        # Mock the file system structure
        mock_walk.return_value = [
            ('/testing', [], ['test_a.py', 'test_a_smoke.py', 'test_b.py']),
        ]
        
        redundant_groups = find_redundant_tests(test_dir="testing")
        
        assert "test_a" in redundant_groups
        assert "/testing/test_a_smoke.py" in redundant_groups["test_a"]
        assert "test_b" not in redundant_groups

    def test_determine_files_to_remove(self):
        """Test the logic for determining which files to remove."""
        redundant_groups = {
            'test_a': ['/testing/test_a_smoke.py', '/testing/test_a.py'],
            'test_b': ['/testing/test_b_extra.py'],
            'test_c': ['/testing/test_c_smoke.py', '/testing/test_c_deep.py']
        }
        
        files_to_remove = determine_files_to_remove(redundant_groups)
        
        assert '/testing/test_a_smoke.py' in files_to_remove
        assert '/testing/test_a.py' in files_to_remove
        assert '/testing/test_b_extra.py' not in files_to_remove # Kept as it is the only one
        assert '/testing/test_c_smoke.py' in files_to_remove # _deep is higher priority to keep
        assert '/testing/test_c_deep.py' not in files_to_remove

    @patch('scripts.cleanup_redundant_tests.determine_files_to_remove')
    @patch('scripts.cleanup_redundant_tests.find_redundant_tests')
    @patch('os.remove')
    def test_cleanup_redundant_tests_dry_run(self, mock_remove, mock_find, mock_determine):
        """Test the cleanup script in dry-run mode."""
        mock_find.return_value = {}
        mock_determine.return_value = ["/testing/test_a_smoke.py"]
        
        cleanup_redundant_tests(dry_run=True, execute=False)
        mock_remove.assert_not_called()

    @patch('scripts.cleanup_redundant_tests.determine_files_to_remove')
    @patch('scripts.cleanup_redundant_tests.find_redundant_tests')
    @patch('os.remove')
    def test_cleanup_redundant_tests_execute(self, mock_remove, mock_find, mock_determine):
        """Test the cleanup script in execute mode."""
        file_to_remove = "/testing/test_a_smoke.py"
        mock_find.return_value = {}
        mock_determine.return_value = [file_to_remove]
        
        cleanup_redundant_tests(dry_run=False, execute=True)
        mock_remove.assert_called_once_with(file_to_remove)
