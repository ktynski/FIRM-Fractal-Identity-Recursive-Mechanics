from utils.precision_framework import compute_with_precision
import numpy as np


def test_precision_framework_multiple_operations():
    res1, analysis1 = compute_with_precision("phi_power", 3)
    assert analysis1.precision_achieved >= 30
    mat = np.array([[1.0, 0.0], [0.0, 2.0]], dtype=np.complex128)
    res2, analysis2 = compute_with_precision("eigenvalue", mat)
    assert isinstance(res2, (list, tuple)) or res2 is not None
