/**
 * Cosmogenesis Functions
 * Standalone functions for cosmogenesis control and phase management
 */

/**
 * Start progressive cosmogenesis sequence
 */
export function startProgressiveCosmogenesis() {
  console.log('🔍 DEBUG: startProgressiveCosmogenesis called');
  
  const progressiveCosmogenesis = window.progressiveCosmogenesis;
  
  console.log('🔍 DEBUG: window.progressiveCosmogenesis =', progressiveCosmogenesis);
  console.log('🔍 DEBUG: window.simulationCore =', window.simulationCore);
  
  if (!progressiveCosmogenesis) {
    console.error('❌ Progressive cosmogenesis system not initialized');
    console.log('🔍 DEBUG: Available window properties:', Object.keys(window).filter(k => k.includes('cosmos') || k.includes('progress') || k.includes('simulation')));
    return;
  }
  
  if (progressiveCosmogenesis.active) {
    console.log('🚀 Progressive cosmogenesis already running');
    return;
  }
  
  console.log('🚀 STARTING Progressive Cosmogenesis');
  progressiveCosmogenesis.active = true;
  progressiveCosmogenesis.currentPhase = 0;
  progressiveCosmogenesis.phaseStartTime = Date.now();
  console.log('✅ DEBUG: Window cosmogenesis state set:', progressiveCosmogenesis);

  // CRITICAL FIX: Also start the FSCTF engine to trigger Grace Operator emergence
  // Wait a moment for simulationCore to be fully initialized
  setTimeout(() => {
    console.log('🔍 DEBUG: Delayed simulationCore check:', window.simulationCore);
    if (window.simulationCore && window.simulationCore.startCosmogenesis) {
      console.log('🌟 Starting FSCTF engine for Grace Operator emergence...');
      window.simulationCore.startCosmogenesis();
      console.log('✅ FSCTF engine started successfully');
    } else if (window.simulationCore) {
      console.error('❌ CRITICAL: simulationCore found but startCosmogenesis method missing!');
      console.log('🔍 DEBUG: Available simulation methods:', Object.keys(window.simulationCore));
    } else {
      console.error('❌ CRITICAL: simulationCore not available globally!');
      console.log('🔍 DEBUG: Available global properties with "simulation":', 
        Object.keys(window).filter(k => k.toLowerCase().includes('simulation')));
    }
  }, 100);
  
  // Also try immediate call in case it's available
  if (window.simulationCore && window.simulationCore.startCosmogenesis) {
    console.log('🌟 Starting FSCTF engine for Grace Operator emergence (immediate)...');
    window.simulationCore.startCosmogenesis();
    console.log('✅ FSCTF engine started successfully (immediate)');
  }
  
  // SKIP VOID PHASE: Start directly with visible particles
  // Skip void phase for immediate visualization
  // cosmogenesisPipeline.executePhase(0); // Execute Phase 0: Ex Nihilo (Void) - DISABLED
  
  // ADVANCE TO PHASE 1 SETUP: Void is instant, prepare for Grace Operator
  progressiveCosmogenesis.currentPhase = 1; // Move to Phase 1 (Grace Operator)
  progressiveCosmogenesis.phaseStartTime = Date.now(); // Reset timer for Grace phase
  
  // FORCE IMMEDIATE VISUAL UPDATE: Ensure black screen appears instantly
  if (window.updateCosmogenesisUI) {
    window.updateCosmogenesisUI();
  }
  
  // Update button state
  const executeCosmogenesisBtn = document.getElementById('executeCosmogenesis');
  if (executeCosmogenesisBtn) {
    executeCosmogenesisBtn.disabled = true;
    executeCosmogenesisBtn.textContent = 'COSMOGENESIS ACTIVE...';
    executeCosmogenesisBtn.style.background = '#f84';
    console.log('✅ DEBUG: Button state updated to active');
  } else {
    console.error('❌ DEBUG: Button not found when trying to update state');
  }
  
  // CRITICAL FIX: Also trigger the class-based ProgressiveCosmogenesis if available
  setTimeout(() => {
    console.log('🔍 DEBUG: Delayed fsctfEngine check...');
    const fsctfEngine = window.simulationCore?.fsctfEngine;
    console.log('🔍 DEBUG: fsctfEngine =', fsctfEngine);
    
    if (fsctfEngine?.progressiveCosmogenesis) {
      console.log('🌟 Starting class-based ProgressiveCosmogenesis...');
      try {
        // Start the ProgressiveCosmogenesis class using its start() method
        const started = fsctfEngine.progressiveCosmogenesis.start();
        console.log('🔍 DEBUG: ProgressiveCosmogenesis.start() returned:', started);
        console.log('✅ DEBUG: Class-based ProgressiveCosmogenesis activated');
      } catch (error) {
        console.error('❌ ERROR starting class-based ProgressiveCosmogenesis:', error);
      }
    } else {
      console.log('🔍 DEBUG: Class-based ProgressiveCosmogenesis not found after delay');
      console.log('🔍 DEBUG: Available fsctfEngine properties:', fsctfEngine ? Object.keys(fsctfEngine) : 'none');
    }
  }, 150);
  
  // Reset pipeline state
  if (window.cosmogenesisPipeline) {
    window.cosmogenesisPipeline.reset();
  }
  
  if (window.updateCosmogenesisUI) {
    window.updateCosmogenesisUI();
  }
}

