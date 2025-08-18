/**
 * Simulation Core
 * Main simulation loop and coordination of all subsystems
 */

import { PERFORMANCE_MONITOR, updatePerformanceMetrics } from '../performance/performance.js';
import { FSCTFEngine } from '../fsctf/fsctf-engine.js';

export class SimulationCore {
  constructor(gl, shaders, params, canvas = null) {
    this.gl = gl;
    this.shaders = shaders;
    this.params = params;
    this.canvas = canvas;
    
    // Frame tracking
    this.frameCounter = 0;
    this.lastFrameTime = performance.now();
    
    // FSCTF Engine with WebGL context for blob detection
    this.fsctfEngine = new FSCTFEngine(gl, canvas);
    
    // WebGL state
    this.isContextLost = false;
    
    console.log('🎮 Simulation Core initialized');
  }
  
  /**
   * Main simulation update loop
   */
  update() {
    const frameStart = performance.now();
    const now = frameStart * 0.001;
    const deltaTime = frameStart - this.lastFrameTime;
    this.lastFrameTime = frameStart;
    
    // Update performance metrics
    const avgFrameTime = updatePerformanceMetrics(deltaTime);
    
    // PERFORMANCE: Target 30 FPS for 1M particles (more realistic than 60 FPS)
    const frameBudget = 33.33; // 30 FPS target for high particle counts
    
    // Track frame time globally for performance monitoring
    window.lastFrameTime = deltaTime;
    
    // ANTI-STROBE: Disable frame skipping for 1M particles - causes visual juddering
    // With 1M particles, 30fps (33ms) is acceptable, 20fps (50ms) is still usable
    // Skipping creates worse visual artifacts than slower but consistent frame rates
    if (deltaTime > 200) { // Only skip if completely frozen (< 5 FPS)
      console.warn(`⚠️ Frame time ${deltaTime.toFixed(1)}ms critical - system may be frozen`);
      return { skipped: true, reason: 'system-freeze', time: now, frameTime: deltaTime };
    }
    
    // Update FSCTF engine
    this.fsctfEngine.update(this.params, now, this.frameCounter);
    
    // Get current state
    const fsctfState = this.fsctfEngine.getState();
    
    this.frameCounter++;
    
    return {
      skipped: false,
      frameTime: deltaTime,
      avgFrameTime: avgFrameTime,
      fsctfState: fsctfState,
      time: now,
      frame: this.frameCounter
    };
  }
  
  /**
   * Initialize cosmogenesis
   */
  startCosmogenesis() {
    this.fsctfEngine.initializeCosmogenesis();
  }
  
  /**
   * Get shader uniforms for rendering
   */
  getShaderUniforms(time) {
    return this.fsctfEngine.getShaderUniforms(time);
  }
  
  /**
   * Get morphic strands for particle effects
   */
  getMorphicStrands() {
    return this.fsctfEngine.getMorphicStrands();
  }
  
  /**
   * Handle context loss
   */
  onContextLost() {
    this.isContextLost = true;
    console.warn('🚨 WebGL context lost in simulation core');
  }
  
  /**
   * Handle context restoration
   */
  onContextRestored() {
    this.isContextLost = false;
    console.log('✅ WebGL context restored, reinitializing simulation');
    // Reinitialize WebGL resources here
  }
  
  /**
   * Get current FSCTF state
   */
  getFSCTFState() {
    return this.fsctfEngine.getState();
  }
  
  /**
   * Force phase advancement for testing
   */
  forcePhaseAdvancement() {
    this.fsctfEngine.forcePhaseAdvancement();
  }
}
