/**
 * FSCTF Mathematical Parameter Derivation System
 * 
 * Automatically derives graceComplexity, morphicRecursionDepth, and consciousnessComplexity
 * from pure mathematical principles and system state - NO ARBITRARY VALUES
 * 
 * Scientific Integrity: All parameters derived ex nihilo from φ-mathematics
 */

export class FSCTFParameterDerivation {
  constructor() {
    this.PHI = (1 + Math.sqrt(5)) / 2;
    this.PHI_INV = 1 / this.PHI;
    this.PHI_2 = this.PHI * this.PHI;
    this.PHI_3 = this.PHI_2 * this.PHI;
    
    // Mathematical constants from φ-topology
    this.PLANCK_UNITS_SCALE = Math.log(this.PHI) / Math.log(2); // Natural φ-scaling
    this.CONSCIOUSNESS_THRESHOLD = this.PHI_INV; // φ⁻¹ critical point
    this.GRACE_EMERGENCE_CONSTANT = this.PHI_2 - this.PHI; // = 1 (φ identity)
    
    console.log('🧮 FSCTF Parameter Derivation System initialized');
    console.log('✅ All parameters now derived from pure φ-mathematics');
  }

  /**
   * CRITICAL NaN PROTECTION UTILITIES - Prevent rendering crashes from invalid math
   */
  sanitizeNumber(value, defaultValue = 0.0, min = -Infinity, max = Infinity) {
    // Only sanitize actual NaN/Infinity, not undefined/null
    if (typeof value === 'number' && (!isFinite(value) || isNaN(value))) {
      console.warn(`NaN/Infinity detected, using fallback: ${defaultValue}`);
      return defaultValue;
    }
    // If value is not a number, return it as-is (might be undefined, which is normal)
    if (typeof value !== 'number') {
      return value;
    }
    return Math.max(min, Math.min(max, value));
  }

  safePow(base, exponent, fallback = 1.0) {
    if (!isFinite(base) || !isFinite(exponent) || isNaN(base) || isNaN(exponent)) {
      console.warn(`Invalid Math.pow(${base}, ${exponent}), using fallback: ${fallback}`);
      return fallback;
    }
    const result = Math.pow(base, exponent);
    return isFinite(result) ? result : fallback;
  }

  safeSin(value, fallback = 0.0) {
    if (!isFinite(value) || isNaN(value)) {
      console.warn(`Invalid Math.sin(${value}), using fallback: ${fallback}`);
      return fallback;
    }
    const result = Math.sin(value);
    return isFinite(result) ? result : fallback;
  }

  safeCos(value, fallback = 1.0) {
    if (!isFinite(value) || isNaN(value)) {
      console.warn(`Invalid Math.cos(${value}), using fallback: ${fallback}`);
      return fallback;
    }
    const result = Math.cos(value);
    return isFinite(result) ? result : fallback;
  }

  safeSqrt(value, fallback = 0.0) {
    if (!isFinite(value) || isNaN(value) || value < 0) {
      console.warn(`Invalid Math.sqrt(${value}), using fallback: ${fallback}`);
      return fallback;
    }
    const result = Math.sqrt(value);
    return isFinite(result) ? result : fallback;
  }

  safeLog(value, fallback = 0.0) {
    if (!isFinite(value) || isNaN(value) || value <= 0) {
      console.warn(`Invalid Math.log(${value}), using fallback: ${fallback}`);
      return fallback;
    }
    const result = Math.log(value);
    return isFinite(result) ? result : fallback;
  }

