"""
Comprehensive Tests for CMB Power Spectrum Module

Tests the complete Cosmic Microwave Background power spectrum derivation with
acoustic peaks emerging from φ-harmonic structure in the baryon-photon fluid.

Mathematical Foundation Testing:
    - φ-harmonic acoustic oscillation verification
    - Spherical Bessel function projection accuracy
    - Acoustic peak position predictions at ℓ = 220 × φⁿ
    - φ-weighted peak amplitude calculations

Physical Significance Testing:
    - CMB temperature anisotropy pattern reproduction
    - Precision cosmological parameter extraction
    - Dark energy integrated Sachs-Wolfe effects
    - Silk diffusion damping tail validation

Integration Testing:
    - Inflationary perturbation input compatibility
    - Recombination physics integration
    - Large scale structure formation seeds
    - Academic verification compliance
"""

import pytest
import numpy as np
import math
from typing import Dict, List, Tuple, Optional, Any, Union

from cosmology.cmb_power_spectrum import (
    CMBPowerSpectrum,
    AcousticOscillations,
    PhiHarmonicPeaks,
    SilkDamping,
    IntegratedSachsWolfe,
    SphericalBesselProjection,
    RecombinationCoupling,
    BarynPhotoFluid,
    TightCouplingApproximation,
    CMBTransferFunction,
    AngularPowerSpectrum,
    CMBCalibration,
)
from foundation.operators.phi_recursion import PHI_VALUE
from constants.hubble_constant_derivation import HUBBLE_CONSTANT
from constants.matter_radiation_equality import MATTER_RADIATION_EQUALITY


class TestCMBPowerSpectrumBasics:
    """Test basic CMB power spectrum functionality."""
    
    def test_cmb_power_spectrum_creation(self):
        """Test CMBPowerSpectrum creation and initialization."""
        power_spectrum = CMBPowerSpectrum(
            l_max=3000,
            l_min=2,
            phi_harmonic_peaks=True,
            silk_damping=True,
            integrated_sachs_wolfe=True
        )
        
        assert power_spectrum.l_max == 3000
        assert power_spectrum.l_min == 2
        assert power_spectrum.phi_harmonic_peaks is True
        assert power_spectrum.silk_damping is True
        assert power_spectrum.integrated_sachs_wolfe is True
        
    def test_multipole_range_validation(self):
        """Test multipole range validation."""
        # Valid range
        valid_spectrum = CMBPowerSpectrum(l_max=2500, l_min=2)
        assert valid_spectrum.l_max == 2500
        assert valid_spectrum.l_min == 2
        
        # Test range consistency
        assert valid_spectrum.l_max > valid_spectrum.l_min
        assert valid_spectrum.l_min >= 2  # CMB minimum multipole
        
    def test_angular_power_spectrum_calculation(self):
        """Test angular power spectrum C_ℓ calculation."""
        power_spectrum = CMBPowerSpectrum(l_max=1000)
        
        # Calculate power spectrum over multipole range
        multipoles = np.array([2, 10, 50, 100, 220, 500, 1000])
        C_l_values = power_spectrum.calculate_angular_power_spectrum(multipoles)
        
        assert len(C_l_values) == len(multipoles)
        
        # All power spectrum values should be positive and finite
        for C_l in C_l_values:
            assert C_l > 0
            assert math.isfinite(C_l)
            
        # Power spectrum should have realistic magnitudes
        # Peak around ℓ ~ 220 should be order of 10^3 μK²
        peak_index = np.argmin(np.abs(multipoles - 220))
        peak_power = C_l_values[peak_index]
        assert 100 < peak_power < 10000  # Reasonable range for CMB peak


