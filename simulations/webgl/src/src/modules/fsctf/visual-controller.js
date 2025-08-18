/**
 * FSCTF Visual Controller
 * Centralized, fail-safe management of all visual parameters
 * Performance-first design with automatic quality scaling
 */

export class FSCTFVisualController {
  constructor() {
    // Manual override tracking
    this.manualOverrides = new Map();
    this.manualModeActive = false;
    this.lastManualChange = 0;
    this.manualOverrideTimeout = 120000; // 2 minutes of automatic control pause after manual change
    this.frameCount = 0; // For debugging throttling
    
    // Parameter change detection
    this.lastParams = {};
    
    // FAIL-SAFE DEFAULTS - Always safe, never blow up
    this.safeDefaults = {
      brightness: 0.8,
      pointSize: 2.0,
      exposure: 1.0,
      wireframeDensity: 16,
      domain: 8.0,
      graceComplexity: 1.0,
      showWireframe: false,
      trailFade: 0.9
    };

    // PERFORMANCE QUALITY LEVELS
    this.qualityLevels = {
      EMERGENCY: { // Frame time > 200ms
        brightness: 0.6,
        pointSize: 1.0,
        exposure: 0.8,
        wireframeDensity: 0,
        domain: 5.0,
        graceComplexity: 0.3,
        showWireframe: false,
        trailFade: 0.85,
        maxShaderIntensity: 1.5
      },
      LOW: { // Frame time > 60ms  
        brightness: 0.8,
        pointSize: 3.0,
        exposure: 1.0,
        wireframeDensity: 16,
        domain: 8.0,
        graceComplexity: 1.0,
        showWireframe: false,
        trailFade: 0.9,
        maxShaderIntensity: 2.0
      },
      MEDIUM: { // Frame time < 60ms - ENHANCED FOR EMERGENT COMPLEXITY
        brightness: 2.0,         // INCREASED: Better base brightness
        pointSize: 25.0,         // INCREASED: Better base particle size
        exposure: 2.5,           // INCREASED: Better base exposure  
        wireframeDensity: 0,
        domain: 50.0,            // INCREASED: Better base domain
        graceComplexity: 15.0,   // INCREASED: Better base complexity
        showWireframe: false,
        trailFade: 0.95,
        maxShaderIntensity: 5.0  // INCREASED: Better base intensity
      },
      HIGH: { // Frame time < 30ms - COSMIC SCALE BASE VALUES
        brightness: 3.0,         // INCREASED: Cosmic base brightness
        pointSize: 50.0,         // INCREASED: Cosmic base particle size  
        exposure: 3.5,           // INCREASED: Cosmic base exposure
        wireframeDensity: 0,
        domain: 100.0,           // INCREASED: Cosmic base domain
        graceComplexity: 25.0,   // INCREASED: Cosmic base complexity
        showWireframe: false,
        trailFade: 0.98,
        maxShaderIntensity: 8.0  // INCREASED: Cosmic base intensity
      }
    };

    // PHASE-SPECIFIC SAFE PARAMETERS - Extended to support dramatic complexity evolution
    this.phaseParams = {
      1: { // Grace emergence
        brightnessMultiplier: 0.7,
        sizeMultiplier: 0.3,
        colorTint: [1.0, 0.8, 0.4], // Warm golden
        complexityFactor: 0.2,
        visualEffects: 0.1
      },
      2: { // Morphic emergence  
        brightnessMultiplier: 1.0,
        sizeMultiplier: 1.0,
        colorTint: [0.4, 1.0, 0.9], // Bright cyan
        complexityFactor: 0.6,
        visualEffects: 0.3
      },
      3: { // Dimensional bridge
        brightnessMultiplier: 1.1,
        sizeMultiplier: 1.5,
        colorTint: [0.6, 1.0, 0.4], // Bright green
        complexityFactor: 0.8,
        visualEffects: 0.5
      },
      4: { // Coherence topology - HYPERCUBE EMERGENCE BEGINS
        brightnessMultiplier: 1.3,
        sizeMultiplier: 2.5,
        colorTint: [1.0, 0.9, 0.8], // Warm white
        complexityFactor: 1.2,
        visualEffects: 0.7 // Enable 4D hypercube projections
      },
      5: { // Soul emergence - TESSERACT STRUCTURES
        brightnessMultiplier: 1.5,
        sizeMultiplier: 3.5,
        colorTint: [1.0, 0.5, 0.8], // Rose/magenta
        complexityFactor: 1.8,
        visualEffects: 0.8 // Advanced hyperdimensional geometry
      },
      6: { // Cosmic inflation - 5D HYPERCUBE NETWORKS
        brightnessMultiplier: 1.8,
        sizeMultiplier: 5.0,
        colorTint: [0.8, 0.9, 1.0], // Blue-white cosmic light
        complexityFactor: 2.5,
        visualEffects: 0.9 // Maximum geometric complexity
      },
      7: { // CMB formation - FRACTAL HYPERCUBE CASCADES
        brightnessMultiplier: 2.2,
        sizeMultiplier: 7.0,
        colorTint: [1.0, 0.95, 0.8], // Warm cosmic background
        complexityFactor: 3.5,
        visualEffects: 1.0 // Full visual effects
      },
      8: { // Observable universe - INFINITE RECURSIVE HYPERCUBES
        brightnessMultiplier: 2.8,
        sizeMultiplier: 10.0,
        colorTint: [1.0, 1.0, 1.0], // Pure white - all wavelengths
        complexityFactor: 5.0,
        visualEffects: 1.0 // Maximum emergent complexity
      },
      
      // EXTENDED HYPERDIMENSIONAL PHASES 9-16 - BEYOND BASIC HYPERCUBES
      9: { // Early universe cooling - HYPERCUBE NETWORKS
        brightnessMultiplier: 3.2,
        sizeMultiplier: 12.0,
        colorTint: [0.9, 0.95, 1.0], // Cooler blue-white
        complexityFactor: 6.0,
        visualEffects: 1.0 // Network structures
      },
      10: { // Primordial nucleosynthesis - FRACTAL HYPERCUBE MATRICES
        brightnessMultiplier: 3.5,
        sizeMultiplier: 15.0,
        colorTint: [1.0, 0.9, 0.9], // Warm nucleosynthesis glow
        complexityFactor: 7.0,
        visualEffects: 1.0 // Matrix formations
      },
      11: { // Recombination era - HYPERCUBE CRYSTALLIZATION
        brightnessMultiplier: 3.8,
        sizeMultiplier: 18.0,
        colorTint: [1.0, 0.8, 0.6], // Golden recombination
        complexityFactor: 8.0,
        visualEffects: 1.0 // Crystalline structures
      },
      12: { // Dark ages - SHADOW HYPERCUBES
        brightnessMultiplier: 2.0,
        sizeMultiplier: 20.0,
        colorTint: [0.3, 0.3, 0.5], // Dark universe
        complexityFactor: 9.0,
        visualEffects: 1.0 // Shadow geometry
      },
      13: { // First stars - STELLAR HYPERCUBE BIRTH
        brightnessMultiplier: 4.5,
        sizeMultiplier: 25.0,
        colorTint: [1.0, 1.0, 0.8], // First starlight
        complexityFactor: 10.0,
        visualEffects: 1.0 // Stellar emergence
      },
      14: { // Galaxy formation - GALACTIC HYPERCUBE SPIRALS
        brightnessMultiplier: 5.0,
        sizeMultiplier: 30.0,
        colorTint: [0.8, 0.9, 1.0], // Galactic spiral arms
        complexityFactor: 12.0,
        visualEffects: 1.0 // Spiral geometries
      },
      15: { // Heavy element formation - METALLIC HYPERCUBE LATTICES
        brightnessMultiplier: 5.5,
        sizeMultiplier: 35.0,
        colorTint: [0.9, 0.8, 0.7], // Metallic elements
        complexityFactor: 15.0,
        visualEffects: 1.0 // Lattice structures
      },
      16: { // Solar system formation - PLANETARY HYPERCUBE SYSTEMS
        brightnessMultiplier: 6.0,
        sizeMultiplier: 40.0,
        colorTint: [1.0, 0.9, 0.8], // Planetary formation
        complexityFactor: 18.0,
        visualEffects: 1.0 // Planetary systems
      }
    };

    // Current state - Start with HIGH quality for maximum emergent complexity
    this.currentQuality = 'HIGH';
    this.currentPhase = 1;
    this.frameTimeHistory = [];
    this.lastFrameTime = 16.6;
    // Smoothed phase to avoid per-phase target jumps
    this.phaseF = 1.0;

    console.log('🎛️ FSCTF Visual Controller initialized - centralized fail-safe design');
    console.log('   Manual override timeout: 2 minutes after user changes');
    this._lastQuality = 'MEDIUM';
  }

