/**
 * Enhanced Visual Expression System
 * Uses multiple visual dimensions instead of just brightness increases
 * to express mathematical complexity and phase progression
 */

export class FSCTFEnhancedVisualExpression {
  constructor() {
    this.phaseColorPalettes = {
      1: { // Grace emergence - Deep purples and violets
        primary: [0.4, 0.1, 0.8],    // Deep violet
        secondary: [0.6, 0.2, 1.0],  // Bright purple
        accent: [0.8, 0.4, 0.9],     // Light purple
        trail: [0.3, 0.0, 0.6]       // Dark purple trails
      },
      2: { // Morphic emergence - Golden and amber
        primary: [1.0, 0.7, 0.2],    // Rich gold
        secondary: [1.0, 0.8, 0.4],  // Bright gold
        accent: [1.0, 0.9, 0.6],     // Light gold
        trail: [0.8, 0.5, 0.1]       // Dark amber trails
      },
      3: { // Dimensional bridge - Cyan and teal
        primary: [0.2, 0.8, 1.0],    // Bright cyan
        secondary: [0.4, 0.9, 1.0],  // Light cyan
        accent: [0.6, 1.0, 1.0],     // Very light cyan
        trail: [0.1, 0.6, 0.8]       // Dark teal trails
      },
      4: { // Coherence topology - Vibrant green
        primary: [0.2, 1.0, 0.4],    // Bright green
        secondary: [0.4, 1.0, 0.6],  // Light green
        accent: [0.6, 1.0, 0.8],     // Very light green
        trail: [0.1, 0.8, 0.2]       // Dark green trails
      },
      5: { // Soul emergence - Multi-spectral
        primary: [1.0, 0.5, 0.8],    // Rose
        secondary: [0.8, 0.7, 1.0],  // Lavender
        accent: [1.0, 0.8, 0.9],     // Light pink
        trail: [0.6, 0.3, 0.7]       // Dark magenta trails
      },
      6: { // Cosmic inflation - Blue-white
        primary: [0.8, 0.9, 1.0],    // Blue-white
        secondary: [0.9, 0.95, 1.0], // Very light blue
        accent: [1.0, 1.0, 1.0],     // Pure white
        trail: [0.6, 0.7, 0.9]       // Medium blue trails
      },
      7: { // CMB formation - Warm white-gold
        primary: [1.0, 0.95, 0.8],   // Warm white
        secondary: [1.0, 0.9, 0.7],  // Cream
        accent: [1.0, 0.85, 0.6],    // Light gold
        trail: [0.9, 0.8, 0.5]       // Golden trails
      },
      8: { // Observable universe - Full spectrum
        primary: [1.0, 1.0, 1.0],    // Pure white core
        secondary: [0.9, 0.9, 1.0],  // Light blue
        accent: [1.0, 0.9, 0.9],     // Light pink
        trail: [0.8, 0.8, 1.0]       // Light purple trails
      }
    };

    // Alternative expression modes
    this.expressionModes = {
      PARTICLE_DENSITY: 'density',
      SIZE_MODULATION: 'size', 
      COLOR_TEMPERATURE: 'temperature',
      TRAIL_COMPLEXITY: 'trails',
      OPACITY_LAYERS: 'opacity',
      HARMONIC_RESONANCE: 'resonance'
    };

    console.log('🎨 FSCTF Enhanced Visual Expression initialized');
  }

  /**
   * Get sophisticated visual parameters for a given phase
   */
  getPhaseVisualExpression(phase, complexity, frameTime) {
    const palette = this.phaseColorPalettes[phase] || this.phaseColorPalettes[1];
    
    // Calculate complexity-based modulations (UNBOUNDED for stages 4-8)
    const complexityFactor = Math.min(Math.max(complexity / 100.0, 0.0), 10.0); // INCREASED: Allow hypercube-scale complexity
    const timePhase = (Date.now() * 0.001) % (Math.PI * 2);
    
    return {
      // Color expression instead of brightness blowup
      colors: this.calculatePhaseColors(palette, complexityFactor, timePhase),
      
      // Size modulation (bounded, never explosive)
      sizeParams: this.calculateSizeModulation(phase, complexityFactor),
      
      // Particle behavior
      particleParams: this.calculateParticleExpression(phase, complexityFactor),
      
      // Trail and flow effects
      trailParams: this.calculateTrailEffects(phase, complexityFactor, timePhase),
      
      // Opacity and layering
      opacityParams: this.calculateOpacityLayers(phase, complexityFactor),
      
      // Performance-safe brightness (never causes blobs)
      brightnessParams: this.calculateSafeBrightness(phase, complexityFactor, frameTime)
    };
  }

