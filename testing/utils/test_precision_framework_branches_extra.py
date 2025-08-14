def test_precision_framework_operations_and_validation():
    import numpy as np
    from utils.precision_framework import PRECISION_FRAMEWORK, PrecisionRequirement

    # compute phi_power (int and float)
    r_int, ea_int = PRECISION_FRAMEWORK.compute_with_precision("phi_power", 3)
    r_float, ea_float = PRECISION_FRAMEWORK.compute_with_precision("phi_power", 2.5)
    assert ea_int.convergence_verified is True and ea_float.convergence_verified is True

    # grace_operator path
    r_go, ea_go = PRECISION_FRAMEWORK.compute_with_precision("grace_operator", None)
    assert ea_go.precision_achieved >= 50

    # eigenvalue path
    mat = np.array([[1.0, 0.0],[0.0, 2.0]], dtype=float)
    r_ev, ea_ev = PRECISION_FRAMEWORK.compute_with_precision("eigenvalue", mat)
    assert len(r_ev) == 2

    # propagate various errors
    add_err = PRECISION_FRAMEWORK.propagate_errors("addition", [(1.0, 1e-3), (2.0, 1e-3)])
    mul_err = PRECISION_FRAMEWORK.propagate_errors("multiplication", [(2.0, 1e-3), (3.0, 2e-3)])
    pow_err = PRECISION_FRAMEWORK.propagate_errors("power", [(2.0, 1e-3), (3, )])
    log_err = PRECISION_FRAMEWORK.propagate_errors("logarithm", [(2.0, 1e-3)])
    exp_err = PRECISION_FRAMEWORK.propagate_errors("exponential", [(1.0, 1e-3)])
    assert all(isinstance(x, float) for x in (add_err, mul_err, pow_err, log_err, exp_err))

    # validate_precision_chain
    chain = [
        {"operation": "addition", "operands": [(1.0, 1e-6), (2.0, 1e-6)]},
        {"operation": "multiplication", "operands": [(2.0, 1e-6), (3.0, 1e-6)]},
        {"operation": "power", "operands": [(2.0, 1e-6), (3,)]},
    ]
    val = PRECISION_FRAMEWORK.validate_precision_chain(chain)
    assert isinstance(val, dict) and "validation_passed" in val
