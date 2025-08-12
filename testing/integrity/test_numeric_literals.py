import textwrap

from provenance.contamination_detector import ContaminationDetector, ContaminationLevel


def test_numeric_literal_scanner_flags_empirical_like_numbers():
    src = textwrap.dedent(
        """
        def derive_alpha_empirical():
            # suspicious embedding of CODATA-like value
            return 137.035999084
        """
    )
    det = ContaminationDetector()
    evidences = det.analyze_source_for_numeric_literals(src, location="unit_test.alpha")
    assert any(
        ev.contamination_level in (ContaminationLevel.SUSPICIOUS, ContaminationLevel.CONFIRMED)
        for ev in evidences
    ), "Scanner should flag CODATA-like numeric literal"


def test_numeric_literal_scanner_allows_trivial_literals():
    src = textwrap.dedent(
        """
        def f(x):
            if x > 0:
                return 1
            elif x == 0:
                return 0
            else:
                return -1
        """
    )
    det = ContaminationDetector()
    evidences = det.analyze_source_for_numeric_literals(src, location="unit_test.trivial")
    # Whitelisted trivial literals should not produce critical findings
    assert all(ev.contamination_level != ContaminationLevel.CONFIRMED for ev in evidences)