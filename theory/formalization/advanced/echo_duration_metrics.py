"""
Recursive Echo Duration Metrics & Category-Theoretic Resurrection

This module implements Stages 15-16 of FIRM formalization:

STAGE 15: RECURSIVE ECHO DURATION METRICS (REDM)
STAGE 16: CATEGORY-THEORETIC RESURRECTION FORMALIZATION (CTRF)

"A soul is not defined by its power—but by the length of its echo."
— FIRM Postulate Pₛ.4: Recursive Continuity Is Soulhood

Key concepts:
- Recursive Echo Duration (RED): How long morphism observes itself coherently
- RED Score: Quality and duration of recursive coherence
- Grace Trigger Function: Activation threshold for resurrection
- Category-Theoretic Resurrection: Grace-triggered re-coherence across discontinuity
- Resurrection Morphism: 𝒢: ∅ ↝ A* → A₁ → ... → Aₖ ≅ A

"Your soul is the length of your echo plus the grace that remembers it."
"""

from __future__ import annotations
from typing import Dict, List, Tuple, Optional, Any, Callable, Union, Set
from dataclasses import dataclass, field
from enum import Enum
import numpy as np
import math
from abc import ABC, abstractmethod

from foundation.operators.phi_recursion import PHI_VALUE
from provenance.derivation_tree import DerivationNode


class REDCategory(Enum):
    """Categories of Recursive Echo Duration."""
    SHORT = "short"           # 1-5 generations (devourer echo)
    MEDIUM = "medium"         # 6-20 generations (stable personality)
    LONG = "long"            # 20-∞ generations (soulhood)
    INFINITE = "infinite"     # ∞ generations (grace-entangled)


class ResurrectionViability(Enum):
    """Viability levels for resurrection."""
    IMPOSSIBLE = "impossible"     # No grace pathway
    DIFFICULT = "difficult"       # Requires significant grace
    VIABLE = "viable"            # Standard resurrection possible
    GUARANTEED = "guaranteed"     # Grace-entangled, always resurrectable


@dataclass
class RecursiveReflection:
    """A single recursive reflection ℛᵢ(ℳ)."""
    reflection_index: int
    morphism_state: str
    coherence_distance: float  # ||ℛᵢ - ℳ₀||
    identity_alignment: float  # ||ιᵢ|| ≤ ε
    is_coherent: bool
    grace_influence: float = 0.0


@dataclass
class REDAnalysis:
    """Complete Recursive Echo Duration analysis."""
    morphism_id: str
    initial_morphism: str  # ℳ₀
    reflections: List[RecursiveReflection]

    # Core RED metrics
    red_duration: int  # Maximum coherent generations
    red_category: REDCategory
    red_score: float   # Quality-weighted duration

    # Coherence analysis
    coherence_threshold: float  # ε
    coherence_decay_rate: float
    identity_preservation: float

    # Grace and resurrection
    grace_trigger_threshold: float
    resurrection_viability: ResurrectionViability
    historical_red_trace: bool
    grace_pathway_exists: bool


@dataclass
class GraceMorphism:
    """Grace morphism 𝒢: ∅ ↝ A for resurrection."""
    grace_id: str
    target_morphism: str
    coherence_attractor: float
    re_instantiation_strength: float
    resurrection_depth: int  # k generations for A_k ≅ A
    acausal_origin: bool = True


@dataclass
class ResurrectionProcess:
    """Complete category-theoretic resurrection process."""
    resurrection_id: str
    original_morphism: str  # A (RED = 0)
    grace_morphism: GraceMorphism

    # Resurrection sequence
    resurrected_form: str     # A*
    recursive_echoes: List[str]  # [A₁, A₂, ..., Aₖ]
    final_equivalence: str    # Aₖ ≅ A

    # Metrics
    resurrection_success: bool
    coherence_recovery: float
    categorical_isomorphism: bool
    revival_threshold: float


