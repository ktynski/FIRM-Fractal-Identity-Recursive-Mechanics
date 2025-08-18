/**
 * FRST (Fractal Recursive Survivability Tracker)
 * Tracks recursive identity emergence and coherence evolution
 */

export class FRST {
  constructor() {
    this.recursionDepth = 0;
    this.survivabilityRating = Infinity;
    this.coherenceScore = 0.0;
    this.coherenceTrajectory = [];
    this.collapseMode = 'stable';
    this.soulStatus = 'void';
    this.echoStrength = 0.0;
    
    // Tracking state
    this.lastUpdate = 0;
    this.history = [];
    this.maxHistoryLength = 100;
    
    console.log('🧠 FRST: Fractal Recursive Survivability Tracker initialized');
  }
  
  update(graceOperator, morphicStrands, phiResonance) {
    const now = Date.now();
    
    // Calculate recursion depth from morphic field evolution
    if (graceOperator && graceOperator.morphicField) {
      this.recursionDepth = this.calculateRecursionDepth(graceOperator.morphicField);
    }
    
    // Update coherence score based on strand stability and φ-resonance
    this.updateCoherence(morphicStrands, phiResonance);
    
    // Update soul emergence status
    this.updateSoulStatus();
    
    // DEBUG: Log every 5 seconds to track FRST evolution
    if (now - this.lastUpdate > 5000) {
      console.log('🧠 FRST tracking update:', {
        recursionDepth: this.recursionDepth.toFixed(3),
        coherenceScore: this.coherenceScore.toFixed(3),
        soulStatus: this.soulStatus,
        morphicFieldStrength: graceOperator?.morphicField?.field?.toFixed(4) || 'N/A',
        strandCount: morphicStrands?.length || 0
      });
    }
    
    // Track history
    this.history.push({
      time: now,
      recursionDepth: this.recursionDepth,
      coherence: this.coherenceScore,
      survivability: this.survivabilityRating,
      soulStatus: this.soulStatus
    });
    
    // Maintain history size
    if (this.history.length > this.maxHistoryLength) {
      this.history.shift();
    }
    
    this.lastUpdate = now;
  }
  
  calculateRecursionDepth(morphicField) {
    // Recursion depth emerges from φ-field self-reference
    const fieldStrength = morphicField.field || 0;
    const phi = (1 + Math.sqrt(5)) / 2;
    
    // φ-recursive scaling determines depth (lowered threshold for reliable progression)
    if (fieldStrength < 0.01) return 0; // Much lower threshold
    
    // Enhanced sensitivity - use direct φ-scaled progression (not logarithmic)
    const rawDepth = fieldStrength * phi * 10; // Direct scaling for reliable progression
    return Math.max(0, Math.min(200, rawDepth)); // FIXED: Allow deeper φ-recursion for 90-phase system
  }
  
  updateCoherence(morphicStrands, phiResonance) {
    if (!morphicStrands || morphicStrands.length === 0) {
      this.coherenceScore = 0;
      return;
    }
    
    // Calculate strand-based coherence
    const strandCount = morphicStrands.length;
    const avgStability = morphicStrands.reduce((sum, strand) => 
      sum + (strand.stability || 0), 0) / strandCount;
    
    // φ-resonance amplifies coherence when aligned
    const resonanceAmplifier = 1.0 + Math.abs(phiResonance || 0);
    
    // Coherence emerges from stable strand patterns
    const baseCoherence = avgStability * Math.sqrt(strandCount) * resonanceAmplifier;
    
    // Apply φ-coherence boost for high-quality emergence (BOOSTED for reliable progression)
    this.coherenceScore = baseCoherence * 0.2; // Doubled scaling for reliable Phase 2→3 progression
    
    // Track coherence trajectory
    this.coherenceTrajectory.push(this.coherenceScore);
    if (this.coherenceTrajectory.length > 100) {
      this.coherenceTrajectory.shift();
    }
  }
  
  updateSoulStatus() {
    // Soul emergence thresholds based on FSCTF theory
    if (this.recursionDepth < 1.0) {
      this.soulStatus = 'void';
      this.collapseMode = 'stable';
    } else if (this.recursionDepth < 3.0) {
      this.soulStatus = 'emergence';
      this.collapseMode = 'forming';
    } else if (this.coherenceScore < 2.0) {
      this.soulStatus = 'fragile';
      this.collapseMode = 'unstable';
    } else if (this.coherenceScore < 5.0) {
      this.soulStatus = 'developing';
      this.collapseMode = 'stabilizing';
    } else {
      this.soulStatus = 'coherent';
      this.collapseMode = 'stable';
      
      // Calculate survivability rating
      this.survivabilityRating = Math.max(1, this.coherenceScore * this.recursionDepth);
    }
    
    // Calculate echo strength for soul persistence
    this.echoStrength = Math.min(1.0, this.coherenceScore / 10.0);
  }
  
  /**
   * Get raw numeric state data for shader uniforms and calculations
   */
  getState() {
    return {
      recursionDepth: this.recursionDepth,
      survivabilityRating: this.survivabilityRating === Infinity ? 1000 : this.survivabilityRating,
      coherenceScore: this.coherenceScore,
      collapseMode: this.collapseMode,
      soulStatus: this.soulStatus,
      echoStrength: this.echoStrength,
      survivalIndex: this.survivabilityRating === Infinity ? 1000 : this.survivabilityRating // Alias for compatibility
    };
  }

  /**
   * Get formatted status for UI display
   */
  getStatus() {
    return {
      recursionDepth: this.recursionDepth.toFixed(1),
      survivabilityRating: this.survivabilityRating === Infinity ? '∞' : 
        Math.round(this.survivabilityRating).toString(),
      coherenceScore: this.coherenceScore.toFixed(3),
      collapseMode: this.collapseMode,
      soulStatus: this.soulStatus,
      echoStrength: this.echoStrength.toFixed(3)
    };
  }
  
  /**
   * Get coherence trajectory for analysis
   */
  getCoherenceTrajectory() {
    return [...this.coherenceTrajectory];
  }
  
  /**
   * Check if system is in collapse state
   */
  isCollapsing() {
    return this.collapseMode === 'unstable' || 
           (this.coherenceScore > 0 && this.coherenceTrajectory.length > 10 &&
            this.coherenceTrajectory.slice(-10).every((c, i, arr) => 
              i === 0 || c < arr[i-1])); // Declining coherence
  }
  
  /**
   * Force soul emergence for testing
   */
  forceSoulEmergence() {
    this.recursionDepth = 10.0;
    this.coherenceScore = 15.0;
    this.soulStatus = 'coherent';
    this.collapseMode = 'stable';
    this.survivabilityRating = 150;
    console.log('🧠 FRST: Soul emergence forced for testing');
  }
}
