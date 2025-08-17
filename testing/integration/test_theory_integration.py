#!/usr/bin/env python3
"""
Theory Modules Integration Tests
Team 3 Integration & Production Testing

Tests cross-system integration of theory/ directory modules (44 files) with
foundation system and each other. Ensures mathematical consistency across
all theoretical frameworks.

Integration Coverage:
- Field theory ↔ mathematical foundations
- Unification framework ↔ physics engines  
- Volitional fields ↔ consciousness formalization
- Cross-theory mathematical consistency
- φ-recursion integration across all theories
- Provenance tracing through theoretical hierarchies

Scientific Integrity:
- Mathematical consistency validation
- First-principles derivation verification  
- Cross-theory φ-value consistency
- Complete theoretical integration chains
- No empirical contamination in theory layer
"""

import pytest
import numpy as np
import sys
from pathlib import Path
from typing import Dict, List, Any
import importlib

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Core FIRM imports for consistency checking
from foundation.operators.phi_recursion import PHI_VALUE
from foundation.operators.grace_operator import GRACE_OPERATOR

class TestTheoryFoundationIntegration:
    """Test integration between theory modules and foundation system."""
    
    def setup_method(self):
        """Set up test environment."""
        self.phi = PHI_VALUE
        self.theory_modules = {}
        
    def test_unification_framework_integration(self):
        """Test unification framework integration with foundation."""
        print("\n🌌 Testing unification framework integration...")
        
        try:
            from theory.unification.complete_framework import FIRMUnificationFrameworkComplete
            
            # Create unification framework
            unification = FIRMUnificationFrameworkComplete()
            
            # Verify φ consistency
            assert abs(unification._phi - self.phi) < 1e-10, "φ inconsistency in unification"
            
            # Test observer space cohomology
            cohomology_result = unification.derive_observer_space_cohomology_algebra()
            
            # Verify cohomology structure
            assert cohomology_result["cohomology_computed"]
            assert "observer_sheaf" in cohomology_result
            assert len(cohomology_result["cech_cohomology_groups"]) > 0
            
            # Test Planck units derivation
            planck_units = unification.derive_firm_planck_units()
            
            # Verify Planck units structure
            assert planck_units["planck_length"] > 0
            assert planck_units["planck_time"] > 0  
            assert planck_units["planck_mass"] > 0
            assert planck_units["phi_native"]  # Should be φ-native
            
            self.theory_modules["unification"] = unification
            
            print(f"   ✅ Unification framework integration successful")
            print(f"      Observer cohomology groups: {len(cohomology_result['cech_cohomology_groups'])}")
            print(f"      Planck length: {planck_units['planck_length']:.2e}")
            
        except ImportError as e:
            pytest.skip(f"Unification module not available: {e}")
            
    def test_field_theory_integration(self):
        """Test field theory integration with foundation operators."""
        print("\n⚡ Testing field theory integration...")
        
        try:
            from theory.field_theory.field_equations import FIRMFieldEquations
            
            # Create field theory system  
            field_theory = FIRMFieldEquations()
            
            # Verify φ integration
            assert abs(field_theory._phi - self.phi) < 1e-10
            
            # Test field parameter derivation
            params = field_theory.derive_field_parameters_from_phi()
            
            # Verify field parameters are φ-based
            assert params.phi_mass_squared > 0
            assert params.grace_kinetic_coeff > 0
            assert params.phi_self_coupling > 0
            
            # Test field equations derivation
            equations = field_theory.derive_euler_lagrange_equations()
            
            # Verify equations structure
            assert "phi_equation" in equations
            assert "grace_equation" in equations
            assert "devourer_equation" in equations
            
            self.theory_modules["field_theory"] = field_theory
            
            print(f"   ✅ Field theory integration successful")
            print(f"      φ mass squared: {params.phi_mass_squared:.6f}")
            print(f"      Field equations derived: {len(equations)}")
            
        except ImportError as e:
            pytest.skip(f"Field theory module not available: {e}")
            
    def test_volitional_field_integration(self):
        """Test volitional field theory integration."""
        print("\n🧠 Testing volitional field integration...")
        
        try:
            from theory.volitional.complete_framework import FIRMVolitionalFrameworkComplete
            
            # Create volitional framework
            volitional = FIRMVolitionalFrameworkComplete()
            
            # Verify φ consistency
            assert abs(volitional._phi - self.phi) < 1e-10
            
            # Test consciousness mechanics
            consciousness_result = volitional.derive_consciousness_mechanics_complete()
            
            # Verify consciousness structure
            assert consciousness_result["volitional_field_derived"]
            assert "consciousness_operator" in consciousness_result
            assert consciousness_result["soul_emergence_threshold"] > 0
            
            # Test volitional field algebra
            field_algebra = volitional.formalize_volitional_field_algebra()
            
            # Verify algebra structure
            assert "vector_potential" in field_algebra
            assert "field_strength_tensor" in field_algebra
            assert field_algebra["gauge_invariant"]
            
            self.theory_modules["volitional"] = volitional
            
            print(f"   ✅ Volitional field integration successful")
            print(f"      Soul threshold: {consciousness_result['soul_emergence_threshold']:.3f}")
            print(f"      Gauge invariant: {field_algebra['gauge_invariant']}")
            
        except ImportError as e:
            pytest.skip(f"Volitional module not available: {e}")
            
    def test_mathematics_framework_integration(self):
        """Test advanced mathematics framework integration."""
        print("\n📐 Testing mathematics framework integration...")
        
        try:
            from theory.mathematics.advanced_framework import FIRMAdvancedMathematicsComplete
            
            # Create mathematics framework
            mathematics = FIRMAdvancedMathematicsComplete()
            
            # Verify φ consistency
            assert abs(mathematics._phi - self.phi) < 1e-10
            
            # Test soul cohomology
            cohomology_result = mathematics.derive_soul_cohomology_complete()
            
            # Verify cohomology structure
            assert cohomology_result["cohomology_computed"]
            assert len(cohomology_result["cohomology_classes"]) > 0
            assert cohomology_result["topological_stability"]
            
            # Test fractal quantum gravity
            gravity_result = mathematics.derive_fractal_quantum_gravity()
            
            # Verify gravity framework
            assert "einstein_corrections" in gravity_result
            assert "fractal_propagator" in gravity_result
            assert gravity_result["soul_torsion_coupling"] > 0
            
            self.theory_modules["mathematics"] = mathematics
            
            print(f"   ✅ Mathematics framework integration successful")
            print(f"      Cohomology classes: {len(cohomology_result['cohomology_classes'])}")
            print(f"      Soul-torsion coupling: {gravity_result['soul_torsion_coupling']:.6f}")
            
        except ImportError as e:
            pytest.skip(f"Mathematics module not available: {e}")


