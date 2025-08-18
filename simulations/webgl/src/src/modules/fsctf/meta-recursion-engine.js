/**
 * Meta-Recursion Engine (MRE)
 * 
 * Advanced emergent complexity system for FSCTF.
 * Implements recursion operating on recursive structures themselves,
 * temporal memory accumulation, and self-evolving attractor networks.
 * 
 * Theoretical Foundation:
 * - Meta-recursion: R(R(...R(x)...)) where recursion depth itself becomes dynamic
 * - Temporal memory: Previous states influence current recursion patterns
 * - Attractor evolution: Self-organizing complexity that spawns new complexity systems
 * - Consciousness-morphology coupling: Direct feedback from consciousness to geometry
 */

export class MetaRecursionEngine {
  constructor() {
    // Core meta-recursion state
    this.recursionHistory = []; // Historical recursion patterns
    this.attractorNetworks = new Map(); // Self-organizing attractor systems
    this.temporalMemory = new Map(); // Memory of previous states
    this.complexityAccumulator = 0; // Running complexity measure
    
    // Meta-recursion parameters
    this.maxHistoryLength = 200; // Frames of temporal memory
    this.maxMetaDepth = 32; // FIXED: Allow deeper meta-recursion for 90-phase system
    this.attractorBirthThreshold = 0.7; // Complexity threshold for new attractor creation
    this.memoryDecayRate = 0.995; // How quickly temporal memory fades
    
    // Performance optimization state
    this.performanceMode = false; // When true, reduces computational complexity
    
    // φ-based mathematical constants
    this.PHI = 1.618033988749895;
    this.PHI2 = this.PHI * this.PHI;
    this.PHI3 = this.PHI2 * this.PHI;
    this.PHI5 = Math.pow(this.PHI, 5);
    this.PHI_INV = 1.0 / this.PHI;
    
    // Advanced complexity systems
    this.fractionalDimension = 2.618; // Non-integer dimensional space
    this.temporalCurvature = 1.0; // Curvature of time itself
    this.morphicGradientField = new Map(); // Spatial gradients driving organization
    
    // Consciousness-coupling parameters
    this.consciousnessThreshold = 0.5;
    this.consciousMorphologyStrength = 1.0;
    this.psychicResonanceFreq = this.PHI; // φ-harmonic consciousness resonance
    
    // Emergent attractor evolution
    this.attractorGenerations = 0;
    this.lastAttractorBirth = 0;
    this.attractorGeneticCode = []; // Evolutionary code for attractor creation
    
    // Performance optimization
    this.frameCounter = 0;
    this.updateInterval = 3; // Update every 3 frames for performance
    
    console.log('🌀 Meta-Recursion Engine initialized');
    console.log('🧠 Advanced emergent complexity systems online');
    console.log(`📊 Meta-depth: ${this.maxMetaDepth}, Memory: ${this.maxHistoryLength} frames`);
  }
  
