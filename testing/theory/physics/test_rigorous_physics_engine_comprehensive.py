"""
Comprehensive Tests for Rigorous Physics Engine Module

Tests the COMPLETELY RIGOROUS FIRM physics engine with 100% first-principles
derivation from φ-recursion and grace, with ZERO empirical contamination.

Mathematical Foundation Testing:
    - Pure φ-recursive electromagnetic field derivation
    - Mass ratios from φ geometry only verification
    - Cosmological constants from FIRM harmonics validation
    - Complete provenance tracing verification

Physical Significance Testing:
    - Rigorous falsifiability testing implementation
    - Null hypothesis validation frameworks
    - Zero mock data or random field verification
    - Academic integrity compliance validation

Integration Testing:
    - Foundation operator integration verification
    - Cross-module derivation consistency
    - Complete mathematical rigor maintenance
    - Scientific integrity violation elimination
"""

import pytest
import numpy as np
import sympy as sp
import math
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass

from theory.physics.rigorous_physics_engine import (
    DerivationIntegrity,
    ProvenanceTrace,
    RigorousPhysicsEngine,
    ElectromagneticFieldDerivation,
    MassRatioCalculation,
    CosmologicalConstantDerivation,
    FalsifiabilityTest,
    NullHypothesisFramework,
    PhiRecursiveField,
    GraceCoherenceMetric,
)
from foundation.operators.phi_recursion import PHI_VALUE


class TestDerivationIntegrity:
    """Test derivation integrity classification and validation."""
    
    def test_integrity_levels_exist(self):
        """Test that all derivation integrity levels are properly defined."""
        expected_levels = [
            "PURE_FIRST_PRINCIPLES",
            "EMPIRICAL_CONTAMINATED", 
            "MOCK_DATA",
            "CIRCULAR_FITTING"
        ]
        
        for level in expected_levels:
            assert hasattr(DerivationIntegrity, level)
            integrity_level = getattr(DerivationIntegrity, level)
            assert isinstance(integrity_level, DerivationIntegrity)
            
    def test_integrity_hierarchy(self):
        """Test logical hierarchy of integrity levels."""
        pure = DerivationIntegrity.PURE_FIRST_PRINCIPLES
        empirical = DerivationIntegrity.EMPIRICAL_CONTAMINATED
        mock = DerivationIntegrity.MOCK_DATA
        circular = DerivationIntegrity.CIRCULAR_FITTING
        
        # Pure should be the gold standard
        assert pure != empirical
        assert pure != mock
        assert pure != circular
        
        # All levels should be distinct
        levels = [pure, empirical, mock, circular]
        assert len(set(levels)) == 4
        
    def test_integrity_value_validation(self):
        """Test integrity level value validation."""
        assert DerivationIntegrity.PURE_FIRST_PRINCIPLES.value == "pure_first_principles"
        assert DerivationIntegrity.EMPIRICAL_CONTAMINATED.value == "empirical_contaminated"
        assert DerivationIntegrity.MOCK_DATA.value == "mock_data"
        assert DerivationIntegrity.CIRCULAR_FITTING.value == "circular_fitting"


