from __future__ import annotations

import sys
import pytest

from validation import validate_all_firm_predictions, main


def test_validate_all_firm_predictions_structure():
    results = validate_all_firm_predictions()
    assert isinstance(results, dict)
    # Expect several standard keys to be present
    expected_some = {
        "firewall_active",
        "sealed_datasets_intact",
        "comparator_enabled",
        "analysis_nonempty",
        "precision_framework_operational",
        "phi_recursion_convergence",
        "grace_operator_contraction",
        "banach_conditions",
        "spacetime_dimensionality",
        "axiom_system_valid",
    }
    assert expected_some.issubset(set(results.keys()))

    # Each item should expose a validation_status with .value
    sample_key = next(iter(expected_some))
    item = results[sample_key]
    assert hasattr(item, "validation_status")
    assert hasattr(item.validation_status, "value")


def test_validation_main_cli_exits():
    # main() prints summary and exits; accept either success/failure code
    old_argv = sys.argv
    sys.argv = ["firm-validate"]
    try:
        with pytest.raises(SystemExit) as exc:
            main()
        assert isinstance(exc.value.code, int)
        assert exc.value.code in (0, 1)
    finally:
        sys.argv = old_argv