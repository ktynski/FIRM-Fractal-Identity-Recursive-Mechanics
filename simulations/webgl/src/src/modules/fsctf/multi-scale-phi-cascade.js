/**
 * Multi-Scale φ-Cascade Hierarchy System
 * 
 * CRITICAL MISSING PIECE: True emergent complexity through scale-crossing interactions
 * 
 * Creates 7-level φ-scaled hierarchy where emergence happens BETWEEN scales
 * This is where true FSCTF complexity comes from - not single-scale dynamics
 */

export class MultiScalePhiCascade {
  constructor() {
    this.φ = (1 + Math.sqrt(5)) / 2;
    this.φ_inv = 1 / this.φ;
    this.enabled = false; // Safe default - enable via keyboard shortcut
    
    // 7-level φ-cascade hierarchy (each level φ times smaller than previous)
    this.cascadeLevels = [
      { 
        name: "Cosmic",           scale: 1.0,              strandCount: 89,  
        color: [0.9, 0.1, 0.9],   description: "Universal patterns and cosmic topology"
      },
      { 
        name: "Galactic",         scale: this.φ_inv,       strandCount: 144, 
        color: [0.1, 0.5, 0.9],   description: "Galactic-scale morphic resonance fields"
      },
      { 
        name: "Stellar",          scale: this.φ_inv**2,    strandCount: 233, 
        color: [0.1, 0.9, 0.5],   description: "Star formation and gravitational patterns"
      },
      { 
        name: "Planetary",        scale: this.φ_inv**3,    strandCount: 377, 
        color: [0.9, 0.9, 0.1],   description: "Planetary system dynamics"
      },
      { 
        name: "Biological",       scale: this.φ_inv**4,    strandCount: 610, 
        color: [0.9, 0.5, 0.1],   description: "Life emergence and evolution patterns"
      },
      { 
        name: "Molecular",        scale: this.φ_inv**5,    strandCount: 987, 
        color: [0.9, 0.1, 0.1],   description: "Chemical bond and molecular structures"
      },
      { 
        name: "Quantum",          scale: this.φ_inv**6,    strandCount: 1597,
        color: [0.5, 0.1, 0.9],   description: "Quantum field fluctuations and virtual particles"
      }
    ];
    
    // Initialize each level with its morphic strands
    this.cascadeLevels.forEach(level => {
      level.morphicStrands = [];
      level.φResonance = 0.0;
      level.emergenceIntensity = 0.0;
      level.upwardInfluence = 0.0;    // How this level affects larger scales
      level.downwardInfluence = 0.0;  // How this level affects smaller scales
      level.lastUpdate = 0;
    });
    
    // Cross-scale interaction matrix (7x7)
    this.crossScaleInteractions = new Array(7).fill(0).map(() => new Array(7).fill(0));
    
    // Emergence hotspots - where cross-scale patterns create new behaviors
    this.emergenceHotspots = [];
    this.maxHotspots = 50;
    
    // Performance controls
    this.updateInterval = 200; // Update every 200ms for performance
    this.lastGlobalUpdate = 0;
    
    console.log('🌊 Multi-Scale φ-Cascade Hierarchy initialized');
    console.log('   ✨ 7 levels from Cosmic to Quantum scales');
    console.log('   🔗 Cross-scale resonance matrix active');
    console.log('   ⚡ Emergence hotspots detection enabled');
  }
  
  /**
   * CORE METHOD: Update multi-scale cascade with cross-scale resonance
   */
  updateCascade(morphicField, graceOperator, time) {
    if (!this.enabled) return null;
    
    const now = performance.now();
    if (now - this.lastGlobalUpdate < this.updateInterval) return this.getState();
    
    try {
      // Step 1: Update individual scale dynamics
      this.updateIndividualScales(morphicField, graceOperator, time);
      
      // Step 2: Calculate cross-scale φ-interference patterns
      this.calculateCrossScaleInterference();
      
      // Step 3: Detect emergence hotspots between scales  
      this.detectEmergenceHotspots();
      
      // Step 4: Apply cross-scale feedback
      this.applyCrossScaleFeedback();
      
      this.lastGlobalUpdate = now;
      
      // Log major emergence events
      const totalEmergence = this.getTotalEmergenceIntensity();
      if (totalEmergence > 5.0 && now % 5000 < this.updateInterval) {
        console.log(`🌊 φ-Cascade MAJOR EMERGENCE: Total intensity ${totalEmergence.toFixed(2)}`);
        console.log(`   🔥 Active hotspots: ${this.emergenceHotspots.length}`);
        this.logActiveScales();
      }
      
      return this.getState();
      
    } catch (error) {
      console.warn('🌊 Multi-Scale Cascade: Safe fallback due to:', error.message);
      this.enabled = false; // Safe disable on error
      return null;
    }
  }
  