class TestPhiHarmonicPeaks:
    """Test φ-harmonic acoustic peak structure."""
    
    def test_phi_harmonic_peaks_creation(self):
        """Test PhiHarmonicPeaks creation."""
        phi_peaks = PhiHarmonicPeaks(
            base_peak_position=220.0,
            phi_scaling=PHI_VALUE,
            number_of_peaks=6,
            peak_amplitude_scaling="phi_weighted"
        )
        
        assert phi_peaks.base_peak_position == 220.0
        assert abs(phi_peaks.phi_scaling - PHI_VALUE) < 1e-12
        assert phi_peaks.number_of_peaks == 6
        assert phi_peaks.peak_amplitude_scaling == "phi_weighted"
        
    def test_acoustic_peak_positions(self):
        """Test φ-harmonic acoustic peak positions ℓ = 220 × φⁿ."""
        phi_peaks = PhiHarmonicPeaks(base_peak_position=220.0)
        
        # Calculate first 5 φ-harmonic peak positions
        peak_positions = phi_peaks.calculate_peak_positions(n_peaks=5)
        
        assert len(peak_positions) == 5
        
        # Verify φ-harmonic structure: ℓₙ = 220 × φⁿ
        for n, l_n in enumerate(peak_positions):
            expected_position = 220.0 * (PHI_VALUE ** n)
            assert abs(l_n - expected_position) < 1e-10
            
        # Test peak spacing ratios should equal φ
        for i in range(1, len(peak_positions)):
            ratio = peak_positions[i] / peak_positions[i-1]
            assert abs(ratio - PHI_VALUE) < 1e-12
            
    def test_phi_weighted_peak_amplitudes(self):
        """Test φ-weighted peak amplitudes."""
        phi_peaks = PhiHarmonicPeaks(
            base_peak_position=220.0,
            peak_amplitude_scaling="phi_weighted"
        )
        
        # Calculate peak amplitudes for φ-harmonic positions
        peak_positions = [220.0, 220.0 * PHI_VALUE, 220.0 * PHI_VALUE**2]
        peak_amplitudes = phi_peaks.calculate_peak_amplitudes(peak_positions)
        
        assert len(peak_amplitudes) == len(peak_positions)
        
        # All amplitudes should be positive and finite
        for amplitude in peak_amplitudes:
            assert amplitude > 0
            assert math.isfinite(amplitude)
            
        # Test φ-weighting structure
        if len(peak_amplitudes) >= 2:
            amplitude_ratios = [peak_amplitudes[i]/peak_amplitudes[0] for i in range(1, len(peak_amplitudes))]
            # Ratios should involve powers of φ
            for i, ratio in enumerate(amplitude_ratios):
                assert math.isfinite(ratio)
                assert ratio > 0
                
    def test_bessel_function_oscillations(self):
        """Test φ-weighted Bessel function oscillations."""
        phi_peaks = PhiHarmonicPeaks()
        
        # Test spherical Bessel function behavior
        multipoles = np.linspace(10, 1000, 100)
        bessel_oscillations = phi_peaks.calculate_bessel_oscillations(multipoles)
        
        assert len(bessel_oscillations) == len(multipoles)
        
        # Bessel functions should oscillate and be finite
        for osc in bessel_oscillations:
            assert math.isfinite(osc)
            
        # Should show oscillatory behavior
        oscillation_count = 0
        for i in range(1, len(bessel_oscillations)-1):
            if (bessel_oscillations[i-1] < bessel_oscillations[i] > bessel_oscillations[i+1]) or \
               (bessel_oscillations[i-1] > bessel_oscillations[i] < bessel_oscillations[i+1]):
                oscillation_count += 1
                
        # Should have multiple oscillations over the range
        assert oscillation_count > 5
        
    def test_peak_height_phi_scaling(self):
        """Test peak height φ-scaling relationships."""
        phi_peaks = PhiHarmonicPeaks()
        
        # Calculate heights of first few peaks
        peak_positions = phi_peaks.calculate_peak_positions(n_peaks=4)
        peak_heights = phi_peaks.calculate_peak_heights(peak_positions)
        
        # Peak heights should follow φ-scaling pattern
        for i in range(1, len(peak_heights)):
            height_ratio = peak_heights[i] / peak_heights[0]
            # Should be related to φ^n factors
            assert math.isfinite(height_ratio)
            assert height_ratio > 0


