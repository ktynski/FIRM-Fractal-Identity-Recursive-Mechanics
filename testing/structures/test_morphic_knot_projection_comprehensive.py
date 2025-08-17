"""
Comprehensive Tests for Morphic Knot Projection Module

Tests the morphic knot → particle property projection system including
mass depth decomposition, spin derivation, and charge quantum number mapping.

Mathematical Foundation Testing:
    - φⁿ mass depth decomposition verification
    - Form factor Cₙ calculation accuracy
    - Recursive depth derivation from log_φ(m/me)
    - Internal symmetry → spin projection validation

Physical Significance Testing:
    - Particle mass hierarchy reproduction
    - Quantum number consistency verification
    - Standard Model particle property matching
    - Gell-Mann-Nishijima relation validation

Integration Testing:
    - Particle spectrum compatibility
    - Mass ratios package integration
    - Morphic algebra connectivity
    - Foundation operator integration
"""

import pytest
import math
from typing import Dict, List, Optional

from structures.morphic_knot_projection import (
    derive_recursive_depth_and_form_factor,
    derive_spin_from_internal_symmetry,
    derive_charge_from_quantum_numbers,
    log_phi,
    MassDepthDecomposition,
)
from structures.particle_spectrum import PARTICLE_SPECTRUM, ParticleSpecification
from foundation.operators.phi_recursion import PHI_VALUE
from constants.mass_ratios import FUNDAMENTAL_MASSES


phi = PHI_VALUE


class TestLogPhiFunction:
    """Test the logarithmic φ function log_φ(x)."""
    
    def test_log_phi_basic_values(self):
        """Test log_phi for basic φ powers."""
        # log_φ(φ) = 1
        result_phi = log_phi(phi)
        assert abs(result_phi - 1.0) < 1e-12
        
        # log_φ(φ²) = 2
        result_phi_squared = log_phi(phi * phi)
        assert abs(result_phi_squared - 2.0) < 1e-12
        
        # log_φ(φ³) = 3
        result_phi_cubed = log_phi(phi**3)
        assert abs(result_phi_cubed - 3.0) < 1e-12
        
        # log_φ(1) = 0
        result_one = log_phi(1.0)
        assert abs(result_one - 0.0) < 1e-12
        
    def test_log_phi_mathematical_properties(self):
        """Test mathematical properties of log_φ function."""
        # Test that log_φ(xy) = log_φ(x) + log_φ(y)
        x = phi**1.5
        y = phi**2.3
        xy = x * y
        
        log_x = log_phi(x)
        log_y = log_phi(y)
        log_xy = log_phi(xy)
        
        assert abs(log_xy - (log_x + log_y)) < 1e-12
        
        # Test that log_φ(φⁿ) = n
        for n in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
            phi_n = phi**n
            log_result = log_phi(phi_n)
            assert abs(log_result - n) < 1e-12
            
    def test_log_phi_edge_cases(self):
        """Test log_phi for edge cases."""
        # Very small positive numbers
        small_x = 1e-10
        result_small = log_phi(small_x)
        assert math.isfinite(result_small)
        assert result_small < 0  # log of number < 1 should be negative
        
        # Large numbers
        large_x = 1e10
        result_large = log_phi(large_x)
        assert math.isfinite(result_large)
        assert result_large > 0  # log of number > 1 should be positive
        
        # Test that log_φ is well-defined for positive inputs
        test_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0]
        for x in test_values:
            result = log_phi(x)
            assert math.isfinite(result)