  /**
   * Update dynamics within each scale level
   */
  updateIndividualScales(morphicField, graceOperator, time) {
    const baseField = morphicField?.field || 0;
    const basePhase = morphicField?.phase || 0;
    const morphicStrands = graceOperator?.morphicStrands || [];
    
    this.cascadeLevels.forEach((level, index) => {
      // Each scale gets φ-scaled version of base morphic field
      const scaleField = baseField * Math.pow(this.φ, index - 3); // Center around level 3
      const scalePhase = basePhase + index * this.φ * 0.1;
      
      // Update φ-resonance for this scale
      level.φResonance = this.calculateScalePhiResonance(level, scaleField, scalePhase, time);
      
      // Create scale-specific morphic strands if field is strong enough
      if (Math.abs(scaleField) > 0.1 && level.morphicStrands.length < level.strandCount) {
        this.createScaleMorphicStrand(level, scaleField, scalePhase, time);
      }
      
      // Update existing strands for this scale
      level.morphicStrands = level.morphicStrands.filter(strand => {
        strand.lifetime += 0.016; // ~60fps
        strand.φPhase += level.φResonance * 0.01;
        strand.intensity *= 0.995; // Gradual decay
        
        return strand.lifetime < 10.0 && strand.intensity > 0.01;
      });
    });
  }
  
  /**
   * CRITICAL: Calculate φ-interference between adjacent scales
   */
  calculateCrossScaleInterference() {
    for (let i = 0; i < this.cascadeLevels.length; i++) {
      for (let j = 0; j < this.cascadeLevels.length; j++) {
        if (i === j) continue;
        
        const levelA = this.cascadeLevels[i];
        const levelB = this.cascadeLevels[j];
        
        // φ-interference strength based on scale separation
        const scaleSeparation = Math.abs(i - j);
        const φInterference = Math.pow(this.φ_inv, scaleSeparation);
        
        // Resonance coupling between scales
        const resonanceCoupling = levelA.φResonance * levelB.φResonance;
        
        // Cross-scale interaction strength
        this.crossScaleInteractions[i][j] = φInterference * resonanceCoupling * 0.1;
        
        // Adjacent scales have strongest coupling
        if (scaleSeparation === 1) {
          this.crossScaleInteractions[i][j] *= 5.0; // Boost adjacent coupling
          
          // Upward and downward influence
          if (i < j) { // i is larger scale, j is smaller scale
            levelA.downwardInfluence += this.crossScaleInteractions[i][j];
            levelB.upwardInfluence += this.crossScaleInteractions[i][j];
          }
        }
      }
    }
  }
  
  /**
   * Detect emergence hotspots where cross-scale patterns create new behaviors
   */
  detectEmergenceHotspots() {
    this.emergenceHotspots = []; // Reset each update
    
    for (let i = 0; i < this.cascadeLevels.length - 1; i++) {
      const upperScale = this.cascadeLevels[i];
      const lowerScale = this.cascadeLevels[i + 1];
      
      // Look for resonance alignment between adjacent scales
      const resonanceAlignment = Math.abs(upperScale.φResonance - lowerScale.φResonance * this.φ);
      
      if (resonanceAlignment < 0.1) { // Strong alignment = emergence opportunity
        const emergenceIntensity = (upperScale.φResonance + lowerScale.φResonance) / resonanceAlignment;
        
        if (emergenceIntensity > 10.0) { // Emergence threshold
          this.emergenceHotspots.push({
            upperScale: i,
            lowerScale: i + 1,
            intensity: emergenceIntensity,
            φAlignment: resonanceAlignment,
            position: this.calculateHotspotPosition(upperScale, lowerScale),
            emergenceType: this.classifyEmergenceType(i, emergenceIntensity),
            birthTime: performance.now()
          });
        }
      }
    }
    
    // Limit hotspots for performance
    if (this.emergenceHotspots.length > this.maxHotspots) {
      this.emergenceHotspots.sort((a, b) => b.intensity - a.intensity);
      this.emergenceHotspots = this.emergenceHotspots.slice(0, this.maxHotspots);
    }
    
    // Update emergence intensity for each level
    this.cascadeLevels.forEach(level => level.emergenceIntensity = 0);
    this.emergenceHotspots.forEach(hotspot => {
      this.cascadeLevels[hotspot.upperScale].emergenceIntensity += hotspot.intensity * 0.1;
      this.cascadeLevels[hotspot.lowerScale].emergenceIntensity += hotspot.intensity * 0.1;
    });
  }
  
