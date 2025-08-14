from structures.dimensional_bridge import DimensionalBridge, DimensionalQuantity, DimensionType


def test_basic_conversion_roundtrip_dimensionless_and_units():
    bridge = DimensionalBridge()
    # Mass dimension 1
    mq = DimensionalQuantity(value=2.0, dimensions={DimensionType.MASS: 1}, unit="math", mathematical_justification="test")
    pq = bridge.convert_mathematical_to_physical(mq)
    assert pq.unit != "dimensionless"
    # Roundtrip back to mathematical
    back = bridge.convert_physical_to_mathematical(pq)
    # Roundtrip should recover original value within numerical tolerance
    assert abs(back.value - mq.value) < 1e-12
    # Consistency check API: using identical dimensions should be True
    assert bridge.verify_dimensional_consistency([mq, mq]) is True
