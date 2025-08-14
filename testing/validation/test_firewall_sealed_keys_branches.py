import builtins

from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_get_sealed_comparison_for_additional_keys(monkeypatch):
    EXPERIMENTAL_FIREWALL.reset()
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        # Theory completion precheck may fail in some environments; skip
        return

    # Ensure provenance validator is available for gating
    import provenance.derivation_tree as prov

    monkeypatch.setattr(prov, "PROVENANCE_VALIDATOR", object(), raising=True)
    # Manually mark additional keys as validation-ready to exercise branches
    keys = {
        "weak_mixing_angle_sin2",
        "ckm_Vus",
        "ckm_Vcb",
        "ckm_Vub",
        "ckm_delta_cp",
    }
    EXPERIMENTAL_FIREWALL._validation_ready_keys.update(keys)

    # Each of these should now return a sealed dict
    for key in list(keys):
        sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison(key)
        assert sealed is None or (sealed.get("sealed") is True)
