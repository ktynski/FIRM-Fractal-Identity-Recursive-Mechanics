"""Comprehensive tests for gauge couplings module to boost coverage to 95%+."""

import pytest
from constants.gauge_couplings import (
    GaugeCouplingDerivation,
    GAUGE_COUPLINGS,
    GaugeGroup,
    CouplingType,
    EnergyScale
)


def test_running_couplings_computation():
    """Test running coupling computation at various energy scales."""
    gc = GaugeCouplingDerivation()

    # Test at reference scale (should return baseline values)
    running_ref = gc.compute_running_couplings(1.0)
    assert "alpha1_inv" in running_ref
    assert "alpha2_inv" in running_ref
    assert "alpha3_inv" in running_ref
    assert "scale_ratio" in running_ref
    assert running_ref["scale_ratio"] == 1.0

    # Test at higher energy (couplings should evolve)
    running_high = gc.compute_running_couplings(100.0)
    assert running_high["alpha1_inv"] != running_ref["alpha1_inv"]
    assert running_high["scale_ratio"] == 100.0

    # Test at very low energy
    running_low = gc.compute_running_couplings(0.1)
    assert running_low["alpha1_inv"] > 0
    assert running_low["scale_ratio"] == 0.1


def test_sm_one_loop_betas():
    """Test SM one-loop beta coefficients."""
    gc = GaugeCouplingDerivation()
    b1, b2, b3 = gc._compute_sm_one_loop_betas()

    # Check expected SM values
    assert abs(b1 - 41.0/6.0) < 1e-10
    assert abs(b2 - (-19.0/6.0)) < 1e-10
    assert abs(b3 - (-7.0)) < 1e-10


def test_grand_unification_analysis():
    """Test GUT scale analysis and predictions."""
    gc = GaugeCouplingDerivation()
    gc._analyze_grand_unification()

    # Check GUT coupling was created
    assert "GUT_unified" in gc._coupling_results
    gut = gc._coupling_results["GUT_unified"]

    assert gut.gauge_group == GaugeGroup.SU2_WEAK
    assert gut.coupling_type == CouplingType.UNIFIED
    assert gut.energy_scale == EnergyScale.GUT
    assert gut.alpha_inverse > 0
    assert "φ⁵" in gut.phi_expression


def test_gut_scale_unification_api():
    """Test public GUT unification prediction API."""
    gc = GaugeCouplingDerivation()
    gut_pred = gc.predict_gut_scale_unification()

    required_keys = [
        "unification_scale", "unification_scale_factor",
        "reference_scale_label", "alpha_gut", "unification_precision"
    ]
    for key in required_keys:
        assert key in gut_pred

    assert gut_pred["reference_scale_label"] == "MZ"
    assert gut_pred["unification_scale"] > 0
    assert gut_pred["alpha_gut"] > 0
    assert gut_pred["unification_precision"] > 0


def test_coupling_constants_report_generation():
    """Test complete coupling constants report generation."""
    gc = GaugeCouplingDerivation()
    report = gc.generate_coupling_constants_report()

    assert isinstance(report, str)
    assert "FIRM Gauge Coupling Constants Report" in report
    assert "φ =" in report
    assert "STANDARD MODEL GAUGE COUPLINGS" in report
    assert "ELECTROMAGNETIC COUPLING" in report
    assert "GRAND UNIFICATION" in report
    assert "φ-mathematics" in report


def test_experimental_agreement_verification():
    """Test experimental agreement verification (theory-only mode)."""
    gc = GaugeCouplingDerivation()
    agreement = gc.verify_experimental_agreement()

    # In theory-only mode, should return empty or handle gracefully
    assert isinstance(agreement, dict)


def test_coupling_provenance_all_groups():
    """Test provenance building for all gauge groups."""
    gc = GaugeCouplingDerivation()

    groups = ["U1_hypercharge", "SU2_weak", "SU3_strong", "EM_coupling"]
    for group in groups:
        tree = gc.build_coupling_provenance(group)
        assert tree is not None
        assert len(tree.nodes) > 5  # Should have axioms + terms + computation

        # Check for expected node types
        node_types = {node.derivation_type.value for node in tree.nodes.values()}
        assert "axiom" in node_types
        assert "definition" in node_types or "lemma" in node_types


def test_coupling_provenance_corrected_em():
    """Test EM coupling provenance with corrected variant nodes."""
    gc = GaugeCouplingDerivation()

    # Test corrected=True adds variant nodes
    tree_corr = gc.build_coupling_provenance("EM_coupling", corrected=True)
    corrected_nodes = [
        "VAR_TERM_ALPHA_PHI", "VAR_TERM_LOG_PHI11",
        "VAR_TERM_PHI_INV", "VAR_SIN2_THETA_W_CORRECTED"
    ]
    for node_id in corrected_nodes:
        assert node_id in tree_corr.nodes


def test_coupling_provenance_invalid_group():
    """Test provenance building with invalid gauge group."""
    gc = GaugeCouplingDerivation()

    with pytest.raises(ValueError, match="Unknown gauge group"):
        gc.build_coupling_provenance("INVALID_GROUP")


def test_gauge_couplings_singleton_properties():
    """Test GAUGE_COUPLINGS singleton properties and methods."""
    # Test alpha_em_inverse property
    alpha_em_inv = GAUGE_COUPLINGS.alpha_em_inverse
    assert alpha_em_inv is None or alpha_em_inv > 0

    # Test individual coupling derivation methods
    u1_result = GAUGE_COUPLINGS.derive_u1_hypercharge_coupling()
    assert u1_result.gauge_group == GaugeGroup.U1_HYPERCHARGE
    assert u1_result.alpha_inverse > 0

    su2_result = GAUGE_COUPLINGS.derive_su2_weak_coupling()
    assert su2_result.gauge_group == GaugeGroup.SU2_WEAK
    assert su2_result.alpha_inverse > 0

    su3_result = GAUGE_COUPLINGS.derive_su3_strong_coupling()
    assert su3_result.gauge_group == GaugeGroup.SU3_STRONG
    assert su3_result.alpha_inverse > 0


def test_gut_unification_back_compat():
    """Test back-compatibility method for GUT predictions."""
    gc = GaugeCouplingDerivation()
    gut_pred1 = gc.predict_gut_unification()
    gut_pred2 = gc.predict_gut_scale_unification()

    # Should return same result
    assert gut_pred1 == gut_pred2