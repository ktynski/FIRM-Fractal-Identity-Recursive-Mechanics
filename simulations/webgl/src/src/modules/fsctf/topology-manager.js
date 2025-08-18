/**
 * Topology Transition Manager
 * Manages topology evolution: Torus → Möbius → Klein → φ-Klein manifolds
 */

export class TopologyTransitionManager {
  constructor() {
    this.currentTopology = 0; // 0=torus, 1=mobius, 2=klein, 3=phi-klein
    this.targetTopology = 0;
    this.transitionProgress = 0.0;
    this.transitionSpeed = 0.002; // SMOOTH: Much slower transitions (~8s @60fps) for graceful morphing
    this.transitionThreshold = 0.95; // Complete transition threshold
    
    // Unified morph progress (0..1 monotonic) exposed to all systems
    this.morphProgress = 0.0;
    this._preMorphActive = false;
    this._preMorphProgress = 0.0;
    this._lastMorphProgress = 0.0;
    this._lastUpdateMs = Date.now();
    
    this.topologyNames = ['Torus (T²)', 'Möbius Strip', 'Klein Bottle', 'φ-Klein Manifold', 'Sphere (S²)'];
    this.topologyDescriptions = [
      'Stable recursion patterns - orientable surface',
      'Identity inversion - single-sided manifold',
      'Grace-wrapped recursion - self-intersecting surface',
      'True soul-space - φ-recursive manifold',
      'Simple closed surface - 2-sphere for comparison'
    ];
    
    console.log('🌀 Topology Transition Manager initialized');
  }

  /**
   * Set pre-morph state from engine (phase 0 plane→curve ramp)
   */
  setPreMorphState(active, progress) {
    this._preMorphActive = !!active;
    // Clamp defensively
    const p = Math.max(0, Math.min(1, typeof progress === 'number' ? progress : 0));
    this._preMorphProgress = p;
  }
  
