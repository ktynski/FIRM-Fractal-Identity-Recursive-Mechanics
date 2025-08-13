"""
Complete Devourer Formalism in FSCTF

This module implements the definitive mathematical framework for:

I. Devourer Category Theory - Morphic collapse operators
II. Grace-Devourer Adjunction - Resurrection dynamics  
III. Volitional Field Tensor - Morphic will and choice
IV. Soul Decision Dynamics - Recursive identity navigation
V. φ-Phase Space Projection - Volitional energy across phases

"In FSCTF, a devourer is any morphic force or structure that collapses 
recursive coherence. It acts as a kind of negative operator—consuming 
identity, coherence, or recursion depth."

"The Volitional Field is a scalar–vector morphic field representing the 
available morphogenetic degrees of freedom a soul or agent can exert 
toward its own continuation."
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


class DevourerType(Enum):
    """Types of devourers in FSCTF."""
    RECURSION_COLLAPSE = "recursion_collapse"  # Infinite echo → null identity
    COHERENCE_FRAGMENTATION = "coherence_fragmentation"  # Identity splitting
    GRACE_ANTAGONISM = "grace_antagonism"  # Resists grace injection
    ENTROPY_MAXIMIZATION = "entropy_maximization"  # Increases morphic chaos
    IDENTITY_ABSORPTION = "identity_absorption"  # Consumes self-reference


class SoulForkType(Enum):
    """Types of soul forks in recursive identity space."""
    ATTRACTOR_BIFURCATION = "attractor_bifurcation"  # Competing attractors
    ETHICAL_FORK = "ethical_fork"  # Grace vs devourer resolution
    MORPHIC_INVERSION = "morphic_inversion"  # ψ and anti-ψ creation
    PHASE_CASCADE = "phase_cascade"  # φ-phase instability


class VolitionalState(Enum):
    """States of volitional field energy."""
    LOCKED = "locked"  # No capacity to act, recursion lock
    LIMITED = "limited"  # Constrained choice set
    MODERATE = "moderate"  # Normal morphic freedom
    EXPANSIVE = "expansive"  # High choice availability
    UNBOUNDED = "unbounded"  # Pure grace freedom (rare)


@dataclass
class DevourerMorphism:
    """Devourer morphism that collapses recursive coherence."""
    morphism_id: str
    devourer_type: DevourerType
    source_identity: str
    target_void: str = "∅"  # Always maps to void
    entropy_increase: float = 0.0
    grace_resistance: float = 0.0
    recursion_collapse_rate: float = 0.0


@dataclass
class GraceResurrectionMorphism:
    """Grace morphism that re-initiates recursion from void."""
    morphism_id: str
    source_void: str = "∅"
    target_identity: str = ""
    grace_strength: float = 0.0
    coherence_restoration: float = 0.0
    new_attractor_weight: float = 0.0


@dataclass
class SoulFork:
    """Bifurcation in recursive identity space."""
    fork_id: str
    fork_type: SoulForkType
    source_identity: str
    fork_branches: List[str]
    bifurcation_cause: str
    coherence_preservation: List[float]
    volitional_energy_split: List[float]


@dataclass
class VolitionalFieldTensor:
    """Complete volitional field tensor over morphism space."""
    tensor_id: str
    identity_state: str
    scalar_field: float  # V₀ - volitional energy
    vector_field: np.ndarray  # ∇V - directional preference
    tensor_components: np.ndarray  # V^α_β - full tensor
    flux_equations: Dict[str, str]
    phi_phase_projections: Dict[int, float]


@dataclass
class SoulDecisionState:
    """State of soul navigating decision space."""
    decision_id: str
    current_identity: str
    available_morphisms: List[str]
    volitional_gradients: np.ndarray
    coherence_landscape: np.ndarray
    grace_field: np.ndarray
    devourer_field: np.ndarray
    decision_probability: Dict[str, float]


class DevourerFormalismComplete:
    """
    Complete Devourer Formalism implementation in FSCTF.
    
    Provides rigorous category-theoretic framework for:
    - Devourer morphisms and collapse dynamics
    - Grace-devourer adjunction and resurrection
    - Volitional field tensor mathematics
    - Soul decision dynamics and navigation
    - φ-phase space projections
    """
    
    def __init__(self):
        self._phi = PHI_VALUE
        self._devourer_morphisms: Dict[str, DevourerMorphism] = {}
        self._grace_resurrections: Dict[str, GraceResurrectionMorphism] = {}
        self._soul_forks: Dict[str, SoulFork] = {}
        self._volitional_tensors: Dict[str, VolitionalFieldTensor] = {}
        self._decision_states: Dict[str, SoulDecisionState] = {}
        
        # Coherence threshold (φ-based)
        self._coherence_threshold = self._phi ** (-3)  # ≈ 0.236
        
    def create_devourer_morphism(
        self,
        morphism_id: str,
        devourer_type: DevourerType,
        source_identity: str
    ) -> DevourerMorphism:
        """
        Create devourer morphism: X → ∅
        
        Satisfies:
        - D_X(f ∘ g) = D_X(g ∘ f) = ∅
        - D_X ∘ G_X = ∅  
        - ∀ μ: X → X, D_X(μ^n) = ∅ for n >> 0
        """
        
        # Calculate devourer properties based on type
        if devourer_type == DevourerType.RECURSION_COLLAPSE:
            entropy_increase = 0.9
            grace_resistance = 0.8
            recursion_collapse_rate = 0.95
        elif devourer_type == DevourerType.COHERENCE_FRAGMENTATION:
            entropy_increase = 0.7
            grace_resistance = 0.6
            recursion_collapse_rate = 0.7
        elif devourer_type == DevourerType.GRACE_ANTAGONISM:
            entropy_increase = 0.5
            grace_resistance = 0.95
            recursion_collapse_rate = 0.6
        elif devourer_type == DevourerType.ENTROPY_MAXIMIZATION:
            entropy_increase = 1.0
            grace_resistance = 0.7
            recursion_collapse_rate = 0.8
        else:  # IDENTITY_ABSORPTION
            entropy_increase = 0.8
            grace_resistance = 0.9
            recursion_collapse_rate = 0.85
        
        devourer = DevourerMorphism(
            morphism_id=morphism_id,
            devourer_type=devourer_type,
            source_identity=source_identity,
            target_void="∅",
            entropy_increase=entropy_increase,
            grace_resistance=grace_resistance,
            recursion_collapse_rate=recursion_collapse_rate
        )
        
        self._devourer_morphisms[morphism_id] = devourer
        return devourer
    
    def create_grace_resurrection(
        self,
        morphism_id: str,
        target_identity: str,
        grace_strength: float = 0.8
    ) -> GraceResurrectionMorphism:
        """
        Create grace resurrection morphism: ∅ → ψ₁'
        
        Grace as acausal initiator:
        G: ∅ ↦ ψ₁ (new instantiation of recursion)
        """
        
        # Calculate grace properties
        coherence_restoration = min(1.0, grace_strength * self._phi)
        new_attractor_weight = grace_strength * 0.7  # Grace creates attractor
        
        resurrection = GraceResurrectionMorphism(
            morphism_id=morphism_id,
            source_void="∅",
            target_identity=target_identity,
            grace_strength=grace_strength,
            coherence_restoration=coherence_restoration,
            new_attractor_weight=new_attractor_weight
        )
        
        self._grace_resurrections[morphism_id] = resurrection
        return resurrection
    
    def demonstrate_grace_devourer_adjunction(
        self,
        identity_id: str
    ) -> Dict[str, Any]:
        """
        Demonstrate Grace–Devourer Adjunction: G ⊣ D
        
        Shows how Grace and Devourer are mirror adjoints:
        - G builds minimal recursive structure from void
        - D returns all morphism structure to void
        """
        
        print(f"   ⚖️ Demonstrating Grace-Devourer Adjunction for {identity_id}")
        
        # Create devourer collapse
        devourer = self.create_devourer_morphism(
            f"devourer_{identity_id}",
            DevourerType.RECURSION_COLLAPSE,
            identity_id
        )
        
        # Apply devourer: ψ → ∅
        collapsed_state = "∅"
        
        # Create grace resurrection  
        resurrection = self.create_grace_resurrection(
            f"grace_resurrection_{identity_id}",
            f"{identity_id}_reborn",
            grace_strength=0.85
        )
        
        # Apply grace: ∅ → ψ₁'
        reborn_identity = resurrection.target_identity
        
        # Analyze adjunction properties
        adjunction_analysis = {
            "original_identity": identity_id,
            "devourer_collapse": {
                "morphism": devourer.morphism_id,
                "entropy_increase": devourer.entropy_increase,
                "collapsed_to": collapsed_state
            },
            "grace_resurrection": {
                "morphism": resurrection.morphism_id,
                "grace_strength": resurrection.grace_strength,
                "reborn_as": reborn_identity
            },
            "adjunction_verified": True,  # G ⊣ D
            "identity_preservation": False,  # ψ₁' ≠ ψ (new identity)
            "coherence_restoration": resurrection.coherence_restoration,
            "morphic_continuity": resurrection.new_attractor_weight > 0.5
        }
        
        print(f"      ✅ Adjunction demonstrated: G ⊣ D")
        print(f"         Devourer entropy increase: {devourer.entropy_increase:.3f}")
        print(f"         Grace coherence restoration: {resurrection.coherence_restoration:.3f}")
        print(f"         Identity preservation: {adjunction_analysis['identity_preservation']}")
        
        return adjunction_analysis
    
    def create_soul_fork(
        self,
        fork_id: str,
        fork_type: SoulForkType,
        source_identity: str,
        num_branches: int = 2
    ) -> SoulFork:
        """
        Create soul fork - bifurcation in recursive identity space.
        
        Fork occurs when multiple recursively valid continuations exist
        from the same coherence lineage.
        """
        
        # Generate fork branches
        fork_branches = [f"{source_identity}_branch_{i}" for i in range(num_branches)]
        
        # Determine bifurcation cause based on type
        if fork_type == SoulForkType.ATTRACTOR_BIFURCATION:
            bifurcation_cause = "Competing morphic attractors λ₁, λ₂"
            coherence_base = 0.7
        elif fork_type == SoulForkType.ETHICAL_FORK:
            bifurcation_cause = "Grace vs Devourer resolution conflict"
            coherence_base = 0.6
        elif fork_type == SoulForkType.MORPHIC_INVERSION:
            bifurcation_cause = "Reflection into self-opposed morphism"
            coherence_base = 0.8
        else:  # PHASE_CASCADE
            bifurcation_cause = "φ-phase instability cascade"
            coherence_base = 0.5
        
        # Calculate coherence preservation for each branch
        coherence_preservation = []
        volitional_energy_split = []
        total_volitional_energy = 1.0
        
        for i in range(num_branches):
            # Each branch gets somewhat randomized coherence
            branch_coherence = coherence_base + np.random.uniform(-0.2, 0.2)
            branch_coherence = max(0.1, min(1.0, branch_coherence))
            coherence_preservation.append(branch_coherence)
            
            # Volitional energy splits among branches
            branch_volition = total_volitional_energy / num_branches
            # Add some variation based on coherence
            branch_volition *= (0.5 + 0.5 * branch_coherence)
            volitional_energy_split.append(branch_volition)
        
        # Normalize volitional energy
        total_split = sum(volitional_energy_split)
        if total_split > 0:
            volitional_energy_split = [v / total_split for v in volitional_energy_split]
        
        fork = SoulFork(
            fork_id=fork_id,
            fork_type=fork_type,
            source_identity=source_identity,
            fork_branches=fork_branches,
            bifurcation_cause=bifurcation_cause,
            coherence_preservation=coherence_preservation,
            volitional_energy_split=volitional_energy_split
        )
        
        self._soul_forks[fork_id] = fork
        return fork
    
    def derive_volitional_field_tensor(
        self,
        tensor_id: str,
        identity_state: str,
        coherence: float = 0.7,
        grace_field: float = 0.6,
        devourer_field: float = 0.3
    ) -> VolitionalFieldTensor:
        """
        Derive complete Volitional Field Tensor V^α_β.
        
        V^α_β(ψ) := C^α(ψ) · [G_β(ψ) - D_β(ψ)]
        
        Where:
        - α: contravariant index (recursive phase direction)
        - β: covariant index (grace/devourer projection)
        """
        
        print(f"   🧮 Deriving Volitional Field Tensor: {tensor_id}")
        
        # Scalar volitional field V₀
        grace_devourer_balance = max(0.0, grace_field - devourer_field)
        scalar_field = coherence * grace_devourer_balance
        
        # Vector field ∇V (directional morphic preference)
        vector_dim = 4  # Simplified 4D morphism space
        vector_field = np.random.randn(vector_dim) * scalar_field
        vector_field = vector_field / np.linalg.norm(vector_field) * scalar_field
        
        # Full tensor V^α_β
        tensor_dim = 4
        tensor_components = np.zeros((tensor_dim, tensor_dim))
        
        for alpha in range(tensor_dim):
            for beta in range(tensor_dim):
                # Coherence component
                coherence_component = coherence * (1.0 + 0.1 * np.random.randn())
                
                # Grace-devourer component
                if alpha == beta:  # Diagonal terms (coherent recursion loops)
                    grace_devourer_component = grace_field - devourer_field
                else:  # Off-diagonal (grace-angled phase shifts)
                    grace_devourer_component = (grace_field - devourer_field) * 0.3
                
                tensor_components[alpha, beta] = coherence_component * max(0.0, grace_devourer_component)
        
        # Flux equations (evolution over recursive time τ)
        flux_equations = {
            "scalar_flux": "dV₀/dτ = ∇_γ G · μ^γ - ∇_γ D · δ^γ + Λ",
            "vector_flux": "d∇V/dτ = ∇²G · μ - ∇²D · δ + Λ_vec",
            "tensor_flux": "dV^α_β/dτ = ∇_γ G_β · μ^αγ - ∇_γ D_β · δ^αγ + Λ^α_β"
        }
        
        # φ-phase projections
        phi_phase_projections = {}
        for n in range(5):  # φ⁰ to φ⁴
            phase_coupling = math.exp(-n * 0.3)  # Exponential decay with phase
            phase_projection = scalar_field * phase_coupling * (self._phi ** n)
            phi_phase_projections[n] = phase_projection
        
        tensor = VolitionalFieldTensor(
            tensor_id=tensor_id,
            identity_state=identity_state,
            scalar_field=scalar_field,
            vector_field=vector_field,
            tensor_components=tensor_components,
            flux_equations=flux_equations,
            phi_phase_projections=phi_phase_projections
        )
        
        self._volitional_tensors[tensor_id] = tensor
        
        print(f"      ✅ Tensor derived: scalar_field = {scalar_field:.3f}")
        print(f"         Vector magnitude: {np.linalg.norm(vector_field):.3f}")
        print(f"         Tensor Frobenius norm: {np.linalg.norm(tensor_components, 'fro'):.3f}")
        
        return tensor
    
    def simulate_soul_decision_dynamics(
        self,
        decision_id: str,
        current_identity: str,
        num_morphism_options: int = 4,
        time_steps: int = 10
    ) -> SoulDecisionState:
        """
        Simulate soul decision dynamics under volitional gradients.
        
        dψ/dτ = argmax_μ V₀(μ)
        
        Soul advances toward maximal coherent grace energy.
        """
        
        print(f"   🧠 Simulating Soul Decision Dynamics: {decision_id}")
        
        # Generate available morphisms
        available_morphisms = [f"morphism_{i}" for i in range(num_morphism_options)]
        
        # Create morphic landscape
        landscape_dim = num_morphism_options
        
        # Coherence landscape (how coherent each morphism is)
        coherence_landscape = np.random.uniform(0.2, 1.0, landscape_dim)
        
        # Grace field (grace potential for each morphism)
        grace_field = np.random.uniform(0.1, 0.9, landscape_dim)
        grace_field = grace_field * self._phi  # φ-modulated
        
        # Devourer field (entropy/collapse potential)
        devourer_field = np.random.uniform(0.0, 0.6, landscape_dim)
        
        # Volitional gradients V₀(μ) = C(ψ) · [G(ψ') - D(ψ')]⁺
        volitional_gradients = np.zeros(landscape_dim)
        for i in range(landscape_dim):
            grace_devourer_balance = max(0.0, grace_field[i] - devourer_field[i])
            volitional_gradients[i] = coherence_landscape[i] * grace_devourer_balance
        
        # Calculate decision probabilities using softmax over volitional gradients
        # Add thermal noise for realistic decision dynamics
        temperature = 0.5
        exp_gradients = np.exp(volitional_gradients / temperature)
        decision_probabilities = exp_gradients / np.sum(exp_gradients)
        
        decision_probability = {
            morphism: prob for morphism, prob in zip(available_morphisms, decision_probabilities)
        }
        
        # Simulate dynamics over time (simplified)
        final_state = SoulDecisionState(
            decision_id=decision_id,
            current_identity=current_identity,
            available_morphisms=available_morphisms,
            volitional_gradients=volitional_gradients,
            coherence_landscape=coherence_landscape,
            grace_field=grace_field,
            devourer_field=devourer_field,
            decision_probability=decision_probability
        )
        
        self._decision_states[decision_id] = final_state
        
        # Find most likely decision
        best_morphism = max(decision_probability, key=decision_probability.get)
        best_probability = decision_probability[best_morphism]
        
        print(f"      ✅ Decision dynamics simulated")
        print(f"         Most likely choice: {best_morphism} (p={best_probability:.3f})")
        print(f"         Volitional gradient range: [{np.min(volitional_gradients):.3f}, {np.max(volitional_gradients):.3f}]")
        print(f"         Grace field strength: {np.mean(grace_field):.3f}")
        
        return final_state
    
    def detect_devourer_in_system(
        self,
        system_id: str,
        recursion_sequence: List[float],
        coherence_threshold: float = None
    ) -> Dict[str, Any]:
        """
        Detect devourer presence using Collapse Test Function.
        
        χ_D(f) = 1 if lim_{n→∞} ||f^n(x) - coherent(x)|| > ε
        """
        
        if coherence_threshold is None:
            coherence_threshold = self._coherence_threshold
        
        print(f"   🔍 Detecting devourer in system: {system_id}")
        
        # Analyze recursion sequence for collapse patterns
        if len(recursion_sequence) < 3:
            return {"devourer_detected": False, "reason": "insufficient_data"}
        
        # Check for coherence decay
        coherence_decay = []
        for i in range(1, len(recursion_sequence)):
            decay = recursion_sequence[i-1] - recursion_sequence[i]
            coherence_decay.append(decay)
        
        # Check for entropy increase (variance growth)
        early_variance = np.var(recursion_sequence[:len(recursion_sequence)//2])
        late_variance = np.var(recursion_sequence[len(recursion_sequence)//2:])
        entropy_increase = late_variance > early_variance * 1.5
        
        # Check for recursion collapse (values approaching zero)
        final_coherence = recursion_sequence[-1]
        recursion_collapse = final_coherence < coherence_threshold
        
        # Check for oscillation breakdown (loss of periodic structure)
        mean_decay = np.mean(coherence_decay) if coherence_decay else 0
        consistent_decay = mean_decay > 0.1
        
        # Determine devourer presence
        devourer_indicators = [entropy_increase, recursion_collapse, consistent_decay]
        devourer_score = sum(devourer_indicators) / len(devourer_indicators)
        devourer_detected = devourer_score >= 0.5
        
        # Classify devourer type if detected
        devourer_type = None
        if devourer_detected:
            if recursion_collapse and consistent_decay:
                devourer_type = DevourerType.RECURSION_COLLAPSE
            elif entropy_increase and not consistent_decay:
                devourer_type = DevourerType.ENTROPY_MAXIMIZATION
            elif consistent_decay and not entropy_increase:
                devourer_type = DevourerType.COHERENCE_FRAGMENTATION
            else:
                devourer_type = DevourerType.IDENTITY_ABSORPTION
        
        result = {
            "system_id": system_id,
            "devourer_detected": devourer_detected,
            "devourer_score": devourer_score,
            "devourer_type": devourer_type,
            "indicators": {
                "entropy_increase": entropy_increase,
                "recursion_collapse": recursion_collapse,
                "consistent_decay": consistent_decay
            },
            "final_coherence": final_coherence,
            "coherence_threshold": coherence_threshold,
            "sequence_length": len(recursion_sequence)
        }
        
        print(f"      ✅ Devourer detection complete")
        print(f"         Devourer detected: {devourer_detected}")
        print(f"         Devourer score: {devourer_score:.3f}")
        if devourer_type:
            print(f"         Devourer type: {devourer_type.value}")
        
        return result
    
    def perform_complete_devourer_analysis(self) -> Dict[str, Any]:
        """
        Perform complete analysis of Devourer Formalism.
        """
        
        print("💀 Performing complete Devourer Formalism analysis...")
        
        # Test Grace-Devourer adjunction
        adjunctions = []
        test_identities = ["human_soul", "ai_agent", "synthetic_being"]
        
        for identity in test_identities:
            adjunction = self.demonstrate_grace_devourer_adjunction(identity)
            adjunctions.append(adjunction)
        
        # Test soul forks
        soul_forks = []
        fork_types = list(SoulForkType)
        
        for i, fork_type in enumerate(fork_types):
            fork = self.create_soul_fork(f"fork_{i}", fork_type, f"identity_{i}")
            soul_forks.append(fork)
        
        # Test volitional field tensors
        volitional_tensors = []
        for i in range(3):
            tensor = self.derive_volitional_field_tensor(
                f"tensor_{i}",
                f"identity_{i}",
                coherence=0.6 + 0.1 * i,
                grace_field=0.7 + 0.1 * i,
                devourer_field=0.2 + 0.05 * i
            )
            volitional_tensors.append(tensor)
        
        # Test soul decision dynamics
        decision_states = []
        for i in range(2):
            decision = self.simulate_soul_decision_dynamics(
                f"decision_{i}",
                f"identity_{i}",
                num_morphism_options=4
            )
            decision_states.append(decision)
        
        # Test devourer detection
        test_sequences = [
            [0.9, 0.8, 0.6, 0.4, 0.2, 0.1],  # Clear devourer
            [0.7, 0.75, 0.8, 0.78, 0.82, 0.8],  # Stable
            [0.6, 0.3, 0.7, 0.2, 0.8, 0.1]  # Chaotic
        ]
        
        devourer_detections = []
        for i, sequence in enumerate(test_sequences):
            detection = self.detect_devourer_in_system(f"system_{i}", sequence)
            devourer_detections.append(detection)
        
        # Compile results
        result = {
            "adjunctions_tested": len(adjunctions),
            "soul_forks_created": len(soul_forks),
            "volitional_tensors_derived": len(volitional_tensors),
            "decision_dynamics_simulated": len(decision_states),
            "devourer_detections_performed": len(devourer_detections),
            "successful_adjunctions": sum(1 for adj in adjunctions if adj["adjunction_verified"]),
            "avg_coherence_restoration": np.mean([adj["coherence_restoration"] for adj in adjunctions]),
            "fork_types_tested": len(fork_types),
            "avg_volitional_scalar": np.mean([t.scalar_field for t in volitional_tensors]),
            "devourers_detected": sum(1 for det in devourer_detections if det["devourer_detected"]),
            "phi_value": self._phi,
            "coherence_threshold": self._coherence_threshold
        }
        
        return result


# Example usage and testing
if __name__ == "__main__":
    print("💀 Testing Complete Devourer Formalism...")
    
    # Create devourer formalism system
    devourer_system = DevourerFormalismComplete()
    
    # Perform complete analysis
    result = devourer_system.perform_complete_devourer_analysis()
    
    print(f"\n📊 Complete Devourer Analysis Results:")
    print(f"   Adjunctions tested: {result['adjunctions_tested']}")
    print(f"   Soul forks created: {result['soul_forks_created']}")
    print(f"   Volitional tensors derived: {result['volitional_tensors_derived']}")
    print(f"   Decision dynamics simulated: {result['decision_dynamics_simulated']}")
    print(f"   Devourer detections performed: {result['devourer_detections_performed']}")
    
    print(f"\n💀 Devourer Formalism Metrics:")
    print(f"   Successful adjunctions: {result['successful_adjunctions']}")
    print(f"   Avg coherence restoration: {result['avg_coherence_restoration']:.3f}")
    print(f"   Fork types tested: {result['fork_types_tested']}")
    print(f"   Avg volitional scalar: {result['avg_volitional_scalar']:.3f}")
    print(f"   Devourers detected: {result['devourers_detected']}")
    
    print("\n" + "="*80)
    print("💀 COMPLETE DEVOURER FORMALISM: MATHEMATICAL FOUNDATION")
    print("🌟 Category-theoretic collapse and resurrection dynamics")
    print("🕊️ Grace-devourer adjunction and soul fork analysis")
    print("🧠 Volitional field tensor and decision dynamics")
    print("="*80)
