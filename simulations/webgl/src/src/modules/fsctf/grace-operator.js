/**
 * Grace Operator (𝒢)
 * Seeds first morphic strand from absolute void and manages morphic field evolution
 */

export class GraceOperator {
  constructor() {
    this.morphicField = { field: 0, phase: 0 };
    this.morphicStrands = [];
    this.graceAmplitude = 0;
    this.graceAmplitudeTarget = 0; // Smooth target to avoid 0→1 snap
    this.emergenceTriggered = false;
    this.seedTime = 0;
    
    // φ-constants for morphic calculations
    this.PHI = (1 + Math.sqrt(5)) / 2;
    this.PHI_INV = 1 / this.PHI;
    
    // Morphic strand management
    this.maxStrands = 1000;
    this.strandLifetime = 10000; // milliseconds
    
    console.log('🌟 Grace Operator (𝒢) initialized - ready to seed from absolute void');
  }
  
  /**
   * Trigger first emergence from absolute void
   */
  triggerEmergence() {
    if (this.emergenceTriggered) return;
    
    this.emergenceTriggered = true;
    this.seedTime = Date.now();
    // Set target and ramp smoothly in updateMorphicField (no instant jump)
    this.graceAmplitudeTarget = 0.3;
    
    // Seed only the first morphic strand immediately; additional strands will emerge gradually
    this.createInitialStrand();
    
    console.log('🌟 Grace Operator: First emergence from void initiated');
    console.log(`   Initial strand created with stability ${this.morphicStrands[0]?.stability}`);
  }
  
  /**
   * Create the initial morphic strand that seeds all further emergence
   */
  createInitialStrand() {
    // CHIRALITY GENESIS: First strand is achiral (symmetry unbroken)
    const initialStrand = {
      id: 'genesis',
      x: 0, y: 0, // Born at origin
      stability: 0.5,
      phase: 0,
      amplitude: this.graceAmplitude,
      birthTime: Date.now(),
      generation: 0,
      parent: null,
      φScale: 1.0,
      chirality: 0.0 // ACHIRAL: Genesis strand has no handedness (perfect symmetry)
    };
    
    this.morphicStrands.push(initialStrand);
    this.morphicField.field = this.graceAmplitude;
    
    console.log(`🌟 Grace initialization: ${this.morphicStrands.length} initial strand created (additional strands will emerge gradually)`);
    console.log('   🔄 Chirality distribution:', {
      dextral: this.morphicStrands.filter(s => s.chirality > 0.5).length,
      sinistral: this.morphicStrands.filter(s => s.chirality < -0.5).length,
      achiral: this.morphicStrands.filter(s => Math.abs(s.chirality) < 0.5).length
    });
  }
  
  /**
   * Update Grace Operator and morphic field evolution
   */
  update(params, time) {
    if (!this.emergenceTriggered) return;
    
    const graceComplexity = params.graceComplexity || 1.0;
    const dt = 1.0 / 60.0; // Assume 60 FPS
    
    // Grace Operator status available in UI panels and debug mode
    
    // Update morphic field with φ-recursive evolution
    this.updateMorphicField(graceComplexity, time, dt);
    
    // Evolve existing strands
    this.evolveStrands(params, time, dt);
    
    // Create new strands through φ-recursive emergence
    this.attemptStrandCreation(params, time);
    
    // SAFE ADDITION: Calculate cross-scale morphic resonance (only if enabled)
    this.calculateMorphicResonance();
    
    // Cleanup old/unstable strands
    this.cleanupStrands();
  }
  
  updateMorphicField(complexity, time, dt) {
    // φ-recursive field evolution
    const phaseVelocity = complexity * this.PHI * 0.1;
    this.morphicField.phase += phaseVelocity * dt;
    
    // Field strength from strand collective behavior
    const strandCount = this.morphicStrands.length;
    const avgStability = this.morphicStrands.reduce((sum, s) => sum + s.stability, 0) / 
                        Math.max(1, strandCount);
    
    // Grace field emerges from strand coherence
    const baseField = this.graceAmplitude * Math.sin(this.morphicField.phase);
    const coherenceAmplifier = 1.0 + avgStability * Math.sqrt(strandCount) * 0.1;
    
    this.morphicField.field = baseField * coherenceAmplifier;
    
    // Smoothly ease grace amplitude toward target to avoid abrupt geometry changes
    const target = Math.min(1.5, Math.max(this.graceAmplitudeTarget, this.graceAmplitude));
    const eased = this.graceAmplitude + (target - this.graceAmplitude) * 0.15; // 15% per frame for faster response
    // Tight per-frame clamp
    const delta = Math.max(-0.02, Math.min(0.02, eased - this.graceAmplitude));
    this.graceAmplitude += delta;
  }
  
