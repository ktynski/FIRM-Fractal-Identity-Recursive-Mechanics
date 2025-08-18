/**
 * GPU Measurements System
 * High-performance GPU-based measurements of simulation state
 */

export class GPUMeasurements {
  constructor(gl) {
    this.gl = gl;
    
    // Check for required extensions
    this.hasFloatTextures = !!gl.getExtension('EXT_color_buffer_float');
    this.hasHalfFloatTextures = !!gl.getExtension('EXT_color_buffer_half_float');
    
    // Measurement configuration
    this.sampleWidth = 24;   // Reduced for performance
    this.sampleHeight = 24;
    this.corrSize = 32;      // Correlation measurement size
    
    console.log('📏 GPU Measurements System initialized');
    console.log(`   Float textures: ${this.hasFloatTextures ? 'available' : 'not available'}`);
    console.log(`   Sample size: ${this.sampleWidth}x${this.sampleHeight}`);
  }
  
  /**
   * Measure average kinetic energy E ≈ <|v|^2>
   * Uses downsampled velocity texture for efficiency
   */
  measureEnergy(velTexture, reduceProg, quadVao, fboSample) {
    const gl = this.gl;
    
    // Save current viewport
    const prevViewport = gl.getParameter(gl.VIEWPORT);
    
    // Render to sample framebuffer
    gl.bindFramebuffer(gl.FRAMEBUFFER, fboSample);
    gl.viewport(0, 0, this.sampleWidth, this.sampleHeight);
    
    // Use reduce program to compute velocity magnitude squared
    gl.useProgram(reduceProg);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, velTexture);
    gl.uniform1i(gl.getUniformLocation(reduceProg, 'velTex'), 0);
    
    // Render fullscreen quad
    gl.bindVertexArray(quadVao);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.bindVertexArray(null);
    
    // Read back results
    let sum = 0.0;
    if (this.hasFloatTextures) {
      const buf = new Float32Array(this.sampleWidth * this.sampleHeight * 4);
      gl.readPixels(0, 0, this.sampleWidth, this.sampleHeight, gl.RGBA, gl.FLOAT, buf);
      for (let i = 0; i < buf.length; i += 4) {
        sum += buf[i];
      }
    } else {
      const buf = new Uint8Array(this.sampleWidth * this.sampleHeight * 4);
      gl.readPixels(0, 0, this.sampleWidth, this.sampleHeight, gl.RGBA, gl.UNSIGNED_BYTE, buf);
      for (let i = 0; i < buf.length; i += 4) {
        sum += buf[i] / 255.0;
      }
    }
    
    // Restore viewport
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    gl.viewport(prevViewport[0], prevViewport[1], prevViewport[2], prevViewport[3]);
    
