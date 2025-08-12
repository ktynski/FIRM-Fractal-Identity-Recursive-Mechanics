from foundation.categories.fixed_point_category import (
    PHYSICAL_REALITY,
    GraceEquivariantMorphism,
    PhysicalSystem,
)


def test_enumerate_groups_and_derive_constants():
    cat = PHYSICAL_REALITY
    # Ensure we can enumerate gauge groups
    groups = cat.enumerate_gauge_groups()
    assert isinstance(groups, dict)
    assert any("U(1)" in v for v in groups.values())

    # Add an EM → EM morphism and derive constants
    em = cat.example_object("X")  # maps to U1_EM
    morph = GraceEquivariantMorphism(source=em, target=em, morphism_data=lambda p: p, physical_process="electromagnetic interaction")
    cat.add_grace_morphism(morph)
    consts = cat.derive_fundamental_constants()
    # Presence of fine-structure alpha derived from morphism
    assert "fine_structure_alpha" in consts and consts["fine_structure_alpha"] > 0
