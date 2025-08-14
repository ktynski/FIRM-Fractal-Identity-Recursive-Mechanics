from constants.fine_structure_alpha import (
    FineStructureConstant,
    DerivationMethod,
    FINE_STRUCTURE_ALPHA,
    ALPHA_THEORETICAL,
    ALPHA_INVERSE_THEORETICAL,
)


def test_fine_structure_alpha_derivations_and_provenance():
    inst = FineStructureConstant()
    # Alternative derivation path returns sensible values
    alt = inst.derive_alternative_phi_expression()
    assert alt.alpha_value > 0 and alt.alpha_inverse_value > 0
    # Morphic alias returns consistent values
    morph = inst.derive_morphic_structure_expression()
    assert morph.alpha_value > 0 and morph.alpha_inverse_value > 0
    # Provenance for primary path is available
    prov = inst.build_complete_provenance(DerivationMethod.PHI_POWERS_PRIMARY)
    if isinstance(prov, list):
        assert len(prov) >= 1
    else:
        assert hasattr(prov, "root_node") and hasattr(prov, "nodes")
    # Module-level theory constants are positive
    assert ALPHA_THEORETICAL > 0 and ALPHA_INVERSE_THEORETICAL > 0
