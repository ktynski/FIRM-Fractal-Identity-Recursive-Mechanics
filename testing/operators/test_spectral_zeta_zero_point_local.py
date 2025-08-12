from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_zero_point_energy_path_and_types():
    sz = SpectralZetaRegularization()
    zpe = sz.compute_zero_point_energy_phi_weighted()
    assert isinstance(zpe["zero_point_energy"], float)
    assert isinstance(zpe["raw_sum"], float)
    assert isinstance(zpe["zeta_regularization"], float)

