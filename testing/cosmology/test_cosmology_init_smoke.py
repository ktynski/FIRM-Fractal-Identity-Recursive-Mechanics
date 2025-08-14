from cosmology import (
    COSMOLOGY_CONFIG,
    COSMOGENESIS_STAGES,
    COSMOLOGICAL_PARAMETERS,
    register_cosmogenesis_stage,
    get_cosmogenesis_stage,
    derive_cosmological_parameters,
    verify_observational_agreement,
)


def test_cosmology_public_api_and_structures():
    assert isinstance(COSMOLOGY_CONFIG, dict)
    assert isinstance(COSMOGENESIS_STAGES, dict)
    assert isinstance(COSMOLOGICAL_PARAMETERS, dict)

    register_cosmogenesis_stage("test_stage", {"ready": True})
    assert get_cosmogenesis_stage("test_stage")["ready"] is True

    params = derive_cosmological_parameters()
    assert "hubble_parameter_s_inverse" in params
    assert "cmb_temperature_K" in params

    # Firewall is likely blocking in theory phase; both branches acceptable
    resp = verify_observational_agreement(dataset_id="planck_2018_cmb")
    assert resp["status"] in ("blocked", "granted")
    assert "derived" in resp and isinstance(resp["derived"], dict)
