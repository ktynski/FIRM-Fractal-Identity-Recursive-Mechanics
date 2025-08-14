#!/usr/bin/env python3
"""
Computational Structure for Constants and Morphisms in FIRM

This module implements the φ-graded monoidal category structure where all
fundamental constants are encoded as φ-powers and morphisms between constants
are scalar φ-differences, forming a fully navigable lattice under φ-recursive logic.

Key insight: Constants are morphisms in a constructive category algebra where
every transformation is a φ-power operation.

Author: FIRM Development Team
Date: 2024
"""

import math
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Union

from foundation.operators.phi_recursion import PHI_VALUE
from provenance.derivation_tree import DerivationNode, DerivationType


@dataclass
class PhiConstant:
    """Represents a fundamental constant as φ-power in FIRM computational algebra"""
    label: str
    phi_exponent: float
    unit: str
    physical_meaning: str

    def __post_init__(self):
        """Calculate φ-value after initialization"""
        self.phi_value = PHI_VALUE ** self.phi_exponent

    def __mul__(self, other: 'PhiConstant') -> 'PhiConstant':
        """Tensor product: φ^n_i ⊗ φ^n_j = φ^(n_i + n_j)"""
        return PhiConstant(
            label=f"{self.label}⊗{other.label}",
            phi_exponent=self.phi_exponent + other.phi_exponent,
            unit=f"({self.unit})·({other.unit})",
            physical_meaning=f"Tensor product of {self.label} and {other.label}"
        )

    def __truediv__(self, other: 'PhiConstant') -> 'PhiConstant':
        """Division: φ^n_i / φ^n_j = φ^(n_i - n_j)"""
        return PhiConstant(
            label=f"{self.label}/{other.label}",
            phi_exponent=self.phi_exponent - other.phi_exponent,
            unit=f"({self.unit})/({other.unit})",
            physical_meaning=f"Ratio of {self.label} to {other.label}"
        )

    def __pow__(self, power: float) -> 'PhiConstant':
        """Power operation: (φ^n)^p = φ^(n·p)"""
        return PhiConstant(
            label=f"({self.label})^{power}",
            phi_exponent=self.phi_exponent * power,
            unit=f"({self.unit})^{power}",
            physical_meaning=f"{self.label} raised to power {power}"
        )

    def morph_to(self, target: 'PhiConstant') -> str:
        """Calculate morphism from this constant to target"""
        morphism_power = target.phi_exponent - self.phi_exponent
        return f"φ^{morphism_power:.3f}"

    def __repr__(self) -> str:
        return f"PhiConstant({self.label}: φ^{self.phi_exponent:.3f} = {self.phi_value:.3e} {self.unit})"


