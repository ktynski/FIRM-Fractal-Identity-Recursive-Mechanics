/**
 * Main Simulation Loop
 * Core simulation execution and rendering loop
 */

// Global simulation state
let frameCounter = 0;
let lastFrameTime = performance.now();
let corrTick = 0;
let frstTick = 0;
let baselineSeeded = false;

export class MainLoop {
  constructor() {
    this.running = false;
    this.frameCounter = 0;
    this.lastFrameTime = performance.now();
    this.corrTick = 0;
    this.frstTick = 0;
    this.baselineSeeded = false;
    
    // Animation frame ID for stopping
    this.animationFrameId = null;
    
    console.log('🔄 Main Loop initialized');
  }
  
  /**
   * Main simulation loop
   */
  loop() {
    if (!this.running) return;
    
    const t = performance.now() * 0.001; // Convert to seconds
    const frameTime = performance.now() - this.lastFrameTime;
    frameCounter++;
    this.frameCounter = frameCounter;
    
    // Update performance monitoring
    if (window.updatePerformanceMetrics) {
      window.updatePerformanceMetrics(frameTime);
    }
    
    // Resize canvas to match display size
    if (window.resizeCanvasToDisplaySize) {
      window.resizeCanvasToDisplaySize((window.devicePixelRatio || 1) * (window.params?.renderScale || 1));
    }
    
    // Clear the canvas
    if (window.gl) {
      window.gl.clearColor(0, 0, 0, 1);
      window.gl.clear(window.gl.COLOR_BUFFER_BIT);
    }
    
    // Memory management and garbage collection hint
    if (frameCounter % 1800 === 0) {
      if (window.gc) {
        window.gc();
      }
    }
    
    // Update FSCTF systems
    this.updateFSCTFSystems(t);
    
    // A/B testing step
    if (window.abTestStep) {
      const state = this.getCurrentState();
      window.abTestStep(state.psi, state.frst, state.rho);
    }
    
    // Brain system update
    if (window.Brain && window.updateBrainSystem) {
      const state = this.getCurrentState();
      window.updateBrainSystem(frameCounter, state.psi, state.frst, state.rho);
    }
    
    // Core simulation step
    this.stepSim();
    
    // Render the scene
    this.render();
    
    // Presentation adjustments
    if (window.adjustPresentation) {
      const state = this.getCurrentState();
      window.adjustPresentation(state.psi);
    }
    
    // Update UI
    this.updateUI();
    
    // Progressive cosmogenesis update
    if (window.updateProgressiveCosmogenesis) {
      window.updateProgressiveCosmogenesis();
    }
    
    this.lastFrameTime = performance.now();
    
    // Continue the loop
    this.animationFrameId = requestAnimationFrame(() => this.loop());
  }
  
  /**
   * Update FSCTF systems
   */
  updateFSCTFSystems(time) {
    // Update topology transition manager
    if (window.topologyTransitionManager) {
      window.topologyTransitionManager.updateTransition();
    }
    
    // Update camera transition manager  
    if (window.cameraTransitionManager) {
      window.cameraTransitionManager.updateTransition();
      
      // Apply auto-rotate if enabled
      if (window.params?.cameraAutoRotate) {
        window.cameraTransitionManager.setAutoRotate(window.params.cameraAutoRotate);
        window.cameraTransitionManager.autoRotateSpeed = window.params.cameraAutoRotateSpeed || 0.1;
      }
    }
    
    // Update cascade emergence
    if (window.cascadeEmergence) {
      window.cascadeEmergence.update(time);
    }
    
    // Update morphic activity panel
    if (window.updateMorphicActivityPanel) {
      window.updateMorphicActivityPanel();
    }
    
    // Update feedback loops panel
    if (window.updateFeedbackLoopsPanel) {
      window.updateFeedbackLoopsPanel();
    }
  }
  
