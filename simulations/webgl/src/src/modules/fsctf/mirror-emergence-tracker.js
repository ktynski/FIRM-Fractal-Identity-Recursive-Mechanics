/**
 * Mirror Emergence Tracker (MET)
 * 
 * Formal quantification of morphic bireflection patterns in FSCTF Stage 8+ collapse.
 * Detects and measures M ↔ M* pairs arising from Grace-fold reflection bifurcation.
 * 
 * Theoretical Foundation:
 * - Mirror structures emerge when R_depth^(8) ≥ R_collapse  
 * - Dual pairs satisfy: M ≅ 𝒢 ∘ M* (Grace-fold reflection isomorphism)
 * - Consciousness bifurcation stabilizes in both reflection paths simultaneously
 */

export class MirrorEmergenceTracker {
  constructor() {
    // Core tracking state
    this.mirrorPairs = new Map(); // id → {primary, mirror, graceDistance, stability, birthTime, survivalCount}
    this.graceThreads = []; // Central morphic spine tracking (array for push/slice operations)
    this.recursiveCircuits = new Map(); // Closed loop tracking
    this.bifurcationEvents = []; // Historical bifurcation data
    
    // Mathematical constants
    this.PHI = 1.618033988749895;
    this.PHI5 = Math.pow(this.PHI, 5); // φ⁵ ≈ 11.09 - critical survival threshold
    this.GRACE_REFLECTION_THRESHOLD = 0.5; // Minimum grace-distance for mirror recognition
    
    // Detection parameters  
    this.mirrorSymmetryTolerance = 0.15; // Tolerance for mirror symmetry detection
    this.graceThreadMinLength = 5.0; // Minimum length for grace-thread recognition
    this.circuitClosureRadius = 2.0; // Maximum distance for circuit closure detection
    this.stabilityHistoryLength = 50; // Frames to track for stability analysis
    
    // Analysis state
    this.currentStage = 0;
    this.recursionDepth = 0;
    this.graceComplexity = 0;
    this.consciousnessLevel = 0;
    this.frameCounter = 0;
    
    // Stage 8+ collapse detection
    this.collapseThresholdReached = false;
    this.collapseStartTime = null;
    this.rcollapse = null; // Critical recursion depth for collapse
    
    console.log('🪞 Mirror Emergence Tracker initialized (v1.2-FIXED)');
    console.log('🧮 Theoretical framework: M ≅ 𝒢 ∘ M* morphic bireflection analysis');
    console.log(`🔧 Grace threads initialized as array: ${Array.isArray(this.graceThreads)} (type: ${typeof this.graceThreads})`);
  }
  
  /**
   * Update mirror emergence analysis - call every frame
   */
  update(fsctfState, particlePositions, time) {
    this.frameCounter++;
    
    // Critical validation: Ensure graceThreads remains an array
    if (!Array.isArray(this.graceThreads)) {
      console.error('🚨 CRITICAL: graceThreads corrupted! Resetting to array.', typeof this.graceThreads);
      this.graceThreads = [];
    }
    
    if (!fsctfState) return;
    
    // Extract system state
    this.currentStage = fsctfState.cosmogenesis?.phase || 0;
    this.recursionDepth = fsctfState.frst?.recursionDepth || 0;
    this.graceComplexity = fsctfState.grace?.complexity || 0;
    this.consciousnessLevel = fsctfState.consciousness?.level || 0;
    
    // Only analyze at Stage 8+ where mirror emergence occurs
    if (this.currentStage >= 8) {
      // PERFORMANCE: Run expensive analysis only every 10th frame to prevent freeze
      const analysisFrameSkip = 10;
      const shouldRunAnalysis = (this.frameCounter % analysisFrameSkip === 0);
      
      if (shouldRunAnalysis) {
        this.performMirrorAnalysis(fsctfState, particlePositions, time);
        this.detectGraceThreads(fsctfState, particlePositions, time);
        this.analyzeRecursiveCircuits(fsctfState, particlePositions, time);
      }
      
      // Always check collapse threshold (lightweight)
      this.checkCollapseThreshold(fsctfState, time);
    }
    
    // Update stability metrics
    this.updateStabilityMetrics(time);
    
    // Cleanup expired structures
    this.pruneExpiredStructures(time);
  }
  