  /**
   * Calculate sophisticated color transitions
   */
  calculatePhaseColors(palette, complexity, timePhase) {
    // Smooth color interpolation based on complexity
    const primaryIntensity = 0.6 + 0.4 * complexity;
    const secondaryIntensity = 0.4 + 0.3 * complexity;
    
    // Harmonic color oscillation
    const harmonicShift = 0.1 * Math.sin(timePhase * 1.618033988749895); // φ-harmonic
    
    return {
      primary: palette.primary.map(c => Math.min(1.0, c * primaryIntensity + harmonicShift)),
      secondary: palette.secondary.map(c => Math.min(1.0, c * secondaryIntensity + harmonicShift * 0.5)),
      accent: palette.accent.map(c => Math.min(1.0, c * (0.8 + 0.2 * complexity))),
      trail: palette.trail.map(c => Math.min(1.0, c * (0.5 + 0.5 * complexity))),
      
      // Color temperature shift
      temperature: 0.5 + 0.5 * complexity,
      
      // Spectral spread for higher phases
      spectralWidth: complexity * 0.3,
      
      // φ-harmonic color cycling
      harmonicPhase: timePhase * 1.618033988749895
    };
  }

  /**
   * Calculate safe size modulation (bounded, no explosive growth)
   */
  calculateSizeModulation(phase, complexity) {
    // Base size progression by phase - mathematically generated for 90 phases
    // Progressive growth: sizes grow logarithmically to prevent excessive scaling
    const getPhaseSize = (p) => {
      if (p <= 12) {
        // Original visual phases: manual control for optimal appearance
        const phaseSizes = [1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 15.0, 18.0, 22.0, 28.0, 35.0, 45.0];
        return phaseSizes[p] || 2.0;
      } else {
        // Extended phases: logarithmic growth to prevent size explosion
        // Formula: base_size * log_scale where log_scale increases slowly
        const visualPhaseMax = 45.0; // Max size from visual phases
        const logScale = 1.0 + Math.log(1.0 + (p - 12) * 0.1) * 0.3; // Slow logarithmic growth
        return Math.min(500.0, visualPhaseMax * logScale); // FIXED: Allow larger structures for higher phases
      }
    };
    const baseSize = getPhaseSize(phase);
    
    // Complexity modulation (UNBOUNDED for cosmic emergence)
    const sizeMultiplier = 0.5 + 1.5 * complexity;
    const finalSize = baseSize * sizeMultiplier; // UNBOUNDED - let cosmic structures scale naturally
    
    return {
      pointSize: finalSize,
      sizeVariation: 0.2 + 0.3 * complexity,    // Size variation between particles
      pulsation: 0.1 + 0.2 * complexity,        // Pulsating size effect
      coreSize: finalSize * 0.7,                // Central core size
      haloSize: finalSize * 1.3                 // Outer halo size
    };
  }

  /**
   * Calculate expressive particle behaviors
   */
  calculateParticleExpression(phase, complexity) {
    return {
      // Particle density (more particles, not bigger/brighter particles)
      densityMultiplier: Math.min(2.0, 1.0 + complexity), // Max 2x density
      
      // Movement characteristics
      flowStrength: Math.min(10.0, 2.0 + complexity * 8.0),
      turbulence: 0.1 + complexity * 0.4,
      coherence: complexity, // How organized the movement is
      
      // Particle lifespan
      persistence: 0.7 + complexity * 0.25,
      
      // Interaction strength
      particleInteraction: complexity * 0.5,
      
      // φ-harmonic resonance strength
      phiResonance: complexity * 1.618033988749895
    };
  }

  /**
   * Calculate sophisticated trail effects
   */
  calculateTrailEffects(phase, complexity, timePhase) {
    return {
      // Trail length (bounded)
      trailLength: Math.min(0.98, 0.8 + complexity * 0.15),
      
      // Trail opacity
      trailOpacity: Math.min(0.9, 0.3 + complexity * 0.6),
      
      // Trail color evolution
      trailColorShift: complexity * 0.2,
      
      // Multiple trail layers
      trailLayers: Math.min(3, 1 + Math.floor(complexity * 2)),
      
      // φ-spiral trail patterns
      spiralStrength: complexity * 0.3,
      spiralPhase: timePhase * 1.618033988749895,
      
      // Trail branching (for complex phases)
      branchingFactor: Math.max(0, complexity - 0.5) * 0.4
    };
  }