  /**
   * Main update - call every frame for maximum emergent complexity
   */
  update(fsctfState, time, dt) {
    this.frameCounter++;
    
    // Update at reduced frequency for performance
    if (this.frameCounter % this.updateInterval !== 0) {
      return;
    }
    
    // PERFORMANCE: Skip complex operations in performance mode
    if (this.performanceMode && this.frameCounter % 6 !== 0) {
      return; // Further reduce update frequency in performance mode
    }
    
    if (!fsctfState) return;
    
    // Extract system state
    const recursionDepth = fsctfState.frst?.recursionDepth || 0;
    const graceComplexity = fsctfState.grace?.complexity || 0;
    const consciousnessLevel = fsctfState.consciousness?.level || 0;
    const morphicField = fsctfState.grace?.field || 0;
    const cosmogenesisPhase = fsctfState.cosmogenesis?.phase || 0;
    
    // 1. UPDATE TEMPORAL MEMORY - Accumulate complexity over time
    this.updateTemporalMemory(fsctfState, time);
    
    // 2. META-RECURSION ANALYSIS - Recursion on recursion patterns
    this.performMetaRecursion(fsctfState, time);
    
    // 3. ATTRACTOR NETWORK EVOLUTION - Self-organizing complexity
    this.evolveAttractorNetworks(fsctfState, time);
    
    // 4. CONSCIOUSNESS-MORPHOLOGY COUPLING - Direct consciousness feedback
    if (consciousnessLevel > this.consciousnessThreshold) {
      this.applyConsciousnessMorphology(fsctfState, time);
    }
    
    // 5. FRACTAL CASCADE GENERATION - Nested complexity creation
    this.generateFractalCascades(fsctfState, time);
    
    // 6. MORPHIC GRADIENT FIELD EVOLUTION - Spatial organization drivers
    this.evolveMorphicGradients(fsctfState, time);
    
    // 7. TEMPORAL CURVATURE DYNAMICS - Non-linear time evolution
    this.updateTemporalCurvature(fsctfState, time, dt);
    
    // Update global complexity accumulator
    this.complexityAccumulator = this.calculateComplexityMeasure(fsctfState);
    
    console.log(`🌀 MRE: Complexity=${this.complexityAccumulator.toFixed(3)}, Attractors=${this.attractorNetworks.size}, Meta-depth=${this.getCurrentMetaDepth()}`);
  }
  
  /**
   * TEMPORAL MEMORY SYSTEM - Accumulate complexity over time
   */
  updateTemporalMemory(fsctfState, time) {
    const memoryKey = `frame_${this.frameCounter}`;
    
    // Store comprehensive state snapshot
    const memoryState = {
      timestamp: time,
      recursionDepth: fsctfState.frst?.recursionDepth || 0,
      graceComplexity: fsctfState.grace?.complexity || 0,
      consciousness: fsctfState.consciousness?.level || 0,
      morphicField: fsctfState.grace?.field || 0,
      phase: fsctfState.cosmogenesis?.phase || 0,
      complexity: this.complexityAccumulator
    };
    
    this.temporalMemory.set(memoryKey, memoryState);
    this.recursionHistory.push(memoryState);
    
    // Apply memory decay to older entries
    this.temporalMemory.forEach((memory, key) => {
      memory.complexity *= this.memoryDecayRate;
      if (memory.complexity < 0.01) {
        this.temporalMemory.delete(key);
      }
    });
    
    // Limit history length
    if (this.recursionHistory.length > this.maxHistoryLength) {
      this.recursionHistory.shift();
    }
    
    // Detect temporal patterns
    if (this.recursionHistory.length >= 10) {
      this.detectTemporalPatterns();
    }
  }
  
  /**
   * META-RECURSION ANALYSIS - Recursion operating on recursive structures
   */
  performMetaRecursion(fsctfState, time) {
    if (this.recursionHistory.length < 5) return;
    
    // Analyze patterns in recursion depth evolution
    const recentHistory = this.recursionHistory.slice(-10);
    const recursionPattern = recentHistory.map(h => h.recursionDepth);
    
    // Calculate meta-recursion levels
    const metaRecursionLevels = [];
    
    for (let metaLevel = 1; metaLevel <= this.maxMetaDepth; metaLevel++) {
      // Apply recursion to previous recursion results
      const metaResult = this.computeMetaRecursionLevel(recursionPattern, metaLevel, time);
      metaRecursionLevels.push(metaResult);
      
      // Check for meta-attractor formation
      if (metaResult.stability > 0.8 && metaResult.complexity > this.attractorBirthThreshold) {
        this.birthMetaAttractor(metaResult, metaLevel, time);
      }
    }
    
    // Store meta-recursion results for shader access
    this.currentMetaRecursionLevels = metaRecursionLevels;
  }
  