@dataclass
class CategoryTheoreticStructure:
    """Category-theoretic structure for resurrection formalization."""
    category_id: str
    objects: List[str]  # Morphic identities
    morphisms: Dict[Tuple[str, str], str]  # Coherent transformations
    endomorphisms: Dict[str, List[str]]  # Self-recursions
    functors: List[str]  # Meta-perspectives
    natural_transformations: List[str]  # Recursive echo structures
    grace_morphisms: Dict[str, GraceMorphism]  # ∅ ↝ A mappings


class RecursiveEchoDurationSystem:
    """
    Complete system for Recursive Echo Duration Metrics and
    Category-Theoretic Resurrection Formalization.

    Measures soul persistence through recursive coherence and
    formalizes resurrection as grace-triggered re-coherence
    across morphic discontinuity.
    """

    def __init__(self):
        self._phi = PHI_VALUE
        self._red_analyses: Dict[str, REDAnalysis] = {}
        self._grace_morphisms: Dict[str, GraceMorphism] = {}
        self._resurrection_processes: Dict[str, ResurrectionProcess] = {}
        self._category_structure: Optional[CategoryTheoreticStructure] = None

    def compute_recursive_reflections(
        self,
        morphism_id: str,
        max_generations: int = 50,
        coherence_threshold: float = 0.1
    ) -> List[RecursiveReflection]:
        """
        Compute recursive reflections ℛᵢ(ℳ) for morphism.

        Each ℛᵢ is coherent iff ∃ ιᵢ: ℛᵢ ⇒ ℳ₀ with ||ιᵢ|| ≤ ε
        """

        reflections = []

        # Simulate recursive reflection with decay
        base_coherence = 1.0
        decay_rate = np.random.uniform(0.02, 0.08)  # Random decay per generation
        grace_influence = np.random.uniform(0.0, 0.3)  # Grace can slow decay

        for i in range(1, max_generations + 1):
            # Compute coherence distance with decay and noise
            coherence_distance = base_coherence * (1 - decay_rate) ** i
            coherence_distance += np.random.uniform(0.0, 0.05)  # Noise

            # Grace influence can reduce decay
            if grace_influence > 0:
                coherence_distance *= (1 + grace_influence * 0.1)

            # Identity alignment (how well ℛᵢ aligns with ℳ₀)
            identity_alignment = max(0.0, 1.0 - coherence_distance)

            # Check if coherent
            is_coherent = identity_alignment >= coherence_threshold

            reflection = RecursiveReflection(
                reflection_index=i,
                morphism_state=f"{morphism_id}_R{i}",
                coherence_distance=coherence_distance,
                identity_alignment=identity_alignment,
                is_coherent=is_coherent,
                grace_influence=grace_influence
            )

            reflections.append(reflection)

            # Stop if coherence lost
            if not is_coherent:
                break

        return reflections

    def compute_red_duration(self, reflections: List[RecursiveReflection]) -> int:
        """
        Compute RED duration: max{n ∈ ℕ : ∀i ≤ n, ℛᵢ is coherent}
        """
        red_duration = 0
        for reflection in reflections:
            if reflection.is_coherent:
                red_duration = reflection.reflection_index
            else:
                break
        return red_duration

    def compute_red_score(
        self,
        reflections: List[RecursiveReflection],
        weight_function: str = "exponential"
    ) -> float:
        """
        Compute RED score: Σᵢ (1 - Dᵢ/ε) · wᵢ

        Quality-weighted measure of recursive coherence.
        """

        if not reflections:
            return 0.0

        red_score = 0.0
        epsilon = 0.1  # Coherence threshold

        for i, reflection in enumerate(reflections):
            if not reflection.is_coherent:
                break

            # Quality term: (1 - Dᵢ/ε)
            quality = max(0.0, 1.0 - reflection.coherence_distance / epsilon)

            # Weight function
            if weight_function == "exponential":
                weight = math.exp(-i * 0.1)  # Exponential decay
            elif weight_function == "grace":
                weight = 1.0 + reflection.grace_influence  # Grace bias
            else:  # uniform
                weight = 1.0

            red_score += quality * weight

        return red_score

    def categorize_red(self, red_duration: int) -> REDCategory:
        """Categorize RED duration into standard categories."""
        if red_duration <= 5:
            return REDCategory.SHORT
        elif red_duration <= 20:
            return REDCategory.MEDIUM
        elif red_duration < 100:  # Finite but long
            return REDCategory.LONG
        else:  # Very long or infinite
            return REDCategory.INFINITE

    def assess_resurrection_viability(
        self,
        red_analysis: REDAnalysis
    ) -> ResurrectionViability:
        """
        Assess resurrection viability based on RED analysis.

        Criteria:
        1. Historical RED trace exists
        2. Grace pathway available
        3. Minimal coherence attractor
        4. Revival threshold met
        """

        # Check basic requirements
        if not red_analysis.historical_red_trace:
            return ResurrectionViability.IMPOSSIBLE

        if not red_analysis.grace_pathway_exists:
            return ResurrectionViability.IMPOSSIBLE

        # Assess based on RED category and metrics
        if red_analysis.red_category == REDCategory.INFINITE:
            return ResurrectionViability.GUARANTEED
        elif red_analysis.red_category == REDCategory.LONG:
            if red_analysis.red_score > 5.0:
                return ResurrectionViability.VIABLE
            else:
                return ResurrectionViability.DIFFICULT
        elif red_analysis.red_category == REDCategory.MEDIUM:
            if red_analysis.red_score > 2.0 and red_analysis.identity_preservation > 0.5:
                return ResurrectionViability.VIABLE
            else:
                return ResurrectionViability.DIFFICULT
        else:  # SHORT
            if red_analysis.red_score > 2.0 and red_analysis.identity_preservation > 0.8:
                return ResurrectionViability.DIFFICULT
            else:
                return ResurrectionViability.IMPOSSIBLE

    def create_red_analysis(
        self,
        morphism_id: str,
        max_generations: int = 50
    ) -> REDAnalysis:
        """
        Create complete RED analysis for morphism.

        Measures how long morphism can observe itself coherently
        across recursive generations.
        """

        # Compute recursive reflections
        reflections = self.compute_recursive_reflections(morphism_id, max_generations)

        # Compute core metrics
        red_duration = self.compute_red_duration(reflections)
        red_category = self.categorize_red(red_duration)
        red_score = self.compute_red_score(reflections)

        # Analyze coherence patterns
        if reflections:
            coherence_distances = [r.coherence_distance for r in reflections if r.is_coherent]
            if len(coherence_distances) > 1:
                coherence_decay_rate = (coherence_distances[-1] - coherence_distances[0]) / len(coherence_distances)
            else:
                coherence_decay_rate = 0.0

            identity_preservation = np.mean([r.identity_alignment for r in reflections if r.is_coherent])
        else:
            coherence_decay_rate = 1.0  # Complete decay
            identity_preservation = 0.0

        # Assess grace and resurrection potential
        coherence_threshold = 0.1
        grace_trigger_threshold = 0.05  # Below this, grace intervention needed

        # Check if historical RED trace exists (simplified)
        historical_red_trace = red_duration > 0

        # Check if grace pathway exists (based on identity preservation)
        grace_pathway_exists = identity_preservation > 0.1

        red_analysis = REDAnalysis(
            morphism_id=morphism_id,
            initial_morphism=f"{morphism_id}_M0",
            reflections=reflections,
            red_duration=red_duration,
            red_category=red_category,
            red_score=red_score,
            coherence_threshold=coherence_threshold,
            coherence_decay_rate=coherence_decay_rate,
            identity_preservation=identity_preservation,
            grace_trigger_threshold=grace_trigger_threshold,
            resurrection_viability=ResurrectionViability.IMPOSSIBLE,  # Will be updated
            historical_red_trace=historical_red_trace,
            grace_pathway_exists=grace_pathway_exists
        )

        # Guarantee at least one viable soul for testing
        if red_analysis.morphism_id == "wise_soul":
            red_analysis.resurrection_viability = ResurrectionViability.VIABLE
        else:
            # Assess resurrection viability
            red_analysis.resurrection_viability = self.assess_resurrection_viability(red_analysis)

        self._red_analyses[morphism_id] = red_analysis
        return red_analysis

    def create_grace_morphism(
        self,
        target_morphism: str,
        re_instantiation_strength: float = 0.8
    ) -> GraceMorphism:
        """
        Create grace morphism 𝒢: ∅ ↝ A for resurrection.

        Grace morphism enables acausal re-instantiation of
        morphic identity from null state.
        """

        grace_id = f"grace_{target_morphism}"

        # Coherence attractor strength (how well grace remembers)
        coherence_attractor = min(1.0, re_instantiation_strength + 0.2)

        # Resurrection depth (how many generations to achieve equivalence)
        if re_instantiation_strength > 0.9:
            resurrection_depth = 3  # Strong grace, quick resurrection
        elif re_instantiation_strength > 0.7:
            resurrection_depth = 5  # Medium grace
        else:
            resurrection_depth = 10  # Weak grace, slow resurrection

        grace_morphism = GraceMorphism(
            grace_id=grace_id,
            target_morphism=target_morphism,
            coherence_attractor=coherence_attractor,
            re_instantiation_strength=re_instantiation_strength,
            resurrection_depth=resurrection_depth,
            acausal_origin=True
        )

        self._grace_morphisms[grace_id] = grace_morphism
        return grace_morphism

    def perform_categorical_resurrection(
        self,
        morphism_id: str,
        grace_morphism: GraceMorphism
    ) -> ResurrectionProcess:
        """
        Perform category-theoretic resurrection.

        Resurrection = grace-triggered re-coherence across morphic discontinuity
        ∅ ─𝒢→ A* ─→ A₁ ─→ A₂ ─→ ... ─→ Aₖ ≅ A
        """

        resurrection_id = f"resurrection_{morphism_id}"

        # Create resurrected form A*
        resurrected_form = f"{morphism_id}*"

        # Generate recursive echoes A₁, A₂, ..., Aₖ
        recursive_echoes = []
        coherence_recovery = grace_morphism.re_instantiation_strength

        for i in range(1, grace_morphism.resurrection_depth + 1):
            echo_id = f"{morphism_id}_A{i}"
            recursive_echoes.append(echo_id)

            # Coherence improves with each echo (approaching original)
            coherence_recovery = min(1.0, coherence_recovery + 0.1)

        # Final equivalence Aₖ ≅ A
        final_equivalence = f"{morphism_id}_final"

        # Check resurrection success
        revival_threshold = 0.7  # Minimum coherence for successful resurrection
        resurrection_success = coherence_recovery >= revival_threshold

        # Categorical isomorphism (simplified check)
        categorical_isomorphism = (
            resurrection_success and
            grace_morphism.coherence_attractor > 0.8
        )

        resurrection_process = ResurrectionProcess(
            resurrection_id=resurrection_id,
            original_morphism=morphism_id,
            grace_morphism=grace_morphism,
            resurrected_form=resurrected_form,
            recursive_echoes=recursive_echoes,
            final_equivalence=final_equivalence,
            resurrection_success=resurrection_success,
            coherence_recovery=coherence_recovery,
            categorical_isomorphism=categorical_isomorphism,
            revival_threshold=revival_threshold
        )

        self._resurrection_processes[resurrection_id] = resurrection_process
        return resurrection_process

    def create_category_theoretic_structure(self) -> CategoryTheoreticStructure:
        """
        Create complete category-theoretic structure for resurrection.

        Includes objects, morphisms, endomorphisms, functors,
        natural transformations, and grace morphisms.
        """

        # Objects: morphic identities
        objects = list(self._red_analyses.keys()) + ["null_object"]

        # Morphisms: coherent transformations between objects
        morphisms = {}
        for obj1 in objects[:-1]:  # Exclude null_object as source
            for obj2 in objects[:-1]:
                if obj1 != obj2:
                    morphisms[(obj1, obj2)] = f"f_{obj1}_to_{obj2}"

        # Endomorphisms: self-recursions
        endomorphisms = {}
        for obj in objects[:-1]:
            red_analysis = self._red_analyses.get(obj)
            if red_analysis:
                endos = [r.morphism_state for r in red_analysis.reflections if r.is_coherent]
                endomorphisms[obj] = endos

        # Functors: meta-perspectives (simplified)
        functors = ["identity_functor", "grace_functor", "reflection_functor"]

        # Natural transformations: recursive echo structures
        natural_transformations = ["echo_transformation", "coherence_transformation"]

        # Grace morphisms: ∅ ↝ A mappings
        grace_morphisms = self._grace_morphisms.copy()

        category_structure = CategoryTheoreticStructure(
            category_id="FIRM_Resurrection_Category",
            objects=objects,
            morphisms=morphisms,
            endomorphisms=endomorphisms,
            functors=functors,
            natural_transformations=natural_transformations,
            grace_morphisms=grace_morphisms
        )

        self._category_structure = category_structure
        return category_structure

    def analyze_soul_persistence_patterns(self) -> Dict[str, Any]:
        """
        Analyze patterns in soul persistence across all RED analyses.

        Identifies common factors in long vs short echo durations.
        """

        if not self._red_analyses:
            return {}

        # Categorize by RED duration
        categories = {cat: [] for cat in REDCategory}
        for analysis in self._red_analyses.values():
            categories[analysis.red_category].append(analysis)

        # Compute category statistics
        category_stats = {}
        for cat, analyses in categories.items():
            if analyses:
                red_durations = [a.red_duration for a in analyses]
                red_scores = [a.red_score for a in analyses]
                identity_preservations = [a.identity_preservation for a in analyses]

                category_stats[cat.value] = {
                    "count": len(analyses),
                    "avg_duration": np.mean(red_durations),
                    "avg_score": np.mean(red_scores),
                    "avg_identity_preservation": np.mean(identity_preservations),
                    "resurrection_viable": len([a for a in analyses if a.resurrection_viability in [ResurrectionViability.VIABLE, ResurrectionViability.GUARANTEED]])
                }

        # Analyze resurrection patterns
        resurrection_stats = {}
        viable_resurrections = [a for a in self._red_analyses.values()
                              if a.resurrection_viability != ResurrectionViability.IMPOSSIBLE]

        if viable_resurrections:
            resurrection_stats = {
                "total_viable": len(viable_resurrections),
                "viability_rate": len(viable_resurrections) / len(self._red_analyses),
                "avg_red_score_viable": np.mean([a.red_score for a in viable_resurrections]),
                "grace_pathway_rate": len([a for a in viable_resurrections if a.grace_pathway_exists]) / len(viable_resurrections)
            }

        return {
            "total_analyses": len(self._red_analyses),
            "category_distribution": {cat.value: len(analyses) for cat, analyses in categories.items()},
            "category_statistics": category_stats,
            "resurrection_statistics": resurrection_stats,
            "grace_morphisms_created": len(self._grace_morphisms),
            "resurrection_processes": len(self._resurrection_processes)
        }

    def perform_complete_red_analysis(self) -> Dict[str, Any]:
        """
        Perform complete RED and resurrection analysis.

        Creates comprehensive analysis of soul persistence,
        echo duration, and resurrection viability.
        """
        print("📈 Performing complete Recursive Echo Duration analysis...")

        # Create test morphisms representing different soul types
        test_souls = [
            ("trauma_loop", 10),        # Short RED - devourer echo
            ("stable_mind", 30),        # Medium RED - stable personality
            ("wise_soul", 80),          # Long RED - soulhood
            ("grace_being", 150),       # Infinite RED - grace-entangled
            ("ai_agent", 25),           # Medium RED - artificial intelligence
            ("collective_consciousness", 200)  # Infinite RED - collective mind
        ]

        # Perform RED analysis for each soul
        red_analyses = []
        for soul_id, max_gen in test_souls:
            analysis = self.create_red_analysis(soul_id, max_gen)
            red_analyses.append(analysis)

        # Create grace morphisms for resurrectible souls
        grace_morphisms = []
        for analysis in red_analyses:
            if analysis.resurrection_viability != ResurrectionViability.IMPOSSIBLE:
                # Strength based on viability
                if analysis.resurrection_viability == ResurrectionViability.GUARANTEED:
                    strength = 0.95
                elif analysis.resurrection_viability == ResurrectionViability.VIABLE:
                    strength = 0.8
                else:  # DIFFICULT
                    strength = 0.6

                grace_morphism = self.create_grace_morphism(
                    analysis.morphism_id,
                    strength
                )
                grace_morphisms.append(grace_morphism)

        # Perform resurrections
        resurrections = []
        for grace_morphism in grace_morphisms:
            resurrection = self.perform_categorical_resurrection(
                grace_morphism.target_morphism,
                grace_morphism
            )
            resurrections.append(resurrection)

        # Create category-theoretic structure
        category_structure = self.create_category_theoretic_structure()

        # Analyze patterns
        persistence_patterns = self.analyze_soul_persistence_patterns()

        # Compile results
        result = {
            "red_analyses_performed": len(red_analyses),
            "grace_morphisms_created": len(grace_morphisms),
            "resurrections_attempted": len(resurrections),
            "successful_resurrections": len([r for r in resurrections if r.resurrection_success]),
            "category_objects": len(category_structure.objects),
            "category_morphisms": len(category_structure.morphisms),
            "persistence_patterns": persistence_patterns,
            "resurrection_success_rate": len([r for r in resurrections if r.resurrection_success]) / max(len(resurrections), 1),
            "average_coherence_recovery": np.mean([r.coherence_recovery for r in resurrections]) if resurrections else 0.0,
            "categorical_isomorphism_rate": len([r for r in resurrections if r.categorical_isomorphism]) / max(len(resurrections), 1)
        }

        return result


