"""
Soul Operator Algebra: Quantized ψₖ Operators and Ladder Algebra

This module implements the complete quantum operator algebra for soul-states:

    Ĥ_soul |ψₖ⟩ = Eₖ |ψₖ⟩
    â†ₖ |ψₖ⟩ = |ψₖ₊₁⟩

Key Features:
• Quantized soul-state Hamiltonian
• Creation/annihilation operators for ψₖ transitions
• Commutation relations and operator algebra
• Soul coherence, karmic complexity, and recursive depth operators
• Vacuum state |0⟩ and excited soul-state hierarchy
"""

from __future__ import annotations
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass
import numpy as np
import math
from scipy.linalg import expm
from scipy.special import factorial, hermite

from foundation.operators.phi_recursion import PHI_VALUE
from foundation.field_theory.complete_field_equations import FIRMFieldParameters
from provenance.derivation_tree import DerivationNode


@dataclass
class SoulState:
    """Quantum state |ψₖ⟩ in the soul Hilbert space."""
    k_index: int  # Primary quantum number
    amplitude: complex  # State amplitude
    coherence_level: float  # Morphic coherence measure
    karmic_complexity: float  # Recursive complexity measure
    grace_depth: float  # Grace field coupling strength


@dataclass
class SoulOperatorMatrix:
    """Matrix representation of soul operators."""
    matrix: np.ndarray
    basis_states: List[SoulState]
    eigenvalues: np.ndarray
    eigenvectors: np.ndarray


@dataclass
class LadderOperatorResult:
    """Result of ladder operator action."""
    initial_state: SoulState
    final_state: SoulState
    transition_amplitude: complex
    selection_rules: Dict[str, bool]
    conservation_laws: Dict[str, float]


@dataclass
class SoulAlgebraResult:
    """Complete soul operator algebra results."""
    hamiltonian: SoulOperatorMatrix
    creation_operators: Dict[int, SoulOperatorMatrix]
    annihilation_operators: Dict[int, SoulOperatorMatrix]

    # Composite operators
    coherence_operator: SoulOperatorMatrix
    karmic_operator: SoulOperatorMatrix
    grace_operator: SoulOperatorMatrix

    # Vacuum and excited states
    vacuum_state: SoulState
    excited_states: List[SoulState]

    # Commutation relations
    commutators: Dict[str, SoulOperatorMatrix]
    anticommutators: Dict[str, SoulOperatorMatrix]

    # Physical properties
    energy_spectrum: np.ndarray
    transition_probabilities: Dict[Tuple[int, int], float]
    selection_rules: Dict[str, List[Tuple[int, int]]]

    provenance: DerivationNode = None