    const avgEnergy = sum / (this.sampleWidth * this.sampleHeight);
    return avgEnergy;
  }
  
  /**
   * Measure flow correlation
   * Computes normalized dot product of flow fields
   */
  measureCorrelation(corrProg, quadVao, fboCorr, params) {
    const gl = this.gl;
    
    // Save current viewport
    const prevViewport = gl.getParameter(gl.VIEWPORT);
    
    // Render correlation computation
    gl.bindFramebuffer(gl.FRAMEBUFFER, fboCorr);
    gl.viewport(0, 0, this.corrSize, this.corrSize);
    
    gl.useProgram(corrProg);
    
    // Set uniforms for correlation computation
    gl.uniform1f(gl.getUniformLocation(corrProg, 'fieldScale'), params.fieldScale || 1.0);
    gl.uniform1f(gl.getUniformLocation(corrProg, 'timeScale'), params.timeScale || 1.0);
    gl.uniform1f(gl.getUniformLocation(corrProg, 'reflectDelta'), 0.731);
    gl.uniform1f(gl.getUniformLocation(corrProg, 'time'), performance.now() * 0.001);
    gl.uniform1f(gl.getUniformLocation(corrProg, 'domain'), params.domain || 1.0);
    
    // Render
    gl.bindVertexArray(quadVao);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.bindVertexArray(null);
    
    // Read back correlation values
    let sum = 0;
    if (this.hasFloatTextures) {
      const buf = new Float32Array(this.corrSize * this.corrSize * 4);
      gl.readPixels(0, 0, this.corrSize, this.corrSize, gl.RGBA, gl.FLOAT, buf);
      for (let i = 0; i < buf.length; i += 4) {
        sum += buf[i];
      }
    } else {
      const buf = new Uint8Array(this.corrSize * this.corrSize * 4);
      gl.readPixels(0, 0, this.corrSize, this.corrSize, gl.RGBA, gl.UNSIGNED_BYTE, buf);
      for (let i = 0; i < buf.length; i += 4) {
        sum += buf[i] / 255.0;
      }
    }
    
    // Restore viewport
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    gl.viewport(prevViewport[0], prevViewport[1], prevViewport[2], prevViewport[3]);
    
    const avgCorrelation = sum / (this.corrSize * this.corrSize);
    return avgCorrelation;
  }
  
  /**
   * Blit texture to framebuffer with optional fade
   */
  blitTo(targetFbo, srcTex, width, height, decayProg, quadVao, fade = 1.0) {
    const gl = this.gl;
    
    const prevViewport = gl.getParameter(gl.VIEWPORT);
    gl.bindFramebuffer(gl.FRAMEBUFFER, targetFbo);
    gl.viewport(0, 0, width, height);
    
    gl.useProgram(decayProg);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, srcTex);
    gl.uniform1i(gl.getUniformLocation(decayProg, 'srcTex'), 0);
    gl.uniform1f(gl.getUniformLocation(decayProg, 'fade'), fade);
    
    gl.bindVertexArray(quadVao);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.bindVertexArray(null);
    
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    gl.viewport(prevViewport[0], prevViewport[1], prevViewport[2], prevViewport[3]);
  }
  
  /**
   * Compute Psi and FRST metrics from history textures
   */
  computePsiAndFrst(histA, histB, fboSampleHistA, fboSampleHistB, decayProg, quadVao) {
    const gl = this.gl;
    
    // Downsample current and previous histories
    this.blitTo(fboSampleHistA, histA, this.sampleWidth, this.sampleHeight, decayProg, quadVao);
    this.blitTo(fboSampleHistB, histB, this.sampleWidth, this.sampleHeight, decayProg, quadVao);
    
    let bufA, bufB;
    
    // Read back both history buffers
    if (this.hasFloatTextures) {
      bufA = new Float32Array(this.sampleWidth * this.sampleHeight * 4);
      bufB = new Float32Array(this.sampleWidth * this.sampleHeight * 4);
      
      gl.bindFramebuffer(gl.FRAMEBUFFER, fboSampleHistA);
      gl.readPixels(0, 0, this.sampleWidth, this.sampleHeight, gl.RGBA, gl.FLOAT, bufA);
      gl.bindFramebuffer(gl.FRAMEBUFFER, fboSampleHistB);
      gl.readPixels(0, 0, this.sampleWidth, this.sampleHeight, gl.RGBA, gl.FLOAT, bufB);
    } else {
      bufA = new Uint8Array(this.sampleWidth * this.sampleHeight * 4);
      bufB = new Uint8Array(this.sampleWidth * this.sampleHeight * 4);
      
      gl.bindFramebuffer(gl.FRAMEBUFFER, fboSampleHistA);
      gl.readPixels(0, 0, this.sampleWidth, this.sampleHeight, gl.RGBA, gl.UNSIGNED_BYTE, bufA);
      gl.bindFramebuffer(gl.FRAMEBUFFER, fboSampleHistB);
      gl.readPixels(0, 0, this.sampleWidth, this.sampleHeight, gl.RGBA, gl.UNSIGNED_BYTE, bufB);
    }
    
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    
    // Process buffers to compute Psi and FRST
    const results = this.processPsiFrstBuffers(bufA, bufB);
    
    return results;
  }
  
  /**
   * Process history buffers to compute Psi and FRST metrics
   */
  processPsiFrstBuffers(bufA, bufB) {
    const n = this.sampleWidth * this.sampleHeight;
    let sumActivity = 0, sumStability = 0, sumCoherence = 0;
    let maxActivity = 0;
    
    const scaleFactor = this.hasFloatTextures ? 1.0 : (1.0 / 255.0);
    
    for (let i = 0; i < n * 4; i += 4) {
      // Extract values (assuming R=activity, G=stability, B=coherence)
      const activity = bufA[i] * scaleFactor;
      const stability = bufA[i + 1] * scaleFactor;
      const coherence = bufA[i + 2] * scaleFactor;
      
      sumActivity += activity;
      sumStability += stability;
      sumCoherence += coherence;
      
      maxActivity = Math.max(maxActivity, activity);
    }
    
    // Compute normalized metrics
    const avgActivity = sumActivity / n;
    const avgStability = sumStability / n;
    const avgCoherence = sumCoherence / n;
    
    // Psi: particle activity metric
    const psi = avgActivity * (1.0 + maxActivity * 0.1); // Boost for peak activity
    
    // FRST: Fractal Recursive Survivability Tracker
    const frst = avgStability * avgCoherence * Math.sqrt(avgActivity);
    
    return {
      psi: Math.max(0, psi),
      frst: Math.max(0, frst),
      activity: avgActivity,
      stability: avgStability,
      coherence: avgCoherence,
      maxActivity: maxActivity,
      samples: n
    };
  }
  
  /**
   * Get measurement capabilities
   */
  getCapabilities() {
    return {
      hasFloatTextures: this.hasFloatTextures,
      hasHalfFloatTextures: this.hasHalfFloatTextures,
      sampleSize: `${this.sampleWidth}x${this.sampleHeight}`,
      correlationSize: `${this.corrSize}x${this.corrSize}`,
      precision: this.hasFloatTextures ? 'float32' : 'uint8'
    };
  }
  
  /**
   * Update sample dimensions (for performance tuning)
   */
  setSampleSize(width, height) {
    this.sampleWidth = Math.max(8, Math.min(64, width));
    this.sampleHeight = Math.max(8, Math.min(64, height));
    console.log(`📏 Sample size updated to ${this.sampleWidth}x${this.sampleHeight}`);
  }
  
  /**
   * Cleanup resources
   */
  cleanup() {
    // GPU measurement cleanup if needed
    console.log('📏 GPU Measurements cleanup');
  }
}
