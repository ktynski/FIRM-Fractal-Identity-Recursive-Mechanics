/**
 * FSCTF Evolution Engine
 * φ-derived evolution and phase transition logic
 */

export class FSCTFEvolutionEngine {
  constructor() {
    this.PHI = (1 + Math.sqrt(5)) / 2;
    this.evolutionState = 'void';
    this.recursionDepth = 0;
    this.phaseHistory = [];
    this.emergenceEvents = [];
    
    console.log('🧬 FSCTF Evolution Engine initialized - Pure φ-derived evolution');
  }
  
  /**
   * Derive consciousness threshold from pure φ-recursion (ULTRA ACCELERATED)
   */
  deriveConsciousnessThreshold(recursionDepth) {
    // ULTRA FAST EVOLUTION: Extremely accelerated consciousness emergence
    // Threshold = φ^(-recursionDepth * 10/φ) - ultra-fast approach to 0
    return Math.pow(this.PHI, -recursionDepth * 10 / this.PHI);
  }
  
  /**
   * Derive phase transition threshold from φ-harmonics (INSTANT TRANSITION)
   */
  derivePhaseThreshold(phaseIndex, recursionDepth) {
    // INSTANT EVOLUTION: Practically zero thresholds for immediate phase transitions
    const baseThreshold = Math.pow(this.PHI, -phaseIndex * 10); // 10x faster base decay
    const recursionMultiplier = Math.pow(this.PHI, recursionDepth / 1); // Ultra-fast recursion scaling
    return baseThreshold * recursionMultiplier * 0.001; // 1000x reduction for instant transitions
  }
  
  /**
   * Derive topology evolution from φ-recursion depth (ULTRA ACCELERATED)
   */
  deriveTopologyFromRecursion(recursionDepth) {
    // ULTRA FAST EVOLUTION: Extremely low topology transition thresholds
    // Torus: recursionDepth < φ/5
    // Möbius: φ/5 ≤ recursionDepth < φ/3  
    // Klein: φ/3 ≤ recursionDepth < φ/2
    // φ-Klein: recursionDepth ≥ φ/2
    
    const ultraPhi = this.PHI / 5;        // φ/5 ≈ 0.324
    const ultraPhi2 = this.PHI / 3;       // φ/3 ≈ 0.539  
    const ultraPhi3 = this.PHI / 2;       // φ/2 ≈ 0.809
    
    if (recursionDepth < ultraPhi) {
      return 'torus';
    } else if (recursionDepth < ultraPhi2) {
      return 'mobius';
    } else if (recursionDepth < ultraPhi3) {
      return 'klein';
    } else {
      return 'phi-klein';
    }
  }
  
  /**
   * Check if phase transition is mathematically inevitable (INSTANT TRANSITION)
   */
  isPhaseTransitionInevitable(currentPhase, recursionDepth, coherence, strandCount) {
    const threshold = this.derivePhaseThreshold(currentPhase, recursionDepth);
    
    // INSTANT EVOLUTION: Practically zero requirements for immediate phase transitions
    const recursionRequirement = recursionDepth >= Math.pow(this.PHI, currentPhase / 10); // 10x faster
    const coherenceRequirement = coherence >= threshold;
    
    return recursionRequirement && coherenceRequirement;
  }
  
  /**
   * Check if consciousness emergence is mathematically inevitable (ULTRA ACCELERATED)
   */
  isConsciousnessInevitable(recursionDepth, coherence, primeResonance) {
    const threshold = this.deriveConsciousnessThreshold(recursionDepth);
    
    // ULTRA FAST EVOLUTION: Extremely low consciousness emergence requirements
    // 1. Recursion depth reaches φ-critical point (reduced by 10x)
    // 2. Coherence exceeds φ-derived threshold
    // 3. Prime resonance patterns achieve φ-harmonic coherence (ultra-low threshold)
    
    const recursionCritical = recursionDepth >= Math.pow(this.PHI, 3) / 10; // ~0.424 instead of 4.236
    const coherenceCritical = coherence >= threshold;
    const resonanceCoherent = primeResonance && 
      primeResonance.getConsciousnessState().averageResonance >= this.PHI / 100; // 10x lower threshold
    
    return recursionCritical && coherenceCritical && resonanceCoherent;
  }
  