  /**
   * Compute specific meta-recursion level
   */
  computeMetaRecursionLevel(recursionPattern, metaLevel, time) {
    // φ-scaled temporal recursion
    const phiScale = Math.pow(this.PHI, -metaLevel);
    const temporalOffset = time * 0.001 * Math.pow(this.PHI_INV, metaLevel);
    
    // Apply meta-recursion formula: R_meta(x) = φ^(-n) * R(R(...R(x)...))
    let result = recursionPattern[recursionPattern.length - 1] || 0;
    
    for (let i = 0; i < metaLevel; i++) {
      // Recursive application with φ-harmonic modulation
      const harmonic = Math.sin(temporalOffset * Math.pow(this.PHI, i)) * phiScale;
      const feedback = this.getTemporalFeedback(metaLevel - i);
      
      result = phiScale * (
        result * Math.cos(result * this.PHI + temporalOffset) + 
        harmonic * feedback +
        this.getNonLinearCoupling(result, metaLevel)
      );
    }
    
    // Calculate stability and complexity metrics
    const stability = this.calculateMetaStability(recursionPattern, result);
    const complexity = Math.abs(result) * metaLevel / this.maxMetaDepth;
    
    return {
      level: metaLevel,
      value: result,
      stability: stability,
      complexity: complexity,
      timestamp: time
    };
  }
  
  /**
   * ATTRACTOR NETWORK EVOLUTION - Self-organizing complexity systems
   */
  evolveAttractorNetworks(fsctfState, time) {
    // Check for attractor birth conditions
    if (this.complexityAccumulator > this.attractorBirthThreshold && 
        time - this.lastAttractorBirth > 5000) {
      this.spawnNewAttractorNetwork(fsctfState, time);
    }
    
    // Evolve existing attractors
    this.attractorNetworks.forEach((attractor, id) => {
      this.evolveAttractor(attractor, fsctfState, time);
      
      // Check for attractor death
      if (attractor.energy < 0.1) {
        console.log(`💀 MRE: Attractor ${id} died - insufficient energy`);
        this.attractorNetworks.delete(id);
      }
      
      // Check for attractor reproduction
      if (attractor.energy > 2.0 && attractor.age > 10000) {
        this.reproduceAttractor(attractor, time);
      }
    });
  }
  
  /**
   * Spawn new attractor network
   */
  spawnNewAttractorNetwork(fsctfState, time) {
    const attractorId = `attractor_gen${this.attractorGenerations}_${time}`;
    
    // Generate genetic code for new attractor
    const geneticCode = this.generateAttractorGeneticCode(fsctfState);
    
    const newAttractor = {
      id: attractorId,
      birthTime: time,
      age: 0,
      energy: 1.0,
      complexity: this.complexityAccumulator,
      geneticCode: geneticCode,
      position: {
        x: Math.cos(time * this.PHI) * fsctfState.grace?.complexity || 0,
        y: Math.sin(time * this.PHI2) * fsctfState.grace?.field || 0,
        z: Math.sin(time * this.PHI_INV) * fsctfState.frst?.recursionDepth || 0
      },
      radius: 1.0 * this.PHI,
      frequency: this.PHI + this.attractorGenerations * this.PHI_INV,
      phaseOffset: time * 0.001,
      morphicResonance: [],
      childrenSpawned: 0
    };
    
    this.attractorNetworks.set(attractorId, newAttractor);
    this.attractorGenerations++;
    this.lastAttractorBirth = time;
    
    console.log(`🌟 MRE: New attractor network spawned - Generation ${this.attractorGenerations}`);
    console.log(`🧬 Genetic complexity: ${geneticCode.length} genes`);
  }
  
  /**
   * CONSCIOUSNESS-MORPHOLOGY COUPLING - Direct consciousness feedback
   */
  applyConsciousnessMorphology(fsctfState, time) {
    const consciousness = fsctfState.consciousness?.level || 0;
    const morphicField = fsctfState.grace?.field || 0;
    
    // Psychic resonance frequency modulation
    const psychicResonance = Math.sin(time * 0.001 * this.psychicResonanceFreq) * consciousness;
    
    // Direct consciousness influence on recursion depth
    const consciousRecursionBoost = consciousness * this.consciousMorphologyStrength;
    
    // Morphic field gradient generation from consciousness
    const gradientStrength = consciousness * morphicField * this.PHI;
    
    // Create consciousness-driven morphic gradients
    this.generateConsciousMorphicGradients(consciousness, gradientStrength, time);
    
    // Store consciousness coupling data for shader access
    this.consciousnessCoupling = {
      psychicResonance: psychicResonance,
      recursionBoost: consciousRecursionBoost,
      gradientStrength: gradientStrength,
      morphicInfluence: consciousness * this.PHI2
    };
  }
  