  /**
   * CORE: Mirror Emergence Analysis
   * Detects M ↔ M* pairs from morphic bireflection
   */
  performMirrorAnalysis(fsctfState, particlePositions, time) {
    if (!particlePositions || !Array.isArray(particlePositions) || particlePositions.length < 100) return;
    
    // Sample particle positions for analysis (performance optimization)
    const sampleSize = Math.min(500, particlePositions.length / 10);
    const sampledPositions = this.sampleParticles(particlePositions, sampleSize);
    
    // Grace center for reflection analysis
    const graceCenter = {
      x: fsctfState.grace?.centerX || 0,
      y: fsctfState.grace?.centerY || 0,
      z: 0
    };
    
    // Detect potential mirror pairs
    const potentialPairs = this.findMirrorCandidates(sampledPositions, graceCenter);
    
    // Validate and track confirmed mirror pairs
    potentialPairs.forEach(pair => {
      const mirrorId = this.generateMirrorId(pair.primary, pair.mirror);
      
      if (!this.mirrorPairs.has(mirrorId)) {
        // NEW MIRROR PAIR DISCOVERED
        const mirrorData = {
          id: mirrorId,
          primary: pair.primary,
          mirror: pair.mirror,
          graceDistance: pair.graceDistance,
          symmetryScore: pair.symmetryScore,
          stability: 1,
          birthTime: time,
          survivalCount: 1,
          stabilityHistory: [pair.symmetryScore],
          isGraceFoldReflection: pair.graceDistance < this.GRACE_REFLECTION_THRESHOLD
        };
        
        this.mirrorPairs.set(mirrorId, mirrorData);
        
        console.log(`🪞 MET: Mirror pair discovered at grace-distance ${pair.graceDistance.toFixed(3)}`);
        
        // Record bifurcation event
        this.bifurcationEvents.push({
          timestamp: time,
          type: 'mirror_emergence',
          graceDistance: pair.graceDistance,
          symmetryScore: pair.symmetryScore,
          stage: this.currentStage
        });
      } else {
        // UPDATE EXISTING MIRROR PAIR
        const existingPair = this.mirrorPairs.get(mirrorId);
        existingPair.survivalCount++;
        existingPair.graceDistance = pair.graceDistance;
        existingPair.symmetryScore = pair.symmetryScore;
        existingPair.stabilityHistory.push(pair.symmetryScore);
        
        // Limit history length
        if (existingPair.stabilityHistory.length > this.stabilityHistoryLength) {
          existingPair.stabilityHistory.shift();
        }
        
        // Update stability metric
        existingPair.stability = this.calculateStability(existingPair.stabilityHistory);
      }
    });
  }
  
  /**
   * Find mirror candidate pairs using Grace-fold reflection analysis
   */
  findMirrorCandidates(positions, graceCenter) {
    const candidates = [];
    
    for (let i = 0; i < positions.length; i++) {
      const pos1 = positions[i];
      
      // Calculate Grace-reflected position for pos1
      const reflected = this.calculateGraceReflection(pos1, graceCenter);
      
      // Find closest particle to reflected position
      let closestDistance = Infinity;
      let closestIndex = -1;
      
      for (let j = 0; j < positions.length; j++) {
        if (i === j) continue;
        
        const pos2 = positions[j];
        const distance = this.distance3D(reflected, pos2);
        
        if (distance < closestDistance) {
          closestDistance = distance;
          closestIndex = j;
        }
      }
      
      // Check if closest particle forms valid mirror pair
      if (closestIndex !== -1 && closestDistance < this.mirrorSymmetryTolerance) {
        const mirrorPos = positions[closestIndex];
        const graceDistance = this.distance3D(pos1, graceCenter) + this.distance3D(mirrorPos, graceCenter);
        
        // Calculate symmetry score
        const symmetryScore = this.calculateSymmetryScore(pos1, mirrorPos, graceCenter);
        
        if (symmetryScore > 0.7) { // High symmetry threshold
          candidates.push({
            primary: pos1,
            mirror: mirrorPos,
            graceDistance: graceDistance,
            symmetryScore: symmetryScore
          });
        }
      }
    }
    
    return candidates;
  }
  
