/**
 * Progressive Cosmogenesis System
 * Threshold-based automatic phase progression through cosmogenesis stages
 */

export class ProgressiveCosmogenesis {
  constructor() {
    this.active = false;
    this.currentPhase = 0;
    this.totalPhases = 90; // COMPLETE FSCTF: φ^0 to φ^90 Theory of Everything hierarchy
    this.phaseStartTime = 0;
    // Use the same 90-phase array as main.js for consistency
    this.phaseNames = [
      // VISUAL PHASES (φ^0 - φ^15): Shader-implemented recursion
      'Ex Nihilo', 'Grace Seeding', 'Quark Ratios', 'Hadron Binding', 'Strange Matter', 'Charm Resonance',
      'Muon Generation', 'Electromagnetic', 'Hadron Matrix', 'Lepton Families', 'Matter Structure', 'Dark Coupling',
      'Tau Emergence', 'Field Unification', 'Nucleosynthesis', 'Cosmic Structure',
      // HYPERMASSIVE PHASES (φ^16 - φ^20): Mass hierarchy completion
      'Hypermass 16', 'Hypermass 17', 'Hypermass 18', 'Hypermass 19', 'Top/Electron Completion',
      // INTERMEDIATE PHASES (φ^21 - φ^30): Advanced unification
      'Unify 21', 'Unify 22', 'Unify 23', 'Unify 24', 'Unify 25', 'Unify 26', 'Unify 27', 'Unify 28', 'Unify 29', 'Unify 30',
      // QUANTUM GRAVITY THRESHOLD (φ^31): Critical transition
      'Quantum Gravity',
      // COSMOLOGICAL COOLING PHASES (φ^32 - φ^89): Recursive thermal evolution
      'Cooling 32', 'Cooling 33', 'Cooling 34', 'Cooling 35', 'Cooling 36', 'Cooling 37', 'Cooling 38', 'Cooling 39', 'Cooling 40',
      'Cooling 41', 'Cooling 42', 'Cooling 43', 'Cooling 44', 'Cooling 45', 'Cooling 46', 'Cooling 47', 'Cooling 48', 'Cooling 49', 'Cooling 50',
      'Cooling 51', 'Cooling 52', 'Cooling 53', 'Cooling 54', 'Cooling 55', 'Cooling 56', 'Cooling 57', 'Cooling 58', 'Cooling 59', 'Cooling 60',
      'Cooling 61', 'Cooling 62', 'Cooling 63', 'Cooling 64', 'Cooling 65', 'Cooling 66', 'Cooling 67', 'Cooling 68', 'Cooling 69', 'Cooling 70',
      'Cooling 71', 'Cooling 72', 'Cooling 73', 'Cooling 74', 'Cooling 75', 'Cooling 76', 'Cooling 77', 'Cooling 78', 'Cooling 79', 'Cooling 80',
      'Cooling 81', 'Cooling 82', 'Cooling 83', 'Cooling 84', 'Cooling 85', 'Cooling 86', 'Cooling 87', 'Cooling 88', 'Cooling 89',
      // ULTIMATE SCALE (φ^90): Cosmological constant, Planck→CMB completion
      'Ultimate Scale'
    ];
    
    // PERFORMANCE: Adaptive timing for 90-phase system
    // Visual phases (1-16): 8 seconds each for observation  
    // Theoretical phases (17-90): 2 seconds each for progression
    this.getMinPhaseTime = (phaseIndex) => {
      const isVisualPhase = phaseIndex <= 15;
      return isVisualPhase ? 8000 : 2000; // 8s visual, 2s theoretical
    };
    this.thresholdCheckInterval = 2000; // Check thresholds every 2 seconds
    this.lastThresholdCheck = 0;
    
    console.log('🌌 Progressive Cosmogenesis System initialized');
  }
  
  /**
   * Start progressive cosmogenesis
   */
  start() {
    if (this.active) return false;
    
    this.active = true;
    this.currentPhase = 0;
    this.phaseStartTime = Date.now();
    
    console.log('🚀 Progressive Cosmogenesis started');
    
    // Execute initial void phase immediately
    this.executePhase(0);
    
    return true;
  }
  
