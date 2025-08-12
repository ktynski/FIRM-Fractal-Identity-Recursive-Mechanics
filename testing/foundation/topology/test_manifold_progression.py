"""
Tests for the manifold progression theory module.

These tests verify the mathematical consistency and correctness of the
manifold progression theory, including the topological invariants,
phase transitions, and integration with cosmogenesis.
"""

import unittest
from typing import Dict, List, Optional

from foundation.topology.manifold_progression import (
    ManifoldType,
    CosmogenesisPhase,
    Manifold,
    ManifoldTransition,
    TopologicalInvariants,
    ManifoldProgression,
    MANIFOLD_PROGRESSION,
    get_manifold_for_cosmogenesis_stage,
    display_mathematical_theory
)

class TestManifoldProgression(unittest.TestCase):
    """Test suite for manifold progression theory."""

    def setUp(self):
        """Set up test environment."""
        self.manifold_progression = MANIFOLD_PROGRESSION

    def test_manifold_initialization(self):
        """Test that all manifolds are properly initialized."""
        manifolds = self.manifold_progression.get_all_manifolds()

        # Check we have all four manifold types
        self.assertEqual(len(manifolds), 4, "Should have 4 manifold types")

        # Check each manifold has the correct properties
        manifold_types = [m.type for m in manifolds]
        self.assertIn(ManifoldType.TORUS, manifold_types)
        self.assertIn(ManifoldType.MOBIUS_STRIP, manifold_types)
        self.assertIn(ManifoldType.KLEIN_BOTTLE, manifold_types)
        self.assertIn(ManifoldType.PHI_KLEIN, manifold_types)

        # Check Torus properties
        torus = next(m for m in manifolds if m.type == ManifoldType.TORUS)
        self.assertEqual(torus.invariants.fundamental_group, "ℤ × ℤ")
        self.assertEqual(torus.invariants.euler_characteristic, 0)
        self.assertTrue(torus.invariants.orientable)
        self.assertEqual(torus.invariants.genus, 1)
        self.assertEqual(torus.invariants.boundary_count, 0)
        self.assertFalse(torus.invariants.self_intersecting)

        # Check Klein Bottle properties
        klein = next(m for m in manifolds if m.type == ManifoldType.KLEIN_BOTTLE)
        self.assertIn("aba⁻¹b", klein.invariants.fundamental_group)
        self.assertEqual(klein.invariants.euler_characteristic, 0)
        self.assertFalse(klein.invariants.orientable)
        self.assertEqual(klein.invariants.boundary_count, 0)
        self.assertTrue(klein.invariants.self_intersecting)

    def test_transitions(self):
        """Test that transitions between manifolds are properly defined."""
        transitions = self.manifold_progression.get_all_transitions()

        # Check we have three transitions (Torus → Möbius → Klein → φ-Klein)
        self.assertEqual(len(transitions), 3, "Should have 3 transitions")

        # Check transition sequence
        self.assertEqual(transitions[0].source, ManifoldType.TORUS)
        self.assertEqual(transitions[0].target, ManifoldType.MOBIUS_STRIP)

        self.assertEqual(transitions[1].source, ManifoldType.MOBIUS_STRIP)
        self.assertEqual(transitions[1].target, ManifoldType.KLEIN_BOTTLE)

        self.assertEqual(transitions[2].source, ManifoldType.KLEIN_BOTTLE)
        self.assertEqual(transitions[2].target, ManifoldType.PHI_KLEIN)

        # Check phase transitions
        self.assertEqual(
            transitions[0].phase_transition,
            (CosmogenesisPhase.PHASE_1_2, CosmogenesisPhase.PHASE_3_4)
        )

        self.assertEqual(
            transitions[1].phase_transition,
            (CosmogenesisPhase.PHASE_3_4, CosmogenesisPhase.PHASE_5_6)
        )

        self.assertEqual(
            transitions[2].phase_transition,
            (CosmogenesisPhase.PHASE_5_6, CosmogenesisPhase.PHASE_7_8)
        )

    def test_phase_mapping(self):
        """Test that cosmogenesis phases are correctly mapped to manifolds."""
        # Check that each phase maps to the correct manifold
        self.assertEqual(
            self.manifold_progression.get_manifold_for_phase(CosmogenesisPhase.PHASE_1_2).type,
            ManifoldType.TORUS
        )

        self.assertEqual(
            self.manifold_progression.get_manifold_for_phase(CosmogenesisPhase.PHASE_3_4).type,
            ManifoldType.MOBIUS_STRIP
        )

        self.assertEqual(
            self.manifold_progression.get_manifold_for_phase(CosmogenesisPhase.PHASE_5_6).type,
            ManifoldType.KLEIN_BOTTLE
        )

        self.assertEqual(
            self.manifold_progression.get_manifold_for_phase(CosmogenesisPhase.PHASE_7_8).type,
            ManifoldType.PHI_KLEIN
        )

    def test_complexity_metric(self):
        """Test the complexity metric calculation."""
        # Check that complexity increases with each manifold
        torus_complexity = self.manifold_progression.calculate_complexity_metric(ManifoldType.TORUS)
        mobius_complexity = self.manifold_progression.calculate_complexity_metric(ManifoldType.MOBIUS_STRIP)
        klein_complexity = self.manifold_progression.calculate_complexity_metric(ManifoldType.KLEIN_BOTTLE)
        phi_klein_complexity = self.manifold_progression.calculate_complexity_metric(ManifoldType.PHI_KLEIN)

        self.assertLess(torus_complexity, mobius_complexity)
        self.assertLess(mobius_complexity, klein_complexity)
        self.assertEqual(phi_klein_complexity, float('inf'))

    def test_integration_with_cosmogenesis(self):
        """Test integration with cosmogenesis pipeline."""
        # Check mapping from cosmogenesis stages to manifolds
        self.assertEqual(
            self.manifold_progression.integrate_with_cosmogenesis("nothingness"),
            ManifoldType.TORUS
        )

        self.assertEqual(
            self.manifold_progression.integrate_with_cosmogenesis("grace_operator"),
            ManifoldType.MOBIUS_STRIP
        )

        self.assertEqual(
            self.manifold_progression.integrate_with_cosmogenesis("physical_constants"),
            ManifoldType.KLEIN_BOTTLE
        )

        self.assertEqual(
            self.manifold_progression.integrate_with_cosmogenesis("cmb_formation"),
            ManifoldType.PHI_KLEIN
        )

        # Check utility function
        self.assertEqual(
            get_manifold_for_cosmogenesis_stage("cosmic_evolution").type,
            ManifoldType.PHI_KLEIN
        )

    def test_displayMathematicalProgression(self):
        """Test the mathematical progression display data generation."""
        display_data = self.manifold_progression.displayMathematicalProgression()

        # Check required fields
        self.assertIn("title", display_data)
        self.assertIn("complexity_data", display_data)
        self.assertIn("visualization_data", display_data)
        self.assertIn("progression_data", display_data)
        self.assertIn("phi_value", display_data)

        # Check stages data
        self.assertEqual(len(display_data["progression_data"]["stages"]), 4)

        # Check transitions data
        self.assertEqual(len(display_data["progression_data"]["transitions"]), 3)

        # Check utility function
        theory_data = display_mathematical_theory()
        self.assertEqual(theory_data, display_data)

    def test_mathematical_consistency(self):
        """Test mathematical consistency verification."""
        consistency = self.manifold_progression.verify_mathematical_consistency()

        self.assertTrue(consistency["manifolds_defined"])
        self.assertTrue(consistency["transition_chain_complete"])
        self.assertTrue(consistency["phase_mapping_complete"])
        self.assertTrue(consistency["topological_invariants_valid"])
        self.assertTrue(consistency["mathematical_justifications_provided"])
        self.assertTrue(consistency["overall_consistency"])

    def test_mathematical_theory_description(self):
        """Test the mathematical theory description."""
        description = self.manifold_progression.get_mathematical_theory_description()

        self.assertIn("TORUS T² = S¹ × S¹", description)
        self.assertIn("MÖBIUS STRIP M", description)
        self.assertIn("KLEIN BOTTLE K", description)
        self.assertIn("φ-KLEIN RECURSIVE MANIFOLD", description)
        self.assertIn("COMPLEXITY PROGRESSION: 1 → 2 → 3 → ∞", description)


if __name__ == "__main__":
    unittest.main()
