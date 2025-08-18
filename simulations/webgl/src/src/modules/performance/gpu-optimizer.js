/**
 * GPU Performance Optimizer for FSCTF Particle Systems
 * 
 * Dynamically adapts particle count, rendering quality, and shader complexity 
 * based on real-time performance metrics to maintain smooth 60fps experience
 * while maximizing visual fidelity of soul emergence structures.
 * 
 * FSCTF Integration: Preserves morphogenetic cascade visual integrity
 * while optimizing computational load through intelligent quality scaling.
 */

export class GPUOptimizer {
  constructor(targetFPS = 60, minFPS = 30) {
    // Performance targets
    this.targetFPS = targetFPS;
    this.minFPS = minFPS;
    this.maxFPS = targetFPS + 10; // Allow headroom
    
    // Frame rate monitoring
    this.frameTimes = []; // Rolling window of frame times
    this.frameTimeWindow = 60; // Monitor last 60 frames (~1 second)
    this.currentFPS = 60;
    this.averageFPS = 60;
    this.lastFrameTime = performance.now();
    
    // Quality adaptation state - OPTIMIZED for better performance scaling
    this.qualityLevel = 1.0; // 0.1 to 2.0 scale
    this.particleCountMultiplier = 1.0; // Adjusts base particle count
    this.shaderComplexityLevel = 1.0; // Reduces shader calculations
    this.adaptationSmoothing = 0.95; // Faster adaptation for better responsiveness
    
    // PERFORMANCE OPTIMIZATIONS: Particle LOD and culling
    this.dynamicLOD = true; // Enable particle level of detail
    this.cullDistantParticles = true; // Cull particles outside view
    this.maxRenderDistance = 50.0; // Maximum rendering distance for culling
    
    // Performance profiling
    this.gpuTimings = [];
    this.cpuTimings = [];
    this.bottleneckDetector = {
      gpuBound: 0,
      cpuBound: 0,
      memoryBound: 0
    };
    
    // AGGRESSIVE ADAPTATION: More responsive to performance drops
    this.qualityThresholds = {
      // FPS -> Quality multiplier mapping (more aggressive scaling)
      excellent: { fps: 50, quality: 1.2, particles: 1.0 }, // Conservative scaling up
      good: { fps: 40, quality: 1.0, particles: 1.0 },      // Maintain current
      fair: { fps: 30, quality: 0.6, particles: 0.4 },      // Quick reduction
      poor: { fps: 20, quality: 0.3, particles: 0.2 },      // Aggressive reduction
      critical: { fps: 10, quality: 0.15, particles: 0.1 }   // Emergency minimum
    };
    
    // Quality presets for different performance levels
    this.qualityPresets = {
      ultra: {
        name: 'Ultra (1M+ particles)',
        cols: 1024, rows: 1024, // 1,048,576 particles
        shaderComplexity: 1.0,
        visualEffects: 1.0,
        updateFrequency: 1 // Every frame
      },
      high: {
        name: 'High (590K particles)', 
        cols: 768, rows: 768, // 589,824 particles
        shaderComplexity: 0.9,
        visualEffects: 0.95,
        updateFrequency: 1
      },
      standard: {
        name: 'Standard (262K particles)',
        cols: 512, rows: 512, // 262,144 particles  
        shaderComplexity: 0.8,
        visualEffects: 0.9,
        updateFrequency: 1
      },
      performance: {
        name: 'Performance (65K particles)',
        cols: 256, rows: 256, // 65,536 particles
        shaderComplexity: 0.6,
        visualEffects: 0.7,
        updateFrequency: 2 // Every other frame
      },
      battery: {
        name: 'Battery Saver (16K particles)',
        cols: 128, rows: 128, // 16,384 particles
        shaderComplexity: 0.4,
        visualEffects: 0.5,
        updateFrequency: 3 // Every 3rd frame
      }
    };
    
    this.currentPreset = 'standard';
    this.autoAdaptationEnabled = true;
    this.lastAdaptationTime = 0;
    this.adaptationCooldown = 2000; // 2 second cooldown between major changes
    
    // Performance history for learning
    this.performanceHistory = [];
    this.maxHistoryLength = 300; // 5 minutes at 1Hz sampling
    
    console.log('🚀 GPU Optimizer initialized');
    console.log(`📊 Target: ${targetFPS}fps, Min: ${minFPS}fps`);
    console.log(`🎮 Current preset: ${this.qualityPresets[this.currentPreset].name}`);
  }
  
