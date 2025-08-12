from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_spectral_helpers_cutoff_and_weighting():
    sz = SpectralZetaRegularization()
    # exercise cutoff dependence proxy
    cdep = sz._analyze_cutoff_dependence()
    assert isinstance(cdep, float) and cdep >= 0.0
    # exercise phi weighting stability proxy
    pws = sz._analyze_phi_weighting_stability()
    assert isinstance(pws, float) and pws >= 0.0

