def test_precision_framework_high_precision_constants():
    from utils.precision_framework import PRECISION_FRAMEWORK
    consts = PRECISION_FRAMEWORK.high_precision_constants
    # Ensure keys present and values are Decimal-like
    for k in ("phi", "pi", "e", "ln_phi"):
        assert k in consts

