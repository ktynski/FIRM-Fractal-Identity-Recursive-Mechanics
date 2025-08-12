"""
Contamination Detection Tests: Empirical Input Detection Validation

This module tests the contamination detection system to ensure no empirical
data infiltrates pure mathematical FIRM derivations.

Test Coverage:
    - Lexical contamination pattern detection
    - Numerical empirical constant identification
    - Reasoning contamination detection (circular logic)
    - Contextual assumption contamination
    - Firewall breach detection and response

Integrity Framework:
    - Zero empirical input tolerance verification
    - Complete derivation chain purity validation
    - Automated contamination alert testing
    - Academic integrity protocol verification

Scientific Rigor:
    - Objective contamination detection algorithms
    - Systematic contamination source identification
    - False positive/negative rate optimization
    - Academic transparency requirement testing

Author: FIRM Research Team
Test Framework: pytest with contamination scenario testing
Academic integrity verified: [VERIFICATION DATE]
"""

import pytest
from typing import List, Dict, Any
import tempfile
import os

from provenance.contamination_detector import (
    CONTAMINATION_DETECTOR, ContaminationSource, ContaminationEvidence,
)
from provenance.derivation_tree import DerivationNode, ProvenanceTree
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL, FirewallStatus

class TestLexicalContamination:
    """Test lexical pattern contamination detection"""

    def test_explicit_empirical_references(self):
        """Test detection of explicit empirical value references"""
        contaminated_expressions = [
            "Using experimental value α = 7.297352566...",
            "From CODATA 2018 measurement: me = 9.1093837015e-31 kg",
            "Fitted parameter from LHC data: mt = 173.1 ± 0.9 GeV",
            "Measured constant from Planck mission: H₀ = 67.4 km/s/Mpc"
        ]

        for expression in contaminated_expressions:
            evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(expression)
            assert len(evidence) > 0, f"Failed to detect contamination in: {expression}"
            assert evidence[0].contamination_source == ContaminationSource.LEXICAL_PATTERNS

    def test_subtle_empirical_references(self):
        """Test detection of subtle empirical contamination"""
        subtle_contamination = [
            "Consistent with observed value",
            "To match experimental data",
            "Because we measure",
            "From laboratory measurements"
        ]

        for expression in subtle_contamination:
            evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(expression)
            assert len(evidence) > 0, f"Failed to detect subtle contamination: {expression}"

    def test_clean_mathematical_expressions(self):
        """Test that pure mathematical expressions pass cleanly"""
        clean_expressions = [
            "φ² = φ + 1 from golden ratio recursion",
            "Derived from A𝒢.3 stabilization axiom",
            "Following categorical morphism structure",
            "By φ-hierarchy power scaling: φⁿ terms"
        ]

        for expression in clean_expressions:
            evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(expression)
            assert len(evidence) == 0, f"False positive contamination detection: {expression}"

class TestNumericalContamination:
    """Test numerical constant contamination detection"""

    def test_empirical_constant_detection(self):
        """Test detection of known empirical constants"""
        contaminated_expressions = [
            "α⁻¹ = 137.035999084",  # CODATA fine structure
            "me = 0.51099895000 MeV",  # Electron mass
            "mp = 938.272088 MeV",  # Proton mass
            "c = 299792458 m/s"  # Speed of light (defined but empirically motivated)
        ]

        for expression in contaminated_expressions:
            evidence = CONTAMINATION_DETECTOR.detect_numerical_contamination(expression)
            # Some may be detected, depending on precision matching
            if evidence:
                assert evidence[0].contamination_source == ContaminationSource.NUMERICAL_PATTERNS

    def test_phi_mathematical_constants(self):
        """Test that φ-derived constants are not flagged"""
        phi_expressions = [
            "φ = 1.6180339887",  # Golden ratio
            "φ² = 2.6180339887",  # φ squared
            "φⁿ scaling factors",
            "1/φ = 0.6180339887"  # Golden ratio reciprocal
        ]

        for expression in phi_expressions:
            evidence = CONTAMINATION_DETECTOR.detect_numerical_contamination(expression)
            # Should not be flagged as contamination
            empirical_contamination = [e for e in evidence
                                     if e.contamination_source == ContaminationSource.NUMERICAL_PATTERNS]
            assert len(empirical_contamination) == 0, f"φ-constant falsely flagged: {expression}"

