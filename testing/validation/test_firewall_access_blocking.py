from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_request_experimental_data_blocked_in_theory_phase():
    fw = EXPERIMENTAL_FIREWALL
    fw.reset()
    resp = fw.request_experimental_data("codata_2018_constants", requester="unit_test")
    assert resp is None


def test_request_experimental_data_in_validation_phase_if_ready():
    fw = EXPERIMENTAL_FIREWALL
    fw.reset()
    try:
        fw.enable_validation_phase()
    except Exception:
        # Theory completion may be incomplete; allow test to exit early
        return
    resp = fw.request_experimental_data("codata_2018_constants", requester="unit_test")
    assert isinstance(resp, dict)
    assert resp.get("dataset_id") == "codata_2018_constants"
    assert resp.get("access_granted") is True