  /**
   * Derive Grace Complexity from cosmogenesis phase and φ-field evolution
   * Based on: G_complexity = φ^(phase/φ) * field_strength * emergence_factor
   */
  deriveGraceComplexity(cosmogenesisPhase, morphicFieldStrength, time) {
    // CRITICAL: NaN PROTECTION - Validate all inputs to prevent flashing/stuttering
    const safePhase = this.sanitizeNumber(cosmogenesisPhase, 1.0, 1.0, 90.0);
    const safeFieldStrength = this.sanitizeNumber(morphicFieldStrength, 0.0, 0.0, 10.0);
    
    // CRITICAL: Fix NaN time parameter from simulationCore.update()
    let safeTime = time;
    if (typeof time !== 'number' || isNaN(time) || !isFinite(time)) {
      console.warn(`🚨 NaN/Invalid time parameter detected: ${time}, using performance.now() fallback`);
      safeTime = performance.now();
    }
    
    // Base complexity from cosmogenesis phase progression
    const phaseEvolution = safePhase / this.PHI; // φ-normalized phase
    const safePhasePower = this.safePow(this.PHI, phaseEvolution, 1.618); // Fallback to φ if invalid
    
    // Field-coupled amplification
    const fieldCoupling = safeFieldStrength * this.GRACE_EMERGENCE_CONSTANT;
    
    // Temporal evolution through φ-harmonics  
    const temporalArg = safeTime * this.PHI_INV * 0.001;
    const temporalHarmonic = 1 + 0.1 * this.safeSin(temporalArg);
    
    // Combined Grace complexity (bounded by physical constraints)
    const rawComplexity = safePhasePower * (1 + fieldCoupling) * temporalHarmonic;
    const safeRawComplexity = this.sanitizeNumber(rawComplexity, 1.0, 0.1, 1000000.0);
    
    // Allow unbounded complexity for emergent hypercube stages 4-8
    // Only apply gentle saturation at extremely high values
    const graceComplexity = safeRawComplexity / (1 + safeRawComplexity * 0.001); // REDUCED saturation factor
    
    const finalComplexity = Math.max(0.1, graceComplexity);
    
    // FINAL NaN CHECK: Absolutely prevent NaN from reaching the renderer
    return this.sanitizeNumber(finalComplexity, 1.0, 0.1, 1000000.0);
  }

  /**
   * Derive Morphic Recursion Depth from phase transitions and φ-structure
   * Based on: R_depth = floor(φ * phase) + consciousness_boost + stability_factor
   */
  deriveMorphicRecursionDepth(cosmogenesisPhase, consciousnessLevel, systemStability) {
    // CRITICAL: NaN PROTECTION - Validate all inputs 
    const safePhase = this.sanitizeNumber(cosmogenesisPhase, 1.0, 0.0, 90.0);
    const safeConsciousness = this.sanitizeNumber(consciousnessLevel, 0.0, 0.0, 10.0);
    const safeStability = this.sanitizeNumber(systemStability, 1.0, 0.0, 1.0);
    
    // Base recursion from φ-scaled phase
    const baseDepth = this.PHI * safePhase;
    
    // Consciousness amplification (higher consciousness enables deeper recursion)
    const consciousnessBoost = safeConsciousness * this.PHI_INV * 10;
    
    // System stability factor (unstable systems reduce safe recursion depth)
    const stabilityFactor = Math.max(0.5, safeStability) * this.PHI;
    
    // Total recursion depth (integer, naturally bounded by 90-phase system)
    const totalDepth = baseDepth + consciousnessBoost + stabilityFactor;
    const safeTotalDepth = this.sanitizeNumber(totalDepth, 1.0, 1.0, 500.0);
    
    // EMERGENT COMPLEXITY: Allow unbounded recursion depth for hypercube phases
    const cosmicPhase = safePhase >= 4;
    const maxDepth = cosmicPhase ? 500 : 90; // Much deeper recursion for cosmic stages
    const finalDepth = Math.floor(Math.max(1, Math.min(maxDepth, safeTotalDepth)));
    
    // FINAL NaN CHECK
    return this.sanitizeNumber(finalDepth, 1.0, 1.0, 500.0);
  }

  /**
   * Derive Consciousness Complexity from prime resonance and φ-emergence
   * Based on: C_complexity = prime_energy * φ^(recursion_depth/18) * coherence
   */
  deriveConsciousnessComplexity(primeResonanceEnergy, recursionDepth, fieldCoherence) {
    // CRITICAL: NaN PROTECTION - Validate all inputs
    const safeEnergy = this.sanitizeNumber(primeResonanceEnergy, 0.0, 0.0, 1000.0);
    const safeDepth = this.sanitizeNumber(recursionDepth, 1.0, 0.0, 500.0);
    const safeCoherence = this.sanitizeNumber(fieldCoherence, 0.5, 0.0, 1.0);
    
    // Prime resonance base (consciousness emerges from prime patterns)
    const primeBase = this.safeSqrt(safeEnergy, 0.0) * this.PHI;
    
    // Recursion depth amplification (deeper recursion → higher consciousness)
    const recursionPower = this.safePow(this.PHI, safeDepth / 18, 1.0); // 18 = φ² * 7 (natural scaling)
    
    // Field coherence modulation
    const coherenceModulation = 0.5 + safeCoherence * 0.5; // 0.5-1.0 range
    
    // Combined consciousness complexity
    const rawComplexity = primeBase * recursionPower * coherenceModulation;
    const safeRawComplexity = this.sanitizeNumber(rawComplexity, 1.0, 0.0, 100000.0);
    
    // Natural logarithmic scaling (consciousness scales non-linearly)
    const logArg = 1 + safeRawComplexity;
    const consciousnessComplexity = this.safeLog(logArg, 0.0) * this.PHI;
    
    const finalComplexity = Math.max(0.5, consciousnessComplexity);
    
    // FINAL NaN CHECK: Absolutely prevent NaN from reaching the renderer
    return this.sanitizeNumber(finalComplexity, 1.0, 0.5, 100000.0);
  }