  /**
   * Apply cross-scale feedback - larger scales constrain smaller scales
   */
  applyCrossScaleFeedback() {
    for (let i = 0; i < this.cascadeLevels.length - 1; i++) {
      const upperScale = this.cascadeLevels[i];
      const lowerScale = this.cascadeLevels[i + 1];
      
      // Upper scale provides boundary conditions for lower scale
      const boundaryConstraint = upperScale.φResonance * 0.1;
      
      // Adjust lower scale resonance based on upper scale
      lowerScale.φResonance += boundaryConstraint;
      lowerScale.φResonance = Math.max(-5.0, Math.min(5.0, lowerScale.φResonance)); // Clamp
      
      // Lower scale provides detailed dynamics to upper scale
      const detailFeedback = lowerScale.φResonance * lowerScale.emergenceIntensity * 0.01;
      upperScale.φResonance += detailFeedback;
      upperScale.φResonance = Math.max(-5.0, Math.min(5.0, upperScale.φResonance)); // Clamp
    }
  }
  
  /**
   * Calculate φ-resonance for a specific scale
   */
  calculateScalePhiResonance(level, scaleField, scalePhase, time) {
    const φOscillation = Math.sin(scalePhase + time * 0.001 * level.scale);
    const fieldAmplification = scaleField * Math.pow(this.φ, Math.sin(time * 0.001));
    const scaleModulation = Math.cos(time * 0.001 / level.scale) * this.φ_inv;
    
    return (φOscillation + fieldAmplification + scaleModulation) * level.scale;
  }
  
  /**
   * Create morphic strand specific to a scale level
   */
  createScaleMorphicStrand(level, scaleField, scalePhase, time) {
    const strand = {
      position: [
        Math.random() * 20 - 10,
        Math.random() * 20 - 10,
        Math.random() * 20 - 10
      ],
      velocity: [
        (Math.random() - 0.5) * level.scale,
        (Math.random() - 0.5) * level.scale,
        (Math.random() - 0.5) * level.scale
      ],
      intensity: Math.abs(scaleField) * (0.5 + Math.random() * 0.5),
      φPhase: scalePhase,
      lifetime: 0,
      scale: level.scale,
      color: [...level.color],
      emergenceContribution: 0
    };
    
    level.morphicStrands.push(strand);
  }
  
  /**
   * Calculate hotspot position in 3D space
   */
  calculateHotspotPosition(upperScale, lowerScale) {
    return [
      (Math.random() - 0.5) * 15,
      (Math.random() - 0.5) * 15,
      (Math.random() - 0.5) * 15
    ];
  }
  
  /**
   * Classify the type of emergence occurring
   */
  classifyEmergenceType(scaleLevel, intensity) {
    const types = [
      'Cosmic-Galactic Bridge',
      'Galactic-Stellar Formation', 
      'Stellar-Planetary System',
      'Planetary-Biological Genesis',
      'Biological-Molecular Assembly',
      'Molecular-Quantum Interface'
    ];
    
    let type = types[scaleLevel] || 'Scale Interface';
    
    if (intensity > 50.0) type = `MAJOR ${type}`;
    else if (intensity > 20.0) type = `Significant ${type}`;
    
    return type;
  }
  
  /**
   * Get total emergence intensity across all scales
   */
  getTotalEmergenceIntensity() {
    return this.cascadeLevels.reduce((sum, level) => sum + level.emergenceIntensity, 0);
  }
  
