from foundation.categories.fixed_point_category import FixedPointCategory, GraceEquivariantMorphism


def test_morphisms_and_extract_physical_constants_branches():
    cat = FixedPointCategory()
    x = cat.example_object("X")  # U1_EM
    y = cat.example_object("Y")  # SU2_Weak
    z = cat.example_object("Z")  # SU3_Strong

    m_em = GraceEquivariantMorphism(source=x, target=x, morphism_data=lambda p: p, physical_process="electromagnetic process")
    m_weak = GraceEquivariantMorphism(source=y, target=y, morphism_data=lambda p: p, physical_process="weak process")
    m_strong = GraceEquivariantMorphism(source=z, target=z, morphism_data=lambda p: p, physical_process="strong process")

    cat.add_grace_morphism(m_em)
    cat.add_grace_morphism(m_weak)
    cat.add_grace_morphism(m_strong)

    # constants extraction branches
    c_em = m_em.extract_physical_constants()
    c_wk = m_weak.extract_physical_constants()
    c_st = m_strong.extract_physical_constants()
    assert "fine_structure_alpha" in c_em
    assert "weak_coupling" in c_wk
    assert "strong_coupling" in c_st

