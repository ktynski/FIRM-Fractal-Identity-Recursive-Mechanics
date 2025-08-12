import os
from validation.falsification_tester import FALSIFICATION_TESTER, FalsificationCriterion, AlertLevel


def test_alert_level_mapping_and_status_mapping():
    # Use internal methods deterministically
    tester = FALSIFICATION_TESTER
    # Map thresholds: explicitly test mapping function defaults
    assert tester._determine_falsification_status(AlertLevel.INFO).value == "safe"
    assert tester._determine_falsification_status(AlertLevel.WARNING).value == "warning"
    assert tester._determine_falsification_status(AlertLevel.URGENT).value == "critical"
    assert tester._determine_falsification_status(AlertLevel.EMERGENCY).value == "falsified"


def test_generate_alert_structure():
    tester = FALSIFICATION_TESTER
    spec = next(iter(tester._criteria_specifications.values()))
    alert = tester._generate_alert(spec.criterion, spec, observed_value=spec.threshold_value * 2, alert_level=AlertLevel.EMERGENCY)
    d = alert.to_dict()
    assert d["criterion"] == spec.criterion.value and d["alert_level"] == AlertLevel.EMERGENCY.value