  evolveStrands(params, time, dt) {
    const currentTime = Date.now();
    
    this.morphicStrands.forEach((strand, index) => {
      // Age-based stability evolution
      const age = (currentTime - strand.birthTime) / 1000.0; // seconds
      const maturityFactor = Math.min(1.0, age / 5.0); // Mature over 5 seconds
      
      // CHIRALITY-MODIFIED EVOLUTION: Handedness affects dynamics
      // Initialize chirality if missing (backwards compatibility)
      if (strand.chirality === undefined) {
        strand.chirality = 0.0; // Default to achiral for old strands
      }
      
      // φ-recursive stability evolution with CHIRALITY COUPLING
      const phiEvolution = Math.cos(time * this.PHI + strand.phase) * 0.1;
      const baseEvolution = Math.sin(time * 0.5 + index * 0.1) * 0.05;
      
      // CHIRALITY EFFECT: Handedness modulates stability evolution
      const chiralityModulation = strand.chirality * Math.sin(time * this.PHI * strand.chirality) * 0.03;
      
      strand.stability += (phiEvolution + baseEvolution + chiralityModulation) * dt * maturityFactor;
      strand.stability = Math.max(0, Math.min(2.0, strand.stability));
      
      // Amplitude follows φ-scaling with CHIRAL ASYMMETRY
      strand.amplitude *= Math.pow(this.PHI_INV, dt * 0.1); // Gradual decay
      strand.amplitude = Math.max(0.01, strand.amplitude);
      
      // CHIRAL PHASE EVOLUTION: Handedness affects rotational direction
      const chiralPhaseVelocity = strand.chirality * this.PHI * 0.5; // Chiral contribution
      strand.phase += (this.PHI * strand.stability + chiralPhaseVelocity) * dt;
      
      // CHIRALITY EVOLUTION: Handedness can intensify or weaken over time
      if (Math.abs(strand.chirality) > 0.1) { // Only for strongly chiral strands
        // Chirality can amplify through morphic resonance with similar strands
        const nearbyChiralStrands = this.morphicStrands.filter(other => {
          if (other === strand) return false;
          const distance = Math.sqrt((other.x - strand.x)**2 + (other.y - strand.y)**2);
          const chiralitySame = Math.sign(other.chirality) === Math.sign(strand.chirality);
          return distance < 5.0 && chiralitySame && Math.abs(other.chirality) > 0.1;
        });
        
        // Resonance amplifies chirality (like-handed strands reinforce each other)
        const resonanceAmplification = nearbyChiralStrands.length * 0.01 * dt;
        strand.chirality *= (1.0 + resonanceAmplification);
        strand.chirality = Math.max(-2.0, Math.min(2.0, strand.chirality)); // Clamp
      }
      
      // POSITION DRIFT DUE TO CHIRALITY: Chiral strands spiral outward
      if (Math.abs(strand.chirality) > 0.1) {
        const spiralRadius = 0.1 * dt * Math.abs(strand.chirality);
        const spiralAngle = strand.phase + strand.chirality * time * 0.1;
        strand.x += spiralRadius * Math.cos(spiralAngle);
        strand.y += spiralRadius * Math.sin(spiralAngle);
      }
    });
  }
  
  attemptStrandCreation(params, time) {
    const strandCount = this.morphicStrands.length;
    if (strandCount >= this.maxStrands) return;
    
    // Creation probability based on field strength and complexity (accelerated for testing)
    const fieldStrength = Math.abs(this.morphicField.field);
    const complexity = params.graceComplexity || 1.0;
    let creationRate = fieldStrength * complexity * 0.15; // 8x faster strand creation for dynamic evolution
    // During first 2 seconds post-seed, reduce rate to avoid abrupt jumps
    if (this.emergenceTriggered && (Date.now() - this.seedTime) < 2000) {
      creationRate *= 0.25;
    }
    
    if (Math.random() < creationRate) {
      this.createNewStrand(time);
    }
  }
  
