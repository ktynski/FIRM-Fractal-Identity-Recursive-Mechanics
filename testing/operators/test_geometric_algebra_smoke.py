from foundation.operators.geometric_algebra import (
    GEOMETRIC_ALGEBRA_FOUNDATION,
    GeometricAlgebraFoundation,
    Multivector,
    MultivectorGrade,
    CliffordSignature,
)


def _mv(coeffs, interp=""):
    return Multivector(coefficients=coeffs, grade=None, phi_scaling=1.0, geometric_interpretation=interp)


def test_geometric_algebra_products():
    ga = GeometricAlgebraFoundation(signature=CliffordSignature.MINKOWSKI)
    a = _mv({(0,): 1.0}, "time-like basis")
    b = _mv({(1,): 2.0}, "space-like basis")

    gp = ga.geometric_product(a, b)
    assert gp.operation_type == "geometric_product"
    assert isinstance(gp.result_multivector.coefficients, dict)

    ext = ga.exterior_product(a, b)
    assert ext.operation_type == "exterior_product"
    assert any(len(k) == 2 for k in ext.result_multivector.coefficients.keys())

    dot = ga.interior_product(a, b)
    assert dot.operation_type == "interior_product"


def test_spacetime_basis_and_emergence():
    ga = GEOMETRIC_ALGEBRA_FOUNDATION
    basis = ga.create_spacetime_basis()
    assert set(["e_0", "e_1", "e_2", "e_3", "I"]).issubset(set(basis.keys()))
    assert basis["e_0"].grade == MultivectorGrade.VECTOR
    emergent = ga.derive_spacetime_emergence()
    assert "spacetime_dimension" in emergent and emergent["spacetime_dimension"] == 4