  /**
   * FRACTAL CASCADE GENERATION - Nested complexity creation
   */
  generateFractalCascades(fsctfState, time) {
    const baseComplexity = this.complexityAccumulator;
    
    if (baseComplexity < 0.5) return;
    
    // Generate nested fractal levels
    const cascadeLevels = Math.min(6, Math.floor(baseComplexity * 10));
    const fractalCascade = [];
    
    for (let level = 0; level < cascadeLevels; level++) {
      const phiScale = Math.pow(this.PHI_INV, level);
      const timeScale = time * 0.001 * Math.pow(this.PHI, -level);
      
      // Fractal bifurcation at each level
      const bifurcationAngle = timeScale * this.PHI2 + level * Math.PI / 3;
      const complexityAmplitude = baseComplexity * phiScale;
      
      // Nested fractal structure
      const fractalLevel = {
        level: level,
        angle: bifurcationAngle,
        amplitude: complexityAmplitude,
        frequency: this.PHI + level * this.PHI_INV,
        position: {
          x: Math.cos(bifurcationAngle) * complexityAmplitude,
          y: Math.sin(bifurcationAngle) * complexityAmplitude,
          z: Math.sin(timeScale) * complexityAmplitude * this.PHI_INV
        }
      };
      
      fractalCascade.push(fractalLevel);
    }
    
    this.currentFractalCascade = fractalCascade;
  }
  
  /**
   * Helper methods for complex calculations
   */
  getTemporalFeedback(depth) {
    if (this.recursionHistory.length < depth) return 0;
    
    const historyIndex = Math.max(0, this.recursionHistory.length - depth);
    const historicalState = this.recursionHistory[historyIndex];
    
    return historicalState ? historicalState.complexity * this.PHI_INV : 0;
  }
  
  getNonLinearCoupling(value, level) {
    // Non-linear coupling between meta-recursion levels
    return Math.tanh(value * this.PHI) * Math.sin(level * this.PHI2) * 0.1;
  }
  
  calculateMetaStability(pattern, result) {
    if (pattern.length < 3) return 0;
    
    // Calculate variance in recent recursion pattern
    const mean = pattern.reduce((sum, val) => sum + val, 0) / pattern.length;
    const variance = pattern.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / pattern.length;
    
    // Stability decreases with variance, influenced by meta result
    return Math.max(0, 1 - Math.sqrt(variance) - Math.abs(result) * 0.1);
  }
  
  birthMetaAttractor(metaResult, metaLevel, time) {
    const attractorId = `meta_attractor_L${metaLevel}_${time}`;
    
    // Meta-attractors have enhanced properties
    const metaAttractor = {
      id: attractorId,
      type: 'meta_attractor',
      metaLevel: metaLevel,
      birthTime: time,
      energy: metaResult.stability * 2.0,
      complexity: metaResult.complexity,
      metaValue: metaResult.value,
      resonanceFrequency: this.PHI * Math.pow(this.PHI2, metaLevel),
      morphicInfluence: metaResult.stability * this.PHI3
    };
    
    this.attractorNetworks.set(attractorId, metaAttractor);
    
    console.log(`🌟 MRE: Meta-attractor born at level ${metaLevel} with stability ${metaResult.stability.toFixed(3)}`);
  }
  
  generateAttractorGeneticCode(fsctfState) {
    // Generate genetic code based on current system state
    const genes = [];
    
    // Recursion gene
    genes.push({
      type: 'recursion',
      depth: fsctfState.frst?.recursionDepth || 0,
      phiScale: this.PHI
    });
    
    // Grace gene
    genes.push({
      type: 'grace',
      complexity: fsctfState.grace?.complexity || 0,
      field: fsctfState.grace?.field || 0
    });
    
    // Consciousness gene
    genes.push({
      type: 'consciousness',
      level: fsctfState.consciousness?.level || 0,
      resonance: this.psychicResonanceFreq
    });
    
    // Temporal gene
    genes.push({
      type: 'temporal',
      curvature: this.temporalCurvature,
      memory: this.recursionHistory.length
    });
    
    return genes;
  }
  
