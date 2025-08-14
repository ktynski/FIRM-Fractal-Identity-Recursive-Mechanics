from validation.falsification_tester import FalsificationTester, AlertLevel, FalsificationStatus


def test_status_mapping_from_alert_levels():
    t = FalsificationTester()
    m = {
        AlertLevel.INFO: FalsificationStatus.SAFE,
        AlertLevel.WARNING: FalsificationStatus.WARNING,
        AlertLevel.URGENT: FalsificationStatus.CRITICAL,
        AlertLevel.EMERGENCY: FalsificationStatus.FALSIFIED,
    }
    for al, expected in m.items():
        assert t._determine_falsification_status(al) == expected