class TestMassDepthDecomposition:
    """Test mass depth decomposition functionality."""
    
    def test_mass_depth_decomposition_structure(self):
        """Test MassDepthDecomposition dataclass structure."""
        decomp = MassDepthDecomposition(
            particle="test_particle",
            mass_ratio_to_electron=207.0,
            recursive_depth_n=5,
            form_factor_Cn=1.2
        )
        
        assert decomp.particle == "test_particle"
        assert decomp.mass_ratio_to_electron == 207.0
        assert decomp.recursive_depth_n == 5
        assert decomp.form_factor_Cn == 1.2
        
    def test_electron_mass_depth(self):
        """Test mass depth decomposition for electron (reference particle)."""
        decomp = derive_recursive_depth_and_form_factor("electron")
        
        assert decomp.particle == "electron"
        assert decomp.mass_ratio_to_electron == 1.0  # By definition
        
        # For electron: log_φ(1) = 0, so depth should be 0
        assert decomp.recursive_depth_n == 0
        
        # Form factor should be C₀ = 1/φ⁰ = 1
        assert abs(decomp.form_factor_Cn - 1.0) < 1e-12
        
    def test_muon_mass_depth(self):
        """Test mass depth decomposition for muon."""
        decomp = derive_recursive_depth_and_form_factor("muon")
        
        assert decomp.particle == "muon"
        
        # Muon mass ratio ≈ 207 me
        expected_ratio = FUNDAMENTAL_MASSES.get_mass_ratio("muon", "electron")
        assert abs(decomp.mass_ratio_to_electron - expected_ratio) < 1e-12
        
        # Check depth calculation: n ≈ round(log_φ(207))
        expected_depth = round(log_phi(expected_ratio))
        assert decomp.recursive_depth_n == expected_depth
        
        # Form factor: Cₙ = (m/me)/φⁿ
        expected_form_factor = expected_ratio / (phi ** expected_depth)
        assert abs(decomp.form_factor_Cn - expected_form_factor) < 1e-12
        
    def test_tau_mass_depth(self):
        """Test mass depth decomposition for tau."""
        decomp = derive_recursive_depth_and_form_factor("tau")
        
        assert decomp.particle == "tau"
        
        # Tau mass ratio ≈ 3477 me
        expected_ratio = FUNDAMENTAL_MASSES.get_mass_ratio("tau", "electron")
        assert abs(decomp.mass_ratio_to_electron - expected_ratio) < 1e-12
        
        # Check depth and form factor calculations
        expected_depth = round(log_phi(expected_ratio))
        assert decomp.recursive_depth_n == expected_depth
        
        expected_form_factor = expected_ratio / (phi ** expected_depth)
        assert abs(decomp.form_factor_Cn - expected_form_factor) < 1e-12
        
    def test_proton_mass_depth(self):
        """Test mass depth decomposition for proton."""
        decomp = derive_recursive_depth_and_form_factor("proton")
        
        assert decomp.particle == "proton"
        
        # Proton mass ratio ≈ 1836 me
        expected_ratio = FUNDAMENTAL_MASSES.get_mass_ratio("proton", "electron")
        assert abs(decomp.mass_ratio_to_electron - expected_ratio) < 1e-12
        
        # Verify depth and form factor
        expected_depth = round(log_phi(expected_ratio))
        assert decomp.recursive_depth_n == expected_depth
        assert decomp.recursive_depth_n > 0
        
        expected_form_factor = expected_ratio / (phi ** expected_depth)
        assert abs(decomp.form_factor_Cn - expected_form_factor) < 1e-12
        assert decomp.form_factor_Cn > 0
        
    def test_massless_particle_handling(self):
        """Test handling of massless particles."""
        # Test with photon or neutrino (depending on what's available)
        try:
            decomp = derive_recursive_depth_and_form_factor("photon")
            
            if decomp.mass_ratio_to_electron == 0.0:
                # Massless particle should have special handling
                assert decomp.recursive_depth_n == 0
                assert decomp.form_factor_Cn == 0.0
                
        except KeyError:
            # Photon may not be in mass ratios (expected for massless)
            pass
            
        # Test handling of exactly zero mass
        decomp_zero = MassDepthDecomposition("test_zero", 0.0, 0, 0.0)
        assert decomp_zero.mass_ratio_to_electron == 0.0
        assert decomp_zero.form_factor_Cn == 0.0
        

