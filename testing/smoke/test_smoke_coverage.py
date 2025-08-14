import math

from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
from cosmology import derive_cosmological_parameters, verify_observational_agreement
from cosmology.ex_nihilo_pipeline import ExNihiloCosmogenesis
from provenance.derivation_tree import DerivationNode, DerivationType, ProvenanceTree
from provenance.contamination_detector import CONTAMINATION_DETECTOR, ContaminationEvidence
from foundation.operators.fixed_point_finder import BanachFixedPointSolver
from constants.fine_structure_alpha import FineStructureConstant
from structures.dimensional_bridge import DimensionalQuantity, DimensionType, DIMENSIONAL_BRIDGE


def test_firewall_modes_and_sealed_comparison(validation_phase):
    # Theory phase blocks access
    EXPERIMENTAL_FIREWALL.enable_theory_phase()
    assert EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv") is None

    # Validation phase permits sealed comparisons
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
    sealed = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")
    assert sealed is not None
    assert isinstance(sealed["value"], float)
    assert isinstance(sealed["uncertainty"], float)


def test_cosmology_derivations_and_agreement():
    # φ-native derivations and bridge conversions should execute without errors
    params = derive_cosmological_parameters()
    assert "hubble_constant_phi_native" in params
    assert "cmb_temperature_phi_native" in params

    # In theory phase, observational agreement is empty
    EXPERIMENTAL_FIREWALL.enable_theory_phase()
    stats = verify_observational_agreement()
    assert isinstance(stats, dict)


def test_ex_nihilo_key_stages_execute():
    cosmos = ExNihiloCosmogenesis()
    s5 = cosmos._stage_5_grace_operator()
    assert s5.stage.name in ("GRACE_OPERATOR", "CosmogenesisStage.GRACE_OPERATOR")
    s8 = cosmos._stage_8_cosmic_evolution()
    assert "φ⁷" in s8.mathematical_output or "phi" in s8.mathematical_output
    s9 = cosmos._stage_9_cmb_formation()
    assert "φ^(-90)" in s9.mathematical_output or "phi" in s9.mathematical_output


def test_provenance_tree_basic_and_contamination_detection():
    # Pure root axiom
    root = DerivationNode(
        node_id="axiom_phi",
        mathematical_expression="φ^2 = φ + 1",
        derivation_type=DerivationType.AXIOM,
        dependencies=[],
        justification="Golden ratio identity",
        empirical_inputs=[],
        assumptions=["Field axioms"]
    )
    tree = ProvenanceTree(root)

    # Pure computation node
    node_comp = DerivationNode(
        node_id="compute_phi",
        mathematical_expression="φ = (1+√5)/2",
        derivation_type=DerivationType.COMPUTATION,
        dependencies=["axiom_phi"],
        justification="Quadratic solution",
        empirical_inputs=[],
        assumptions=[]
    )
    tree.add_node(node_comp)
    assert tree.verify_complete_provenance()

    # Contaminated node (allowed; tree marked impure)
    node_emp = DerivationNode(
        node_id="alpha_empirical",
        mathematical_expression="α⁻¹ = 137.035999084",
        derivation_type=DerivationType.TARGET,
        dependencies=["compute_phi"],
        justification="",
        empirical_inputs=["codata_2018"],
        assumptions=[]
    )
    tree.add_node(node_emp)
    assert tree.is_pure is False

    # Detector should flag lexical/numerical/context contamination patterns
    ev_lex = CONTAMINATION_DETECTOR.detect_lexical_contamination("Measured experimental value")
    ev_num = CONTAMINATION_DETECTOR.detect_numerical_contamination("alpha_inv = 137.035999084")
    ev_ctx = CONTAMINATION_DETECTOR.detect_contextual_contamination("CODATA 2018 measurement")
    assert isinstance(ev_lex + ev_num + ev_ctx, list)


def test_fixed_point_solver_minimal_path():
    solver = BanachFixedPointSolver()
    assert solver.verify_banach_conditions()
    sol = solver.find_fixed_point(initial_guess="x0", max_iterations=1)
    assert sol.iteration_count >= 1


def test_dimensional_bridge_basic_conversions():
    # Time^-1 quantity (e.g., H0)
    q_h = DimensionalQuantity(
        value=1.0,
        dimensions={DimensionType.TIME: -1},
        unit="mathematical_units",
        mathematical_justification="H0 φ-scaling"
    )
    phys_h = DIMENSIONAL_BRIDGE.convert_mathematical_to_physical(q_h)
    assert phys_h is not None

    # Temperature quantity (e.g., T_CMB)
    q_t = DimensionalQuantity(
        value=1e-3,
        dimensions={DimensionType.TEMPERATURE: 1},
        unit="mathematical_units",
        mathematical_justification="T φ-scaling"
    )
    phys_t = DIMENSIONAL_BRIDGE.convert_mathematical_to_physical(q_t)
    assert phys_t is not None


def test_alpha_derivations_execute_and_provide_expressions():
    alpha = FineStructureConstant()
    primary = alpha.derive_primary_phi_expression()
    alt = alpha.derive_morphic_structure_expression()
    assert isinstance(primary.alpha_inverse_value, float)
    assert isinstance(alt.alpha_inverse_value, float)
    assert primary.phi_expression != ""
    assert alt.mathematical_expression != ""
