from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_theory_vs_validation_access_paths():
    # Clean state ensured by autouse fixture; should be in theory phase
    assert EXPERIMENTAL_FIREWALL._theory_phase_active is True
    assert EXPERIMENTAL_FIREWALL._validation_phase_active is False
    assert EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv") is None

    # Enable validation and ensure sealed comparison returns metadata
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
    sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    assert isinstance(sealed, dict) and sealed.get("sealed") is True

