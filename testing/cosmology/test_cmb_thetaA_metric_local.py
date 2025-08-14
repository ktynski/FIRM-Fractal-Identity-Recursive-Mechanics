import numpy as np
from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_thetaA_and_structure_metric_branches():
    cmb = AcousticPeakStructure()
    res = cmb.compute_cmb_power_spectrum(ell_max=128)
    # theta_A used internally; ensure first-peak positive
    assert res.acoustic_peaks[0].multipole_position > 0
    # structure metric computed and finite
    assert np.isfinite(res.total_chi_squared)