  /**
   * Update performance monitoring and trigger adaptations
   */
  update(frameTime, renderStats = {}) {
    const currentTime = performance.now();
    const deltaTime = currentTime - this.lastFrameTime;
    this.lastFrameTime = currentTime;
    
    // Track frame time
    this.frameTimes.push(deltaTime);
    if (this.frameTimes.length > this.frameTimeWindow) {
      this.frameTimes.shift();
    }
    
    // Calculate current and average FPS
    this.currentFPS = 1000 / deltaTime;
    if (this.frameTimes.length > 10) {
      const avgFrameTime = this.frameTimes.reduce((sum, t) => sum + t, 0) / this.frameTimes.length;
      this.averageFPS = 1000 / avgFrameTime;
    }
    
    // Store performance metrics
    if (renderStats.gpuTime) {
      this.gpuTimings.push(renderStats.gpuTime);
      if (this.gpuTimings.length > 60) this.gpuTimings.shift();
    }
    
    if (renderStats.cpuTime) {
      this.cpuTimings.push(renderStats.cpuTime);
      if (this.cpuTimings.length > 60) this.cpuTimings.shift();
    }
    
    // Detect bottlenecks
    this.detectBottlenecks();
    
    // Trigger adaptation if needed
    if (this.autoAdaptationEnabled) {
      this.adaptQuality(currentTime);
    }
    
    // Store performance history periodically
    if (currentTime - this.lastHistoryUpdate > 1000) {
      this.updatePerformanceHistory();
      this.lastHistoryUpdate = currentTime;
    }
  }
  
  /**
   * Detect whether we're GPU-bound, CPU-bound, or memory-bound
   */
  detectBottlenecks() {
    if (this.gpuTimings.length < 10 || this.cpuTimings.length < 10) return;
    
    const avgGPU = this.gpuTimings.reduce((sum, t) => sum + t, 0) / this.gpuTimings.length;
    const avgCPU = this.cpuTimings.reduce((sum, t) => sum + t, 0) / this.cpuTimings.length;
    
    // Simple heuristics for bottleneck detection
    if (avgGPU > avgCPU * 2) {
      this.bottleneckDetector.gpuBound++;
    } else if (avgCPU > avgGPU * 2) {
      this.bottleneckDetector.cpuBound++;
    }
    
    // Memory bound detection (simplified)
    const totalTime = avgGPU + avgCPU;
    if (totalTime > 16.67 && avgGPU / totalTime < 0.6 && avgCPU / totalTime < 0.6) {
      this.bottleneckDetector.memoryBound++;
    }
  }
  
