/**
 * GPU-Morphic Bridge
 * Bridges CPU morphic strands to GPU particle system for massive emergence
 */

export class GPUMorphicBridge {
  constructor() {
    this.enabled = false; // Safe default - off until user enables
    this.particleFieldTexture = null;
    this.morphicInfluenceRadius = 5.0;
    this.φRecursionLevels = 12; // Start conservative, can increase
    this.lastUpdate = 0;
    this.updateInterval = 250; // JITTER FIX: Update every 250ms for smoother performance
    
    console.log('🌊 GPU-Morphic Bridge initialized (disabled by default)');
  }
  
  /**
   * Safe bridge: CPU strands influence GPU particles without breaking existing logic
   */
  bridgeMorphicFieldToGPU(morphicStrands, gl, positionTexture) {
    if (!this.enabled || !morphicStrands || morphicStrands.length === 0) return;
    
    const now = performance.now();
    if (now - this.lastUpdate < this.updateInterval) return; // Throttle updates
    
    try {
      // ANTI-JITTER: Use much smaller texture and pre-allocated buffer
      if (!this.fieldDataBuffer) {
        this.fieldDataBuffer = new Float32Array(256 * 256 * 4); // 256KB instead of 16MB
        this.textureSize = 256;
      }
      
      // Clear the buffer (reuse allocation)
      this.fieldDataBuffer.fill(0);
      
      // Each morphic strand creates a φ-scaled influence field (limited to prevent hitches)
      const maxStrands = Math.min(morphicStrands.length, 50); // Limit processing
      for (let i = 0; i < maxStrands; i++) {
        this.addStrandInfluence(this.fieldDataBuffer, morphicStrands[i], this.textureSize, this.textureSize);
      }
      
      // Upload to GPU for use by simulation shader
      this.updateMorphicFieldTexture(gl, this.fieldDataBuffer);
      this.lastUpdate = now;
      
    } catch (error) {
      console.warn('🌊 GPU-Morphic Bridge: Safe fallback due to:', error.message);
      // Safe fallback - disable if error occurs
      this.enabled = false;
    }
  }
  
  /**
   * Add φ-recursive morphic strand influence to field texture
   */
  addStrandInfluence(fieldData, strand, width, height) {
    const phi = 1.618033988749895;
    const strandX = ((strand.x + 2.0) / 4.0) * width;  // Map from [-2,2] to texture coords
    const strandY = ((strand.y + 2.0) / 4.0) * height;
    
    // φ-recursive influence field around each strand
    const radius = this.morphicInfluenceRadius * (strand.amplitude || 1.0);
    const maxRadius = Math.min(50, radius); // Performance limit
    
    const centerX = Math.floor(strandX);
    const centerY = Math.floor(strandY);
    const radiusInt = Math.floor(maxRadius);
    
    for (let dy = -radiusInt; dy <= radiusInt; dy++) {
      for (let dx = -radiusInt; dx <= radiusInt; dx++) {
        const x = centerX + dx;
        const y = centerY + dy;
        
        if (x < 0 || x >= width || y < 0 || y >= height) continue;
        
        const dist = Math.sqrt(dx*dx + dy*dy);
        if (dist > maxRadius) continue;
        
        const index = (y * width + x) * 4;
        
        // φ-recursive field calculation
        const φScale = Math.pow(phi, -dist / maxRadius);
        const influence = (strand.stability || 0.5) * φScale * Math.exp(-dist / maxRadius);
        const chirality = strand.chirality || 0.0;
        
        // RGBA channels carry different aspects of morphic field
        fieldData[index + 0] += influence;                    // Red: Field strength
        fieldData[index + 1] += influence * chirality;        // Green: Chirality
        fieldData[index + 2] += influence * (strand.phase || 0);     // Blue: Phase
        fieldData[index + 3] += influence * φScale;           // Alpha: φ-scaling
      }
    }
  }
  
  /**
   * Update GPU texture with morphic field data
   */
  updateMorphicFieldTexture(gl, fieldData) {
    if (!this.particleFieldTexture) {
      // Create texture first time
      this.particleFieldTexture = gl.createTexture();
      gl.bindTexture(gl.TEXTURE_2D, this.particleFieldTexture);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    } else {
      gl.bindTexture(gl.TEXTURE_2D, this.particleFieldTexture);
    }
    
    // Upload field data to GPU
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA32F, 1024, 1024, 0, gl.RGBA, gl.FLOAT, fieldData);
  }
  
  /**
   * Get shader uniforms for morphic field access
   */
  getShaderUniforms() {
    return {
      enableMorphicBridge: this.enabled ? 1.0 : 0.0,
      morphicInfluenceRadius: this.morphicInfluenceRadius,
      morphicFieldTexture: this.particleFieldTexture,
      phiRecursionLevels: this.φRecursionLevels
    };
  }
  
  /**
   * Enable GPU-Morphic Bridge
   */
  enable() {
    this.enabled = true;
    console.log('🌊 GPU-Morphic Bridge ACTIVATED');
    console.log('   1,048,576 particles now respond to morphic field');
    console.log('   CPU strands create φ-recursive influence fields on GPU');
    
    // Visual feedback
    if (typeof document !== 'undefined') {
      document.body.style.borderTop = '3px solid #39f';
      setTimeout(() => {
        if (document.body.style.borderTop === '3px solid rgb(51, 153, 255)') {
          document.body.style.borderTop = '';
        }
      }, 2000);
    }
  }
  
  /**
   * Disable GPU-Morphic Bridge
   */
  disable() {
    this.enabled = false;
    console.log('🌊 GPU-Morphic Bridge deactivated');
    console.log('   Back to CPU-only morphic strands');
  }
  
  /**
   * Get bridge statistics
   */
  getStats() {
    return {
      enabled: this.enabled,
      influenceRadius: this.morphicInfluenceRadius,
      recursionLevels: this.φRecursionLevels,
      lastUpdate: this.lastUpdate,
      textureCreated: !!this.particleFieldTexture
    };
  }
  
  /**
   * Cleanup resources
   */
  cleanup(gl) {
    if (this.particleFieldTexture && gl) {
      gl.deleteTexture(this.particleFieldTexture);
      this.particleFieldTexture = null;
    }
  }
}