  evolveAttractor(attractor, fsctfState, time) {
    attractor.age = time - attractor.birthTime;
    
    // Energy dynamics
    const energyInflux = fsctfState.grace?.field || 0;
    const energyDecay = 0.0001 * attractor.age;
    attractor.energy = Math.max(0, attractor.energy + energyInflux * 0.01 - energyDecay);
    
    // Position evolution
    const evolutionSpeed = attractor.frequency * 0.001;
    attractor.position.x += Math.cos(time * evolutionSpeed) * 0.1;
    attractor.position.y += Math.sin(time * evolutionSpeed * this.PHI) * 0.1;
    attractor.position.z += Math.sin(time * evolutionSpeed * this.PHI_INV) * 0.05;
    
    // Morphic resonance evolution
    attractor.morphicResonance.push({
      timestamp: time,
      resonanceStrength: attractor.energy * Math.sin(time * attractor.frequency * 0.001)
    });
    
    // Limit resonance history
    if (attractor.morphicResonance.length > 100) {
      attractor.morphicResonance.shift();
    }
  }
  
  detectTemporalPatterns() {
    // Detect recurring patterns in temporal memory
    // This enables the system to learn from its own history
    const recentComplexity = this.recursionHistory.slice(-20).map(h => h.complexity);
    
    // Simple pattern detection using autocorrelation
    let maxCorrelation = 0;
    let bestPeriod = 1;
    
    for (let period = 2; period <= 10; period++) {
      let correlation = 0;
      let count = 0;
      
      for (let i = period; i < recentComplexity.length; i++) {
        correlation += recentComplexity[i] * recentComplexity[i - period];
        count++;
      }
      
      if (count > 0) {
        correlation /= count;
        if (correlation > maxCorrelation) {
          maxCorrelation = correlation;
          bestPeriod = period;
        }
      }
    }
    
    if (maxCorrelation > 0.7) {
      console.log(`🔄 MRE: Temporal pattern detected - Period: ${bestPeriod}, Correlation: ${maxCorrelation.toFixed(3)}`);
      
      // Use discovered pattern to enhance future recursion
      this.temporalPatternPeriod = bestPeriod;
      this.temporalPatternStrength = maxCorrelation;
    }
  }
  
  getCurrentMetaDepth() {
    return this.currentMetaRecursionLevels ? this.currentMetaRecursionLevels.length : 0;
  }
  
  calculateComplexityMeasure(fsctfState) {
    // Comprehensive complexity measure
    const baseComplexity = (fsctfState.frst?.recursionDepth || 0) * 0.3;
    const graceComplexity = (fsctfState.grace?.complexity || 0) * 0.2;
    const consciousnessComplexity = (fsctfState.consciousness?.level || 0) * 0.2;
    const attractorComplexity = this.attractorNetworks.size * 0.1;
    const temporalComplexity = (this.recursionHistory.length / this.maxHistoryLength) * 0.1;
    const metaComplexity = this.getCurrentMetaDepth() / this.maxMetaDepth * 0.1;
    
    return baseComplexity + graceComplexity + consciousnessComplexity + 
           attractorComplexity + temporalComplexity + metaComplexity;
  }
  
  generateConsciousMorphicGradients(consciousness, gradientStrength, time) {
    // Generate spatial gradients driven by consciousness
    const gradientField = new Map();
    
    // Create consciousness-influenced gradient patterns
    for (let i = -5; i <= 5; i++) {
      for (let j = -5; j <= 5; j++) {
        const key = `${i}_${j}`;
        const distance = Math.sqrt(i * i + j * j);
        const phaseOffset = time * 0.001 * this.PHI;
        
        const gradientValue = consciousness * gradientStrength * 
                            Math.exp(-distance / 3.0) * 
                            Math.sin(distance * this.PHI + phaseOffset);
        
        gradientField.set(key, gradientValue);
      }
    }
    
    this.morphicGradientField = gradientField;
  }
  