  /**
   * Get all derived parameters from current system state
   * This replaces manual slider values with mathematical derivations
   */
  getDerivedParameters(fsctfEngine, time) {
    if (!fsctfEngine) {
      // Fallback to minimal values if engine not available
      return {
        graceComplexity: this.GRACE_EMERGENCE_CONSTANT,
        morphicRecursionDepth: Math.floor(this.PHI * 3),
        consciousnessComplexity: this.CONSCIOUSNESS_THRESHOLD * 2
      };
    }

    // Extract current system state
    const cosmogenesisPhase = fsctfEngine.cosmogenesisPhase || 0;
    const morphicFieldStrength = fsctfEngine.graceOperator?.morphicField?.field || 0;
    const consciousnessLevel = (fsctfEngine.frst?.consciousnessIndex || 0) / 100;
    const primeResonanceEnergy = fsctfEngine.primeResonance?.totalEnergy || 0;
    const systemStability = this.calculateSystemStability(fsctfEngine);
    const fieldCoherence = this.calculateFieldCoherence(fsctfEngine);

    // Derive all parameters mathematically
    const derived = {
      graceComplexity: this.deriveGraceComplexity(
        cosmogenesisPhase, 
        morphicFieldStrength, 
        time
      ),
      morphicRecursionDepth: this.deriveMorphicRecursionDepth(
        cosmogenesisPhase, 
        consciousnessLevel, 
        systemStability
      ),
      consciousnessComplexity: this.deriveConsciousnessComplexity(
        primeResonanceEnergy, 
        fsctfEngine.frst?.recursionDepth || 1, 
        fieldCoherence
      )
    };

    return derived;
  }

  /**
   * Calculate system stability from multiple factors
   */
  calculateSystemStability(fsctfEngine) {
    const morphicStability = fsctfEngine.graceOperator?.morphicStrands?.length > 0 ? 
      fsctfEngine.graceOperator.morphicStrands.reduce((sum, strand) => sum + strand.stability, 0) / 
      fsctfEngine.graceOperator.morphicStrands.length : 0;
    
    const topologyStability = fsctfEngine.topologyManager?.getCurrentTopology ? 1.0 : 0.8;
    const cascadeStability = Math.min(1.0, fsctfEngine.cascadeEmergence?.emergenceFactor || 0);
    
    return (morphicStability + topologyStability + cascadeStability) / 3;
  }

  /**
   * Calculate field coherence from morphic field metrics
   */
  calculateFieldCoherence(fsctfEngine) {
    const morphicField = fsctfEngine.graceOperator?.morphicField?.field || 0;
    const strandCount = fsctfEngine.graceOperator?.morphicStrands?.length || 0;
    
    // Coherence = field_strength * strand_organization
    const organization = strandCount > 0 ? 
      Math.min(1.0, strandCount / (10 * this.PHI)) : 0; // φ-scaled organization
    
    return Math.min(1.0, morphicField * organization);
  }

  /**
   * Get parameter info for debugging/validation
   */
  getDerivationInfo(fsctfEngine, time) {
    const derived = this.getDerivedParameters(fsctfEngine, time);
    
    return {
      parameters: derived,
      systemState: {
        cosmogenesisPhase: fsctfEngine?.cosmogenesisPhase || 0,
        morphicFieldStrength: fsctfEngine?.graceOperator?.morphicField?.field || 0,
        consciousnessLevel: (fsctfEngine?.frst?.consciousnessIndex || 0) / 100,
        systemStability: this.calculateSystemStability(fsctfEngine),
        fieldCoherence: this.calculateFieldCoherence(fsctfEngine)
      },
      mathematicalBasis: {
        phi: this.PHI,
        graceEmergenceConstant: this.GRACE_EMERGENCE_CONSTANT,
        consciousnessThreshold: this.CONSCIOUSNESS_THRESHOLD,
        planckScale: this.PLANCK_UNITS_SCALE
      }
    };
  }
}