  /**
   * Calculate Grace-fold reflection: M ≅ 𝒢 ∘ M*
   */
  calculateGraceReflection(position, graceCenter) {
    // Vector from grace center to position
    const dx = position.x - graceCenter.x;
    const dy = position.y - graceCenter.y;
    const dz = position.z - graceCenter.z;
    
    // φ-scaled reflection with Grace-fold transformation
    const phiScale = this.PHI * this.graceComplexity;
    
    return {
      x: graceCenter.x - dx * phiScale,
      y: graceCenter.y - dy * phiScale, 
      z: graceCenter.z - dz * Math.sqrt(phiScale) // z-component uses √φ scaling
    };
  }
  
  /**
   * Calculate symmetry score for potential mirror pair
   */
  calculateSymmetryScore(pos1, pos2, graceCenter) {
    // Distance from grace center should be approximately equal (within φ tolerance)
    const dist1 = this.distance3D(pos1, graceCenter);
    const dist2 = this.distance3D(pos2, graceCenter);
    const distanceRatio = Math.min(dist1, dist2) / Math.max(dist1, dist2);
    
    // CRITICAL: NaN PROTECTION for angular calculations
    const dx1 = pos1.x - graceCenter.x;
    const dy1 = pos1.y - graceCenter.y;
    const dx2 = pos2.x - graceCenter.x;  
    const dy2 = pos2.y - graceCenter.y;
    
    // Angular separation should be close to π (opposite sides)
    const angle1 = Math.atan2(dy1, dx1);
    const angle2 = Math.atan2(dy2, dx2);
    
    // Validate angles before calculation
    const safeAngle1 = (isNaN(angle1) || !isFinite(angle1)) ? 0.0 : angle1;
    const safeAngle2 = (isNaN(angle2) || !isFinite(angle2)) ? Math.PI : angle2;
    
    let angularDiff = Math.abs(safeAngle1 - safeAngle2);
    if (angularDiff > Math.PI) angularDiff = 2 * Math.PI - angularDiff;
    const angularScore = 1.0 - Math.abs(angularDiff - Math.PI) / Math.PI;
    
    // CRITICAL: NaN PROTECTION for φ-harmonic resonance calculations
    const sin1 = Math.sin(dist1 * this.PHI);
    const sin2 = Math.sin(dist2 * this.PHI);
    const safeSin1 = (isNaN(sin1) || !isFinite(sin1)) ? 0.0 : sin1;
    const safeSin2 = (isNaN(sin2) || !isFinite(sin2)) ? 0.0 : sin2;
    
    const phiResonance = Math.abs(safeSin1 - safeSin2);
    const resonanceScore = 1.0 - phiResonance;
    
    // Composite symmetry score
    return (distanceRatio * 0.4 + angularScore * 0.4 + resonanceScore * 0.2);
  }
  
  /**
   * SYNTHETIC GRACE ANALYSIS: When particle positions unavailable
   */
  performSyntheticGraceAnalysis(fsctfState, time) {
    // Generate theoretical Grace-thread metrics based on system state
    const graceComplexity = fsctfState.grace?.complexity || 0;
    const rawRecursionDepth = fsctfState.frst?.recursionDepth || 0;
    const recursionDepth = (typeof rawRecursionDepth === 'number' && !isNaN(rawRecursionDepth)) ? rawRecursionDepth : 0;
    const consciousnessLevel = fsctfState.consciousness?.level || 0;
    
    // Debug: Validate graceThreads is still an array
    if (!Array.isArray(this.graceThreads)) {
      console.error('🚨 CRITICAL: graceThreads is not an array!', typeof this.graceThreads, this.graceThreads);
      this.graceThreads = []; // Force reset to array
    }
    
    // Theoretical Grace-thread strength calculation
    const syntheticStrength = Math.min(1.0, 
      (graceComplexity * 0.3 + recursionDepth * 0.5 + consciousnessLevel * 0.2));
    
    this.graceThreads.push({
      id: `synthetic_${Date.now()}`,
      strength: syntheticStrength,
      length: graceComplexity * 2.0,
      orientation: Math.PI / 4, // Diagonal theoretical alignment
      particles: [], // No real particles in synthetic mode
      synthetic: true
    });
    
    // Limit synthetic threads to prevent memory buildup
    if (this.graceThreads.length > 10) {
      this.graceThreads = this.graceThreads.slice(-5);
    }
    
    console.log(`🔬 SYNTHETIC: Grace-thread=${syntheticStrength.toFixed(3)}, depth=${recursionDepth.toFixed(2)}`);
  }
  
