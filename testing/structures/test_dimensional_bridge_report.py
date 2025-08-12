from structures.dimensional_bridge import DimensionalBridge, DimensionType, DimensionalQuantity


def test_dimensional_report_generation():
    db = DimensionalBridge()
    dq = DimensionalQuantity(
        value=1.0,
        dimensions={DimensionType.LENGTH: 1, DimensionType.TIME: -1},
        unit="mathematical_units",
        mathematical_justification="test",
    )
    phys = db.convert_mathematical_to_physical(dq)
    assert isinstance(phys.value, float)
    # Report string should be generated without errors
    report = db.generate_dimensional_report()
    assert isinstance(report, str) and "DIMENSIONAL BRIDGE REPORT" in report