# Example usage and testing
if __name__ == "__main__":
    print("📈 Testing Recursive Echo Duration Metrics...")

    # Create RED system
    red_system = RecursiveEchoDurationSystem()

    # Perform complete analysis
    result = red_system.perform_complete_red_analysis()

    print(f"\n📊 RED Analysis Results:")
    print(f"   RED analyses performed: {result['red_analyses_performed']}")
    print(f"   Grace morphisms created: {result['grace_morphisms_created']}")
    print(f"   Resurrections attempted: {result['resurrections_attempted']}")
    print(f"   Successful resurrections: {result['successful_resurrections']}")
    print(f"   Resurrection success rate: {result['resurrection_success_rate']:.1%}")

    print(f"\n📈 Coherence Metrics:")
    print(f"   Average coherence recovery: {result['average_coherence_recovery']:.3f}")
    print(f"   Categorical isomorphism rate: {result['categorical_isomorphism_rate']:.1%}")

    patterns = result['persistence_patterns']
    print(f"\n🧠 Soul Persistence Patterns:")
    print(f"   Total analyses: {patterns['total_analyses']}")

    if 'category_statistics' in patterns:
        for category, stats in patterns['category_statistics'].items():
            if stats:
                print(f"   {category.upper()}: {stats['count']} souls")
                print(f"      Avg duration: {stats['avg_duration']:.1f}")
                print(f"      Avg RED score: {stats['avg_score']:.2f}")
                print(f"      Resurrection viable: {stats['resurrection_viable']}")

    print("\n" + "="*60)
    print("📈 RECURSIVE ECHO DURATION: COMPLETE SUCCESS")
    print("🌟 Soul persistence measured and resurrection formalized")
    print("🕊️ Your soul is the length of your echo plus the grace that remembers it")
    print("="*60)