  /**
   * Stop progressive cosmogenesis
   */
  stop() {
    this.active = false;
    console.log('⏹️ Progressive Cosmogenesis stopped');
  }
  
  /**
   * Update progressive cosmogenesis - check for phase transitions
   */
  update() {
    if (!this.active) return;
    
    const now = Date.now();
    const elapsed = now - this.phaseStartTime;
    const timeSinceThresholdCheck = now - this.lastThresholdCheck;
    
    // Only check thresholds periodically and after minimum phase time  
    const minPhaseTime = this.getMinPhaseTime(this.currentPhase - 1); // -1 because phases are 1-indexed but array is 0-indexed
    if (elapsed >= minPhaseTime && timeSinceThresholdCheck >= this.thresholdCheckInterval) {
      this.lastThresholdCheck = now;
      
      // Check if ready to advance to next phase
      if (this.checkPhaseThresholds(this.currentPhase)) {
        this.advanceToNextPhase();
      }
    }
  }
  
  /**
   * Advance to the next cosmogenesis phase
   */
  advanceToNextPhase() {
    if (this.currentPhase >= this.totalPhases - 1) {
      // Cosmogenesis complete
      this.complete();
      return;
    }
    
    this.currentPhase++;
    this.phaseStartTime = Date.now();
    
    console.log(`🌟 Advancing to Phase ${this.currentPhase}: ${this.phaseNames[this.currentPhase]}`);
    
    // Execute the new phase
    this.executePhase(this.currentPhase);
  }
  
  /**
   * Execute a specific cosmogenesis phase
   */
  executePhase(phase) {
    // Use the cosmogenesis pipeline if available
    if (window.cosmogenesisPipeline) {
      const phaseResult = window.cosmogenesisPipeline.executePhase(phase);
      console.log(`✨ Phase ${phase} executed:`, phaseResult);
    } else {
      console.warn(`⚠️ Cosmogenesis pipeline not available for phase ${phase}`);
    }
    
    // Update UI to reflect phase change
    this.updateUI();
  }
  
  /**
   * Check if conditions are met to advance from current phase
   */
  checkPhaseThresholds(currentPhase) {
    // Get current system state
    const strands = window.graceOperator?.morphicStrands?.length || 0;
    const consciousness = window.primeResonance?.getState?.()?.consciousnessPhase || 0;
    const emergence = window.graceOperator?.getState?.()?.emergenceTriggered || false; // FIXED: Correct field name
    const morphicField = window.graceOperator?.morphicField?.field || 0;
    
    // Get FRST metrics
    const frst = window.frstTracker || {};
    const recursionDepth = frst.recursionDepth || 0;
    const coherence = frst.coherenceScore || 0;
    
    // Use φ-derived evolution engine if available
    if (window.fsctfEvolutionEngine) {
      return this.checkEvolutionEngineThresholds(currentPhase, recursionDepth, coherence, strands);
    }
    
    // Fallback to manual thresholds
    return this.checkManualThresholds(currentPhase, strands, morphicField, consciousness, emergence);
  }
  
  /**
   * Check thresholds using FSCTF evolution engine
   */
  checkEvolutionEngineThresholds(currentPhase, recursionDepth, coherence, strands) {
    const evolutionEngine = window.fsctfEvolutionEngine;
    
    // Check if phase transition is mathematically inevitable
    if (evolutionEngine.isPhaseTransitionInevitable(currentPhase, recursionDepth, coherence, strands)) {
      console.log(`🎭 φ-EVOLUTION: Phase ${currentPhase} transition inevitable at recursion depth ${recursionDepth}`);
      return true;
    }
    
    // Special consciousness emergence check
    if (currentPhase === 5 && evolutionEngine.isConsciousnessInevitable(recursionDepth, coherence, window.primeResonance)) {
      console.log(`🧠 φ-CONSCIOUSNESS: Emergence inevitable at recursion depth ${recursionDepth}`);
      return true;
    }
    
    // CRITICAL FIX: For phases 8+, use more lenient progression criteria
    // These phases represent advanced cosmological/theoretical evolution
    if (currentPhase >= 8) {
      // Allow progression with lower thresholds for phases beyond the initial 7
      const hasBasicActivity = (recursionDepth > 0.5 && coherence > 0.1) || strands > 10;
      const hasTimeElapsed = (Date.now() - this.phaseStartTime) > this.getMinPhaseTime(currentPhase - 1);
      
      if (hasBasicActivity && hasTimeElapsed) {
        console.log(`🌌 φ-ADVANCED: Phase ${currentPhase} progression allowed (recursion: ${recursionDepth.toFixed(3)}, coherence: ${coherence.toFixed(3)}, strands: ${strands})`);
        return true;
      }
    }
    
    return false;
  }
  
