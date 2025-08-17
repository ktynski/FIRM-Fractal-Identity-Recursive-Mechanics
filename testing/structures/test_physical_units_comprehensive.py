"""
Comprehensive Tests for Physical Units Module

Tests the centralized physical units system with exact SI definitions,
unit conversions, and integration with the FIRM framework.

Mathematical Foundation Testing:
    - Exact SI definition verification (2019 redefinition)
    - Unit conversion accuracy and consistency
    - Derived unit calculations verification
    - Mathematical precision preservation

Physical Significance Testing:
    - Speed of light constant validation
    - Planck constant accuracy verification  
    - Boltzmann constant consistency
    - Elementary charge precision

Integration Testing:
    - Cross-module compatibility verification
    - Constants package integration
    - Conversion layer functionality
    - Academic verification compliance
"""

import pytest
import math
from typing import Dict, Any

from structures.physical_units import (
    PhysicalUnits,
    PHYSICAL_UNITS,
)


class TestPhysicalUnitsBasics:
    """Test basic physical units functionality."""
    
    def test_physical_units_singleton_exists(self):
        """Test that PHYSICAL_UNITS singleton exists and is initialized."""
        assert PHYSICAL_UNITS is not None
        assert isinstance(PHYSICAL_UNITS, PhysicalUnits)
        
    def test_physical_units_creation(self):
        """Test PhysicalUnits creation and initialization."""
        units = PhysicalUnits()
        assert isinstance(units, PhysicalUnits)
        
        # Test that it's a frozen dataclass
        with pytest.raises(AttributeError):
            units.C_LIGHT_M_PER_S = 300000000.0  # Should fail due to frozen=True


class TestSIDefinitions:
    """Test exact SI definitions (2019 redefinition)."""
    
    def test_speed_of_light_definition(self):
        """Test speed of light exact SI definition."""
        units = PHYSICAL_UNITS
        
        # Exact SI definition since 1983
        assert units.C_LIGHT_M_PER_S == 299_792_458.0
        
        # Should be exactly this value, not an approximation
        assert units.C_LIGHT_M_PER_S == 299792458
        assert isinstance(units.C_LIGHT_M_PER_S, float)
        
    def test_planck_constant_definition(self):
        """Test Planck constant exact SI definition."""
        units = PHYSICAL_UNITS
        
        # Exact SI definition since 2019 redefinition
        assert units.PLANCK_CONSTANT_J_S == 6.626_070_15e-34
        
        # Verify precision to required decimal places
        expected = 6.62607015e-34
        assert abs(units.PLANCK_CONSTANT_J_S - expected) < 1e-42
        assert isinstance(units.PLANCK_CONSTANT_J_S, float)
        
    def test_boltzmann_constant_definition(self):
        """Test Boltzmann constant exact SI definition."""
        units = PHYSICAL_UNITS
        
        # Exact SI definition since 2019 redefinition  
        assert units.BOLTZMANN_CONSTANT_J_PER_K == 1.380_649e-23
        
        # Verify precision
        expected = 1.380649e-23
        assert abs(units.BOLTZMANN_CONSTANT_J_PER_K - expected) < 1e-29
        assert isinstance(units.BOLTZMANN_CONSTANT_J_PER_K, float)
        
    def test_elementary_charge_definition(self):
        """Test elementary charge exact SI definition."""
        units = PHYSICAL_UNITS
        
        # Exact SI definition since 2019 redefinition
        assert units.ELEMENTARY_CHARGE_C == 1.602_176_634e-19
        
        # Verify precision
        expected = 1.602176634e-19
        assert abs(units.ELEMENTARY_CHARGE_C - expected) < 1e-27
        assert isinstance(units.ELEMENTARY_CHARGE_C, float)


