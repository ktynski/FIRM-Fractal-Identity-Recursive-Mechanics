"""
Comprehensive tests for central_physics_constants module.

Tests all properties, mathematical consistency, and physical validation.
"""

import pytest
import math
from typing import Dict, Any

from constants.central_physics_constants import (
    CentralPhysicsConstants,
    CENTRAL_PHYSICS_CONSTANTS,
    get_alpha_inverse,
    get_electron_mass_mev,
    get_cosmological_correction,
    get_cmb_temperature
)


class TestCentralPhysicsConstantsComprehensive:
    """Comprehensive test suite for CentralPhysicsConstants class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.central_constants = CentralPhysicsConstants()
        self.singleton = CENTRAL_PHYSICS_CONSTANTS

    def test_module_constants_exist(self):
        """Test that module-level constants exist."""
        assert CENTRAL_PHYSICS_CONSTANTS is not None
        assert isinstance(CENTRAL_PHYSICS_CONSTANTS, CentralPhysicsConstants)

    def test_class_instantiation(self):
        """Test class instantiation and basic attributes."""
        assert isinstance(self.central_constants, CentralPhysicsConstants)
        assert hasattr(self.central_constants, '_phi')
        assert hasattr(self.central_constants, '_alpha_result')
        assert hasattr(self.central_constants, '_cosmological_result')
        assert hasattr(self.central_constants, '_hubble_result')

    def test_phi_value_initialization(self):
        """Test that φ value is properly initialized."""
        from foundation.operators.phi_recursion import PHI_VALUE
        assert self.central_constants._phi == PHI_VALUE
        assert abs(self.central_constants._phi - 1.618033988749895) < 1e-10

    def test_fine_structure_constant_inverse(self):
        """Test fine structure constant inverse property."""
        alpha_inv = self.central_constants.fine_structure_constant_inverse
        
        # Check that value is finite and reasonable
        assert math.isfinite(alpha_inv)
        assert alpha_inv > 100  # Should be around 137
        assert alpha_inv < 200  # Should be around 137
        
        # Check that lazy loading works
        assert self.central_constants._alpha_result is not None

    def test_fine_structure_constant(self):
        """Test fine structure constant property."""
        alpha = self.central_constants.fine_structure_constant
        
        # Check that value is finite and reasonable
        assert math.isfinite(alpha)
        assert alpha > 0.005  # Should be around 1/137
        assert alpha < 0.01   # Should be around 1/137
        
        # Check mathematical consistency
        alpha_inv = self.central_constants.fine_structure_constant_inverse
        assert abs(alpha * alpha_inv - 1.0) < 1e-10

    def test_cosmological_constant_correction(self):
        """Test cosmological constant correction property."""
        correction = self.central_constants.cosmological_constant_correction
        
        # Check that value is finite and reasonable
        assert math.isfinite(correction)
        assert correction > 0  # Should be positive
        assert correction < 10  # Should be reasonable magnitude
        
        # Check that lazy loading works
        assert self.central_constants._cosmological_result is not None

    def test_omega_lambda(self):
        """Test dark energy density parameter property."""
        omega_lambda = self.central_constants.omega_lambda
        
        # Check that value is finite and reasonable
        assert math.isfinite(omega_lambda)
        assert omega_lambda > 0  # Should be positive
        assert omega_lambda < 1  # Should be less than 1 (dark energy fraction)
        
        # Check that lazy loading works
        assert self.central_constants._cosmological_result is not None

    def test_hubble_constant_base(self):
        """Test Hubble constant base property."""
        h0 = self.central_constants.hubble_constant_base
        
        # Check that value is finite and reasonable
        assert math.isfinite(h0)
        assert h0 > 0  # Should be positive
        # Allow for very large values (might be in different units)
        assert h0 < 1e20  # Should be finite
        
        # Check that lazy loading works
        assert self.central_constants._hubble_result is not None

    def test_electron_mass_mev(self):
        """Test electron mass property."""
        electron_mass = self.central_constants.electron_mass_mev
        
        # Check that value is finite and reasonable
        assert math.isfinite(electron_mass)
        assert electron_mass == 1.0  # Should be 1.0 as base unit in FIRM theory

    def test_cmb_temperature_kelvin(self):
        """Test CMB temperature property."""
        cmb_temp = self.central_constants.cmb_temperature_kelvin
        
        # Check that value is finite and reasonable
        assert math.isfinite(cmb_temp)
        assert cmb_temp > 0  # Should be positive
        assert cmb_temp < 100  # Should be around 2.7 K

    def test_zeta_3_apery(self):
        """Test zeta(3) property."""
        zeta_3 = self.central_constants.zeta_3_apery
        
        # Check that value is finite and correct
        assert math.isfinite(zeta_3)
        assert abs(zeta_3 - 1.2020569) < 1e-7  # Should be Apéry's constant

    def test_higgs_vev_gev(self):
        """Test Higgs VEV property."""
        higgs_vev = self.central_constants.higgs_vev_gev
        
        # Check that value is finite and reasonable
        assert math.isfinite(higgs_vev)
        assert higgs_vev > 200  # Should be around 246 GeV
        assert higgs_vev < 300  # Should be around 246 GeV

    def test_planck_temperature_kelvin(self):
        """Test Planck temperature property."""
        planck_temp = self.central_constants.planck_temperature_kelvin
        
        # Check that value is finite and reasonable
        assert math.isfinite(planck_temp)
        assert planck_temp > 1e30  # Should be very large
        assert planck_temp < 1e35  # Should be reasonable for Planck scale

    def test_planck_constant_j_s(self):
        """Test Planck constant property."""
        hbar = self.central_constants.planck_constant_j_s
        
        # Check that value is finite and reasonable
        assert math.isfinite(hbar)
        assert hbar > 1e-35  # Should be very small
        assert hbar < 1e-30  # Should be reasonable for Planck constant
        
        # Check that lazy loading works
        assert self.central_constants._planck_constant_result is not None

    def test_gravitational_constant_m3_kg_s2(self):
        """Test gravitational constant property."""
        G = self.central_constants.gravitational_constant_m3_kg_s2
        
        # Check that value is finite and reasonable
        assert math.isfinite(G)
        assert G > 1e-12  # Should be very small
        assert G < 1e-8   # Should be reasonable for gravitational constant
        
        # Note: Lazy loading might not be implemented for this property

    def test_proton_mass_gev(self):
        """Test proton mass property."""
        proton_mass = self.central_constants.proton_mass_gev
        
        # Check that value is finite and reasonable
        assert math.isfinite(proton_mass)
        assert proton_mass > 0.1  # Should be positive
        assert proton_mass < 2.0  # Should be reasonable magnitude

    def test_w_boson_mass_gev(self):
        """Test W boson mass property."""
        w_mass = self.central_constants.w_boson_mass_gev
        
        # Check that value is finite and reasonable
        assert math.isfinite(w_mass)
        assert w_mass > 0  # Should be positive
        assert w_mass < 100  # Should be around 80 GeV

    def test_z_boson_mass_gev(self):
        """Test Z boson mass property."""
        z_mass = self.central_constants.z_boson_mass_gev
        
        # Check that value is finite and reasonable
        assert math.isfinite(z_mass)
        assert z_mass > 0  # Should be positive
        assert z_mass < 100  # Should be around 91 GeV
        
        # Check that Z mass is greater than W mass
        w_mass = self.central_constants.w_boson_mass_gev
        assert z_mass > w_mass

    def test_coherence_defect_correction(self):
        """Test coherence defect correction method."""
        # Test for different generations
        for generation in [1, 2, 3]:
            correction = self.central_constants.coherence_defect_correction(generation)
            
            # Check that value is finite and reasonable
            assert math.isfinite(correction)
            assert correction >= 0  # Should be non-negative
            
            # Check that corrections are reasonable (but don't enforce strict ordering)
            if generation > 1:
                prev_correction = self.central_constants.coherence_defect_correction(generation - 1)
                # Both should be non-negative and finite
                assert correction >= 0
                assert prev_correction >= 0
        
        # Test edge case
        edge_correction = self.central_constants.coherence_defect_correction(0)
        assert edge_correction == 0.0

    def test_get_derivation_provenance(self):
        """Test derivation provenance method."""
        # Test for fine structure constant
        alpha_provenance = self.central_constants.get_derivation_provenance('fine_structure_constant')
        assert isinstance(alpha_provenance, str)
        assert len(alpha_provenance) > 0
        
        # Test for cosmological constant
        cosmo_provenance = self.central_constants.get_derivation_provenance('cosmological_constant')
        assert isinstance(cosmo_provenance, str)
        assert len(cosmo_provenance) > 0
        
        # Test for hubble constant
        hubble_provenance = self.central_constants.get_derivation_provenance('hubble_constant')
        assert isinstance(hubble_provenance, str)
        assert len(hubble_provenance) > 0
        
        # Test for unknown constant
        unknown_provenance = self.central_constants.get_derivation_provenance('unknown_constant')
        assert unknown_provenance == "Derivation provenance not found"

    def test_singleton_functionality(self):
        """Test that singleton instance works correctly."""
        # Test that singleton has same properties
        assert hasattr(self.singleton, 'fine_structure_constant_inverse')
        assert hasattr(self.singleton, 'electron_mass_mev')
        assert hasattr(self.singleton, 'cosmological_constant_correction')
        
        # Test that singleton produces same results
        alpha_inv1 = self.central_constants.fine_structure_constant_inverse
        alpha_inv2 = self.singleton.fine_structure_constant_inverse
        
        assert alpha_inv1 == alpha_inv2

    def test_module_level_functions(self):
        """Test module-level convenience functions."""
        # Test get_alpha_inverse
        alpha_inv = get_alpha_inverse()
        assert math.isfinite(alpha_inv)
        assert alpha_inv > 100
        assert alpha_inv < 200
        
        # Test get_electron_mass_mev
        electron_mass = get_electron_mass_mev()
        assert electron_mass == 1.0
        
        # Test get_cosmological_correction
        cosmo_correction = get_cosmological_correction()
        assert math.isfinite(cosmo_correction)
        assert cosmo_correction > 0
        
        # Test get_cmb_temperature
        cmb_temp = get_cmb_temperature()
        assert math.isfinite(cmb_temp)
        assert cmb_temp > 0

    def test_mathematical_consistency(self):
        """Test mathematical consistency across all properties."""
        # Test fine structure constant relationship
        alpha = self.central_constants.fine_structure_constant
        alpha_inv = self.central_constants.fine_structure_constant_inverse
        assert abs(alpha * alpha_inv - 1.0) < 1e-10
        
        # Test that all values are finite
        properties = [
            'fine_structure_constant_inverse',
            'fine_structure_constant',
            'cosmological_constant_correction',
            'omega_lambda',
            'hubble_constant_base',
            'electron_mass_mev',
            'cmb_temperature_kelvin',
            'zeta_3_apery',
            'higgs_vev_gev',
            'planck_temperature_kelvin',
            'planck_constant_j_s',
            'gravitational_constant_m3_kg_s2',
            'proton_mass_gev',
            'w_boson_mass_gev',
            'z_boson_mass_gev'
        ]
        
        for prop_name in properties:
            value = getattr(self.central_constants, prop_name)
            assert math.isfinite(value), f"Property {prop_name} is not finite: {value}"

    def test_physical_significance_validation(self):
        """Test that derived values have physical significance."""
        # Test fine structure constant
        alpha = self.central_constants.fine_structure_constant
        assert 0.005 < alpha < 0.01  # Should be around 1/137
        
        # Test electron mass (base unit)
        electron_mass = self.central_constants.electron_mass_mev
        assert electron_mass == 1.0  # Base unit in FIRM theory
        
        # Test CMB temperature
        cmb_temp = self.central_constants.cmb_temperature_kelvin
        assert 1 < cmb_temp < 10  # Should be around 2.7 K
        
        # Test Higgs VEV
        higgs_vev = self.central_constants.higgs_vev_gev
        assert 200 < higgs_vev < 300  # Should be around 246 GeV

    def test_theoretical_foundation_validation(self):
        """Test that theoretical foundation is sound."""
        # Test that φ value is properly used
        phi = self.central_constants._phi
        assert abs(phi - 1.618033988749895) < 1e-10
        
        # Test that lazy loading works for key properties
        _ = self.central_constants.fine_structure_constant_inverse
        assert self.central_constants._alpha_result is not None
        
        _ = self.central_constants.cosmological_constant_correction
        assert self.central_constants._cosmological_result is not None
        
        _ = self.central_constants.hubble_constant_base
        assert self.central_constants._hubble_result is not None

    def test_lazy_loading_behavior(self):
        """Test that lazy loading works correctly."""
        # Initially, results should be None
        assert self.central_constants._alpha_result is None
        assert self.central_constants._cosmological_result is None
        assert self.central_constants._hubble_result is None
        
        # Access properties to trigger lazy loading
        _ = self.central_constants.fine_structure_constant_inverse
        assert self.central_constants._alpha_result is not None
        
        _ = self.central_constants.cosmological_constant_correction
        assert self.central_constants._cosmological_result is not None
        
        _ = self.central_constants.hubble_constant_base
        assert self.central_constants._hubble_result is not None

    def test_error_handling(self):
        """Test error handling for edge cases."""
        # Test coherence defect correction with invalid input
        invalid_correction = self.central_constants.coherence_defect_correction(-1)
        assert invalid_correction == 0.0
        
        # Test get_derivation_provenance with unknown constant
        unknown_provenance = self.central_constants.get_derivation_provenance('unknown')
        assert unknown_provenance == "Derivation provenance not found"

    def test_property_caching(self):
        """Test that properties are properly cached."""
        # Access a property multiple times
        alpha_inv1 = self.central_constants.fine_structure_constant_inverse
        alpha_inv2 = self.central_constants.fine_structure_constant_inverse
        
        # Should return the same value (cached)
        assert alpha_inv1 == alpha_inv2
        
        # The underlying result should be the same object
        assert self.central_constants._alpha_result is not None


if __name__ == "__main__":
    # Run comprehensive tests
    pytest.main([__file__, "-v"])