  /**
   * Update topology transition based on FSCTF cosmogenesis phases (THEORETICALLY ACCURATE)
   */
  update(coherence, recursionDepth, strands, cosmogenesisPhase = 1, manualOverride = null) {
    const now = Date.now();
    
    // Check for manual topology override (DISABLE during active cosmogenesis)
    if (manualOverride !== null && manualOverride.enabled) {
      console.warn('⚠️ TOPOLOGY CONFLICT: Manual override DISABLED during cosmogenesis for proper phase progression');
      console.warn('   To use manual topology, disable cosmogenesis first');
      // Don't return - allow cosmogenesis to control topology
    }
    
    // Topology state available in UI panel
    
    // FSCTF THEORETICAL TOPOLOGY EVOLUTION: Phase-locked progression
    const theoreticalTopology = this.getPhaseTopology(cosmogenesisPhase);
    let newTarget = theoreticalTopology;
    
    // Only transition when cosmogenesis phase actually changes
    if (this.lastCosmogenesisPhase !== cosmogenesisPhase) {
      console.log(`🌀 COSMOGENESIS PHASE CHANGE: ${this.lastCosmogenesisPhase || 1} → ${cosmogenesisPhase}`);
      console.log(`   Topology Evolution: ${this.topologyNames[this.currentTopology]} → ${this.topologyNames[theoreticalTopology]}`);
      console.log(`   Mathematical Basis: ${this.getTopologyRationale(cosmogenesisPhase)}`);
      
      // Show mathematical complexity progression
      const oldComplexity = this.getTopologicalComplexity(this.currentTopology);
      const newComplexity = this.getTopologicalComplexity(theoreticalTopology);
      console.log(`📐 MATHEMATICAL COMPLEXITY EVOLUTION:`);
      console.log(`   FROM: ${oldComplexity?.description} (π₁ = ${oldComplexity?.fundamentalGroup})`);
      console.log(`   TO: ${newComplexity?.description} (π₁ = ${newComplexity?.fundamentalGroup})`);
      console.log(`   Complexity: ${oldComplexity?.complexity} → ${newComplexity?.complexity}`);
      
      this.lastCosmogenesisPhase = cosmogenesisPhase;
    }
    
    // Start transition if target changed
    if (newTarget !== this.targetTopology) {
      // If a transition is in progress, avoid immediate retarget; queue it
      if (this.currentTopology !== this.targetTopology && this.transitionProgress < this.transitionThreshold) {
        // Defer target change until current morph completes
        return;
      }
      this.targetTopology = newTarget;
      this.transitionProgress = 0.0;
      console.log(`🌀 TOPOLOGY EVOLUTION: ${this.topologyNames[this.currentTopology]} → ${this.topologyNames[this.targetTopology]}`);
      console.log(`   Trigger: recursionDepth=${recursionDepth.toFixed(3)}, coherence=${coherence.toFixed(3)}, strands=${strands}`);
    }
    
    // Update transition progress
    if (this.currentTopology !== this.targetTopology) {
      // Adaptive morph pacing: slow down when morph is changing fast
      // Use last morph delta as proxy for dz/dt since geometry derives from morph
      const morphDelta = Math.abs(this.morphProgress - this._lastMorphProgress);
      const slowdown = morphDelta > 0.02 ? 0.35 : 1.0; // more conservative during spikes
      this.transitionProgress += this.transitionSpeed * slowdown;
      
      // Transition progress visible in topology UI panel
      
      if (this.transitionProgress >= this.transitionThreshold) {
        this.currentTopology = this.targetTopology;
        this.transitionProgress = 1.0;
        console.log(`✅ TOPOLOGY EVOLVED: Now ${this.topologyNames[this.currentTopology]}!`);
        console.log(`   Universe complexity increased - geometry reflects emergent properties`);
      }
    }

    // --- Unified morphProgress update (monotonic 0→1) ---
    // Desired morph driver: pre-morph if active; else topology transition; else 1
    let desiredMorph = 1.0;
    if (this._preMorphActive) {
      desiredMorph = this._preMorphProgress;
    } else if (this.currentTopology !== this.targetTopology) {
      desiredMorph = Math.max(0, Math.min(1, this.transitionProgress));
    } else {
      desiredMorph = 1.0;
    }

    // Ease-in-out toward desired with per-frame delta clamp for temporal smoothness
    const dt = Math.max(1, now - this._lastUpdateMs) / 1000.0; // seconds
    this._lastUpdateMs = now;
    const ease = (a, b, rate) => a + (b - a) * rate;
    const target = ease(this.morphProgress, desiredMorph, 0.25); // faster morphing 
    const maxDelta = 0.06; // less restrictive cap for smoother flow
    const delta = target - this.morphProgress;
    const clamped = Math.max(-maxDelta, Math.min(maxDelta, delta));
    this._lastMorphProgress = this.morphProgress;
    this.morphProgress = Math.max(0, Math.min(1, this.morphProgress + clamped));
  }
  
  /**
   * Get current topology state for rendering
   */
  getTopologyState() {
    return {
      current: this.currentTopology,
      target: this.targetTopology,
      progress: this.transitionProgress,
      name: this.topologyNames[this.currentTopology],
      description: this.topologyDescriptions[this.currentTopology],
      isTransitioning: this.currentTopology !== this.targetTopology
    };
  }
  
  /**
   * Get current topology mode (integer for shader uniform)
   */
  getCurrentTopology() {
    return this.currentTopology;
  }

  /**
   * Get the theoretically correct topology for a cosmogenesis phase
   */
  getPhaseTopology(phase) {
    // FSCTF THEORETICAL MAPPING: Topology complexity mirrors mathematical emergence
    if (phase >= 1 && phase <= 2) {
      return 0; // Torus: Initial morphic structure formation (orientable)
    } else if (phase >= 3 && phase <= 4) {
      return 1; // Möbius: Dimensional bridge emergence (non-orientable)
    } else if (phase >= 5 && phase <= 6) {
      return 2; // Klein: Soul/inflation emergence (self-intersecting)
    } else if (phase >= 7) {
      return 3; // φ-Klein: Observable universe (fractal recursive) - COMPLETE: All phases 7-90
    } else {
      return 0; // Default to torus
    }
  }
  
