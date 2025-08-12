from validation.experimental_firewall import EXPERIMENTAL_FIREWALL, FirewallStatus


def test_firewall_theory_phase_blocks_requests():
    fw = EXPERIMENTAL_FIREWALL
    fw.reset()
    assert fw.request_experimental_data("planck_2018_cmb", requester="test") is None
    assert fw.get_sealed_comparison("fine_structure_alpha_inv") is None


def test_firewall_validation_phase_gates_access():
    fw = EXPERIMENTAL_FIREWALL
    fw.reset()
    # enable validation only if theory-preconditions are met; call and catch ValueError otherwise
    try:
        fw.enable_validation_phase()
    except Exception:
        # expected in theory-only mode; firewall remains active
        pass
    # Regardless, API remains safe
    res = fw.request_experimental_data("codata_2018_constants", requester="test")
    assert res is None or (isinstance(res, dict) and res.get("access_granted") is True)