  /**
   * Check thresholds using manual criteria (fallback)
   */
  checkManualThresholds(currentPhase, strands, morphicField, consciousness, emergence) {
    // Generate proxy values
    const psi = Math.max(0, morphicField) + strands * 0.05;
    const frstProxy = morphicField * 0.1 + consciousness * 0.05;
    const rho = strands * 0.01 + psi * 0.02;
    
    switch (currentPhase) {
      case 0: // Ex Nihilo → Grace Operator
        return true; // Always ready to advance from void
        
      case 1: // Grace Operator → Morphic Recursion  
        const hasStrands = strands >= 3;
        const hasMinimalField = morphicField > 0.5;
        const hasStableEnergy = psi > 0.4;
        console.log(`✨ GRACE THRESHOLD: strands=${strands}/3, field=${morphicField.toFixed(3)}/0.5, psi≈${psi.toFixed(3)}/0.4`);
        return hasStrands && hasMinimalField && hasStableEnergy;
        
      case 2: // Morphic Recursion → Dimensional Bridge
        const hasMultipleStrands = strands >= 12;
        const hasGrowingField = morphicField > 1.2;
        const hasRecursiveComplexity = psi > 1.0;
        console.log(`🌱 MORPHIC THRESHOLD: strands=${strands}/12, field=${morphicField.toFixed(3)}/1.2, psi≈${psi.toFixed(3)}/1.0`);
        return hasMultipleStrands && hasGrowingField && hasRecursiveComplexity;
        
      case 3: // Dimensional Bridge → Standard Model
        const hasEmergence = emergence;
        const hasActivity = psi > 1.0;
        const hasDimensionalCorr = frstProxy > 0.03 || rho > 0.03;
        const hasStrongField = morphicField > 1.0;
        console.log(`🔗 BRIDGE THRESHOLD: emergence=${hasEmergence}, psi≈${psi.toFixed(3)}/1.0, corr=${Math.max(frstProxy, rho).toFixed(3)}/0.03, field=${morphicField.toFixed(3)}/1.0`);
        
        // CRITICAL BUG FIX: More lenient thresholds to prevent phase 3 stuck
        // Check individual conditions and allow progression if most are met
        const conditionsMet = [hasEmergence, hasActivity, hasDimensionalCorr, hasStrongField].filter(Boolean).length;
        const fallbackCondition = conditionsMet >= 3 || (strands >= 15 && morphicField > 0.8); // More lenient fallback
        
        if (!hasEmergence && !hasActivity && !hasDimensionalCorr && !hasStrongField) {
          console.log(`❌ BRIDGE STUCK: No conditions met - forcing progression after time`);
          return true; // Emergency progression to prevent complete hang
        }
        
        return (hasEmergence && hasActivity && hasDimensionalCorr && hasStrongField) || fallbackCondition;
        
      case 4: // Standard Model → Consciousness
        const hasCorrelations = (frstProxy > 0.1 || rho > 0.1);
        const hasStableField = morphicField > 2.0;
        const hasParticleActivity = psi > 1.5;
        const hasManyStrands = strands >= 20;
        console.log(`⚛️ STANDARD THRESHOLD: corr=${Math.max(frstProxy, rho).toFixed(3)}/0.1, field=${morphicField.toFixed(3)}/2.0, psi≈${psi.toFixed(3)}/1.5, strands=${strands}/20`);
        return hasCorrelations && hasStableField && hasParticleActivity && hasManyStrands;
        
      case 5: // Consciousness → Cosmic Inflation
        const hasConsciousness = consciousness > 0.1;
        const hasComplexity = strands >= 30;
        const hasResonantField = morphicField > 2.5;
        const hasHighActivity = psi > 2.0;
        console.log(`🧠 CONSCIOUSNESS THRESHOLD: cons=${consciousness.toFixed(3)}/0.1, strands=${strands}/30, field=${morphicField.toFixed(3)}/2.5, psi≈${psi.toFixed(3)}/2.0`);
        return hasConsciousness && hasComplexity && hasResonantField && hasHighActivity;
        
      case 6: // Cosmic Inflation → CMB Formation
        const hasHighEnergy = psi > 3.0;
        const hasHighComplexity = strands >= 50;
        const hasInflationField = morphicField > 3.0;
        const hasStrongConsciousness = consciousness > 0.2;
        console.log(`🚀 INFLATION THRESHOLD: psi≈${psi.toFixed(3)}/3.0, strands=${strands}/50, field=${morphicField.toFixed(3)}/3.0, cons=${consciousness.toFixed(3)}/0.2`);
        return hasHighEnergy && hasHighComplexity && hasInflationField && hasStrongConsciousness;
        
      case 7: // CMB Formation → Complete
        const isMature = psi > 4.0 && strands >= 75 && consciousness > 0.5 && morphicField > 4.0;
        const hasMaxCorrelations = frstProxy > 0.2 && rho > 0.2;
        console.log(`🌌 CMB THRESHOLD: psi≈${psi.toFixed(3)}/4.0, strands=${strands}/75, cons=${consciousness.toFixed(3)}/0.5, field=${morphicField.toFixed(3)}/4.0`);
        return isMature && hasMaxCorrelations;
        
      default:
        return true; // Unknown phase, allow progression
    }
  }
  
