#!/usr/bin/env python3
"""
FIRM Master Figure Generator: Complete Figure Regeneration System

This is the master script that can regenerate ALL figures in the FIRM system
from scratch with complete mathematical provenance and quality control.

Usage:
    python figures/MASTER_GENERATOR.py [--category CATEGORY] [--output-dir DIR]

Categories:
    - mathematical_foundations
    - physical_constants
    - cosmological_predictions
    - consciousness_integration
    - theory_validation
    - all (default)

Features:
    ✓ Complete provenance tracking
    ✓ Quality standardization (300+ DPI)
    ✓ Academic publication ready
    ✓ Error handling and recovery
    ✓ Progress reporting
    ✓ Parallel generation support
"""

import sys
import os
import argparse
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import json
import concurrent.futures
from dataclasses import dataclass

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import all figure generators
try:
    from figures.generators.constants_figure_generator import CONSTANTS_GENERATOR
    from figures.generators.cosmology_figure_generator import COSMOLOGY_GENERATOR
    from figures.generators.spacetime_emergence_generator import SPACETIME_GENERATOR
    from figures.generators.advanced_figure_generator import ADVANCED_FIGURE_GENERATOR
    from figures.generators.comprehensive_figure_generator import COMPREHENSIVE_FIGURE_GENERATOR
    from figures.generators.recursive_potential_figure import generate_recursive_potential_wells
    from figures.generators.mass_depth_figure import generate_mass_depth_cn
    from figures.generators.epsilon_components_figure import generate_epsilon_components_scan
    from figures.generators.epsilon_stability_figure import generate_epsilon_stability_scan
    from figures.generators.grace_operator_convergence_generator import generate_grace_operator_convergence_figure
    from figures.generators.phi_recursion_rate_generator import generate_phi_recursion_rate_figure
    from figures.generators.dark_energy_phi_generator import generate_dark_energy_phi_figure
    from figures.generators.dimensional_bridge_generator import generate_dimensional_bridge_figure
    from figures.generators.inflation_evolution_generator import generate_inflation_evolution_figure
    from figures.generators.manifold_progression_generator import generate_manifold_progression_diagram
    
    # Import the 4 new generators we created
    from figures.generators.gauge_couplings_generator import generate_gauge_couplings_theory
    from figures.generators.particle_mass_spectrum_generator import generate_particle_mass_spectrum_theory
    from figures.generators.sparc_rotation_curves_generator import generate_sparc_rotation_curves
    from figures.generators.consciousness_pnp_generator import generate_consciousness_pnp_correlation

    GENERATORS_LOADED = True
except ImportError as e:
    print(f"Warning: Some generators could not be imported: {e}")
    GENERATORS_LOADED = False

@dataclass
class GenerationTask:
    """Individual figure generation task"""
    name: str
    category: str
    generator_func: callable
    description: str
    priority: int = 1  # 1=high, 2=medium, 3=low

@dataclass
class GenerationResult:
    """Result of figure generation"""
    task: GenerationTask
    success: bool
    output_file: Optional[str] = None
    error: Optional[str] = None
    generation_time: Optional[float] = None
    provenance_hash: Optional[str] = None

