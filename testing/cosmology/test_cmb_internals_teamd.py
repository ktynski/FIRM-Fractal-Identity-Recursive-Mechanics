import math


def test_cmb_internal_scales_phi_native():
    from cosmology.cmb_power_spectrum import AcousticPeakStructure

    cmb = AcousticPeakStructure()

    # Ensure φ-native cosmological parameters were consumed
    params = cmb._cosmo_params
    assert params.get("omega_matter") is not None
    assert params.get("hubble_parameter_s_inverse") is not None

    # Sound speed between 0 and 1/sqrt(3)
    cs = cmb._compute_sound_speed(cmb._z_recombination)
    assert 0.0 < cs <= 1.0 / math.sqrt(3.0)

    # Angular acoustic scale finite and positive
    theta_A = cmb._compute_angular_acoustic_scale()
    assert math.isfinite(theta_A) and theta_A > 0

    # Silk damping scale positive
    lsilk = cmb._compute_silk_damping_scale()
    assert math.isfinite(lsilk) and lsilk > 0

