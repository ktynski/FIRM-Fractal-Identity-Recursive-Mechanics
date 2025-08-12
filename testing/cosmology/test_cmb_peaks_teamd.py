import math


def test_phi_harmonic_peaks_monotonic_and_types():
    from cosmology.cmb_power_spectrum import AcousticPeakStructure, AcousticPeakType

    cmb = AcousticPeakStructure()
    peaks = cmb._derive_phi_harmonic_peaks()

    # Expect at least 5-6 peaks, strictly increasing ℓ positions
    assert len(peaks) >= 5
    for i in range(1, len(peaks)):
        assert peaks[i].multipole_position > peaks[i-1].multipole_position

    # Types alternate COMPRESSION/RAREFACTION
    for i, p in enumerate(peaks):
        expected = AcousticPeakType.COMPRESSION if (i % 2 == 0) else AcousticPeakType.RAREFACTION
        assert p.peak_type == expected

    # Amplitudes positive and widths positive
    for p in peaks:
        assert p.peak_amplitude > 0.0
        assert p.peak_width > 0.0