  /**
   * Intelligent quality adaptation based on performance metrics
   */
  adaptQuality(currentTime) {
    // Cooldown check to prevent thrashing
    if (currentTime - this.lastAdaptationTime < this.adaptationCooldown) {
      return;
    }
    
    // Determine target quality level based on FPS
    let targetQuality = this.qualityLevel;
    let targetParticles = this.particleCountMultiplier;
    let shouldChangePreset = false;
    let newPreset = this.currentPreset;
    
    // FPS-based adaptation logic
    if (this.averageFPS > this.qualityThresholds.excellent.fps) {
      // Performance headroom - can increase quality
      targetQuality = Math.min(2.0, this.qualityLevel * 1.1);
      targetParticles = Math.min(2.0, this.particleCountMultiplier * 1.05);
      
      // Consider upgrading preset
      if (this.currentPreset === 'standard' && this.averageFPS > 50) {
        newPreset = 'high';
        shouldChangePreset = true;
      } else if (this.currentPreset === 'high' && this.averageFPS > 55) {
        newPreset = 'ultra';
        shouldChangePreset = true;
      }
      
    } else if (this.averageFPS < this.qualityThresholds.poor.fps) {
      // Poor performance - reduce quality aggressively
      targetQuality = Math.max(0.35, this.qualityLevel * 0.85); // FIXED: Preserve more quality during poor performance
      targetParticles = Math.max(0.25, this.particleCountMultiplier * 0.8); // FIXED: Less aggressive particle reduction
      
      // Consider downgrading preset
      if (this.currentPreset === 'ultra') {
        newPreset = 'high';
        shouldChangePreset = true;
      } else if (this.currentPreset === 'high') {
        newPreset = 'standard';
        shouldChangePreset = true;
      } else if (this.currentPreset === 'standard' && this.averageFPS < 25) {
        newPreset = 'performance';
        shouldChangePreset = true;
      }
      
    } else if (this.averageFPS < this.qualityThresholds.fair.fps) {
      // Fair performance - gentle reduction
      targetQuality = Math.max(0.4, this.qualityLevel * 0.95);
      targetParticles = Math.max(0.4, this.particleCountMultiplier * 0.95); // FIXED: Less aggressive particle reduction for fair performance
    }
    
    // Apply bottleneck-specific optimizations
    if (this.bottleneckDetector.gpuBound > 10) {
      // GPU bottleneck - reduce shader complexity more than particle count
      this.shaderComplexityLevel = Math.max(0.3, this.shaderComplexityLevel * 0.9);
      console.log('🔧 GPU Optimizer: GPU bottleneck detected, reducing shader complexity');
    }
    
    if (this.bottleneckDetector.cpuBound > 10) {
      // CPU bottleneck - reduce update frequency more than visual quality  
      targetParticles = Math.max(0.2, targetParticles * 0.85);
      console.log('🔧 GPU Optimizer: CPU bottleneck detected, reducing particle updates');
    }
    
    // Smooth transitions to avoid visual jumps
    this.qualityLevel = this.qualityLevel * this.adaptationSmoothing + targetQuality * (1 - this.adaptationSmoothing);
    this.particleCountMultiplier = this.particleCountMultiplier * this.adaptationSmoothing + targetParticles * (1 - this.adaptationSmoothing);
    
    // Apply preset change if needed
    if (shouldChangePreset && newPreset !== this.currentPreset) {
      this.changeQualityPreset(newPreset);
      this.lastAdaptationTime = currentTime;
      console.log(`🎮 GPU Optimizer: Quality preset changed: ${this.currentPreset} → ${newPreset}`);
      console.log(`📊 Performance: ${this.averageFPS.toFixed(1)}fps avg`);
    }
    
    // Reset bottleneck counters periodically
    if (currentTime % 5000 < 100) {
      this.bottleneckDetector.gpuBound = 0;
      this.bottleneckDetector.cpuBound = 0;
      this.bottleneckDetector.memoryBound = 0;
    }
  }
  
  /**
   * Change quality preset and update system parameters
   */
  changeQualityPreset(presetName) {
    if (!this.qualityPresets[presetName]) {
      console.warn(`🚨 Invalid quality preset: ${presetName}`);
      return false;
    }
    
    const oldPreset = this.currentPreset;
    const preset = this.qualityPresets[presetName];
    this.currentPreset = presetName;
    
    // Update global quality parameters
    if (window.params) {
      // Update particle resolution
      if (window.updateParticleResolution) {
        window.updateParticleResolution(preset.cols, preset.rows);
      }
      
      // Update shader complexity (will be read by shaders via uniforms)
      window.params.shaderComplexity = preset.shaderComplexity;
      // HYPERCUBE PROTECTION: Don't override visualEffects in cosmic phases 4-8
      const cosmogenesisPhase = window.simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
      if (cosmogenesisPhase < 4) {
        window.params.visualEffects = preset.visualEffects;
      } else {
        console.log('🧊 COSMIC PHASE: Preserving hypercube visualEffects, GPU optimizer disabled');
      }
      
      // Update quality info display
      const qualityInfo = document.getElementById('qualityInfo');
      if (qualityInfo) {
        const particleCount = (preset.cols * preset.rows / 1000).toFixed(0);
        qualityInfo.textContent = `${preset.name.split('(')[0].trim()} (${particleCount}K particles)`;
      }
    }
    
    // Update internal state
    this.shaderComplexityLevel = preset.shaderComplexity;
    
    console.log(`✅ GPU Optimizer: Switched from ${oldPreset} to ${presetName}`);
    console.log(`🎯 New settings: ${preset.cols}×${preset.rows} particles, ${(preset.shaderComplexity*100).toFixed(0)}% complexity`);
    
    return true;
  }
  