  /**
   * Log currently active scales
   */
  logActiveScales() {
    this.cascadeLevels.forEach((level, index) => {
      if (level.emergenceIntensity > 0.5) {
        console.log(`   ${index}: ${level.name} - φRes: ${level.φResonance.toFixed(2)}, ` +
                   `Emergence: ${level.emergenceIntensity.toFixed(2)}, ` +
                   `Strands: ${level.morphicStrands.length}`);
      }
    });
  }
  
  /**
   * Get rendering data for all scale levels
   */
  getVisualizationData() {
    if (!this.enabled) return null;
    
    const scaleData = this.cascadeLevels.map((level, index) => ({
      name: level.name,
      scale: level.scale,
      φResonance: level.φResonance,
      emergenceIntensity: level.emergenceIntensity,
      strandCount: level.morphicStrands.length,
      color: level.color,
      upwardInfluence: level.upwardInfluence,
      downwardInfluence: level.downwardInfluence,
      morphicStrands: level.morphicStrands.map(strand => ({
        position: strand.position,
        intensity: strand.intensity,
        φPhase: strand.φPhase,
        color: strand.color,
        scale: strand.scale
      }))
    }));
    
    return {
      scales: scaleData,
      emergenceHotspots: this.emergenceHotspots,
      crossScaleInteractions: this.crossScaleInteractions,
      totalEmergence: this.getTotalEmergenceIntensity(),
      activeHotspots: this.emergenceHotspots.length
    };
  }
  
  /**
   * Get state for integration with existing systems
   */
  getState() {
    if (!this.enabled) {
      return {
        enabled: false,
        totalEmergence: 0,
        activeScales: 0,
        hotspots: 0
      };
    }
    
    const activeScales = this.cascadeLevels.filter(level => level.emergenceIntensity > 0.1).length;
    
    return {
      enabled: true,
      totalEmergence: this.getTotalEmergenceIntensity(),
      activeScales: activeScales,
      hotspots: this.emergenceHotspots.length,
      cascadeLevels: this.cascadeLevels.length,
      φInteractionStrength: this.getAverageInteractionStrength(),
      dominantScale: this.getDominantScale(),
      emergenceRate: this.calculateEmergenceRate()
    };
  }
  
  /**
   * Get average interaction strength across scales
   */
  getAverageInteractionStrength() {
    let total = 0, count = 0;
    for (let i = 0; i < 7; i++) {
      for (let j = 0; j < 7; j++) {
        if (i !== j) {
          total += Math.abs(this.crossScaleInteractions[i][j]);
          count++;
        }
      }
    }
    return count > 0 ? total / count : 0;
  }
  
  /**
   * Get scale with highest emergence intensity
   */
  getDominantScale() {
    let maxIntensity = 0, dominantIndex = 0;
    this.cascadeLevels.forEach((level, index) => {
      if (level.emergenceIntensity > maxIntensity) {
        maxIntensity = level.emergenceIntensity;
        dominantIndex = index;
      }
    });
    return {
      index: dominantIndex,
      name: this.cascadeLevels[dominantIndex].name,
      intensity: maxIntensity
    };
  }
  
  /**
   * Calculate rate of emergence (hotspots created per second)
   */
  calculateEmergenceRate() {
    const recentHotspots = this.emergenceHotspots.filter(
      hotspot => performance.now() - hotspot.birthTime < 1000
    );
    return recentHotspots.length; // Hotspots per second
  }
  
  /**
   * Enable/disable the cascade system
   */
  setEnabled(enabled) {
    this.enabled = enabled;
    if (enabled) {
      console.log('🌊 Multi-Scale φ-Cascade ACTIVATED!');
      console.log('   🔗 Cross-scale resonance patterns active');
      console.log('   ⚡ Emergence hotspot detection online');
      console.log('   📊 7-level hierarchy from Cosmic to Quantum scales');
    } else {
      console.log('🌊 Multi-Scale φ-Cascade deactivated');
    }
  }
  
  /**
   * Reset all scales to initial state
   */
  reset() {
    this.cascadeLevels.forEach(level => {
      level.morphicStrands = [];
      level.φResonance = 0.0;
      level.emergenceIntensity = 0.0;
      level.upwardInfluence = 0.0;
      level.downwardInfluence = 0.0;
    });
    
    this.crossScaleInteractions = new Array(7).fill(0).map(() => new Array(7).fill(0));
    this.emergenceHotspots = [];
    
    console.log('🌊 Multi-Scale φ-Cascade reset to initial state');
  }
}