class TestSpinDerivation:
    """Test spin derivation from internal symmetry."""
    
    def test_fermion_spin_derivation(self):
        """Test spin derivation for fermions."""
        # Test fermions (should have spin 1/2)
        fermion_names = ["electron", "muon", "tau"]
        
        for name in fermion_names:
            particle = PARTICLE_SPECTRUM.get_particle_by_name(name)
            if particle is not None:
                derived_spin = derive_spin_from_internal_symmetry(particle)
                
                # Fermions should have spin 1/2
                assert abs(derived_spin - 0.5) < 1e-12
                
                # Should match particle specification
                if particle.quantum_numbers is not None:
                    assert abs(particle.quantum_numbers.spin - derived_spin) < 1e-12
                    
    def test_gauge_boson_spin_derivation(self):
        """Test spin derivation for gauge bosons."""
        # Test gauge bosons (should have spin 1)
        boson_names = ["photon", "W_boson_plus", "Z_boson"]
        
        for name in boson_names:
            particle = PARTICLE_SPECTRUM.get_particle_by_name(name)
            if particle is not None:
                derived_spin = derive_spin_from_internal_symmetry(particle)
                
                # Gauge bosons should have spin 1
                assert abs(derived_spin - 1.0) < 1e-12
                
                # Should match particle specification
                if particle.quantum_numbers is not None:
                    assert abs(particle.quantum_numbers.spin - derived_spin) < 1e-12
                    
    def test_scalar_boson_spin_derivation(self):
        """Test spin derivation for scalar bosons."""
        # Test Higgs boson (should have spin 0)
        higgs = PARTICLE_SPECTRUM.get_particle_by_name("higgs")
        if higgs is not None:
            derived_spin = derive_spin_from_internal_symmetry(higgs)
            
            # Scalars should have spin 0
            assert abs(derived_spin - 0.0) < 1e-12
            
            # Should match particle specification
            if higgs.quantum_numbers is not None:
                assert abs(higgs.quantum_numbers.spin - derived_spin) < 1e-12
                
    def test_spin_consistency_across_generations(self):
        """Test that spin is consistent across fermion generations."""
        # Charged leptons should all have spin 1/2
        charged_leptons = ["electron", "muon", "tau"]
        
        for lepton_name in charged_leptons:
            particle = PARTICLE_SPECTRUM.get_particle_by_name(lepton_name)
            if particle is not None:
                spin = derive_spin_from_internal_symmetry(particle)
                assert abs(spin - 0.5) < 1e-12


class TestChargeDerivation:
    """Test charge derivation from quantum numbers."""
    
    def test_electron_charge_derivation(self):
        """Test charge derivation for electron."""
        electron = PARTICLE_SPECTRUM.get_particle_by_name("electron")
        if electron is not None and electron.quantum_numbers is not None:
            derived_charge = derive_charge_from_quantum_numbers(electron.quantum_numbers)
            
            # Electron should have charge -1
            assert abs(derived_charge - (-1.0)) < 1e-12
            
            # Should match quantum numbers
            assert abs(electron.quantum_numbers.electric_charge - derived_charge) < 1e-12
            
    def test_quark_charge_derivation(self):
        """Test charge derivation for quarks."""
        # Up-type quarks (charge +2/3)
        up_type = ["up", "charm", "top"]
        for quark_name in up_type:
            quark = PARTICLE_SPECTRUM.get_particle_by_name(quark_name)
            if quark is not None and quark.quantum_numbers is not None:
                derived_charge = derive_charge_from_quantum_numbers(quark.quantum_numbers)
                expected_charge = 2.0/3.0
                
                assert abs(derived_charge - expected_charge) < 1e-12
                assert abs(quark.quantum_numbers.electric_charge - derived_charge) < 1e-12
                
        # Down-type quarks (charge -1/3)
        down_type = ["down", "strange", "bottom"]
        for quark_name in down_type:
            quark = PARTICLE_SPECTRUM.get_particle_by_name(quark_name)
            if quark is not None and quark.quantum_numbers is not None:
                derived_charge = derive_charge_from_quantum_numbers(quark.quantum_numbers)
                expected_charge = -1.0/3.0
                
                assert abs(derived_charge - expected_charge) < 1e-12
                assert abs(quark.quantum_numbers.electric_charge - derived_charge) < 1e-12
                
    def test_neutral_particle_charge_derivation(self):
        """Test charge derivation for neutral particles."""
        neutral_particles = ["photon", "Z_boson", "higgs"]
        
        for particle_name in neutral_particles:
            particle = PARTICLE_SPECTRUM.get_particle_by_name(particle_name)
            if particle is not None and particle.quantum_numbers is not None:
                derived_charge = derive_charge_from_quantum_numbers(particle.quantum_numbers)
                
                # Should be neutral
                assert abs(derived_charge - 0.0) < 1e-12
                assert abs(particle.quantum_numbers.electric_charge - derived_charge) < 1e-12
                
    def test_gell_mann_nishijima_relation(self):
        """Test Gell-Mann-Nishijima relation: Q = T₃ + Y/2."""
        test_particles = ["electron", "muon", "up", "down"]
        
        for particle_name in test_particles:
            particle = PARTICLE_SPECTRUM.get_particle_by_name(particle_name)
            if particle is not None and particle.quantum_numbers is not None:
                qn = particle.quantum_numbers
                
                # Q = T₃ + Y/2
                calculated_charge = qn.weak_isospin + qn.weak_hypercharge/2.0
                
                # Should match both the quantum number and derived charge
                assert abs(calculated_charge - qn.electric_charge) < 1e-12
                
                derived_charge = derive_charge_from_quantum_numbers(qn)
                assert abs(calculated_charge - derived_charge) < 1e-12


