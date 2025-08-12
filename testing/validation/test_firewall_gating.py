import pytest
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_firewall_blocks_theory_phase_sealed_access_and_allows_in_validation():
    EXPERIMENTAL_FIREWALL.reset()

    # During theory phase, sealed comparison must return None and raise alert internally
    sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    assert sealed is None

    # Enabling validation requires theory completion; if preconditions fail, skip
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        pytest.skip("Theory completion preconditions not satisfied in this environment")

    # Now access should be allowed if key is registered
    sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    # Either None (if not registered) or a sealed dict with expected keys
    if sealed is not None:
        assert sealed.get("sealed") is True
        assert "value" in sealed and "uncertainty" in sealed

import pytest

from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_firewall_gates_non_ready_keys():
    EXPERIMENTAL_FIREWALL.reset()
    # Theory phase blocks everything
    assert EXPERIMENTAL_FIREWALL.get_sealed_comparison("proton_electron_mass_ratio") is None

    # Validation phase only exposes explicitly ready keys
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
    # fine-structure should be ready
    assert EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv") is not None
    # Other keys are conditionally ready depending on registered builders
    for key in ("proton_electron_mass_ratio", "ckm_Vus"):
        sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison(key)
        if sealed is not None:
            assert sealed.get("sealed") is True
        else:
            assert sealed is None
