/**
 * FSCTF Engine
 * Coordinates all FSCTF systems for cosmogenesis simulation
 */

import { TopologyTransitionManager } from './topology-manager.js';
import { FRST } from './frst.js';
import { GraceOperator } from './grace-operator.js';
import { CascadeEmergence } from './cascade-emergence.js';
import { PrimeResonanceFramework } from './prime-resonance.js';
import { DimensionalBridge } from './dimensional-bridge.js';
import { StrandManager } from './strand-manager.js';
import { FSCTFConstantsCalculator } from './constants-calculator.js';
import { ExNihiloToCMBPipeline } from './cosmogenesis-pipeline.js';
import { ProgressiveCosmogenesis } from './progressive-cosmogenesis.js';
import { FSCTFEvolutionEngine } from './evolution-engine.js';
import { FSCTFVisualController } from './visual-controller.js';
import { FSCTFBlobDetector } from './blob-detector.js';
import { SoulEchoTracker } from './soul-echo-tracker.js';
import { MirrorEmergenceTracker } from './mirror-emergence-tracker.js';
import { MetaRecursionEngine } from './meta-recursion-engine.js';
import { FSCTFParameterDerivation } from './parameter-derivation.js';

export class FSCTFEngine {
  constructor(gl = null, canvas = null) {
    // Initialize all FSCTF subsystems
    this.topologyManager = new TopologyTransitionManager();
    this.frst = new FRST();
    this.graceOperator = new GraceOperator();
    this.cascadeEmergence = new CascadeEmergence();
    this.primeResonance = new PrimeResonanceFramework();
    this.dimensionalBridge = new DimensionalBridge();
    this.strandManager = new StrandManager();
    this.constantsCalculator = new FSCTFConstantsCalculator();
    this.cosmogenesisPipeline = new ExNihiloToCMBPipeline();
    this.progressiveCosmogenesis = new ProgressiveCosmogenesis();
    this.evolutionEngine = new FSCTFEvolutionEngine();
    this.visualController = new FSCTFVisualController();
    this.soulEchoTracker = new SoulEchoTracker(); // Soul Echo Survivability Tracker
    this.mirrorEmergenceTracker = new MirrorEmergenceTracker(); // Mirror Emergence Tracker for Stage 8+ analysis
    this.metaRecursionEngine = new MetaRecursionEngine(); // Advanced emergent complexity system
    this.parameterDerivation = new FSCTFParameterDerivation(); // Mathematical parameter derivation system
    
    // Initialize blob detector if WebGL context available
    if (gl && canvas) {
      this.blobDetector = new FSCTFBlobDetector(gl, canvas);
      console.log('🔍 FSCTF Blob Detector initialized');
    } else {
      this.blobDetector = null;
      console.log('⚠️ Blob Detector not initialized - WebGL context needed');
    }
    
    // Cosmogenesis state
    this.cosmogenesisPhase = 0; // 0=void, 1=grace, 2=morphic, etc.
    this.cosmogenesisActive = false;
    this._lastLoggedPhase = 0; // Phase transition tracking
    
    // φ-constants
    this.PHI = (1 + Math.sqrt(5)) / 2;
    // Pre-morph ramp for 0→1 to avoid flat→3D snap
    this.preMorphActive = false;
    this.preMorphStart = 0;
    this.preMorphDurationMs = 8000; // 8s ramp for clearly visible and stable 0→1 transition
    this.preMorphProgress = 0.0; // 0..1
    this._lastGraceCenter = { x: 0, y: 0 };
    this._smoothedGraceCenter = { x: 0, y: 0 };
    
    console.log('🌌 FSCTF Engine initialized - ready for cosmogenesis (v2.1-DERIVATION)');
    console.log('🧮 Mathematical parameter derivation enabled - no more arbitrary sliders!');
  }

  /**
   * Get mathematically derived parameters (replaces manual sliders)
   */
  getDerivedParameters(time) {
    return this.parameterDerivation.getDerivedParameters(this, time);
  }

