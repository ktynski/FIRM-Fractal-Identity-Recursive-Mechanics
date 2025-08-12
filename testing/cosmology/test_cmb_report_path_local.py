from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_cmb_generate_report_contains_expected_sections():
    cmb = AcousticPeakStructure()
    rep = cmb.generate_cmb_report()
    assert "FIRM CMB Power Spectrum Report" in rep
    assert "ACOUSTIC PEAK STRUCTURE" in rep
    assert "COSMOLOGICAL PARAMETERS" in rep

