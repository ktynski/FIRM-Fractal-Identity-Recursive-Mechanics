#!/usr/bin/env python3
"""
Simple test for field_emergence import.
"""

import sys
from pathlib import Path

# Add path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

def test_import_success():
    """Test that field_emergence imports successfully."""
    try:
        from applications.visualization.field_emergence import FIRMFieldVisualizationComplete
        assert True, "Import successful"
    except ImportError as e:
        assert False, f"Import failed: {e}"

def test_class_instantiation():
    """Test that the class can be instantiated."""
    try:
        from applications.visualization.field_emergence import FIRMFieldVisualizationComplete
        field = FIRMFieldVisualizationComplete()
        assert field is not None
        assert hasattr(field, '_phi')
        assert hasattr(field, '_grid_resolution')
    except Exception as e:
        assert False, f"Instantiation failed: {e}"
