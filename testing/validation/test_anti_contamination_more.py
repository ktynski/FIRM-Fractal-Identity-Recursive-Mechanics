from validation.anti_contamination import ANTI_CONTAMINATION


def test_is_empirical_value_container_and_string_paths():
    # String with empirical keyword
    assert ANTI_CONTAMINATION.is_empirical_value("measured value") is True
    # String containing forbidden literal
    assert ANTI_CONTAMINATION.is_empirical_value("alpha inverse 137.035999084") is True
    # Container recursive check
    assert ANTI_CONTAMINATION.is_empirical_value([0.1, "codata ref"]) is True
    # Dict key with empirical keyword triggers
    assert ANTI_CONTAMINATION.is_empirical_value({"measured": 0.1}) is True
    # Benign container
    assert ANTI_CONTAMINATION.is_empirical_value([0.1, 0.2]) is False

