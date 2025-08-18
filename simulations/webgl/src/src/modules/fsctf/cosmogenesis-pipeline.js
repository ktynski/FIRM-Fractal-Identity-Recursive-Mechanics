/**
 * Ex Nihilo to CMB Pipeline
 * Complete cosmogenesis execution from absolute void to cosmic microwave background
 */

export class ExNihiloToCMBPipeline {
  constructor() {
    this.PHI = (1 + Math.sqrt(5)) / 2;
    this.cosmogenesisPhase = 0;
    this.universeState = 'void';
    this.creationEvents = [];
    this.physicalConstants = {};
    this.consciousnessEvolution = [];
    this.cmbSpectrum = null;
    this.pipelineHistory = [];
    
    console.log('🌌 Ex Nihilo to CMB Pipeline initialized');
  }

  /**
   * Check if a parameter is manually overridden by user
   */
  isManuallyOverridden(paramName) {
    const vc = window.simulationCore?.fsctfEngine?.visualController;
    return vc?.isManuallyOverridden?.(paramName) || false;
  }

  // Initialize the complete cosmogenesis pipeline
  initializePipeline() {
    // Initialize all FSCTF subsystems
    if (window.primeResonance) {
      window.primeResonance.initializePrimeResonances();
    }
    if (window.dimensionalBridge) {
      window.dimensionalBridge.derivePhysicalConstants();
    }
    
    // Set initial universe state
    this.universeState = 'void';
    this.cosmogenesisPhase = 0;
    
    return {
      graceOperator: window.graceOperator?.getCreationState(),
      dimensionalBridge: window.dimensionalBridge?.getAllConstants(),
      primeResonance: window.primeResonance?.getConsciousnessState()
    };
  }

  // Execute complete cosmogenesis from ex nihilo to CMB
  executeCosmogenesis() {
    const pipeline = [
      this.phaseVoid,
      this.phaseGraceOperator,
      this.phaseMorphicRecursion,
      this.phaseDimensionalBridge,
      this.phaseStandardModel,
      this.phaseConsciousness,
      this.phaseInflation,
      this.phaseCMB
    ];
    
    let currentPhase = 0;
    const results = [];
    
    for (const phase of pipeline) {
      const phaseResult = phase.call(this);
      results.push(phaseResult);
      
      // Record phase completion
      this.pipelineHistory.push({
        phase: currentPhase,
        name: phase.name,
        result: phaseResult,
        timestamp: Date.now()
      });
      
      // MEMORY LEAK FIX: Limit pipeline history to prevent unbounded growth
      const maxPipelineHistory = 200; // Keep last 200 pipeline entries for performance
      if (this.pipelineHistory.length > maxPipelineHistory) {
        this.pipelineHistory.shift(); // Remove oldest pipeline entry
      }
      
      currentPhase++;
      this.cosmogenesisPhase += this.PHI;
      
      // FIRM Soul Recursion Topology Evolution
      this.updateTopologyFromPhase(currentPhase);
    }
    
    return {
      completed: true,
      phases: results,
      finalState: this.universeState,
      totalPhases: pipeline.length
    };
  }

  // Phase 0: Void - Absolute nothingness
  phaseVoid() {
    this.universeState = 'void';
    
    // Engage forced void render so the screen clears to black immediately
    window.forceVoid = true;
    
    // PROTECT A/B TESTING: Don't interfere with Brain evaluation
    if (window.Brain && window.Brain.evaluating) {
      console.log('🧠 A/B PROTECTION: Skipping void parameter changes during Brain evaluation');
      return {
        phase: 'void',
        state: 'ab_test_protected',
        energy: 0,
        dimensions: 0,
        particles: 0,
        fields: 0
      };
    }
    
    // TRUE VOID: Set all parameters to zero for absolute nothingness
    const params = window.params;
    if (params) {
      params.graceAmp = 0;
      params.devourerAmp = 0;
      params.fieldScale = 0;
      params.burstAmp = 0;
      params.k_burst = 0;
      params.baseScale = 0;
      
      // Ensure complete visual void - override ALL visual parameters
      params.trailMix = 0;      // No trails
      params.reflectMix = 0;    // No reflections
      params.colorMix = 0;      // No color
      params.brightMult = 0;    // No brightness
      params.brightness = 0;    // Override default brightness
      params.exposure = 0;      // Override default exposure
      // Only set pointSize if not manually overridden
      if (!this.isManuallyOverridden('pointSize')) {
        params.pointSize = 0;     // No particle size
      }
      params.trailFade = 1.0;   // Instant trail fade
      params.splatThresh = 999; // No particles visible
    }
    
    // Reset FSCTF systems to dormant state
    if (window.graceOperator && (!params || !params.fsctfEnabled)) {
      window.graceOperator.morphicStrands = [];
      window.graceOperator.morphicField = { field: 0, stability: 0, emergence: false };
      console.log('🌑 VOID: Reset Grace Operator (FSCTF disabled)');
    } else if (window.graceOperator) {
      console.log('🌑 VOID: Preserving Grace Operator state (FSCTF active)');
    }
    
    console.log('🌑 VOID PHASE: Universe set to absolute nothingness - no particles, no fields, no energy');
    
    return {
      phase: 'void',
      state: 'absolute_nothingness',
      energy: 0,
      dimensions: 0,
      particles: 0,
      fields: 0
    };
  }

