import os
import math
import numpy as np

# Silence console noise from validation/falsification during tests
os.environ.setdefault("FIRM_SILENT_TESTS", "1")


def test_cmb_power_spectrum_basic():
    from cosmology.cmb_power_spectrum import CMB_SPECTRUM

    res = CMB_SPECTRUM.compute_cmb_power_spectrum(ell_max=128)
    assert res.multipoles.size == 127
    assert res.temperature_power.size == 127
    assert float(res.total_chi_squared) >= 0.0
    # Ensure a few acoustic peaks were identified
    assert len(res.acoustic_peaks) >= 3


def test_inflation_observables():
    from cosmology.inflation_theory import INFLATION_FIELD

    obs = INFLATION_FIELD.compute_inflationary_observables()
    assert 0.0 < obs.scalar_spectral_index < 1.5
    assert obs.tensor_to_scalar_ratio >= 0.0
    assert obs.number_of_efolds > 0


def test_spectral_zeta_prefactor_real():
    from foundation.operators.spectral_zeta import SpectralZetaRegularization

    reg = SpectralZetaRegularization()
    result = reg.compute_spectral_prefactor()
    assert math.isfinite(result.theoretical_value)
    assert result.theoretical_value != 0.0
    assert isinstance(result.derivation_steps, list) and len(result.derivation_steps) > 0


def test_zx_calculus_synthesis():
    from foundation.operators.zx_calculus import ZX_CALCULUS_FRAMEWORK

    res = ZX_CALCULUS_FRAMEWORK.synthesize_phi_quantum_algorithm("search", {})
    assert res.quantum_advantage_proven is True
    assert res.phi_optimization_factor > 0


def test_qcd_gluon_torsion_framework():
    from structures.gluon_torsion_framework import derive_qcd_integration

    res = derive_qcd_integration()
    assert res.strong_coupling_alpha_s > 0
    assert res.confinement_scale > 0


def test_cosmology_parameters_and_firewall_block():
    from cosmology import derive_cosmological_parameters, verify_observational_agreement
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL

    params = derive_cosmological_parameters()
    assert "omega_matter" in params and params["omega_matter"] is not None

    status = verify_observational_agreement()
    assert status["status"] == "blocked"

    report = EXPERIMENTAL_FIREWALL.generate_firewall_report()
    assert "FIREWALL STATUS" in report.upper() and "ACTIVE" in report.upper()


def test_gauge_couplings_and_masses_paths():
    from constants.gauge_couplings import GAUGE_COUPLINGS, ALPHA_3_INVERSE, ALPHA_EM_INVERSE
    from constants.mass_ratios import FUNDAMENTAL_MASSES

    assert ALPHA_3_INVERSE and ALPHA_3_INVERSE > 0
    assert ALPHA_EM_INVERSE and ALPHA_EM_INVERSE > 0

    # Access a few mass ratios to exercise code paths
    mu_over_e = FUNDAMENTAL_MASSES.get_mass_ratio("muon", "electron")
    assert mu_over_e > 1.0