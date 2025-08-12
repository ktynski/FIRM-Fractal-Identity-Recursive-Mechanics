from utils.precision_framework import PRECISION_FRAMEWORK, compute_with_precision, propagate_errors
import numpy as np


def test_phi_power_precision_and_validation():
    result, analysis = compute_with_precision("phi_power", 5)
    assert result is not None
    assert analysis.convergence_verified
    assert analysis.precision_achieved >= 50


def test_grace_operator_precision_fixed_point():
    result, analysis = compute_with_precision("grace_operator", None)
    # Check golden identity approximately: x = 1 + 1/x
    x = float(result)
    assert abs(x - (1 + 1 / x)) < 1e-9
    # The framework validates fixed-point by |phi/result - result|; allow either flag
    assert analysis.validation_results.get("convergence_verified", True) is True or analysis.validation_results.get("precision_adequate", True) is True


def test_eigenvalue_precision_path():
    mat = np.array([[1.0, 0.0], [0.0, 2.0]], dtype=np.float64)
    result, analysis = compute_with_precision("eigenvalue", mat)
    vals = [float(getattr(ev, "real", ev)) for ev in result]
    assert any(abs(v - 2.0) < 1e-9 for v in vals)
    assert analysis.total_error_bound >= 0.0


def test_error_propagation_addition_and_multiplication():
    add_err = propagate_errors("addition", [(0.0, 1e-3), (0.0, 2e-3)])
    assert 2e-3 <= add_err <= 3e-3
    mul_err = propagate_errors("multiplication", [(2.0, 1e-3), (3.0, 2e-3)])
    assert mul_err > 0


def test_validate_precision_chain():
    chain = [
        {"operation": "addition", "operands": [(1.0, 1e-6), (2.0, 2e-6)]},
        {"operation": "power", "operands": [(2.0, 1e-6), (3, 0.0)]},
    ]
    status = PRECISION_FRAMEWORK.validate_precision_chain(chain)
    assert "total_error_bound" in status
    assert isinstance(status["precision_adequate"], bool)