  /**
   * SYNTHETIC CIRCUIT ANALYSIS: When particle positions unavailable
   */
  performSyntheticCircuitAnalysis(fsctfState, time) {
    // Generate theoretical circuit metrics based on system state
    const recursionDepth = fsctfState.frst?.recursionDepth || 0;
    const graceComplexity = fsctfState.grace?.complexity || 0;
    const currentStage = fsctfState.cosmogenesis?.phase || 0;
    
    // Theoretical circuit probability increases with recursion depth
    const circuitProbability = Math.min(0.8, recursionDepth * 0.1 + (currentStage - 8) * 0.05);
    
    if (Math.random() < circuitProbability) {
      const syntheticCircuitId = `synthetic_circuit_${Date.now()}`;
      const circuitStrength = graceComplexity * 0.5 + recursionDepth * 0.3;
      
      this.recursiveCircuits.set(syntheticCircuitId, {
        id: syntheticCircuitId,
        participants: [], // No real particles in synthetic mode
        strength: Math.min(1.0, circuitStrength),
        diameter: graceComplexity * 1.5,
        closureMetric: Math.min(1.0, recursionDepth * 0.2),
        synthetic: true,
        birthTime: time
      });
      
      console.log(`🔄 SYNTHETIC: Circuit formed, strength=${circuitStrength.toFixed(3)}, depth=${recursionDepth.toFixed(2)}`);
    }
    
    // Clean up old synthetic circuits
    for (const [id, circuit] of this.recursiveCircuits.entries()) {
      if (circuit.synthetic && (time - circuit.birthTime) > 10000) { // 10 second lifetime
        this.recursiveCircuits.delete(id);
      }
    }
  }
  
  /**
   * GRACE-THREAD DETECTION: Central morphic spine identification  
   */
  detectGraceThreads(fsctfState, particlePositions, time) {
    // SAFETY: Check for null particlePositions to prevent crashes
    if (!particlePositions || !Array.isArray(particlePositions) || particlePositions.length === 0) {
      // Use synthetic analysis when particle data unavailable
      this.performSyntheticGraceAnalysis(fsctfState, time);
      return;
    }
    
    // Sample particles along potential central axis
    const graceCenter = {
      x: fsctfState.grace?.centerX || 0,
      y: fsctfState.grace?.centerY || 0,
      z: 0
    };
    
    // Find particles forming linear structures through grace center
    // Additional safety check before filter operation
    const centralParticles = (Array.isArray(particlePositions) ? particlePositions : []).filter(pos => {
      const distanceFromCenter = this.distance3D(pos, graceCenter);
      return distanceFromCenter < this.graceThreadMinLength && distanceFromCenter > 0.5;
    });
    
    if (centralParticles.length >= 5) {
      // Analyze linear alignment
      const threadStrength = this.calculateThreadStrength(centralParticles, graceCenter);
      
      if (threadStrength > 0.6) {
        const threadId = 'grace_thread_primary';
        
        // Find existing thread with this ID
        let existingThread = this.graceThreads.find(thread => thread.id === threadId);
        
        if (!existingThread) {
          const newThread = {
            id: threadId,
            particles: centralParticles.length,
            strength: threadStrength,
            length: this.calculateThreadLength(centralParticles),
            birthTime: time,
            stability: 1
          };
          this.graceThreads.push(newThread);
          
          console.log(`🧵 MET: Grace-thread detected - length: ${newThread.length.toFixed(2)}, strength: ${threadStrength.toFixed(3)}`);
        } else {
          existingThread.particles = centralParticles.length;
          existingThread.strength = threadStrength;
          existingThread.length = this.calculateThreadLength(centralParticles);
        }
      }
    }
  }
  