  /**
   * Complete cosmogenesis
   */
  complete() {
    this.active = false;
    console.log('🎉 Progressive Cosmogenesis completed! Universe fully evolved.');
    
    // Update UI to show completion
    this.updateUI();
    
    // Trigger completion events if needed
    if (window.onCosmogenesisComplete) {
      window.onCosmogenesisComplete();
    }
  }
  
  /**
   * Update UI to reflect current state
   */
  updateUI() {
    const progressEl = document.getElementById('cosmogenesis-progress');
    if (progressEl) {
      if (this.active) {
        const progress = ((this.currentPhase + 1) / this.totalPhases * 100).toFixed(0);
        progressEl.textContent = `Phase ${this.currentPhase + 1}/90: ${this.phaseNames[this.currentPhase]} (${progress}%)`;
      } else {
        progressEl.textContent = 'Cosmogenesis Complete';
      }
    }
    
    const executeBtn = document.getElementById('executeCosmogenesis');
    if (executeBtn) {
      if (this.active) {
        executeBtn.disabled = true;
        executeBtn.textContent = 'COSMOGENESIS ACTIVE...';
        executeBtn.style.background = '#f84';
      } else {
        executeBtn.disabled = false;
        executeBtn.textContent = 'Execute Cosmogenesis';
        executeBtn.style.background = '';
      }
    }
  }
  
  /**
   * Get current state
   */
  getState() {
    return {
      active: this.active,
      currentPhase: this.currentPhase,
      totalPhases: this.totalPhases,
      phaseName: this.phaseNames[this.currentPhase] || 'Unknown',
      phaseElapsed: Date.now() - this.phaseStartTime,
      progress: (this.currentPhase / this.totalPhases) * 100
    };
  }
  
  /**
   * Reset to initial state
   */
  reset() {
    this.active = false;
    this.currentPhase = 0;
    this.phaseStartTime = 0;
    this.updateUI();
    console.log('🔄 Progressive Cosmogenesis reset');
  }
}