/**
 * Check if conditions are met to advance to next cosmogenesis phase
 */
export function checkPhaseThresholds(currentPhase) {
  // Get current system state
  const strands = (window.graceOperator && window.graceOperator.morphicStrands) ? 
    window.graceOperator.morphicStrands.length : 0;
  const consciousness = (window.primeResonance && window.primeResonance.getConsciousnessState) ? 
    window.primeResonance.getConsciousnessState().averageResonance : 0;
  const emergence = (window.graceOperator && window.graceOperator.getState) ? 
    window.graceOperator.getState().emergenceTriggered : false; // FIXED: Use correct method and field name
  const morphicField = (window.graceOperator && window.graceOperator.morphicField) ? 
    window.graceOperator.morphicField.field : 0;
  
  // Get FRST metrics for φ-derived evolution
  const frst = window.frstTracker || {};
  const recursionDepth = frst.recursionDepth || 0;
  const coherence = frst.coherenceScore || 0;
  
  // Use φ-derived evolution engine if available
  if (window.fsctfEvolutionEngine) {
    const evolutionState = window.fsctfEvolutionEngine.getEvolutionState(window.graceOperator, frst);
    
    // Phase transition occurs when mathematically inevitable
    if (window.fsctfEvolutionEngine.isPhaseTransitionInevitable(currentPhase, recursionDepth, coherence, strands)) {
      console.log(`🎭 φ-EVOLUTION: Phase ${currentPhase} transition inevitable at recursion depth ${recursionDepth} (coherence: ${coherence.toFixed(4)})`);
      return true;
    }
    
    // Consciousness emergence when mathematically inevitable
    if (currentPhase === 5 && window.fsctfEvolutionEngine.isConsciousnessInevitable(recursionDepth, coherence, window.primeResonance)) {
      console.log(`🧠 φ-CONSCIOUSNESS: Emergence inevitable at recursion depth ${recursionDepth} (coherence: ${coherence.toFixed(4)})`);
      return true;
    }
    
    // Use existing evolutionState from above
    const threshold = window.fsctfEvolutionEngine.derivePhaseThreshold(currentPhase, recursionDepth);
    const recursionReq = Math.pow(window.fsctfEvolutionEngine.PHI, currentPhase / 10);
    
    console.log(`   Recursion: ${recursionDepth.toFixed(3)} (need ≥ ${recursionReq.toFixed(3)}) ${recursionDepth >= recursionReq ? '✅' : '❌'}`);
    console.log(`   Coherence: ${coherence.toFixed(6)} (need ≥ ${threshold.toFixed(8)}) ${coherence >= threshold ? '✅' : '❌'}`);
    console.log(`   Strands: ${strands}, Topology: ${evolutionState.topology}`);
    return false;
  }
  
  // Fallback to original thresholds if evolution engine not available
  console.log('⚠️ φ-Evolution engine not available, using fallback thresholds');
  
  // Internal Ψ proxy (no readback): field + strand contribution, clamped
  const psi = Math.max(0, (morphicField || 0)) + strands * 0.05;
  
  // Generate proxy values based on current FSCTF state for progression
  const frstProxy = morphicField * 0.1 + consciousness * 0.05;
  const rho = strands * 0.01 + psi * 0.02;
  
  return checkManualThresholds(currentPhase, strands, morphicField, consciousness, emergence, psi, frstProxy, rho);
}

/**
 * Check manual thresholds (fallback implementation)
 */