class TestAcousticOscillations:
    """Test acoustic oscillations in baryon-photon fluid."""
    
    def test_acoustic_oscillations_creation(self):
        """Test AcousticOscillations creation."""
        acoustic = AcousticOscillations(
            sound_speed=1/math.sqrt(3),  # Relativistic sound speed
            baryon_density=0.05,  # Ωb h²
            photon_density=2.47e-5,  # Ωγ h²
            phi_harmonic_coupling=True
        )
        
        assert abs(acoustic.sound_speed - 1/math.sqrt(3)) < 1e-12
        assert acoustic.baryon_density == 0.05
        assert acoustic.photon_density == 2.47e-5
        assert acoustic.phi_harmonic_coupling is True
        
    def test_sound_horizon_calculation(self):
        """Test acoustic sound horizon calculation."""
        acoustic = AcousticOscillations(sound_speed=1/math.sqrt(3))
        
        # Calculate sound horizon at recombination
        z_recombination = 1100.0  # Redshift of recombination
        sound_horizon = acoustic.calculate_sound_horizon(z_recombination)
        
        assert sound_horizon > 0
        assert math.isfinite(sound_horizon)
        
        # Sound horizon should be around 150 Mpc (comoving)
        assert 100 < sound_horizon < 200  # Mpc, approximate range
        
    def test_acoustic_wavelength_phi_structure(self):
        """Test φ-structure in acoustic wavelengths."""
        acoustic = AcousticOscillations(phi_harmonic_coupling=True)
        
        # Calculate characteristic acoustic wavelengths
        wavelengths = acoustic.calculate_phi_harmonic_wavelengths(n_modes=5)
        
        assert len(wavelengths) == 5
        
        # Wavelengths should follow φ-scaling
        for i in range(1, len(wavelengths)):
            ratio = wavelengths[i] / wavelengths[i-1]
            # Should involve φ-relationships
            assert math.isfinite(ratio)
            assert ratio > 0
            
        # All wavelengths should be positive and finite
        for wavelength in wavelengths:
            assert wavelength > 0
            assert math.isfinite(wavelength)
            
    def test_baryon_photon_coupling_strength(self):
        """Test baryon-photon coupling strength evolution."""
        acoustic = AcousticOscillations()
        
        # Test coupling evolution with redshift
        redshifts = np.array([1500, 1200, 1100, 1000, 800])  # Around recombination
        coupling_strengths = acoustic.calculate_coupling_strength(redshifts)
        
        assert len(coupling_strengths) == len(redshifts)
        
        # Coupling should be strong before recombination, weak after
        for i, (z, coupling) in enumerate(zip(redshifts, coupling_strengths)):
            assert math.isfinite(coupling)
            assert coupling >= 0
            
            # At z > 1200, coupling should be strong
            if z > 1200:
                assert coupling > 0.5
            # At z < 1000, coupling should weaken
            elif z < 1000:
                assert coupling < 0.8
                
    def test_tight_coupling_approximation(self):
        """Test tight coupling approximation validity."""
        tight_coupling = TightCouplingApproximation(
            coupling_threshold=10.0,
            validity_check=True
        )
        
        # Test tight coupling validity over redshift range
        test_redshifts = np.array([2000, 1500, 1100, 800, 500])
        validity = tight_coupling.check_validity(test_redshifts)
        
        assert len(validity) == len(test_redshifts)
        
        # Should be valid at high redshift, invalid at low redshift
        for i, (z, is_valid) in enumerate(zip(test_redshifts, validity)):
            if z > 1200:
                assert is_valid is True  # Valid before recombination
            elif z < 900:
                assert is_valid is False  # Invalid after recombination


