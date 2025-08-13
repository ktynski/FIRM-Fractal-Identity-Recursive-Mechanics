φ-Recursion Convergence – Machine-Checkable Skeleton

Scope
- Formalize convergence of x_{n+1} = 1 + 1/x_n to φ = (1+√5)/2 for x_0 > 0.

Mapping (Code → Lemma/Theorem)
- foundation/operators/phi_recursion.py
  - PhiRecursion.recursion_function → f(x) = 1 + 1/x definition
  - PhiRecursion.prove_convergence → Convergence proof outline
  - verify_phi_properties → Algebraic identities for φ

Intended Formal Artifacts
- phi_recursion/Defs.lean: Definition of f and fixed point φ
- phi_recursion/Convergence.lean: |f'(φ)| = φ⁻² < 1 → contraction near φ
- phi_recursion/Global.lean: Monotone/oscillatory convergence for x_0 > 0
- phi_recursion/Main.lean: Theorem ConvergesToPhi

Assumptions
- Real analysis library with fixed-point and derivative rules

Verification Plan
1) Show φ solves φ = 1 + 1/φ
2) Show |f'(φ)| = φ⁻² < 1 ⇒ local contraction
3) Show sequence remains in domain and approaches φ
4) Bound error: |x_n - φ| = O((φ⁻²)^n)