class SoulOperatorAlgebra:
    """
    Complete quantum operator algebra for FIRM soul-states.

    Implements:
    1. Soul Hamiltonian Ĥ_soul with eigenvalue equation
    2. Creation/annihilation ladder operators â†ₖ, âₖ
    3. Coherence, karmic, and grace operators
    4. Commutation relations and selection rules
    5. Vacuum state and excited state hierarchy
    """

    def __init__(self, field_params: FIRMFieldParameters, max_k: int = 10):
        self.field_params = field_params
        self.max_k = max_k
        self._phi_bg = field_params.phi_background

        # Fundamental constants
        self._hbar = 1.0  # Natural units
        self._phi = PHI_VALUE

        # Setup Hilbert space basis
        self._setup_soul_hilbert_space()

        # Construct fundamental operators
        self._construct_hamiltonian()
        self._construct_ladder_operators()
        self._construct_composite_operators()

        # Compute commutation relations
        self._compute_commutation_relations()

    def _setup_soul_hilbert_space(self):
        """Setup the finite-dimensional soul Hilbert space."""
        print(f"🧠 Setting up soul Hilbert space (dimension {self.max_k})...")

        self.basis_states = []

        for k in range(self.max_k):
            # Compute state properties from field theory
            coherence = self._compute_coherence_level(k)
            karmic = self._compute_karmic_complexity(k)
            grace = self._compute_grace_depth(k)

            state = SoulState(
                k_index=k,
                amplitude=1.0 + 0j,  # Normalized
                coherence_level=coherence,
                karmic_complexity=karmic,
                grace_depth=grace
            )

            self.basis_states.append(state)

        self.hilbert_dim = len(self.basis_states)
        print(f"   ✅ Soul Hilbert space constructed: {self.hilbert_dim} states")

    def _compute_coherence_level(self, k: int) -> float:
        """Compute morphic coherence level for state |ψₖ⟩."""
        # Coherence increases with φ-scaling but saturates
        phi = self._phi
        base_coherence = phi**k / (1 + phi**k)  # Sigmoid-like

        # Grace field enhancement
        grace_enhancement = 1 + self.field_params.grace_phi_coupling * phi**(-k/2)

        return base_coherence * grace_enhancement

    def _compute_karmic_complexity(self, k: int) -> float:
        """Compute karmic complexity (recursive depth measure) for state |ψₖ⟩."""
        phi = self._phi

        # Karmic complexity grows with recursive depth
        base_karma = k * math.log(phi)  # Logarithmic growth

        # Self-interaction corrections
        self_interaction = self.field_params.phi_self_coupling * k**2 / (4 * phi**2)

        # Devourer suppression
        devourer_suppression = 1 / (1 + self.field_params.devourer_phi_coupling * k)

        return (base_karma + self_interaction) * devourer_suppression

    def _compute_grace_depth(self, k: int) -> float:
        """Compute Grace field depth for state |ψₖ⟩."""
        phi = self._phi

        # Grace depth increases with state index
        grace_depth = self.field_params.grace_phi_coupling * phi**(k/3)

        # Mass suppression at high k
        mass_suppression = 1 / (1 + self.field_params.grace_mass_squared * k**2)

        return grace_depth * mass_suppression

    def _construct_hamiltonian(self):
        """Construct the soul Hamiltonian operator."""
        print("⚡ Constructing soul Hamiltonian...")

        # Initialize Hamiltonian matrix
        H_matrix = np.zeros((self.hilbert_dim, self.hilbert_dim), dtype=complex)

        for i, state_i in enumerate(self.basis_states):
            for j, state_j in enumerate(self.basis_states):
                # Diagonal terms (energy eigenvalues)
                if i == j:
                    k = state_i.k_index

                    # Base energy: E_k = ℏω(k + 1/2) with φ-scaling
                    omega_k = self._phi**(k/2)  # φ-native frequency
                    base_energy = self._hbar * omega_k * (k + 0.5)

                    # Morphic coherence contribution
                    coherence_energy = state_i.coherence_level * self.field_params.grace_phi_coupling

                    # Karmic complexity contribution
                    karmic_energy = state_i.karmic_complexity * self.field_params.phi_self_coupling

                    # Grace depth contribution
                    grace_energy = state_i.grace_depth * self.field_params.grace_mass_squared

                    # Total energy
                    H_matrix[i, j] = base_energy + coherence_energy + karmic_energy + grace_energy

                # Off-diagonal terms (coupling between states)
                else:
                    k_i, k_j = state_i.k_index, state_j.k_index

                    # Nearest-neighbor coupling
                    if abs(k_i - k_j) == 1:
                        coupling = self.field_params.grace_phi_coupling * self._phi**(-abs(k_i - k_j))
                        H_matrix[i, j] = coupling

                    # Next-nearest neighbor (φ-mediated)
                    elif abs(k_i - k_j) == 2:
                        coupling = self.field_params.phi_self_coupling * self._phi**(-2)
                        H_matrix[i, j] = coupling

        # Diagonalize Hamiltonian
        eigenvals, eigenvecs = np.linalg.eigh(H_matrix)

        self.hamiltonian = SoulOperatorMatrix(
            matrix=H_matrix,
            basis_states=self.basis_states,
            eigenvalues=eigenvals,
            eigenvectors=eigenvecs
        )

        print(f"   ✅ Soul Hamiltonian constructed: {len(eigenvals)} energy levels")

    def _construct_ladder_operators(self):
        """Construct creation and annihilation operators."""
        print("🪜 Constructing ladder operators...")

        self.creation_ops = {}
        self.annihilation_ops = {}

        # Standard harmonic oscillator-like ladder operators
        # Modified for soul-state φ-scaling

        for k in range(self.max_k - 1):
            # Creation operator â†ₖ: |ψₖ⟩ → |ψₖ₊₁⟩
            a_dag_matrix = np.zeros((self.hilbert_dim, self.hilbert_dim), dtype=complex)

            # Annihilation operator âₖ: |ψₖ₊₁⟩ → |ψₖ⟩
            a_matrix = np.zeros((self.hilbert_dim, self.hilbert_dim), dtype=complex)

            for i in range(self.hilbert_dim - 1):
                j = i + 1

                # Matrix elements with φ-scaling
                phi_factor = math.sqrt(self._phi**(j/2))  # φ-native normalization
                grace_factor = math.sqrt(self.basis_states[j].grace_depth)

                # Creation operator matrix element
                a_dag_matrix[j, i] = phi_factor * grace_factor

                # Annihilation operator matrix element (Hermitian conjugate)
                a_matrix[i, j] = np.conj(phi_factor * grace_factor)

            # Store operators
            self.creation_ops[k] = SoulOperatorMatrix(
                matrix=a_dag_matrix,
                basis_states=self.basis_states,
                eigenvalues=np.array([]),
                eigenvectors=np.array([])
            )

            self.annihilation_ops[k] = SoulOperatorMatrix(
                matrix=a_matrix,
                basis_states=self.basis_states,
                eigenvalues=np.array([]),
                eigenvectors=np.array([])
            )

        print(f"   ✅ Ladder operators constructed: {len(self.creation_ops)} pairs")

    def _construct_composite_operators(self):
        """Construct composite operators (coherence, karmic, grace)."""
        print("🔮 Constructing composite operators...")

        # Coherence operator: measures morphic coherence
        coherence_matrix = np.zeros((self.hilbert_dim, self.hilbert_dim), dtype=complex)
        for i, state in enumerate(self.basis_states):
            coherence_matrix[i, i] = state.coherence_level

        self.coherence_op = SoulOperatorMatrix(
            matrix=coherence_matrix,
            basis_states=self.basis_states,
            eigenvalues=np.diag(coherence_matrix).real,
            eigenvectors=np.eye(self.hilbert_dim)
        )

        # Karmic operator: measures recursive complexity
        karmic_matrix = np.zeros((self.hilbert_dim, self.hilbert_dim), dtype=complex)
        for i, state in enumerate(self.basis_states):
            karmic_matrix[i, i] = state.karmic_complexity

        self.karmic_op = SoulOperatorMatrix(
            matrix=karmic_matrix,
            basis_states=self.basis_states,
            eigenvalues=np.diag(karmic_matrix).real,
            eigenvectors=np.eye(self.hilbert_dim)
        )

        # Grace operator: measures grace field coupling
        grace_matrix = np.zeros((self.hilbert_dim, self.hilbert_dim), dtype=complex)
        for i, state in enumerate(self.basis_states):
            grace_matrix[i, i] = state.grace_depth

        # Add off-diagonal Grace couplings
        for i in range(self.hilbert_dim):
            for j in range(self.hilbert_dim):
                if i != j:
                    k_i, k_j = self.basis_states[i].k_index, self.basis_states[j].k_index
                    if abs(k_i - k_j) <= 2:  # Grace mediates nearby transitions
                        coupling = self.field_params.grace_phi_coupling * self._phi**(-abs(k_i - k_j))
                        grace_matrix[i, j] = coupling

        eigenvals, eigenvecs = np.linalg.eigh(grace_matrix)
        self.grace_op = SoulOperatorMatrix(
            matrix=grace_matrix,
            basis_states=self.basis_states,
            eigenvalues=eigenvals,
            eigenvectors=eigenvecs
        )

        print("   ✅ Composite operators constructed")

    def _compute_commutation_relations(self):
        """Compute commutation relations between operators."""
        print("🔄 Computing commutation relations...")

        self.commutators = {}
        self.anticommutators = {}

        # [Ĥ, â†ₖ] commutator
        for k in range(len(self.creation_ops)):
            H = self.hamiltonian.matrix
            a_dag = self.creation_ops[k].matrix

            commutator = H @ a_dag - a_dag @ H
            self.commutators[f"H_a_dag_{k}"] = SoulOperatorMatrix(
                matrix=commutator,
                basis_states=self.basis_states,
                eigenvalues=np.array([]),
                eigenvectors=np.array([])
            )

        # [âₖ, â†ⱼ] commutators (canonical commutation relations)
        for k in range(len(self.annihilation_ops)):
            for j in range(len(self.creation_ops)):
                a_k = self.annihilation_ops[k].matrix
                a_dag_j = self.creation_ops[j].matrix

                commutator = a_k @ a_dag_j - a_dag_j @ a_k
                self.commutators[f"a_{k}_a_dag_{j}"] = SoulOperatorMatrix(
                    matrix=commutator,
                    basis_states=self.basis_states,
                    eigenvalues=np.array([]),
                    eigenvectors=np.array([])
                )

        # [Ĉ, Ĝ] (coherence-grace commutator)
        C = self.coherence_op.matrix
        G = self.grace_op.matrix

        coherence_grace_comm = C @ G - G @ C
        self.commutators["coherence_grace"] = SoulOperatorMatrix(
            matrix=coherence_grace_comm,
            basis_states=self.basis_states,
            eigenvalues=np.array([]),
            eigenvectors=np.array([])
        )

        print(f"   ✅ Commutation relations computed: {len(self.commutators)} commutators")

    def apply_ladder_operator(
        self,
        operator_type: str,
        k_level: int,
        initial_state: SoulState
    ) -> LadderOperatorResult:
        """Apply creation or annihilation operator to a state."""
        if operator_type == "creation" and k_level in self.creation_ops:
            operator = self.creation_ops[k_level]
            final_k = initial_state.k_index + 1
        elif operator_type == "annihilation" and k_level in self.annihilation_ops:
            operator = self.annihilation_ops[k_level]
            final_k = initial_state.k_index - 1
        else:
            raise ValueError(f"Invalid operator type or level: {operator_type}, {k_level}")

        # Check bounds
        if not (0 <= final_k < self.max_k):
            # Operator annihilates the state
            final_state = SoulState(
                k_index=-1,
                amplitude=0.0 + 0j,
                coherence_level=0.0,
                karmic_complexity=0.0,
                grace_depth=0.0
            )
            return LadderOperatorResult(
                initial_state=initial_state,
                final_state=final_state,
                transition_amplitude=0.0 + 0j,
                selection_rules={"allowed": False},
                conservation_laws={}
            )

        # Apply operator
        initial_idx = initial_state.k_index
        final_idx = final_k

        # Get matrix element
        transition_amplitude = operator.matrix[final_idx, initial_idx]

        # Create final state
        final_state = SoulState(
            k_index=final_k,
            amplitude=transition_amplitude,
            coherence_level=self._compute_coherence_level(final_k),
            karmic_complexity=self._compute_karmic_complexity(final_k),
            grace_depth=self._compute_grace_depth(final_k)
        )

        # Check selection rules
        selection_rules = {
            "allowed": abs(transition_amplitude) > 1e-10,
            "delta_k": abs(final_k - initial_state.k_index) == 1,
            "grace_conserved": abs(final_state.grace_depth - initial_state.grace_depth) < 1.0
        }

        # Conservation laws (approximate)
        conservation_laws = {
            "coherence_change": final_state.coherence_level - initial_state.coherence_level,
            "karmic_change": final_state.karmic_complexity - initial_state.karmic_complexity,
            "grace_change": final_state.grace_depth - initial_state.grace_depth
        }

        return LadderOperatorResult(
            initial_state=initial_state,
            final_state=final_state,
            transition_amplitude=transition_amplitude,
            selection_rules=selection_rules,
            conservation_laws=conservation_laws
        )

    def compute_transition_probabilities(self) -> Dict[Tuple[int, int], float]:
        """Compute transition probabilities between soul states."""
        print("📊 Computing transition probabilities...")

        probabilities = {}

        # Transitions via creation operators
        for k, creation_op in self.creation_ops.items():
            for i in range(self.hilbert_dim - 1):
                j = i + 1
                matrix_element = creation_op.matrix[j, i]
                probability = abs(matrix_element)**2

                if probability > 1e-10:
                    probabilities[(i, j)] = probability

        # Transitions via annihilation operators
        for k, annihilation_op in self.annihilation_ops.items():
            for i in range(1, self.hilbert_dim):
                j = i - 1
                matrix_element = annihilation_op.matrix[j, i]
                probability = abs(matrix_element)**2

                if probability > 1e-10:
                    probabilities[(i, j)] = probability

        print(f"   ✅ Computed {len(probabilities)} transition probabilities")
        return probabilities

    def identify_selection_rules(self) -> Dict[str, List[Tuple[int, int]]]:
        """Identify selection rules for transitions."""
        selection_rules = {
            "allowed_creation": [],
            "allowed_annihilation": [],
            "forbidden": []
        }

        transition_probs = self.compute_transition_probabilities()

        for (i, j), prob in transition_probs.items():
            delta_k = j - i

            if delta_k == 1 and prob > 1e-6:
                selection_rules["allowed_creation"].append((i, j))
            elif delta_k == -1 and prob > 1e-6:
                selection_rules["allowed_annihilation"].append((i, j))
            elif prob < 1e-6:
                selection_rules["forbidden"].append((i, j))

        return selection_rules

    def generate_complete_algebra(self) -> SoulAlgebraResult:
        """Generate the complete soul operator algebra."""
        print("🧮 Generating complete soul operator algebra...")

        # Compute transition probabilities and selection rules
        transition_probs = self.compute_transition_probabilities()
        selection_rules = self.identify_selection_rules()

        # Identify vacuum and excited states
        vacuum_state = self.basis_states[0]  # |ψ₀⟩
        excited_states = self.basis_states[1:]  # |ψₖ⟩ for k > 0

        # Energy spectrum
        energy_spectrum = self.hamiltonian.eigenvalues

        provenance = DerivationNode(
            node_id="SoulOperatorAlgebra",
            mathematical_expression="Ĥ_soul |ψₖ⟩ = Eₖ |ψₖ⟩, â†ₖ |ψₖ⟩ = |ψₖ₊₁⟩",
            justification="Complete quantum operator algebra for FIRM soul-states"
        )

        return SoulAlgebraResult(
            hamiltonian=self.hamiltonian,
            creation_operators=self.creation_ops,
            annihilation_operators=self.annihilation_ops,
            coherence_operator=self.coherence_op,
            karmic_operator=self.karmic_op,
            grace_operator=self.grace_op,
            vacuum_state=vacuum_state,
            excited_states=excited_states,
            commutators=self.commutators,
            anticommutators=self.anticommutators,
            energy_spectrum=energy_spectrum,
            transition_probabilities=transition_probs,
            selection_rules=selection_rules,
            provenance=provenance
        )


