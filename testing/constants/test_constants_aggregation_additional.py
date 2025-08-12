from constants import (
    FUNDAMENTAL_CONSTANTS,
    FINE_STRUCTURE_ALPHA,
    GAUGE_COUPLINGS,
    FUNDAMENTAL_MASSES,
)


def test_constants_registry_contains_core_systems():
    assert "fine_structure" in FUNDAMENTAL_CONSTANTS
    assert FUNDAMENTAL_CONSTANTS["fine_structure"] is FINE_STRUCTURE_ALPHA
    assert FUNDAMENTAL_CONSTANTS["gauge_couplings"] is GAUGE_COUPLINGS
    assert FUNDAMENTAL_CONSTANTS["mass_ratios"] is FUNDAMENTAL_MASSES

