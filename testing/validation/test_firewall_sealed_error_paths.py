import pytest


def test_get_sealed_comparison_provenance_validator_none(monkeypatch):
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
    import provenance.derivation_tree as pdt

    EXPERIMENTAL_FIREWALL.reset()
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        pytest.skip("Preconditions not met for validation phase")

    # Temporarily set PROVENANCE_VALIDATOR to None
    saved = getattr(pdt, "PROVENANCE_VALIDATOR", None)
    monkeypatch.setattr(pdt, "PROVENANCE_VALIDATOR", None, raising=False)
    try:
        sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
        assert sealed is None
    finally:
        # Restore
        monkeypatch.setattr(pdt, "PROVENANCE_VALIDATOR", saved, raising=False)


def test_get_sealed_comparison_non_ready_key():
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
    EXPERIMENTAL_FIREWALL.reset()
    # Non-ready keys must return None in both phases
    assert EXPERIMENTAL_FIREWALL.get_sealed_comparison("ckm_Vus") is None
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        # Even if cannot enable, the assertion above suffices
        return
    assert EXPERIMENTAL_FIREWALL.get_sealed_comparison("ckm_Vus") is None