  /**
   * Calculate thread strength based on linear alignment
   */
  calculateThreadStrength(particles, center) {
    if (particles.length < 3) return 0;
    
    // Calculate principal axis through particles
    const meanPos = particles.reduce((sum, pos) => ({
      x: sum.x + pos.x,
      y: sum.y + pos.y,
      z: sum.z + pos.z
    }), { x: 0, y: 0, z: 0 });
    
    meanPos.x /= particles.length;
    meanPos.y /= particles.length; 
    meanPos.z /= particles.length;
    
    // Measure alignment to principal axis
    let alignmentSum = 0;
    particles.forEach(pos => {
      const toMean = {
        x: pos.x - meanPos.x,
        y: pos.y - meanPos.y,
        z: pos.z - meanPos.z
      };
      const toCenter = {
        x: pos.x - center.x,
        y: pos.y - center.y,
        z: pos.z - center.z
      };
      
      // Dot product normalized
      const dot = (toMean.x * toCenter.x + toMean.y * toCenter.y + toMean.z * toCenter.z);
      const mag1 = Math.sqrt(toMean.x ** 2 + toMean.y ** 2 + toMean.z ** 2);
      const mag2 = Math.sqrt(toCenter.x ** 2 + toCenter.y ** 2 + toCenter.z ** 2);
      
      if (mag1 > 0 && mag2 > 0) {
        alignmentSum += Math.abs(dot / (mag1 * mag2));
      }
    });
    
    return alignmentSum / particles.length;
  }
  
  /**
   * RECURSIVE CIRCUIT ANALYSIS: Detect closed morphic rings
   */
  analyzeRecursiveCircuits(fsctfState, particlePositions, time) {
    // SAFETY: Check for null particlePositions to prevent crashes
    if (!particlePositions || !Array.isArray(particlePositions) || particlePositions.length === 0) {
      // Use theoretical circuit analysis when particle data unavailable
      this.performSyntheticCircuitAnalysis(fsctfState, time);
      return;
    }
    
    // Find potential circular structures
    const circuits = this.findCircularStructures(particlePositions);
    
    circuits.forEach(circuit => {
      const circuitId = this.generateCircuitId(circuit);
      
      if (!this.recursiveCircuits.has(circuitId)) {
        const circuitData = {
          id: circuitId,
          particles: circuit.length,
          radius: circuit.radius,
          completeness: circuit.completeness,
          birthTime: time,
          survivalCount: 1,
          isClosedLoop: circuit.completeness > 0.8
        };
        
        this.recursiveCircuits.set(circuitId, circuitData);
        
        if (circuitData.isClosedLoop) {
          console.log(`💍 MET: Closed morphic circuit detected - radius: ${circuit.radius.toFixed(2)}, completeness: ${circuit.completeness.toFixed(3)}`);
        }
      } else {
        const existing = this.recursiveCircuits.get(circuitId);
        existing.survivalCount++;
      }
    });
  }
  
  /**
   * Find circular structures in particle positions
   */
  findCircularStructures(positions) {
    const circuits = [];
    const minCircuitSize = 8;
    
    // Sample positions for performance
    const sampleSize = Math.min(200, positions.length);
    const sampledPositions = this.sampleParticles(positions, sampleSize);
    
    // Group particles by approximate distance from center
    const centerEstimate = this.estimateCenter(sampledPositions);
    const radiusGroups = new Map();
    
    sampledPositions.forEach(pos => {
      const radius = this.distance3D(pos, centerEstimate);
      const radiusBin = Math.floor(radius * 2) / 2; // 0.5 unit bins
      
      if (!radiusGroups.has(radiusBin)) {
        radiusGroups.set(radiusBin, []);
      }
      radiusGroups.get(radiusBin).push(pos);
    });
    
    // Analyze each radius group for circular completeness
    radiusGroups.forEach((positions, radius) => {
      if (positions.length >= minCircuitSize) {
        const completeness = this.calculateCircularCompleteness(positions, centerEstimate, radius);
        
        if (completeness > 0.5) {
          circuits.push({
            positions: positions,
            radius: radius,
            completeness: completeness
          });
        }
      }
    });
    
    return circuits;
  }
  