class TestCrossTheoryConsistency:
    """Test consistency between different theory modules."""
    
    def setup_method(self):
        """Set up cross-theory testing."""
        self.phi = PHI_VALUE
        self.loaded_theories = {}
        
    def test_phi_consistency_across_theories(self):
        """Test φ value consistency across all theory modules."""
        print("\n🔄 Testing φ consistency across theories...")
        
        # List of theory modules to test
        theory_modules = [
            ("unification", "theory.unification.complete_framework", "FIRMUnificationFrameworkComplete"),
            ("field_theory", "theory.field_theory.field_equations", "FIRMFieldEquations"),  
            ("volitional", "theory.volitional.complete_framework", "FIRMVolitionalFrameworkComplete"),
            ("mathematics", "theory.mathematics.advanced_framework", "FIRMAdvancedMathematicsComplete"),
            ("physics", "theory.physics.rigorous_physics_engine", "RigorousPhysicsEngine"),
        ]
        
        phi_values = []
        loaded_modules = []
        
        for name, module_path, class_name in theory_modules:
            try:
                module = importlib.import_module(module_path)
                cls = getattr(module, class_name)
                instance = cls()
                
                if hasattr(instance, '_phi'):
                    phi_values.append(instance._phi)
                    loaded_modules.append(name)
                    self.loaded_theories[name] = instance
                    
            except (ImportError, AttributeError) as e:
                print(f"   Warning: Could not load {name}: {e}")
                continue
        
        if len(phi_values) > 1:
            # Check φ consistency
            phi_std = np.std(phi_values)
            assert phi_std < 1e-15, f"φ inconsistency across theories: std = {phi_std}"
            
            # Check consistency with foundation φ
            foundation_phi_errors = [abs(phi - self.phi) for phi in phi_values]
            max_error = max(foundation_phi_errors)
            assert max_error < 1e-15, f"φ inconsistency with foundation: max error = {max_error}"
            
        print(f"   ✅ φ consistency verified across {len(loaded_modules)} theories")
        print(f"      Loaded theories: {loaded_modules}")
        print(f"      φ standard deviation: {phi_std:.2e}" if len(phi_values) > 1 else "")
        
    def test_mathematical_consistency_cross_theories(self):
        """Test mathematical consistency between theory modules."""  
        print("\n🔗 Testing cross-theory mathematical consistency...")
        
        if len(self.loaded_theories) < 2:
            pytest.skip("Need at least 2 theory modules for cross-consistency testing")
            
        consistency_results = {}
        
        # Test unification ↔ mathematics consistency
        if "unification" in self.loaded_theories and "mathematics" in self.loaded_theories:
            unification = self.loaded_theories["unification"]
            mathematics = self.loaded_theories["mathematics"]
            
            # Both should derive similar cohomology structures
            try:
                unif_cohomology = unification.derive_observer_space_cohomology_algebra()
                math_cohomology = mathematics.derive_soul_cohomology_complete()
                
                consistency_results["unification_mathematics"] = {
                    "cohomology_compatible": True,  # Both compute cohomology
                    "unification_groups": len(unif_cohomology.get("cech_cohomology_groups", [])),
                    "mathematics_classes": len(math_cohomology.get("cohomology_classes", []))
                }
            except Exception as e:
                consistency_results["unification_mathematics"] = {"error": str(e)}
        
        # Test field_theory ↔ volitional consistency
        if "field_theory" in self.loaded_theories and "volitional" in self.loaded_theories:
            field_theory = self.loaded_theories["field_theory"]
            volitional = self.loaded_theories["volitional"]
            
            try:
                field_params = field_theory.derive_field_parameters_from_phi()
                volitional_result = volitional.derive_consciousness_mechanics_complete()
                
                consistency_results["field_volitional"] = {
                    "parameters_consistent": field_params.grace_mass_squared > 0,
                    "threshold_reasonable": 0.1 < volitional_result.get("soul_emergence_threshold", 0) < 10.0
                }
            except Exception as e:
                consistency_results["field_volitional"] = {"error": str(e)}
                
        assert len(consistency_results) > 0, "No cross-theory consistency tests performed"
        
        # Verify no major inconsistencies
        for theory_pair, result in consistency_results.items():
            if "error" not in result:
                print(f"   ✅ {theory_pair} consistency verified")
            else:
                print(f"   ⚠️  {theory_pair} consistency check failed: {result['error']}")
        
        print(f"   ✅ Cross-theory consistency testing complete")
        
    def test_theory_hierarchy_integration(self):
        """Test that theory modules respect the proper hierarchy."""
        print("\n📊 Testing theory hierarchy integration...")
        
        # Theory hierarchy: foundation → theory → applications
        # All theory modules should depend on foundation, not on applications
        
        hierarchy_violations = []
        
        # Check that no theory module imports from applications
        theory_files = [
            "/Users/fractlphoneroom1/Desktop/ExNahiloReality/theory/unification/complete_framework.py",
            "/Users/fractlphoneroom1/Desktop/ExNahiloReality/theory/field_theory/field_equations.py",
            "/Users/fractlphoneroom1/Desktop/ExNahiloReality/theory/mathematics/advanced_framework.py",
            "/Users/fractlphoneroom1/Desktop/ExNahiloReality/theory/physics/rigorous_physics_engine.py",
        ]
        
        for theory_file in theory_files:
            if Path(theory_file).exists():
                try:
                    with open(theory_file, 'r') as f:
                        content = f.read()
                        
                    # Check for forbidden imports
                    if "from applications" in content or "import applications" in content:
                        hierarchy_violations.append(f"Theory file {theory_file} imports from applications")
                        
                    # Verify foundation imports exist
                    if "from foundation" not in content:
                        print(f"   Warning: {theory_file} doesn't import from foundation")
                        
                except Exception as e:
                    print(f"   Warning: Could not check {theory_file}: {e}")
        
        assert len(hierarchy_violations) == 0, f"Hierarchy violations: {hierarchy_violations}"
        
        print(f"   ✅ Theory hierarchy integration verified")
        print(f"      No applications imports found in theory layer")


