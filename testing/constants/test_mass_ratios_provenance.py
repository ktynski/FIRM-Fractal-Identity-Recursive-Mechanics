from constants.mass_ratios import FUNDAMENTAL_MASSES


def test_mass_ratio_provenance_builder_proton_electron():
    tree = FUNDAMENTAL_MASSES.build_mass_ratio_provenance("proton", "electron")
    assert tree is not None
    assert "m_proton/m_electron" in tree.root_node.mathematical_expression or "m_proton/m_electron" in tree.target_result
    # Value sanity via API
    ratio = FUNDAMENTAL_MASSES.get_mass_ratio("proton", "electron")
    assert ratio > 1.0