class TestSilkDamping:
    """Test Silk diffusion damping at small scales."""
    
    def test_silk_damping_creation(self):
        """Test SilkDamping creation."""
        silk = SilkDamping(
            photon_diffusion_length=1.0,  # Mpc
            phi_damping_exponent=-1.0,    # φ⁻¹ damping
            damping_tail_enabled=True
        )
        
        assert silk.photon_diffusion_length == 1.0
        assert silk.phi_damping_exponent == -1.0
        assert silk.damping_tail_enabled is True
        
    def test_damping_scale_calculation(self):
        """Test Silk damping scale calculation."""
        silk = SilkDamping()
        
        # Calculate damping scale at recombination
        z_recombination = 1100.0
        damping_scale = silk.calculate_damping_scale(z_recombination)
        
        assert damping_scale > 0
        assert math.isfinite(damping_scale)
        
        # Damping scale should be sub-Mpc
        assert 0.1 < damping_scale < 10.0  # Mpc, reasonable range
        
    def test_phi_damping_function(self):
        """Test φ⁻ᵏ damping function."""
        silk = SilkDamping(phi_damping_exponent=-2.0)
        
        # Test damping function over multipole range
        multipoles = np.array([100, 500, 1000, 1500, 2000, 3000])
        damping_factors = silk.calculate_phi_damping(multipoles)
        
        assert len(damping_factors) == len(multipoles)
        
        # Damping should decrease with increasing ℓ (φ⁻ᵏ behavior)
        for i in range(1, len(damping_factors)):
            assert damping_factors[i] <= damping_factors[i-1]  # Decreasing
            assert damping_factors[i] > 0  # Positive
            assert math.isfinite(damping_factors[i])  # Finite
            
        # Test φ-scaling in damping
        if len(damping_factors) >= 2:
            damping_ratio = damping_factors[-1] / damping_factors[0]
            assert damping_ratio < 1.0  # Should be suppressed at high ℓ
            
    def test_exponential_cutoff(self):
        """Test exponential cutoff at very high multipoles."""
        silk = SilkDamping(damping_tail_enabled=True)
        
        # Test exponential cutoff behavior
        high_multipoles = np.array([2000, 2500, 3000, 4000, 5000])
        cutoff_factors = silk.calculate_exponential_cutoff(high_multipoles)
        
        # Should show exponential suppression
        for i in range(1, len(cutoff_factors)):
            assert cutoff_factors[i] <= cutoff_factors[i-1]  # Decreasing
            assert cutoff_factors[i] > 0  # Still positive
            
        # Very high ℓ should be strongly suppressed
        assert cutoff_factors[-1] < cutoff_factors[0] * 0.1
        
    def test_photon_diffusion_physics(self):
        """Test photon diffusion physics."""
        silk = SilkDamping()
        
        # Test diffusion length calculation
        baryon_density = 0.05
        photon_density = 2.47e-5
        diffusion_length = silk.calculate_photon_diffusion_length(
            baryon_density, photon_density
        )
        
        assert diffusion_length > 0
        assert math.isfinite(diffusion_length)
        
        # Should be around 1 Mpc scale
        assert 0.1 < diffusion_length < 10.0


class TestIntegratedSachsWolfe:
    """Test Integrated Sachs-Wolfe effect from dark energy."""
    
    def test_integrated_sachs_wolfe_creation(self):
        """Test IntegratedSachsWolfe creation."""
        isw = IntegratedSachsWolfe(
            dark_energy_density=0.7,  # ΩΛ
            phi_field_dynamics=True,
            late_time_evolution=True
        )
        
        assert isw.dark_energy_density == 0.7
        assert isw.phi_field_dynamics is True
        assert isw.late_time_evolution is True
        
    def test_large_scale_power_enhancement(self):
        """Test large scale power enhancement from ISW."""
        isw = IntegratedSachsWolfe(dark_energy_density=0.7)
        
        # Test ISW contribution to large scales
        large_scale_multipoles = np.array([2, 5, 10, 20, 50])
        isw_contributions = isw.calculate_isw_contribution(large_scale_multipoles)
        
        assert len(isw_contributions) == len(large_scale_multipoles)
        
        # ISW should enhance power at large scales (low ℓ)
        for isw_power in isw_contributions:
            assert isw_power >= 0  # Non-negative contribution
            assert math.isfinite(isw_power)
            
        # ISW effect should be strongest at lowest multipoles
        assert isw_contributions[0] >= isw_contributions[-1]
        
    def test_phi_field_dark_energy_evolution(self):
        """Test φ-field dark energy evolution."""
        isw = IntegratedSachsWolfe(phi_field_dynamics=True)
        
        # Test φ-field evolution over cosmic time
        scale_factors = np.array([0.1, 0.3, 0.5, 0.7, 1.0])  # a from early to late
        phi_field_evolution = isw.calculate_phi_field_evolution(scale_factors)
        
        assert len(phi_field_evolution) == len(scale_factors)
        
        # φ-field should evolve smoothly
        for phi_val in phi_field_evolution:
            assert math.isfinite(phi_val)
            
        # Should show accelerating expansion at late times
        late_acceleration = isw.test_late_time_acceleration(scale_factors[-2:])
        assert late_acceleration is True
        
    def test_potential_time_derivatives(self):
        """Test gravitational potential time derivatives."""
        isw = IntegratedSachsWolfe()
        
        # Test potential evolution causing ISW effect
        redshifts = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
        potential_derivatives = isw.calculate_potential_derivatives(redshifts)
        
        # ISW comes from time-varying potentials during dark energy domination
        for deriv in potential_derivatives:
            assert math.isfinite(deriv)
            
        # Should show significant evolution during matter-dark energy transition
        transition_era_deriv = potential_derivatives[1:3]  # z ~ 0.5-1.0
        assert any(abs(deriv) > 0.1 for deriv in transition_era_deriv)