class MasterFigureGenerator:
    """Master figure generation system with complete provenance and quality control"""

    def __init__(self, output_dir: str = "figures/outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Generation statistics
        self.stats = {
            "total_tasks": 0,
            "successful": 0,
            "failed": 0,
            "start_time": None,
            "end_time": None
        }

        # Define all generation tasks
        self.tasks = self._define_generation_tasks()

    def _define_generation_tasks(self) -> List[GenerationTask]:
        """Define all figure generation tasks"""
        tasks = []

        # Mathematical foundations (Priority 1 - Core theory)
        if GENERATORS_LOADED:
            tasks.extend([
                GenerationTask("phi_recursion_verification", "mathematical_foundations",
                             generate_phi_recursion_rate_figure,
                             "φ-recursion convergence verification", 1),
                GenerationTask("grace_operator_convergence", "mathematical_foundations",
                             generate_grace_operator_convergence_figure,
                             "Grace Operator fixed point convergence", 1),
                GenerationTask("recursive_potential_wells", "mathematical_foundations",
                             generate_recursive_potential_wells,
                             "Recursive potential V[φ] well structures", 1),
                GenerationTask("dimensional_bridge", "mathematical_foundations",
                             generate_dimensional_bridge_figure,
                             "Mathematical to physical unit bridge", 1),
                GenerationTask("spacetime_emergence", "mathematical_foundations",
                             SPACETIME_GENERATOR.generate_spacetime_metric_figure,
                             "Spacetime metric emergence from Grace Operator", 1),
                GenerationTask("manifold_progression", "mathematical_foundations",
                             generate_manifold_progression_diagram,
                             "Topological manifold progression", 2),
                GenerationTask("epsilon_components", "mathematical_foundations",
                             generate_epsilon_components_scan,
                             "ε-component analysis scan", 2),
                GenerationTask("epsilon_stability", "mathematical_foundations",
                             generate_epsilon_stability_scan,
                             "ε-stability analysis scan", 2),
            ])

            # Physical constants (Priority 1 - Testable predictions)
            tasks.extend([
                GenerationTask("alpha_inverse", "physical_constants",
                             CONSTANTS_GENERATOR.generate_alpha_inverse_figure,
                             "Fine structure constant α^(-1) derivation", 1),
                GenerationTask("constants_table", "physical_constants",
                             CONSTANTS_GENERATOR.generate_mass_ratios_table_figure,
                             "Physical constants derivation table", 1),
                GenerationTask("mass_depth", "physical_constants",
                             generate_mass_depth_cn,
                             "Particle mass form factors from recursive depth", 1),
            ])

            # Cosmological predictions (Priority 1 - Observable universe)
            tasks.extend([
                GenerationTask("bao_comparison", "cosmological_predictions",
                             COSMOLOGY_GENERATOR.generate_bao_comparison_figure,
                             "Baryon acoustic oscillations comparison", 1),
                GenerationTask("hubble_evolution", "cosmological_predictions",
                             COSMOLOGY_GENERATOR.generate_hubble_evolution_figure,
                             "Hubble parameter H(z) evolution", 1),
                GenerationTask("supernova_distances", "cosmological_predictions",
                             COSMOLOGY_GENERATOR.generate_supernova_distances_figure,
                             "Type Ia supernova distance-redshift relation", 1),
                GenerationTask("dark_energy_evolution", "cosmological_predictions",
                             generate_dark_energy_phi_figure,
                             "Dark energy φ-scaling evolution", 1),
                GenerationTask("inflation_timeline", "cosmological_predictions",
                             generate_inflation_evolution_figure,
                             "Cosmic inflation timeline", 2),
                GenerationTask("sparc_rotation_curves", "cosmological_predictions",
                             generate_sparc_rotation_curves,
                             "SPARC galaxy rotation curves vs FIRM predictions", 1),
            ])

            # Physical Constants (continued)
            tasks.extend([
                GenerationTask("gauge_couplings_theory", "physical_constants",
                             generate_gauge_couplings_theory,
                             "Gauge coupling constants emergence and unification", 1),
                GenerationTask("particle_mass_spectrum", "physical_constants",
                             generate_particle_mass_spectrum_theory,
                             "Complete Standard Model particle mass spectrum", 1),
            ])

            # Consciousness Integration (Priority 2 - Novel predictions)
            tasks.extend([
                GenerationTask("consciousness_pnp_correlation", "consciousness_integration",
                             generate_consciousness_pnp_correlation,
                             "P=NP consciousness correlation with φ-harmonics", 2),
            ])

        return tasks

    def generate_category(self, category: str, parallel: bool = True) -> List[GenerationResult]:
        """Generate all figures in a specific category"""
        category_tasks = [task for task in self.tasks if task.category == category]

        print(f"\n🎯 Generating {category} figures ({len(category_tasks)} tasks)")
        print("=" * 60)

        if parallel and len(category_tasks) > 1:
            return self._generate_parallel(category_tasks)
        else:
            return self._generate_sequential(category_tasks)

    def generate_all(self, parallel: bool = True) -> Dict[str, List[GenerationResult]]:
        """Generate all figures with complete provenance tracking"""
        self.stats["start_time"] = datetime.datetime.now()
        self.stats["total_tasks"] = len(self.tasks)

        print("🚀 FIRM Master Figure Generator: Complete Regeneration")
        print("=" * 60)
        print(f"Total tasks: {self.stats['total_tasks']}")
        print(f"Started: {self.stats['start_time']}")
        print(f"Output directory: {self.output_dir}")
        print()

        # Group tasks by category
        categories = {}
        for task in self.tasks:
            if task.category not in categories:
                categories[task.category] = []
            categories[task.category].append(task)

        # Generate by category with priority ordering
        results = {}
        category_order = ["mathematical_foundations", "physical_constants",
                         "cosmological_predictions", "consciousness_integration",
                         "theory_validation"]

        for category in category_order:
            if category in categories:
                results[category] = self.generate_category(category, parallel)

        # Final statistics
        self.stats["end_time"] = datetime.datetime.now()
        duration = (self.stats["end_time"] - self.stats["start_time"]).total_seconds()

        print("\n" + "=" * 60)
        print("📊 GENERATION COMPLETE")
        print("=" * 60)
        print(f"Total time: {duration:.1f} seconds")
        print(f"Successful: {self.stats['successful']}")
        print(f"Failed: {self.stats['failed']}")
        print(f"Success rate: {100*self.stats['successful']/self.stats['total_tasks']:.1f}%")
        print(f"Generated files in: {self.output_dir}")

        # Save generation report
        self._save_generation_report(results)

        return results

    def _generate_sequential(self, tasks: List[GenerationTask]) -> List[GenerationResult]:
        """Generate figures sequentially"""
        results = []

        for i, task in enumerate(sorted(tasks, key=lambda t: t.priority)):
            print(f"[{i+1}/{len(tasks)}] Generating {task.name}...")
            result = self._execute_task(task)
            results.append(result)

            if result.success:
                print(f"  ✅ Success: {result.output_file}")
                self.stats["successful"] += 1
            else:
                print(f"  ❌ Failed: {result.error}")
                self.stats["failed"] += 1

        return results

    def _generate_parallel(self, tasks: List[GenerationTask]) -> List[GenerationResult]:
        """Generate figures in parallel"""
        results = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            # Submit all tasks
            future_to_task = {
                executor.submit(self._execute_task, task): task
                for task in sorted(tasks, key=lambda t: t.priority)
            }

            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_task):
                task = future_to_task[future]
                try:
                    result = future.result()
                    results.append(result)

                    if result.success:
                        print(f"  ✅ {task.name}: {result.output_file}")
                        self.stats["successful"] += 1
                    else:
                        print(f"  ❌ {task.name}: {result.error}")
                        self.stats["failed"] += 1

                except Exception as e:
                    print(f"  ❌ {task.name}: Exception {e}")
                    self.stats["failed"] += 1

        return results

    def _execute_task(self, task: GenerationTask) -> GenerationResult:
        """Execute a single generation task"""
        import time
        start_time = time.time()

        try:
            # Call the generator function
            if hasattr(task.generator_func, '__self__'):
                # Method call
                result_data = task.generator_func()
            else:
                # Function call - may need output path
                try:
                    result_data = task.generator_func()
                except TypeError:
                    # Try with output path
                    output_path = self.output_dir / f"{task.name}.png"
                    result_data = task.generator_func(out_path=output_path)

            # Extract file path from result
            if isinstance(result_data, dict):
                output_file = result_data.get('file', None)
                provenance_hash = result_data.get('provenance_hash', None)
            else:
                output_file = str(result_data) if result_data else None
                provenance_hash = None

            generation_time = time.time() - start_time

            return GenerationResult(
                task=task,
                success=True,
                output_file=output_file,
                generation_time=generation_time,
                provenance_hash=provenance_hash
            )

        except Exception as e:
            generation_time = time.time() - start_time
            return GenerationResult(
                task=task,
                success=False,
                error=str(e),
                generation_time=generation_time
            )

    def _save_generation_report(self, results: Dict[str, List[GenerationResult]]):
        """Save comprehensive generation report"""
        report = {
            "generation_timestamp": self.stats["start_time"].isoformat(),
            "completion_timestamp": self.stats["end_time"].isoformat(),
            "duration_seconds": (self.stats["end_time"] - self.stats["start_time"]).total_seconds(),
            "statistics": self.stats,
            "output_directory": str(self.output_dir),
            "categories": {}
        }

        for category, category_results in results.items():
            report["categories"][category] = {
                "total_tasks": len(category_results),
                "successful": sum(1 for r in category_results if r.success),
                "failed": sum(1 for r in category_results if not r.success),
                "tasks": [
                    {
                        "name": r.task.name,
                        "description": r.task.description,
                        "success": r.success,
                        "output_file": r.output_file,
                        "error": r.error,
                        "generation_time": r.generation_time,
                        "provenance_hash": r.provenance_hash
                    }
                    for r in category_results
                ]
            }

        # Save report
        report_file = self.output_dir / "generation_report.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)

        print(f"\n📄 Generation report saved: {report_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="FIRM Master Figure Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Categories:
  mathematical_foundations    Core mathematical theory figures
  physical_constants         Derived physical constants
  cosmological_predictions   Observable universe predictions
  consciousness_integration  Consciousness-physics integration
  theory_validation         Theory comparison and validation
  all                       All categories (default)

Examples:
  python figures/MASTER_GENERATOR.py                           # Generate all figures
  python figures/MASTER_GENERATOR.py --category physical_constants
  python figures/MASTER_GENERATOR.py --output-dir custom_output/
        """
    )

    parser.add_argument('--category',
                       choices=['mathematical_foundations', 'physical_constants',
                               'cosmological_predictions', 'consciousness_integration',
                               'theory_validation', 'all'],
                       default='all',
                       help='Category of figures to generate')

    parser.add_argument('--output-dir',
                       default='figures/outputs',
                       help='Output directory for generated figures')

    parser.add_argument('--no-parallel',
                       action='store_true',
                       help='Disable parallel generation')

    args = parser.parse_args()

    # Create master generator
    generator = MasterFigureGenerator(output_dir=args.output_dir)

    if not GENERATORS_LOADED:
        print("❌ Critical: Figure generators could not be loaded!")
        print("   Please check import paths and dependencies.")
        return 1

    # Generate figures
    try:
        if args.category == 'all':
            results = generator.generate_all(parallel=not args.no_parallel)
        else:
            results = generator.generate_category(args.category, parallel=not args.no_parallel)

        # Return success/failure code
        if isinstance(results, dict):
            total_failed = generator.stats["failed"]
        else:
            total_failed = sum(1 for r in results if not r.success)
        return 0 if total_failed == 0 else 1

    except KeyboardInterrupt:
        print("\n⏸️  Generation interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Generation failed with error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
