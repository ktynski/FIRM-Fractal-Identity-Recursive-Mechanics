import math

from constants.mass_ratios import FUNDAMENTAL_MASSES


def test_basic_mass_access_and_ratios():
    # Access a few masses
    m_e = FUNDAMENTAL_MASSES.get_mass_mev("electron")
    m_mu = FUNDAMENTAL_MASSES.get_mass_mev("muon")
    m_p = FUNDAMENTAL_MASSES.get_mass_mev("proton")

    assert m_e > 0.0
    assert m_mu > m_e
    assert m_p > m_e

    # Ratios
    mu_over_e = FUNDAMENTAL_MASSES.get_mass_ratio("muon", "electron")
    p_over_e = FUNDAMENTAL_MASSES.get_mass_ratio("proton", "electron")
    n_over_p = FUNDAMENTAL_MASSES.get_mass_ratio("neutron", "proton")

    assert mu_over_e > 1.0
    assert p_over_e > 1.0
    assert 1.0 <= n_over_p <= 1.1


def test_mass_spectrum_report_generation():
    report = FUNDAMENTAL_MASSES.generate_mass_spectrum_report()
    assert isinstance(report, str) and "FIRM Fundamental Mass Spectrum Report" in report
