/**
 * System Constants
 * Core configuration constants used throughout the system
 */

// === Simulation Parameters ===
export const SIMULATION = {
  SIDE: 1024,           // Texture side length (power of 2)
  get COLS() { return this.SIDE; },
  get ROWS() { return this.SIDE; },
  get NUM() { return this.COLS * this.ROWS; }, // Total particles: 1,048,576
};

// === Performance Constants ===
export const PERFORMANCE = {
  SAMPLE_W: 24,         // Readback width (reduced for performance)
  SAMPLE_H: 24,         // Readback height (reduced for performance)  
  TRACK: 64,            // Number of tracked particles (reduced for perf)
  TARGET_FPS: 60,       // Target frame rate
  FRAME_TIME_BUDGET: 16.67, // Frame time budget in ms (1000/60)
};

// === Memory Management ===
export const MEMORY_LIMITS = {
  MAX_STRANDS: 100,                   // Cap total strands to prevent memory explosion
  MAX_STRANDS_PER_FRAME: 10,          // Limit new strands per frame
  CLEANUP_INTERVAL: 300,              // Cleanup every 300 frames
  MAX_COMPLEXITY: 200.0,              // Maximum allowed complexity before throttling
  MEMORY_WARNING_THRESHOLD: 1000,     // Warn if arrays get too large
  PERFORMANCE_MODE: true              // Enable performance optimizations
};

// === Mathematical Constants ===
export const MATH = {
  PHI: (() => {
    // CRITICAL: NaN PROTECTION - Validate φ calculation 
    const sqrt5 = Math.sqrt(5);
    if (isNaN(sqrt5) || !isFinite(sqrt5)) {
      console.warn('🚨 Math.sqrt(5) produced NaN/Infinity, using fallback φ = 1.618033988749895');
      return 1.618033988749895;
    }
    const phi = (1 + sqrt5) / 2;
    if (isNaN(phi) || !isFinite(phi)) {
      console.warn('🚨 φ calculation produced NaN/Infinity, using fallback φ = 1.618033988749895');
      return 1.618033988749895;
    }
    return phi;
  })(),
  get PHI_INV() { 
    const inv = 1 / this.PHI;
    return (isNaN(inv) || !isFinite(inv)) ? 0.618033988749895 : inv;
  },
  get PHI_2() { 
    const phi2 = this.PHI * this.PHI;
    return (isNaN(phi2) || !isFinite(phi2)) ? 2.618033988749895 : phi2;
  },
  get PHI_3() { return this.PHI_2 * this.PHI; }, // φ³
  get PHI_4() { return this.PHI_2 * this.PHI_2; }, // φ⁴
  
  PI: Math.PI,
  TAU: 2 * Math.PI,
  E: Math.E,
  
  // Common mathematical functions
  SQRT2: Math.SQRT2,
  SQRT1_2: Math.SQRT1_2,
  LN2: Math.LN2,
  LN10: Math.LN10,
};

// === WebGL Constants ===
export const WEBGL = {
  FLOAT_TEXTURE_TYPE: 'RGBA32F',      // Float texture format
  DEPTH_BITS: 24,                     // Depth buffer bits  
  STENCIL_BITS: 8,                    // Stencil buffer bits
  ANTIALIAS: true,                    // ENABLE for finest detail rendering
  PREMULTIPLIED_ALPHA: false,         // Better color precision
  PRESERVE_DRAWING_BUFFER: false,     // Performance optimization
  POWER_PREFERENCE: 'high-performance', // Request discrete GPU
};

// === Physics Constants (for FSCTF calculations) ===
export const PHYSICS = {
  // Fundamental constants (experimental values)
  FINE_STRUCTURE_ALPHA_INV: 137.036,  // Fine structure constant inverse
  WEINBERG_ANGLE_SIN2: 0.2312,        // Weinberg angle sin²(θ_W)
  STRONG_COUPLING: 0.1181,             // Strong coupling constant α_s
  HIGGS_VEV: 246.22,                   // Higgs vacuum expectation value (GeV)
  W_BOSON_MASS: 80.4,                  // W boson mass (GeV)
  
  // Derived φ-topological scaling
  get PHI_SCALE_1() { return Math.pow(MATH.PHI, -1); },
  get PHI_SCALE_2() { return Math.pow(MATH.PHI, -2); },
  get PHI_SCALE_3() { return Math.pow(MATH.PHI, -3); },
  get PHI_SCALE_4() { return Math.pow(MATH.PHI, -4); },
};

