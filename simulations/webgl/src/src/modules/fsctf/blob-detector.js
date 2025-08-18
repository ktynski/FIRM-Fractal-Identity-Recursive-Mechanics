/**
 * Real-time Blob Detection & Prevention System
 * Monitors rendering output and automatically prevents brightness blowups
 */

export class FSCTFBlobDetector {
  constructor(gl, canvas) {
    this.gl = gl;
    this.canvas = canvas;
    
    // Blob detection thresholds (made less sensitive to reduce false positives)
    this.whitePixelThreshold = 0.98; // RGB values above this are "white" (stricter)
    this.whitePixelRatioThreshold = 0.25; // If >25% of pixels are white, it's a blob (higher threshold) 
    this.consecutiveFramesThreshold = 5; // Trigger after 5 consecutive blob frames (more patience)
    
    // State tracking
    this.consecutiveBlobFrames = 0;
    this.lastFrameWasBlob = false;
    this.emergencyModeActive = false;
    this.emergencyStartTime = 0;
    this.frameSampleBuffer = new Uint8Array(128 * 128 * 4); // Sample 128x128 region
    
    // Performance tracking
    this.checkInterval = 5; // Check every 5 frames for performance
    this.frameCount = 0;
    
    console.log('🔍 FSCTF Blob Detector initialized - real-time brightness monitoring active');
  }

  /**
   * Check if current frame contains white blob
   */
  checkForBlob() {
    this.frameCount++;
    
    // Only check every N frames for performance
    if (this.frameCount % this.checkInterval !== 0) return false;
    
    try {
      // Sample center region of screen (where blobs usually appear)
      const centerX = Math.floor(this.canvas.width / 2) - 64;
      const centerY = Math.floor(this.canvas.height / 2) - 64;
      const sampleWidth = 128;
      const sampleHeight = 128;
      
      // Read pixels from center region
      this.gl.readPixels(
        centerX, centerY, 
        sampleWidth, sampleHeight, 
        this.gl.RGBA, this.gl.UNSIGNED_BYTE, 
        this.frameSampleBuffer
      );
      
      // Count white/bright pixels
      let whitePixelCount = 0;
      const totalPixels = sampleWidth * sampleHeight;
      
      for (let i = 0; i < this.frameSampleBuffer.length; i += 4) {
        const r = this.frameSampleBuffer[i] / 255.0;
        const g = this.frameSampleBuffer[i + 1] / 255.0;
        const b = this.frameSampleBuffer[i + 2] / 255.0;
        
        // Check if pixel is "white" (very bright)
        const brightness = (r + g + b) / 3.0;
        if (brightness > this.whitePixelThreshold) {
          whitePixelCount++;
        }
      }
      
      const whiteRatio = whitePixelCount / totalPixels;
      const isBlob = whiteRatio > this.whitePixelRatioThreshold;
      
      // Track consecutive blob frames
      if (isBlob) {
        this.consecutiveBlobFrames++;
      } else {
        this.consecutiveBlobFrames = 0;
      }
      
      // Log blob detection for debugging
      if (isBlob && this.frameCount % 30 === 0) { // Log every 30 frames when blob detected
        console.warn(`🚨 BLOB DETECTED: ${(whiteRatio * 100).toFixed(1)}% white pixels (threshold: ${(this.whitePixelRatioThreshold * 100).toFixed(1)}%)`);
      }
      
      this.lastFrameWasBlob = isBlob;
      return isBlob;
      
    } catch (error) {
      console.warn('⚠️ Blob detection error:', error);
      return false; // Fail safe
    }
  }