  /**
   * Detect if user has manually changed parameters
   */
  detectManualChanges() {
    if (!window.params) return;
    
    const currentTime = Date.now();
    const monitoredParams = ['brightness', 'pointSize', 'exposure', 'wireframeDensity', 'domain', 'graceComplexity', 'showWireframe', 'trailFade'];
    
    let changesDetected = false;
    
    for (const param of monitoredParams) {
      const currentValue = window.params[param];
      const lastValue = this.lastParams[param];
      
      // Detect significant changes (handle both numbers and booleans)
      let changeDetected = false;
      
      if (typeof currentValue === 'boolean') {
        // Boolean parameters (like showWireframe)
        changeDetected = lastValue !== undefined && currentValue !== lastValue;
      } else if (typeof currentValue === 'number') {
        // Numeric parameters - detect significant changes (not just floating point precision)
        changeDetected = lastValue !== undefined && Math.abs(currentValue - lastValue) > 0.01;
      }
      
      if (changeDetected) {
        // Mark this parameter as manually overridden
        this.manualOverrides.set(param, {
          value: currentValue,
          timestamp: currentTime,
          source: 'user'
        });
        
        changesDetected = true;
        
        // Format output based on parameter type
        if (typeof currentValue === 'boolean') {
          console.log(`🎛️ Manual override detected: ${param} = ${currentValue} (was ${lastValue})`);
        } else {
          console.log(`🎛️ Manual override detected: ${param} = ${currentValue.toFixed(3)} (was ${lastValue.toFixed(3)})`);
        }
      }
      
      this.lastParams[param] = currentValue;
    }
    
    if (changesDetected) {
      this.lastManualChange = currentTime;
      console.log('🎛️ Manual control active - automatic adjustments paused for 2 minutes');
    }
  }

