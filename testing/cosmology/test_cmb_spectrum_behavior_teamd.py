import numpy as np


def test_cmb_spectrum_damping_and_nonnegative():
    from cosmology.cmb_power_spectrum import AcousticPeakStructure

    cmb = AcousticPeakStructure()
    res = cmb.compute_cmb_power_spectrum(ell_max=256)

    Dl = res.temperature_power
    assert np.all(np.isfinite(Dl))
    assert np.all(Dl >= 0.0)

    # Damping: verify damping factors decrease with ℓ
    import numpy as _np
    ells = _np.arange(2, 256 + 1, dtype=float)
    damping = cmb._compute_damping_tail(ells)
    assert damping[0] >= damping[-1]
    # And tail damping is significantly smaller than low-ℓ damping
    m = damping.size
    low_damp_mean = float(damping[: max(1, m // 10)].mean())
    high_damp_mean = float(damping[-max(1, m // 10) :].mean())
    assert high_damp_mean < low_damp_mean
