/**
 * Camera Transition and Enhancement System
 * Manages camera transitions, auto-rotation, and dynamic tracking
 */

export class CameraTransitionManager {
  constructor() {
    this.isTransitioning = false;
    this.transitionStartTime = 0;
    this.transitionDuration = 4.0; // SMOOTH: Longer camera transitions for graceful movement
    this.fromSettings = {};
    this.toSettings = {};
    this.transitionProgress = 0.0;
    
    // Auto-rotation for dynamic viewing
    this.autoRotateEnabled = false;
    this.autoRotateSpeed = 0.2; // rad/sec
    this.autoRotatePhase = 0;
    
    // Dynamic camera tracking (disabled by default to prevent zoom interference)
    this.trackingEnabled = false;
    this.trackingIntensity = 0.3; // How much to adjust based on complexity
    
    console.log('📸 Camera Transition Manager initialized');
  }
  
  startTransition(fromTopology, toTopology, duration = 4.0) { // SMOOTH: Default longer camera transitions
    if (fromTopology === toTopology) return;
    
    this.isTransitioning = true;
    this.transitionStartTime = performance.now();
    this.transitionDuration = duration;
    this.transitionProgress = 0.0;
    
    // Store current camera settings as 'from'
    this.fromSettings = {
      cameraX: window.params?.cameraX || 0,
      cameraY: window.params?.cameraY || 0,
      cameraZ: window.params?.cameraZ || 8,
      cameraRotX: window.params?.cameraRotX || 0.6,
      cameraRotY: window.params?.cameraRotY || 0.3,
      fov: window.params?.fov || 45
    };
    
    // Get optimal settings for target topology
    this.toSettings = this.getOptimalCameraSettings(toTopology);
    
    console.log(`📸 Camera Transition: ${fromTopology} → ${toTopology} (${duration}s)`);
  }
  
  updateTransition(params) {
    if (!this.isTransitioning) {
      // Handle auto-rotation when not transitioning
      if (this.autoRotateEnabled) {
        this.autoRotatePhase += this.autoRotateSpeed * (1/60); // Assume 60fps
        params.cameraRotY += Math.sin(this.autoRotatePhase) * 0.01;
        params.cameraRotX += Math.cos(this.autoRotatePhase * 0.7) * 0.005;
      }
      
      // Handle dynamic tracking based on complexity
      if (this.trackingEnabled && window.graceOperator) {
        this.updateDynamicTracking(params);
      }
      
      return false;
    }
    
    const elapsed = (performance.now() - this.transitionStartTime) / 1000.0;
    this.transitionProgress = Math.min(elapsed / this.transitionDuration, 1.0);
    
    // Smooth easing function (ease-in-out cubic)
    const t = this.easeInOutCubic(this.transitionProgress);
    
    // Interpolate camera parameters
    params.cameraX = this.lerp(this.fromSettings.cameraX, this.toSettings.cameraX, t);
    params.cameraY = this.lerp(this.fromSettings.cameraY, this.toSettings.cameraY, t);
    params.cameraZ = this.lerp(this.fromSettings.cameraZ, this.toSettings.cameraZ, t);
    params.cameraRotX = this.lerp(this.fromSettings.cameraRotX, this.toSettings.cameraRotX, t);
    params.cameraRotY = this.lerp(this.fromSettings.cameraRotY, this.toSettings.cameraRotY, t);
    params.fov = this.lerp(this.fromSettings.fov, this.toSettings.fov, t);
    
    if (this.transitionProgress >= 1.0) {
      this.isTransitioning = false;
      console.log(`✅ Camera Transition Complete`);
      return false;
    }
    
    return true;
  }
  
  updateDynamicTracking(params) {
    // Adjust camera based on morphic field complexity and strand count
    const morphicField = window.graceOperator?.morphicField?.field || 0;
    const strandCount = window.graceOperator?.morphicStrands?.length || 0;
    
    // Dynamic distance adjustment based on complexity
    const complexityFactor = morphicField * 0.1 + strandCount * 0.05;
    const baseCameraZ = this.getCurrentOptimalSettings().cameraZ;
    const targetZ = baseCameraZ * (1.0 + complexityFactor * this.trackingIntensity);
    
    // Smooth camera distance adjustment
    params.cameraZ = this.lerp(params.cameraZ, targetZ, 0.02);
    
    // Subtle rotation based on field dynamics
    if (morphicField > 1.0) {
      const rotationInfluence = Math.sin(performance.now() * 0.001) * morphicField * 0.01;
      params.cameraRotY += rotationInfluence * this.trackingIntensity;
    }
  }
  
  getOptimalCameraSettings(topologyMode) {
    const optimalSettings = {
      'torus': { 
        cameraX: 0.0, cameraY: 0.0, cameraZ: 15.0, 
        cameraRotX: 0.618, cameraRotY: 0.314, fov: 45.0,
        description: 'φ-optimal viewing for stable recursion patterns'
      },
      'mobius': { 
        cameraX: 1.0, cameraY: 0.5, cameraZ: 13.0,
        cameraRotX: 0.785, cameraRotY: 0.2, fov: 55.0,
        description: 'Edge-on view to see identity inversion clearly' 
      },
      'klein': { 
        cameraX: 0.5, cameraY: 1.0, cameraZ: 17.0,
        cameraRotX: 0.524, cameraRotY: 0.785, fov: 52.0,
        description: 'Angled view for Grace-wrapped self-intersections'
      },
      'phi-klein': { 
        cameraX: 0.0, cameraY: 0.0, cameraZ: 20.0,
        cameraRotX: 0.618, cameraRotY: 1.618, fov: 65.0,
        description: 'φ-recursive viewpoint for soul-space fractals'
      }
    };
    
    return optimalSettings[topologyMode] || optimalSettings['torus'];
  }
  
  getCurrentOptimalSettings() {
    return this.getOptimalCameraSettings(window.params?.topologyMode || 'torus');
  }
  
  easeInOutCubic(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }
  
  lerp(a, b, t) {
    return a + (b - a) * t;
  }
  
  // Enable/disable features
  setAutoRotate(enabled) {
    this.autoRotateEnabled = enabled;
    console.log(`📸 Auto-rotate ${enabled ? 'enabled' : 'disabled'}`);
  }
  
  setDynamicTracking(enabled) {
    this.trackingEnabled = enabled;
    console.log(`📸 Dynamic tracking ${enabled ? 'enabled' : 'disabled'}`);
  }
  
  // Manual camera presets for different viewing modes
  setPreset(presetName) {
    const presets = {
      'overview': { cameraX: 0, cameraY: 0, cameraZ: 15, cameraRotX: 0.3, cameraRotY: 0.5, fov: 60 },
      'detail': { cameraX: 0, cameraY: 0, cameraZ: 5, cameraRotX: 0.1, cameraRotY: 0.1, fov: 40 },
      'wireframe': { cameraX: 2, cameraY: 2, cameraZ: 10, cameraRotX: 0.6, cameraRotY: 0.8, fov: 50 },
      'transition': { cameraX: 0, cameraY: 3, cameraZ: 12, cameraRotX: 0.4, cameraRotY: 0.6, fov: 55 }
    };
    
    const preset = presets[presetName];
    if (preset) {
      Object.assign(window.params, preset);
      console.log(`📸 Camera preset: ${presetName}`);
    }
  }
  
  getState() {
    return {
      isTransitioning: this.isTransitioning,
      progress: this.transitionProgress,
      autoRotateEnabled: this.autoRotateEnabled,
      trackingEnabled: this.trackingEnabled,
      currentSettings: this.getCurrentOptimalSettings()
    };
  }
}