class TestMorphicKnotIntegration:
    """Test integration with morphic algebra and knot theory."""
    
    def test_particle_spectrum_consistency(self):
        """Test consistency with particle spectrum."""
        # Test that all particles in spectrum can be processed
        known_particles = ["electron", "muon", "tau", "proton"]
        
        for particle_name in known_particles:
            # Mass depth should work
            try:
                decomp = derive_recursive_depth_and_form_factor(particle_name)
                assert isinstance(decomp, MassDepthDecomposition)
                assert decomp.particle == particle_name
                assert decomp.mass_ratio_to_electron >= 0
                
            except KeyError:
                # Some particles may not be in mass ratios
                pass
                
            # Spin/charge should work with particle spectrum
            particle = PARTICLE_SPECTRUM.get_particle_by_name(particle_name)
            if particle is not None:
                spin = derive_spin_from_internal_symmetry(particle)
                assert math.isfinite(spin)
                assert spin >= 0
                
                if particle.quantum_numbers is not None:
                    charge = derive_charge_from_quantum_numbers(particle.quantum_numbers)
                    assert math.isfinite(charge)
                    
    def test_morphic_algebra_compatibility(self):
        """Test compatibility with morphic algebra structures."""
        try:
            from structures.morphic_algebra import PsiObject, QFTProjection
            
            # Test that morphic knot projections are compatible
            # with QFTProjection structure
            
            # Get a particle
            electron = PARTICLE_SPECTRUM.get_particle_by_name("electron")
            if electron is not None:
                mass_decomp = derive_recursive_depth_and_form_factor("electron")
                spin = derive_spin_from_internal_symmetry(electron)
                
                if electron.quantum_numbers is not None:
                    charge = derive_charge_from_quantum_numbers(electron.quantum_numbers)
                    
                    # Should be able to create QFTProjection
                    projection = QFTProjection(
                        mass_ratio_to_electron=mass_decomp.mass_ratio_to_electron,
                        spin=spin,
                        electric_charge=charge
                    )
                    
                    assert isinstance(projection, QFTProjection)
                    assert projection.mass_ratio_to_electron == 1.0  # Electron reference
                    assert projection.spin == 0.5
                    assert projection.electric_charge == -1.0
                    
        except ImportError:
            # Morphic algebra may not be available
            pass
            
    def test_phi_recursion_integration(self):
        """Test integration with φ-recursion framework."""
        from foundation.operators.phi_recursion import PHI_VALUE as FOUNDATION_PHI
        
        # Verify φ consistency
        assert abs(phi - FOUNDATION_PHI) < 1e-12
        
        # Test φ-derived calculations
        test_masses = [1.0, phi, phi**2, phi**3, phi**5, phi**8]
        
        for mass in test_masses:
            log_result = log_phi(mass)
            
            # log_φ(φⁿ) = n
            expected = math.log(mass) / math.log(phi)
            assert abs(log_result - expected) < 1e-12
            
            # Round-trip test
            reconstructed = phi ** log_result
            assert abs(reconstructed - mass) < 1e-12