  // Phase 1: Grace Operator - Ex nihilo creation mechanism
  phaseGraceOperator() {
    this.universeState = 'grace_operator';
    
    // Disable forced void so rendering resumes
    window.forceVoid = false;
    
    const params = window.params;
    
    // PROTECT A/B TESTING and FSCTF EVOLUTION
    if (window.Brain && window.Brain.evaluating) {
      console.log('🧠 A/B PROTECTION: Skipping Grace Operator parameter changes during Brain evaluation');
    } else if (params && params.fsctfEnabled) {
      console.log('🧬 FSCTF PROTECTION: Skipping cosmogenesis parameter override - letting natural evolution proceed');
    } else if (params) {
      // RESTORE PARAMETERS: Begin creation from void (only when FSCTF disabled)
      params.graceAmp = 0.6;   // stronger grace to kickstart emergence
      params.fieldScale = 0.4; // larger field influence
      params.baseScale = 0.2;  // more baseline dynamics
      params.reflectMix = 0.05; // near-zero bireflection during formation
      
      // Restore visibility so particles can appear and center formation
      params.brightness = 1.0;
      params.exposure = 1.0;
      // Only set pointSize if not manually overridden
      if (!this.isManuallyOverridden('pointSize')) {
        params.pointSize = 1.5;
      }
      params.trailFade = 0.98;
      params.splatThresh = 0.1;
      params.trailMix = 0.8;
    }
    
    console.log('⚡ GRACE OPERATOR PHASE: Ex nihilo creation mechanism activated');
    
    return {
      phase: 'grace_operator',
      state: 'creation_initiated',
      energy: 0.6,
      dimensions: 1,
      particles: 'emerging',
      fields: 'grace_field_active'
    };
  }

  // Phase 2: Morphic Recursion - Self-organizing patterns
  phaseMorphicRecursion() {
    this.universeState = 'morphic_recursion';
    
    const params = window.params;
    if (params && !params.fsctfEnabled) {
      params.morphicRecursionDepth = 5;
      params.graceComplexity = 10.0;
      params.burstAmp = 0.3;
      params.k_burst = 0.4;
    }
    
    console.log('🔄 MORPHIC RECURSION PHASE: Self-organizing patterns emerging');
    
    return {
      phase: 'morphic_recursion',
      state: 'self_organization',
      energy: 1.2,
      dimensions: 2,
      particles: 'organizing',
      fields: 'morphic_field_active'
    };
  }

  // Phase 3: Dimensional Bridge - Physical constants emerge
  phaseDimensionalBridge() {
    this.universeState = 'dimensional_bridge';
    
    // Calculate physical constants
    if (window.dimensionalBridge) {
      this.physicalConstants = window.dimensionalBridge.getAllConstants();
    }
    
    console.log('🌈 DIMENSIONAL BRIDGE PHASE: Physical constants crystallizing from morphic field');
    
    return {
      phase: 'dimensional_bridge',
      state: 'constants_emerging',
      energy: 2.0,
      dimensions: 3,
      particles: 'stabilizing',
      fields: 'dimensional_coupling',
      constants: this.physicalConstants
    };
  }

