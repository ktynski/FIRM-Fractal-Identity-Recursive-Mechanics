import numpy as np
from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_structure_metric_exists_and_runs():
    cmb = AcousticPeakStructure()
    ells = np.arange(2, 50)
    theory = np.ones_like(ells, dtype=float)
    # Access via public compute to ensure call path uses the renamed method
    result = cmb.compute_cmb_power_spectrum(ell_max=50)
    assert hasattr(cmb, "_compute_structure_metric")
    # Direct call for sanity
    val = cmb._compute_structure_metric(ells, theory)
    assert isinstance(val, float)
    assert val >= 0.0