// === UI Constants ===
export const UI = {
  PANEL_WIDTH: 320,                   // UI panel width in pixels
  CONTROL_HEIGHT: 24,                 // Height of UI controls
  FONT_SIZE: 10,                      // Base font size
  ANIMATION_DURATION: 200,            // UI animation duration (ms)
  
  COLORS: {
    BACKGROUND: 'rgba(0, 20, 40, 0.9)',
    BORDER: '#456',
    TEXT: '#ccc',
    ACCENT: '#9cf',
    SUCCESS: '#6f6',
    WARNING: '#fc6',
    ERROR: '#f84',
  }
};

// === Cosmogenesis Phase Constants ===
export const COSMOGENESIS = {
  PHASES: [
    'Ex Nihilo', 'Grace Operator', 'Morphic Recursion', 'Dimensional Bridge',
    'Standard Model', 'Consciousness', 'Cosmic Inflation', 'CMB Formation'
  ],
  
  PHASE_COLORS: [
    [0, 0, 0],          // Void - black
    [0.2, 0.1, 0.3],    // Grace - deep purple
    [0.4, 0.2, 0.6],    // Morphic - purple
    [0.6, 0.4, 0.8],    // Bridge - light purple
    [0.8, 0.6, 1.0],    // Standard - bright purple
    [1.0, 0.8, 0.6],    // Consciousness - gold
    [1.0, 1.0, 0.8],    // Inflation - bright gold
    [1.0, 1.0, 1.0],    // CMB - white
  ],
  
  MIN_PHASE_TIME: 3000,               // Minimum time per phase (ms)
};

// === Debug and Logging ===
export const DEBUG = {
  VERBOSE: false,                     // Enable verbose logging
  PERFORMANCE_LOGGING: true,          // Log performance metrics
  SHADER_DEBUG: false,                // Enable shader debugging
  MEMORY_DEBUG: false,                // Enable memory usage logging
  
  LOG_COLORS: {
    INFO: '#9cf',
    WARNING: '#fc6', 
    ERROR: '#f84',
    SUCCESS: '#6f6',
    DEBUG: '#999',
  }
};

// === Default Parameter Values ===
export const DEFAULT_PARAMS = {
  // Core simulation
  fieldScale: 1.0,
  timeScale: 1.0,
  damping: 0.02,
  jitterSigma: 0.05,
  
  // Grace operator
  graceAmp: 0.5,
  graceRadius: 0.5,
  devourerAmp: 0.3,
  
  // Visual
  brightness: 1.0,
  exposure: 1.0,
  pointSize: 1.5,
  trailFade: 0.98,
  trailMix: 0.8,
  
  // FSCTF
  fsctfEnabled: true,
  graceComplexity: 1000.0,        // MID SETTINGS: Balanced emergence complexity (default)
  morphicRecursionDepth: 500,     // MID SETTINGS: Deep cosmogenesis depth (default)  
  consciousnessComplexity: 1000.0, // MID SETTINGS: Rich consciousness emergence (default)
  
  // Camera
  cameraX: 0.0,
  cameraY: 0.0,
  cameraZ: 8.0,
  cameraRotX: 0.6,
  cameraRotY: 0.3,
  fov: 45.0,
};

// Export all constants as a combined object for convenience
export const CONSTANTS = {
  SIMULATION,
  PERFORMANCE,
  MEMORY_LIMITS,
  MATH,
  WEBGL,
  PHYSICS,
  UI,
  COSMOGENESIS,
  DEBUG,
  DEFAULT_PARAMS,
};

