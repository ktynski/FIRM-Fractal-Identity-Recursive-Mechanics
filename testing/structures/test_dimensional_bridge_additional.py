from structures.dimensional_bridge import DIMENSIONAL_BRIDGE, DimensionalQuantity, DimensionType


def test_dimensionless_passthrough_and_units():
    q_math = DimensionalQuantity(
        value=2.0,
        dimensions={DimensionType.DIMENSIONLESS: 0},
        unit="dimensionless",
        mathematical_justification="test"
    )
    q_phys = DIMENSIONAL_BRIDGE.convert_mathematical_to_physical(q_math)
    assert q_phys.unit == "dimensionless"
    assert q_phys.value == 2.0


def test_length_conversion_symmetry_and_consistency():
    q_math = DimensionalQuantity(
        value=3.0,
        dimensions={DimensionType.LENGTH: 1},
        unit="L",
        mathematical_justification="φ-native length"
    )
    q_phys = DIMENSIONAL_BRIDGE.convert_mathematical_to_physical(q_math)
    q_back = DIMENSIONAL_BRIDGE.convert_physical_to_mathematical(q_phys)
    assert abs(q_back.value - q_math.value) < 1e-12
    assert q_phys.unit in ("m", "m^1")
