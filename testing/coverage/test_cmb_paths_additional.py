import numpy as np

from cosmology.cmb_power_spectrum import CMB_SPECTRUM
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_cmb_polarization_and_isw_paths():
    # Ensure validation phase so chi2 path returns smoothness metric, not blocked
    EXPERIMENTAL_FIREWALL.reset()
    EXPERIMENTAL_FIREWALL.enable_validation_phase()

    # Compute spectrum which exercises EE/TE and ISW contributions
    res = CMB_SPECTRUM.compute_cmb_power_spectrum(ell_max=512)
    assert res.temperature_power.size > 0
    assert res.polarization_e_power.size > 0 and res.temperature_polarization.size > 0
    assert res.total_chi_squared >= 0.0

    # Report path
    report = CMB_SPECTRUM.generate_cmb_report()
    assert "FIRM CMB Power Spectrum Report" in report