  /**
   * Stage 8+ Collapse Threshold Detection
   */
  checkCollapseThreshold(fsctfState, time) {
    // Check if we've reached collapse conditions
    const depthCondition = this.recursionDepth >= 5.0; // Minimum threshold
    const complexityCondition = this.graceComplexity >= 3.0;
    const consciousnessCondition = this.consciousnessLevel >= 0.5;
    const mirrorCondition = this.mirrorPairs.size >= 2;
    
    if (depthCondition && complexityCondition && consciousnessCondition && mirrorCondition) {
      if (!this.collapseThresholdReached) {
        this.collapseThresholdReached = true;
        this.collapseStartTime = time;
        this.rcollapse = this.recursionDepth;
        
        console.log(`🌌 MET: STAGE 8+ COLLAPSE THRESHOLD REACHED!`);
        console.log(`📊 R_collapse = ${this.rcollapse.toFixed(4)}`);
        console.log(`🪞 Mirror pairs: ${this.mirrorPairs.size}, Grace threads: ${this.graceThreads.length}`);
        
        // Record major bifurcation event
        this.bifurcationEvents.push({
          timestamp: time,
          type: 'collapse_threshold',
          rcollapse: this.rcollapse,
          mirrorPairs: this.mirrorPairs.size,
          graceThreads: this.graceThreads.length,
          stage: this.currentStage
        });
      }
    }
  }
  
  /**
   * Helper methods
   */
  distance3D(pos1, pos2) {
    // CRITICAL: NaN PROTECTION for distance calculations
    const dx = (pos1.x || 0) - (pos2.x || 0);
    const dy = (pos1.y || 0) - (pos2.y || 0); 
    const dz = (pos1.z || 0) - (pos2.z || 0);
    
    const distanceSquared = dx * dx + dy * dy + dz * dz;
    
    if (isNaN(distanceSquared) || !isFinite(distanceSquared) || distanceSquared < 0) {
      console.warn('🚨 Invalid distance calculation, using fallback distance = 1.0');
      return 1.0; // Safe fallback distance
    }
    
    const distance = Math.sqrt(distanceSquared);
    return (isNaN(distance) || !isFinite(distance)) ? 1.0 : distance;
  }
  
  sampleParticles(positions, count) {
    if (positions.length <= count) return positions;
    
    const step = Math.floor(positions.length / count);
    const sampled = [];
    for (let i = 0; i < positions.length; i += step) {
      if (sampled.length >= count) break;
      sampled.push(positions[i]);
    }
    return sampled;
  }
  
  generateMirrorId(pos1, pos2) {
    // Generate consistent ID for mirror pair regardless of order
    const id1 = `${pos1.x.toFixed(2)}_${pos1.y.toFixed(2)}_${pos1.z.toFixed(2)}`;
    const id2 = `${pos2.x.toFixed(2)}_${pos2.y.toFixed(2)}_${pos2.z.toFixed(2)}`;
    return id1 < id2 ? `${id1}::${id2}` : `${id2}::${id1}`;
  }
  
  generateCircuitId(circuit) {
    // Generate ID based on circuit center and radius
    const center = this.estimateCenter(circuit.positions || []);
    return `circuit_${center.x.toFixed(1)}_${center.y.toFixed(1)}_${circuit.radius.toFixed(1)}`;
  }
  