class TestDerivedUnits:
    """Test derived unit calculations and conversions."""
    
    def test_planck_constant_ev_s(self):
        """Test Planck constant in eV·s derived unit."""
        units = PHYSICAL_UNITS
        
        h_ev_s = units.PLANCK_CONSTANT_EV_S
        
        # Should be h_J_s / e_C
        expected = units.PLANCK_CONSTANT_J_S / units.ELEMENTARY_CHARGE_C
        assert abs(h_ev_s - expected) < 1e-36
        
        # Verify reasonable magnitude (≈ 4.136 × 10⁻¹⁵ eV·s)
        assert h_ev_s > 4.0e-15
        assert h_ev_s < 4.2e-15
        assert math.isfinite(h_ev_s)
        
    def test_boltzmann_constant_ev_per_k(self):
        """Test Boltzmann constant in eV/K derived unit."""
        units = PHYSICAL_UNITS
        
        k_ev_k = units.BOLTZMANN_CONSTANT_EV_PER_K
        
        # Should be k_J_K / e_C
        expected = units.BOLTZMANN_CONSTANT_J_PER_K / units.ELEMENTARY_CHARGE_C
        assert abs(k_ev_k - expected) < 1e-29
        
        # Verify reasonable magnitude (≈ 8.617 × 10⁻⁵ eV/K)
        assert k_ev_k > 8.0e-5
        assert k_ev_k < 9.0e-5
        assert math.isfinite(k_ev_k)
        
    def test_derived_unit_consistency(self):
        """Test consistency between base and derived units."""
        units = PHYSICAL_UNITS
        
        # Test that derived calculations are consistent
        h_j_s = units.PLANCK_CONSTANT_J_S
        h_ev_s = units.PLANCK_CONSTANT_EV_S
        e_c = units.ELEMENTARY_CHARGE_C
        
        # h_j_s = h_ev_s × e_c
        reconstructed_h_j_s = h_ev_s * e_c
        assert abs(h_j_s - reconstructed_h_j_s) < 1e-42
        
        # Same for Boltzmann constant
        k_j_k = units.BOLTZMANN_CONSTANT_J_PER_K
        k_ev_k = units.BOLTZMANN_CONSTANT_EV_PER_K
        
        reconstructed_k_j_k = k_ev_k * e_c
        assert abs(k_j_k - reconstructed_k_j_k) < 1e-29


class TestUnitConversions:
    """Test unit conversion calculations."""
    
    def test_energy_unit_conversions(self):
        """Test energy unit conversions (J ↔ eV)."""
        units = PHYSICAL_UNITS
        
        # 1 eV = e × 1 V = elementary charge in Joules
        one_ev_in_joules = units.ELEMENTARY_CHARGE_C
        assert one_ev_in_joules == units.ELEMENTARY_CHARGE_C
        
        # 1 J in eV
        one_joule_in_ev = 1.0 / units.ELEMENTARY_CHARGE_C
        assert abs(one_joule_in_ev - 6.241509074e18) < 1e12  # Approximate value
        
    def test_temperature_energy_conversions(self):
        """Test temperature-energy conversions."""
        units = PHYSICAL_UNITS
        
        # Room temperature ≈ 300 K
        room_temp_k = 300.0
        room_temp_ev = room_temp_k * units.BOLTZMANN_CONSTANT_EV_PER_K
        
        # Should be approximately 0.026 eV
        assert room_temp_ev > 0.025
        assert room_temp_ev < 0.027
        assert math.isfinite(room_temp_ev)
        
        # Test conversion consistency
        back_to_kelvin = room_temp_ev / units.BOLTZMANN_CONSTANT_EV_PER_K
        assert abs(back_to_kelvin - room_temp_k) < 1e-12
        
    def test_frequency_energy_conversions(self):
        """Test frequency-energy conversions via Planck constant."""
        units = PHYSICAL_UNITS
        
        # Test E = h × f conversion
        frequency_hz = 1e15  # 1 PHz
        energy_j = units.PLANCK_CONSTANT_J_S * frequency_hz
        energy_ev = units.PLANCK_CONSTANT_EV_S * frequency_hz
        
        # Should be consistent
        energy_ev_from_j = energy_j / units.ELEMENTARY_CHARGE_C
        assert abs(energy_ev - energy_ev_from_j) < 1e-12
        
        # Verify reasonable magnitudes
        assert energy_j > 6e-19  # Order of magnitude check
        assert energy_j < 7e-19
        assert energy_ev > 4.0    # About 4 eV
        assert energy_ev < 5.0