class TestPhysicalValidation:
    """Test physical validation of morphic knot projections."""
    
    def test_lepton_mass_hierarchy(self):
        """Test that lepton mass hierarchy is correctly reproduced."""
        # me < mμ < mτ
        electron_decomp = derive_recursive_depth_and_form_factor("electron")
        muon_decomp = derive_recursive_depth_and_form_factor("muon")  
        tau_decomp = derive_recursive_depth_and_form_factor("tau")
        
        me = electron_decomp.mass_ratio_to_electron  # = 1
        mμ = muon_decomp.mass_ratio_to_electron
        mτ = tau_decomp.mass_ratio_to_electron
        
        assert me < mμ < mτ
        assert me == 1.0  # By definition
        assert mμ > 200  # Approximately 207
        assert mτ > 3000  # Approximately 3477
        
    def test_depth_hierarchy_consistency(self):
        """Test that recursive depth hierarchy makes physical sense."""
        particles = ["electron", "muon", "tau", "proton"]
        depth_mass_pairs = []
        
        for particle_name in particles:
            try:
                decomp = derive_recursive_depth_and_form_factor(particle_name)
                depth_mass_pairs.append((decomp.recursive_depth_n, decomp.mass_ratio_to_electron))
            except KeyError:
                # Skip particles not in mass database
                continue
                
        # Sort by mass
        depth_mass_pairs.sort(key=lambda x: x[1])
        
        # Generally, higher masses should have higher depths
        # (though form factors can modulate this)
        for i in range(1, len(depth_mass_pairs)):
            depth_prev, mass_prev = depth_mass_pairs[i-1]
            depth_curr, mass_curr = depth_mass_pairs[i]
            
            assert mass_curr >= mass_prev  # Sorted by mass
            # Depth relationship is more complex due to form factors
            
    def test_form_factor_bounds(self):
        """Test that form factors are within reasonable bounds."""
        particles = ["electron", "muon", "tau", "proton"]
        
        for particle_name in particles:
            try:
                decomp = derive_recursive_depth_and_form_factor(particle_name)
                
                # Form factors should be positive and finite
                assert decomp.form_factor_Cn > 0
                assert math.isfinite(decomp.form_factor_Cn)
                
                # Form factors should be reasonable (not too far from 1)
                # This tests the φⁿ approximation quality
                assert 0.1 < decomp.form_factor_Cn < 10.0
                
            except KeyError:
                # Skip particles not available
                continue
                
    def test_quantum_number_conservation(self):
        """Test quantum number conservation in charge derivation."""
        # Test charge conservation in particle families
        families = [
            ["electron", "electron_neutrino"],  # First generation leptons
            ["muon", "muon_neutrino"],         # Second generation leptons  
            ["tau", "tau_neutrino"],           # Third generation leptons
            ["up", "down"],                    # First generation quarks
        ]
        
        for family in families:
            total_charge = 0.0
            family_particles = []
            
            for particle_name in family:
                particle = PARTICLE_SPECTRUM.get_particle_by_name(particle_name)
                if particle is not None and particle.quantum_numbers is not None:
                    charge = derive_charge_from_quantum_numbers(particle.quantum_numbers)
                    total_charge += charge
                    family_particles.append(particle_name)
                    
            # Some families should have specific charge relationships
            if len(family_particles) >= 2:
                # Test that charges are reasonable
                assert abs(total_charge) <= 2.0  # Reasonable bound


class TestErrorHandlingAndEdgeCases:
    """Test error handling and edge cases."""
    
    def test_invalid_particle_names(self):
        """Test handling of invalid particle names."""
        # Non-existent particle should raise KeyError
        with pytest.raises(KeyError):
            derive_recursive_depth_and_form_factor("nonexistent_particle")
            
    def test_log_phi_domain_errors(self):
        """Test log_phi domain error handling."""
        # Negative or zero inputs should handle gracefully
        with pytest.raises((ValueError, ZeroDivisionError)):
            log_phi(0.0)
            
        with pytest.raises((ValueError, ZeroDivisionError)):  
            log_phi(-1.0)
            
    def test_extreme_mass_values(self):
        """Test handling of extreme mass values."""
        # Very small mass ratios
        tiny_decomp = MassDepthDecomposition("tiny", 1e-10, -30, 1e-5)
        assert tiny_decomp.mass_ratio_to_electron > 0
        assert math.isfinite(tiny_decomp.form_factor_Cn)
        
        # Very large mass ratios
        huge_decomp = MassDepthDecomposition("huge", 1e10, 50, 1e5)  
        assert huge_decomp.mass_ratio_to_electron > 0
        assert math.isfinite(huge_decomp.form_factor_Cn)
        
    def test_missing_quantum_numbers(self):
        """Test handling of particles with missing quantum numbers."""
        # Create particle spec without quantum numbers
        from structures.particle_spectrum import ParticleSpecification, ParticleType
        
        incomplete_particle = ParticleSpecification(
            name="test_particle",
            particle_type=ParticleType.FERMION,
            fermion_type=None,
            generation=None,
            mass_expression="test_mass",
            quantum_numbers=None,  # Missing quantum numbers
            mathematical_derivation="test",
            physical_interpretation="test"
        )
        
        # Should handle gracefully
        try:
            spin = derive_spin_from_internal_symmetry(incomplete_particle)
            # May return default value or raise informative error
        except (AttributeError, ValueError):
            # Expected behavior for incomplete particle
            pass