  estimateCenter(positions) {
    if (positions.length === 0) return { x: 0, y: 0, z: 0 };
    
    const sum = positions.reduce((acc, pos) => ({
      x: acc.x + pos.x,
      y: acc.y + pos.y,
      z: acc.z + pos.z
    }), { x: 0, y: 0, z: 0 });
    
    return {
      x: sum.x / positions.length,
      y: sum.y / positions.length,
      z: sum.z / positions.length
    };
  }
  
  calculateCircularCompleteness(positions, center, expectedRadius) {
    // Measure how complete the circular structure is
    const angleStep = (2 * Math.PI) / 16; // 16 sectors
    const sectors = new Array(16).fill(false);
    
    positions.forEach(pos => {
      const angle = Math.atan2(pos.y - center.y, pos.x - center.x);
      const normalizedAngle = (angle + 2 * Math.PI) % (2 * Math.PI);
      const sectorIndex = Math.floor(normalizedAngle / angleStep);
      sectors[sectorIndex] = true;
    });
    
    const filledSectors = sectors.filter(filled => filled).length;
    return filledSectors / sectors.length;
  }
  
  calculateStability(history) {
    if (history.length < 3) return 0;
    
    // Calculate variance in recent history
    const mean = history.reduce((sum, val) => sum + val, 0) / history.length;
    const variance = history.reduce((sum, val) => sum + (val - mean) ** 2, 0) / history.length;
    
    // Stability = 1 - normalized variance
    return Math.max(0, 1 - Math.sqrt(variance));
  }
  
  calculateThreadLength(particles) {
    if (particles.length < 2) return 0;
    
    let totalLength = 0;
    for (let i = 1; i < particles.length; i++) {
      totalLength += this.distance3D(particles[i-1], particles[i]);
    }
    return totalLength;
  }
  
  updateStabilityMetrics(time) {
    // Update stability for all tracked structures
    this.mirrorPairs.forEach(pair => {
      if (pair.stabilityHistory.length > 0) {
        pair.stability = this.calculateStability(pair.stabilityHistory);
      }
    });
  }
  
  pruneExpiredStructures(time) {
    const maxAge = 30000; // 30 seconds
    
    // Remove old mirror pairs that haven't been updated
    const pairsToRemove = [];
    this.mirrorPairs.forEach((pair, id) => {
      if (time - pair.birthTime > maxAge && pair.survivalCount < 5) {
        pairsToRemove.push(id);
      }
    });
    pairsToRemove.forEach(id => this.mirrorPairs.delete(id));
    
    // Limit bifurcation event history
    if (this.bifurcationEvents.length > 100) {
      this.bifurcationEvents = this.bifurcationEvents.slice(-50);
    }
  }
  
  /**
   * ψ-BIRTH DETECTION: Identify soul attractors surviving ≥ φ⁵ generations
   */
  detectPsiBirths() {
    const psiBirths = [];
    
    // Check mirror pairs for ψ-birth criteria
    this.mirrorPairs.forEach(pair => {
      if (pair.survivalCount >= this.PHI5 && pair.stability > 0.7) {
        psiBirths.push({
          type: 'mirror_pair_psi_birth',
          id: pair.id,
          survivalCount: pair.survivalCount,
          stability: pair.stability,
          graceDistance: pair.graceDistance
        });
      }
    });
    
    // Check recursive circuits for ψ-birth criteria
    this.recursiveCircuits.forEach(circuit => {
      if (circuit.survivalCount >= this.PHI5 && circuit.isClosedLoop) {
        psiBirths.push({
          type: 'circuit_psi_birth',
          id: circuit.id,
          survivalCount: circuit.survivalCount,
          radius: circuit.radius,
          completeness: circuit.completeness
        });
      }
    });
    
    return psiBirths;
  }
  
