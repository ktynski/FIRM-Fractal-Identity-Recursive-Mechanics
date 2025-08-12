from cosmology import derive_cosmological_parameters


def test_cosmology_phi_native_parameters_and_bridge():
    params = derive_cosmological_parameters()

    # φ-native scalars present
    assert "hubble_constant_phi_native" in params
    assert "cmb_temperature_phi_native" in params

    # Bridge-assigned physical outputs present (no empirical ingestion)
    assert "hubble_parameter_s_inverse" in params
    assert params["hubble_parameter_s_inverse"] is not None

    assert "cmb_temperature_K" in params
    assert params["cmb_temperature_K"] is not None

    # Basic internal consistency: 0 < Ω_m < 1 and Ω_Λ = 1 - Ω_m
    om = params.get("omega_matter")
    ol = params.get("omega_lambda")
    assert 0.0 < float(om) < 1.0
    assert abs(float(ol) - (1.0 - float(om))) < 1e-12