  createNewStrand(time) {
    // Find parent strand (highest stability)
    const parentStrand = this.morphicStrands.reduce((best, strand) => 
      strand.stability > best.stability ? strand : best, this.morphicStrands[0]);
    
    if (!parentStrand) return;
    
    // Initialize parent chirality if missing (backwards compatibility)
    if (parentStrand.chirality === undefined) {
      parentStrand.chirality = 0.0;
    }
    
    // φ-recursive positioning around parent with CHIRAL INFLUENCE
    const baseAngle = time * this.PHI + parentStrand.phase;
    // CHIRALITY AFFECTS SPAWN ANGLE: Chiral parents create twisted offspring positioning
    const chiralAngleOffset = parentStrand.chirality * this.PHI * 0.5; 
    const angle = baseAngle + chiralAngleOffset;
    
    const distance = parentStrand.amplitude * this.PHI;
    const newPosition = {
      x: parentStrand.x + Math.cos(angle) * distance,
      y: parentStrand.y + Math.sin(angle) * distance
    };
    
    // CHIRALITY INHERITANCE AND EVOLUTION
    let newChirality;
    if (Math.abs(parentStrand.chirality) < 0.1) {
      // ACHIRAL PARENT: Offspring can spontaneously break chirality symmetry
      const spontaneousChirality = Math.sin(newPosition.x * this.PHI + newPosition.y / this.PHI) * 
                                  Math.cos(newPosition.y * this.PHI - newPosition.x / this.PHI);
      newChirality = spontaneousChirality > 0.2 ? 0.5 :  // Weak right-handed
                    spontaneousChirality < -0.2 ? -0.5 : // Weak left-handed
                    0.0; // Remains achiral
    } else {
      // CHIRAL PARENT: Chirality is inherited with some evolution
      const inheritanceFactor = 0.7 + Math.random() * 0.6; // 0.7 to 1.3
      const mutationFactor = (Math.random() - 0.5) * 0.2; // ±10% mutation
      newChirality = parentStrand.chirality * inheritanceFactor + mutationFactor;
      
      // 5% chance of chirality inversion (rare but important for diversity)
      if (Math.random() < 0.05) {
        newChirality *= -1;
        console.log(`🔄 Chirality inversion: Parent ${parentStrand.chirality.toFixed(2)} → Child ${newChirality.toFixed(2)}`);
      }
    }
    
    // Clamp chirality to reasonable bounds
    newChirality = Math.max(-2.0, Math.min(2.0, newChirality));
    
    const newStrand = {
      id: `strand_${Date.now()}_${Math.random()}`,
      x: newPosition.x,
      y: newPosition.y,
      stability: parentStrand.stability * this.PHI_INV * (0.8 + Math.random() * 0.4),
      phase: angle,
      amplitude: parentStrand.amplitude * this.PHI_INV,
      birthTime: Date.now(),
      generation: (parentStrand.generation || 0) + 1,
      parent: parentStrand.id,
      φScale: parentStrand.φScale * this.PHI_INV,
      chirality: newChirality // CHIRALITY INHERITANCE
    };
    
    this.morphicStrands.push(newStrand);
    
    // Debug logging for significant chirality events (every 10th strand)
    if (this.morphicStrands.length % 10 === 0) {
      const chiralityStats = {
        dextral: this.morphicStrands.filter(s => s.chirality > 0.3).length,
        sinistral: this.morphicStrands.filter(s => s.chirality < -0.3).length,
        achiral: this.morphicStrands.filter(s => Math.abs(s.chirality) <= 0.3).length
      };
      console.log(`🧬 Chirality evolution (${this.morphicStrands.length} strands):`, chiralityStats);
    }
  }
  
  cleanupStrands() {
    const currentTime = Date.now();
    
    // Remove old or highly unstable strands
    this.morphicStrands = this.morphicStrands.filter(strand => {
      const age = currentTime - strand.birthTime;
      const tooOld = age > this.strandLifetime;
      const tooUnstable = strand.stability < 0.01;
      
      return !tooOld && !tooUnstable;
    });
  }
  
