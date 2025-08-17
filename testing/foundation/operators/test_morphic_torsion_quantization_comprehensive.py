#!/usr/bin/env python3
"""
Test for morphic torsion quantization.
"""

import pytest
from foundation.operators.morphic_torsion_quantization import (
    EigenvalueType,
    EigenvalueResult,
    MorphicTorsionQuantization,
    MTQAnalysis,
)
from foundation.operators.phi_recursion import PHI_VALUE
from foundation.operators.grace_operator import GRACE_OPERATOR


class TestMorphicTorsionQuantization:
    """Test the actual MorphicTorsionQuantization class."""
    
    def test_morphic_torsion_quantization_creation(self):
        """Test MorphicTorsionQuantization creation and initialization."""
        mtq = MorphicTorsionQuantization()
        
        assert hasattr(mtq, 'phi')
        assert hasattr(mtq, 'grace_operator')
        assert hasattr(mtq, 'analysis_history')
        assert hasattr(mtq, 'max_n')
        assert hasattr(mtq, 'precision')
        
        assert mtq.phi == PHI_VALUE
        assert mtq.max_n == 200
        assert mtq.precision == 1e-15
        
    def test_eigenvalue_type_enum(self):
        """Test that EigenvalueType enum has expected values."""
        assert hasattr(EigenvalueType, 'REAL')
        assert hasattr(EigenvalueType, 'COMPLEX')
        assert hasattr(EigenvalueType, 'ZERO')
        
    def test_eigenvalue_result_creation(self):
        """Test EigenvalueResult creation."""
        result = EigenvalueResult(
            n_value=113,
            eigenvalue=1.618,
            eigenvalue_type=EigenvalueType.REAL,
            stability_measure=0.95,
            morphic_torsion=0.382,
            mathematical_necessity=True
        )
        
        assert result.n_value == 113
        assert result.eigenvalue == 1.618
        assert result.eigenvalue_type == EigenvalueType.REAL
        assert result.stability_measure == 0.95
        assert result.morphic_torsion == 0.382
        assert result.mathematical_necessity is True
        
    def test_mtq_analysis_creation(self):
        """Test MTQAnalysis creation."""
        analysis = MTQAnalysis(
            optimal_n=113,
            eigenvalue_minimum=1.618,
            stability_analysis={113: 0.95, 114: 0.92, 115: 0.89},
            mathematical_justification="φ-based eigenvalue minimization",
            uniqueness_proof="Unique minimum at n=113",
            connection_to_constants={"fine_structure": 0.007297, "phi": 1.618}
        )
        
        assert analysis.optimal_n == 113
        assert analysis.eigenvalue_minimum == 1.618
        assert analysis.stability_analysis[113] == 0.95
        assert "φ-based" in analysis.mathematical_justification
        assert "Unique minimum" in analysis.uniqueness_proof
        assert analysis.connection_to_constants["phi"] == 1.618