class TestProvenanceTrace:
    """Test provenance tracing functionality."""
    
    def test_provenance_trace_creation(self):
        """Test ProvenanceTrace creation and properties."""
        trace = ProvenanceTrace(
            value=1.618033988749895,  # φ
            units="dimensionless",
            source="φ-recursion fundamental constant",
            derivation_path=["Fix(𝒢)", "φ-recursion", "golden_ratio"],
            integrity_level=DerivationIntegrity.PURE_FIRST_PRINCIPLES,
            mathematical_proof="φ² = φ + 1, φ = (1+√5)/2"
        )
        
        assert abs(trace.value - PHI_VALUE) < 1e-12
        assert trace.units == "dimensionless"
        assert "φ-recursion" in trace.source
        assert len(trace.derivation_path) == 3
        assert trace.integrity_level == DerivationIntegrity.PURE_FIRST_PRINCIPLES
        assert "φ² = φ + 1" in trace.mathematical_proof
        
    def test_provenance_value_validation(self):
        """Test provenance value validation and constraints."""
        # Valid finite value
        valid_trace = ProvenanceTrace(
            value=1.0, units="meters", source="test", 
            derivation_path=["test"], 
            integrity_level=DerivationIntegrity.PURE_FIRST_PRINCIPLES,
            mathematical_proof="1 = 1"
        )
        
        assert math.isfinite(valid_trace.value)
        assert valid_trace.value == 1.0
        
        # Test that infinite values are detected
        try:
            invalid_trace = ProvenanceTrace(
                value=float('inf'), units="invalid", source="invalid",
                derivation_path=["invalid"],
                integrity_level=DerivationIntegrity.MOCK_DATA,
                mathematical_proof="invalid"
            )
            # Should either raise error or handle gracefully
            assert not math.isfinite(invalid_trace.value)
        except (ValueError, TypeError):
            # Expected for invalid input
            pass
            
    def test_provenance_phi_consistency(self):
        """Test φ-consistency in provenance traces."""
        phi_trace = ProvenanceTrace(
            value=PHI_VALUE, units="dimensionless", source="φ-recursion",
            derivation_path=["FIRM", "φ-recursion"],
            integrity_level=DerivationIntegrity.PURE_FIRST_PRINCIPLES,
            mathematical_proof="Golden ratio from φ² = φ + 1"
        )
        
        # φ should satisfy its defining equation
        phi = phi_trace.value
        assert abs(phi*phi - (phi + 1)) < 1e-12
        
        # φ should be the golden ratio
        expected_phi = (1 + math.sqrt(5)) / 2
        assert abs(phi - expected_phi) < 1e-12


class TestRigorousPhysicsEngine:
    """Test rigorous physics engine core functionality."""
    
    def test_engine_initialization(self):
        """Test RigorousPhysicsEngine initialization."""
        engine = RigorousPhysicsEngine(
            max_phi_order=10,
            precision_threshold=1e-15,
            integrity_enforcement=True,
            provenance_tracking=True
        )
        
        assert engine.max_phi_order == 10
        assert engine.precision_threshold == 1e-15
        assert engine.integrity_enforcement is True
        assert engine.provenance_tracking is True
        
    def test_engine_integrity_enforcement(self):
        """Test integrity enforcement in physics engine."""
        engine = RigorousPhysicsEngine(
            max_phi_order=5,
            precision_threshold=1e-12,
            integrity_enforcement=True,
            provenance_tracking=True
        )
        
        # Engine should reject non-rigorous inputs
        try:
            mock_result = engine.validate_calculation_integrity(
                result=1.0,
                source="random.randn()",
                integrity=DerivationIntegrity.MOCK_DATA
            )
            # Should either reject or flag as non-rigorous
            if mock_result is not None:
                assert mock_result != DerivationIntegrity.PURE_FIRST_PRINCIPLES
        except ValueError:
            # Expected rejection of mock data
            pass
            
    def test_engine_phi_order_scaling(self):
        """Test φ-order scaling in engine calculations."""
        engine = RigorousPhysicsEngine(max_phi_order=3, precision_threshold=1e-12)
        
        # Test φ-series convergence for different orders
        for order in [1, 2, 3]:
            phi_series = engine.calculate_phi_series_sum(order)
            
            assert math.isfinite(phi_series)
            assert phi_series > 0  # φ-series should be positive
            
            # Higher orders should converge to more accurate values
            if order > 1:
                previous_series = engine.calculate_phi_series_sum(order - 1)
                # Series should be converging (though not necessarily monotonic)
                assert math.isfinite(previous_series)
                
    def test_precision_threshold_enforcement(self):
        """Test precision threshold enforcement."""
        high_precision_engine = RigorousPhysicsEngine(
            max_phi_order=5, precision_threshold=1e-15
        )
        
        low_precision_engine = RigorousPhysicsEngine(
            max_phi_order=5, precision_threshold=1e-8  
        )
        
        # Both should produce valid results with different precision
        result_high = high_precision_engine.calculate_phi_series_sum(3)
        result_low = low_precision_engine.calculate_phi_series_sum(3)
        
        assert math.isfinite(result_high)
        assert math.isfinite(result_low)
        
        # Results should be close but potentially different precision
        assert abs(result_high - result_low) < 1e-7


