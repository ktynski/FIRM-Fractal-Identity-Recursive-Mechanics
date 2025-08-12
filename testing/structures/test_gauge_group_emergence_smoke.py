from structures.gauge_group_emergence import GAUGE_GROUP_EMERGENCE


def test_standard_model_groups_present():
    u1 = GAUGE_GROUP_EMERGENCE.get_standard_model_group("U1_Y")
    su2 = GAUGE_GROUP_EMERGENCE.get_standard_model_group("SU2_L")
    su3 = GAUGE_GROUP_EMERGENCE.get_standard_model_group("SU3_C")
    assert u1 is not None and su2 is not None and su3 is not None
    uni = GAUGE_GROUP_EMERGENCE.compute_gauge_coupling_unification()
    assert "alpha_gut_predicted" in uni and uni["alpha_gut_predicted"] > 0