function checkManualThresholds(currentPhase, strands, morphicField, consciousness, emergence, psi, frstProxy, rho) {
  switch (currentPhase) {
    case 0: // Ex Nihilo → Grace Operator
      // Void phase advances immediately after execution (already established absolute void)
      const isVoid = window.params?.graceAmp === 0 && window.params?.fieldScale === 0 && window.params?.burstAmp === 0;
      console.log(`🌑 VOID THRESHOLD: isVoid=${isVoid}, graceAmp=${window.params?.graceAmp} - VOID READY TO ADVANCE`);
      return true; // Always ready to advance from void (void is instant)
      
    case 1: // Grace Operator → Morphic Recursion  
      // Requires: Substantial morphic strand creation and strong field emergence
      const hasStrands = strands >= 3; // Reduced threshold for unleashed complexity
      const hasMinimalField = morphicField > 0.5; // Lower field threshold for high complexity
      const hasStableEnergy = psi > 0.4; // Lower energy threshold for unleashed parameters
      console.log(`✨ GRACE THRESHOLD: strands=${strands}/3, field=${morphicField.toFixed(3)}/0.5, psi≈${psi.toFixed(3)}/0.4`);
      return hasStrands && hasMinimalField && hasStableEnergy;
      
    case 2: // Morphic Recursion → Dimensional Bridge
      // Requires: Significant strand multiplication and field stabilization
      const hasMultipleStrands = strands >= 12; // Substantial growth - no upper limit
      const hasGrowingField = morphicField > 1.2; // Strong field above emergence threshold
      const hasRecursiveComplexity = psi > 1.0; // Clear visual complexity (proxy)
      console.log(`🌱 MORPHIC THRESHOLD: strands=${strands}/12, field=${morphicField.toFixed(3)}/1.2, psi≈${psi.toFixed(3)}/1.0`);
      return hasMultipleStrands && hasGrowingField && hasRecursiveComplexity;
      
    case 3: // Dimensional Bridge → Standard Model
      // Requires: Emergence + dimensional stability + correlations
      const hasEmergence = emergence;
      const hasActivity = psi > 1.0; // Reduced from 1.2 for smoother progression
      const hasDimensionalCorr = frstProxy > 0.03 || rho > 0.03; // Reduced from 0.05 for easier progression
      const hasStrongField = morphicField > 1.0; // Reduced from 1.5 for smoother advancement
      console.log(`🔗 BRIDGE THRESHOLD: emergence=${hasEmergence}, psi≈${psi.toFixed(3)}/1.0, corr=${Math.max(frstProxy, rho).toFixed(3)}/0.03, field=${morphicField.toFixed(3)}/1.0`);
      return hasEmergence && hasActivity && hasDimensionalCorr && hasStrongField;
      
    case 4: // Standard Model → Consciousness
      // Requires: Strong particle interactions and field correlations
      const hasCorrelations = (frstProxy > 0.1 || rho > 0.1); // Strong correlations
      const hasStableField = morphicField > 2.0; // Very stable field
      const hasParticleActivity = psi > 1.5; // High particle activity
      const hasManyStrands = strands >= 20; // Complex strand network - scales indefinitely
      console.log(`⚛️ STANDARD THRESHOLD: corr=${Math.max(frstProxy, rho).toFixed(3)}/0.1, field=${morphicField.toFixed(3)}/2.0, psi≈${psi.toFixed(3)}/1.5, strands=${strands}/20`);
      return hasCorrelations && hasStableField && hasParticleActivity && hasManyStrands;
      
    case 5: // Consciousness → Cosmic Inflation
      // Requires: Significant consciousness resonance and complexity
      const hasConsciousness = consciousness > 0.1; // Substantial consciousness
      const hasComplexity = strands >= 30; // High complexity - unbounded growth
      const hasResonantField = morphicField > 2.5; // Resonant field strength
      const hasHighActivity = psi > 2.0; // Very high activity
      console.log(`🧠 CONSCIOUSNESS THRESHOLD: cons=${consciousness.toFixed(3)}/0.1, strands=${strands}/30, field=${morphicField.toFixed(3)}/2.5, psi≈${psi.toFixed(3)}/2.0`);
      return hasConsciousness && hasComplexity && hasResonantField && hasHighActivity;
      
    case 6: // Cosmic Inflation → CMB Formation
      // Requires: Extreme energy and maximum complexity
      const hasHighEnergy = psi > 3.0; // Extreme energy levels
      const hasHighComplexity = strands >= 50; // High strand complexity - φ-recursive scaling
      const hasInflationField = morphicField > 3.0; // Inflation-level field
      const hasStrongConsciousness = consciousness > 0.2; // Strong consciousness
      console.log(`🚀 INFLATION THRESHOLD: psi≈${psi.toFixed(3)}/3.0, strands=${strands}/50, field=${morphicField.toFixed(3)}/3.0, cons=${consciousness.toFixed(3)}/0.2`);
      return hasHighEnergy && hasHighComplexity && hasInflationField && hasStrongConsciousness;
      
    case 7: // CMB Formation → Dark Ages
      // Requires: Fully mature universe with all systems at maximum
      const isMature = psi > 4.0 && strands >= 75 && consciousness > 0.5 && morphicField > 4.0; // Continues scaling beyond these minimums
      const hasMaxCorrelations = frstProxy > 0.2 && rho > 0.2; // Strong field correlations
      console.log(`🌌 CMB THRESHOLD: psi≈${psi.toFixed(3)}/4.0, strands=${strands}/75, cons=${consciousness.toFixed(3)}/0.5, field=${morphicField.toFixed(3)}/4.0, corr=${Math.min(frstProxy, rho).toFixed(3)}/0.2`);
      return isMature && hasMaxCorrelations;
      
    case 8: // Dark Ages → Star Formation
      // Post-CMB cooling period requires sustained high complexity
      const hasPostCMBComplexity = psi > 5.0 && morphicField > 5.0;
      const hasDeepRecursion = strands >= 100; // Deep φ-recursive structures
      const hasSustainedConsciousness = consciousness > 0.7;
      console.log(`🌑 DARK AGES THRESHOLD: psi≈${psi.toFixed(3)}/5.0, strands=${strands}/100, field=${morphicField.toFixed(3)}/5.0, cons=${consciousness.toFixed(3)}/0.7`);
      return hasPostCMBComplexity && hasDeepRecursion && hasSustainedConsciousness;
      
    case 9: // Star Formation → Galaxy Formation  
      // First stellar nucleosynthesis requires extreme energy concentration
      const hasStarFormation = psi > 6.0 && morphicField > 6.0;
      const hasExtremeDensity = strands >= 150; // Extremely dense φ-recursive networks
      const hasEvolvedConsciousness = consciousness > 1.0; // Beyond human-level
      console.log(`⭐ STAR FORMATION THRESHOLD: psi≈${psi.toFixed(3)}/6.0, strands=${strands}/150, field=${morphicField.toFixed(3)}/6.0, cons=${consciousness.toFixed(3)}/1.0`);
      return hasStarFormation && hasExtremeDensity && hasEvolvedConsciousness;
      
    case 10: // Galaxy Formation → Complex Structures
      // Galactic structures require maximum system integration
      const hasGalacticComplexity = psi > 8.0 && morphicField > 8.0;
      const hasMaxRecursion = strands >= 200; // Maximum φ-recursive depth
      const hasTranscendentConsciousness = consciousness > 1.5; // Transcendent awareness
      console.log(`🌌 GALAXY FORMATION THRESHOLD: psi≈${psi.toFixed(3)}/8.0, strands=${strands}/200, field=${morphicField.toFixed(3)}/8.0, cons=${consciousness.toFixed(3)}/1.5`);
      return hasGalacticComplexity && hasMaxRecursion && hasTranscendentConsciousness;
      
    case 11: // Complex Structures → Ultimate Emergence
      // Final phase of cosmogenesis - ultimate complexity achievement
      const hasUltimateComplexity = psi > 10.0 && morphicField > 10.0;
      const hasInfiniteRecursion = strands >= 300; // Near-infinite φ-recursive structures
      const hasCosmicConsciousness = consciousness > 2.0; // Cosmic-level consciousness
      console.log(`✨ COMPLEX STRUCTURES THRESHOLD: psi≈${psi.toFixed(3)}/10.0, strands=${strands}/300, field=${morphicField.toFixed(3)}/10.0, cons=${consciousness.toFixed(3)}/2.0`);
      return hasUltimateComplexity && hasInfiniteRecursion && hasCosmicConsciousness;
      
    default:
      return true; // Unknown phase, allow progression
  }
}