class TestPhysicalConstantRelationships:
    """Test relationships between physical constants."""
    
    def test_fundamental_constant_scales(self):
        """Test that fundamental constants have correct relative scales."""
        units = PHYSICAL_UNITS
        
        # Speed of light >> other constants in SI base units
        assert units.C_LIGHT_M_PER_S > 1e8
        
        # Planck constant is very small
        assert units.PLANCK_CONSTANT_J_S < 1e-30
        
        # Elementary charge is small but larger than Planck constant
        assert units.ELEMENTARY_CHARGE_C > units.PLANCK_CONSTANT_J_S
        assert units.ELEMENTARY_CHARGE_C < 1e-15
        
        # Boltzmann constant is small
        assert units.BOLTZMANN_CONSTANT_J_PER_K < 1e-20
        
    def test_natural_unit_relationships(self):
        """Test relationships relevant for natural units."""
        units = PHYSICAL_UNITS
        
        # In natural units, ħ = c = k = 1
        # Test that our constants can form these relationships
        
        h_bar = units.PLANCK_CONSTANT_J_S / (2 * math.pi)
        c = units.C_LIGHT_M_PER_S
        k = units.BOLTZMANN_CONSTANT_J_PER_K
        
        # All should be positive and finite
        assert h_bar > 0 and math.isfinite(h_bar)
        assert c > 0 and math.isfinite(c)
        assert k > 0 and math.isfinite(k)
        
        # Test some dimensionless combinations
        fine_structure_like = units.ELEMENTARY_CHARGE_C**2 / (4 * math.pi)
        assert fine_structure_like > 0
        assert math.isfinite(fine_structure_like)
        
    def test_planck_units_foundation(self):
        """Test foundation for Planck unit calculations."""
        units = PHYSICAL_UNITS
        
        # Planck units would be derived from ħ, c, G
        # We have ħ and c, test their combination makes sense
        
        h_bar = units.PLANCK_CONSTANT_J_S / (2 * math.pi)
        c = units.C_LIGHT_M_PER_S
        
        # Characteristic scale from ħc
        hbar_c = h_bar * c  # Has units of J·m
        assert hbar_c > 0
        assert math.isfinite(hbar_c)
        
        # Should be around 2e-25 J·m
        assert hbar_c > 1e-26
        assert hbar_c < 1e-24


class TestSingletonConsistency:
    """Test singleton consistency and immutability."""
    
    def test_singleton_identity(self):
        """Test that PHYSICAL_UNITS is a consistent singleton."""
        # Import multiple times to verify same object
        from structures.physical_units import PHYSICAL_UNITS as UNITS_1
        from structures.physical_units import PHYSICAL_UNITS as UNITS_2
        
        assert UNITS_1 is UNITS_2
        assert UNITS_1 is PHYSICAL_UNITS
        
    def test_dataclass_immutability(self):
        """Test that PhysicalUnits dataclass is properly frozen."""
        units = PHYSICAL_UNITS
        
        # Attempt to modify should fail
        with pytest.raises(AttributeError):
            units.C_LIGHT_M_PER_S = 300000000.0
            
        with pytest.raises(AttributeError):  
            units.PLANCK_CONSTANT_J_S = 7e-34
            
        with pytest.raises(AttributeError):
            units.new_constant = 42.0
            
    def test_property_consistency(self):
        """Test that derived properties are consistent across calls."""
        units = PHYSICAL_UNITS
        
        # Multiple calls to same property should give same result
        h_ev_s_1 = units.PLANCK_CONSTANT_EV_S
        h_ev_s_2 = units.PLANCK_CONSTANT_EV_S
        assert h_ev_s_1 == h_ev_s_2
        
        k_ev_k_1 = units.BOLTZMANN_CONSTANT_EV_PER_K
        k_ev_k_2 = units.BOLTZMANN_CONSTANT_EV_PER_K
        assert k_ev_k_1 == k_ev_k_2