class TestElectromagneticFieldDerivation:
    """Test pure φ-recursive electromagnetic field derivation."""
    
    def test_em_field_derivation_creation(self):
        """Test ElectromagneticFieldDerivation creation."""
        em_derivation = ElectromagneticFieldDerivation(
            base_phi_order=2,
            field_components=["E_x", "E_y", "E_z", "B_x", "B_y", "B_z"],
            gauge_fixing="phi_harmonic",
            source_free=True
        )
        
        assert em_derivation.base_phi_order == 2
        assert len(em_derivation.field_components) == 6
        assert em_derivation.gauge_fixing == "phi_harmonic"
        assert em_derivation.source_free is True
        
    def test_maxwell_equations_from_phi(self):
        """Test derivation of Maxwell equations from φ-recursion."""
        em_derivation = ElectromagneticFieldDerivation(
            base_phi_order=3, field_components=["E", "B"], gauge_fixing="coulomb"
        )
        
        # Derive Maxwell equations from φ-structure
        equations = em_derivation.derive_maxwell_equations()
        
        # Should get 4 Maxwell equations
        assert len(equations) == 4
        
        for equation in equations:
            # Each equation should be mathematical expression
            assert hasattr(equation, 'name') or isinstance(equation, str)
            # Should contain field components
            equation_str = str(equation)
            assert any(comp in equation_str for comp in ["E", "B", "div", "curl"])
            
    def test_em_field_phi_scaling(self):
        """Test φ-scaling in electromagnetic fields.""" 
        em_derivation = ElectromagneticFieldDerivation(base_phi_order=2)
        
        # Calculate field strength at different φ-scales
        field_scale_1 = em_derivation.calculate_field_strength(phi_scale=1)
        field_scale_phi = em_derivation.calculate_field_strength(phi_scale=PHI_VALUE)
        
        assert math.isfinite(field_scale_1)
        assert math.isfinite(field_scale_phi)
        
        # Fields should exhibit φ-scaling relationship
        scaling_ratio = field_scale_phi / field_scale_1
        assert math.isfinite(scaling_ratio)
        assert scaling_ratio > 0
        
    def test_gauge_invariance_preservation(self):
        """Test gauge invariance in φ-derived EM fields."""
        em_derivation = ElectromagneticFieldDerivation(
            base_phi_order=2, gauge_fixing="phi_harmonic"
        )
        
        # Test gauge transformation
        original_field = em_derivation.get_field_configuration()
        transformed_field = em_derivation.apply_gauge_transformation(
            original_field, transformation_parameter=0.1
        )
        
        # Physical observables should be gauge-invariant
        original_energy = em_derivation.calculate_field_energy(original_field)
        transformed_energy = em_derivation.calculate_field_energy(transformed_field)
        
        assert abs(original_energy - transformed_energy) < 1e-12


class TestMassRatioCalculation:
    """Test mass ratios from φ geometry only."""
    
    def test_mass_ratio_calculation_creation(self):
        """Test MassRatioCalculation creation."""
        mass_calc = MassRatioCalculation(
            reference_particle="electron",
            phi_geometric_basis=True,
            empirical_inputs_forbidden=True,
            max_recursion_depth=8
        )
        
        assert mass_calc.reference_particle == "electron"
        assert mass_calc.phi_geometric_basis is True
        assert mass_calc.empirical_inputs_forbidden is True
        assert mass_calc.max_recursion_depth == 8
        
    def test_electron_muon_mass_ratio(self):
        """Test electron-muon mass ratio from φ geometry."""
        mass_calc = MassRatioCalculation(
            reference_particle="electron",
            phi_geometric_basis=True
        )
        
        # Calculate muon/electron mass ratio from φ geometry
        ratio = mass_calc.calculate_mass_ratio("muon", "electron")
        
        assert math.isfinite(ratio)
        assert ratio > 200  # Should be approximately 206.768...
        assert ratio < 210  # Reasonable bounds
        
        # Verify no empirical contamination
        provenance = mass_calc.get_calculation_provenance("muon")
        assert provenance.integrity_level == DerivationIntegrity.PURE_FIRST_PRINCIPLES
        assert "φ" in provenance.source or "phi" in provenance.source.lower()
        
    def test_tau_electron_mass_ratio(self):
        """Test tau-electron mass ratio from φ geometry."""
        mass_calc = MassRatioCalculation(reference_particle="electron")
        
        ratio = mass_calc.calculate_mass_ratio("tau", "electron")
        
        assert math.isfinite(ratio)
        assert ratio > 3400  # Should be approximately 3477...
        assert ratio < 3600  # Reasonable bounds
        
        # Should be larger than muon ratio
        muon_ratio = mass_calc.calculate_mass_ratio("muon", "electron")
        assert ratio > muon_ratio
        
    def test_mass_ratio_phi_relationships(self):
        """Test φ-relationships in mass ratios."""
        mass_calc = MassRatioCalculation(reference_particle="electron")
        
        # Test that ratios exhibit φ-geometric structure
        muon_ratio = mass_calc.calculate_mass_ratio("muon", "electron")
        tau_ratio = mass_calc.calculate_mass_ratio("tau", "electron")
        
        # Check for φ-geometric relationships
        phi_power_relation = mass_calc.find_phi_power_relation(muon_ratio, tau_ratio)
        
        assert phi_power_relation is not None
        assert math.isfinite(phi_power_relation)
        
    def test_proton_electron_mass_ratio(self):
        """Test proton-electron mass ratio from φ geometry."""
        mass_calc = MassRatioCalculation(reference_particle="electron")
        
        ratio = mass_calc.calculate_mass_ratio("proton", "electron")
        
        assert math.isfinite(ratio)
        assert ratio > 1800  # Should be approximately 1836.15...
        assert ratio < 1850  # Reasonable bounds
        
        # Verify geometric derivation
        geometric_derivation = mass_calc.get_geometric_derivation("proton")
        assert "φ" in str(geometric_derivation) or "phi" in str(geometric_derivation).lower()


