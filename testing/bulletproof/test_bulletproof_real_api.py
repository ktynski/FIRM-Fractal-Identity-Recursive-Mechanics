#!/usr/bin/env python3
"""
Targeted Tests for Real Bulletproof Infrastructure APIs

This module provides comprehensive test coverage for the bulletproof
infrastructure modules using their ACTUAL APIs, not assumed ones.

Target Modules:
- constants/bulletproof_fine_structure_derivation.py (251 lines)
- foundation/proofs/bulletproof_axiom_independence.py (397 lines) 
- validation/comprehensive_error_handling.py (308 lines)

Total Coverage Boost: 956 lines (5% coverage improvement)

Author: FIRM Development Team
Created: 2024
"""

import pytest
import sys
import os
from pathlib import Path
import numpy as np
from typing import Any

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Import bulletproof modules
from constants.bulletproof_fine_structure_derivation import BulletproofFineStructureDerivation
from foundation.proofs.bulletproof_axiom_independence import BulletproofAxiomIndependence
from validation.comprehensive_error_handling import ComprehensiveErrorHandler

class TestBulletproofFineStructureReal:
    """Real API tests for bulletproof fine structure derivation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.derivation = BulletproofFineStructureDerivation()
    
    def test_initialization_real(self):
        """Test actual initialization."""
        assert self.derivation is not None
        assert hasattr(self.derivation, '_phi')
        assert abs(self.derivation._phi - 1.618033988749) < 1e-10
    
    def test_derive_phi_sixth_correction_real(self):
        """Test actual φ⁻⁶ correction derivation."""
        result = self.derivation.derive_phi_sixth_correction()
        
        assert result is not None
        assert hasattr(result, 'alpha_inverse')
        assert hasattr(result, 'method')
        assert result.alpha_inverse > 0
        assert 130 < result.alpha_inverse < 140
    
    def test_derive_phi_fifth_correction_real(self):
        """Test actual φ⁻⁵ correction derivation."""
        result = self.derivation.derive_phi_fifth_correction()
        
        assert result is not None
        assert hasattr(result, 'alpha_inverse')
        assert result.alpha_inverse > 0
        assert 130 < result.alpha_inverse < 140
    
    def test_derive_systematic_optimization_real(self):
        """Test actual systematic optimization method."""
        result = self.derivation.derive_systematic_optimization(max_power=10)
        
        assert result is not None
        assert hasattr(result, 'alpha_inverse')
        assert result.alpha_inverse > 0
        assert 130 < result.alpha_inverse < 140
    
    def test_generate_comprehensive_report_real(self):
        """Test actual comprehensive report generation."""
        report = self.derivation.generate_comprehensive_report()
        
        assert report is not None
        assert isinstance(report, str)
        assert len(report) > 100  # Substantial report
        assert "φ" in report  # Contains mathematical content
    
    def test_internal_methods_real(self):
        """Test actual internal methods.""" 
        # Test phi power calculation
        phi_power = self.derivation._get_phi_power(-6, use_cache=True)
        assert phi_power > 0
        assert phi_power < 1
        
        # Test base coupling
        base = self.derivation._get_base_coupling_safe()
        assert base > 136
        assert base < 138


class TestBulletproofAxiomIndependenceReal:
    """Real API tests for bulletproof axiom independence."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.prover = BulletproofAxiomIndependence()
    
    def test_initialization_real(self):
        """Test actual initialization."""
        assert self.prover is not None
        assert hasattr(self.prover, 'cache_enabled')
        assert hasattr(self.prover, 'strict_verification')
    
    def test_prove_ag1_independence_real(self):
        """Test actual AG1 independence proof."""
        result = self.prover.prove_axiom_independence_bulletproof('AG1')
        
        assert result is not None
        assert hasattr(result, 'axiom')
        assert hasattr(result, 'independent')
        assert hasattr(result, 'countermodel')
        assert result.axiom == 'AG1'
        assert result.independent is True
    
    def test_prove_ag2_independence_real(self):
        """Test actual AG2 independence proof."""
        result = self.prover.prove_axiom_independence_bulletproof('AG2')
        
        assert result is not None
        assert result.axiom == 'AG2'
        assert result.independent is True
    
    def test_prove_ag3_independence_real(self):
        """Test actual AG3 independence proof."""
        result = self.prover.prove_axiom_independence_bulletproof('AG3')
        
        assert result is not None
        assert result.axiom == 'AG3'
        assert result.independent is True
    
    def test_prove_ag4_independence_real(self):
        """Test actual AG4 independence proof."""
        result = self.prover.prove_axiom_independence_bulletproof('AG4')
        
        assert result is not None
        assert result.axiom == 'AG4'
        assert result.independent is True
    
    def test_prove_apsi1_independence_real(self):
        """Test actual AΨ1 independence proof."""
        result = self.prover.prove_axiom_independence_bulletproof('AΨ1')
        
        assert result is not None
        assert result.axiom == 'AΨ1'
        assert result.independent is True
    
    def test_prove_all_axioms_real(self):
        """Test actual proving all axioms."""
        results = self.prover.prove_all_axioms_bulletproof()
        
        assert len(results) == 5
        for axiom, result in results.items():
            assert result.independent is True
    
    def test_generate_report_real(self):
        """Test actual report generation."""
        report = self.prover.generate_comprehensive_report()
        
        assert report is not None
        assert isinstance(report, str)
        assert len(report) > 100
        assert "axiom" in report.lower()