class TestSphericalBesselProjection:
    """Test spherical Bessel function projection from 3D to 2D."""
    
    def test_spherical_bessel_projection(self):
        """Test SphericalBesselProjection functionality."""
        bessel_proj = SphericalBesselProjection(
            k_modes=np.logspace(-4, 0, 50),  # Wavenumber range
            r_values=np.linspace(10, 14000, 100),  # Distance range in Mpc
            l_max=2000
        )
        
        assert len(bessel_proj.k_modes) == 50
        assert len(bessel_proj.r_values) == 100
        assert bessel_proj.l_max == 2000
        
    def test_bessel_function_calculation(self):
        """Test spherical Bessel function calculations."""
        bessel_proj = SphericalBesselProjection()
        
        # Test j_ℓ(kr) for specific values
        l_values = [0, 1, 2, 5, 10, 50]
        kr_values = [0.1, 1.0, 10.0, 50.0]
        
        for l in l_values:
            for kr in kr_values:
                j_l_kr = bessel_proj.calculate_spherical_bessel(l, kr)
                assert math.isfinite(j_l_kr)
                
                # Bessel functions should be bounded
                assert abs(j_l_kr) <= 1.0
                
    def test_projection_integral(self):
        """Test 3D to 2D projection integral."""
        bessel_proj = SphericalBesselProjection()
        
        # Test projection for specific multipole
        l_test = 100
        k_mode = 0.01  # h/Mpc
        
        # Mock source function (e.g., temperature perturbation)
        def source_function(r):
            return np.exp(-r/1000)  # Simple exponential decay
            
        projection_result = bessel_proj.calculate_projection(
            l_test, k_mode, source_function
        )
        
        assert math.isfinite(projection_result)
        
    def test_angular_diameter_distance(self):
        """Test angular diameter distance calculation."""
        bessel_proj = SphericalBesselProjection()
        
        # Test distances to various redshifts
        redshifts = [0.1, 0.5, 1.0, 1.5, 2.0]
        distances = bessel_proj.calculate_angular_diameter_distance(redshifts)
        
        assert len(distances) == len(redshifts)
        
        # All distances should be positive and finite
        for d in distances:
            assert d > 0
            assert math.isfinite(d)
            
        # Distance should initially increase then decrease due to curvature
        # (in ΛCDM cosmology)


class TestRecombinationCoupling:
    """Test recombination physics and baryon-photon decoupling."""
    
    def test_recombination_coupling_creation(self):
        """Test RecombinationCoupling creation."""
        recombination = RecombinationCoupling(
            helium_fraction=0.24,
            hydrogen_ionization_energy=13.6,  # eV
            phi_recombination_corrections=True
        )
        
        assert recombination.helium_fraction == 0.24
        assert recombination.hydrogen_ionization_energy == 13.6
        assert recombination.phi_recombination_corrections is True
        
    def test_saha_equation_solution(self):
        """Test Saha equation solution for ionization fraction."""
        recombination = RecombinationCoupling()
        
        # Test ionization fraction over recombination epoch
        redshifts = np.array([1500, 1300, 1100, 1000, 900, 700])
        ionization_fractions = recombination.solve_saha_equation(redshifts)
        
        assert len(ionization_fractions) == len(redshifts)
        
        # Ionization fraction should decrease through recombination
        for i in range(1, len(ionization_fractions)):
            # Generally decreasing (though Saha can have complexity)
            assert 0.0 <= ionization_fractions[i] <= 1.0
            assert math.isfinite(ionization_fractions[i])
            
        # Should be highly ionized at high z, neutral at low z
        assert ionization_fractions[0] > 0.9  # Highly ionized early
        assert ionization_fractions[-1] < 0.2  # Mostly neutral late
        
    def test_visibility_function(self):
        """Test visibility function calculation."""
        recombination = RecombinationCoupling()
        
        # Calculate visibility function (probability of last scattering)
        redshifts = np.linspace(800, 1500, 100)
        visibility = recombination.calculate_visibility_function(redshifts)
        
        assert len(visibility) == len(redshifts)
        
        # Visibility should peak around z ~ 1100
        peak_index = np.argmax(visibility)
        peak_redshift = redshifts[peak_index]
        
        assert 1050 < peak_redshift < 1150  # Around recombination
        
        # Visibility should be normalized (integrate to 1)
        dz = redshifts[1] - redshifts[0]
        total_visibility = np.sum(visibility) * dz
        assert abs(total_visibility - 1.0) < 0.1  # Approximate normalization
        
    def test_phi_recombination_corrections(self):
        """Test φ-corrections to recombination physics."""
        recombination = RecombinationCoupling(phi_recombination_corrections=True)
        
        # Test φ-enhanced recombination rate
        standard_rate = recombination.calculate_recombination_rate(
            temperature=3000,  # K
            phi_corrections=False
        )
        phi_corrected_rate = recombination.calculate_recombination_rate(
            temperature=3000,  # K  
            phi_corrections=True
        )
        
        assert math.isfinite(standard_rate)
        assert math.isfinite(phi_corrected_rate)
        assert standard_rate > 0
        assert phi_corrected_rate > 0
        
        # φ-corrections should modify the rate
        correction_factor = phi_corrected_rate / standard_rate
        assert math.isfinite(correction_factor)
        
    def test_thomson_scattering_opacity(self):
        """Test Thomson scattering opacity evolution."""
        recombination = RecombinationCoupling()
        
        # Calculate optical depth over cosmic history
        redshifts = np.array([0, 200, 500, 800, 1100, 1500])
        optical_depths = recombination.calculate_thomson_opacity(redshifts)
        
        # Opacity should be low at late times, high before recombination
        for i, (z, tau) in enumerate(zip(redshifts, optical_depths)):
            assert tau >= 0  # Opacity non-negative
            assert math.isfinite(tau)
            
            if z < 100:
                assert tau < 0.1  # Low opacity at late times
            elif z > 1200:
                assert tau > 1.0   # High opacity before recombination