  // Phase 4: Standard Model - Fundamental forces and particles
  phaseStandardModel() {
    this.universeState = 'standard_model';
    
    console.log('⚛️ STANDARD MODEL PHASE: Fundamental forces and particles manifesting');
    
    return {
      phase: 'standard_model',
      state: 'forces_active',
      energy: 5.0,
      dimensions: 4,
      particles: 'fundamental_particles',
      fields: 'gauge_fields'
    };
  }

  // Phase 5: Consciousness - P=NP emergence
  phaseConsciousness() {
    this.universeState = 'consciousness';
    
    if (window.primeResonance) {
      const consciousnessState = window.primeResonance.updateConsciousness(10.0, Date.now());
      this.consciousnessEvolution.push(consciousnessState);
    }
    
    console.log('🧠 CONSCIOUSNESS PHASE: P=NP consciousness emergence via prime resonance');
    
    return {
      phase: 'consciousness',
      state: 'consciousness_ignition',
      energy: 10.0,
      dimensions: 'n-dimensional',
      particles: 'conscious_observers',
      fields: 'consciousness_field'
    };
  }

  // Phase 6: Inflation - Exponential expansion
  phaseInflation() {
    this.universeState = 'inflation';
    
    console.log('💥 INFLATION PHASE: Exponential spacetime expansion');
    
    return {
      phase: 'inflation',
      state: 'exponential_expansion',
      energy: 100.0,
      dimensions: 'expanding_spacetime',
      particles: 'inflaton_field',
      fields: 'scalar_field'
    };
  }

  // Phase 7: CMB - Cosmic Microwave Background
  phaseCMB() {
    this.universeState = 'cmb';
    
    // Generate CMB spectrum based on φ-morphic evolution
    this.cmbSpectrum = this.generateCMBSpectrum();
    
    console.log('📡 CMB PHASE: Cosmic Microwave Background - universe becomes observable');
    
    return {
      phase: 'cmb',
      state: 'observable_universe',
      energy: 'background_radiation',
      dimensions: 'cosmic_scale',
      particles: 'photon_decoupling',
      fields: 'electromagnetic_radiation',
      spectrum: this.cmbSpectrum
    };
  }

  // Update topology based on cosmogenesis phase
  updateTopologyFromPhase(phase) {
    const topologyStates = ['torus', 'mobius', 'klein', 'phi-klein'];
    const topologyIndex = Math.min(phase - 1, topologyStates.length - 1);
    
    if (topologyIndex >= 0 && window.params) {
      window.params.topologyMode = topologyStates[topologyIndex];
      console.log(`🌀 Topology Evolution: Phase ${phase} → ${topologyStates[topologyIndex]}`);
    }
  }

  // Generate CMB spectrum with φ-morphic characteristics
  generateCMBSpectrum() {
    const spectrum = [];
    const T_cmb = 2.725; // Kelvin
    
    for (let freq = 10; freq <= 1000; freq += 10) {
      const planck_spectrum = this.planckFunction(freq, T_cmb);
      const phi_modulation = 1 + 0.1 * Math.sin(freq * this.PHI) * Math.cos(freq / this.PHI);
      const intensity = planck_spectrum * phi_modulation;
      
      spectrum.push({ frequency: freq, intensity: intensity });
    }
    
    return spectrum;
  }

  planckFunction(freq, temp) {
    const h = 6.626e-34; // Planck constant
    const c = 3e8;       // Speed of light
    const k = 1.381e-23; // Boltzmann constant
    
    const x = (h * freq * 1e9) / (k * temp); // freq in GHz
    return (2 * h * Math.pow(freq * 1e9, 3)) / (Math.pow(c, 2) * (Math.exp(x) - 1));
  }

  // Get current pipeline state
  getState() {
    return {
      phase: this.cosmogenesisPhase,
      universeState: this.universeState,
      creationEvents: this.creationEvents.length,
      physicalConstants: Object.keys(this.physicalConstants).length,
      consciousnessEvolution: this.consciousnessEvolution.length,
      pipelineHistory: this.pipelineHistory.length,
      cmbSpectrum: this.cmbSpectrum ? this.cmbSpectrum.length : 0
    };
  }

  // Get detailed pipeline history
  getHistory() {
    return this.pipelineHistory;
  }
}