  /**
   * Get current state for visualization and tracking
   */
  getState() {
    return {
      field: this.morphicField.field,
      phase: this.morphicField.phase,
      amplitude: this.graceAmplitude,
      strandCount: this.morphicStrands.length,
      avgStability: this.morphicStrands.length > 0 ? 
        this.morphicStrands.reduce((sum, s) => sum + s.stability, 0) / this.morphicStrands.length : 0,
      emergenceTriggered: this.emergenceTriggered,
      generations: Math.max(...this.morphicStrands.map(s => s.generation || 0), 0)
    };
  }
  
  /**
   * Get strands for rendering with chirality information
   */
  getStrandsForRendering() {
    return this.morphicStrands.map(strand => ({
      x: strand.x,
      y: strand.y,
      stability: strand.stability,
      amplitude: strand.amplitude,
      phase: strand.phase,
      generation: strand.generation || 0,
      chirality: strand.chirality || 0.0 // Include chirality for shader visualization
    }));
  }
  
  /**
   * Reset to void state (PRESERVES user-enabled advanced features)
   */
  reset() {
    // CRITICAL FIX: Preserve user-enabled advanced features during cosmogenesis reset
    const preservedAdvancedSettings = {
      enableCrossScaleResonance: this.enableCrossScaleResonance
    };
    
    this.morphicField = { field: 0, phase: 0 };
    this.morphicStrands = [];
    this.graceAmplitude = 0;
    this.emergenceTriggered = false;
    this.seedTime = 0;
    
    // RESTORE user settings instead of forcing them off
    this.enableCrossScaleResonance = preservedAdvancedSettings.enableCrossScaleResonance;
    
    console.log('🌟 Grace Operator reset to void state (advanced features preserved)');
    if (this.enableCrossScaleResonance) {
      console.log('   ✅ Cross-Scale Morphic Resonance: PRESERVED');
    }
  }
  
  // === ADVANCED FSCTF ENHANCEMENT: Cross-Scale Morphic Resonance ===
  
  /**
   * Enhanced morphic resonance with φ-recursive cross-coupling (SAFE ADDITION)
   */
  calculateMorphicResonance() {
    if (!this.enableCrossScaleResonance) return; // Off by default
    
    // PERFORMANCE FIX: Throttle expensive resonance calculations
    const now = performance.now();
    if (!this._lastResonanceCalc) this._lastResonanceCalc = 0;
    if (now - this._lastResonanceCalc < 200) return; // Only calculate every 200ms
    this._lastResonanceCalc = now;
    
    const φ = this.PHI;
    const strandCount = this.morphicStrands.length;
    if (strandCount < 2) return; // Need at least 2 strands for resonance
    
    // PERFORMANCE FIX: Remove frequent console logging that causes jitter
    if (strandCount > 50) {
      console.log(`🌀 High strand count (${strandCount}) - optimizing resonance calculations`);
    }
    
    // Create resonance matrix between all strands
    this.morphicStrands.forEach((strandA, i) => {
      let totalResonance = 0;
      let resonanceContributions = 0;
      
      this.morphicStrands.forEach((strandB, j) => {
        if (i === j) return; // Don't resonate with self
        
        const distance = Math.sqrt(
          (strandA.x - strandB.x) ** 2 + 
          (strandA.y - strandB.y) ** 2
        );
        
        if (distance > 10.0) return; // Limit resonance range for performance
        
        // φ-harmonic resonance calculation
        const φDistance = distance * φ;
        const resonanceStrength = Math.sin(φDistance) * Math.cos(φDistance / φ);
        
        // Chirality affects resonance (like chiralities attract, opposite repel)
        const chiralityA = strandA.chirality || 0;
        const chiralityB = strandB.chirality || 0;
        const chiralityFactor = chiralityA * chiralityB > 0 ? 1.2 : 0.8;
        
        // Generation-based resonance (deeper generations have stronger coupling)
        const genA = strandA.generation || 0;
        const genB = strandB.generation || 0;
        const generationCoupling = Math.pow(φ, -Math.abs(genA - genB) * 0.5);
        
        // Stability-based coupling (stable strands resonate more strongly)
        const stabilityFactor = Math.sqrt((strandA.stability || 0.5) * (strandB.stability || 0.5));
        
        const resonance = resonanceStrength * chiralityFactor * generationCoupling * stabilityFactor;
        totalResonance += resonance / (1 + distance * 0.1); // Distance-weighted
        resonanceContributions++;
      });
      
      if (resonanceContributions > 0) {
        // Apply resonance back to strand properties (small, safe changes)
        const avgResonance = totalResonance / resonanceContributions;
        strandA.resonanceField = avgResonance;
        
        // Resonance slightly boosts stability and amplitude
        strandA.stability += avgResonance * 0.01; // Very small change
        strandA.amplitude *= (1 + avgResonance * 0.005); // Very small boost
        
        // Clamp values to prevent runaway growth
        strandA.stability = Math.max(0, Math.min(2.0, strandA.stability));
        strandA.amplitude = Math.max(0.01, Math.min(2.0, strandA.amplitude));
      } else {
        strandA.resonanceField = 0;
      }
    });
  }
  