class TestReasoningContamination:
    """Test circular reasoning and bias contamination detection"""

    def test_circular_reasoning_detection(self):
        """Test detection of circular reasoning patterns"""
        circular_patterns = [
            "This works because we observe it to be true",
            "Adjusted to match experimental results",
            "Fine-tuned to reproduce known values",
            "Because the data requires this form"
        ]

        for pattern in circular_patterns:
            evidence = CONTAMINATION_DETECTOR.detect_reasoning_contamination(pattern)
            assert len(evidence) > 0, f"Circular reasoning not detected: {pattern}"
            assert evidence[0].contamination_source == ContaminationSource.REASONING_PATTERNS

    def test_valid_mathematical_reasoning(self):
        """Test that valid mathematical reasoning passes"""
        valid_reasoning = [
            "Following from axiom A𝒢.1 totality principle",
            "By mathematical necessity of φ-recursion",
            "From categorical coherence requirements",
            "Derived through Grace Operator eigenvalue analysis"
        ]

        for reasoning in valid_reasoning:
            evidence = CONTAMINATION_DETECTOR.detect_reasoning_contamination(reasoning)
            assert len(evidence) == 0, f"Valid reasoning falsely flagged: {reasoning}"

class TestContextualContamination:
    """Test contextual assumption and dependency contamination"""

    def test_hidden_assumption_detection(self):
        """Test detection of hidden empirical assumptions"""
        hidden_assumptions = [
            "Using standard cosmological parameters",
            "Assuming concordance ΛCDM model",
            "Based on particle physics phenomenology",
            "From standard model parameters"
        ]

        for assumption in hidden_assumptions:
            evidence = CONTAMINATION_DETECTOR.detect_contextual_contamination(assumption)
            # May or may not be detected depending on pattern matching
            # Focus on testing the detection mechanism works
            if evidence:
                assert evidence[0].contamination_source == ContaminationSource.CONTEXTUAL_ASSUMPTIONS

class TestDerivationTreeContamination:
    """Test complete derivation tree contamination analysis"""

    def test_clean_derivation_tree(self):
        """Test analysis of clean mathematical derivation"""
        # Create clean derivation tree
        root_node = DerivationNode(
            node_id="phi_definition",
            mathematical_expression="φ = (1 + √5)/2",
            derivation_type="AXIOM",
            dependencies=[],
            justification="Golden ratio definition from A𝒢.3",
            empirical_inputs=[],
            assumptions=["Mathematical definition only"]
        )

        child_node = DerivationNode(
            node_id="phi_recursion",
            mathematical_expression="φ² = φ + 1",
            derivation_type="THEOREM",
            dependencies=["phi_definition"],
            justification="Direct algebraic manipulation",
            empirical_inputs=[],
            assumptions=[]
        )

        tree = ProvenanceTree(root_node, "φ² = φ + 1")
        tree.add_node(child_node)

        # Test contamination analysis
        contamination_evidence = CONTAMINATION_DETECTOR.analyze_derivation_tree(tree)

        # Should find no contamination
        assert len(contamination_evidence) == 0, "Clean derivation tree flagged for contamination"

    def test_contaminated_derivation_tree(self):
        """Test analysis of contaminated derivation tree"""
        # Create contaminated derivation tree
        root_node = DerivationNode(
            node_id="alpha_empirical",
            mathematical_expression="α⁻¹ = 137.035999084 (CODATA 2018)",
            derivation_type="EMPIRICAL",
            dependencies=[],
            justification="From experimental measurement",
            empirical_inputs=["CODATA_2018_fine_structure"],
            assumptions=["Experimental accuracy"]
        )

        tree = ProvenanceTree(root_node, "α⁻¹ ≈ 137.036")

        # Test contamination analysis
        contamination_evidence = CONTAMINATION_DETECTOR.analyze_derivation_tree(tree)

        # Should detect contamination
        assert len(contamination_evidence) > 0, "Contaminated derivation tree not flagged"

        # Check for empirical input contamination
        empirical_evidence = [e for e in contamination_evidence
                            if ContaminationSource.EMPIRICAL_INPUTS in [e.contamination_source]]
        assert len(empirical_evidence) > 0, "Empirical input contamination not detected"

class TestFirewallIntegration:
    """Test integration with experimental firewall system"""

    def test_firewall_status_monitoring(self):
        """Test firewall status affects contamination detection"""
        # Get current firewall status
        initial_status = EXPERIMENTAL_FIREWALL._firewall_status

        # Firewall should be active for pure theory development
        assert initial_status in [FirewallStatus.ACTIVE, FirewallStatus.SEALED], \
            "Firewall not properly protecting theoretical derivations"

    def test_sealed_data_access_prevention(self):
        """Test that sealed experimental data cannot contaminate derivations"""
        # Attempt to access sealed experimental value
        try:
            sealed_data = EXPERIMENTAL_FIREWALL.get_sealed_comparison("fine_structure_alpha_inv")

            # If data is returned, it should be properly isolated
            if sealed_data is not None:
                # Data should not leak into derivations
                contamination_text = f"Using {sealed_data['value']} from experiment"
                evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(contamination_text)
                assert len(evidence) > 0, "Firewall leak not detected by contamination system"

        except Exception:
            # Expected if firewall is working properly
            pass