  /**
   * Check if a parameter is currently under manual override
   */
  isManuallyOverridden(param) {
    const override = this.manualOverrides.get(param);
    if (!override) {
      // Debug: Reduced logging now that path is fixed
      if (param === 'pointSize' && this.frameCount % 300 === 0) {
        console.log(`🔍 No manual override for ${param} (${this.manualOverrides.size} total overrides)`);
      }
      return false;
    }
    
    const currentTime = Date.now();
    const timeoutExpired = (currentTime - override.timestamp) > this.manualOverrideTimeout;
    
    if (timeoutExpired) {
      this.manualOverrides.delete(param);
      console.log(`🎛️ Manual override for ${param} expired - resuming automatic control`);
      return false;
    }
    
    // Debug: Show active overrides
    if (param === 'pointSize' && this.frameCount % 120 === 0) {
      const age = (currentTime - override.timestamp) / 1000;
      console.log(`✅ Active manual override for ${param}: value=${override.value}, age=${age.toFixed(1)}s`);
    }
    
    return true;
  }

  /**
   * Toggle manual mode on/off
   */
  toggleManualMode() {
    this.manualModeActive = !this.manualModeActive;
    
    if (this.manualModeActive) {
      console.log('🎛️ MANUAL MODE: All automatic parameter adjustments disabled');
    } else {
      this.manualOverrides.clear();
      console.log('🎛️ AUTOMATIC MODE: Resuming performance-based parameter management');
    }
    
    return this.manualModeActive;
  }