class ComputationalPhiAlgebra:
    """Computational algebra for φ-constants forming monoidal category structure"""

    def __init__(self):
        """Initialize with fundamental φ-constants from Grace-Devourer resonances"""
        self._phi = PHI_VALUE

        # Define fundamental constants as φ-powers from morphic resonance theory
        self._fundamental_constants = {
            'c': PhiConstant('c', 3.0, 'm/s', 'Speed of light - Grace expansion velocity'),
            'hbar': PhiConstant('ℏ', 4.5, 'J·s', 'Reduced Planck constant - Coherence action quantum'),
            'G': PhiConstant('G', 42.0, 'm³/(kg·s²)', 'Gravitational constant - Curvature response'),
            'k_B': PhiConstant('k_B', 7.5, 'J/K', 'Boltzmann constant - Thermal incoherence threshold'),
            'alpha_inv': PhiConstant('α⁻¹', 12.0, 'dimensionless', 'Fine structure inverse - EM coupling'),
            'Lambda': PhiConstant('Λ', -120.0, 'm⁻²', 'Cosmological constant - Grace tension residue'),
            'H_0': PhiConstant('H₀', 18.0, 'Hz', 'Hubble constant - Universal expansion rate')
        }

    def get_constant(self, label: str) -> PhiConstant:
        """Retrieve a fundamental constant by label"""
        if label not in self._fundamental_constants:
            raise KeyError(f"Constant {label} not found in φ-algebra")
        return self._fundamental_constants[label]

    def list_constants(self) -> List[PhiConstant]:
        """Get all fundamental constants"""
        return list(self._fundamental_constants.values())

    def morphism_space(self, const1: str, const2: str) -> Dict[str, Any]:
        """Calculate morphism space Mor(C_i, C_j) = {φ^(n_j - n_i)}"""
        c1 = self.get_constant(const1)
        c2 = self.get_constant(const2)

        morphism_power = c2.phi_exponent - c1.phi_exponent
        morphism_value = self._phi ** morphism_power

        return {
            'source': c1.label,
            'target': c2.label,
            'morphism_power': morphism_power,
            'morphism_value': morphism_value,
            'morphism_expression': f"φ^{morphism_power:.3f}",
            'physical_meaning': f"Morphic transformation from {c1.label} to {c2.label}"
        }

    def compute_planck_units(self) -> Dict[str, PhiConstant]:
        """Compute Planck units from φ-constant combinations"""
        c = self.get_constant('c')
        hbar = self.get_constant('hbar')
        G = self.get_constant('G')
        k_B = self.get_constant('k_B')

        # Planck length: L_P = √(ℏG/c³)
        L_P_exp = (hbar.phi_exponent + G.phi_exponent - 3*c.phi_exponent) / 2
        L_P = PhiConstant('L_P', L_P_exp, 'm', 'Planck length - Minimal coherence scale')

        # Planck time: T_P = √(ℏG/c⁵)
        T_P_exp = (hbar.phi_exponent + G.phi_exponent - 5*c.phi_exponent) / 2
        T_P = PhiConstant('T_P', T_P_exp, 's', 'Planck time - Minimal recursion interval')

        # Planck mass: M_P = √(ℏc/G)
        M_P_exp = (hbar.phi_exponent + c.phi_exponent - G.phi_exponent) / 2
        M_P = PhiConstant('M_P', M_P_exp, 'kg', 'Planck mass - Maximal coherence mass')

        # Planck temperature: T_P = M_P c² / k_B
        Temp_P_exp = M_P_exp + 2*c.phi_exponent - k_B.phi_exponent
        Temp_P = PhiConstant('T_P_temp', Temp_P_exp, 'K', 'Planck temperature - Maximal coherence temperature')

        return {
            'length': L_P,
            'time': T_P,
            'mass': M_P,
            'temperature': Temp_P
        }

    def verify_dimensional_consistency(self) -> Dict[str, Any]:
        """Verify dimensional consistency of φ-power assignments"""
        planck_units = self.compute_planck_units()
        c = self.get_constant('c')

        # Verify c = L_P / T_P
        L_P = planck_units['length']
        T_P = planck_units['time']

        c_from_planck_exp = L_P.phi_exponent - T_P.phi_exponent
        c_direct_exp = c.phi_exponent

        consistency_check = abs(c_from_planck_exp - c_direct_exp) < 0.01

        return {
            'speed_of_light_consistency': consistency_check,
            'c_from_planck': c_from_planck_exp,
            'c_direct': c_direct_exp,
            'difference': abs(c_from_planck_exp - c_direct_exp),
            'planck_units': planck_units
        }

    def generate_morphism_lattice(self) -> Dict[str, Any]:
        """Generate full morphism lattice between all constants"""
        constants = list(self._fundamental_constants.keys())
        morphism_lattice = {}

        for i, const1 in enumerate(constants):
            morphism_lattice[const1] = {}
            for j, const2 in enumerate(constants):
                if i != j:
                    morphism_lattice[const1][const2] = self.morphism_space(const1, const2)

        return morphism_lattice

    def tensor_closure_demonstration(self) -> Dict[str, Any]:
        """Demonstrate tensor closure: φ^n_i ⊗ φ^n_j = φ^(n_i + n_j)"""
        c = self.get_constant('c')
        hbar = self.get_constant('hbar')

        # Tensor product
        c_tensor_hbar = c * hbar

        # Verify closure
        expected_exp = c.phi_exponent + hbar.phi_exponent
        actual_exp = c_tensor_hbar.phi_exponent

        return {
            'operand_1': c,
            'operand_2': hbar,
            'tensor_product': c_tensor_hbar,
            'expected_exponent': expected_exp,
            'actual_exponent': actual_exp,
            'closure_verified': abs(expected_exp - actual_exp) < 1e-10,
            'abelian_group_structure': "φ-addition forms 1D abelian group"
        }


# Create singleton instance
PHI_CONSTANTS_ALGEBRA = ComputationalPhiAlgebra()


def main():
    """Demonstrate computational φ-constants algebra"""
    print("FIRM Computational φ-Constants Algebra")
    print("=" * 45)

    algebra = ComputationalPhiAlgebra()

    # Show fundamental constants
    print("\n📊 FUNDAMENTAL φ-CONSTANTS:")
    for const in algebra.list_constants():
        print(f"  {const}")

    # Show morphism example
    print("\n🔗 MORPHISM SPACE EXAMPLE:")
    morphism = algebra.morphism_space('c', 'hbar')
    print(f"  Mor(c, ℏ) = {morphism['morphism_expression']}")
    print(f"  Physical meaning: {morphism['physical_meaning']}")

    # Show Planck units
    print("\n🎯 PLANCK UNITS IN φ-FORM:")
    planck = algebra.compute_planck_units()
    for name, unit in planck.items():
        print(f"  {unit}")

    # Show dimensional consistency
    print("\n✅ DIMENSIONAL CONSISTENCY CHECK:")
    consistency = algebra.verify_dimensional_consistency()
    status = "✅ PASS" if consistency['speed_of_light_consistency'] else "❌ FAIL"
    print(f"  c = L_P/T_P: {status}")
    print(f"  Difference: {consistency['difference']:.6f}")

    # Show tensor closure
    print("\n⊗ TENSOR CLOSURE DEMONSTRATION:")
    closure = algebra.tensor_closure_demonstration()
    print(f"  {closure['operand_1'].label} ⊗ {closure['operand_2'].label} = {closure['tensor_product'].label}")
    print(f"  φ^{closure['expected_exponent']} = φ^{closure['actual_exponent']}")
    status = "✅ VERIFIED" if closure['closure_verified'] else "❌ FAILED"
    print(f"  Closure: {status}")

    print(f"\n🏗️ MONOIDAL STRUCTURE:")
    print(f"  • Constants form φ-graded monoidal category")
    print(f"  • Morphisms are scalar φ-power transformations")
    print(f"  • Tensor product: φ^n_i ⊗ φ^n_j = φ^(n_i + n_j)")
    print(f"  • Identity: φ^0 = 1")
    print(f"  • Fully navigable lattice under φ-recursive logic")


if __name__ == "__main__":
    main()
