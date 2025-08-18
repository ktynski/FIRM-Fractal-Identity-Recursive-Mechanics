/**
 * Strand Manager
 * Manages morphic strand lifecycle and memory optimization
 */

export class StrandManager {
  constructor() {
    this.MEMORY_LIMITS = {
      MAX_STRANDS: 500,
      MAX_GENERATIONS: 20,
      CLEANUP_THRESHOLD: 400
    };
    
    this.cleanupCount = 0;
    this.lastCleanup = 0;
    this.strandMetrics = {
      created: 0,
      cleaned: 0,
      maxStability: 0,
      avgLifetime: 0
    };
    
    console.log('🌊 Strand Manager initialized - morphic strand lifecycle management');
  }
  
  cleanupStrands(graceOperator) {
    if (!graceOperator || !graceOperator.morphicStrands) return;
    
    const strands = graceOperator.morphicStrands;
    const currentTime = Date.now();
    
    if (strands.length > this.MEMORY_LIMITS.MAX_STRANDS) {
      const sortedStrands = strands
        .map((s, i) => ({ ...s, index: i, age: currentTime - (s.timestamp || currentTime) }))
        .sort((a, b) => {
          const stabilityA = this.getStabilityScore(a.stability);
          const stabilityB = this.getStabilityScore(b.stability);
          if (stabilityA !== stabilityB) return stabilityB - stabilityA;
          return a.age - b.age;
        });
      
      const keepCount = Math.floor(this.MEMORY_LIMITS.MAX_STRANDS * 0.8);
      graceOperator.morphicStrands = sortedStrands.slice(0, keepCount);
      
      this.cleanupCount++;
      this.strandMetrics.cleaned += strands.length - keepCount;
      
      console.log(`🧹 Strand cleanup: removed ${strands.length - keepCount} old strands, kept ${keepCount}`);
    }
    
    // Remove strands older than 5 seconds
    const initialCount = graceOperator.morphicStrands.length;
    graceOperator.morphicStrands = graceOperator.morphicStrands.filter(strand => {
      const age = currentTime - (strand.timestamp || currentTime);
      return age < 5000; // 5 seconds
    });
    
    if (graceOperator.morphicStrands.length < initialCount) {
      console.log(`⏰ Age cleanup: removed ${initialCount - graceOperator.morphicStrands.length} old strands`);
    }
    
    this.lastCleanup = currentTime;
  }
  
  getStabilityScore(stability) {
    if (typeof stability === 'number') return Math.max(0, Math.min(2, stability));
    if (typeof stability === 'object' && stability.value) return stability.value;
    return 0;
  }
  
  analyzeStrands(strands) {
    if (!strands || strands.length === 0) {
      return { avgStability: 0, maxStability: 0, strandCount: 0, generations: 0 };
    }
    
    let totalStability = 0;
    let maxStability = 0;
    let maxGeneration = 0;
    
    strands.forEach(strand => {
      const stability = this.getStabilityScore(strand.stability);
      totalStability += stability;
      maxStability = Math.max(maxStability, stability);
      maxGeneration = Math.max(maxGeneration, strand.generation || 0);
    });
    
    return {
      avgStability: totalStability / strands.length,
      maxStability: maxStability,
      strandCount: strands.length,
      generations: maxGeneration
    };
  }
  
  getMetrics() {
    return {
      ...this.strandMetrics,
      cleanupCount: this.cleanupCount,
      lastCleanup: this.lastCleanup,
      memoryLimits: this.MEMORY_LIMITS
    };
  }
  
  shouldCleanup(strandCount) {
    return strandCount > this.MEMORY_LIMITS.CLEANUP_THRESHOLD || 
           (Date.now() - this.lastCleanup) > 10000; // 10 seconds
  }
}

/**
 * Optimized particle data management
 */
export class OptimizedStrandManager extends StrandManager {
  constructor() {
    super();
    this.particleData = new Float32Array(0);
    this.particleBuffer = null;
    this.lastUpdateFrame = -1;
    this.updateThreshold = 5; // Update every 5 frames
  }
  
  updateParticleBuffer(gl, frameCount) {
    // Only update GPU buffer when necessary
    if (frameCount - this.lastUpdateFrame < this.updateThreshold) {
      return;
    }
    
    if (!this.particleBuffer) {
      this.particleBuffer = gl.createBuffer();
    }
    
    // Batch update all particle data at once
    const strands = this.getActiveStrands();
    const dataSize = strands.length * 8; // x, y, z, phase, amplitude, stability, chirality, generation
    
    if (this.particleData.length !== dataSize) {
      this.particleData = new Float32Array(dataSize);
    }
    
    let offset = 0;
    for (const strand of strands) {
      this.particleData[offset++] = strand.x || 0;
      this.particleData[offset++] = strand.y || 0;
      this.particleData[offset++] = strand.z || 0;
      this.particleData[offset++] = strand.phase || 0;
      this.particleData[offset++] = strand.amplitude || 0;
      this.particleData[offset++] = strand.stability || 0;
      this.particleData[offset++] = strand.chirality || 0;
      this.particleData[offset++] = strand.generation || 0;
    }
    
    gl.bindBuffer(gl.ARRAY_BUFFER, this.particleBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, this.particleData, gl.DYNAMIC_DRAW);
    
    this.lastUpdateFrame = frameCount;
  }
  
  getActiveStrands() {
    // Return active strands for buffer updates
    return this.strands || [];
  }
}
