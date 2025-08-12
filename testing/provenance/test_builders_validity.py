from provenance.derivation_tree import PROVENANCE_VALIDATOR


def _assert_tree_valid(tree):
    results = PROVENANCE_VALIDATOR.validate_tree(tree)
    assert results["structure_valid"] is True
    assert results["provenance_complete"] is True
    assert results["contamination_free"] is True


def test_alpha_provenance_builder_valid():
    from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA, DerivationMethod
    tree = FINE_STRUCTURE_ALPHA.build_complete_provenance(DerivationMethod.PHI_POWERS_PRIMARY)
    _assert_tree_valid(tree)


def test_mass_ratio_provenance_builder_valid():
    from constants.mass_ratios import FUNDAMENTAL_MASSES
    tree = FUNDAMENTAL_MASSES.build_mass_ratio_provenance("proton", "electron")
    _assert_tree_valid(tree)


def test_mixing_angles_provenance_builders_valid():
    from constants.mixing_angles import MixingAnglesDerivation
    M = MixingAnglesDerivation()
    _assert_tree_valid(M.build_weinberg_provenance())
    # Exercise per-element variants
    for elem in ("V_us", "V_cb", "V_ub"):
        _assert_tree_valid(M.build_ckm_provenance(elem))