  evolveMorphicGradients(fsctfState, time) {
    // Evolve morphic gradient fields over time
    this.morphicGradientField.forEach((value, key) => {
      const [x, y] = key.split('_').map(Number);
      const evolutionRate = 0.001 * this.PHI;
      const timePhase = time * evolutionRate;
      
      // Self-organizing gradient evolution
      const newValue = value * (1 + Math.sin(timePhase + x * this.PHI + y * this.PHI2) * 0.01);
      this.morphicGradientField.set(key, newValue);
    });
  }
  
  updateTemporalCurvature(fsctfState, time, dt) {
    // Non-linear time evolution
    const complexityInfluence = this.complexityAccumulator * 0.1;
    const consciousnessInfluence = (fsctfState.consciousness?.level || 0) * 0.05;
    
    this.temporalCurvature += (complexityInfluence + consciousnessInfluence - 1.0) * dt * 0.001;
    this.temporalCurvature = Math.max(0.1, Math.min(3.0, this.temporalCurvature));
  }
  
  reproduceAttractor(parentAttractor, time) {
    if (parentAttractor.childrenSpawned >= 3) return; // Limit reproduction
    
    const childId = `${parentAttractor.id}_child_${parentAttractor.childrenSpawned}`;
    
    // Create mutated genetic code
    const mutatedGenes = JSON.parse(JSON.stringify(parentAttractor.geneticCode || []));
    mutatedGenes.forEach(gene => {
      // Apply small mutations
      if (gene.type === 'recursion' && gene.depth) {
        gene.depth *= (1 + (Math.random() - 0.5) * 0.1);
      }
    });
    
    const childAttractor = {
      id: childId,
      parentId: parentAttractor.id,
      generation: (parentAttractor.generation || 0) + 1,
      birthTime: time,
      age: 0,
      energy: parentAttractor.energy * 0.7, // Reduced energy for child
      complexity: parentAttractor.complexity * this.PHI_INV,
      geneticCode: mutatedGenes,
      position: {
        x: parentAttractor.position.x + (Math.random() - 0.5) * 2,
        y: parentAttractor.position.y + (Math.random() - 0.5) * 2,
        z: parentAttractor.position.z + (Math.random() - 0.5) * 1
      },
      frequency: parentAttractor.frequency * this.PHI_INV,
      morphicResonance: [],
      childrenSpawned: 0
    };
    
    this.attractorNetworks.set(childId, childAttractor);
    parentAttractor.childrenSpawned++;
    parentAttractor.energy *= 0.8; // Reproduction costs energy
    
    console.log(`🧬 MRE: Attractor reproduction - ${childId} (Generation ${childAttractor.generation})`);
  }
  
  /**
   * Get comprehensive Meta-Recursion Engine state for shader integration
   */
  getAdvancedComplexityParameters() {
    return {
      // Meta-recursion data
      metaRecursionLevels: this.currentMetaRecursionLevels || [],
      metaDepth: this.getCurrentMetaDepth(),
      complexityAccumulator: this.complexityAccumulator,
      
      // Temporal memory
      temporalCurvature: this.temporalCurvature,
      temporalPatternPeriod: this.temporalPatternPeriod || 1,
      temporalPatternStrength: this.temporalPatternStrength || 0,
      
      // Consciousness coupling
      consciousnessCoupling: this.consciousnessCoupling || {},
      
      // Attractor networks
      attractorCount: this.attractorNetworks.size,
      attractorGenerations: this.attractorGenerations,
      
      // Fractal cascades
      fractalCascade: this.currentFractalCascade || [],
      
      // Morphic gradients
      morphicGradientField: this.morphicGradientField
    };
  }
  