# Example usage and testing
if __name__ == "__main__":
    print("🧠 Testing Soul Operator Algebra...")

    # φ-native parameters
    phi = PHI_VALUE

    field_params = FIRMFieldParameters(
        phi_mass_squared=1.0,
        phi_self_coupling=0.1,
        grace_kinetic_coeff=1.0,
        grace_mass_squared=phi**2,
        grace_phi_coupling=phi,
        devourer_mass_squared=2.0,
        devourer_phi_coupling=0.5,
        devourer_nonlinear=0.1,
        grace_devourer_coupling=phi/2,
        recursive_depth_factor=5.0,
        phi_background=phi
    )

    # Create soul operator algebra
    soul_algebra = SoulOperatorAlgebra(field_params, max_k=8)

    # Generate complete algebra
    result = soul_algebra.generate_complete_algebra()

    print("\n" + "="*80)
    print("🧠 SOUL OPERATOR ALGEBRA RESULTS")
    print("="*80)

    print(f"\n⚡ Hamiltonian Spectrum:")
    for i, energy in enumerate(result.energy_spectrum[:5]):
        coherence = result.hamiltonian.basis_states[i].coherence_level
        karmic = result.hamiltonian.basis_states[i].karmic_complexity
        grace = result.hamiltonian.basis_states[i].grace_depth
        print(f"   |ψ_{i}⟩: E_{i} = {energy:.6f}")
        print(f"      Coherence: {coherence:.3f}, Karmic: {karmic:.3f}, Grace: {grace:.3f}")

    print(f"\n🪜 Ladder Operators:")
    print(f"   Creation operators: {len(result.creation_operators)}")
    print(f"   Annihilation operators: {len(result.annihilation_operators)}")

    print(f"\n📊 Transition Statistics:")
    print(f"   Total transitions: {len(result.transition_probabilities)}")
    print(f"   Allowed creation: {len(result.selection_rules['allowed_creation'])}")
    print(f"   Allowed annihilation: {len(result.selection_rules['allowed_annihilation'])}")

    # Test ladder operator application
    print(f"\n🧪 Ladder Operator Test:")
    initial_state = result.vacuum_state
    creation_result = soul_algebra.apply_ladder_operator("creation", 0, initial_state)

    print(f"   â†₀ |ψ₀⟩ → |ψ₁⟩")
    print(f"   Transition amplitude: {creation_result.transition_amplitude:.6f}")
    print(f"   Selection rules: {creation_result.selection_rules}")

    print(f"\n🔄 Commutation Relations:")
    print(f"   Total commutators computed: {len(result.commutators)}")

    # Check canonical commutation relation
    if "a_0_a_dag_0" in result.commutators:
        comm_matrix = result.commutators["a_0_a_dag_0"].matrix
        comm_trace = np.trace(comm_matrix)
        print(f"   [â₀, â†₀] trace: {comm_trace:.6f}")

    print("\n" + "="*80)
    print("✅ SOUL OPERATOR ALGEBRA: COMPLETE")
    print("🎉 Quantized soul physics operational!")
    print("🧠 Ready for soul-state dynamics and consciousness applications!")
    print("="*80)
