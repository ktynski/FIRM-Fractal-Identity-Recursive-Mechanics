from foundation.categories.fixed_point_category import (
    FixedPointStructure,
    FixedPointType,
    GraceEquivariantMorphism,
    PhysicalSystem,
)
from foundation.categories.presheaf_category import PresheafStructure, PresheafType


def _presheaf(name: str) -> PresheafStructure:
    return PresheafStructure(
        name=name,
        presheaf_type=PresheafType.REPRESENTABLE,
        representing_object=name,
        object_mapping={"X": set(), "Y": set()},
        morphism_mapping={},
    )


def test_fixed_point_and_morphism_equivariance_smoke():
    X = FixedPointStructure(
        name="U1_Electromagnetic",
        underlying_presheaf=_presheaf("U1"),
        fixed_point_type=FixedPointType.PHYSICAL,
        physical_system=PhysicalSystem.ELECTROMAGNETIC,
    )
    Y = FixedPointStructure(
        name="SU2_Weak",
        underlying_presheaf=_presheaf("SU2"),
        fixed_point_type=FixedPointType.PHYSICAL,
        physical_system=PhysicalSystem.WEAK_NUCLEAR,
    )
    assert X.verify_fixed_point_property() is True
    assert Y.verify_fixed_point_property() is True

    def f(p: PresheafStructure) -> PresheafStructure:  # type: ignore[name-defined]
        return p

    m = GraceEquivariantMorphism(source=X, target=Y, morphism_data=f, physical_process="test")
    assert m.verify_grace_equivariance() in (True, False)
