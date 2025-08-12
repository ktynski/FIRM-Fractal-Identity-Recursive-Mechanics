from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_cmb_structure_public_api_smoke():
    aps = AcousticPeakStructure()
    # compute with small ell_max for speed if supported; else default path
    try:
        res = aps.compute_cmb_power_spectrum(ell_max=128)
    except TypeError:
        res = aps.compute_cmb_power_spectrum()
    assert hasattr(res, "multipoles") and hasattr(res, "temperature_power")
    assert hasattr(res, "acoustic_peaks") and isinstance(res.acoustic_peaks, list)
    assert hasattr(res, "cosmological_parameters") and isinstance(res.cosmological_parameters, dict)