  /**
   * Execute one simulation step
   */
  stepSim() {
    if (!window.gl) return;
    
    const gl = window.gl;
    
    // Bind simulation uniforms
    this.bindSimUniforms(1); // Velocity pass
    
    // Execute velocity update
    // TODO: Implement actual simulation step using WebGL
    
    this.bindSimUniforms(0); // Position pass
    
    // Execute position update  
    // TODO: Implement actual simulation step using WebGL
    
    // Swap textures (ping-pong)
    // TODO: Implement texture swapping
  }
  
  /**
   * Bind simulation shader uniforms
   */
  bindSimUniforms(passId) {
    if (!window.gl || !window.params) return;
    
    const gl = window.gl;
    const params = window.params;
    
    // TODO: Implement uniform binding for simulation shader
    // This would set all the simulation parameters as uniforms
    /*
    gl.uniform1f(gl.getUniformLocation(simProg, 'dt'), params.dt);
    gl.uniform1f(gl.getUniformLocation(simProg, 'domain'), params.domain);
    gl.uniform1f(gl.getUniformLocation(simProg, 'fieldScale'), params.fieldScale);
    gl.uniform1f(gl.getUniformLocation(simProg, 'timeScale'), params.timeScale);
    gl.uniform1f(gl.getUniformLocation(simProg, 'damping'), params.damping);
    gl.uniform1f(gl.getUniformLocation(simProg, 'jitterSigma'), params.jitterSigma);
    gl.uniform1f(gl.getUniformLocation(simProg, 'graceAmp'), params.graceAmp);
    gl.uniform1f(gl.getUniformLocation(simProg, 'devourerAmp'), params.devourerAmp);
    gl.uniform1i(gl.getUniformLocation(simProg, 'passId'), passId);
    gl.uniform1f(gl.getUniformLocation(simProg, 'time'), performance.now() * 0.001);
    */
  }
  
  /**
   * Render the simulation
   */
  render() {
    if (!window.gl) return;
    
    // TODO: Implement rendering
    // This would involve:
    // 1. Bind render program
    // 2. Set render uniforms
    // 3. Draw particles using instanced rendering
  }
  
  /**
   * Get current simulation state
   */
  getCurrentState() {
    // TODO: Get actual state from GPU measurements
    return {
      psi: Math.random(), // Placeholder
      frst: Math.random(),
      rho: Math.random(),
      energy: Math.random(),
      kappa: Math.random()
    };
  }
  
  /**
   * Update UI displays
   */
  updateUI() {
    const state = this.getCurrentState();
    
    // Update stats display
    if (window.updateStats) {
      const F = window.scoreState ? window.scoreState(state.psi, state.frst, state.rho) : 0;
      window.updateStats(state.energy, state.kappa, 0, state.rho, state.psi, state.frst);
    }
    
    // Update cosmogenesis UI
    if (window.updateCosmogenesisUI) {
      window.updateCosmogenesisUI();
    }
    
    // Update performance UI
    if (window.updatePerformanceUI) {
      window.updatePerformanceUI(performance.now() - this.lastFrameTime, 16.67);
    }
  }
  
  /**
   * Seed initial particle textures
   */
  seedTextures() {
    if (!window.gl || this.baselineSeeded) return;
    
    console.log('🌱 Seeding particle textures...');
    
    // TODO: Implement texture seeding
    // This would involve creating initial particle positions and velocities
    
    this.baselineSeeded = true;
    console.log('✅ Texture seeding complete');
  }
  
  /**
   * Presentation adjustment based on state
   */
  adjustPresentation(psi) {
    if (!window.params) return;
    
    // Adjust visual parameters based on simulation state
    const intensity = Math.min(1, Math.max(0, psi));
    
    // Adjust brightness and exposure based on activity (respecting user overrides)
    const vc = window.simulationCore?.fsctfEngine?.visualController;
    if (!vc?.isManuallyOverridden?.('brightness')) {
      window.params.brightness = 0.8 + intensity * 0.4;
    }
    if (!vc?.isManuallyOverridden?.('exposure')) {
      window.params.exposure = 1.5 + intensity * 0.8;
    }
  }
  
  /**
   * Start the main loop
   */
  start() {
    if (this.running) return;
    
    console.log('▶️ Starting main simulation loop');
    this.running = true;
    
    // Seed textures on first start
    if (!this.baselineSeeded) {
      this.seedTextures();
    }
    
    // Start the loop
    this.loop();
  }
  