/**
 * Update progressive cosmogenesis state
 */
export function updateProgressiveCosmogenesis() {
  const progressiveCosmogenesis = window.progressiveCosmogenesis;
  
  if (!progressiveCosmogenesis || !progressiveCosmogenesis.active) return;
  
  const now = Date.now();
  const elapsed = now - progressiveCosmogenesis.phaseStartTime;
  
  // PERFORMANCE: Adaptive timing for 90-phase system
  // Visual phases (1-16): 8 seconds each for observation  
  // Theoretical phases (17-90): 2 seconds each for progression
  const isVisualPhase = phase <= 16;
  const minTime = isVisualPhase ? 8000 : 2000; // 8s visual, 2s theoretical
  
  if (elapsed >= minTime) {
    // Execute the current phase
    // Use phase names from progressive cosmogenesis system for consistency
    const phaseName = (window.progressiveCosmogenesis?.phaseNames?.[progressiveCosmogenesis.currentPhase]) || 
                     (window.progressiveCosmogenesis?.getState?.()?.phaseName) || 
                     `Phase ${progressiveCosmogenesis.currentPhase + 1}`;
    
    // Execute cosmogenesis pipeline phase
    if (window.cosmogenesisPipeline) {
      const phaseResult = window.cosmogenesisPipeline.executePhase(progressiveCosmogenesis.currentPhase);
      console.log(`✨ Phase ${progressiveCosmogenesis.currentPhase}: ${phaseName} executed -`, phaseResult);
    }
    
    // Check if ready to advance to next phase
    if (checkPhaseThresholds(progressiveCosmogenesis.currentPhase)) {
      // Advance to next phase
      progressiveCosmogenesis.currentPhase++;
      progressiveCosmogenesis.phaseStartTime = now;
      
      if (progressiveCosmogenesis.currentPhase >= progressiveCosmogenesis.totalPhases) {
        // Cosmogenesis complete
        progressiveCosmogenesis.active = false;
        console.log('🎉 Progressive Cosmogenesis COMPLETE! Universe fully evolved from Ex Nihilo to CMB.');
        
        // Reset button
        const executeCosmogenesisBtn = document.getElementById('executeCosmogenesis');
        if (executeCosmogenesisBtn) {
          executeCosmogenesisBtn.disabled = false;
          executeCosmogenesisBtn.textContent = 'BEGIN COSMOGENESIS';
          executeCosmogenesisBtn.style.background = '';
        }
      } else {
        const newPhaseName = phaseNames[progressiveCosmogenesis.currentPhase];
        console.log(`🌟 Phase transition: ${phaseName} → ${newPhaseName} (Phase ${progressiveCosmogenesis.currentPhase + 1})`);
      }
    }
  }
}