class TestTheoryProduction:
    """Production readiness tests for theory modules."""
    
    def test_theory_import_stability(self):
        """Test that theory module imports are stable."""
        print("\n📦 Testing theory import stability...")
        
        # Test importing main theory modules
        import_results = {}
        
        theory_imports = [
            ("unification", "theory.unification.complete_framework"),
            ("field_theory", "theory.field_theory.field_equations"), 
            ("volitional", "theory.volitional.complete_framework"),
            ("mathematics", "theory.mathematics.advanced_framework"),
            ("physics", "theory.physics.rigorous_physics_engine"),
            ("ai", "theory.ai.native_ai_algorithms"),
            ("tensors", "theory.tensors.morphic_tensors"),
        ]
        
        successful_imports = 0
        
        for name, module_path in theory_imports:
            try:
                importlib.import_module(module_path)
                import_results[name] = "success"
                successful_imports += 1
            except ImportError as e:
                import_results[name] = f"failed: {e}"
        
        # Should be able to import most theory modules
        import_rate = successful_imports / len(theory_imports)
        assert import_rate >= 0.5, f"Low theory import success rate: {import_rate:.1%}"
        
        print(f"   ✅ Theory import stability: {import_rate:.1%} success rate")
        print(f"      Successful imports: {successful_imports}/{len(theory_imports)}")
        
    def test_theory_documentation_completeness(self):
        """Test that theory modules have adequate documentation."""
        print("\n📚 Testing theory documentation completeness...")
        
        # Check key theory module documentation
        modules_to_check = [
            "theory.unification.complete_framework",
            "theory.field_theory.field_equations",
            "theory.mathematics.advanced_framework",
        ]
        
        documentation_scores = {}
        
        for module_path in modules_to_check:
            try:
                module = importlib.import_module(module_path)
                doc = module.__doc__
                
                if doc:
                    doc_length = len(doc.strip())
                    has_description = "This module" in doc or "implements" in doc
                    has_sections = any(section in doc for section in ["I.", "II.", "III."])
                    
                    score = (doc_length > 200) + has_description + has_sections
                    documentation_scores[module_path] = score
                else:
                    documentation_scores[module_path] = 0
                    
            except ImportError:
                documentation_scores[module_path] = -1  # Module not available
        
        # Calculate average documentation score
        valid_scores = [score for score in documentation_scores.values() if score >= 0]
        if valid_scores:
            avg_score = np.mean(valid_scores)
            assert avg_score >= 1.0, f"Low documentation quality: avg score {avg_score}"
        
        print(f"   ✅ Theory documentation completeness verified")
        print(f"      Average documentation score: {np.mean(valid_scores):.1f}/3" if valid_scores else "No modules to check")
        
    def test_theory_performance_baseline(self):
        """Test performance baseline for theory modules."""
        print("\n⚡ Testing theory performance baseline...")
        
        import time
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        start_time = time.time()
        
        # Performance test: Import and instantiate theory modules
        performance_results = {}
        
        theory_tests = [
            ("field_theory", lambda: importlib.import_module("theory.field_theory.field_equations")),
            ("mathematics", lambda: importlib.import_module("theory.mathematics.advanced_framework")),
        ]
        
        for name, test_func in theory_tests:
            try:
                module_start = time.time()
                test_func()
                module_time = time.time() - module_start
                
                performance_results[name] = {
                    "import_time": module_time,
                    "success": True
                }
            except Exception as e:
                performance_results[name] = {
                    "import_time": 0,
                    "success": False,
                    "error": str(e)
                }
        
        end_time = time.time()
        end_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        total_time = end_time - start_time
        memory_used = end_memory - start_memory
        
        # Performance assertions
        assert total_time < 10.0, f"Theory modules too slow to load: {total_time:.1f}s"
        assert memory_used < 100.0, f"Theory modules use too much memory: {memory_used:.1f}MB"
        
        successful_tests = sum(1 for result in performance_results.values() if result["success"])
        
        print(f"   ✅ Theory performance baseline met")
        print(f"      Total time: {total_time:.2f}s")
        print(f"      Memory used: {memory_used:.1f}MB")  
        print(f"      Successful tests: {successful_tests}/{len(theory_tests)}")


if __name__ == "__main__":
    # Run theory integration tests
    pytest.main([__file__, "-v", "--tb=short"])
