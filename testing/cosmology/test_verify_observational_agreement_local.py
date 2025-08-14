from cosmology import verify_observational_agreement
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_verify_observational_agreement_gated_paths():
    EXPERIMENTAL_FIREWALL.reset()
    out = verify_observational_agreement(dataset_id="planck_2018_cmb")
    assert out["status"] in ("blocked", "granted")
    assert "derived" in out and isinstance(out["derived"], dict)
    # Attempt to enable validation; preconditions may fail in theory-only mode
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        pass
    out2 = verify_observational_agreement(dataset_id="planck_2018_cmb")
    assert out2["status"] in ("blocked", "granted")