/**
 * Setup cosmogenesis button event listener
 */
export function setupCosmogenesisButton() {
  const executeCosmogenesisBtn = document.getElementById('executeCosmogenesis');
  
  console.log('🔍 DEBUG: Looking for cosmogenesis button...', executeCosmogenesisBtn);
  
  if (executeCosmogenesisBtn) {
    // Remove any existing listeners to prevent duplicates
    executeCosmogenesisBtn.replaceWith(executeCosmogenesisBtn.cloneNode(true));
    const freshBtn = document.getElementById('executeCosmogenesis');
    
    freshBtn.addEventListener('click', (event) => {
      event.preventDefault();
      console.log('🚀 USER TRIGGERED: Progressive cosmogenesis execution');
      console.log('🔍 DEBUG: About to call startProgressiveCosmogenesis...');
      
      try {
        startProgressiveCosmogenesis();
        console.log('✅ DEBUG: startProgressiveCosmogenesis completed');
      } catch (error) {
        console.error('❌ ERROR in startProgressiveCosmogenesis:', error);
      }
    });
    
    console.log('🎛️ Cosmogenesis button listener attached successfully');
  } else {
    console.error('❌ CRITICAL: Cosmogenesis button not found! Available buttons:', 
      Array.from(document.querySelectorAll('button')).map(b => b.id || b.textContent));
  }
}

/**
 * Initialize phase indicators UI
 */
export function initializePhaseIndicators() {
  const phaseIndicatorsEl = document.getElementById('phase-indicators');
  
  if (phaseIndicatorsEl) {
    // Use abbreviated phase names for visual indicators (key milestones only)
    const keyPhases = ['Ex Nihilo', 'Grace', 'Quarks', 'Hadrons', 'Strange', 'Charm', 'Muon', 'EM', 'Matrix', 'Leptons', 'Matter', 'Dark', 'Tau', 'Unified', 'Nuclear', 'Cosmic', 'Hyper+', 'QG', 'Cool+', 'Ultimate'];
    phaseIndicatorsEl.innerHTML = keyPhases.map((phase, i) => 
      `<div style="flex:1; padding:2px; text-align:center; font-size:9px; color:#666; background:rgba(100,100,100,0.2); border-radius:2px;" title="Phase ${i+1}: ${phase}">${phase}</div>`
    ).join('');
    
    console.log('🏷️ Phase indicators initialized');
  } else {
    console.warn('⚠️ Phase indicators element not found');
  }
}