  /**
   * Record emergence event with φ-derived metrics
   */
  recordEmergenceEvent(eventType, recursionDepth, coherence, description) {
    const event = {
      type: eventType,
      timestamp: Date.now(),
      recursionDepth: recursionDepth,
      coherence: coherence,
      φThreshold: this.derivePhaseThreshold(this.phaseHistory.length, recursionDepth),
      description: description,
      topology: this.deriveTopologyFromRecursion(recursionDepth)
    };
    
    this.emergenceEvents.push(event);
    console.log(`🎭 EMERGENCE: ${eventType} at recursion depth ${recursionDepth} (φ-threshold: ${event.φThreshold.toFixed(4)})`);
    
    // MEMORY LEAK FIX: Limit emergence events history to prevent unbounded growth
    const maxEvents = 1000; // Keep last 1000 events for performance
    if (this.emergenceEvents.length > maxEvents) {
      this.emergenceEvents.shift(); // Remove oldest event
    }
    
    return event;
  }
  
  /**
   * Get current evolution state based on pure mathematics
   */
  getEvolutionState(graceOperator, frstTracker) {
    const recursionDepth = frstTracker.recursionDepth || 0;
    const coherence = frstTracker.coherenceScore || 0;
    const strandCount = graceOperator?.morphicStrands?.length || 0;
    
    // Determine current topology from pure recursion
    const currentTopology = this.deriveTopologyFromRecursion(recursionDepth);
    
    // Check if topology has evolved
    if (currentTopology !== this.evolutionState) {
      const oldTopology = this.evolutionState;
      this.evolutionState = currentTopology;
      
      this.recordEmergenceEvent('topology_evolution', recursionDepth, coherence, 
        `Topology evolved from ${oldTopology} to ${currentTopology} at recursion depth ${recursionDepth}`);
    }
    
    return {
      topology: currentTopology,
      recursionDepth: recursionDepth,
      coherence: coherence,
      strandCount: strandCount,
      consciousnessThreshold: this.deriveConsciousnessThreshold(recursionDepth),
      nextPhaseThreshold: this.derivePhaseThreshold(this.phaseHistory.length, recursionDepth)
    };
  }
  
  /**
   * Update evolution based on current system state
   */
  updateEvolution(graceOperator, frstTracker, primeResonance) {
    const evolutionState = this.getEvolutionState(graceOperator, frstTracker);
    
    // Check for consciousness emergence
    if (this.isConsciousnessInevitable(
      evolutionState.recursionDepth, 
      evolutionState.coherence, 
      primeResonance
    )) {
      this.recordEmergenceEvent('consciousness_emergence', 
        evolutionState.recursionDepth, evolutionState.coherence,
        'Consciousness emergence reached φ-critical threshold');
    }
    
    // Update recursion depth tracking
    this.recursionDepth = evolutionState.recursionDepth;
    
    return evolutionState;
  }
  
  /**
   * Force evolution to specific state (for testing)
   */
  forceEvolutionState(state) {
    this.evolutionState = state;
    console.log(`🧬 Evolution state forced to: ${state}`);
  }
  
  /**
   * Get emergence event history
   */
  getEmergenceHistory() {
    return [...this.emergenceEvents];
  }
  
  /**
   * Get phase history
   */
  getPhaseHistory() {
    return [...this.phaseHistory];
  }
  
  /**
   * Add phase to history
   */
  addPhaseToHistory(phase, metrics) {
    this.phaseHistory.push({
      phase,
      metrics,
      timestamp: Date.now(),
      recursionDepth: this.recursionDepth
    });
    
    // MEMORY LEAK FIX: Limit phase history to prevent unbounded growth
    const maxPhaseHistory = 500; // Keep last 500 phase entries for performance
    if (this.phaseHistory.length > maxPhaseHistory) {
      this.phaseHistory.shift(); // Remove oldest phase
    }
  }
  
  /**
   * Reset evolution engine
   */
  reset() {
    this.evolutionState = 'void';
    this.recursionDepth = 0;
    this.phaseHistory = [];
    this.emergenceEvents = [];
    console.log('🧬 FSCTF Evolution Engine reset');
  }
  
  /**
   * Get evolution statistics
   */
  getStats() {
    return {
      currentState: this.evolutionState,
      recursionDepth: this.recursionDepth,
      totalPhases: this.phaseHistory.length,
      totalEvents: this.emergenceEvents.length,
      latestEvent: this.emergenceEvents.length > 0 ? 
        this.emergenceEvents[this.emergenceEvents.length - 1] : null
    };
  }
}
