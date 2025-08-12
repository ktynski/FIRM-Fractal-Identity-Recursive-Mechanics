from structures.physical_units import PHYSICAL_UNITS


def test_physical_units_exact_and_conversions():
    u = PHYSICAL_UNITS
    # Exact SI definitions should match floats and be positive
    assert u.C_LIGHT_M_PER_S == 299_792_458.0
    assert u.PLANCK_CONSTANT_J_S > 0
    assert u.BOLTZMANN_CONSTANT_J_PER_K > 0
    assert u.ELEMENTARY_CHARGE_C > 0
    # Derived conversions
    assert abs(u.PLANCK_CONSTANT_EV_S - (u.PLANCK_CONSTANT_J_S / u.ELEMENTARY_CHARGE_C)) < 1e-30
    assert abs(u.BOLTZMANN_CONSTANT_EV_PER_K - (u.BOLTZMANN_CONSTANT_J_PER_K / u.ELEMENTARY_CHARGE_C)) < 1e-30

