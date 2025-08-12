from structures.dimensional_bridge import DimensionalBridge, DimensionalQuantity, DimensionType


def test_dimensions_compatibility_and_interpretation():
    db = DimensionalBridge()
    dq1 = DimensionalQuantity(1.0, {DimensionType.LENGTH: 1}, "mu", "")
    dq2 = DimensionalQuantity(2.0, {DimensionType.LENGTH: 1}, "mu", "")
    dq3 = DimensionalQuantity(3.0, {DimensionType.LENGTH: 1, DimensionType.TIME: -1}, "mu", "")
    # Same dims → compatible
    assert db._are_dimensions_compatible(dq1.dimensions, dq2.dimensions) is True  # type: ignore[attr-defined]
    # Different dims → not compatible
    assert db._are_dimensions_compatible(dq1.dimensions, dq3.dimensions) is False  # type: ignore[attr-defined]
    # Interpretation string includes exponents
    s = db._generate_dimensional_interpretation(dq3.dimensions)  # type: ignore[attr-defined]
    text = s.lower().replace(" ", "")
    assert "length" in text and ("time^-1" in text or "time^-1" in text)