  /**
   * Apply emergency blob prevention measures
   * Respects manual parameter overrides set by user
   */
  applyEmergencyMeasures(params, visualController = null) {
    const currentTime = Date.now();
    
    // COSMIC PHASE PROTECTION: No blob detection interference in stages 4-8
    const cosmogenesisPhase = window.simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
    if (cosmogenesisPhase >= 4) {
      if (this.frameCount % 300 === 0) { // Log every 5 seconds
        console.log('🌌 COSMIC PHASE: Blob detection disabled for emergent hypercube complexity');
      }
      return params; // No interference during cosmic complexity emergence
    }
    
    // Check if we need to trigger emergency mode
    if (this.consecutiveBlobFrames >= this.consecutiveFramesThreshold) {
      if (!this.emergencyModeActive) {
        this.emergencyModeActive = true;
        this.emergencyStartTime = currentTime;
        console.error('🚨 EMERGENCY BLOB PREVENTION ACTIVATED');
        console.error(`🚨 Blob detection: ${this.consecutiveBlobFrames} consecutive frames`);
      }
    }
    
    // Debug blob detection activity
    if (this.emergencyModeActive && this.frameCount % 60 === 0) {
      const emergencyDuration = currentTime - this.emergencyStartTime;
      console.log(`🚨 BLOB EMERGENCY: Duration=${(emergencyDuration/1000).toFixed(1)}s, Level=${emergencyDuration < 2000 ? 1 : emergencyDuration < 5000 ? 2 : 3}`);
    }
    
    // Helper function to check if parameter is manually overridden
    const isManuallySet = (paramName) => {
      return visualController?.isManuallyOverridden?.(paramName) || false;
    };
    
    // Apply progressive emergency measures (FULLY respecting manual overrides)
    if (this.emergencyModeActive) {
      const emergencyDuration = currentTime - this.emergencyStartTime;
      
      // Count how many critical visual params are manually controlled
      const criticalParams = ['brightness', 'pointSize', 'exposure'];
      const manuallyControlled = criticalParams.filter(param => isManuallySet(param));
      
      // If user has manual control over visual quality, provide warning but don't override
      if (manuallyControlled.length > 0) {
        if (this.frameCount % 120 === 0) { // Every 2 seconds
          console.warn(`🎛️ BLOB DETECTED: User has manual control over [${manuallyControlled.join(', ')}] - emergency measures limited`);
          console.warn('   💡 Consider reducing these values manually to prevent blob formation');
        }
      }
      
      if (emergencyDuration < 2000) {
        // Level 1: Moderate reduction (0-2 seconds) - ONLY if not manually controlled
        if (!isManuallySet('brightness')) {
          params.brightness = Math.min(params.brightness, 0.6);
        }
        if (!isManuallySet('pointSize')) {
          params.pointSize = Math.min(params.pointSize, 8.0);
        }
        if (!isManuallySet('exposure')) {
          params.exposure = Math.min(params.exposure, 0.8);
        }
        if (!isManuallySet('wireframeDensity')) {
          params.wireframeDensity = Math.min(params.wireframeDensity, 16);
        }
        
      } else if (emergencyDuration < 5000) {
        // Level 2: Aggressive reduction (2-5 seconds)
        if (!isManuallySet('brightness')) {
          params.brightness = Math.min(params.brightness, 0.4);
        }
        if (!isManuallySet('pointSize')) {
          params.pointSize = Math.min(params.pointSize, 4.0);
        }
        if (!isManuallySet('exposure')) {
          params.exposure = Math.min(params.exposure, 0.6);
        }
        if (!isManuallySet('showWireframe')) {
          params.showWireframe = false;
        }
        // EMERGENT COMPLEXITY: Allow higher complexity in stages 4-8 for hypercube emergence
        if (!isManuallySet('graceComplexity')) {
          const cosmogenesisPhase = window.simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
          const maxAllowedComplexity = (cosmogenesisPhase >= 4) ? 10.0 : 1.0; // Higher for cosmic phases
          params.graceComplexity = Math.min(params.graceComplexity, maxAllowedComplexity);
        }
        
      } else {
        // Level 3: Ultra-conservative mode (>5 seconds)
        if (!isManuallySet('brightness')) {
          params.brightness = 0.3;
        }
        if (!isManuallySet('pointSize')) {
          params.pointSize = 2.0;
        }
        if (!isManuallySet('exposure')) {
          params.exposure = 0.5;
        }
        if (!isManuallySet('showWireframe')) {
          params.showWireframe = false;
        }
        // EMERGENT COMPLEXITY: Allow cosmic complexity in stages 4-8
        if (!isManuallySet('graceComplexity')) {
          const cosmogenesisPhase = window.simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
          params.graceComplexity = (cosmogenesisPhase >= 4) ? 5.0 : 0.5; // Much higher for hypercube phases
        }
        if (!isManuallySet('domain')) {
          params.domain = Math.min(params.domain, 8.0);
        }
      }
      
      // Check if blob is resolved
      if (this.consecutiveBlobFrames === 0 && emergencyDuration > 1000) {
        this.emergencyModeActive = false;
        console.log('✅ Emergency blob prevention successful - normal rendering resumed');
      }
    }
    
    return params;
  }

  /**
   * Get safe shader intensities based on blob detection
   */
  getSafeShaderIntensities(baseIntensities) {
    if (this.emergencyModeActive) {
      // During emergency, drastically reduce all shader intensities
      return {
        coherenceLevel: Math.min(baseIntensities.coherenceLevel, 20),
        strandDensity: Math.min(baseIntensities.strandDensity, 100),
        survivalRating: Math.min(baseIntensities.survivalRating, 30),
        totalShaderIntensity: 1.0, // Very conservative
        maxShaderIntensity: 1.5
      };
    }
    
    // Normal operation - just apply reasonable caps
    return {
      coherenceLevel: Math.min(baseIntensities.coherenceLevel, 50),
      strandDensity: Math.min(baseIntensities.strandDensity, 500),
      survivalRating: Math.min(baseIntensities.survivalRating, 100),
      totalShaderIntensity: Math.min(baseIntensities.totalShaderIntensity || 2.0, 2.5),
      maxShaderIntensity: 3.0
    };
  }

  /**
   * Get diagnostic info for debugging
   */
  getDebugInfo() {
    return {
      consecutiveBlobFrames: this.consecutiveBlobFrames,
      emergencyModeActive: this.emergencyModeActive,
      emergencyDuration: this.emergencyModeActive ? Date.now() - this.emergencyStartTime : 0,
      framesSinceLastCheck: this.frameCount % this.checkInterval,
      lastFrameWasBlob: this.lastFrameWasBlob
    };
  }

  /**
   * Manual reset for testing
   */
  reset() {
    this.consecutiveBlobFrames = 0;
    this.emergencyModeActive = false;
    this.lastFrameWasBlob = false;
    console.log('🔄 Blob detector reset');
  }
}