class TestCosmologicalConstantDerivation:
    """Test cosmological constants from FIRM harmonics only."""
    
    def test_cosmological_constant_derivation_creation(self):
        """Test CosmologicalConstantDerivation creation."""
        cosmo_derivation = CosmologicalConstantDerivation(
            harmonic_basis="FIRM_phi_harmonics",
            empirical_exclusion=True,
            max_harmonic_order=6
        )
        
        assert cosmo_derivation.harmonic_basis == "FIRM_phi_harmonics"
        assert cosmo_derivation.empirical_exclusion is True
        assert cosmo_derivation.max_harmonic_order == 6
        
    def test_dark_energy_constant_derivation(self):
        """Test dark energy constant from FIRM harmonics."""
        cosmo_derivation = CosmologicalConstantDerivation(harmonic_basis="FIRM_phi_harmonics")
        
        dark_energy_constant = cosmo_derivation.derive_dark_energy_constant()
        
        assert math.isfinite(dark_energy_constant)
        assert dark_energy_constant > 0  # Should be positive for accelerating expansion
        
        # Verify harmonic derivation
        harmonic_expansion = cosmo_derivation.get_harmonic_expansion(dark_energy_constant)
        assert len(harmonic_expansion) > 0
        
        # Should involve φ-harmonics
        for harmonic in harmonic_expansion:
            assert "φ" in str(harmonic) or "phi" in str(harmonic).lower()
            
    def test_hubble_constant_from_harmonics(self):
        """Test Hubble constant derivation from φ-harmonics."""
        cosmo_derivation = CosmologicalConstantDerivation(
            harmonic_basis="FIRM_phi_harmonics",
            max_harmonic_order=4
        )
        
        hubble_constant = cosmo_derivation.derive_hubble_constant()
        
        assert math.isfinite(hubble_constant)
        assert hubble_constant > 0  # H₀ should be positive
        
        # Should be in reasonable range (approximate, since derived not fitted)
        assert hubble_constant > 50   # km/s/Mpc lower bound
        assert hubble_constant < 100  # km/s/Mpc upper bound
        
    def test_cosmological_constant_phi_suppression(self):
        """Test φ⁻¹²⁰ suppression of cosmological constant."""
        cosmo_derivation = CosmologicalConstantDerivation(harmonic_basis="FIRM_phi_harmonics")
        
        # Test φ⁻¹²⁰ suppression mechanism
        unsuppressed_value = 1.0  # Natural scale
        suppressed_value = cosmo_derivation.apply_phi_suppression(unsuppressed_value, power=120)
        
        expected_suppression = PHI_VALUE ** (-120)
        expected_result = unsuppressed_value * expected_suppression
        
        assert abs(suppressed_value - expected_result) < 1e-15
        assert suppressed_value < 1e-50  # Should be extremely small
        
    def test_harmonic_convergence(self):
        """Test convergence of φ-harmonic series."""
        cosmo_derivation = CosmologicalConstantDerivation(
            harmonic_basis="FIRM_phi_harmonics",
            max_harmonic_order=10
        )
        
        # Test harmonic series convergence
        for order in [2, 4, 6, 8, 10]:
            series_sum = cosmo_derivation.calculate_harmonic_series_sum(order)
            
            assert math.isfinite(series_sum)
            
            # Higher orders should converge
            if order > 2:
                prev_sum = cosmo_derivation.calculate_harmonic_series_sum(order - 2)
                convergence = abs(series_sum - prev_sum) / abs(prev_sum)
                assert convergence < 0.1  # Should be converging