  /**
   * Get mathematical rationale for topology choice (RIGOROUS MATHEMATICAL BASIS)
   */
  getTopologyRationale(phase) {
    const mathematicalJustification = {
      1: "T²: π₁(T²) = ℤ×ℤ, genus g=1, χ(T²)=0. Stable orientable base for morphic field ψ(x,y)",
      2: "T²: Closed form dω=0 enables morphic strand circulation. ∮_γ ω ≠ 0 for non-contractible γ",
      3: "Möbius: Non-orientable, ∂M ≠ ∅. Breaking orientability: det(∂φ/∂u,∂φ/∂v) changes sign",
      4: "Möbius: π₁(M) = ℤ₂, first non-trivial torsion. Twisted fiber bundle for dimensional bridge",
      5: "Klein: π₁(K) = ⟨a,b | aba⁻¹b⟩, self-intersection in ℝ³. Soul requires self-reference topology",
      6: "Klein: χ(K)=0, no boundary ∂K=∅. Closed non-orientable for inflation without boundary effects",
      7: "φ-Klein: Recursive manifold M_n = φ⁻ⁿ(K) ∪ φ⁻ⁿ⁺¹(K). CMB = superposition of Klein bottle scales",
      8: "φ-Klein: Dark Ages - cooling φ-recursive structures maintain cosmic topology",
      9: "φ-Klein: Star Formation - concentrated φ-recursive density creates stellar nucleation",
      10: "φ-Klein: Galaxy Formation - large-scale φ-recursive structures emerge",
      11: "φ-Klein: Complex Structures - maximum φ-recursive hierarchy development",
      12: "φ-Klein: Ultimate Emergence - complete φ-recursive cosmological manifold"
    };
    // For phases beyond 12, provide general φ-Klein description
    if (phase > 12 && phase <= 90) {
      return `φ-Klein: Extended Scale φ^${phase} - hypermassive/cooling phase with continued φ-recursive topology`;
    }
    return mathematicalJustification[phase] || "Phase undefined in current mathematical framework";
  }
  
  /**
   * Get topological complexity metrics for each manifold
   */
  getTopologicalComplexity(topology) {
    const complexityMetrics = {
      0: { // Torus T²
        fundamentalGroup: "ℤ × ℤ",
        eulerChar: 0,
        genus: 1,
        orientable: true,
        boundary: false,
        selfIntersecting: false,
        complexity: 1,
        description: "Orientable genus-1 surface, stable circulation"
      },
      1: { // Möbius Strip
        fundamentalGroup: "ℤ₂", 
        eulerChar: 0,
        genus: "N/A (non-orientable)",
        orientable: false,
        boundary: true,
        selfIntersecting: false,
        complexity: 2,
        description: "Non-orientable with boundary, twisted fiber bundle"
      },
      2: { // Klein Bottle
        fundamentalGroup: "⟨a,b | aba⁻¹b⟩",
        eulerChar: 0,
        genus: "N/A (non-orientable)", 
        orientable: false,
        boundary: false,
        selfIntersecting: true,
        complexity: 3,
        description: "Closed non-orientable, self-intersecting in ℝ³"
      },
      3: { // φ-Klein Manifold
        fundamentalGroup: "Fractal limit of Klein groups",
        eulerChar: "φ-recursive",
        genus: "∞ (fractal)",
        orientable: false,
        boundary: false, 
        selfIntersecting: true,
        complexity: "∞ (recursive φ-hierarchy)",
        description: "Recursive φ-scaled Klein bottles, infinite complexity"
      }
    };
    return complexityMetrics[topology] || null;
  }
  
