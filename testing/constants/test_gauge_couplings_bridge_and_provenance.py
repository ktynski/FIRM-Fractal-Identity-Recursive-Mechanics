from constants.gauge_couplings import GaugeCouplingDerivation


def test_coupling_provenance_trees_build():
    gcd = GaugeCouplingDerivation()
    for key in ("U1_hypercharge", "SU2_weak", "SU3_strong", "EM_coupling"):
        tree = gcd.build_coupling_provenance(key)
        assert tree is not None
        assert "α" in tree.target_result or "alpha" in tree.target_result


def test_running_couplings_dimensionless_and_monotonic_sanity():
    gcd = GaugeCouplingDerivation()
    # Evaluate at two scales (dimensionless ratio check only)
    r1 = gcd.compute_running_couplings(10.0)
    r2 = gcd.compute_running_couplings(100.0)
    for k in ("alpha1_inv", "alpha2_inv", "alpha3_inv"):
        assert isinstance(r1[k], float) and isinstance(r2[k], float)
    # Scale ratios should be positive and ordered
    assert r1["scale_ratio"] > 0
    assert r2["scale_ratio"] > r1["scale_ratio"]