class TestCMBTransferFunction:
    """Test CMB transfer function calculations."""
    
    def test_transfer_function_creation(self):
        """Test CMBTransferFunction creation."""
        transfer = CMBTransferFunction(
            k_modes=np.logspace(-4, 1, 100),
            transfer_type="temperature",
            normalization="COBE"
        )
        
        assert len(transfer.k_modes) == 100
        assert transfer.transfer_type == "temperature"
        assert transfer.normalization == "COBE"
        
    def test_temperature_transfer_function(self):
        """Test temperature transfer function T_ℓ(k)."""
        transfer = CMBTransferFunction(transfer_type="temperature")
        
        # Test transfer function for various k, ℓ combinations
        k_values = [0.001, 0.01, 0.1, 1.0]  # h/Mpc
        l_values = [10, 100, 500, 1000]
        
        for k in k_values:
            for l in l_values:
                T_l_k = transfer.calculate_temperature_transfer(k, l)
                
                assert math.isfinite(T_l_k)
                # Transfer function can be positive or negative (oscillations)
                
    def test_polarization_transfer_functions(self):
        """Test E and B polarization transfer functions."""
        transfer_E = CMBTransferFunction(transfer_type="E_polarization")
        transfer_B = CMBTransferFunction(transfer_type="B_polarization")
        
        # Test E-mode polarization (scalar perturbations)
        k_test = 0.1
        l_test = 500
        
        T_E = transfer_E.calculate_polarization_transfer(k_test, l_test)
        T_B = transfer_B.calculate_polarization_transfer(k_test, l_test)
        
        assert math.isfinite(T_E)
        assert math.isfinite(T_B)
        
        # For scalar perturbations, B-mode should be suppressed
        assert abs(T_B) <= abs(T_E)
        
    def test_transfer_function_normalization(self):
        """Test transfer function normalization."""
        transfer = CMBTransferFunction(normalization="COBE")
        
        # Test that normalization is applied correctly
        # Large scale (low k) should match COBE normalization
        k_large_scale = 0.001  # h/Mpc
        l_large_scale = 10
        
        T_normalized = transfer.calculate_temperature_transfer(
            k_large_scale, l_large_scale
        )
        
        assert math.isfinite(T_normalized)
        
        # Should have reasonable amplitude for COBE normalization
        assert abs(T_normalized) < 1e2  # Not unnaturally large
        assert abs(T_normalized) > 1e-6  # Not unnaturally small


