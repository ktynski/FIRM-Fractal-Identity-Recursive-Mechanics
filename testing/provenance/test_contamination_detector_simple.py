from provenance.contamination_detector import CONTAMINATION_DETECTOR


def test_contamination_detector_numeric_literal_scan():
    text = "This derivation uses 137.0 directly which should be flagged."
    ev = CONTAMINATION_DETECTOR.detect_numerical_contamination(text)
    assert any("Forbidden hardcoded numeric" in e.description or "matches experimental" in e.description for e in ev)
