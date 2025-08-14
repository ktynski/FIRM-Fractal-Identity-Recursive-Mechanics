from constants import validate_all_constants, generate_constants_report


def test_constants_derive_and_report_shapes():
    validation = validate_all_constants()
    assert isinstance(validation, dict)
    # Check that validation results have expected structure
    assert len(validation) > 0
    for name, result in validation.items():
        assert "status" in result

    report = generate_constants_report()
    assert isinstance(report, str)  # Report is a string, not dict
    assert "FIRM" in report and "constants" in report