class TestIntegrationWithFIRM:
    """Test integration with other FIRM framework components."""
    
    def test_constants_package_compatibility(self):
        """Test compatibility with constants package if available."""
        try:
            from constants import fine_structure_alpha
            
            units = PHYSICAL_UNITS
            
            # Should be able to use physical units with constants
            # Test basic compatibility
            assert units.ELEMENTARY_CHARGE_C > 0
            assert math.isfinite(units.ELEMENTARY_CHARGE_C)
            
        except ImportError:
            # Constants integration may not be available
            pass
            
    def test_dimensional_bridge_compatibility(self):
        """Test compatibility with dimensional bridge if available."""
        try:
            from structures.dimensional_bridge import DIMENSIONAL_BRIDGE
            
            units = PHYSICAL_UNITS
            
            # Physical units should be compatible with dimensional analysis
            # Test basic coexistence
            assert units.C_LIGHT_M_PER_S > 0
            assert DIMENSIONAL_BRIDGE is not None
            
        except ImportError:
            # Dimensional bridge may not be available
            pass
            
    def test_phi_mathematics_independence(self):
        """Test that physical units are independent of φ-mathematics."""
        from foundation.operators.phi_recursion import PHI_VALUE
        
        units = PHYSICAL_UNITS
        
        # Physical units should be exact SI definitions, not φ-derived
        # This tests the provenance principle: no empirical contamination
        
        # Test that unit values are exact, not φ-scaled
        assert units.C_LIGHT_M_PER_S == 299792458.0  # Exact
        assert units.PLANCK_CONSTANT_J_S == 6.62607015e-34  # Exact
        
        # Verify independence from φ
        assert abs(units.C_LIGHT_M_PER_S / PHI_VALUE - 185410664.6) > 100  # Not φ-related
        
    def test_academic_verification_compliance(self):
        """Test compliance with academic verification requirements."""
        units = PHYSICAL_UNITS
        
        # All values should match CODATA 2018/SI 2019 exactly
        # These are not empirical inputs but definitional constants
        
        # Verify exact SI definitions (post-2019 redefinition)
        si_2019_values = {
            'c': 299792458.0,                    # m/s (exact)
            'h': 6.62607015e-34,                 # J⋅s (exact)
            'e': 1.602176634e-19,                # C (exact)  
            'k': 1.380649e-23,                   # J/K (exact)
        }
        
        assert units.C_LIGHT_M_PER_S == si_2019_values['c']
        assert units.PLANCK_CONSTANT_J_S == si_2019_values['h']
        assert units.ELEMENTARY_CHARGE_C == si_2019_values['e']
        assert units.BOLTZMANN_CONSTANT_J_PER_K == si_2019_values['k']


