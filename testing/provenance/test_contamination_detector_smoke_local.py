from provenance.contamination_detector import CONTAMINATION_DETECTOR


def test_contamination_detector_basic_helpers():
    ev_lex = CONTAMINATION_DETECTOR.detect_lexical_contamination("measured constant appears")
    ev_num = CONTAMINATION_DETECTOR.detect_numerical_contamination("value 137.0 shows up")
    ev_ctx = CONTAMINATION_DETECTOR.detect_contextual_contamination("CODATA 2018 reference")
    rep = CONTAMINATION_DETECTOR.generate_contamination_report(ev_lex + ev_num + ev_ctx)
    assert isinstance(rep, str) and "FIRM Contamination Detection Report" in rep