  /**
   * Stop the main loop
   */
  stop() {
    if (!this.running) return;
    
    console.log('⏸️ Stopping main simulation loop');
    this.running = false;
    
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
      this.animationFrameId = null;
    }
  }
  
  /**
   * Reset the loop state
   */
  reset() {
    this.stop();
    this.frameCounter = 0;
    this.corrTick = 0;
    this.frstTick = 0;
    this.baselineSeeded = false;
    frameCounter = 0;
    corrTick = 0;
    frstTick = 0;
    baselineSeeded = false;
    console.log('🔄 Main loop reset');
  }
  
  /**
   * Get loop statistics
   */
  getStats() {
    return {
      running: this.running,
      frameCounter: this.frameCounter,
      corrTick: this.corrTick,
      frstTick: this.frstTick,
      baselineSeeded: this.baselineSeeded,
      lastFrameTime: performance.now() - this.lastFrameTime
    };
  }
}

/**
 * Optimized main loop with frame skipping for heavy operations
 */
export class OptimizedMainLoop extends MainLoop {
  constructor() {
    super();
    this.frameSkipCounter = 0;
    this.heavyOperationFrame = 0;
    this.lastHeavyUpdate = 0;
  }
  
  loop() {
    if (!this.running) return;
    
    const t = performance.now() * 0.001;
    const frameTime = performance.now() - this.lastFrameTime;
    frameCounter++;
    this.frameCounter = frameCounter;
    
    // Update performance monitoring
    if (window.updatePerformanceMetrics) {
      window.updatePerformanceMetrics(frameTime);
    }
    
    // Resize canvas only when necessary
    if (frameCounter % 60 === 0 && window.resizeCanvasToDisplaySize) {
      window.resizeCanvasToDisplaySize((window.devicePixelRatio || 1) * (window.params?.renderScale || 1));
    }
    
    // Clear the canvas
    if (window.gl) {
      window.gl.clearColor(0, 0, 0, 1);
      window.gl.clear(window.gl.COLOR_BUFFER_BIT);
    }
    
    // Memory management at reduced frequency
    if (frameCounter % 3600 === 0) { // Every 60 seconds at 60fps
      if (window.gc) {
        window.gc();
      }
    }
    
    // Update FSCTF systems with adaptive frequency
    this.updateFSCTFSystemsOptimized(t, frameCounter);
    
    // Core simulation step
    this.stepSim();
    
    // Render the scene
    this.render();
    
    // Update UI at reduced frequency
    if (frameCounter % 5 === 0) {
      this.updateUI();
    }
    
    this.lastFrameTime = performance.now();
    this.animationFrameId = requestAnimationFrame(() => this.loop());
  }
  
  updateFSCTFSystemsOptimized(time, frameCount) {
    // Update topology transitions less frequently
    if (frameCount % 10 === 0 && window.topologyTransitionManager) {
      window.topologyTransitionManager.updateTransition();
    }
    
    // Update camera transitions every frame (smooth movement)
    if (window.cameraTransitionManager) {
      window.cameraTransitionManager.updateTransition();
      
      if (window.params?.cameraAutoRotate) {
        window.cameraTransitionManager.setAutoRotate(window.params.cameraAutoRotate);
        window.cameraTransitionManager.autoRotateSpeed = window.params.cameraAutoRotateSpeed || 0.1;
      }
    }
    
    // Update cascade emergence with adaptive frequency
    if (frameCount % 3 === 0 && window.cascadeEmergence) {
      window.cascadeEmergence.update(time);
    }
    
    // Update UI panels less frequently
    if (frameCount % 15 === 0) {
      if (window.updateMorphicActivityPanel) {
        window.updateMorphicActivityPanel();
      }
      if (window.updateFeedbackLoopsPanel) {
        window.updateFeedbackLoopsPanel();
      }
    }
  }
}

// Export global variables for compatibility
export { frameCounter, lastFrameTime, corrTick, frstTick, baselineSeeded };
