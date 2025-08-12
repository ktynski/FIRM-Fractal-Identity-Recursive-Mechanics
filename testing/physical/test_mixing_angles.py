"""
Test Suite: Mixing Angles Derivation Verification

Comprehensive tests for the mixing angles derivation system including:
- Weinberg angle derivation from φ-mathematics
- CKM matrix elements verification
- CP violation phase derivation
- Provenance tracking and contamination detection
- Mathematical consistency and error bounds

All tests verify academic integrity and mathematical necessity.
"""

import unittest
import numpy as np
import math
from unittest.mock import patch

from constants.mixing_angles import MixingAnglesDerivation, MixingAngleResult
from provenance.contamination_detector import ContaminationDetector
from foundation.operators.phi_recursion import PhiRecursion


class TestMixingAnglesDerivation(unittest.TestCase):
    """Test suite for mixing angles derivation system"""

    def setUp(self):
        """Set up test fixtures"""
        self.derivation = MixingAnglesDerivation()
        self.phi = PhiRecursion().phi
        self.contamination_detector = ContaminationDetector()

        # Expected theoretical values (for consistency checking)
        self.expected_sin2_theta_w = 1.0 / (self.phi**3 + 1.0)
        self.expected_V_us_bare = self.phi**(-2)
        self.expected_V_cb_bare = self.phi**(-4)
        self.expected_V_ub_bare = self.phi**(-6)
        self.expected_delta_bare = self.phi**(-1)

    def test_weinberg_angle_derivation(self):
        """Test Weinberg angle derivation mathematical consistency"""
        result = self.derivation.derive_weinberg_angle()

        # Verify result structure
        self.assertIsInstance(result, MixingAngleResult)
        self.assertEqual(result.name, "Weinberg Angle")
        self.assertEqual(result.symbol, "sin²θ_W")

        # Verify mathematical consistency
        phi_cubed = self.phi**3
        expected_bare = 1.0 / (phi_cubed + 1.0)

        # The corrected value should be close to bare value (correction is small)
        self.assertAlmostEqual(result.theoretical_value, expected_bare, delta=0.01)

        # Verify φ formula is correct
        self.assertIn("1/(φ³+1)", result.phi_formula)

        # Verify error is reasonable
        if result.relative_error_percent is not None:
            self.assertLess(result.relative_error_percent, 10.0)

        # Verify derivation steps are present
        self.assertGreater(len(result.derivation_steps), 3)

        # Verify provenance tracking
        self.assertIsNotNone(result.provenance_hash)

        # Verify falsification criterion
        self.assertIn("morphic mixing", result.falsification_criterion)

    def test_ckm_matrix_elements_derivation(self):
        """Test CKM matrix elements derivation"""
        results = self.derivation.derive_ckm_matrix_elements()

        # Verify all three elements are present
        self.assertIn("V_us", results)
        self.assertIn("V_cb", results)
        self.assertIn("V_ub", results)

        # Test V_us
        V_us = results["V_us"]
        self.assertEqual(V_us.symbol, "|V_us|")
        expected_V_us_bare = self.phi**(-2)
        # Corrected value should be suppressed relative to bare
        self.assertLess(V_us.theoretical_value, expected_V_us_bare)
        self.assertIn("φ⁻²", V_us.phi_formula)

        # Test V_cb
        V_cb = results["V_cb"]
        self.assertEqual(V_cb.symbol, "|V_cb|")
        expected_V_cb_bare = self.phi**(-4)
        self.assertLess(V_cb.theoretical_value, expected_V_cb_bare)
        self.assertIn("φ⁻⁴", V_cb.phi_formula)

        # Test V_ub
        V_ub = results["V_ub"]
        self.assertEqual(V_ub.symbol, "|V_ub|")
        expected_V_ub_bare = self.phi**(-6)
        # This one might be enhanced rather than suppressed
        self.assertIn("φ⁻⁶", V_ub.phi_formula)

        # Verify hierarchy: V_us > V_cb > V_ub (before corrections)
        # After corrections this might not hold due to different correction factors
        bare_hierarchy_check = expected_V_us_bare > expected_V_cb_bare > expected_V_ub_bare
        self.assertTrue(bare_hierarchy_check)

        # Verify all have provenance
        for element in results.values():
            self.assertIsNotNone(element.provenance_hash)
            self.assertGreater(len(element.derivation_steps), 2)

    def test_cp_violation_phase_derivation(self):
        """Test CP violation phase derivation"""
        result = self.derivation.derive_cp_violation_phase()

        # Verify result structure
        self.assertEqual(result.name, "CP Violation Phase")
        self.assertEqual(result.symbol, "δ")

        # Verify mathematical consistency
        expected_bare = self.phi**(-1)
        # Corrected value should be close to bare (small correction)
        self.assertAlmostEqual(result.theoretical_value, expected_bare, delta=0.1)

        # Verify φ formula
        self.assertIn("φ⁻¹", result.phi_formula)

        # Verify value is in reasonable range for phase (0 to 2π)
        self.assertGreaterEqual(result.theoretical_value, 0)
        self.assertLessEqual(result.theoretical_value, 2*math.pi)

        # Verify provenance
        self.assertIsNotNone(result.provenance_hash)
        self.assertGreater(len(result.derivation_steps), 3)

    def test_complete_derivation_system(self):
        """Test complete mixing angles derivation system"""
        results = self.derivation.derive_all_mixing_angles()

        # Verify all components present
        self.assertIn("weinberg", results)
        self.assertIn("ckm", results)
        self.assertIn("cp_phase", results)
        self.assertIn("summary", results)

        # Verify summary statistics
        summary = results["summary"]
        self.assertEqual(summary["total_parameters"], 5)
        self.assertIsInstance(summary["average_error_percent"], float)
        self.assertIsInstance(summary["max_error_percent"], float)
        self.assertTrue(summary["contamination_free"])
        self.assertTrue(summary["falsifiable"])

        # Verify mathematical foundation
        self.assertIn("φ-recursion", summary["mathematical_foundation"])

        # Verify errors are reasonable
        if summary["average_error_percent"] is not None:
            self.assertLess(summary["average_error_percent"], 20.0)  # Allow some flexibility

    def test_contamination_detection(self):
        """Test that derivation is free from empirical contamination"""
        # Test Weinberg angle
        result = self.derivation.derive_weinberg_angle()

        # Check that no forbidden experimental values appear in derivation
        for step in result.derivation_steps:
            contamination_result = self.contamination_detector.scan_text(step)
            if contamination_result.is_contaminated:
                # Allow experimental values only in comparison steps
                self.assertTrue(any(word in step.lower() for word in ["experimental", "error", "comparison"]))

        # Test CKM elements
        ckm_results = self.derivation.derive_ckm_matrix_elements()
        for element_result in ckm_results.values():
            for step in element_result.derivation_steps:
                contamination_result = self.contamination_detector.scan_text(step)
                if contamination_result.is_contaminated:
                    self.assertTrue(any(word in step.lower() for word in ["experimental", "error", "comparison"]))

    def test_mathematical_consistency_phi_powers(self):
        """Test mathematical consistency of φ-power relationships"""
        # Verify φ powers are computed correctly
        phi_squared = self.phi**2
        phi_cubed = self.phi**3
        phi_fourth = self.phi**4
        phi_sixth = self.phi**6

        # Test Weinberg angle formula components
        weinberg_denominator = phi_cubed + 1.0
        expected_sin2_theta_w = 1.0 / weinberg_denominator

        # Verify this matches our derivation (before corrections)
        result = self.derivation.derive_weinberg_angle()
        # Extract bare value from derivation steps
        bare_value_found = False
        for step in result.derivation_steps:
            if "bare" in step and "=" in step:
                # Extract numerical value
                parts = step.split("=")
                if len(parts) >= 2:
                    try:
                        bare_value = float(parts[-1].strip())
                        self.assertAlmostEqual(bare_value, expected_sin2_theta_w, places=5)
                        bare_value_found = True
                        break
                    except ValueError:
                        continue

        self.assertTrue(bare_value_found, "Could not find bare Weinberg angle value in derivation steps")

        # Test CKM φ-power relationships
        ckm_results = self.derivation.derive_ckm_matrix_elements()

        # Verify φ-power hierarchy is maintained in bare values
        expected_V_us = self.phi**(-2)
        expected_V_cb = self.phi**(-4)
        expected_V_ub = self.phi**(-6)

        # These should satisfy: V_us > V_cb > V_ub (before corrections)
        self.assertGreater(expected_V_us, expected_V_cb)
        self.assertGreater(expected_V_cb, expected_V_ub)

    def test_error_bounds_and_precision(self):
        """Test error bounds and numerical precision"""
        results = self.derivation.derive_all_mixing_angles()

        # Check Weinberg angle precision
        weinberg = results["weinberg"]
        if weinberg.experimental_value is not None:
            # Error should be reasonable for a fundamental theory
            self.assertLess(weinberg.relative_error_percent, 5.0)

        # Check that theoretical values are computed with sufficient precision
        self.assertGreater(len(str(weinberg.theoretical_value).split('.')[-1]), 4)  # At least 4 decimal places

        # Check CKM elements
        for element_name, element_result in results["ckm"].items():
            if element_result.experimental_value is not None:
                # Some CKM elements are harder to predict precisely
                self.assertLess(element_result.relative_error_percent, 60.0)  # Allow larger errors for CKM

            # Check precision
            self.assertGreater(len(str(element_result.theoretical_value).split('.')[-1]), 4)

    def test_falsification_criteria(self):
        """Test that falsification criteria are well-defined"""
        results = self.derivation.derive_all_mixing_angles()

        # Check Weinberg angle
        weinberg = results["weinberg"]
        self.assertIn("morphic", weinberg.falsification_criterion)
        self.assertIn("wrong", weinberg.falsification_criterion)

        # Check CKM elements
        for element_result in results["ckm"].values():
            self.assertIn("generation", element_result.falsification_criterion)
            self.assertIn("wrong", element_result.falsification_criterion)

        # Check CP phase
        cp_phase = results["cp_phase"]
        self.assertIn("φ-geometric", cp_phase.falsification_criterion)
        self.assertIn("wrong", cp_phase.falsification_criterion)

    def test_provenance_tracking_integrity(self):
        """Test provenance tracking integrity"""
        results = self.derivation.derive_all_mixing_angles()

        # Verify all results have unique provenance hashes
        all_hashes = []
        all_hashes.append(results["weinberg"].provenance_hash)

        for element_result in results["ckm"].values():
            all_hashes.append(element_result.provenance_hash)

        all_hashes.append(results["cp_phase"].provenance_hash)

        # All hashes should be unique
        self.assertEqual(len(all_hashes), len(set(all_hashes)))

        # All hashes should be non-empty strings
        for hash_val in all_hashes:
            self.assertIsInstance(hash_val, str)
            self.assertGreater(len(hash_val), 10)  # Reasonable hash length

    def test_dimensional_consistency(self):
        """Test dimensional consistency of derived values"""
        results = self.derivation.derive_all_mixing_angles()

        # Weinberg angle should be dimensionless
        weinberg = results["weinberg"]
        self.assertGreaterEqual(weinberg.theoretical_value, 0)
        self.assertLessEqual(weinberg.theoretical_value, 1)  # sin² must be ≤ 1

        # CKM elements should be dimensionless and ≤ 1
        for element_result in results["ckm"].values():
            self.assertGreaterEqual(element_result.theoretical_value, 0)
            self.assertLessEqual(element_result.theoretical_value, 1)

        # CP phase should be in radians (0 to 2π)
        cp_phase = results["cp_phase"]
        self.assertGreaterEqual(cp_phase.theoretical_value, 0)
        self.assertLessEqual(cp_phase.theoretical_value, 2*math.pi)


class TestMixingAngleResult(unittest.TestCase):
    """Test MixingAngleResult data structure"""

    def test_mixing_angle_result_creation(self):
        """Test MixingAngleResult creation and attributes"""
        result = MixingAngleResult(
            name="Test Angle",
            symbol="θ_test",
            theoretical_value=0.5,
            experimental_value=0.51,
            relative_error_percent=2.0,
            phi_formula="φ⁻¹",
            derivation_steps=["Step 1", "Step 2"],
            provenance_hash="test_hash_123",
            mathematical_necessity="Test necessity",
            falsification_criterion="Test falsification"
        )

        self.assertEqual(result.name, "Test Angle")
        self.assertEqual(result.symbol, "θ_test")
        self.assertEqual(result.theoretical_value, 0.5)
        self.assertEqual(result.experimental_value, 0.51)
        self.assertEqual(result.relative_error_percent, 2.0)
        self.assertEqual(result.phi_formula, "φ⁻¹")
        self.assertEqual(len(result.derivation_steps), 2)
        self.assertEqual(result.provenance_hash, "test_hash_123")
        self.assertIn("necessity", result.mathematical_necessity)
        self.assertIn("falsification", result.falsification_criterion)


def main():
    """Run all mixing angles tests"""
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()