import numpy as np
from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_sachs_wolfe_plateau_supressed_towards_acoustic_scale():
    cmb = AcousticPeakStructure()
    # trigger scale init
    _ = cmb.compute_cmb_power_spectrum(ell_max=128)
    ell = np.arange(2, 200)
    sw = cmb._compute_sachs_wolfe_plateau(ell)
    # Suppression increases with ell; monotone in the tested coarse sense
    assert sw[0] > np.median(sw) > sw[-1]