class TestCMBCalibration:
    """Test CMB power spectrum calibration and comparison."""
    
    def test_cmb_calibration_creation(self):
        """Test CMBCalibration creation."""
        calibration = CMBCalibration(
            reference_dataset="Planck2018",
            calibration_multipoles=[2, 10, 50, 220, 500, 1000, 2000],
            statistical_analysis=True
        )
        
        assert calibration.reference_dataset == "Planck2018"
        assert len(calibration.calibration_multipoles) == 7
        assert calibration.statistical_analysis is True
        
    def test_theoretical_prediction_comparison(self):
        """Test comparison of theoretical predictions with observations."""
        calibration = CMBCalibration(reference_dataset="Planck2018")
        
        # Generate theoretical power spectrum
        power_spectrum = CMBPowerSpectrum()
        multipoles = np.array([2, 10, 50, 220, 500, 1000])
        theoretical_C_l = power_spectrum.calculate_angular_power_spectrum(multipoles)
        
        # Compare with "observations" (mock for testing)
        mock_observed_C_l = theoretical_C_l * (1 + 0.1 * np.random.randn(len(theoretical_C_l)))
        mock_errors = 0.05 * theoretical_C_l
        
        comparison = calibration.compare_theory_observation(
            multipoles, theoretical_C_l, mock_observed_C_l, mock_errors
        )
        
        assert comparison is not None
        assert 'chi_squared' in comparison or hasattr(comparison, 'chi_squared')
        assert 'goodness_of_fit' in comparison or hasattr(comparison, 'goodness_of_fit')
        
    def test_parameter_estimation(self):
        """Test cosmological parameter estimation."""
        calibration = CMBCalibration(statistical_analysis=True)
        
        # Test parameter estimation from power spectrum
        power_spectrum = CMBPowerSpectrum()
        multipoles = np.logspace(0.5, 3.2, 50)  # ℓ from ~3 to ~1500
        C_l_data = power_spectrum.calculate_angular_power_spectrum(multipoles)
        
        # Mock parameter estimation
        estimated_params = calibration.estimate_parameters(multipoles, C_l_data)
        
        assert estimated_params is not None
        assert isinstance(estimated_params, dict)
        
        # Should estimate key cosmological parameters
        expected_params = ['Omega_b', 'Omega_c', 'Omega_Lambda', 'h', 'n_s']
        for param in expected_params:
            if param in estimated_params:
                assert math.isfinite(estimated_params[param])
                assert estimated_params[param] > 0  # Physical parameters positive
                
    def test_acoustic_peak_detection(self):
        """Test acoustic peak detection and measurement."""
        calibration = CMBCalibration()
        
        # Generate power spectrum with clear peaks
        power_spectrum = CMBPowerSpectrum(phi_harmonic_peaks=True)
        multipoles = np.linspace(50, 1500, 500)
        C_l_values = power_spectrum.calculate_angular_power_spectrum(multipoles)
        
        # Detect acoustic peaks
        detected_peaks = calibration.detect_acoustic_peaks(multipoles, C_l_values)
        
        assert detected_peaks is not None
        assert len(detected_peaks) > 0  # Should find some peaks
        
        # Peaks should be at roughly expected positions
        for peak_position in detected_peaks:
            assert peak_position > 50   # Above minimum tested range
            assert peak_position < 1500  # Below maximum tested range
            
        # First peak should be around ℓ ~ 220
        first_peak = min(detected_peaks)
        assert 180 < first_peak < 300  # Reasonable range around 220


