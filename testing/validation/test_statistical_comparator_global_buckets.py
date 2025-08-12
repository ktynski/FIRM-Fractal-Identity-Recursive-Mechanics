from validation.statistical_comparator import StatisticalComparator


def test_assess_global_evidence_buckets_direct():
    sc = StatisticalComparator()
    # Direct bucket checks
    assert sc._assess_global_evidence(10**6) in ("overwhelming", "decisive")
    assert sc._assess_global_evidence(10**3) in ("decisive", "very_strong")
    assert sc._assess_global_evidence(10**1) in ("very_strong", "strong")
    assert sc._assess_global_evidence(10**0.6) in ("strong", "substantial")
    assert sc._assess_global_evidence(10**0.1) in ("substantial",)
    assert sc._assess_global_evidence(10**-1) in ("insufficient",)