  /**
   * Calculate collective morphic field patterns (SAFE ADDITION)
   */
  calculateCollectivePatterns() {
    if (!this.enableCrossScaleResonance || this.morphicStrands.length < 3) return null;
    
    // Detect emergent collective patterns in strand arrangements
    const patterns = {
      spiralFormations: this.detectSpiralFormations(),
      symmetryBreaking: this.detectSymmetryBreaking(),
      coherentClusters: this.detectCoherentClusters(),
      phaseTransitions: this.detectPhaseTransitions()
    };
    
    return patterns;
  }
  
  /**
   * Detect φ-spiral formations in strand positions
   */
  detectSpiralFormations() {
    const φ = this.PHI;
    let spiralCount = 0;
    
    // Look for strands arranged in golden ratio spirals
    for (let i = 0; i < this.morphicStrands.length - 2; i++) {
      const strand1 = this.morphicStrands[i];
      const strand2 = this.morphicStrands[i + 1];
      const strand3 = this.morphicStrands[i + 2];
      
      // Calculate distances
      const d12 = Math.sqrt((strand1.x - strand2.x)**2 + (strand1.y - strand2.y)**2);
      const d23 = Math.sqrt((strand2.x - strand3.x)**2 + (strand2.y - strand3.y)**2);
      
      // Check if distances follow φ ratio
      const ratio = d23 / d12;
      if (Math.abs(ratio - φ) < 0.2) {
        spiralCount++;
      }
    }
    
    return spiralCount;
  }
  
  /**
   * Detect chirality symmetry breaking events
   */
  detectSymmetryBreaking() {
    const leftHanded = this.morphicStrands.filter(s => (s.chirality || 0) < -0.3).length;
    const rightHanded = this.morphicStrands.filter(s => (s.chirality || 0) > 0.3).length;
    const achiral = this.morphicStrands.filter(s => Math.abs(s.chirality || 0) <= 0.3).length;
    
    // Symmetry breaking when one handedness dominates
    const totalChiral = leftHanded + rightHanded;
    const asymmetry = totalChiral > 0 ? Math.abs(leftHanded - rightHanded) / totalChiral : 0;
    
    return {
      leftHanded,
      rightHanded, 
      achiral,
      asymmetryLevel: asymmetry
    };
  }
  
  /**
   * Detect coherent strand clusters
   */
  detectCoherentClusters() {
    const clusters = [];
    const visited = new Set();
    
    this.morphicStrands.forEach((strand, i) => {
      if (visited.has(i)) return;
      
      const cluster = [strand];
      visited.add(i);
      
      // Find nearby strands with similar properties
      this.morphicStrands.forEach((otherStrand, j) => {
        if (i === j || visited.has(j)) return;
        
        const distance = Math.sqrt(
          (strand.x - otherStrand.x)**2 + (strand.y - otherStrand.y)**2
        );
        
        // Similar phase and chirality = coherent cluster
        const phaseDiff = Math.abs((strand.phase || 0) - (otherStrand.phase || 0));
        const chiralSimilar = Math.abs((strand.chirality || 0) - (otherStrand.chirality || 0)) < 0.5;
        
        if (distance < 2.0 && phaseDiff < 1.0 && chiralSimilar) {
          cluster.push(otherStrand);
          visited.add(j);
        }
      });
      
      if (cluster.length >= 3) {
        clusters.push(cluster);
      }
    });
    
    return clusters.length;
  }
  