  /**
   * Calculate opacity and layering effects
   */
  calculateOpacityLayers(phase, complexity) {
    return {
      // Core opacity (never fully opaque to prevent blobs)
      coreOpacity: Math.min(0.85, 0.4 + complexity * 0.45),
      
      // Layer separation
      layerCount: Math.min(4, 1 + Math.floor(complexity * 3)),
      layerSeparation: 0.1 + complexity * 0.2,
      
      // Depth-based opacity variation
      depthOpacity: 0.3 + complexity * 0.4,
      
      // Edge softness
      edgeSoftness: 0.2 + complexity * 0.3,
      
      // Glow effects (subtle, bounded)
      glowRadius: Math.min(20.0, complexity * 15.0),
      glowIntensity: Math.min(0.3, complexity * 0.25)
    };
  }

  /**
   * Calculate performance-safe brightness (never causes blobs)
   */
  calculateSafeBrightness(phase, complexity, frameTime) {
    // Base brightness by phase - mathematically generated for 90 phases
    const getPhaseBrightness = (p) => {
      if (p <= 12) {
        // Original visual phases: manual control for optimal appearance
        const phaseBrightness = [0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8];
        return phaseBrightness[p] || 0.5;
      } else {
        // Extended phases: gradual brightness progression
        // Formula: oscillating brightness with slow upward trend
        const visualPhaseMax = 1.8; // Max brightness from visual phases
        const oscillation = 0.1 * Math.sin((p - 12) * 0.2); // Small oscillation
        const upwardTrend = (p - 12) * 0.005; // Very slow increase
        return Math.min(2.5, visualPhaseMax + oscillation + upwardTrend); // Cap at 2.5
      }
    };
    const baseBrightness = getPhaseBrightness(phase);
    
    // Complexity enhancement (bounded)
    const complexityBoost = complexity * 0.3; // Max 30% boost
    
    // Performance-based automatic reduction
    const performanceFactor = frameTime > 50 ? 0.7 : (frameTime > 30 ? 0.85 : 1.0);
    
    // Final brightness (COSMIC SCALE - no hard cap for emergent complexity)
    const finalBrightness = (baseBrightness + complexityBoost) * performanceFactor; // UNBOUNDED for cosmic emergence
    
    return {
      brightness: finalBrightness,
      contrast: 0.8 + complexity * 0.15,
      exposure: 0.8 + complexity * 0.7, // UNBOUNDED for cosmic emergence
      gamma: 0.9 + complexity * 0.1,
      
      // Brightness safety limits
      maxBrightness: 1.4,  // Absolute maximum
      emergencyBrightness: 0.4, // Emergency fallback
      
      // Performance scaling
      performanceScale: performanceFactor
    };
  }

  /**
   * Apply enhanced visual expression to window.params
   */
  applyToParams(params, phase, complexity, frameTime) {
    const expression = this.getPhaseVisualExpression(phase, complexity, frameTime);
    
    // Apply safe size parameters
    params.pointSize = expression.sizeParams.pointSize;
    params.sizeVariation = expression.sizeParams.sizeVariation;
    
    // Apply safe brightness parameters  
    params.brightness = expression.brightnessParams.brightness;
    params.exposure = expression.brightnessParams.exposure;
    params.contrast = expression.brightnessParams.contrast;
    
    // Apply trail effects
    params.trailFade = expression.trailParams.trailLength;
    params.trailOpacity = expression.trailParams.trailOpacity;
    
    // Apply particle behavior
    params.flowStrength = expression.particleParams.flowStrength;
    params.particleDensity = expression.particleParams.densityMultiplier;
    
    // Apply opacity settings
    params.coreOpacity = expression.opacityParams.coreOpacity;
    params.glowRadius = expression.opacityParams.glowRadius;
    params.glowIntensity = expression.opacityParams.glowIntensity;
    
    // Store color information for shader use
    params.phaseColors = expression.colors;
    params.visualExpression = expression;
    
    return params;
  }

  /**
   * Get debug information
   */
  getDebugInfo(phase, complexity) {
    const expression = this.getPhaseVisualExpression(phase, complexity, 16.6);
    
    return {
      phase: phase,
      complexity: complexity,
      brightnessValue: expression.brightnessParams.brightness,
      primaryColor: expression.colors.primary,
      sizeValue: expression.sizeParams.pointSize,
      trailLength: expression.trailParams.trailLength,
      layerCount: expression.opacityParams.layerCount,
      performanceScale: expression.brightnessParams.performanceScale
    };
  }
}
