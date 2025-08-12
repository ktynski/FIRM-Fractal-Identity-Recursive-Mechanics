from constants import derive_all_constants, generate_constants_report


def test_constants_derive_and_report_shapes():
    deriv = derive_all_constants()
    assert isinstance(deriv, dict)
    assert "fine_structure_primary" in deriv and "mass_spectrum" in deriv

    report = generate_constants_report()
    assert isinstance(report, dict)
    assert "derivation_results" in report and "experimental_validation" in report