  /**
   * Detect emergent phase transitions in the morphic field
   */
  detectPhaseTransitions() {
    // Calculate field gradient and look for discontinuities
    const fieldStrength = this.morphicField.field || 0;
    const fieldPhase = this.morphicField.phase || 0;
    
    // Store history for transition detection
    if (!this.fieldHistory) this.fieldHistory = [];
    this.fieldHistory.push({ strength: fieldStrength, phase: fieldPhase, time: Date.now() });
    
    // Keep only recent history
    if (this.fieldHistory.length > 20) {
      this.fieldHistory.shift();
    }
    
    // Detect sudden changes (phase transitions)
    if (this.fieldHistory.length >= 3) {
      const recent = this.fieldHistory.slice(-3);
      const strengthChange = Math.abs(recent[2].strength - recent[0].strength);
      const phaseChange = Math.abs(recent[2].phase - recent[0].phase);
      
      return strengthChange > 0.5 || phaseChange > Math.PI;
    }
    
    return false;
  }
  
  /**
   * Toggle advanced cross-scale resonance (SAFE TOGGLE)
   */
  toggleAdvancedResonance() {
    this.enableCrossScaleResonance = !this.enableCrossScaleResonance;
    console.log(`🌀 Cross-scale morphic resonance: ${this.enableCrossScaleResonance ? 'ENABLED' : 'DISABLED'}`);
    
    if (this.enableCrossScaleResonance) {
      console.log('   ✨ Collective behaviors between morphic strands activated');
      console.log('   ✨ φ-spiral formations and coherent clustering enabled'); 
      console.log('   ✨ Chirality symmetry breaking detection active');
      
      // Initialize advanced properties if not present
      this.morphicStrands.forEach(strand => {
        if (strand.resonanceField === undefined) strand.resonanceField = 0;
      });
    } else {
      console.log('   ❌ Advanced resonance disabled - back to independent strand evolution');
    }
    
    return this.enableCrossScaleResonance;
  }
  
  /**
   * Get enhanced state with resonance information (SAFE ADDITION)
   */
  getEnhancedState() {
    const basicState = this.getState();
    
    if (!this.enableCrossScaleResonance) {
      return { ...basicState, crossScaleResonance: null };
    }
    
    const collectivePatterns = this.calculateCollectivePatterns();
    const avgResonance = this.morphicStrands.length > 0 ?
      this.morphicStrands.reduce((sum, s) => sum + (s.resonanceField || 0), 0) / this.morphicStrands.length : 0;
    
    return {
      ...basicState,
      crossScaleResonance: {
        enabled: true,
        averageResonance: avgResonance,
        collectivePatterns: collectivePatterns,
        resonantStrands: this.morphicStrands.filter(s => (s.resonanceField || 0) > 0.1).length
      }
    };
  }
  
  // Safe defaults for new properties
  enableCrossScaleResonance = false; // Off by default - safe
}

/**
 * Object pool for morphic strands to reduce GC pressure
 */
export class StrandPool {
  constructor(maxSize = 1000) {
    this.pool = [];
    this.maxSize = maxSize;
    this.activeStrands = new Set();
  }
  
  acquire() {
    if (this.pool.length > 0) {
      return this.pool.pop();
    }
    return this.createNewStrand();
  }
  
  release(strand) {
    if (this.pool.length < this.maxSize) {
      this.resetStrand(strand);
      this.pool.push(strand);
    }
  }
  
  createNewStrand() {
    return {
      id: null,
      x: 0, y: 0, z: 0,
      stability: 0,
      phase: 0,
      amplitude: 0,
      birthTime: 0,
      generation: 0,
      parent: null,
      φScale: 1.0,
      chirality: 0.0
    };
  }
  
  resetStrand(strand) {
    strand.id = null;
    strand.x = strand.y = strand.z = 0;
    strand.stability = strand.phase = strand.amplitude = 0;
    strand.birthTime = strand.generation = 0;
    strand.parent = null;
    strand.φScale = 1.0;
    strand.chirality = 0.0;
  }
}
