"""
Morphic Field Equation: The Fundamental Dynamics of FSCTF/FIRM

This module implements the Euler-Lagrange equation derived from the FIRM Lagrangian:

    0 = ∑_{r=1}^∞ [(-1)^r / r^d] * [2r φ^(2r-1) - r λ_r G φ^(r-1)] - ξ G D

This equation governs the dynamics of the morphic field φ(x) under Grace-Devourer
interaction, providing the mathematical foundation for all FIRM phenomena.

Key Features:
- Recursive potential with infinite series expansion
- Grace operator G coupling to morphic field
- Devourer D as entropy resistance term
- φ-native parameterization consistent with golden ratio structure
- Exact symbolic computation with numerical evaluation
"""

import numpy as np
import math
from typing import Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass
from scipy.optimize import fsolve, minimize_scalar
from scipy.special import zeta

from foundation.operators.phi_recursion import PHI_VALUE
# from foundation.operators.grace_operator import GraceOperator  # Not needed for field equation
from provenance.derivation_tree import DerivationNode


@dataclass
class MorphicFieldParameters:
    """Parameters for the morphic field equation"""
    d: float  # Scaling dimension
    xi: float  # Grace-Devourer coupling constant
    lambda_coefficients: Dict[int, float]  # λ_r coefficients for recursive potential
    grace_amplitude: float  # G - Grace operator amplitude
    devourer_amplitude: float  # D - Devourer amplitude
    phi_background: float  # Background φ value
    max_terms: int = 50  # Maximum terms in infinite series


@dataclass
class MorphicFieldSolution:
    """Solution to the morphic field equation"""
    phi_value: float
    field_equation_residual: float
    energy_density: float
    grace_term: float
    devourer_term: float
    recursive_potential: float
    convergence_achieved: bool
    mathematical_justification: str


