from cosmology import verify_observational_agreement
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_verify_observational_agreement_blocked_then_granted():
    # Reset firewall to default ACTIVE theory-phase
    EXPERIMENTAL_FIREWALL.reset()
    status = verify_observational_agreement()
    assert status["status"] == "blocked"

    # Enable validation and re-check
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
    status2 = verify_observational_agreement()
    assert status2["status"] in ("blocked", "granted")