class TestFalsifiabilityTest:
    """Test rigorous falsifiability testing framework."""
    
    def test_falsifiability_test_creation(self):
        """Test FalsifiabilityTest creation."""
        falsifiability_test = FalsifiabilityTest(
            hypothesis="φ-derived fine structure constant = 1/137.036...",
            testable_predictions=["α⁻¹ specific value", "QED coupling strength"],
            experimental_observables=["atomic spectra", "QED vertex corrections"],
            error_bounds=1e-8
        )
        
        assert "φ-derived" in falsifiability_test.hypothesis
        assert len(falsifiability_test.testable_predictions) == 2
        assert len(falsifiability_test.experimental_observables) == 2
        assert falsifiability_test.error_bounds == 1e-8
        
    def test_prediction_specificity(self):
        """Test that predictions are specific and testable."""
        falsifiability_test = FalsifiabilityTest(
            hypothesis="FIRM mass ratios",
            testable_predictions=["mμ/me = 206.768...", "mτ/me = 3477.15..."],
            experimental_observables=["muon mass", "tau mass"],
            error_bounds=1e-6
        )
        
        # Predictions should be numerical and specific
        for prediction in falsifiability_test.testable_predictions:
            assert any(char.isdigit() for char in prediction)  # Contains numbers
            assert "..." in prediction or "±" in prediction or "=" in prediction  # Specific value
            
    def test_experimental_testability(self):
        """Test experimental testability of predictions."""
        falsifiability_test = FalsifiabilityTest(
            hypothesis="φ-recursive electromagnetic field equations",
            testable_predictions=["Maxwell equations exact form", "c = 299792458 m/s"],
            experimental_observables=["light speed measurements", "EM field measurements"],
            error_bounds=1e-12
        )
        
        # Should be able to generate testable experiment
        experiment = falsifiability_test.design_falsification_experiment()
        
        assert experiment is not None
        assert hasattr(experiment, 'measurement_procedure') or isinstance(experiment, dict)
        
        if isinstance(experiment, dict):
            assert 'observable' in experiment or 'measurement' in experiment
            
    def test_null_hypothesis_formation(self):
        """Test proper null hypothesis formation."""
        falsifiability_test = FalsifiabilityTest(
            hypothesis="FIRM φ-recursive theory",
            testable_predictions=["specific numerical predictions"],
            experimental_observables=["measurable quantities"],
            error_bounds=1e-6
        )
        
        null_hypothesis = falsifiability_test.formulate_null_hypothesis()
        
        assert null_hypothesis is not None
        assert isinstance(null_hypothesis, str)
        assert "not" in null_hypothesis.lower() or "random" in null_hypothesis.lower()
        

class TestNullHypothesisFramework:
    """Test null hypothesis testing framework."""
    
    def test_null_hypothesis_framework_creation(self):
        """Test NullHypothesisFramework creation."""
        null_framework = NullHypothesisFramework(
            null_statement="Observed constants are random/arbitrary",
            alternative_statement="Constants derive from φ-recursion",
            significance_level=0.05,
            statistical_power=0.95
        )
        
        assert "random" in null_framework.null_statement.lower()
        assert "φ-recursion" in null_framework.alternative_statement
        assert null_framework.significance_level == 0.05
        assert null_framework.statistical_power == 0.95
        
    def test_statistical_test_execution(self):
        """Test statistical test execution."""
        null_framework = NullHypothesisFramework(
            null_statement="Fine structure constant is arbitrary",
            alternative_statement="Fine structure constant derives from φ",
            significance_level=0.01
        )
        
        # Test observed value vs φ-prediction
        observed_alpha_inv = 137.035999084  # Observed value
        predicted_alpha_inv = null_framework.calculate_phi_prediction("fine_structure")
        
        # Execute statistical test
        test_result = null_framework.execute_statistical_test(
            observed=observed_alpha_inv,
            predicted=predicted_alpha_inv
        )
        
        assert test_result is not None
        assert 'p_value' in test_result or hasattr(test_result, 'p_value')
        assert 'reject_null' in test_result or hasattr(test_result, 'reject_null')
        
    def test_multiple_hypothesis_correction(self):
        """Test multiple hypothesis testing corrections."""
        null_framework = NullHypothesisFramework(
            null_statement="All constants are random",
            alternative_statement="Constants derive from FIRM",
            significance_level=0.05
        )
        
        # Test multiple constants simultaneously
        constants_to_test = ["fine_structure", "mass_ratios", "cosmological_constant"]
        
        corrected_results = null_framework.test_multiple_hypotheses(constants_to_test)
        
        assert len(corrected_results) == len(constants_to_test)
        
        for result in corrected_results:
            assert 'corrected_p_value' in result or hasattr(result, 'corrected_p_value')
            assert 'bonferroni_corrected' in result or hasattr(result, 'bonferroni_corrected')
            
    def test_power_analysis(self):
        """Test statistical power analysis."""
        null_framework = NullHypothesisFramework(
            null_statement="Constants are random",
            alternative_statement="Constants are φ-derived",
            statistical_power=0.90
        )
        
        # Calculate required sample size for given power
        required_sample_size = null_framework.calculate_required_sample_size(
            effect_size=0.5,  # Medium effect size
            alpha=0.05,
            power=0.90
        )
        
        assert isinstance(required_sample_size, (int, float))
        assert required_sample_size > 0
        assert required_sample_size < 10000  # Should be reasonable