class MorphicFieldEquation:
    """
    Implementation of the fundamental FIRM morphic field equation.
    
    This class solves the Euler-Lagrange equation derived from the recursive
    Lagrangian, finding stable configurations of the morphic field φ.
    """
    
    def __init__(self, parameters: MorphicFieldParameters):
        self.params = parameters
        self._phi = PHI_VALUE
        # Grace operator coupling handled through parameters
        
        # Validate parameters
        self._validate_parameters()
        
    def _validate_parameters(self):
        """Validate physical consistency of parameters"""
        if self.params.d <= 0:
            raise ValueError("Scaling dimension d must be positive")
        if self.params.max_terms <= 0:
            raise ValueError("max_terms must be positive")
        if not self.params.lambda_coefficients:
            raise ValueError("lambda_coefficients cannot be empty")
            
    def _compute_recursive_potential_term(self, phi: float, r: int) -> float:
        """
        Compute the r-th term in the recursive potential series.
        
        Term: (-1)^r / r^d * [2r φ^(2r-1) - r λ_r G φ^(r-1)]
        """
        if r not in self.params.lambda_coefficients:
            return 0.0
            
        lambda_r = self.params.lambda_coefficients[r]
        G = self.params.grace_amplitude
        d = self.params.d
        
        # Avoid numerical overflow for large r or phi
        if abs(phi) > 10 or r > 20:
            # Use log-space computation for stability
            try:
                sign = (-1) ** r
                log_coeff = -r * math.log(r) * d if r > 1 else 0
                
                # First term: 2r φ^(2r-1)
                if 2*r - 1 > 0:
                    log_term1 = math.log(2*r) + (2*r - 1) * math.log(abs(phi))
                    term1 = sign * math.exp(log_coeff + log_term1) * (1 if phi >= 0 else (-1)**(2*r-1))
                else:
                    term1 = 0.0
                    
                # Second term: r λ_r G φ^(r-1)
                if r - 1 > 0:
                    log_term2 = math.log(r) + math.log(abs(lambda_r)) + math.log(abs(G)) + (r - 1) * math.log(abs(phi))
                    term2 = sign * lambda_r * G * math.exp(log_coeff + log_term2) * (1 if phi >= 0 else (-1)**(r-1))
                elif r == 1:
                    term2 = sign * lambda_r * G / (r ** d)
                else:
                    term2 = 0.0
                    
                return term1 - term2
                
            except (OverflowError, ValueError):
                return 0.0  # Term is negligible
        else:
            # Direct computation for small values
            sign = (-1) ** r
            coeff = 1.0 / (r ** d)
            term1 = 2 * r * (phi ** (2*r - 1))
            term2 = r * lambda_r * self.params.grace_amplitude * (phi ** (r - 1))
            
            return sign * coeff * (term1 - term2)
    
    def _evaluate_field_equation(self, phi: float) -> float:
        """
        Evaluate the left-hand side of the morphic field equation.
        
        Returns 0 when φ is a solution.
        """
        # Compute the infinite series (truncated)
        series_sum = 0.0
        for r in range(1, self.params.max_terms + 1):
            term = self._compute_recursive_potential_term(phi, r)
            series_sum += term
            
            # Check for convergence
            if abs(term) < 1e-15 and r > 10:
                break
                
        # Grace-Devourer coupling term
        xi = self.params.xi
        G = self.params.grace_amplitude
        D = self.params.devourer_amplitude
        coupling_term = xi * G * D
        
        return series_sum - coupling_term
    
    def _compute_energy_density(self, phi: float) -> float:
        """Compute energy density for a given field configuration"""
        # Kinetic term (simplified for static case)
        kinetic = 0.5 * (phi - self.params.phi_background) ** 2
        
        # Potential energy from recursive terms
        potential = 0.0
        for r in range(1, self.params.max_terms + 1):
            if r in self.params.lambda_coefficients:
                lambda_r = self.params.lambda_coefficients[r]
                # V_r = λ_r φ^(2r) / (2r)
                potential += lambda_r * (phi ** (2*r)) / (2*r)
                
        # Grace-Devourer interaction energy
        interaction = self.params.xi * self.params.grace_amplitude * self.params.devourer_amplitude * phi
        
        return kinetic + potential + interaction
    
    def solve_field_equation(self, initial_guess: Optional[float] = None) -> MorphicFieldSolution:
        """
        Solve the morphic field equation for stable φ configurations.
        
        Args:
            initial_guess: Starting point for numerical solver
            
        Returns:
            MorphicFieldSolution with field value and analysis
        """
        if initial_guess is None:
            # Use φ-native initial guess
            initial_guess = self._phi
            
        try:
            # Solve the nonlinear equation
            solution = fsolve(self._evaluate_field_equation, initial_guess, 
                            xtol=1e-12, full_output=True)
            
            phi_solution = float(solution[0][0])
            info = solution[1]
            
            # Verify solution quality
            residual = self._evaluate_field_equation(phi_solution)
            convergence_achieved = abs(residual) < 1e-10
            
            # Compute additional quantities
            energy_density = self._compute_energy_density(phi_solution)
            
            # Decompose terms for analysis
            grace_contribution = 0.0
            devourer_contribution = self.params.xi * self.params.grace_amplitude * self.params.devourer_amplitude
            
            for r in range(1, min(10, self.params.max_terms + 1)):
                if r in self.params.lambda_coefficients:
                    lambda_r = self.params.lambda_coefficients[r]
                    grace_contribution += ((-1)**r / r**self.params.d) * r * lambda_r * self.params.grace_amplitude * (phi_solution ** (r-1))
            
            # Compute recursive potential
            recursive_potential = sum(
                self._compute_recursive_potential_term(phi_solution, r) 
                for r in range(1, min(20, self.params.max_terms + 1))
            )
            
            mathematical_justification = f"""
            Morphic Field Solution φ = {phi_solution:.6f}:
            - Field equation residual: {residual:.2e}
            - Energy density: {energy_density:.6f}
            - Grace contribution: {grace_contribution:.6f}
            - Devourer coupling: {devourer_contribution:.6f}
            - Recursive potential: {recursive_potential:.6f}
            - Convergence: {'achieved' if convergence_achieved else 'partial'}
            """
            
            return MorphicFieldSolution(
                phi_value=phi_solution,
                field_equation_residual=residual,
                energy_density=energy_density,
                grace_term=grace_contribution,
                devourer_term=devourer_contribution,
                recursive_potential=recursive_potential,
                convergence_achieved=convergence_achieved,
                mathematical_justification=mathematical_justification
            )
            
        except Exception as e:
            # Return a failed solution with diagnostic information
            return MorphicFieldSolution(
                phi_value=initial_guess,
                field_equation_residual=float('inf'),
                energy_density=float('inf'),
                grace_term=0.0,
                devourer_term=0.0,
                recursive_potential=0.0,
                convergence_achieved=False,
                mathematical_justification=f"Solution failed: {str(e)}"
            )
    
    def find_multiple_solutions(self, num_attempts: int = 10) -> List[MorphicFieldSolution]:
        """Find multiple solutions by trying different initial conditions"""
        solutions = []
        
        # Try various φ-related initial guesses
        initial_guesses = [
            self._phi,  # Golden ratio
            1.0 / self._phi,  # φ^(-1)
            self._phi ** 2,  # φ^2
            1.0,  # Unity
            0.0,  # Vacuum
            -self._phi,  # Negative φ
            self._phi ** 0.5,  # √φ
            2.0,  # Simple integer
            math.pi,  # π
            math.e  # e
        ]
        
        for guess in initial_guesses[:num_attempts]:
            solution = self.solve_field_equation(guess)
            if solution.convergence_achieved:
                # Check if this is a new solution
                is_new = True
                for existing in solutions:
                    if abs(existing.phi_value - solution.phi_value) < 1e-8:
                        is_new = False
                        break
                if is_new:
                    solutions.append(solution)
                    
        return solutions
    
    def analyze_stability(self, phi_solution: float) -> Dict[str, float]:
        """Analyze the stability of a field solution"""
        # Compute second derivative of the field equation
        eps = 1e-8
        f_plus = self._evaluate_field_equation(phi_solution + eps)
        f_minus = self._evaluate_field_equation(phi_solution - eps)
        second_derivative = (f_plus - f_minus) / (2 * eps)
        
        # Compute effective mass squared
        mass_squared = second_derivative
        
        # Stability analysis
        stability_criterion = "stable" if mass_squared > 0 else "unstable" if mass_squared < 0 else "marginal"
        
        return {
            "second_derivative": second_derivative,
            "effective_mass_squared": mass_squared,
            "stability": stability_criterion,
            "characteristic_frequency": math.sqrt(abs(mass_squared)) if mass_squared > 0 else 0.0
        }