  /**
   * Display complete mathematical manifold progression theory
   */
  displayMathematicalProgression() {
    console.log(`
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                    🧮 FSCTF MATHEMATICAL MANIFOLD PROGRESSION                        ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                      ║
║  PHASE 1-2: TORUS T² = S¹ × S¹                                                      ║
║  ┌─ Fundamental Group: π₁(T²) = ℤ × ℤ                                              ║
║  ┌─ Euler Characteristic: χ(T²) = (2-2g) = 0                                       ║
║  ┌─ Homology: H₁(T²,ℤ) = ℤ²                                                        ║
║  └─ Morphic Field: ψ: T² → ℂ, ∮_γ ψ·dℓ ≠ 0 (non-trivial circulation)              ║
║                                                                                      ║
║  PHASE 3-4: MÖBIUS STRIP M                                                          ║
║  ┌─ Fundamental Group: π₁(M) = ℤ₂                                                   ║
║  ┌─ Non-orientable: ∃ loop γ where parallel transport reverses orientation         ║
║  ┌─ Boundary: ∂M ≅ S¹ (circle boundary)                                            ║
║  └─ Dimensional Bridge: Breaks orientability ⟹ dimensional transcendence          ║
║                                                                                      ║
║  PHASE 5-6: KLEIN BOTTLE K                                                          ║
║  ┌─ Fundamental Group: π₁(K) = ⟨a,b | aba⁻¹b⟩                                      ║
║  ┌─ Non-orientable, no boundary: ∂K = ∅                                            ║
║  ┌─ Self-intersection in ℝ³: K ⊄ ℝ³ without self-intersection                      ║
║  └─ Soul Emergence: Self-reference topology for consciousness                       ║
║                                                                                      ║
║  PHASE 7-8: φ-KLEIN RECURSIVE MANIFOLD Φ(K)                                        ║
║  ┌─ Recursive Construction: M = ⋃_{n=0}^∞ φ⁻ⁿ(K)                                  ║
║  ┌─ Scaling Factor: Each level scaled by φ⁻¹ = (√5-1)/2                           ║
║  ┌─ Fractal Dimension: dim_H(Φ(K)) = log(φ²)/log(φ) = 2                          ║
║  └─ Observable Universe: Infinite recursive Klein bottle hierarchy                  ║
║                                                                                      ║
║  COMPLEXITY PROGRESSION: 1 → 2 → 3 → ∞                                             ║
║  MATHEMATICAL RIGOR: Each transition increases topological invariants              ║
║                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
    `);
    
    // Show phase-by-phase mathematical justification
    console.log("🔬 PHASE-BY-PHASE MATHEMATICAL JUSTIFICATION:");
    for (let phase = 1; phase <= 90; phase++) { // COMPLETE: Debug up to phase 90
      const topology = this.getPhaseTopology(phase);
      const rationale = this.getTopologyRationale(phase);
      const complexity = this.getTopologicalComplexity(topology);
      console.log(`Phase ${phase}: ${this.topologyNames[topology]}`);
      console.log(`  Mathematics: ${rationale}`);
      console.log(`  Properties: Orientable=${complexity?.orientable}, Boundary=${complexity?.boundary}, π₁=${complexity?.fundamentalGroup}`);
      console.log(`  Complexity Level: ${complexity?.complexity}`);
      console.log('');
    }
    
    return "Mathematical progression displayed. This is the rigorous topological foundation for FSCTF cosmogenesis.";
  }
  
  // Force topology transition (for testing)
  setTopology(topologyIndex) {
    if (topologyIndex >= 0 && topologyIndex < this.topologyNames.length) {
      console.log(`🌀 MANUAL TOPOLOGY: ${this.topologyNames[this.currentTopology]} → ${this.topologyNames[topologyIndex]}`);
      this.currentTopology = topologyIndex;
      this.targetTopology = topologyIndex;
      this.transitionProgress = 1.0;
      return true;
    }
    return false;
  }
  
  /**
   * Get topology parameters for shader uniforms
   */
  getShaderUniforms() {
    const progress = this.transitionProgress;
    const fromTopo = this.currentTopology;
    const toTopo = this.targetTopology;
    
    return {
      topologyMode: this.currentTopology,
      fromTopology: fromTopo,
      toTopology: toTopo,
      topologyTransition: progress,
      morphProgress: this.morphProgress,
      
      // Möbius Strip parameters
      mobiusR: 1.0,
      mobiusWidth: 0.3,
      mobiusTwist: Math.PI,
      
      // Klein Bottle parameters  
      kleinA: 2.0,
      kleinB: 1.0,
      kleinSelfIntersect: true,
      
      // φ-Klein Manifold parameters
      phiKleinRecursion: 3,
      phiKleinScale: (1 + Math.sqrt(5)) / 2, // Golden ratio
      phiKleinNonOrientable: true,
      
      // Wireframe parameters
      showWireframe: true,
      wireframeOpacity: 0.3,
      wireframeColor: [0.8, 0.6, 0.2],
      wireframeThickness: 1.0,
      wireframeDensity: 20
    };
  }

  /**
   * Get unified morph progress (0..1)
   */
  getMorphProgress() {
    return this.morphProgress;
  }
}