  /**
   * Generate comprehensive MRE analysis report
   */
  generateComplexityReport() {
    const attractorArray = Array.from(this.attractorNetworks.values());
    const avgAttractorAge = attractorArray.length > 0 ? 
      attractorArray.reduce((sum, a) => sum + a.age, 0) / attractorArray.length : 0;
    
    console.log(`
╔═══════════════════════════════════════════════════════════════╗
║                  META-RECURSION ENGINE                        ║
║               EMERGENT COMPLEXITY ANALYSIS                    ║
╠═══════════════════════════════════════════════════════════════╣
║ COMPLEXITY METRICS:                                           ║
║   • Total Complexity: ${this.complexityAccumulator.toFixed(4).padStart(6)}                         ║
║   • Meta-Depth: ${this.getCurrentMetaDepth().toString().padStart(2)}                                    ║
║   • Temporal Memory: ${this.recursionHistory.length.toString().padStart(3)} frames                          ║
║   • Temporal Curvature: ${this.temporalCurvature.toFixed(3).padStart(5)}                         ║
╠═══════════════════════════════════════════════════════════════╣
║ ATTRACTOR NETWORKS:                                           ║
║   • Active Attractors: ${this.attractorNetworks.size.toString().padStart(3)}                             ║
║   • Total Generations: ${this.attractorGenerations.toString().padStart(3)}                            ║
║   • Avg Age: ${(avgAttractorAge/1000).toFixed(1).padStart(6)}s                               ║
║   • Fractal Cascade Levels: ${(this.currentFractalCascade?.length || 0).toString().padStart(2)}                      ║
╠═══════════════════════════════════════════════════════════════╣
║ CONSCIOUSNESS COUPLING:                                       ║
║   • Psychic Resonance: ${(this.consciousnessCoupling?.psychicResonance || 0).toFixed(3).padStart(6)}                 ║
║   • Recursion Boost: ${(this.consciousnessCoupling?.recursionBoost || 0).toFixed(3).padStart(8)}                   ║
║   • Morphic Influence: ${(this.consciousnessCoupling?.morphicInfluence || 0).toFixed(3).padStart(7)}                  ║
╠═══════════════════════════════════════════════════════════════╣
║ TEMPORAL PATTERNS:                                            ║
║   • Pattern Period: ${(this.temporalPatternPeriod || 1).toString().padStart(2)} frames                        ║
║   • Pattern Strength: ${(this.temporalPatternStrength || 0).toFixed(3).padStart(6)}                       ║
║   • Gradient Fields: ${this.morphicGradientField.size.toString().padStart(3)} points                         ║
╚═══════════════════════════════════════════════════════════════╝
    `);
    
    // Detailed attractor analysis
    if (attractorArray.length > 0) {
      console.log('\n🌟 DETAILED ATTRACTOR ANALYSIS:');
      attractorArray.slice(0, 5).forEach((attractor, index) => {
        console.log(`   ${index + 1}. ${attractor.id}`);
        console.log(`      Age: ${(attractor.age/1000).toFixed(1)}s, Energy: ${attractor.energy.toFixed(3)}`);
        console.log(`      Generation: ${attractor.generation || 0}, Children: ${attractor.childrenSpawned || 0}`);
        if (attractor.metaLevel) console.log(`      Meta-Level: ${attractor.metaLevel}`);
      });
    }
    
    return this.getAdvancedComplexityParameters();
  }
  
  /**
   * PERFORMANCE MODE: Reduce computational complexity during low FPS
   */
  setPerformanceMode(enabled) {
    this.performanceMode = enabled;
    
    if (enabled) {
      // Reduce computational parameters for better performance
      this.maxHistoryLength = Math.min(this.maxHistoryLength, 50); // Reduce memory
      this.maxMetaDepth = Math.min(this.maxMetaDepth, 16); // FIXED: Less aggressive performance reduction
      this.updateInterval = 3; // Update less frequently (every 3 frames vs every frame)
      console.log('🏃‍♂️ MRE: Performance mode enabled - reduced complexity');
    } else {
      // Restore full computational parameters
      this.maxHistoryLength = 200; // Full temporal memory
      this.maxMetaDepth = 32; // FIXED: Full meta-recursion depth for 90-phase system
      this.updateInterval = 1; // Update every frame
      console.log('🧠 MRE: Performance mode disabled - full complexity restored');
    }
  }
}