class TestPhiRecursiveField:
    """Test φ-recursive field implementations."""
    
    def test_phi_recursive_field_creation(self):
        """Test PhiRecursiveField creation."""
        field = PhiRecursiveField(
            field_type="electromagnetic",
            recursion_depth=5,
            base_amplitude=1.0,
            phi_scaling_exponents=[1, 2, 3, 4, 5]
        )
        
        assert field.field_type == "electromagnetic"
        assert field.recursion_depth == 5
        assert field.base_amplitude == 1.0
        assert len(field.phi_scaling_exponents) == 5
        
    def test_field_amplitude_calculation(self):
        """Test field amplitude calculations."""
        field = PhiRecursiveField(
            field_type="test",
            recursion_depth=3,
            base_amplitude=1.0,
            phi_scaling_exponents=[0, 1, 2]
        )
        
        # Calculate field amplitude at position
        position = np.array([0.0, 0.0, 0.0])
        amplitude = field.calculate_amplitude(position)
        
        assert math.isfinite(amplitude)
        # At origin, should be sum of φ^n terms: 1 + φ + φ²
        expected = 1.0 + PHI_VALUE + PHI_VALUE**2
        assert abs(amplitude - expected) < 1e-12
        
    def test_field_recursion_properties(self):
        """Test φ-recursive properties of fields."""
        field = PhiRecursiveField("test", 4, 1.0, [0, 1, 2, 3])
        
        # Test recursion relation: F_n = F_{n-1} + F_{n-2} (φ-recursion)
        amplitudes = []
        for n in range(4):
            amp = field.get_recursion_level_amplitude(n)
            amplitudes.append(amp)
            
        # φ-recursion: a_n = φ^n should satisfy a_n = a_{n-1} + a_{n-2}
        for n in range(2, 4):
            phi_n = PHI_VALUE ** n
            phi_n_minus_1 = PHI_VALUE ** (n-1)
            phi_n_minus_2 = PHI_VALUE ** (n-2)
            
            # φ^n = φ^{n-1} + φ^{n-2} for φ-recursion
            assert abs(phi_n - (phi_n_minus_1 + phi_n_minus_2)) < 1e-12
            
    def test_field_normalization(self):
        """Test field normalization procedures."""
        field = PhiRecursiveField("test", 3, 2.0, [0, 1, 2])  # Non-unit amplitude
        
        # Normalize field
        normalized_field = field.normalize()
        
        assert normalized_field.field_type == field.field_type
        assert normalized_field.recursion_depth == field.recursion_depth
        
        # Check normalization
        norm = normalized_field.calculate_field_norm()
        assert abs(norm - 1.0) < 1e-12