  /**
   * Get current particle count recommendation based on performance
   */
  getOptimalParticleCount() {
    const preset = this.qualityPresets[this.currentPreset];
    const baseCount = preset.cols * preset.rows;
    return Math.floor(baseCount * this.particleCountMultiplier);
  }

  /**
   * Get optimized particle rendering parameters for better performance
   */
  getParticleRenderingOptimizations() {
    const optimizations = {
      // Base particle count optimization
      drawFraction: Math.min(1.0, this.particleCountMultiplier * this.qualityLevel),
      
      // LOD-based particle culling
      enableLOD: this.dynamicLOD && this.averageFPS < 45,
      lodReductionFactor: Math.max(0.3, this.averageFPS / 60.0),
      
      // Distance-based culling
      enableDistanceCulling: this.cullDistantParticles && this.averageFPS < 35,
      maxRenderDistance: this.maxRenderDistance * Math.max(0.5, this.qualityLevel),
      
      // Particle update optimization
      updateSkipFrames: this.averageFPS < 30 ? Math.max(1, Math.floor(30 / this.averageFPS)) : 1,
      
      // Batch rendering optimization
      enableBatching: this.averageFPS < 40,
      batchSize: Math.max(1000, Math.floor(this.getOptimalParticleCount() * 0.1))
    };
    
    return optimizations;
  }
  
  /**
   * Get shader optimization parameters
   */
  getShaderOptimizations() {
    return {
      complexityLevel: this.shaderComplexityLevel,
      maxRecursionDepth: Math.max(4, Math.floor(90 * this.shaderComplexityLevel)), // FIXED: Scale with 90-phase system
      phiHarmonicReduction: this.shaderComplexityLevel < 0.7,
      skipAdvancedEffects: this.shaderComplexityLevel < 0.5,
      useLOD: this.particleCountMultiplier > 1.0
    };
  }
  
  /**
   * Store performance history for analysis
   */
  updatePerformanceHistory() {
    const entry = {
      timestamp: Date.now(),
      fps: this.averageFPS,
      qualityLevel: this.qualityLevel,
      particleMultiplier: this.particleCountMultiplier,
      preset: this.currentPreset,
      shaderComplexity: this.shaderComplexityLevel
    };
    
    this.performanceHistory.push(entry);
    if (this.performanceHistory.length > this.maxHistoryLength) {
      this.performanceHistory.shift();
    }
  }
  
  /**
   * Force specific quality preset (for manual control)
   */
  setQualityPreset(presetName, disableAutoAdaptation = false) {
    if (this.changeQualityPreset(presetName)) {
      if (disableAutoAdaptation) {
        this.autoAdaptationEnabled = false;
        console.log('🔒 GPU Optimizer: Auto-adaptation disabled (manual control)');
      }
      return true;
    }
    return false;
  }
  
  /**
   * Enable/disable automatic quality adaptation
   */
  setAutoAdaptation(enabled) {
    this.autoAdaptationEnabled = enabled;
    console.log(`${enabled ? '🔓' : '🔒'} GPU Optimizer: Auto-adaptation ${enabled ? 'enabled' : 'disabled'}`);
  }
  
  /**
   * Get comprehensive performance statistics
   */
  getPerformanceStats() {
    const avgGPU = this.gpuTimings.length > 0 ? 
      this.gpuTimings.reduce((sum, t) => sum + t, 0) / this.gpuTimings.length : 0;
    const avgCPU = this.cpuTimings.length > 0 ? 
      this.cpuTimings.reduce((sum, t) => sum + t, 0) / this.cpuTimings.length : 0;
      
    return {
      currentFPS: this.currentFPS,
      averageFPS: this.averageFPS,
      targetFPS: this.targetFPS,
      qualityLevel: this.qualityLevel,
      particleMultiplier: this.particleCountMultiplier,
      shaderComplexity: this.shaderComplexityLevel,
      currentPreset: this.currentPreset,
      optimalParticleCount: this.getOptimalParticleCount(),
      autoAdaptationEnabled: this.autoAdaptationEnabled,
      bottlenecks: { ...this.bottleneckDetector },
      timings: {
        avgGPU: avgGPU,
        avgCPU: avgCPU,
        totalFrame: avgGPU + avgCPU
      },
      performanceHistory: this.performanceHistory.slice(-20) // Last 20 entries
    };
  }
  