  /**
   * Main update - called every frame to determine optimal visual settings
   */
  update(frameTime, cosmogenesisPhase) {
    this.frameCount++;
    
    // Manual detection disabled - UI sliders call markAsUserOverride explicitly
    // Auto-detection caused false positives during system parameter changes
    
    // If in full manual mode, don't apply any automatic changes
    if (this.manualModeActive) {
      return null; // Signal to skip automatic application
    }
    
    this.lastFrameTime = frameTime;
    this.currentPhase = Math.max(1, Math.min(90, cosmogenesisPhase || 1)); // COMPLETE: Up to phase 90
    // SMOOTH: Much slower phase blending for graceful transitions
    this.phaseF += (this.currentPhase - this.phaseF) * 0.08; // REDUCED: Slower blending for smoother changes
    this.phaseF = Math.max(1.0, Math.min(90.0, this.phaseF)); // COMPLETE: Up to phase 90
    
    // EMERGENT COMPLEXITY MONITORING - Track cosmic phases and beyond
    if (this.currentPhase >= 4 && this.currentPhase <= 16 && frameTime % 2000 < 16) { // Log every ~2 seconds
      const phaseNames = {
        4: 'HYPERCUBE EMERGENCE', 5: 'TESSERACT STRUCTURES', 6: '5D HYPERCUBE NETWORKS', 
        7: 'FRACTAL HYPERCUBE CASCADES', 8: 'INFINITE RECURSIVE HYPERCUBES',
        9: 'HYPERCUBE NETWORKS', 10: 'FRACTAL HYPERCUBE MATRICES', 11: 'HYPERCUBE CRYSTALLIZATION',
        12: 'SHADOW HYPERCUBES', 13: 'STELLAR HYPERCUBE BIRTH', 14: 'GALACTIC HYPERCUBE SPIRALS',
        15: 'METALLIC HYPERCUBE LATTICES', 16: 'PLANETARY HYPERCUBE SYSTEMS'
      };
      console.log(`🌌 ADVANCED COMPLEXITY TRACKER: Phase ${this.currentPhase} - ${phaseNames[this.currentPhase] || 'UNKNOWN'}`);
      console.log(`   Blended phase: ${this.phaseF.toFixed(2)} → visualEffects: ${this.phaseParams[this.currentPhase]?.visualEffects || 'undefined'}`);
      console.log(`   Size: ${this.phaseParams[this.currentPhase]?.sizeMultiplier || 'undefined'}x, Complexity: ${this.phaseParams[this.currentPhase]?.complexityFactor || 'undefined'}x`);
    }
    
    // Track frame time history for stability
    this.frameTimeHistory.push(frameTime);
    if (this.frameTimeHistory.length > 10) {
      this.frameTimeHistory.shift();
    }
    
    // Determine quality level based on recent performance
    const avgFrameTime = this.frameTimeHistory.reduce((a, b) => a + b, 0) / this.frameTimeHistory.length;
    this.currentQuality = this.determineQualityLevel(avgFrameTime);
    
    // Calculate safe parameters (respecting manual overrides)
    return this.calculateSafeParameters();
  }

  /**
   * Determine quality level based on performance
   */
  determineQualityLevel(avgFrameTime) {
    // Hysteresis to avoid flapping and target jumps
    const q = this._lastQuality || 'MEDIUM';
    let next = q;
    switch(q){
      case 'HIGH':
        if (avgFrameTime > 35) next = 'MEDIUM';
        break;
      case 'MEDIUM':
        if (avgFrameTime < 25) next = 'HIGH';
        else if (avgFrameTime > 70) next = 'LOW';
        break;
      case 'LOW':
        if (avgFrameTime < 50) next = 'MEDIUM';
        else if (avgFrameTime > 220) next = 'EMERGENCY';
        break;
      case 'EMERGENCY':
        if (avgFrameTime < 180) next = 'LOW';
        break;
    }
    this._lastQuality = next;
    return next;
  }