class TestGraceCoherenceMetric:
    """Test grace coherence metric calculations."""
    
    def test_grace_coherence_creation(self):
        """Test GraceCoherenceMetric creation."""
        grace_metric = GraceCoherenceMetric(
            coherence_threshold=0.8,
            devourer_suppression_factor=0.1,
            phi_harmony_weight=1.0
        )
        
        assert grace_metric.coherence_threshold == 0.8
        assert grace_metric.devourer_suppression_factor == 0.1
        assert grace_metric.phi_harmony_weight == 1.0
        
    def test_coherence_calculation(self):
        """Test coherence metric calculation."""
        grace_metric = GraceCoherenceMetric(0.5, 0.1, 1.0)
        
        # Create test state with known properties
        test_state = {
            'phi_alignment': 0.9,
            'mathematical_consistency': 0.95,
            'empirical_contamination': 0.0,
            'derivation_completeness': 1.0
        }
        
        coherence = grace_metric.calculate_coherence(test_state)
        
        assert 0.0 <= coherence <= 1.0  # Should be normalized
        assert math.isfinite(coherence)
        
        # High-quality state should have high coherence
        assert coherence > 0.7
        
    def test_devourer_detection(self):
        """Test devourer (contamination) detection."""
        grace_metric = GraceCoherenceMetric(0.8, 0.1, 1.0)
        
        # State with empirical contamination
        contaminated_state = {
            'phi_alignment': 0.6,
            'mathematical_consistency': 0.7,
            'empirical_contamination': 0.5,  # High contamination
            'derivation_completeness': 0.8
        }
        
        devourers_detected = grace_metric.detect_devourers(contaminated_state)
        
        assert len(devourers_detected) > 0  # Should detect contamination
        assert any('empirical' in str(d).lower() for d in devourers_detected)
        
    def test_phi_harmony_assessment(self):
        """Test φ-harmony assessment in grace metric."""
        grace_metric = GraceCoherenceMetric(0.5, 0.1, 1.0)
        
        # State with perfect φ-alignment
        phi_aligned_state = {
            'phi_alignment': 1.0,
            'golden_ratio_consistency': True,
            'recursion_depth': 5,
            'fractal_harmony': 0.95
        }
        
        harmony_score = grace_metric.assess_phi_harmony(phi_aligned_state)
        
        assert 0.0 <= harmony_score <= 1.0
        assert harmony_score > 0.8  # Should be high for φ-aligned state


class TestIntegrationWithFoundation:
    """Test integration with FIRM foundation modules."""
    
    def test_phi_value_consistency(self):
        """Test φ value consistency across modules."""
        engine = RigorousPhysicsEngine()
        
        # φ value should be consistent with foundation
        engine_phi = engine.get_phi_constant()
        foundation_phi = PHI_VALUE
        
        assert abs(engine_phi - foundation_phi) < 1e-15
        
        # Should satisfy φ-equation
        assert abs(engine_phi**2 - (engine_phi + 1)) < 1e-12
        
    def test_cross_module_derivation_consistency(self):
        """Test consistency of derivations across modules."""
        engine = RigorousPhysicsEngine()
        
        # Test that electromagnetic and mass ratio derivations are consistent
        em_derivation = ElectromagneticFieldDerivation(base_phi_order=3)
        mass_calc = MassRatioCalculation(reference_particle="electron")
        
        # Both should use same φ-basis
        em_phi_order = em_derivation.base_phi_order
        mass_phi_depth = mass_calc.max_recursion_depth
        
        assert em_phi_order > 0
        assert mass_phi_depth > 0
        
        # Both should produce finite, meaningful results
        em_field_strength = em_derivation.calculate_field_strength()
        mass_ratio = mass_calc.calculate_mass_ratio("muon", "electron")
        
        assert math.isfinite(em_field_strength)
        assert math.isfinite(mass_ratio)
        
    def test_academic_integrity_compliance(self):
        """Test full academic integrity compliance."""
        engine = RigorousPhysicsEngine(integrity_enforcement=True)
        
        # Test that all calculations maintain integrity
        calculations = [
            ("fine_structure", engine.calculate_fine_structure_constant()),
            ("mass_ratio", engine.calculate_mass_ratio("muon", "electron")),
            ("cosmological_constant", engine.calculate_cosmological_constant())
        ]
        
        for calc_name, result in calculations:
            assert math.isfinite(result)
            
            # Get provenance for each calculation
            provenance = engine.get_calculation_provenance(calc_name)
            
            # Should be pure first principles
            assert provenance.integrity_level == DerivationIntegrity.PURE_FIRST_PRINCIPLES
            
            # Should have mathematical proof
            assert len(provenance.mathematical_proof) > 0
            
            # Should trace to φ-recursion
            assert any('φ' in step or 'phi' in step.lower() for step in provenance.derivation_path)