  /**
   * Generate performance report
   */
  generatePerformanceReport() {
    const stats = this.getPerformanceStats();
    const preset = this.qualityPresets[this.currentPreset];
    
    console.log(`
╔═══════════════════════════════════════════════════════════════╗
║                    GPU PERFORMANCE OPTIMIZER                 ║
║                       REAL-TIME REPORT                       ║
╠═══════════════════════════════════════════════════════════════╣
║ PERFORMANCE METRICS:                                          ║
║   • Current FPS: ${stats.currentFPS.toFixed(1).padStart(6)}                               ║
║   • Average FPS: ${stats.averageFPS.toFixed(1).padStart(6)}                               ║
║   • Target FPS:  ${stats.targetFPS.toString().padStart(6)}                                ║
║   • Quality Level: ${(stats.qualityLevel * 100).toFixed(0).padStart(4)}%                               ║
╠═══════════════════════════════════════════════════════════════╣
║ CURRENT CONFIGURATION:                                        ║
║   • Preset: ${this.currentPreset.padEnd(12)}                                 ║
║   • Particles: ${(preset.cols * preset.rows / 1000).toFixed(0).padStart(4)}K (${preset.cols}×${preset.rows})                    ║
║   • Shader Complexity: ${(stats.shaderComplexity * 100).toFixed(0).padStart(3)}%                        ║
║   • Particle Multiplier: ${stats.particleMultiplier.toFixed(2)}x                          ║
║   • Auto-Adaptation: ${stats.autoAdaptationEnabled ? 'ENABLED ' : 'DISABLED'}                        ║
╠═══════════════════════════════════════════════════════════════╣
║ BOTTLENECK ANALYSIS:                                          ║
║   • GPU Bound: ${stats.bottlenecks.gpuBound.toString().padStart(3)} occurrences                      ║
║   • CPU Bound: ${stats.bottlenecks.cpuBound.toString().padStart(3)} occurrences                      ║
║   • Memory Bound: ${stats.bottlenecks.memoryBound.toString().padStart(3)} occurrences                   ║
╠═══════════════════════════════════════════════════════════════╣
║ TIMING BREAKDOWN:                                             ║
║   • Avg GPU Time: ${stats.timings.avgGPU.toFixed(2).padStart(5)}ms                           ║
║   • Avg CPU Time: ${stats.timings.avgCPU.toFixed(2).padStart(5)}ms                           ║
║   • Total Frame: ${stats.timings.totalFrame.toFixed(2).padStart(6)}ms                          ║
╚═══════════════════════════════════════════════════════════════╝
    `);
    
    return stats;
  }
  
  /**
   * Emergency performance recovery
   */
  emergencyPerformanceRecovery() {
    console.log('🚨 GPU Optimizer: EMERGENCY PERFORMANCE RECOVERY ACTIVATED');
    
    // Force lowest quality preset
    this.changeQualityPreset('battery');
    
    // FIXED: Less aggressive emergency reduction - preserve some complexity
    this.qualityLevel = 0.4;
    this.particleCountMultiplier = 0.3;
    this.shaderComplexityLevel = 0.5;
    
    // Enable aggressive optimizations
    if (window.params) {
      window.params.shaderComplexity = 0.3;
      // HYPERCUBE PROTECTION: Never disable hypercube effects in cosmic phases
      const cosmogenesisPhase = window.simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
      if (cosmogenesisPhase < 4) {
        window.params.visualEffects = 0.4;  // Emergency reduction for early phases only
      } else {
        console.log('🧊 EMERGENCY: Cosmic phase detected, maintaining minimum hypercube threshold');
        window.params.visualEffects = Math.max(window.params.visualEffects || 0.7, 0.7); // Never below tesseract threshold
      }
      
      // Reduce update frequencies for non-critical systems
      if (window.simulationCore?.fsctfEngine?.soulEchoTracker) {
        window.simulationCore.fsctfEngine.soulEchoTracker.analysisFrameInterval = 30; // Every 30 frames
      }
    }
    
    console.log('🛡️ Emergency settings applied - minimal viable performance mode');
    console.log('💡 Re-enable auto-adaptation once performance stabilizes');
    
    // Re-enable auto-adaptation after delay
    setTimeout(() => {
      this.autoAdaptationEnabled = true;
      console.log('🔄 Auto-adaptation re-enabled');
    }, 5000);
  }
}