  /**
   * Calculate safe parameters that can never blow up
   */
  calculateSafeParameters() {
    const quality = this.qualityLevels[this.currentQuality];
    // Blend phase multipliers between floor(phaseF) and ceil(phaseF)
    const pf = this.phaseF;
    const p0 = Math.floor(pf);
    const p1 = Math.min(90, p0 + 1); // FIXED: Allow full 90-phase visual progression
    const pt = pf - p0;
    const d0 = this.phaseParams[p0] || this.phaseParams[1];
    const d1 = this.phaseParams[p1] || d0;
    const phaseBrightness = (d0.brightnessMultiplier || 1.0) * (1.0 - pt) + (d1.brightnessMultiplier || 1.0) * pt;
    const phaseSize = (d0.sizeMultiplier || 1.0) * (1.0 - pt) + (d1.sizeMultiplier || 1.0) * pt;
    const c0 = d0.colorTint || [1,1,1];
    const c1 = d1.colorTint || c0;
    const phaseColorTint = [
      c0[0]*(1-pt)+c1[0]*pt,
      c0[1]*(1-pt)+c1[1]*pt,
      c0[2]*(1-pt)+c1[2]*pt
    ];
    const phaseComplexity = (d0.complexityFactor || 1.0) * (1.0 - pt) + (d1.complexityFactor || 1.0) * pt;
    const phaseVisualEffects = (d0.visualEffects || 0.1) * (1.0 - pt) + (d1.visualEffects || 0.1) * pt;

    // MAXIMUM EMERGENT COMPLEXITY - No pre-calculation limits for cosmic scales
    const baseBrightness = quality.brightness;
    const emergentBrightness = baseBrightness * phaseBrightness; // UNBOUNDED: Let safety clamps handle final limits

    const baseSize = quality.pointSize;
    const emergentSize = baseSize * phaseSize; // UNBOUNDED: Let safety clamps handle final limits

    const safeParams = {
      // Core visual parameters - MAXIMUM EMERGENT COMPLEXITY
      brightness: emergentBrightness,
      pointSize: emergentSize,
      exposure: quality.exposure * phaseBrightness, // UNBOUNDED: Cosmic-scale exposure
      
      // Complexity parameters - FULLY UNBOUNDED FOR STAGES 4-8
      wireframeDensity: 0,
      domain: quality.domain * phaseComplexity, // UNBOUNDED: Universe-scale domains
      graceComplexity: quality.graceComplexity * phaseComplexity, // UNBOUNDED: Pure mathematical derivation
      complexityFactor: phaseComplexity, // Track complexity multiplier for diagnostics
      showWireframe: false,
      trailFade: quality.trailFade,
      
      // Shader parameters - MAXIMUM HYPERCUBE SUPPORT  
      maxShaderIntensity: quality.maxShaderIntensity * phaseComplexity, // UNBOUNDED: Cosmic intensity
      visualEffects: phaseVisualEffects, // Enable 4D/5D projections in stages 4-8
      colorTint: phaseColorTint,
      
      // Quality metadata
      qualityLevel: this.currentQuality,
      phase: this.currentPhase,
      avgFrameTime: this.frameTimeHistory.reduce((a, b) => a + b, 0) / this.frameTimeHistory.length
    };

    // FINAL SAFETY CHECK - Ensure nothing can blow up
    return this.applySafetyClamps(safeParams);
  }

  /**
   * Apply safety clamps - COSMIC SCALE for maximum emergent complexity
   */
  applySafetyClamps(params) {
    return {
      brightness: Math.max(0.1, Math.min(50.0, params.brightness)), // COSMIC: Ultra-high brightness
      pointSize: Math.max(1.0, Math.min(2000.0, params.pointSize)), // COSMIC: Massive hypercube structures  
      exposure: Math.max(0.5, Math.min(25.0, params.exposure)), // COSMIC: Cosmic-scale exposure
      wireframeDensity: Math.max(0, Math.min(64, params.wireframeDensity)),
      domain: Math.max(3.0, Math.min(1000.0, params.domain)), // COSMIC: Universe-scale domains
      graceComplexity: Math.max(0.1, params.graceComplexity), // UNBOUNDED: No artificial ceiling
      showWireframe: params.showWireframe && params.wireframeDensity > 0,
      trailFade: Math.max(0.8, Math.min(0.999, params.trailFade)),
      maxShaderIntensity: Math.max(1.0, Math.min(50.0, params.maxShaderIntensity)), // COSMIC: Massive intensity
      visualEffects: Math.max(0.0, Math.min(1.0, params.visualEffects)), // NEW: Enable hypercube projections
      colorTint: params.colorTint,
      qualityLevel: params.qualityLevel,
      phase: params.phase,
      avgFrameTime: params.avgFrameTime
    };
  }

