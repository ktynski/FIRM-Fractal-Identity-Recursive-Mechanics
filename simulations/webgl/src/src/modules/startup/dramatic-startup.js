/**
 * Dramatic Startup System
 * Initializes FSCTF systems and creates dramatic initial conditions
 */

import { vlog } from '../utils/logging.js';

export class DramaticStartup {
  constructor() {
    this.initialized = false;
    this.startupPhases = [
      'FSCTF Initialization',
      'Parameter Chaos',
      'Evolution Kickstart'
    ];
    this.currentPhase = 0;
    
    console.log('🚀 Dramatic Startup System initialized');
  }
  
  /**
   * Execute dramatic startup sequence
   */
  execute() {
    if (this.initialized) {
      console.log('🚀 Dramatic startup already executed');
      return;
    }
    
    vlog("🚀 FSCTF: Initializing MAXIMUM DRAMATIC EMERGENCE...");
    vlog("👀 WATCH FOR: Swirling Grace zones (center), Collapsing Devourers (moving), Traveling waves");
    vlog("🧠 Brain modes cycle every 20 seconds: SEEKING → COHERENT → CHAOTIC");
    
    // Phase 1: Initialize FSCTF systems
    this.initializeFSCTFSystems();
    
    // Phase 2: Set dramatic initial parameters
    this.setDramaticParameters();
    
    // Phase 3: Schedule parameter chaos
    this.scheduleChaos();
    
    this.initialized = true;
    console.log('✨ Dramatic startup sequence complete');
  }
  
  /**
   * Initialize FSCTF theoretical framework
   */
  initializeFSCTFSystems() {
    if (!window.params?.fsctfEnabled) {
      console.log('⏸️ FSCTF disabled - skipping initialization');
      return;
    }
    
    console.log('🌌 Initializing FSCTF Theoretical Framework...');
    
    try {
      // Initialize cosmogenesis pipeline
      if (window.cosmogenesisPipeline) {
        const initResults = window.cosmogenesisPipeline.initializePipeline();
        console.log('🌌 FSCTF Cosmogenesis Pipeline initialized:', initResults);
      }
      
      // Initialize φ-derived evolution engine if available
      if (window.FSCTFEvolutionEngine) {
        window.fsctfEvolutionEngine = new window.FSCTFEvolutionEngine();
        console.log('🧬 φ-Evolution Engine initialized');
      }
      
      // Log derived constants
      if (window.dimensionalBridge) {
        const constants = window.dimensionalBridge.getAllConstants();
        console.log('🔬 FSCTF Derived Constants:', {
          phi: constants.phi,
          planckMass: constants.constants?.planckMass,
          fineStructure: constants.constants?.fineStructureConstant,
          electronMass: constants.constants?.electronMass
        });
      }
      
      console.log('✅ FSCTF systems initialization complete');
    } catch (error) {
      console.error('❌ FSCTF initialization error:', error);
    }
  }
  
  /**
   * Set dramatic initial parameters for immediate visual impact
   */
  setDramaticParameters() {
    if (!window.params) {
      console.warn('⚠️ Global params not available - skipping dramatic parameters');
      return;
    }
    
    console.log('⚡ Setting dramatic initial parameters...');
    
    // Force EXTREME initial parameters for IMMEDIATE visual impact
    const dramaticParams = {
      graceAmp: 0.95,
      devourerAmp: 0.8,
      reflectMix: 0.9,
      k_flow: 4.0,
      burstAmp: 2.0,
      fieldScale: 1.2,
      timeScale: 0.8
    };
    
    Object.assign(window.params, dramaticParams);
    
    // Start with seeking mode for traveling Grace
    if (window.Brain) {
      window.Brain.emergenceMode = 'seeking';
      window.Brain.lastModeSwitch = performance.now() * 0.001;
    }
    
    // Update UI to reflect changes
    if (window.updateParamVisualizations) {
      window.updateParamVisualizations({});
    }
    
    console.log('⚡ Dramatic parameters set:', dramaticParams);
  }
  
