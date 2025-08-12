"""Simple tests for codebase mapper to boost coverage."""

import pytest
import sys
from pathlib import Path
from utils.codebase_mapper import main, safe_read_text, now_iso, expr_to_str


def test_main_function_exists():
    """Test that main function exists and handles help."""
    assert callable(main)

    # Test with help flag (should exit gracefully)
    old_argv = sys.argv
    try:
        sys.argv = ['codebase_mapper.py', '--help']
        with pytest.raises(SystemExit):
            main()
    finally:
        sys.argv = old_argv


def test_safe_read_text():
    """Test safe_read_text utility function."""
    # Test with non-existent file
    result = safe_read_text('/non/existent/file.txt')
    assert result is None

    # Test with this test file itself
    test_file = __file__
    result = safe_read_text(test_file)
    assert result is not None
    assert isinstance(result, str)
    assert 'test_safe_read_text' in result


def test_now_iso():
    """Test now_iso timestamp function."""
    timestamp = now_iso()
    assert isinstance(timestamp, str)
    assert 'T' in timestamp  # Should be ISO format
    assert '+' in timestamp or 'Z' in timestamp  # Should have timezone


def test_expr_to_str():
    """Test expr_to_str AST utility."""
    import ast

    # Test with None
    result = expr_to_str(None)
    assert result is None

    # Test with simple AST node
    node = ast.parse('42').body[0].value
    result = expr_to_str(node)
    assert result is not None


def test_codebase_mapper_cli_with_minimal_args():
    """Test codebase mapper CLI with minimal valid arguments."""
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a simple test file
        test_file = temp_path / "test.py"
        test_file.write_text("# Test file\nprint('hello')\n")

        old_argv = sys.argv
        try:
            sys.argv = [
                'codebase_mapper.py',
                '--root', str(temp_path),
                '--output-json', str(temp_path / 'output.json')
            ]

            # Should run without crashing
            main()

            # Check output file was created
            output_file = temp_path / 'output.json'
            assert output_file.exists()

        except SystemExit as e:
            # Exit code 0 is success
            if e.code != 0:
                raise
        finally:
            sys.argv = old_argv