  /**
   * Get safe shader uniforms - bounded values only
   */
  getSafeShaderUniforms(coherenceLevel, strandDensity, survivalRating) {
    const quality = this.qualityLevels[this.currentQuality];
    
    // BOUNDED ADDITIVE CALCULATIONS - No multiplication chains
    // CRITICAL FIX: Remove false ceilings that restrict emergent complexity
    const safeCoherence = Math.min(500, Math.max(0, coherenceLevel || 0)); // Allow higher coherence
    const safeStrandDensity = Math.min(10000, Math.max(0, strandDensity || 0)); // Allow higher strand density
    const safeSurvival = Math.min(1000, Math.max(0, survivalRating || 0)); // Allow higher soul survival
    
    // ADDITIVE INTENSITY - No exponential blowup possible
    const coherenceContribution = safeCoherence / 100.0; // 0-0.5
    const strandContribution = safeStrandDensity / 2000.0; // 0-0.5  
    const survivalContribution = safeSurvival / 200.0; // 0-0.5
    
    // Anti-blob: soften intensity growth and add micro-dither to break sync
    let totalIntensity = 0.5 + coherenceContribution + strandContribution + survivalContribution;
    
    // CRITICAL: NaN PROTECTION - Validate before Math.sqrt to prevent NaN cascades
    const safeTotalIntensity = Math.max(0.0, Math.min(100.0, totalIntensity || 0.5));
    const sqrtTerm = Math.sqrt(safeTotalIntensity);
    const safeSqrtTerm = (isFinite(sqrtTerm) && !isNaN(sqrtTerm)) ? sqrtTerm : 0.7; // φ^-1 fallback
    
    totalIntensity = safeTotalIntensity * 0.9 + 0.1 * safeSqrtTerm; // compress growth
    
    // Mild blue-noise-like perturbation (deterministic per-frame via Date.now bucket)
    const tBucket = Math.floor(Date.now() / 33) % 1024;
    const sinValue = Math.sin(tBucket * 12.9898);
    const safeSinValue = (isFinite(sinValue) && !isNaN(sinValue)) ? sinValue : 0.0;
    const dither = ((safeSinValue * 78.233) % 1.0) * 0.02 - 0.01;
    
    totalIntensity = Math.min(quality.maxShaderIntensity, Math.max(0.0, totalIntensity + dither));
    
    return {
      coherenceLevel: safeCoherence,
      strandDensity: safeStrandDensity,
      survivalRating: safeSurvival,
      totalShaderIntensity: totalIntensity,
      maxIntensity: quality.maxShaderIntensity
    };
  }

  /**
   * Emergency fallback - instant safe mode
   */
  emergencyFallback() {
    console.warn('🚨 VISUAL CONTROLLER: Emergency fallback activated');
    this.currentQuality = 'EMERGENCY';
    return this.calculateSafeParameters();
  }