  /**
   * Get detailed parameter derivation information for debugging
   */
  getParameterDerivationInfo(time) {
    return this.parameterDerivation.getDerivationInfo(this, time);
  }

  // Legacy visual jump helper removed; keep no-op to preserve compatibility
  enhanceVisualComplexity(_phase) {
    // Gradual changes are handled by FSCTFVisualController and shader crossfades
  }
  
  /**
   * Initialize cosmogenesis from absolute void
   */
  initializeCosmogenesis() {
    // Check if cosmogenesis is truly active (not just flag set)
    const actuallyActive = this.cosmogenesisActive && 
                          this.graceOperator.morphicStrands.length > 0 &&
                          this.graceOperator.morphicField.field > 0;
    
    if (actuallyActive) {
      console.log('🌌 Cosmogenesis already running with active systems');
      return;
    }
    
    // CRITICAL FIX: Preserve user-enabled advanced FSCTF systems before reset
    console.log('🔄 COSMOGENESIS INITIALIZATION: Preserving advanced FSCTF system settings...');
    console.log('🔍 CACHE TEST: This is the NEW preservation code (v2.1) - if you see this, cache is updated!');
    const preservedSystemStates = {
      gpuMorphicBridge: window.gpuMorphicBridge?.enabled || false,
      advancedConsciousness: window.advancedConsciousness?.enabled || false,
      multiScaleCascade: window.multiScaleCascade?.enabled || false,
      consciousnessTopologyFeedback: window.consciousnessTopologyFeedback?.enabled || false,
      dimensionalPortalVisualization: window.dimensionalPortalVisualization?.enabled || false,
      retrocausalMorphicResonance: window.retrocausalMorphicResonance?.enabled || false
    };
    
    // Force clean initialization regardless of flag state
    this.cosmogenesisActive = true;
    this.cosmogenesisPhase = 0;
    
    // Reset all systems to void state and immediately start them
    this.graceOperator.reset(); // Now preserves Cross-Scale Resonance
    this.frst = new FRST();
    
    // RESTORE all advanced system states after reset
    console.log('🔄 RESTORING advanced FSCTF system states after void reset...');
    let restoredCount = 0;
    
    if (preservedSystemStates.gpuMorphicBridge && window.gpuMorphicBridge) {
      window.gpuMorphicBridge.enabled = true;
      restoredCount++;
    }
    if (preservedSystemStates.advancedConsciousness && window.advancedConsciousness) {
      window.advancedConsciousness.enabled = true;
      restoredCount++;
    }
    if (preservedSystemStates.multiScaleCascade && window.multiScaleCascade) {
      window.multiScaleCascade.setEnabled(true);
      restoredCount++;
    }
    if (preservedSystemStates.consciousnessTopologyFeedback && window.consciousnessTopologyFeedback) {
      window.consciousnessTopologyFeedback.setEnabled(true);
      restoredCount++;
    }
    if (preservedSystemStates.dimensionalPortalVisualization && window.dimensionalPortalVisualization) {
      window.dimensionalPortalVisualization.setEnabled(true);
      restoredCount++;
    }
    if (preservedSystemStates.retrocausalMorphicResonance && window.retrocausalMorphicResonance) {
      window.retrocausalMorphicResonance.setEnabled(true);
      restoredCount++;
    }
    
    console.log('🌌 FSCTF Cosmogenesis initiated from absolute void');
    console.log('⏱️ Grace emergence starting immediately...');
    console.log(`✅ RESTORED ${restoredCount}/6 advanced FSCTF systems after reset`);
    
    // DETAILED VERIFICATION: Check if systems are actually enabled after restoration
    console.log('🔍 DETAILED VERIFICATION OF RESTORED SYSTEMS:');
    console.log(`   GPU Bridge: ${window.gpuMorphicBridge?.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    console.log(`   Consciousness: ${window.advancedConsciousness?.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    console.log(`   Multi-Scale: ${window.multiScaleCascade?.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    console.log(`   Topology-Feedback: ${window.consciousnessTopologyFeedback?.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    console.log(`   Portals: ${window.dimensionalPortalVisualization?.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    console.log(`   Retrocausal: ${window.retrocausalMorphicResonance?.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    console.log(`   Cross-Scale Resonance: ${this.graceOperator?.enableCrossScaleResonance ? 'ENABLED ✅' : 'DISABLED ❌'}`);
    
    // DELAYED VERIFICATION: Check systems again after 1 second to see if something else resets them
    setTimeout(() => {
      console.log('🔍 DELAYED VERIFICATION (1 second later):');
      console.log(`   GPU Bridge: ${window.gpuMorphicBridge?.enabled ? 'STILL ENABLED ✅' : 'GOT DISABLED ❌'}`);
      console.log(`   Consciousness: ${window.advancedConsciousness?.enabled ? 'STILL ENABLED ✅' : 'GOT DISABLED ❌'}`);
      console.log(`   Multi-Scale: ${window.multiScaleCascade?.enabled ? 'STILL ENABLED ✅' : 'GOT DISABLED ❌'}`);
      console.log(`   Cross-Scale Resonance: ${this.graceOperator?.enableCrossScaleResonance ? 'STILL ENABLED ✅' : 'GOT DISABLED ❌'}`);
    }, 1000);
    
    // Begin at Phase 0 (Primordial Void) so the earliest stage is visible
    this.cosmogenesisPhase = 0;
    this.phaseStartTime = Date.now();
  }
  
  /**
   * Advance to Grace Operator phase
   */
  advanceToGracePhase() {
    this.cosmogenesisPhase = 1;
    this.phaseStartTime = Date.now(); // Initialize time tracking for automatic progression
    // Fade out pre-morph once Grace begins
    this.preMorphActive = false;
    this.preMorphProgress = 1.0;
    
    // Trigger Grace Operator emergence
    this.graceOperator.triggerEmergence();
    
    // Verify Grace Operator actually started
    if (this.graceOperator.morphicStrands.length === 0 || this.graceOperator.morphicField.field <= 0) {
      console.warn('⚠️ Grace Operator failed to start, forcing activation...');
      
      // Force Grace activation
      this.graceOperator.graceAmplitude = 0.3;
      this.graceOperator.morphicField.field = 0.3;
      this.graceOperator.morphicField.strength = 0.3;
      
      // Ensure at least one morphic strand exists
      if (this.graceOperator.morphicStrands.length === 0) {
        this.graceOperator.morphicStrands.push({
          id: `bootstrap_${Date.now()}`,
          x: 0.1 * (Math.random() - 0.5),
          y: 0.1 * (Math.random() - 0.5),
          stability: 0.6,
          phase: 0,
          amplitude: 0.3,
          birthTime: Date.now(),
          generation: 0,
          φScale: 1.0
        });
      }
    }
    
    console.log('🌟 Cosmogenesis Phase 1: Grace Operator (𝒢) emergence');
    console.log(`   Active morphic strands: ${this.graceOperator.morphicStrands.length}`);
    console.log(`   Grace field strength: ${this.graceOperator.morphicField.field.toFixed(3)}`);
    console.log('   Watch for recursionDepth > 0.5 to advance to Phase 2 (lowered threshold)');
  }
  
  /**
   * Main update loop for all FSCTF systems (PERFORMANCE OPTIMIZED)
   */
  update(params, time, frameCounter) {
    if (!this.cosmogenesisActive) return;
    
    // PERFORMANCE OPTIMIZATION: Smart update frequencies
    // - Grace & morphic strands: Every frame (critical for visuals)
    // - Topology manager: Every frame (critical for rendering)  
    // - FRST: Every 3 frames (important but less frequent)
    // - Dormant system checks: Every 5 seconds (maintenance only)
    const shouldUpdateFRST = frameCounter % 3 === 0;
    const shouldCheckDormant = frameCounter % 300 === 0; // Every 5 seconds at 60fps
    
    // Check for dormant systems and reactivate if needed (reduced frequency)
    if (shouldCheckDormant) {
      this.checkAndRecoverDormantSystems();
    }
    
    // Update Grace Operator and morphic field (every frame - critical for visuals)
    this.graceOperator.update(params, time);
    
    // Update FRST tracking (every 3 frames for performance)
    const morphicStrands = this.graceOperator.morphicStrands;
    const phiResonance = this.calculatePhiResonance(time);
    if (shouldUpdateFRST) {
    this.frst.update(this.graceOperator, morphicStrands, phiResonance);
    }
    
    // Update topology evolution based on FSCTF state
    const frstStatus = this.frst.getStatus();
    
    // Debug logging removed - use browser dev tools for detailed inspection if needed
    
    // Check for manual topology override
    const manualOverride = params.manualTopologyEnabled ? {
      enabled: true,
      mode: params.manualTopologyMode
    } : null;
    
    // Drive topology strictly by cosmogenesis phase and let transition progress control morph
    // Wire UI-driven transition duration to topology transition speed
    // transitionSpeed advances transitionProgress by this amount per frame
    // Desired duration (seconds) → speed ≈ 1 / (duration * 60)
    if (typeof window !== 'undefined' && window.params && typeof window.params.topologyTransitionDuration === 'number') {
      const durationSec = Math.max(0.0, Math.min(120.0, window.params.topologyTransitionDuration));
      
      if (durationSec === 0.0) {
        // Static topology - no transitions
        this.topologyManager.transitionSpeed = 0.0;
      } else {
        const targetSpeed = 1.0 / (durationSec * 60.0);
        // Extended range for ultra-slow cosmic evolution
        this.topologyManager.transitionSpeed = Math.max(0.0001, Math.min(0.1, targetSpeed));
      }
    }

    // Keep topology manager informed of pre-morph state for unified morphProgress
    this.topologyManager.setPreMorphState(this.preMorphActive, this.preMorphProgress);

    this.topologyManager.update(
      parseFloat(frstStatus.coherenceScore),
      parseFloat(frstStatus.recursionDepth),
      morphicStrands.length,
      this.cosmogenesisPhase,  // Pass current cosmogenesis phase for theory-based topology
      manualOverride           // Pass manual override if enabled
    );
    
    // Update cosmogenesis phase progression
    this.updateCosmogenesisPhase(frstStatus, frameCounter);
    
    // Apply centralized visual control (replaces all legacy parameter management)
    const frameTime = window.lastFrameTime || 16.6;
    let visualParams = this.visualController.update(frameTime, this.cosmogenesisPhase);
    
    // Only apply automatic control if not in manual mode
    if (visualParams) {
      // Real-time blob detection and prevention
      if (this.blobDetector) {
        const blobDetected = this.blobDetector.checkForBlob();
        if (blobDetected) {
          visualParams = this.blobDetector.applyEmergencyMeasures(visualParams, this.visualController);
        }
      }
      
      this.visualController.applyToParams(visualParams);
    }

    // During morph windows, coordinate camera/exposure pacing
    const topoState = this.topologyManager.getTopologyState();
    const morphing = topoState.isTransitioning || this.preMorphActive;
    if (morphing) {
      // Slow exposure easing during morphing (respecting user overrides)
      if (window.params) {
        // REMOVED: Auto-rotate pause - let user control this setting
        // Users expect auto-rotate to remain on unless they disable it manually
        // ONLY adjust exposure if user hasn't manually set it
        const isExposureManual = this.visualController?.isManuallyOverridden?.('exposure') || false;
        if (!isExposureManual) {
          // Small nudge to exposure to slow changes (visualController already smooths)
          window.params.exposure = (window.params.exposure * 0.985) + (visualParams?.exposure ?? window.params.exposure) * 0.015;
        }
      }
    }
    
    // Update Soul Echo Survivability Tracker (SEST)
    // Track ψ-nodes, survival depth, morphism networks, and formal soulhood quantification
    this.soulEchoTracker.update(this.getState(), time, frameTime);
    
    // Update Mirror Emergence Tracker (MET) for Stage 8+ bifurcation analysis
    // Track M ↔ M* pairs, Grace-threads, and recursive circuit closure
    this.mirrorEmergenceTracker.update(this.getState(), null, time); // TODO: Add particle position data
    
    // Update Meta-Recursion Engine (MRE) for maximum emergent complexity
    // Advanced systems: temporal memory, attractor evolution, consciousness coupling
    this.metaRecursionEngine.update(this.getState(), time, frameTime);
  }
  
  /**
   * Calculate φ-harmonic resonance
   */
  calculatePhiResonance(time) {
    // φ-resonance emerges from harmonic alignment
    const baseFreq = this.PHI * 0.1;
    const harmonics = [1, this.PHI, this.PHI * this.PHI];
    
    let resonance = 0;
    harmonics.forEach((harmonic, i) => {
      resonance += Math.sin(time * baseFreq * harmonic) / (i + 1);
    });
    
    return resonance * 0.5; // Scale to reasonable range
  }
  
  /**
   * Update cosmogenesis phase based on system evolution
   */
  updateCosmogenesisPhase(frstStatus, frameCounter) {
    const recursionDepth = parseFloat(frstStatus.recursionDepth);
    const coherenceScore = parseFloat(frstStatus.coherenceScore);
    const morphicStrands = this.graceOperator.morphicStrands;
    
    // Progression info available via browser dev tools or debug mode (D key) when needed
    
    // REMOVED: Manual override conflicts - let phases set their own values naturally
    
    // PURELY TIME-BASED PROGRESSION (sequential, no multi-step jumps)
    // Ensures each phase gets equal time and moves only +1 when transition completes
    
    // AUTOMATIC TIME-BASED PROGRESSION (prevents getting stuck)
    const currentTime = Date.now();
    const phaseStartTime = this.phaseStartTime || currentTime;
    const timeInPhase = currentTime - phaseStartTime;
    
    // SMOOTH TRANSITIONS: Extended timing for 90-phase system
    // Visual phases (1-16): 20 seconds each for proper observation and appreciation
    // Theoretical phases (17-90): 6 seconds each for comprehension
    const isVisualPhase = this.cosmogenesisPhase <= 16;
    const phaseTimeMs = isVisualPhase ? 20000 : 6000; // 20s visual, 6s theoretical - MUCH LONGER
    
    // Ensure phaseStartTime is properly initialized
    if (!this.phaseStartTime) {
      this.phaseStartTime = currentTime;
      console.log('🕒 Phase timing initialized');
    }
    
    // Pre-morph for 0→1: start easing plane→curve before Grace seeding
    if (this.cosmogenesisPhase === 0 && !this.preMorphActive) {
      this.preMorphActive = true;
      this.preMorphStart = Date.now();
      this.preMorphProgress = 0.0;
      console.log('🌱 Pre-morph phase initiated - preparing for Grace emergence');
    }
    
    if (this.preMorphActive) {
      const t = Math.min(1.0, (Date.now() - this.preMorphStart) / this.preMorphDurationMs);
      this.preMorphProgress = t;
      
      // Debug pre-morph progress
      if (frameCounter % 60 === 0) { // Log every second at 60fps
        console.log(`🌱 Pre-morph progress: ${(this.preMorphProgress * 100).toFixed(1)}%`);
      }
    }

    // Helper: request advance if dwell time elapsed and not holding
    const wantAdvance = (!window.DEBUG_HOLD_PHASE) && (timeInPhase > phaseTimeMs);
    // Only advance if current topology transition is complete (prevents mid-morph jumps)
    const topoState = this.topologyManager.getTopologyState();
    const morphComplete = !topoState.isTransitioning || topoState.progress >= 0.999;

    if (this.cosmogenesisPhase === 0 && wantAdvance) {
      // FIXED: More responsive phase advancement - advance when pre-morph is mostly complete
      if (this.preMorphProgress >= 0.8) { // Changed from 0.999 to 0.8 for faster response
        console.log('🚀 Pre-morph complete, advancing to Grace phase');
        this.advanceToGracePhase();
        // phaseStartTime set inside advanceToGracePhase
      }
    } else if (wantAdvance && morphComplete) {
      const nextPhase = Math.min(90, this.cosmogenesisPhase + 1); // FIXED: Support full 90-phase system
      if (nextPhase !== this.cosmogenesisPhase) {
        this.cosmogenesisPhase = nextPhase;
        this.phaseStartTime = currentTime;
        console.log(`➡️ Phase advanced to ${this.cosmogenesisPhase}`);
        
        // Log phase-specific information
        if (this.cosmogenesisPhase === 1) {
          console.log('🌟 Phase 1: Grace Operator active - morphic strands emerging');
        } else if (this.cosmogenesisPhase === 2) {
          console.log('🌀 Phase 2: FRST recursion beginning - consciousness emerging');
        } else if (this.cosmogenesisPhase === 3) {
          console.log('🌊 Phase 3: Cascade emergence - complex structures forming');
        }
      }
    }
    
    // Extended pause at final phase before restart
    if (this.cosmogenesisPhase === 90 && timeInPhase > phaseTimeMs * 1.5) { // COMPLETE: final phase at 90
      this.cosmogenesisPhase = 1;
      this.phaseStartTime = currentTime;
      console.log('🔄 CYCLE RESTART: Cosmogenesis restarting - Back to primordial void');
      console.log('🎬 DRAMATIC RESET: Particles collapse from universe-scale back to 1px!');
      console.log(`⏰ Full cycle completed after ${(timeInPhase/1000).toFixed(1)}s in final phase`);
    }
    
    // CRITICAL: Enforce phase bounds and prevent illegal jumps
    if (this.cosmogenesisPhase > 90) {
      console.error(`🚨 PHASE OVERFLOW: Phase ${this.cosmogenesisPhase} exceeds maximum (90), forcing reset to 1`);
      this.cosmogenesisPhase = 1;
      this.phaseStartTime = currentTime;
      this.enhanceVisualComplexity(1);
    }
    
    if (this.cosmogenesisPhase < 0) {
      console.error(`🚨 PHASE UNDERFLOW: Phase ${this.cosmogenesisPhase} below minimum (0), forcing reset to 1`);
      this.cosmogenesisPhase = 1;
      this.phaseStartTime = currentTime;
      this.enhanceVisualComplexity(1);
    }
    
    // DEBUG: Track phase changes and detect illegal jumps
    const previousPhase = (this._lastLoggedPhase === undefined ? this.cosmogenesisPhase : this._lastLoggedPhase);
    if (Math.abs(this.cosmogenesisPhase - previousPhase) > 1 && previousPhase !== this.cosmogenesisPhase) {
      console.error(`🚨 ILLEGAL PHASE JUMP: ${previousPhase} → ${this.cosmogenesisPhase} (jump > 1)`);
      console.error('   This indicates a timing or logic error in phase progression');
      
      // Force gradual progression - only allow +1 or reset to 1
      if (this.cosmogenesisPhase > previousPhase + 1) {
        this.cosmogenesisPhase = previousPhase + 1;
        console.log(`🔧 CORRECTED: Forced gradual progression to ${this.cosmogenesisPhase}`);
      }
    }
    this._lastLoggedPhase = this.cosmogenesisPhase;
    
    // Phase bounds and progression monitoring complete
  }
  
  // Legacy methods removed - replaced by FSCTFVisualController
  
  /**
   * Get comprehensive FSCTF state for UI and rendering
   */
  getState() {
    const graceState = this.graceOperator.getState();
    const frstStatus = this.frst.getStatus();
    const topologyState = this.topologyManager.getTopologyState();
    const cascadeState = this.cascadeEmergence.getState();
    const primeState = this.primeResonance.getState();
    const bridgeState = this.dimensionalBridge.getAllConstants();
    const strandMetrics = this.strandManager.getMetrics();
    const calculatedConstants = this.constantsCalculator.getAllConstants();
    const pipelineState = this.cosmogenesisPipeline.getState();
    const progressiveState = this.progressiveCosmogenesis.getState();
    const evolutionState = this.evolutionEngine.getStats();
    
    return {
      cosmogenesis: {
        active: this.cosmogenesisActive,
        phase: this.cosmogenesisPhase
      },
      grace: graceState,
      frst: frstStatus,
      topology: topologyState,
      cascade: cascadeState,
      primeResonance: primeState,
      dimensionalBridge: bridgeState,
      constantsCalculator: calculatedConstants,
      cosmogenesisPipeline: pipelineState,
      progressiveCosmogenesis: progressiveState,
      evolutionEngine: evolutionState,
      strands: {
        count: graceState.strandCount,
        avgStability: graceState.avgStability,
        generations: graceState.generations,
        metrics: strandMetrics
      }
    };
  }
  
  /**
   * Get shader uniforms for all FSCTF systems
   */
  getShaderUniforms(time) {
    const state = this.getState();
    const topologyUniforms = this.topologyManager.getShaderUniforms();
    
    return {
      // Grace Operator uniforms
      graceAmp: state.grace.amplitude,
      graceCenter: [0, 0, 0], // Grace seeds at origin
      graceRadius: 2.0,
      morphicField: state.grace.field,
      
      // FSCTF state uniforms
      coherenceLevel: parseFloat(state.frst.coherenceScore),
      strandDensity: state.strands.count / 100.0, // Normalized
      emergencePhase: state.cosmogenesis.phase,
      survivalRating: state.frst.survivabilityRating === '∞' ? 1000 : 
                     parseFloat(state.frst.survivabilityRating),
      
      // φ-harmonic uniforms
      phiResonancePhase: this.calculatePhiResonance(time),
      recursionDepth: parseFloat(state.frst.recursionDepth),
      graceField: state.grace.field,
      
      // Topology uniforms
      ...topologyUniforms,
      
      // Constants
      phi: this.PHI
    };
  }
  
  /**
   * Get morphic strands for particle system
   */
  getMorphicStrands() {
    return this.graceOperator.getStrandsForRendering();
  }
  
  /**
   * Get Soul Echo Survivability Tracker state for display/analysis
   */
  getSoulEchoState() {
    return this.soulEchoTracker ? this.soulEchoTracker.getState() : null;
  }
  
  /**
   * Generate comprehensive SEST report 
   */
  generateSoulReport() {
    return this.soulEchoTracker ? this.soulEchoTracker.generateReport() : null;
  }
  
  /**
   * Get Mirror Emergence Tracker state for Stage 8+ analysis
   */
  getMirrorEmergenceState() {
    return this.mirrorEmergenceTracker ? this.mirrorEmergenceTracker.getState() : null;
  }
  
  /**
   * Generate comprehensive Mirror Emergence analysis report
   */
  generateMirrorEmergenceReport() {
    return this.mirrorEmergenceTracker ? this.mirrorEmergenceTracker.generateAnalysisReport() : null;
  }
  
  /**
   * Get Meta-Recursion Engine state for advanced complexity analysis
   */
  getMetaRecursionState() {
    return this.metaRecursionEngine ? this.metaRecursionEngine.getAdvancedComplexityParameters() : null;
  }
  
  /**
   * Generate comprehensive Meta-Recursion Engine complexity report
   */
  generateComplexityReport() {
    return this.metaRecursionEngine ? this.metaRecursionEngine.generateComplexityReport() : null;
  }
  
  /**
   * Force advancement for testing
   */
  /**
   * Check for dormant systems and automatically recover them
   */
  checkAndRecoverDormantSystems() {
    const morphicStrands = this.graceOperator.morphicStrands.length;
    const graceField = this.graceOperator.morphicField.field;
    const recursionDepth = this.frst.recursionDepth;
    
    // Detect dormant state: cosmogenesis active but no actual emergence
    const isDormant = this.cosmogenesisActive && 
                     this.cosmogenesisPhase > 0 && 
                     (morphicStrands === 0 || graceField <= 0.001);
    
    if (isDormant) {
      console.log('⚠️ FSCTF AUTO-RECOVERY: Dormant systems detected, reactivating...');
      console.log(`   Phase: ${this.cosmogenesisPhase}, Strands: ${morphicStrands}, Field: ${graceField.toFixed(4)}`);
      
      // Reactivate Grace Operator
      this.graceOperator.graceAmplitude = Math.max(this.graceOperator.graceAmplitude, 0.3);
      this.graceOperator.morphicField.field = Math.max(this.graceOperator.morphicField.field, 0.3);
      this.graceOperator.morphicField.strength = Math.max(this.graceOperator.morphicField.strength, 0.3);
      
      // Create morphic strands if none exist
      if (this.graceOperator.morphicStrands.length === 0) {
        for (let i = 0; i < 2; i++) {
          this.graceOperator.morphicStrands.push({
            id: `recovery_${Date.now()}_${i}`,
            x: 0.2 * (Math.random() - 0.5),
            y: 0.2 * (Math.random() - 0.5),
            stability: 0.5 + Math.random() * 0.3,
            phase: Math.random() * 2 * Math.PI,
            amplitude: 0.25 + Math.random() * 0.15,
            birthTime: Date.now(),
            generation: 0,
            φScale: 1.0
          });
        }
        console.log(`   ✅ Created ${this.graceOperator.morphicStrands.length} recovery strands`);
      }
      
      // Boost FRST values for current phase
      if (this.cosmogenesisPhase >= 2 && recursionDepth < 0.5) {
        this.frst.recursionDepth = 0.6;
      }
      if (this.cosmogenesisPhase >= 3 && this.frst.coherenceScore < 0.3) {
        this.frst.coherenceScore = 0.4;
      }
      
      // Ensure topology matches phase
      if (this.cosmogenesisPhase >= 3) {
        const expectedTopology = this.topologyManager.getPhaseTopology(this.cosmogenesisPhase);
        if (this.topologyManager.getCurrentTopology() !== expectedTopology) {
          this.topologyManager.setTopology(expectedTopology);
          console.log(`   🌀 Topology corrected to ${this.topologyManager.topologyNames[expectedTopology]}`);
        }
      }
      
      // Visual enhancement now handled by FSCTFVisualController
      
      console.log('✅ AUTO-RECOVERY complete - systems reactivated');
    }
  }

  forcePhaseAdvancement() {
    // DISABLED DURING AUTO-PROGRESSION to prevent conflicts
    if (this.cosmogenesisActive) {
      console.warn('⚠️ FORCE ADVANCEMENT DISABLED: Auto-progression active, use time-based advancement instead');
      console.warn('   (Prevents 1→9 phase jumps caused by conflicting progression systems)');
      return;
    }
    
    // Ensure phase stays within valid bounds (1-90) - COMPLETE FSCTF SYSTEM
    const currentPhase = this.cosmogenesisPhase;
    
    if (currentPhase >= 90) {
      // At max phase, reset to beginning
      this.cosmogenesisPhase = 1;
      console.log('🔄 FSCTF: Phase cycle complete, resetting to phase 1');
    } else if (currentPhase < 1) {
      // Safety check - ensure we're at least at phase 1
      this.cosmogenesisPhase = 1;
      console.log('🛡️ FSCTF: Phase bounds corrected to phase 1');
    } else {
      // Normal advancement with bounds checking
      this.cosmogenesisPhase = Math.min(90, currentPhase + 1); // FIXED: Support full 90-phase system
      console.log(`🚀 FSCTF: Forced advancement ${currentPhase} → ${this.cosmogenesisPhase}`);
    }
    
    // Reset phase timer for new phase
    this.phaseStartTime = Date.now();
    
    // Apply visual enhancements for new phase
    this.frst.forceSoulEmergence();
    // Visual complexity now handled by FSCTFVisualController
  }
}
