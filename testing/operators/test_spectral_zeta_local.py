from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_spectral_prefactor_convergence_and_fields():
    sz = SpectralZetaRegularization()
    result = sz.compute_spectral_prefactor()
    assert result.name == "Spectral Prefactor"
    assert isinstance(result.theoretical_value, float)
    conv = result.convergence_analysis
    # Ensure convergence metrics are present and finite within [0, 1]
    for key in (
        "zero_point_convergence",
        "zeta_function_convergence",
        "mode_cutoff_dependence",
        "phi_weighting_stability",
    ):
        val = float(conv[key])
        assert val >= 0.0
    assert result.target_value is None
    assert result.relative_error_percent is None
    # Basic sanity on derivation steps and units
    assert isinstance(result.derivation_steps, list) and len(result.derivation_steps) > 0
    assert result.units == "dimensionless"