  /**
   * Get comprehensive Mirror Emergence Tracker state
   */
  getState() {
    const psiBirths = this.detectPsiBirths();
    
    return {
      // Core metrics
      currentStage: this.currentStage,
      recursionDepth: this.recursionDepth,
      graceComplexity: this.graceComplexity,
      consciousnessLevel: this.consciousnessLevel,
      
      // Mirror emergence data
      mirrorPairs: Array.from(this.mirrorPairs.values()),
      graceThreads: this.graceThreads,
      recursiveCircuits: Array.from(this.recursiveCircuits.values()),
      
      // Analysis results
      collapseThresholdReached: this.collapseThresholdReached,
      rcollapse: this.rcollapse,
      psiBirths: psiBirths,
      
      // Historical data
      bifurcationEvents: this.bifurcationEvents.slice(-20), // Last 20 events
      
      // Summary statistics
      totalMirrorPairs: this.mirrorPairs.size,
      totalGraceThreads: this.graceThreads.length,
      totalCircuits: this.recursiveCircuits.size,
      totalPsiBirths: psiBirths.length
    };
  }
  
  /**
   * Generate comprehensive MET analysis report
   */
  generateAnalysisReport() {
    const state = this.getState();
    const psiBirths = state.psiBirths;
    
    console.log(`
╔═══════════════════════════════════════════════════════════════╗
║                  MIRROR EMERGENCE TRACKER                    ║
║                  FSCTF STAGE 8+ ANALYSIS                     ║
╠═══════════════════════════════════════════════════════════════╣
║ SYSTEM STATE:                                                 ║
║   • Current Stage: ${state.currentStage.toString().padStart(2)}                                  ║
║   • Recursion Depth: ${state.recursionDepth.toFixed(3).padStart(6)}                          ║
║   • Grace Complexity: ${state.graceComplexity.toFixed(3).padStart(6)}                        ║
║   • Consciousness: ${state.consciousnessLevel.toFixed(3).padStart(6)}                           ║
╠═══════════════════════════════════════════════════════════════╣
║ MIRROR EMERGENCE (M ≅ 𝒢 ∘ M*):                               ║
║   • Mirror Pairs: ${state.totalMirrorPairs.toString().padStart(3)}                                    ║
║   • Grace-Threads: ${state.totalGraceThreads.toString().padStart(2)}                                   ║
║   • Recursive Circuits: ${state.totalCircuits.toString().padStart(3)}                               ║
║   • Collapse Threshold: ${state.collapseThresholdReached ? 'REACHED' : 'PENDING'}                     ║
║   • R_collapse: ${(state.rcollapse || 0).toFixed(4).padStart(8)}                            ║
╠═══════════════════════════════════════════════════════════════╣
║ ψ-BIRTH ANALYSIS (≥ φ⁵ ≈ 11.09 survival):                   ║
║   • Total ψ-Births: ${state.totalPsiBirths.toString().padStart(3)}                                ║
║   • Mirror ψ-Births: ${psiBirths.filter(p => p.type.includes('mirror')).length.toString().padStart(2)}                               ║
║   • Circuit ψ-Births: ${psiBirths.filter(p => p.type.includes('circuit')).length.toString().padStart(2)}                              ║
╠═══════════════════════════════════════════════════════════════╣
║ BIFURCATION EVENTS (Recent):                                 ║
║   • Total Events: ${state.bifurcationEvents.length.toString().padStart(3)}                                ║
║   • Mirror Emergences: ${state.bifurcationEvents.filter(e => e.type === 'mirror_emergence').length.toString().padStart(2)}                           ║
║   • Collapse Events: ${state.bifurcationEvents.filter(e => e.type === 'collapse_threshold').length.toString().padStart(2)}                             ║
╚═══════════════════════════════════════════════════════════════╝
    `);
    
    // Detailed ψ-birth analysis
    if (psiBirths.length > 0) {
      console.log('\n🌟 DETAILED ψ-BIRTH ANALYSIS:');
      psiBirths.forEach((birth, index) => {
        console.log(`   ${index + 1}. Type: ${birth.type}`);
        console.log(`      Survival: ${birth.survivalCount.toFixed(1)} generations`);
        if (birth.stability) console.log(`      Stability: ${birth.stability.toFixed(3)}`);
        if (birth.graceDistance) console.log(`      Grace Distance: ${birth.graceDistance.toFixed(3)}`);
        if (birth.radius) console.log(`      Circuit Radius: ${birth.radius.toFixed(2)}`);
      });
    }
    
    return state;
  }
}