class TestNumericalPrecision:
    """Test numerical precision and accuracy."""
    
    def test_floating_point_precision(self):
        """Test that constants maintain full floating-point precision."""
        units = PHYSICAL_UNITS
        
        # Test that we're not losing precision in storage
        c_exact = 299792458.0
        h_exact = 6.62607015e-34
        e_exact = 1.602176634e-19
        k_exact = 1.380649e-23
        
        # Should be exactly equal (no precision loss)
        assert units.C_LIGHT_M_PER_S == c_exact
        assert units.PLANCK_CONSTANT_J_S == h_exact  
        assert units.ELEMENTARY_CHARGE_C == e_exact
        assert units.BOLTZMANN_CONSTANT_J_PER_K == k_exact
        
    def test_derived_calculation_precision(self):
        """Test precision in derived unit calculations."""
        units = PHYSICAL_UNITS
        
        # Test that derived calculations maintain precision
        h_ev_s = units.PLANCK_CONSTANT_EV_S
        k_ev_k = units.BOLTZMANN_CONSTANT_EV_PER_K
        
        # Should be computed to full precision
        h_expected = units.PLANCK_CONSTANT_J_S / units.ELEMENTARY_CHARGE_C
        k_expected = units.BOLTZMANN_CONSTANT_J_PER_K / units.ELEMENTARY_CHARGE_C
        
        assert abs(h_ev_s - h_expected) < 1e-15 * abs(h_expected)  # Relative precision
        assert abs(k_ev_k - k_expected) < 1e-15 * abs(k_expected)  # Relative precision
        
    def test_no_approximations(self):
        """Test that no approximations are used in unit definitions."""
        units = PHYSICAL_UNITS
        
        # These should be exact values, not approximations
        # No rounding or truncation should be present
        
        c_str = f"{units.C_LIGHT_M_PER_S:.0f}"
        assert c_str == "299792458"  # Exact integer
        
        # Planck constant should have full precision
        h_str = f"{units.PLANCK_CONSTANT_J_S:.15e}"
        assert "6.626070150000000e-34" in h_str
        
        # Elementary charge should have full precision  
        e_str = f"{units.ELEMENTARY_CHARGE_C:.15e}"
        assert "1.602176634000000e-19" in e_str
        
    def test_mathematical_relationships(self):
        """Test exact mathematical relationships between constants."""
        units = PHYSICAL_UNITS
        
        # Test exact conversion relationships
        j_to_ev = 1.0 / units.ELEMENTARY_CHARGE_C
        ev_to_j = units.ELEMENTARY_CHARGE_C
        
        # Should be exact inverses
        assert abs(j_to_ev * ev_to_j - 1.0) < 1e-15
        
        # Test derived unit relationships
        h_j_s = units.PLANCK_CONSTANT_J_S
        h_ev_s = units.PLANCK_CONSTANT_EV_S
        e_c = units.ELEMENTARY_CHARGE_C
        
        # h_j_s = h_ev_s × e_c (exact relationship)
        assert abs(h_j_s - h_ev_s * e_c) < 1e-15 * abs(h_j_s)


class TestErrorHandlingAndEdgeCases:
    """Test error handling and edge cases."""
    
    def test_zero_division_protection(self):
        """Test protection against zero division in derived calculations."""
        # This is mainly a design test - our constants are non-zero
        units = PHYSICAL_UNITS
        
        # All fundamental constants should be non-zero
        assert units.C_LIGHT_M_PER_S != 0.0
        assert units.PLANCK_CONSTANT_J_S != 0.0
        assert units.ELEMENTARY_CHARGE_C != 0.0
        assert units.BOLTZMANN_CONSTANT_J_PER_K != 0.0
        
        # Derived calculations should work without zero division
        h_ev_s = units.PLANCK_CONSTANT_EV_S
        k_ev_k = units.BOLTZMANN_CONSTANT_EV_PER_K
        
        assert math.isfinite(h_ev_s)
        assert math.isfinite(k_ev_k)
        assert h_ev_s != 0.0
        assert k_ev_k != 0.0
        
    def test_infinite_and_nan_protection(self):
        """Test protection against infinite and NaN values."""
        units = PHYSICAL_UNITS
        
        # All constants should be finite
        constants = [
            units.C_LIGHT_M_PER_S,
            units.PLANCK_CONSTANT_J_S, 
            units.ELEMENTARY_CHARGE_C,
            units.BOLTZMANN_CONSTANT_J_PER_K,
        ]
        
        for constant in constants:
            assert math.isfinite(constant)
            assert not math.isnan(constant)
            assert not math.isinf(constant)
            
        # Derived properties should also be finite
        derived = [
            units.PLANCK_CONSTANT_EV_S,
            units.BOLTZMANN_CONSTANT_EV_PER_K,
        ]
        
        for value in derived:
            assert math.isfinite(value)
            assert not math.isnan(value)
            assert not math.isinf(value)
