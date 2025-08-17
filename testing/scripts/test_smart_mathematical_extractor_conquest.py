#!/usr/bin/env python3
"""
Team 2 Scripts Conquest: Smart Mathematical Extractor
Target: scripts/smart_mathematical_extractor.py
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.smart_mathematical_extractor import SmartMathematicalExtractor

class TestSmartMathematicalExtractorConquest:
    """
    Comprehensive conquest tests for the smart mathematical extractor.
    """

    def setup_method(self):
        """Set up the test environment."""
        self.extractor = SmartMathematicalExtractor()

    def test_initialization(self):
        """Verify the extractor initializes correctly."""
        assert self.extractor.constants_dir == Path("constants")

    @patch('importlib.util.spec_from_file_location')
    @patch('importlib.util.module_from_spec')
    def test_execute_module_safely(self, mock_module_from_spec, mock_spec_from_file_location):
        """Test the safe execution of a module."""
        # Create a mock module and spec
        mock_spec = MagicMock()
        mock_module = MagicMock()
        mock_spec_from_file_location.return_value = mock_spec
        mock_module_from_spec.return_value = mock_module

        # Set up the mock module with some attributes
        mock_module.SOME_CONSTANT = 123.45
        mock_module._INTERNAL_VAR = "hidden"
        mock_module.STRING_VAR = "not a constant"

        # Mock the loader's exec_module method
        mock_loader = MagicMock()
        mock_spec.loader = mock_loader

        # Call the method
        module_file = Path("constants/test_module.py")
        computed_values = self.extractor.execute_module_safely(module_file)

        # Assertions
        mock_spec_from_file_location.assert_called_once_with("test_module", module_file)
        mock_module_from_spec.assert_called_once_with(mock_spec)
        mock_loader.exec_module.assert_called_once_with(mock_module)
        assert "SOME_CONSTANT" in computed_values
        assert computed_values["SOME_CONSTANT"] == 123.45
        assert "_INTERNAL_VAR" not in computed_values
        assert "STRING_VAR" not in computed_values

    def test_extract_mathematical_expressions(self):
        """Test the extraction of mathematical expressions."""
        content = """
        ALPHA = 1 / 137.0
        BETA = 2 * PI * R
        GAMMA = np.sqrt(ALPHA ** 2 + BETA ** 2)
        """
        expressions = self.extractor.extract_mathematical_expressions(content)
        expressions.sort(key=lambda x: x['line'])
        assert len(expressions) == 5
        assert expressions[0]['variable'] == 'ALPHA'
        assert expressions[2]['expression'] == '2 * PI * R'
        assert expressions[4]['variable'] == 'GAMMA'

    def test_python_to_latex(self):
        """Test the conversion of Python expressions to LaTeX."""
        assert self.extractor.python_to_latex("2 * PI * R") == r"2  \cdot  \pi  \cdot  R"
        assert self.extractor.python_to_latex("ALPHA ** 2") == r"\alpha^{2}"
        assert self.extractor.python_to_latex("np.sqrt(BETA)") == r"np.\sqrt(BETA)"

    @patch('scripts.smart_mathematical_extractor.SmartMathematicalExtractor.execute_module_safely')
    @patch('scripts.smart_mathematical_extractor.SmartMathematicalExtractor.extract_mathematical_expressions')
    @patch('scripts.smart_mathematical_extractor.SmartMathematicalExtractor.create_derivation_steps')
    def test_generate_module_latex(self, mock_create_steps, mock_extract_expr, mock_execute_safely):
        """Test the generation of a LaTeX module."""
        # Setup mocks
        mock_execute_safely.return_value = {'H0_DERIVED': 67.4}
        mock_extract_expr.return_value = [{'variable': 'H0_DERIVED', 'expression': '2 * 33.7'}]
        mock_create_steps.return_value = [{'latex': 'H_0 &= 67.400000', 'description': 'desc'}]

        module_file = Path("constants/hubble_constant_derivation.py")
        
        with patch('builtins.open', MagicMock()):
            latex_lines = self.extractor.generate_module_latex(module_file)

        assert any("Hubble Constant Derivation" in line for line in latex_lines)
        assert any("H_0 &=" in line for line in latex_lines)
        mock_create_steps.assert_called_once()