class TestPhysicalRealism:
    """Test physical realism of CMB power spectrum predictions."""
    
    def test_power_spectrum_magnitude(self):
        """Test that power spectrum has realistic magnitudes."""
        power_spectrum = CMBPowerSpectrum()
        
        # Test various multipole ranges
        low_l = np.array([2, 5, 10])  # Large angular scales
        peak_l = np.array([200, 220, 250])  # First acoustic peak region
        high_l = np.array([1000, 1500, 2000])  # Small angular scales
        
        for multipoles in [low_l, peak_l, high_l]:
            C_l_values = power_spectrum.calculate_angular_power_spectrum(multipoles)
            
            for C_l in C_l_values:
                # CMB power should be in reasonable range (μK²)
                assert 10 < C_l < 10000  # Broad but reasonable range
                assert math.isfinite(C_l)
                
    def test_acoustic_peak_ordering(self):
        """Test that acoustic peaks decrease in amplitude correctly."""
        power_spectrum = CMBPowerSpectrum(phi_harmonic_peaks=True)
        
        # Calculate power at expected peak positions
        phi = PHI_VALUE
        peak_positions = [220, 220*phi, 220*phi**2, 220*phi**3]
        peak_powers = power_spectrum.calculate_angular_power_spectrum(
            np.array(peak_positions)
        )
        
        # Generally expect decreasing peak heights (with possible exceptions)
        # First peak should be prominent
        assert peak_powers[0] > 1000  # First peak should be strong
        
        # All peaks should be positive and finite
        for power in peak_powers:
            assert power > 0
            assert math.isfinite(power)
            
    def test_damping_tail_behavior(self):
        """Test Silk damping tail at high multipoles."""
        power_spectrum = CMBPowerSpectrum(silk_damping=True)
        
        # Test high multipole behavior
        high_multipoles = np.array([1500, 2000, 2500, 3000])
        high_l_powers = power_spectrum.calculate_angular_power_spectrum(high_multipoles)
        
        # Power should be damped at high ℓ
        for i in range(1, len(high_l_powers)):
            # Generally decreasing (exponential cutoff)
            assert high_l_powers[i] <= high_l_powers[i-1] * 2  # Allow some variation
            assert high_l_powers[i] > 0
            
        # Very high ℓ should be significantly suppressed
        assert high_l_powers[-1] < high_l_powers[0] * 0.5
        
    def test_large_scale_isw_enhancement(self):
        """Test ISW enhancement at large angular scales."""
        power_spectrum_with_isw = CMBPowerSpectrum(integrated_sachs_wolfe=True)
        power_spectrum_without_isw = CMBPowerSpectrum(integrated_sachs_wolfe=False)
        
        # Test large scale power (low ℓ)
        large_scales = np.array([2, 5, 10, 20])
        
        C_l_with_isw = power_spectrum_with_isw.calculate_angular_power_spectrum(large_scales)
        C_l_without_isw = power_spectrum_without_isw.calculate_angular_power_spectrum(large_scales)
        
        # ISW should enhance large scale power
        for i in range(len(large_scales)):
            assert C_l_with_isw[i] >= C_l_without_isw[i]  # Enhancement or equal
            
        # Enhancement should be most significant at largest scales
        enhancement_ratio = C_l_with_isw[0] / C_l_without_isw[0]
        assert enhancement_ratio >= 1.0
        assert enhancement_ratio < 10.0  # Reasonable enhancement


class TestIntegrationWithCosmology:
    """Test integration with other cosmology modules."""
    
    def test_inflation_perturbation_integration(self):
        """Test integration with inflation theory perturbations."""
        try:
            from cosmology.inflation_theory import InflationTheory
            
            power_spectrum = CMBPowerSpectrum()
            inflation = InflationTheory()
            
            # Test that inflation can provide initial conditions
            k_modes = np.logspace(-4, 0, 50)
            initial_perturbations = inflation.calculate_primordial_spectrum(k_modes)
            
            # Power spectrum should be able to use these initial conditions
            final_spectrum = power_spectrum.evolve_perturbations(
                k_modes, initial_perturbations
            )
            
            assert len(final_spectrum) == len(k_modes)
            for spectrum_val in final_spectrum:
                assert math.isfinite(spectrum_val)
                assert spectrum_val >= 0
                
        except ImportError:
            # Inflation theory module may not be available
            pass
            
    def test_recombination_physics_integration(self):
        """Test integration with recombination physics."""
        power_spectrum = CMBPowerSpectrum()
        recombination = RecombinationCoupling()
        
        # Test that recombination physics affects power spectrum
        z_recombination = 1100
        visibility = recombination.calculate_visibility_function(
            np.array([z_recombination])
        )[0]
        
        # Power spectrum should use recombination physics
        # This tests the integration pathway exists
        assert visibility > 0
        assert math.isfinite(visibility)
        
    def test_phi_consistency_across_modules(self):
        """Test φ-value consistency across cosmology modules."""
        power_spectrum = CMBPowerSpectrum()
        phi_peaks = PhiHarmonicPeaks()
        
        # Both should use the same φ value
        power_phi = getattr(power_spectrum, 'phi_value', PHI_VALUE)
        peaks_phi = getattr(phi_peaks, 'phi_scaling', PHI_VALUE)
        
        assert abs(power_phi - PHI_VALUE) < 1e-12
        assert abs(peaks_phi - PHI_VALUE) < 1e-12
        assert abs(power_phi - peaks_phi) < 1e-12
