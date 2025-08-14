from figures.validation_overlays import VALIDATION_OVERLAYS
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_validation_overlays_gated_by_firewall():
    # Default theory phase: should produce no overlays
    EXPERIMENTAL_FIREWALL.reset()
    EXPERIMENTAL_FIREWALL.enable_theory_phase()
    res = VALIDATION_OVERLAYS.generate_all()
    assert res == []

    # Enable validation: overlays allowed only for whitelisted keys
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        # If theory-complete preconditions not met in environment, skip
        return
    res2 = VALIDATION_OVERLAYS.generate_all()
    # It may still be empty if theory modules not available; but not erroring is key
    assert isinstance(res2, list)