  /**
   * Schedule chaos events for continued drama
   */
  scheduleChaos() {
    // First chaos wave after 2 seconds
    setTimeout(() => {
      this.executeParameterChaos('Primary Chaos Wave');
    }, 2000);
    
    // Second chaos wave after 5 seconds
    setTimeout(() => {
      this.executeContinuedEvolution();
    }, 5000);
    
    // Periodic mini-chaos for ongoing drama
    setInterval(() => {
      this.executeMiniChaos();
    }, 8000); // Every 8 seconds to match visual phase timing
  }
  
  /**
   * Execute dramatic parameter chaos
   */
  executeParameterChaos(phaseName = 'Parameter Chaos') {
    if (!window.params) return;
    
    vlog(`⚡ FSCTF: FORCING ${phaseName.toUpperCase()}!`);
    
    const chaosParams = {
      graceAmp: 0.6 + Math.random() * 0.4,
      devourerAmp: 0.3 + Math.random() * 0.5,
      fieldScale: 1.5 + Math.random() * 2.0,
      timeScale: 0.3 + Math.random() * 0.6,
      reflectMix: 0.4 + Math.random() * 0.5
    };
    
    Object.assign(window.params, chaosParams);
    
    if (window.updateParamVisualizations) {
      window.updateParamVisualizations({});
    }
    
    console.log(`🌀 ${phaseName} executed:`, chaosParams);
  }
  
  /**
   * Execute continued evolution parameters
   */
  executeContinuedEvolution() {
    if (!window.params) return;
    
    vlog("🌀 FSCTF: CONTINUING DRAMATIC EVOLUTION!");
    
    const evolutionParams = {
      k_flow: 2.0 + Math.random() * 3.0,
      jitterSigma: 0.02 + Math.random() * 0.06,
      burstAmp: 1.0 + Math.random() * 1.5,
      damping: 0.01 + Math.random() * 0.03
    };
    
    Object.assign(window.params, evolutionParams);
    
    if (window.updateParamVisualizations) {
      window.updateParamVisualizations({});
    }
    
    console.log('🌀 Continued evolution executed:', evolutionParams);
  }
  
  /**
   * Execute mini chaos for ongoing drama
   */
  executeMiniChaos() {
    if (!window.params || !this.initialized) return;
    
    // Only mini-chaos if no user overrides are active
    if (window.hasActiveUserOverrides && window.hasActiveUserOverrides()) return;
    
    const miniChaos = {
      graceAmp: window.params.graceAmp * (0.9 + Math.random() * 0.2),
      devourerAmp: window.params.devourerAmp * (0.95 + Math.random() * 0.1),
      fieldScale: window.params.fieldScale * (0.95 + Math.random() * 0.1)
    };
    
    // Clamp values to reasonable ranges
    miniChaos.graceAmp = Math.max(0.1, Math.min(2.0, miniChaos.graceAmp));
    miniChaos.devourerAmp = Math.max(0.1, Math.min(1.5, miniChaos.devourerAmp));
    miniChaos.fieldScale = Math.max(0.5, Math.min(3.0, miniChaos.fieldScale));
    
    Object.assign(window.params, miniChaos);
    
    console.log('✨ Mini-chaos applied for continued drama');
  }
  
  /**
   * Reset startup state (for testing)
   */
  reset() {
    this.initialized = false;
    this.currentPhase = 0;
    console.log('🔄 Dramatic startup reset');
  }
  
  /**
   * Get startup state
   */
  getState() {
    return {
      initialized: this.initialized,
      currentPhase: this.currentPhase,
      totalPhases: this.startupPhases.length,
      phaseName: this.startupPhases[this.currentPhase] || 'Complete'
    };
  }
  
  /**
   * Force immediate drama (manual trigger)
   */
  forceDrama() {
    console.log('🎭 Forcing immediate dramatic changes...');
    this.executeParameterChaos('Manual Drama Trigger');
  }
  
  /**
   * Set quiet mode (disable chaos)
   */
  setQuietMode(enabled) {
    this.quietMode = enabled;
    console.log(`🔇 Quiet mode ${enabled ? 'enabled' : 'disabled'}`);
  }
}