  /**
   * Apply parameters to window.params safely (respecting manual overrides)
   */
  applyToParams(params) {
    if (!window.params || !params) return;
    
    const safeParams = params;
    
    // Apply with logging for debugging, but respect manual overrides
    const changes = [];
    const skipped = [];
    
    // Only apply automatic changes to parameters not manually overridden
    // NOTE: brightness is now handled in stickyParams loop to prevent duplicate handling
    
    // ALL visual parameter processing moved to unified stickyParams loop below
    // (No individual parameter handling to prevent conflicts)
    
    // wireframeDensity: Non-visual parameter (not in UI sliders)
    if (!this.isManuallyOverridden('wireframeDensity')) {
      window.params.wireframeDensity = safeParams.wireframeDensity;
    } else {
      skipped.push('wireframeDensity');
    }
    
    // REMOVED: domain and graceComplexity now handled exclusively in stickyParams loop below

    // UNIFIED parameter handling: Respect ALL UI "visual quality" sliders as persistent overrides
    const stickyParams = ['colorMix', 'edgeBoost', 'vignetteStrength', 'trailFade', 'brightness', 'pointSize', 'exposure', 'domain', 'graceComplexity'];
    stickyParams.forEach(name => {
      const isOverridden = this.isManuallyOverridden(name);
      
      // Debug: Show override status for pointSize
      if (name === 'pointSize' && this.frameCount % 60 === 0) {
        console.log(`🔍 pointSize override check: ${isOverridden}, overrides: ${this.manualOverrides.size}`);
        if (this.manualOverrides.has('pointSize')) {
          const override = this.manualOverrides.get('pointSize');
          console.log(`   Override found: value=${override.value}, age=${Date.now() - override.timestamp}ms`);
        }
      }
      
      if (isOverridden) {
      const pinned = this.manualOverrides.get(name);
      if (pinned) {
          // Use exact user value - no smoothing or modification
          if (Math.abs(window.params[name] - pinned.value) > 0.001) {
        window.params[name] = pinned.value;
            changes.push(`${name}: restored user value ${pinned.value.toFixed(2)}`);
          }
          skipped.push(`${name} (user controlled)`);
        }
      } else if (safeParams[name] !== undefined) {
        // Apply automatic parameter if not manually overridden
        const current = window.params[name];
        const target = safeParams[name];
        if (Math.abs(current - target) > 0.01) {
          // SMOOTH: Much slower transitions for visual parameters  
          const smoothed = current + (target - current) * 0.03; // REDUCED: Slower smoothing for graceful changes
          window.params[name] = smoothed;
          changes.push(`${name}: ${current.toFixed(2)} → ${smoothed.toFixed(2)} (auto)`);
        }
      }
    });

    // HYPERCUBE SUPPORT: Apply visual effects parameter for stages 4-8
    if (safeParams.visualEffects !== undefined) {
      window.params.visualEffects = safeParams.visualEffects;
      if (safeParams.visualEffects >= 0.7) {
        changes.push(`visualEffects: ${safeParams.visualEffects.toFixed(2)} (HYPERCUBE ACTIVE)`);
        // EMERGENT COMPLEXITY DIAGNOSTIC - Track when advanced structures should be visible
        if (this.currentPhase >= 4 && this.currentPhase <= 16) {
          const structureTypes = {
            4: '4D HYPERCUBES', 5: 'TESSERACT STRUCTURES', 6: '5D HYPERCUBE NETWORKS', 
            7: 'FRACTAL CASCADES', 8: 'INFINITE RECURSIVE HYPERCUBES',
            9: 'HYPERCUBE NETWORKS', 10: 'FRACTAL MATRICES', 11: 'CRYSTALLINE STRUCTURES',
            12: 'SHADOW GEOMETRY', 13: 'STELLAR EMERGENCE', 14: 'GALACTIC SPIRALS',
            15: 'METALLIC LATTICES', 16: 'PLANETARY SYSTEMS'
          };
          console.log(`🚀 ADVANCED STRUCTURE ACTIVE - Phase ${this.currentPhase}: ${structureTypes[this.currentPhase]}`);
          console.log(`   ✅ visualEffects: ${safeParams.visualEffects.toFixed(3)} (threshold: 0.7)`);
          console.log(`   ✅ complexityFactor: ${safeParams.complexityFactor || 'undefined'}x`);
          console.log(`   🔮 Shader should be rendering advanced geometry NOW!`);
        }
      } else if (this.currentPhase >= 4 && this.currentPhase <= 16) {
        console.warn(`⚠️ ADVANCED STRUCTURE ISSUE - Phase ${this.currentPhase} but visualEffects only ${safeParams.visualEffects.toFixed(3)} (need > 0.7)`);
      }
    }
    
    if (!this.isManuallyOverridden('showWireframe')) {
      window.params.showWireframe = safeParams.showWireframe;
    } else {
      skipped.push('showWireframe');
    }
    
    // trailFade is now handled in the stickyParams loop above - removing duplicate handling
    
    // Log changes and manual overrides for debugging
    if (changes.length > 0) {
      console.log(`🎛️ Visual Controller (${safeParams.qualityLevel}): ${changes.join(', ')}`);
    }
    
    if (skipped.length > 0) {
      console.log(`🎛️ Manual overrides active: ${skipped.join(', ')}`);
    }
    
    return safeParams;
  }
}
