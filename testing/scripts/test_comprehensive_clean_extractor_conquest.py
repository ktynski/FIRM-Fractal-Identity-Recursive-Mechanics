#!/usr/bin/env python3
"""
Team 2 Scripts Conquest: Comprehensive Clean Extractor
Target: scripts/comprehensive_clean_extractor.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.comprehensive_clean_extractor import ComprehensiveCleanExtractor

class TestComprehensiveCleanExtractorConquest:
    """
    Comprehensive conquest tests for the comprehensive clean extractor.
    """

    def setup_method(self):
        """Set up the test environment."""
        self.extractor = ComprehensiveCleanExtractor()

    def test_initialization(self):
        """Verify the extractor initializes correctly."""
        assert self.extractor.constants_dir == Path("constants")
        assert "fundamental" in self.extractor.domains

    @patch('builtins.open')
    def test_extract_clean_content(self, mock_open):
        """Test the extraction of clean content from a module."""
        # Mock the file content
        mock_file_content = '''"""
        Module Docstring
        Key Results:
         - Result 1
         - Result 2
        Derivation Path:
         - Step 1 -> Step 2
        """
        '''
        mock_open.return_value.__enter__.return_value.read.return_value = mock_file_content
        
        module_file = Path("constants/test_module.py")
        content = self.extractor.extract_clean_content(module_file)

        assert content['module'] == 'test_module'
        assert "Module Docstring" in content['docstring']
        assert len(content['key_results']) == 3
        assert "Step 1 -> Step 2" in content['derivation_path']
        assert content['has_content'] is True

    def test_generate_clean_latex_section(self):
        """Test the generation of a clean LaTeX section."""
        domain_key = "fundamental"
        domain_info = {
            'title': 'Fundamental Constants',
            'description': 'Core constants'
        }
        module_contents = [
            {
                'has_content': True,
                'module': 'test_module',
                'file_path': 'constants/test_module.py',
                'key_results': ['Result 1: α ≈ 1/137'],
                'derivation_path': 'Path 1 → Path 2',
                'main_result': 'α⁻¹ ≈ 137.036'
            }
        ]
        
        latex_lines = self.extractor.generate_clean_latex_section(domain_key, domain_info, module_contents)

        # Check for key elements in the generated LaTeX
        latex_output = "".join(latex_lines)
        assert "\\subsection{Fundamental Constants}" in latex_output
        assert "\\subsubsection{Test Module}" in latex_output
        assert "\\item Result 1: $\\alpha$ $\\approx$ 1/137" in latex_output
        assert "Path 1 $\\to$ Path 2" in latex_output
        assert "Primary Result:" in latex_output

    @patch('scripts.comprehensive_clean_extractor.ComprehensiveCleanExtractor.extract_clean_content')
    @patch('scripts.comprehensive_clean_extractor.ComprehensiveCleanExtractor.generate_clean_latex_section')
    def test_generate_comprehensive_appendix(self, mock_generate_section, mock_extract_content):
        """Test the generation of the comprehensive appendix."""
        # Setup mocks
        mock_extract_content.return_value = {'has_content': True}
        mock_generate_section.return_value = ["\\subsection{Test Section}"]

        # Mock path existence
        with patch.object(Path, 'exists', return_value=True):
            latex_content = self.extractor.generate_comprehensive_appendix()

        # Assertions
        assert "\\appendix" in latex_content
        assert "\\section{Complete Mathematical Derivations}" in latex_content
        assert mock_extract_content.call_count > 0
        assert mock_generate_section.call_count > 0
        assert "Test Section" in latex_content