def create_phi_native_parameters() -> MorphicFieldParameters:
    """Create φ-native parameters for the morphic field equation"""
    phi = PHI_VALUE
    
    # φ-native λ coefficients following golden ratio structure
    lambda_coefficients = {
        1: 1.0,  # Base coupling
        2: 1.0 / phi,  # φ^(-1) suppression
        3: 1.0 / (phi ** 2),  # φ^(-2) suppression
        4: 1.0 / (phi ** 3),  # φ^(-3) suppression
        5: 1.0 / (phi ** 4),  # φ^(-4) suppression
    }
    
    return MorphicFieldParameters(
        d=phi,  # Scaling dimension = φ
        xi=1.0 / phi,  # Grace-Devourer coupling = φ^(-1)
        lambda_coefficients=lambda_coefficients,
        grace_amplitude=phi,  # G = φ
        devourer_amplitude=1.0 / phi,  # D = φ^(-1)
        phi_background=0.0,  # Vacuum background
        max_terms=20
    )


if __name__ == "__main__":
    # Test the morphic field equation
    print("🔬 Testing FIRM Morphic Field Equation...")
    
    # Create φ-native parameters
    params = create_phi_native_parameters()
    print(f"Parameters: d={params.d:.6f}, ξ={params.xi:.6f}, G={params.grace_amplitude:.6f}")
    
    # Initialize field equation
    field_eq = MorphicFieldEquation(params)
    
    # Find solutions
    print("\n🎯 Finding field solutions...")
    solutions = field_eq.find_multiple_solutions()
    
    print(f"Found {len(solutions)} solutions:")
    for i, sol in enumerate(solutions):
        print(f"  Solution {i+1}: φ = {sol.phi_value:.6f}")
        print(f"    Residual: {sol.field_equation_residual:.2e}")
        print(f"    Energy: {sol.energy_density:.6f}")
        
        # Analyze stability
        stability = field_eq.analyze_stability(sol.phi_value)
        print(f"    Stability: {stability['stability']}")
        
    print("\n✅ Morphic field equation test completed!")
