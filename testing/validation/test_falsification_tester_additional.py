from validation.falsification_tester import FalsificationTester, FalsificationCriterion


def test_falsification_tester_minimal_paths():
    ft = FalsificationTester()
    # Exercise single-criterion checker alias on a criterion
    spec_map = ft._initialize_criteria_specifications()
    ft._check_single_criterion(FalsificationCriterion.MATHEMATICAL_INCONSISTENCY, spec_map[FalsificationCriterion.MATHEMATICAL_INCONSISTENCY])
    status = ft.get_current_status()
    assert "criteria_status" in status

