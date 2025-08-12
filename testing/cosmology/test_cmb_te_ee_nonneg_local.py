import numpy as np
from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_te_ee_nonnegative_shapes_and_same_length():
    cmb = AcousticPeakStructure()
    res = cmb.compute_cmb_power_spectrum(ell_max=256)
    assert res.polarization_e_power.shape == res.temperature_power.shape
    assert res.temperature_polarization.shape == res.temperature_power.shape
    assert np.all(np.isfinite(res.polarization_e_power))
    assert np.all(np.isfinite(res.temperature_polarization))
    # Non-negativity in envelope sense (allow small negative due to oscillatory TE)
    assert res.polarization_e_power.min() >= 0.0