class TestComprehensiveErrorHandlerReal:
    """Real API tests for comprehensive error handler."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.handler = ComprehensiveErrorHandler()
    
    def test_initialization_real(self):
        """Test actual initialization."""
        assert self.handler is not None
        assert hasattr(self.handler, 'error_history')
        assert hasattr(self.handler, 'performance_metrics')
    
    def test_validate_input_real(self):
        """Test actual input validation."""
        validation_rules = {
            'required': True,
            'type': float,
            'min_value': 0.0,
            'max_value': 1000.0
        }
        
        result = self.handler.validate_input(137.036, validation_rules)
        assert result is not None
        assert hasattr(result, 'is_valid')
        assert result.is_valid is True
    
    def test_check_dependencies_real(self):
        """Test actual dependency checking."""
        deps = ['numpy', 'pytest', 'nonexistent_package']
        result = self.handler.check_dependencies(deps)
        
        assert isinstance(result, dict)
        assert 'numpy' in result
        assert result['numpy'] is True
        assert 'pytest' in result
        assert result['pytest'] is True
        assert 'nonexistent_package' in result
        assert result['nonexistent_package'] is False
    
    def test_create_error_report_real(self):
        """Test actual error report creation."""
        test_error = ValueError("Test error")
        report = self.handler.create_error_report(test_error, "test_function")
        
        assert report is not None
        assert hasattr(report, 'error_type')
        assert hasattr(report, 'message')
        assert hasattr(report, 'function_name')
        assert report.error_type == 'ValueError'
        assert report.function_name == 'test_function'
    
    def test_enhance_exception_real(self):
        """Test actual exception enhancement."""
        test_error = ValueError("Test error")
        enhanced = self.handler.enhance_exception(
            test_error, 
            "test_function",
            additional_context={'param': 'test_value'}
        )
        
        assert enhanced is not None
        assert hasattr(enhanced, '__cause__')
    
    def test_safe_computation_real(self):
        """Test actual safe computation wrapper."""
        def test_computation():
            return 137.036
        
        def fallback_computation():
            return 137.0
        
        result = self.handler.safe_computation(
            test_computation, 
            fallback_func=fallback_computation
        )
        
        assert result is not None
        assert isinstance(result, float)
        assert result == 137.036
    
    def test_generate_diagnostic_report_real(self):
        """Test actual diagnostic report generation."""
        # First trigger some activity to generate diagnostics
        self.handler.validate_input(137.0, {'required': True})
        self.handler.check_dependencies(['numpy'])
        
        report = self.handler.generate_diagnostic_report()
        
        assert report is not None
        assert isinstance(report, str)
        assert len(report) > 100


class TestIntegratedBulletproofReal:
    """Integration tests using real APIs."""
    
    def test_full_bulletproof_pipeline_real(self):
        """Test complete bulletproof pipeline with real APIs."""
        # Initialize all components
        derivation = BulletproofFineStructureDerivation()
        prover = BulletproofAxiomIndependence()
        handler = ComprehensiveErrorHandler()
        
        # Derive fine structure constant
        alpha_result = derivation.derive_phi_sixth_correction()
        assert alpha_result is not None
        assert 130 < alpha_result.alpha_inverse < 140
        
        # Prove one axiom independence
        proof_result = prover.prove_axiom_independence_bulletproof('AG1')
        assert proof_result is not None
        assert proof_result.independent is True
        
        # Create diagnostic report
        diagnostics = handler.generate_diagnostic_report()
        assert diagnostics is not None
        assert len(diagnostics) > 50
    
    def test_bulletproof_error_handling_real(self):
        """Test bulletproof error handling with real APIs.""" 
        handler = ComprehensiveErrorHandler()
        
        # Test handling various real error scenarios
        test_error = ValueError("Test error")
        report = handler.create_error_report(test_error, "test_method")
        assert report.error_type == 'ValueError'
        
        # Test safe computation with failure
        def failing_computation():
            raise RuntimeError("Computation failed")
        
        def fallback():
            return "fallback_result"
        
        result = handler.safe_computation(failing_computation, fallback_func=fallback)
        assert result == "fallback_result"


# Focused smoke test for immediate verification
def test_bulletproof_modules_working():
    """Smoke test: Verify bulletproof modules work with real APIs."""
    # Test fine structure derivation
    derivation = BulletproofFineStructureDerivation()
    result1 = derivation.derive_phi_sixth_correction()
    assert result1 is not None
    assert result1.alpha_inverse > 130
    
    # Test axiom independence  
    prover = BulletproofAxiomIndependence()
    result2 = prover.prove_axiom_independence_bulletproof('AG1')
    assert result2 is not None
    assert result2.independent is True
    
    # Test error handler
    handler = ComprehensiveErrorHandler()
    deps = handler.check_dependencies(['numpy'])
    assert deps['numpy'] is True
    
    print("🛡️ All bulletproof modules working with real APIs!")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