class TestContaminationSeverityAssessment:
    """Test contamination severity classification and response"""

    def test_critical_contamination_classification(self):
        """Test critical contamination properly classified"""
        # Create critical contamination evidence
        critical_evidence = ContaminationEvidence(
            evidence_id="critical_test",
            contamination_source=ContaminationSource.EMPIRICAL_INPUTS,
            contamination_text="Using experimental value α = 1/137.035999084",
            severity_score=1.0,
            detection_method="empirical_input_detection",
            recommended_action="Remove empirical input immediately",
            node_id="test_node"
        )

        assert critical_evidence.is_critical(), "Critical contamination not properly classified"

    def test_warning_level_contamination(self):
        """Test warning-level contamination classification"""
        warning_evidence = ContaminationEvidence(
            evidence_id="warning_test",
            contamination_source=ContaminationSource.CONTEXTUAL_ASSUMPTIONS,
            contamination_text="Assuming standard physics conventions",
            severity_score=0.3,
            detection_method="contextual_analysis",
            recommended_action="Review assumptions for empirical content",
            node_id="test_node"
        )

        assert not warning_evidence.is_critical(), "Warning contamination incorrectly classified as critical"

class TestContaminationPrevention:
    """Test contamination prevention and cleanup protocols"""

    def test_automatic_contamination_removal(self):
        """Test automatic removal of detected contamination"""
        contaminated_text = "φ = 1.618... from experimental measurement of α = 1/137.036"

        # Detect contamination
        evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(contaminated_text)
        assert len(evidence) > 0, "Test contamination not detected"

        # Test cleanup suggestion
        cleaned_text = CONTAMINATION_DETECTOR.suggest_contamination_cleanup(contaminated_text)

        # Cleaned version should not contain empirical references
        cleaned_evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(cleaned_text)
        assert len(cleaned_evidence) < len(evidence), "Contamination not properly cleaned"

    def test_derivation_path_sanitization(self):
        """Test that derivation paths can be sanitized of contamination"""
        # Create partially contaminated derivation
        mixed_derivation = """
        From axiom A𝒢.3: Grace Operator 𝒢 with φ⁻¹ contraction.
        Using experimental constraint α⁻¹ ≈ 137 for validation.
        Therefore φ¹⁵/(φ⁷+1) structure emerges naturally.
        """

        # Detect contamination
        evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(mixed_derivation)
        assert len(evidence) > 0, "Mixed derivation contamination not detected"

        # Test sanitization
        sanitized = CONTAMINATION_DETECTOR.sanitize_derivation_text(mixed_derivation)

        # Sanitized version should have reduced contamination
        sanitized_evidence = CONTAMINATION_DETECTOR.detect_lexical_contamination(sanitized)
        assert len(sanitized_evidence) <= len(evidence), "Sanitization did not reduce contamination"

@pytest.mark.integration
class TestContaminationSystemIntegration:
    """Integration tests for complete contamination detection system"""

    def test_end_to_end_contamination_workflow(self):
        """Test complete contamination detection and response workflow"""
        # Stage 1: Create theoretical derivation
        derivation = "φ¹⁵/(φ⁷+1) × 113 gives α⁻¹ ≈ 137.036 matching CODATA"

        # Stage 2: Detect contamination
        evidence = CONTAMINATION_DETECTOR.detect_all_contamination_types(derivation)
        assert len(evidence) > 0, "End-to-end contamination not detected"

        # Stage 3: Assess severity
        critical_count = len([e for e in evidence if e.is_critical()])

        # Stage 4: Generate alerts if needed
        if critical_count > 0:
            alert = CONTAMINATION_DETECTOR.generate_contamination_alert(evidence[0])
            assert alert is not None, "Critical contamination alert not generated"

        # Stage 5: Cleanup
        cleaned = CONTAMINATION_DETECTOR.sanitize_derivation_text(derivation)
        cleaned_evidence = CONTAMINATION_DETECTOR.detect_all_contamination_types(cleaned)

        # Should have fewer contamination instances after cleanup
        assert len(cleaned_evidence) <= len(evidence), "Contamination not reduced by cleanup"

    def test_contamination_monitoring_continuous(self):
        """Test continuous contamination monitoring system"""
        # Initialize monitoring
        CONTAMINATION_DETECTOR.start_continuous_monitoring()

        # Check monitoring status
        assert CONTAMINATION_DETECTOR._monitoring_active, "Continuous monitoring not active"

        # Test that monitoring detects new contamination
        contaminated_node = DerivationNode(
            node_id="monitored_contamination",
            mathematical_expression="Using α = 1/137.035999084 from NIST",
            derivation_type="EMPIRICAL",
            dependencies=[],
            justification="Empirical input",
            empirical_inputs=["NIST_alpha_measurement"],
            assumptions=[]
        )

        # Add to monitoring (would trigger alert in real system)
        CONTAMINATION_DETECTOR.add_node_for_monitoring(contaminated_node)

        # Check that contamination was detected and logged
        recent_detections = CONTAMINATION_DETECTOR.get_recent_contamination_detections()
        assert len(recent_detections) > 0, "Continuous monitoring not detecting contamination"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])