from constants import (
    FIRM_CONSTANTS_REGISTRY,
    fine_structure_alpha,
    mass_ratios,
    get_constants_by_category,
)


def test_constants_registry_contains_core_systems():
    # Test the new unified registry
    all_constants = FIRM_CONSTANTS_REGISTRY.get_all_constants()
    assert "fine_structure_alpha" in all_constants
    assert "mass_ratios" in all_constants

    # Test category-based access
    fundamental = get_constants_by_category("fundamental")
    assert len(fundamental) > 0
