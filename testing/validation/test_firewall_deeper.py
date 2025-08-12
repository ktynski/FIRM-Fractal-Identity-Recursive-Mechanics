import pytest

from validation.experimental_firewall import EXPERIMENTAL_FIREWALL, FirewallStatus


def test_firewall_report_and_alerts_flow():
    EXPERIMENTAL_FIREWALL.reset()
    # Theory phase: access should be blocked and alert logged
    data = EXPERIMENTAL_FIREWALL.request_experimental_data("codata_2018_constants", requester="unit-test")
    assert data is None
    report = EXPERIMENTAL_FIREWALL.generate_firewall_report()
    assert "Firewall Status" in report

    # Enable validation and check sealed comparison returns
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
    meta = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    assert meta and meta.get("sealed") is True


def test_emergency_shutdown_changes_status():
    EXPERIMENTAL_FIREWALL.reset()
    EXPERIMENTAL_FIREWALL.emergency_shutdown("test")
    # Subsequent validation enable should remain disabled
    assert EXPERIMENTAL_FIREWALL._firewall_status == FirewallStatus.DISABLED
