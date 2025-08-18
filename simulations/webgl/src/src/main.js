/**
 * FIRM Recursive Identity Emergence System – Ex Nihilo Cosmogenesis Engine
 * Refactored modular version
 */

import { loadAllShaders, createShaderProgram } from './modules/shaders/shaders-v2.js';
import { initWebGL2, createFloatTexture, createFramebuffer, resizeCanvasToDisplaySize, createFullscreenQuad, createParticleInstanceData, createProgram } from './modules/webgl/webgl-utils.js';
import { PERFORMANCE_MONITOR, setAdaptiveMode, resetPerformanceThrottle } from './modules/performance/performance.js';
import { GPUOptimizer } from './modules/performance/gpu-optimizer.js';
import { SimulationCore } from './modules/core/simulation-core.js?v=5';
import { UIBuilder } from './modules/ui/ui-builder.js';
import { CameraTransitionManager } from './modules/camera/camera-manager.js';
import { safeParamModify, resetUserOverrides, markAsUserOverride } from './modules/utils/param-utils.js';
import { vlog, vwarn, setVerbose } from './modules/utils/logging.js';
import { BrainSystem } from './modules/ai/brain-system.js';
import { MetricsSystem } from './modules/metrics/metrics-system.js';
import { EventHandler } from './modules/input/event-handler.js';
import { CONSTANTS } from './modules/config/constants.js';
import { FSCTFEvolutionEngine } from './modules/fsctf/evolution-engine.js';
import { startProgressiveCosmogenesis, updateProgressiveCosmogenesis, setupCosmogenesisButton, initializePhaseIndicators } from './modules/fsctf/cosmogenesis-functions.js';
import { CosmogenesisUI } from './modules/ui/cosmogenesis-ui.js';

// SAFE ADDITIONS: Advanced FSCTF Systems (off by default)
import { GPUMorphicBridge } from './modules/fsctf/gpu-morphic-bridge.js';
import { AdvancedConsciousnessEngine } from './modules/fsctf/advanced-consciousness-engine.js';
import { MultiScalePhiCascade } from './modules/fsctf/multi-scale-phi-cascade.js';
import { ConsciousnessTopologyFeedback } from './modules/fsctf/consciousness-topology-feedback.js';
import { DimensionalPortalVisualization } from './modules/fsctf/dimensional-portal-visualization.js';
import { RetrocausalMorphicResonance } from './modules/fsctf/retrocausal-morphic-resonance.js';

// Global state
let gl;
let canvas;
let shaders;
let simulationCore;
let gpuOptimizer;

// SAFE ADDITIONS: Advanced FSCTF System Instances (off by default)
let gpuMorphicBridge = null;
let advancedConsciousness = null;
let multiScaleCascade = null;
let consciousnessTopologyFeedback = null;
let dimensionalPortalVisualization = null;
let retrocausalMorphicResonance = null;

// Simulation parameters
const params = {
  // Core simulation parameters
  dt: 1/60,
  domain: 20.0,  // MUCH LARGER: More natural starting volume
  k_flow: 1.0,
  k_attract: 0.01,
  k_burst: 0.3,
  damping: 0.02,
  jitterSigma: 0.01,
  fieldScale: 1.0,
  timeScale: 1.0,
  
  // Rendering parameters (ANTI-STROBE: Fixed values optimized for 1M particles)
  pointSize: 0.8,        // Fixed tiny point size for maximum density
  brightness: 0.6,       // Fixed low brightness to prevent washout
  splatThresh: 0.12,     // Fixed threshold for particle cores
  exposure: 1.0,         // Fixed conservative exposure
  trailFade: 0.992,    // Slower fade for more temporal stability (anti-strobe)
  renderScale: 2.0,  // MAXIMUM DETAIL: 2x render scale for finest detail resolution
  // Visual expression controls
  edgeBoost: 0.8,
  vignetteStrength: 0.12,
  phaseTint: [1.0, 1.0, 1.0],
  tintStrength: 0.12,
  
  // FSCTF/FIRM parameters - TRANSITION: Keep fallbacks until full derivation is tested
  fsctfEnabled: true,
  graceComplexity: 1000.0,     // MID SETTINGS: Balanced emergence complexity (default)
  morphicRecursionDepth: 500,  // MID SETTINGS: Deep cosmogenesis depth (default)  
  consciousnessComplexity: 1000.0, // MID SETTINGS: Rich consciousness emergence (default)
  // NOTE: Above values serve as fallbacks during transition to full mathematical derivation
  
  // Camera parameters (Orbital Camera System)
  cameraEnabled: true,
  autoRotate: true,
  autoRotateSpeed: 1.2,
  cameraDistance: 12.0,       // Distance from center (comfortable default viewing distance)
  cameraAzimuth: 0.0,         // Horizontal rotation (0-360°)
  cameraElevation: 15.0,      // Vertical angle (-90 to 90°)
  cameraX: 0.0,               // Calculated from distance/azimuth/elevation
  cameraY: 0.0,               // Calculated from distance/azimuth/elevation  
  cameraZ: 8.0,               // Calculated from distance/azimuth/elevation
  cameraForwardX: 0.0,        // Camera forward vector (look direction)
  cameraForwardY: 0.0,
  cameraForwardZ: -1.0,
  cameraRightX: 1.0,          // Camera right vector  
  cameraRightY: 0.0,
  cameraRightZ: 0.0,
  cameraUpX: 0.0,             // Camera up vector
  cameraUpY: 1.0,
  cameraUpZ: 0.0,
  cameraSpeed: 1.0,           // Manual control sensitivity
  fov: 70.0,
  near: 0.1,
  far: 100.0,
  
  // Topology parameters
  showWireframe: false,
  wireframeOpacity: 0.3,
  wireframeDensity: 16,
  topologyTransitionDuration: 20.0,  // CINEMATIC: Extended transitions for maximum visual impact and mathematical appreciation
  
  // Manual Topology Override
  manualTopologyEnabled: false,  // Override cosmogenesis-controlled topology
  manualTopologyMode: 0,         // 0=Torus, 1=Möbius, 2=Klein, 3=φ-Klein, 4=Sphere
  torusR: 3.0,      // IMPROVED: Larger major radius for better particle distribution
  torusr: 1.0,      // IMPROVED: Larger minor radius for better visibility
  
  // Visual parameters
  drawFraction: 1.0,          // Fraction of particles to render (1.0 = all 589,824)
  particleQuality: 1.0,       // Overall particle density multiplier for structure clarity
  particleCount: 1048576,     // Number of particles to render - MAXIMUM density (1024×1024 texture capacity)
  densityAlphaReduction: 0.3,  // Fixed aggressive alpha reduction for 1M particles (0.0-1.0)
  colorMix: 0.5,
  selectivity: 0.0,
  
  // GPU Performance Optimization parameters
  shaderComplexity: 1.0,      // Shader computational complexity (0.2-1.0)
  visualEffects: 1.0,         // Visual effects intensity (0.4-1.0)
  maxRecursionDepth: 90.0,    // Maximum φ-recursive depth (4-90) - FIXED: Match 90-phase system
  useLOD: false,              // Level-of-detail optimization
  
  // Legacy cosmogenesis parameters REMOVED - native FSCTF system handles all progression
};

// Make params globally accessible for UI controls
window.params = params;

// Force cache refresh for visual controller
const timestamp = Date.now();

// Expose parameter utilities for UI
window.markAsUserOverride = markAsUserOverride;

// Deep debug pointSize changes to track what's overriding user settings
const originalPointSize = params.pointSize;
let pointSizeDebugEnabled = false;
let lastPointSizeSource = 'initial';

Object.defineProperty(params, 'pointSize', {
  get() {
    return this._pointSize || originalPointSize;
  },
  set(value) {
    if (pointSizeDebugEnabled && this._pointSize !== value) {
      const stack = new Error().stack;
      const caller = stack.split('\n')[2]?.trim() || 'unknown';
      const prevValue = this._pointSize;
      console.log(`🎯 POINTSIZE OVERRIDE: ${prevValue} → ${value}`);
      console.log(`   Source: ${caller}`);
      console.log(`   Previous source: ${lastPointSizeSource}`);
      
      // Get more stack context for deep tracing
      const stackLines = stack.split('\n').slice(1, 6);
      console.log(`   Full stack:`, stackLines);
      
      lastPointSizeSource = caller;
    }
    this._pointSize = value;
  },
  enumerable: true,
  configurable: true
});

// Initial value
params.pointSize = originalPointSize;

// Enable debugging after a delay to avoid startup noise
setTimeout(() => {
  pointSizeDebugEnabled = true;
  console.log('🐛 Deep pointSize debugging enabled - will trace all overrides');
}, 2000);

// WebGL resources
let programs = {};
let textures = {};
let framebuffers = {};
let vaos = {};

// Simulation constants (DYNAMIC RESOLUTION for mathematical structure clarity)
// Quality presets for different hardware capabilities:
// Draft: 256x256 = 65,536 particles | Standard: 512x512 = 262,144 | High: 768x768 = 589,824 | Ultra: 1024x1024 = 1,048,576
const QUALITY_PRESETS = {
  draft: { cols: 256, rows: 256, name: 'Draft (65K particles)' },
  standard: { cols: 512, rows: 512, name: 'Standard (262K particles)' },
  high: { cols: 768, rows: 768, name: 'High (590K particles)' },
  ultra: { cols: 1024, rows: 1024, name: 'Ultra (1M particles)' }
};
const CURRENT_QUALITY = 'standard'; // Balanced quality for performance (262K particles)

// REMOVED: calculateParticleDimensions() and getCurrentParticleDimensions() - No longer needed with fixed texture size

// FIXED texture size for stability - never recreate textures
const FIXED_COLS = 1024;  // Fixed texture width  
const FIXED_ROWS = 1024;  // Fixed texture height
const MAX_PARTICLES = FIXED_COLS * FIXED_ROWS; // 1,048,576 total texture capacity

// Dynamic particle count (how many particles we actually use within the fixed texture)
let NUM = MAX_PARTICLES; // Default: MAXIMUM particles (1M = full texture capacity)

// ULTRA-SIMPLE: Just update particle count - never recreate textures
function updateParticleDimensions() {
  const requestedCount = params.particleCount || MAX_PARTICLES;
  
  console.log(`🎯 SIMPLE UPDATE: Current: ${NUM.toLocaleString()} → Requested: ${requestedCount.toLocaleString()}`);
  
  // Clamp to texture capacity (never exceed fixed texture size)
  const clampedCount = Math.min(requestedCount, MAX_PARTICLES);
  
  if (clampedCount !== requestedCount) {
    console.warn(`⚠️ Clamped particle count to texture capacity: ${clampedCount.toLocaleString()} (max: ${MAX_PARTICLES.toLocaleString()})`);
    params.particleCount = clampedCount;
    
    // Update slider display
    const slider = document.querySelector('input[type="range"][data-param="particleCount"]');
    if (slider) {
      slider.value = clampedCount;
      const valueDisplay = slider.parentElement.querySelector('.parameter-value');
      if (valueDisplay) valueDisplay.textContent = clampedCount.toLocaleString();
    }
  }
  
  // Simply update the active particle count - textures stay the same size
  NUM = clampedCount;
  
  // ANTI-STROBE: Use completely fixed parameters - no dynamic calculations
  // Dynamic parameter system was causing strobing even with smoothing
  
  // Fixed parameters optimized for 1M particles (no changes, no strobing)
  if (!params._userOverridePointSize) params.pointSize = 0.8;      // Tiny points for 1M density
  if (!params._userOverrideBrightness) params.brightness = 0.6;    // Low brightness to prevent washout
  if (!params._userOverrideExposure) params.exposure = 1.0;        // Conservative exposure
  if (!params._userOverrideDensityAlpha) params.densityAlphaReduction = 0.3; // Heavy alpha reduction
  
  // ANTI-STROBE: Never recreate VAO - use fixed maximum capacity always
  // VAO recreation was causing major frame hitches and strobing
  // Instead, just update the draw count - VAO supports full texture capacity
  
  if (!vaos.particles || !vaos.particles.vao) {
    // Only create VAO if it doesn't exist (initialization)
    vaos.particles = createParticleInstanceData(gl, MAX_PARTICLES);
    console.log(`🔧 Initial VAO created with FIXED capacity: ${MAX_PARTICLES.toLocaleString()} particles`);
  }
  
  // VAO never changes - only the draw count in renderParticles() changes
  console.log(`✅ ZERO-HITCH: Using existing VAO, draw count will be ${NUM.toLocaleString()}`);;
  
  // Update display
  const qualityInfo = document.getElementById('qualityInfo');
  if (qualityInfo) {
    const particleCountK = (NUM / 1000).toFixed(0);
    qualityInfo.textContent = `Dynamic (${particleCountK}K particles)`;
  }
  
  console.log(`✅ ANTI-STROBE: Particle count updated to ${NUM.toLocaleString()} with FIXED parameters (Point: ${params.pointSize}, Brightness: ${params.brightness})`);
}

/**
 * Calculate dynamic visual parameters based on particle density
 * Higher density = smaller points + lower brightness to prevent washout and strobing
 */
function calculateDynamicVisualParameters(particleCount, maxParticles) {
  // Calculate density ratio (0.0 = very few particles, 1.0 = maximum density)
  const densityRatio = Math.min(particleCount / maxParticles, 1.0);
  
  // ANTI-STROBE: Temporal smoothing to prevent rapid parameter changes
  if (!calculateDynamicVisualParameters.smoothedRatio) {
    calculateDynamicVisualParameters.smoothedRatio = densityRatio;
  }
  
  // Smooth the density ratio to prevent strobing from rapid changes
  const smoothingFactor = 0.95; // Strong smoothing
  calculateDynamicVisualParameters.smoothedRatio = 
    calculateDynamicVisualParameters.smoothedRatio * smoothingFactor + 
    densityRatio * (1 - smoothingFactor);
  
  const smoothedDensityRatio = calculateDynamicVisualParameters.smoothedRatio;
  
  // DYNAMIC POINT SIZE: Inverse relationship with density (more conservative)
  // At low density (100K): 3.0 point size
  // At max density (1M): 0.8 point size (tiny to prevent overlap)
  const dynamicPointSize = 3.0 - (smoothedDensityRatio * 2.2);
  
  // DYNAMIC BRIGHTNESS: Much more conservative to prevent white washout
  // At low density: 1.2 brightness
  // At max density: 0.6 brightness (low to preserve colors)
  const dynamicBrightness = 1.2 - (smoothedDensityRatio * 0.6);
  
  // DYNAMIC EXPOSURE: Conservative increase, capped to prevent washout
  // At low density: 1.8 exposure
  // At max density: 1.0 exposure (low to preserve colors)
  const dynamicExposure = 1.8 - (smoothedDensityRatio * 0.8);
  
  // DYNAMIC ALPHA REDUCTION: Much more aggressive at high density
  // At low density: 0.95 (less reduction, more opaque)
  // At max density: 0.3 (heavy reduction, prevent oversaturation)
  const dynamicAlphaReduction = 0.95 - (smoothedDensityRatio * 0.65);
  
  // ANTI-STROBE: All console logging disabled (this function shouldn't be called anyway)
  
  return {
    pointSize: dynamicPointSize,
    brightness: dynamicBrightness,
    exposure: dynamicExposure,
    densityAlphaReduction: dynamicAlphaReduction,
    densityRatio: densityRatio
  };
}

/**
 * Reset all visual parameters to dynamic calculation (clear user overrides)
 */
function resetToDynamicVisuals() {
  console.log('🔄 Resetting all visual parameters to dynamic calculation...');
  
  // Clear all user override flags
  params._userOverridePointSize = false;
  params._userOverrideBrightness = false;
  params._userOverrideExposure = false;
  params._userOverrideDensityAlpha = false;
  
  // Recalculate dynamic parameters
  const dynamicParams = calculateDynamicVisualParameters(NUM, MAX_PARTICLES);
  
  // Apply dynamic values
  params.pointSize = dynamicParams.pointSize;
  params.brightness = dynamicParams.brightness;
  params.exposure = dynamicParams.exposure;
  params.densityAlphaReduction = dynamicParams.densityAlphaReduction;
  params.trailFade = 0.992; // Reset to optimized trail fade value
  
  console.log('✅ All visual parameters reset to dynamic calculation');
  
  // Update UI sliders to reflect new values
  const sliders = document.querySelectorAll('input[type="range"]');
  sliders.forEach(slider => {
    const paramName = slider.getAttribute('data-param') || slider.id.replace('param-', '');
    if (['pointSize', 'brightness', 'exposure', 'densityAlphaReduction', 'trailFade'].includes(paramName)) {
      slider.value = params[paramName];
      const valueDisplay = slider.parentElement.querySelector('.parameter-value') || 
                          slider.parentElement.querySelector('span');
      if (valueDisplay) {
        valueDisplay.textContent = params[paramName].toFixed(2);
      }
    }
  });
}

/**
 * Get GPU performance tier for smart rendering decisions
 */
// CACHED: GPU performance tier (detect once at startup, never again)
let cachedGPUTier = null;

function getGPUPerformanceTier() {
  // ANTI-STROBE: Return cached result - never re-detect during runtime
  if (cachedGPUTier) return cachedGPUTier;
  
  if (!gl) {
    cachedGPUTier = 'budget';
    return cachedGPUTier;
  }
  
  try {
    // Get GPU info (expensive - only do once!)
    const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    const renderer = debugInfo ? gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) : 'Unknown';
    const maxTextureSize = gl.getParameter(gl.MAX_TEXTURE_SIZE);
    const maxVertexAttribs = gl.getParameter(gl.MAX_VERTEX_ATTRIBS);
    const maxFragmentTextureUnits = gl.getParameter(gl.MAX_TEXTURE_IMAGE_UNITS);
    
    // Check for high-end GPU indicators
    const isHighEnd = (
      maxTextureSize >= 16384 &&
      maxVertexAttribs >= 16 &&
      maxFragmentTextureUnits >= 16 &&
      (renderer.includes('RTX') || renderer.includes('RX 6') || renderer.includes('RX 7') || 
       renderer.includes('M1') || renderer.includes('M2') || renderer.includes('GTX 1080') ||
       renderer.includes('GTX 1070') || renderer.includes('Radeon Pro'))
    );
    
    // Check for mid-range GPU indicators  
    const isMidRange = (
      maxTextureSize >= 8192 &&
      maxVertexAttribs >= 12 &&
      (renderer.includes('GTX') || renderer.includes('RX') || renderer.includes('Intel Iris') ||
       renderer.includes('Radeon') || renderer.includes('GeForce'))
    );
    
    if (isHighEnd) {
      cachedGPUTier = 'high-end';
    } else if (isMidRange) {
      cachedGPUTier = 'mid-range';  
    } else {
      cachedGPUTier = 'budget';
    }
    
    console.log(`🖥️ GPU TIER CACHED: ${cachedGPUTier.toUpperCase()} (Renderer: ${renderer})`);
    return cachedGPUTier;
    
  } catch (error) {
    console.warn('⚠️ Could not detect GPU tier:', error);
    cachedGPUTier = 'budget'; // Safe fallback
    return cachedGPUTier;
  }
}

// Make functions globally accessible for UI and debugging
window.updateParticleDimensions = updateParticleDimensions;
window.calculateDynamicVisualParameters = calculateDynamicVisualParameters;
window.resetToDynamicVisuals = resetToDynamicVisuals;
window.getGPUPerformanceTier = getGPUPerformanceTier;

// Debug commands for console (try these in browser console!)
console.log('🎮 DYNAMIC VISUAL SYSTEM DEBUG COMMANDS:');
console.log('  📊 calculateDynamicVisualParameters(NUM, MAX_PARTICLES) - Show current dynamic values');
console.log('  🔄 resetToDynamicVisuals() - Reset all visual parameters to dynamic calculation');
console.log('  🎛️ updateParticleDimensions() - Update particle count and recalculate dynamics');
console.log('  🎨 Current params: pointSize=' + (params.pointSize || 'unset') + ', brightness=' + (params.brightness || 'unset'));

// Cinematic overlay functionality removed to streamline UI

/**
 * Update morphic strand activity panel with live data
 */
/**
 * Update enhanced phase status display with comprehensive information
 */
function updateEnhancedPhaseStatus() {
  const phaseStatusCurrent = document.getElementById('phase-status-current');
  const phaseStatusDescription = document.getElementById('phase-status-description');
  const phaseStatusNext = document.getElementById('phase-status-next');
  
  if (!phaseStatusCurrent || !phaseStatusDescription || !phaseStatusNext) return;
  
  // Comprehensive φ-recursion depth phase information database (90 phases)
  const phaseDatabase = {
    0: {
      name: 'Ex Nihilo (φ^0)',
      description: 'Pure mathematical void. φ^0 = 1, unity before emergence. No structure, no recursion.',
      nextExpectation: 'Grace Operator will activate first φ^1 recursion level.',
      visualCues: 'Empty space, minimal activity, mathematical singularity state.',
      physics: 'Pre-creation mathematical state, φ^0 = 1'
    },
    1: {
      name: 'Grace Seeding (φ^1)', 
      description: 'First φ-recursion level active (φ ≈ 1.618). Morphic seed networks emerging from pure mathematics.',
      nextExpectation: 'Quark mass ratios will stabilize at φ^2 recursion depth.',
      visualCues: 'First morphic strands, golden ratio patterns emerging.',
      physics: 'φ^1 = 1.618: Grace Operator activation, morphic field genesis'
    },
    2: {
      name: 'Quark Ratios (φ^2)',
      description: 'φ^2 ≈ 2.618 recursion establishes up/down quark mass ratio (φ^-2 ≈ 0.382).',
      nextExpectation: 'Hadron binding will emerge through φ^3 bottom/charm interactions.',
      visualCues: 'Particle-like structures, fundamental ratios manifesting.',
      physics: 'φ^-2 = 0.382: Up/Down quark mass ratio, fundamental matter asymmetry'
    },
    3: {
      name: 'Hadron Binding (φ^3)',
      description: 'φ^3 ≈ 4.236 recursion creates bottom/charm quark mass ratio, enabling hadron formation.',
      nextExpectation: 'Strange matter will emerge at φ^4 recursion depth.',
      visualCues: 'Bound particle states, multi-particle structures forming.',
      physics: 'φ^3 = 4.236: Bottom/Charm quark ratio, hadron stability'
    },
    4: {
      name: 'Strange Matter (φ^4)',
      description: 'φ^4 ≈ 6.854 recursion establishes strange/down quark ratio, strange particle emergence.',
      nextExpectation: 'Charm resonance will activate at φ^5 depth with new boson emergence.',
      visualCues: 'Exotic particle behavior, strange decay patterns visible.',
      physics: 'φ^4 = 6.854: Strange/Down quark ratio, exotic matter formation'
    },
    5: {
      name: 'Charm Resonance (φ^5)',
      description: 'φ^5 ≈ 11.09 recursion creates charm/strange ratio and predicts new boson (m = φ^5 × m_W).',
      nextExpectation: 'Muon generation will emerge at φ^6 recursion level.',
      visualCues: 'Resonance patterns, new particle types, boson-like structures.',
      physics: 'φ^5 = 11.09: Charm/Strange ratio, new boson mass prediction'
    },
    6: {
      name: 'Muon Generation (φ^6)',
      description: 'φ^6 ≈ 17.94 recursion enables muon emergence via φ^6 mass scaling components.',
      nextExpectation: 'Electromagnetic coupling will form through φ^7 recursive structure.',
      visualCues: 'Second-generation particles, muon-like tracks and decay patterns.',
      physics: 'φ^6 = 17.94: Muon mass scaling, second generation lepton emergence'
    },
    7: {
      name: 'Electromagnetic (φ^7)',
      description: 'φ^7 ≈ 29.03 recursion creates electromagnetic coupling via (φ^7+1)/φ^15 formula.',
      nextExpectation: 'Complex hadron matrix will develop at φ^8 recursion depth.',
      visualCues: 'Electromagnetic effects, charge separation, field-like behaviors.',
      physics: 'φ^7 = 29.03: EM coupling α via (φ^7+1)/φ^15, electromagnetism birth'
    },
    8: {
      name: 'Hadron Matrix (φ^8)',
      description: 'φ^8 ≈ 46.98 recursion enables complex hadron interactions and mirror emergence threshold.',
      nextExpectation: 'Lepton families will diversify at φ^9 recursion level.',
      visualCues: 'Complex particle interactions, tesseract emergence, soul object formation.',
      physics: 'φ^8 = 46.98: Complex hadron matrix, mirror bloom threshold (R_collapse)'
    },
    9: {
      name: 'Lepton Families (φ^9)',
      description: 'φ^9 ≈ 76.01 recursion establishes tau/muon mass ratios and lepton family structure.',
      nextExpectation: 'Matter structure will crystallize at φ^10 recursion depth.',
      visualCues: 'Diverse particle families, generational structure, family patterns.',
      physics: 'φ^9 = 76.01: Tau/electron mass ratio components, lepton generation structure'
    },
    10: {
      name: 'Matter Structure (φ^10)',
      description: 'φ^10 ≈ 122.97 recursion determines electron/proton mass ratio (φ^-10), matter architecture.',
      nextExpectation: 'Dark coupling will emerge at φ^11 recursion level.',
      visualCues: 'Stable matter configurations, atomic-like structures, mass hierarchy.',
      physics: 'φ^-10 = 8.1×10^-6: Electron/proton mass ratio, matter structure stability'
    },
    11: {
      name: 'Dark Coupling (φ^11)',
      description: 'φ^11 ≈ 199.00 recursion creates dark matter coupling (φ^-11) and weak force components.',
      nextExpectation: 'Tau emergence will complete at φ^12 recursion depth.',
      visualCues: 'Dark matter effects, weak interactions, invisible matter influence.',
      physics: 'φ^-11 = 5.0×10^-6: Dark matter coupling, weak coupling terms'
    },
    12: {
      name: 'Tau Emergence (φ^12)',
      description: 'φ^12 ≈ 321.99 recursion completes tau lepton formation (m_τ/m_e = φ^12 × factors).',
      nextExpectation: 'Field unification will begin at φ^13 recursion level.',
      visualCues: 'Heavy lepton completion, third generation particles, tau decay signatures.',
      physics: 'φ^12 = 321.99: Tau/electron mass ratio, third generation completion'
    },
    13: {
      name: 'Field Unification (φ^13)',
      description: 'φ^13 ≈ 521.00 recursion enables advanced field coupling and force unification.',
      nextExpectation: 'Nucleosynthesis will activate at φ^14 recursion depth.',
      visualCues: 'Unified field effects, force coupling, advanced particle interactions.',
      physics: 'φ^13 = 521.00: Advanced field unification, higher-order coupling constants'
    },
    14: {
      name: 'Nucleosynthesis (φ^14)',
      description: 'φ^14 ≈ 842.99 recursion enables heavy element formation and nuclear synthesis.',
      nextExpectation: 'Cosmic structure will complete at φ^15 recursion depth.',
      visualCues: 'Nuclear fusion signatures, element formation, nucleosynthetic processes.',
      physics: 'φ^14 = 842.99: Heavy element synthesis, nuclear process optimization'
    },
    15: {
      name: 'Cosmic Structure (φ^15)',
      description: 'φ^15 ≈ 1364.00 recursion completes electromagnetic constant (φ^15 denominator) and cosmic structure.',
      nextExpectation: 'Hypermassive scale begins - transition to theoretical φ-levels beyond visual recursion.',
      visualCues: 'Cosmic-scale structures, maximum visual complexity, universe-scale organization.',
      physics: 'φ^15 = 1364.00: EM constant completion α = (φ^7+1)/φ^15, cosmic structure'
    },
    // HYPERMASSIVE SCALE (φ^16 - φ^20): Beyond visual recursion, theoretical progression
    16: { name: 'Hypermass φ^16', description: 'φ^16 ≈ 2207 recursion enters hypermassive particle scale.', nextExpectation: 'Higher-order mass relationships emerge.', visualCues: 'Theoretical - beyond visual shader capability.', physics: 'φ^16 = 2207: Hypermassive scale initiation' },
    17: { name: 'Hypermass φ^17', description: 'φ^17 ≈ 3571 recursion develops advanced mass hierarchies.', nextExpectation: 'Strong coupling unification approaches.', visualCues: 'Theoretical - mathematical progression only.', physics: 'φ^17 = 3571: Advanced mass hierarchy, strong coupling terms' },
    18: { name: 'Hypermass φ^18', description: 'φ^18 ≈ 5778 recursion establishes complex gauge relationships.', nextExpectation: 'Top quark mass completion approaches.', visualCues: 'Theoretical - pure mathematical emergence.', physics: 'φ^18 = 5778: Complex gauge field relationships' },
    19: { name: 'Hypermass φ^19', description: 'φ^19 ≈ 9349 recursion approaches top quark mass threshold.', nextExpectation: 'Top/electron mass ratio completion imminent.', visualCues: 'Theoretical - heaviest matter scale.', physics: 'φ^19 = 9349: Pre-top quark mass completion' },
    20: { name: 'Top/Electron Completion (φ^20)', description: 'φ^20 ≈ 15127 recursion completes top/electron mass ratio (φ^20 × factors ≈ 340,000).', nextExpectation: 'Advanced field unification begins across intermediate scales.', visualCues: 'Theoretical - heaviest to lightest matter complete.', physics: 'φ^20 = 15127: m_t/m_e completion, matter hierarchy complete' },
    // INTERMEDIATE UNIFICATION (φ^21 - φ^30): Advanced field theory
    21: { name: 'Advanced Unify φ^21', description: 'φ^21 ≈ 24476 recursion initiates advanced field unification.', nextExpectation: 'Higher-order coupling constants emerge.', visualCues: 'Theoretical - field unification regime.', physics: 'φ^21 = 24476: Advanced field unification initiation' },
    22: { name: 'Advanced Unify φ^22', description: 'φ^22 ≈ 39603 recursion develops complex field interactions.', nextExpectation: 'Multi-field coupling stabilization.', visualCues: 'Theoretical - complex field interactions.', physics: 'φ^22 = 39603: Complex multi-field coupling' },
    23: { name: 'Advanced Unify φ^23', description: 'φ^23 ≈ 64079 recursion establishes higher-order symmetries.', nextExpectation: 'Sterile neutrino mass predictions.', visualCues: 'Theoretical - symmetry completion.', physics: 'φ^23 = 64079: Higher-order symmetries, sterile neutrinos' },
    24: { name: 'Advanced Unify φ^24', description: 'φ^24 ≈ 103682 recursion develops unified field equations.', nextExpectation: 'Pre-gravity unification regime.', visualCues: 'Theoretical - unified field regime.', physics: 'φ^24 = 103682: Unified field equations' },
    25: { name: 'Advanced Unify φ^25', description: 'φ^25 ≈ 167761 recursion approaches gravity-matter coupling.', nextExpectation: 'Quantum gravity threshold approaches.', visualCues: 'Theoretical - pre-gravity coupling.', physics: 'φ^25 = 167761: Gravity-matter pre-coupling' },
    26: { name: 'Advanced Unify φ^26', description: 'φ^26 ≈ 271443 recursion establishes pre-gravitational field structure.', nextExpectation: 'Spacetime geometry emergence.', visualCues: 'Theoretical - pre-gravitational structure.', physics: 'φ^26 = 271443: Pre-gravitational field structure' },
    27: { name: 'Advanced Unify φ^27', description: 'φ^27 ≈ 439204 recursion develops spacetime-matter interactions.', nextExpectation: 'General relativity emergence.', visualCues: 'Theoretical - spacetime-matter coupling.', physics: 'φ^27 = 439204: Spacetime-matter interactions' },
    28: { name: 'Advanced Unify φ^28', description: 'φ^28 ≈ 710647 recursion establishes curved spacetime dynamics.', nextExpectation: 'Quantum gravity emergence imminent.', visualCues: 'Theoretical - curved spacetime regime.', physics: 'φ^28 = 710647: Curved spacetime dynamics' },
    29: { name: 'Advanced Unify φ^29', description: 'φ^29 ≈ 1149851 recursion approaches quantum gravity threshold.', nextExpectation: 'Planck scale physics activation.', visualCues: 'Theoretical - pre-quantum gravity.', physics: 'φ^29 = 1149851: Pre-quantum gravity threshold' },
    30: { name: 'Advanced Unify φ^30', description: 'φ^30 ≈ 1860498 recursion completes pre-quantum gravity unification.', nextExpectation: 'Quantum gravity critical transition at φ^31.', visualCues: 'Theoretical - quantum gravity threshold.', physics: 'φ^30 = 1860498: Pre-quantum gravity completion' },
    // QUANTUM GRAVITY CRITICAL THRESHOLD (φ^31): Where physics changes fundamentally
    31: { name: 'Quantum Gravity (φ^31)', description: 'φ^31 ≈ 3010349 recursion reaches quantum gravity scale (E = φ^31 × E_Planck). General Relativity breakdown threshold.', nextExpectation: 'Cosmological recursive cooling phases begin.', visualCues: 'Theoretical - quantum gravity emergence, spacetime quantization.', physics: 'φ^31 = 3,010,349: E_QG = φ^31 × E_Planck, neutrino masses, quantum spacetime' }
  };
  
  // COSMOLOGICAL COOLING PHASES (φ^32 - φ^89): Fill remaining with cooling progression
  // These represent the recursive thermal evolution from quantum gravity to cosmological scales
  for (let i = 32; i <= 89; i++) {
    const phiPower = Math.pow(1.618033988749895, i);
    const coolingStage = i - 31;
    phaseDatabase[i] = {
      name: `Recursive Cooling φ^${i}`,
      description: `φ^${i} ≈ ${phiPower.toExponential(2)} recursion - cooling stage ${coolingStage}/58 in Planck→CMB thermal evolution.`,
      nextExpectation: i === 89 ? 'Ultimate cosmological scale φ^90 approaches.' : 'Continued recursive thermal evolution.',
      visualCues: 'Theoretical - cosmological thermal evolution, recursive cooling cascade.',
      physics: `φ^${i} = ${phiPower.toExponential(2)}: Cooling stage ${coolingStage}, thermal evolution scale`
    };
  }
  
  // ULTIMATE SCALE (φ^90): The final theoretical scale
  phaseDatabase[89] = {
    name: 'Ultimate Scale (φ^90)',
    description: 'φ^90 ≈ 2.88×10^18 recursion - Ultimate FSCTF scale. Cosmological constant Λ = φ^-90/l_P². Complete Planck→CMB recursive cooling (90 shells).',
    nextExpectation: 'THEORY COMPLETE - φ^90 represents the ultimate scale in FSCTF mathematics.',
    visualCues: 'Theoretical - ultimate cosmological constant scale, theory completion.',
    physics: 'φ^90 = 2.88×10^18: Λ = φ^-90/l_P², ultimate FSCTF scale, theory completion'
  };
  
  if (window.progressiveCosmogenesis && window.progressiveCosmogenesis.active) {
    const currentPhase = window.progressiveCosmogenesis.currentPhase;
    const phase = phaseDatabase[currentPhase] || phaseDatabase[0];
    const nextPhase = phaseDatabase[currentPhase + 1];
    
    // Update current phase display
    phaseStatusCurrent.textContent = `Phase ${currentPhase + 1}/90: ${phase.name}`;
    phaseStatusDescription.textContent = `${phase.description} Physics: ${phase.physics}`;
    
    // Update next phase expectation and distinguish visual vs theoretical phases
    let visualStatus = '';
    if (currentPhase <= 15) {
      visualStatus = ' [VISUAL]';
    } else {
      visualStatus = ' [THEORETICAL]';
    }
    
    if (nextPhase) {
      phaseStatusNext.textContent = `Next: ${nextPhase.name}${visualStatus} - ${phase.nextExpectation}`;
    } else {
      phaseStatusNext.textContent = `🌟 THEORY COMPLETE - φ^90 Ultimate Scale reached! FSCTF mathematics complete from void to cosmological constant.`;
    }
    
  } else {
    // Not active - show initialization status
    phaseStatusCurrent.textContent = 'Phase System Inactive';
    phaseStatusDescription.textContent = 'Click "INVOKE RECURSIVE GENESIS" to begin the 90-phase φ-recursion Theory of Everything sequence.';
    phaseStatusNext.textContent = 'Ready to begin with Phase 1: Grace Operator activation...';
  }
}

function updateMorphicActivityPanel() {
  if (!window.graceOperator) {
    console.warn('⚠️ Grace Operator not available for UI updates');
    return;
  }
  
  const strands = window.graceOperator.morphicStrands || [];
  const field = window.graceOperator.morphicField?.field || 0;
  
  // Calculate stability distribution
  const stableCounts = { stable: 0, meta: 0, unstable: 0 };
  strands.forEach(strand => {
    if (strand.stability > 0.7) stableCounts.stable++;
    else if (strand.stability > 0.3) stableCounts.meta++;
    else stableCounts.unstable++;
  });
  
  // Calculate creation rate (approximate)
  const currentTime = Date.now();
  if (!updateMorphicActivityPanel.lastTime) updateMorphicActivityPanel.lastTime = currentTime;
  if (!updateMorphicActivityPanel.lastStrandCount) updateMorphicActivityPanel.lastStrandCount = strands.length;
  
  const deltaTime = (currentTime - updateMorphicActivityPanel.lastTime) / 1000;
  const deltaStrands = strands.length - updateMorphicActivityPanel.lastStrandCount;
  const creationRate = deltaTime > 0 ? deltaStrands / deltaTime : 0;
  
  updateMorphicActivityPanel.lastTime = currentTime;
  updateMorphicActivityPanel.lastStrandCount = strands.length;
  
  // Update UI elements
  const activeStrandsEl = document.getElementById('active-strands');
  const creationRateEl = document.getElementById('creation-rate');
  const fieldStrengthEl = document.getElementById('field-strength');
  const stableCountEl = document.getElementById('stable-count');
  const metaCountEl = document.getElementById('meta-count');
  const unstableCountEl = document.getElementById('unstable-count');
  
  if (activeStrandsEl) activeStrandsEl.textContent = strands.length.toLocaleString();
  if (creationRateEl) creationRateEl.textContent = Math.max(0, creationRate).toFixed(1);
  if (fieldStrengthEl) fieldStrengthEl.textContent = field.toFixed(3);
  if (stableCountEl) stableCountEl.textContent = stableCounts.stable;
  if (metaCountEl) metaCountEl.textContent = stableCounts.meta;
  if (unstableCountEl) unstableCountEl.textContent = stableCounts.unstable;
}

/**
 * Update brain status display
 */
function updateBrainStatusDisplay() {
  const brainStatusEl = document.getElementById('brain-status');
  if (!brainStatusEl) return;
  
  const cosmogenesisActive = window.simulationCore?.fsctfEngine?.cosmogenesisActive;
  const brainState = window.Brain?.getState();
  
  if (cosmogenesisActive) {
    brainStatusEl.innerHTML = '🧠 FSCTF Brain: <span style="color: #ff6600;">DISABLED (Cosmogenesis Active)</span>';
    brainStatusEl.title = 'Brain System disabled during cosmogenesis to allow dramatic phase-based visual evolution';
  } else if (brainState) {
    const status = brainState.evaluating ? 'EVALUATING' : 'ACTIVE';
    const color = brainState.evaluating ? '#00ff00' : '#0088ff';
    brainStatusEl.innerHTML = `🧠 FSCTF Brain: <span style="color: ${color};">${status}</span> (Archive: ${brainState.archiveSize})`;
    brainStatusEl.title = `Brain System: ${status} - Archive size: ${brainState.archiveSize}, Temperature: ${brainState.temperature.toFixed(2)}`;
  } else {
    brainStatusEl.innerHTML = '🧠 FSCTF Brain: <span style="color: #666666;">INITIALIZING</span>';
  }
}

/**
 * WebGL Context Loss Recovery
 */
function setupWebGLContextRecovery(canvas) {
  let contextLost = false;
  
  canvas.addEventListener('webglcontextlost', function(event) {
    event.preventDefault();
    contextLost = true;
    console.warn('🚨 WebGL context lost! Pausing simulation...');
    
    // Show user notification
    const notification = document.createElement('div');
    notification.id = 'context-lost-notification';
    notification.innerHTML = `
      <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                  background: rgba(0,0,0,0.9); color: #fc6; padding: 20px; 
                  border-radius: 8px; border: 2px solid #fc6; z-index: 9999; text-align: center;">
        <h3>⚠️ Graphics Context Lost</h3>
        <p>Browser minimized or tab switched.<br/>Attempting recovery...</p>
        <div style="width: 200px; height: 4px; background: rgba(255,204,102,0.3); border-radius: 2px; margin: 10px 0;">
          <div style="width: 0%; height: 100%; background: #fc6; border-radius: 2px; 
                      animation: recovery-progress 3s ease-in-out infinite;" id="recovery-progress"></div>
        </div>
      </div>
    `;
    document.body.appendChild(notification);
    
    // Add recovery animation
    const style = document.createElement('style');
    style.textContent = `
      @keyframes recovery-progress {
        0% { width: 0%; }
        50% { width: 70%; }
        100% { width: 0%; }
      }
    `;
    document.head.appendChild(style);
  });
  
  canvas.addEventListener('webglcontextrestored', function() {
    console.log('✅ WebGL context restored! Reinitializing...');
    
    // Remove notification
    const notification = document.getElementById('context-lost-notification');
    if (notification) {
      notification.remove();
    }
    
    // Reinitialize everything
    setTimeout(async () => {
      try {
        contextLost = false;
        
        // Re-get the WebGL context
        gl = initWebGL2(canvas);
        
        // Recreate resources
        shaders = await loadAllShaders();
        createShaderPrograms();
        createWebGLResources();
        
        // Reinitialize simulation
        simulationCore = new SimulationCore(gl, shaders, params, canvas);
    
    // CRITICAL FIX: Expose simulationCore globally for cosmogenesis functions
    window.simulationCore = simulationCore;
    console.log('✅ DEBUG: simulationCore exposed globally:', window.simulationCore);
        
        console.log('🔄 Context recovery complete - resuming simulation');
      } catch (error) {
        console.error('❌ Context recovery failed:', error);
        
        // Show recovery failed notification
        const failedNotification = document.createElement('div');
        failedNotification.innerHTML = `
          <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                      background: rgba(128,0,0,0.9); color: #fff; padding: 20px; 
                      border-radius: 8px; border: 2px solid #f44; z-index: 9999; text-align: center;">
            <h3>❌ Recovery Failed</h3>
            <p>Please refresh the page to continue.</p>
            <button onclick="location.reload()" 
                    style="background: #f44; color: white; border: none; padding: 8px 16px; 
                           border-radius: 4px; cursor: pointer; margin-top: 10px;">
              Refresh Page
            </button>
          </div>
        `;
        document.body.appendChild(failedNotification);
      }
    }, 100);
  });
  
  // Return context loss status checker
  return {
    isLost: () => contextLost
  };
}

/**
 * Loading screen management
 */
const LoadingScreen = {
  updateProgress(percent, text) {
    const progressFill = document.getElementById('loading-progress-fill');
    const loadingText = document.getElementById('loading-text');
    
    if (progressFill) progressFill.style.width = `${percent}%`;
    if (loadingText) loadingText.textContent = text;
  },
  
  hide() {
    const loadingScreen = document.getElementById('loading-screen');
    if (loadingScreen) {
      loadingScreen.classList.add('hidden');
      setTimeout(() => {
        loadingScreen.style.display = 'none';
      }, 500);
    }
  }
};

/**
 * Initialize the application
 */
async function init() {
  try {
    LoadingScreen.updateProgress(10, 'Initializing WebGL context...');
    console.log('🚀 Initializing FSCTF Cosmogenesis System...');
    
    // Get canvas and initialize WebGL
    canvas = document.getElementById('c');
    gl = initWebGL2(canvas);
    
    // Add WebGL context loss recovery
    setupWebGLContextRecovery(canvas);
    LoadingScreen.updateProgress(25, 'WebGL context established');
    
    // Load all shaders
    console.log('📋 Loading shaders...');
    LoadingScreen.updateProgress(40, 'Loading FSCTF shaders...');
    shaders = await loadAllShaders();
    LoadingScreen.updateProgress(55, 'Compiling shader programs...');
    
    // Create shader programs
    createShaderPrograms();
    LoadingScreen.updateProgress(70, 'Creating WebGL resources...');
    
    // Create WebGL resources
    createWebGLResources();
    
    // Initialize simulation core with canvas for blob detection
    LoadingScreen.updateProgress(85, 'Initializing FSCTF systems...');
    simulationCore = new SimulationCore(gl, shaders, params, canvas);
    
    // CRITICAL FIX: Expose simulationCore globally for cosmogenesis functions
    window.simulationCore = simulationCore;
    console.log('✅ DEBUG: simulationCore exposed globally:', window.simulationCore);
    
      // CRITICAL FIX: Ensure simulationCore is globally accessible
  if (!window.simulationCore) {
    console.error('❌ CRITICAL: simulationCore not globally exposed!');
    window.simulationCore = simulationCore;
  }
  console.log('🔍 DEBUG: Global simulationCore check:', !!window.simulationCore);
  console.log('🔍 DEBUG: simulationCore methods:', window.simulationCore ? Object.keys(window.simulationCore) : 'none');
  
  // SAFE ADDITIONS: Initialize advanced FSCTF systems (off by default)
  console.log('🌊 Initializing Advanced FSCTF Enhancement Systems...');
  gpuMorphicBridge = new GPUMorphicBridge();
  advancedConsciousness = new AdvancedConsciousnessEngine();
  multiScaleCascade = new MultiScalePhiCascade();
  consciousnessTopologyFeedback = new ConsciousnessTopologyFeedback();
  dimensionalPortalVisualization = new DimensionalPortalVisualization();
  retrocausalMorphicResonance = new RetrocausalMorphicResonance();
  
  // Expose to global for debugging and UI access
  window.gpuMorphicBridge = gpuMorphicBridge;
  window.advancedConsciousness = advancedConsciousness;
  window.multiScaleCascade = multiScaleCascade;
  window.consciousnessTopologyFeedback = consciousnessTopologyFeedback;
  window.dimensionalPortalVisualization = dimensionalPortalVisualization;
  window.retrocausalMorphicResonance = retrocausalMorphicResonance;
  console.log('✅ Advanced FSCTF systems initialized (disabled by default - use G, C, M keys to activate)');
  
  // Initialize GPU Performance Optimizer
  console.log('🚀 Initializing GPU Performance Optimizer...');
    gpuOptimizer = new GPUOptimizer(60, 30); // Target 60fps, minimum 30fps
    gpuOptimizer.setAutoAdaptation(false); // ANTI-STROBE: Disable auto-adaptation to prevent dynamic changes
    
    // Initialize UI
    LoadingScreen.updateProgress(95, 'Setting up user interface...');
    initializeUI();
    
    // Wire up the new educational UI controls
    wireUpLearningControls();
    
    // Finalization
    LoadingScreen.updateProgress(100, 'Ready for cosmogenesis!');
    
    // Hide loading screen after a brief moment
    setTimeout(() => {
      LoadingScreen.hide();
      
      // PERFORMANCE: Show GPU tier and optimizations
      const detectedGPU = getGPUPerformanceTier();
      console.log(`🖥️ GPU TIER DETECTED: ${detectedGPU.toUpperCase()}`);
      console.log(`🧠 SMART OPTIMIZATIONS: GPU-aware particle culling, shader complexity reduction, physics frequency adjustment`);
      console.log(`🎯 ANTI-STROBE FIXED: Point: ${params.pointSize}, Brightness: ${params.brightness}, Exposure: ${params.exposure}, Alpha: ${params.densityAlphaReduction}`);
      
      updateParticleDimensions(); // This will ensure VAO matches particle count
      
      console.log('✅ Initialization complete, starting main loop with FIXED anti-strobe parameters');
    requestAnimationFrame(mainLoop);
    }, 800);
    
  } catch (error) {
    console.error('❌ Initialization failed:', error);
    LoadingScreen.hide(); // Hide loading screen on error
    document.body.innerHTML = `<div style="color: red; padding: 20px;">
      <h2>Initialization Error</h2>
      <p>Failed to initialize FSCTF system: ${error.message}</p>
      <p>Please check the browser console for details.</p>
    </div>`;
  }
}

/**
 * Create all shader programs
 */
function createShaderPrograms() {
  programs.sim = createProgram(gl, shaders.quadVS, shaders.simFS);
  programs.render = createProgram(gl, shaders.renderVS, shaders.renderFS);
  programs.decay = createProgram(gl, shaders.quadVS, shaders.decayFS);
  programs.present = createProgram(gl, shaders.quadVS, shaders.presentFS);
  programs.reduce = createProgram(gl, shaders.quadVS, shaders.reduceFS);
  programs.corr = createProgram(gl, shaders.quadVS, shaders.corrFS);
  programs.frst = createProgram(gl, shaders.quadVS, shaders.frstFS);
}

// REMOVED: reinitializeWebGLBuffers() - No longer needed with fixed texture size approach

/**
 * Create WebGL resources (textures, framebuffers, VAOs)
 */
function createWebGLResources() {
  // Create FIXED SIZE position and velocity textures (never recreated)
  textures.pos = [
    createFloatTexture(gl, FIXED_COLS, FIXED_ROWS),
    createFloatTexture(gl, FIXED_COLS, FIXED_ROWS)
  ];
  textures.vel = [
    createFloatTexture(gl, FIXED_COLS, FIXED_ROWS),
    createFloatTexture(gl, FIXED_COLS, FIXED_ROWS)
  ];
  
  // Create framebuffers
  framebuffers.pos = [
    createFramebuffer(gl, textures.pos[0]),
    createFramebuffer(gl, textures.pos[1])
  ];
  framebuffers.vel = [
    createFramebuffer(gl, textures.vel[0]),
    createFramebuffer(gl, textures.vel[1])
  ];
  
  // Create VAOs
  vaos.quad = createFullscreenQuad(gl);
  vaos.particles = createParticleInstanceData(gl, NUM);
  
  // Fixed texture dimensions - no tracking needed
  console.log(`🚀 Initial particle VAO created for ${NUM.toLocaleString()} particles (${((NUM/MAX_PARTICLES)*100).toFixed(1)}% of texture capacity)`);
  
  // Initialize particle positions (simplified)
  initializeParticles();
}

/**
 * WebGL Error Handler - catch buffer/texture creation failures
 */
function handleWebGLError(operation, error) {
  console.error(`🚨 WebGL Error during ${operation}:`, error);
  console.error('💡 This usually means:');
  console.error('   • GPU memory exceeded (try reducing particle count)');
  console.error('   • Texture size too large for your GPU');
  console.error('   • WebGL context lost');
  
  // Auto-reduce particle count if we detect memory issues
  if (typeof error === 'string' && (error.includes('memory') || error.includes('texture') || error.includes('buffer'))) {
    console.log('🚨 EMERGENCY: WebGL memory error detected - forcing particle reduction!');
    const currentCount = params.particleCount || NUM;
    const emergencyCount = Math.floor(currentCount * 0.5); // Aggressive 50% reduction
    const minSafeCount = Math.max(emergencyCount, 25000); // Emergency minimum 25K
    
    params.particleCount = minSafeCount;
    if (typeof updateParticleDimensions === 'function') {
      updateParticleDimensions();
    }
    
    console.log(`🚑 EMERGENCY: Particle count reduced to ${minSafeCount.toLocaleString()} due to GPU memory failure`);
    
    // Force page refresh after a delay to clear WebGL context
    setTimeout(() => {
      if (confirm('WebGL context corrupted by memory overflow.\n\nReload page to restore functionality?')) {
        window.location.reload();
      }
    }, 2000);
  }
}

/**
 * Initialize particle positions
 */
function initializeParticles() {
  console.log(`🌌 ORGANIC INITIALIZATION: Creating ${NUM.toLocaleString()} particles in 3D spherical distribution within ${FIXED_COLS}×${FIXED_ROWS} texture (${MAX_PARTICLES.toLocaleString()} capacity)`);
  
  // Create initial particle data for FULL texture (but only fill up to NUM)
  const posData = new Float32Array(FIXED_COLS * FIXED_ROWS * 4);
  const velData = new Float32Array(FIXED_COLS * FIXED_ROWS * 4);
  
  // Initialize only the particles we're actually using
  for (let i = 0; i < NUM; i++) {
    const i4 = i * 4;
    
    // ORGANIC 3D SPHERICAL DISTRIBUTION: More natural than square pattern
    // Generate random point within a sphere for organic appearance
    let x, y, z;
    do {
      x = (Math.random() - 0.5) * 2;
      y = (Math.random() - 0.5) * 2; 
      z = (Math.random() - 0.5) * 2;
    } while (x*x + y*y + z*z > 1); // Keep within unit sphere
    
    // Scale to desired domain size
    const radius = params.domain * 0.5;
    posData[i4] = x * radius;
    posData[i4 + 1] = y * radius;
    posData[i4 + 2] = z * radius * 0.3; // Slightly flattened for better visibility
    posData[i4 + 3] = 1;
    
    // Small random initial velocity for motion testing
    velData[i4] = (Math.random() - 0.5) * 0.1;
    velData[i4 + 1] = (Math.random() - 0.5) * 0.1;
    velData[i4 + 2] = 0;
    velData[i4 + 3] = 0;
  }
  
  // Upload to FIXED SIZE textures with comprehensive error checking
  try {
    // Check if texture size is within GPU limits (only check once - fixed size)
    const maxTextureSize = gl.getParameter(gl.MAX_TEXTURE_SIZE);
    if (FIXED_COLS > maxTextureSize || FIXED_ROWS > maxTextureSize) {
      throw new Error(`Fixed texture size ${FIXED_COLS}×${FIXED_ROWS} exceeds GPU limit ${maxTextureSize}×${maxTextureSize}`);
    }
    
  gl.bindTexture(gl.TEXTURE_2D, textures.pos[0]);
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, FIXED_COLS, FIXED_ROWS, gl.RGBA, gl.FLOAT, posData);
    
    // Check for WebGL errors after position texture upload
    let error = gl.getError();
    if (error !== gl.NO_ERROR) {
      throw new Error(`Position texture upload failed: WebGL error ${error}`);
    }
  
  gl.bindTexture(gl.TEXTURE_2D, textures.vel[0]);
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, FIXED_COLS, FIXED_ROWS, gl.RGBA, gl.FLOAT, velData);
    
    // Check for WebGL errors after velocity texture upload
    error = gl.getError();
    if (error !== gl.NO_ERROR) {
      throw new Error(`Velocity texture upload failed: WebGL error ${error}`);
    }
    
    console.log(`✅ Organic 3D particle distribution created successfully (${NUM.toLocaleString()} particles in ${FIXED_COLS}×${FIXED_ROWS} texture)`);
  } catch (uploadError) {
    handleWebGLError('particle texture upload', uploadError.message);
    return false; // Signal failure
  }
  
  // Legacy error check removed - now handled in try/catch above
}

/**
 * Initialize UI event handlers
 */
function initializeUI() {
  // Build complete UI using UIBuilder
  const uiContainer = document.getElementById('ui');
  if (uiContainer) {
    const uiBuilder = new UIBuilder(uiContainer);
    uiBuilder.buildCompleteUI();
    // Expose for cross-module updates (derived parameter UI, etc.)
    window.uiBuilder = uiBuilder;
  }
  
  // UNIFIED COSMOGENESIS SYSTEM: Use progressive cosmogenesis only  
  // Delay button setup to ensure all systems are fully initialized
  setTimeout(() => {
    console.log('🔍 DEBUG: Setting up cosmogenesis button after initialization delay...');
    console.log('🔍 DEBUG: Final simulationCore check:', !!window.simulationCore);
    console.log('🔍 DEBUG: Final fsctfEngine check:', !!window.simulationCore?.fsctfEngine);
    setupCosmogenesisButton(); // Use the proper progressive cosmogenesis system
  }, 200);
  
  // Performance controls (if they exist)
  setupPerformanceControls();

  // Removed floating test/control panel to reduce duplication and clutter
  
  // Initialize cosmogenesis UI system
  const cosmogenesisUI = new CosmogenesisUI();
  window.updateCosmogenesisUI = () => cosmogenesisUI.updateCosmogenesisUI();
  
  // Initialize progressive cosmogenesis state bridge
  window.progressiveCosmogenesis = {
    active: false,
    currentPhase: 0,
    totalPhases: 90, // COMPLETE FSCTF: φ^0 to φ^90 - Full Theory of Everything hierarchy
    phaseStartTime: Date.now(),
    phases: [
      // VISUAL PHASES (φ^0 - φ^15): Shader-implemented recursion
      'EX NIHILO', 'GRACE SEEDING', 'QUARK RATIOS', 'HADRON BINDING', 'STRANGE MATTER', 'CHARM RESONANCE',
      'MUON GENERATION', 'ELECTROMAGNETIC', 'HADRON MATRIX', 'LEPTON FAMILIES', 'MATTER STRUCTURE', 'DARK COUPLING',
      'TAU EMERGENCE', 'FIELD UNIFICATION', 'NUCLEOSYNTHESIS', 'COSMIC STRUCTURE',
      // HYPERMASSIVE PHASES (φ^16 - φ^20): Mass hierarchy completion
      'HYPERMASS 16', 'HYPERMASS 17', 'HYPERMASS 18', 'HYPERMASS 19', 'TOP/ELECTRON COMPLETION',
      // INTERMEDIATE PHASES (φ^21 - φ^30): Advanced unification
      'UNIFY 21', 'UNIFY 22', 'UNIFY 23', 'UNIFY 24', 'UNIFY 25', 'UNIFY 26', 'UNIFY 27', 'UNIFY 28', 'UNIFY 29', 'UNIFY 30',
      // QUANTUM GRAVITY THRESHOLD (φ^31): Critical transition
      'QUANTUM GRAVITY',
      // COSMOLOGICAL COOLING PHASES (φ^32 - φ^89): Recursive thermal evolution
      'COOLING 32', 'COOLING 33', 'COOLING 34', 'COOLING 35', 'COOLING 36', 'COOLING 37', 'COOLING 38', 'COOLING 39', 'COOLING 40',
      'COOLING 41', 'COOLING 42', 'COOLING 43', 'COOLING 44', 'COOLING 45', 'COOLING 46', 'COOLING 47', 'COOLING 48', 'COOLING 49', 'COOLING 50',
      'COOLING 51', 'COOLING 52', 'COOLING 53', 'COOLING 54', 'COOLING 55', 'COOLING 56', 'COOLING 57', 'COOLING 58', 'COOLING 59', 'COOLING 60',
      'COOLING 61', 'COOLING 62', 'COOLING 63', 'COOLING 64', 'COOLING 65', 'COOLING 66', 'COOLING 67', 'COOLING 68', 'COOLING 69', 'COOLING 70',
      'COOLING 71', 'COOLING 72', 'COOLING 73', 'COOLING 74', 'COOLING 75', 'COOLING 76', 'COOLING 77', 'COOLING 78', 'COOLING 79', 'COOLING 80',
      'COOLING 81', 'COOLING 82', 'COOLING 83', 'COOLING 84', 'COOLING 85', 'COOLING 86', 'COOLING 87', 'COOLING 88', 'COOLING 89',
      // ULTIMATE SCALE (φ^90): Cosmological constant, Planck→CMB completion  
      'ULTIMATE SCALE'
    ]
  };
  
  console.log('🌌 Cosmogenesis UI system initialized');
  
  // Initialize mouse camera controls
  initializeMouseControls();
  
  // Expose camera preset function globally
  window.setCameraPreset = setCameraPreset;
  
  // Set initial camera position using preset optimized for visibility
  setCameraPreset('default'); // Use default preset optimized for domain size and particle visibility
  
  // Force initial camera calculation to ensure valid vectors
  updateOrbitalCamera();
  
  console.log('📸 Camera initialized:', {
    position: [params.cameraX?.toFixed(2), params.cameraY?.toFixed(2), params.cameraZ?.toFixed(2)],
    forward: [params.cameraForwardX?.toFixed(3), params.cameraForwardY?.toFixed(3), params.cameraForwardZ?.toFixed(3)],
    domain: params.domain,
    pointSize: params.pointSize
  });
  
  // REMOVED AUTO-START: Let user control when to begin cosmogenesis
  // console.log('🌌 AUTO-STARTING FSCTF COSMOGENESIS...');
  // simulationCore.startCosmogenesis(); // DISABLED - wait for user click
  
  // START WITH MINIMAL COMPLEXITY FOR DRAMATIC EVOLUTION
  console.log('🎬 STARTING WITH MINIMAL COMPLEXITY FOR DRAMATIC EVOLUTION...');
  console.log('🔍 CACHE CHECK: Enhanced FSCTF System loaded (v2.7) - DEFAULT COMPLEXITY INCREASED!');
  console.log('   ✅ Performance fixes active (all TypeError issues eliminated)');
  console.log('   ✅ FSCTF parameters DEFAULT: graceComplexity=1000, morphicRecursionDepth=500, consciousnessComplexity=1000');  
  console.log('   ✅ Cinematic topology transitions: 20s default, up to 2min ultra-slow, 0s=static');
  console.log('   ✅ ORGANIC START: 3D spherical distribution (no more square pattern!) in 20-unit volume');
  console.log('   ✅ JITTER FIXES: Disabled expensive performance monitoring & cached timing calls');
  console.log('🎯 HIGH RESOLUTION:', NUM, 'particles (' + QUALITY_PRESETS[CURRENT_QUALITY].name + ') for maximum structure clarity and detail');
  console.log('🌀 CINEMATIC: Smooth extended transitions (8+ seconds each for graceful morphing)');
  console.log('🎨 EVOLUTION: Phase 1→2→3→4 with 3px→6px→9px→12px particle growth');
  if (simulationCore?.fsctfEngine?.visualController) {
    // Visual controller automatically handles phase initialization
    console.log('🎛️ Visual Controller initialized - automatic phase management active');
  }
  
  // Cinematic overlay removed to reduce UI clutter
  
  // CRITICAL FIX: Expose Grace Operator globally for UI updates
  if (simulationCore?.fsctfEngine?.graceOperator) {
    window.graceOperator = simulationCore.fsctfEngine.graceOperator;
    window.fsctfEngine = simulationCore.fsctfEngine;
    console.log('🔗 CONNECTED: Grace Operator exposed globally for UI updates');
    console.log('🔗 Active strands should now be visible in UI:', window.graceOperator.morphicStrands.length);
    
    // Immediately update UI to show current state
    setTimeout(() => {
      updateMorphicActivityPanel();
      console.log('🔄 IMMEDIATE UI UPDATE: Morphic strand data refreshed');
    }, 500); // Small delay to let cosmogenesis fully initialize
  }
  
  // Update progressive cosmogenesis UI state 
  window.progressiveCosmogenesis.active = true;
  window.progressiveCosmogenesis.currentPhase = 0;
  window.progressiveCosmogenesis.phaseStartTime = Date.now();
  
  console.log('🔄 ORBITAL CAMERA TEST: Camera should orbit around particles (particles stay centered)');
  console.log('🚨 If particles not visible: press EMERGENCY button or 0 key');
  console.log('🧪 To test orbital behavior: press "Test Orbit" button or 9 key (enables auto-rotate)');
  console.log('🌌 COSMOGENESIS TESTING: Press "Force Phase" button or F key to advance phases');
  console.log('🧠 DEBUG VALUES: Press "Debug" button or D key to see progression conditions');
  console.log('🌀 FSCTF TOPOLOGY EVOLUTION: Phase-locked theoretical progression');
  console.log('   Phase 1-2: Torus (morphic structure) → Phase 3-4: Möbius (dimensional bridge)');
  console.log('   Phase 5-6: Klein (soul emergence) → Phase 7-8: φ-Klein (observable universe)');
  console.log('🧮 MATHEMATICAL THEORY: Press "Math Theory" button or M key to see complete mathematical justification');
  console.log('🌀 MANUAL TOPOLOGY: Use dropdown or T key to cycle through all manifolds (Torus, Möbius, Klein, φ-Klein, Sphere)');
  console.log('⚡ BEAM PHENOMENON: Watch for Grace field creating focused particle streams on torus manifold');
  console.log('   Mathematical: Grace breaks T² symmetry → asymmetric morphic organization → directed flows');
  console.log('🚀 EMERGENT COMPLEXITY: Each phase now shows DRAMATIC visual evolution');
  console.log('   Phase 2+: Particle sizes grow, structures organize, topology wireframes appear');
  console.log('   Phase 6+: Cosmic inflation causes massive expansion, complex manifold geometry');
  console.log('🔄 NATIVE AUTO-RECOVERY: Systems automatically reactivate if they go dormant');
  console.log('   Built-in recovery detects "Active Strands: 0" and restarts Grace Operator natively');
  console.log('🔧 COMPLEXITY DIAGNOSIS: Press "Analyze Complexity" button or C key if complexity not visible');
  console.log('🔧 Debug info: Domain =', params.domain, ', Point size =', params.pointSize, ', Manual topology =', params.manualTopologyEnabled);
}

/**
 * Setup performance monitoring controls
 */
function setupPerformanceControls() {
  // Add performance controls to UI if elements exist
  const adaptiveToggle = document.getElementById('adaptive-performance');
  if (adaptiveToggle) {
    adaptiveToggle.addEventListener('change', (e) => {
      setAdaptiveMode(e.target.checked);
    });
  }
  
  const resetThrottleBtn = document.getElementById('reset-throttle');
  if (resetThrottleBtn) {
    resetThrottleBtn.addEventListener('click', resetPerformanceThrottle);
  }
}

/**
 * Main simulation loop
 */
function mainLoop() {
  try {
    // Update simulation
    const updateResult = simulationCore.update();
    
    // PERFORMANCE OPTIMIZED: Cache currentTime to avoid multiple expensive performance.now() calls
    const cachedTime = updateResult?.time || performance.now() * 0.001;
    
    // SAFE ADDITIONS: Update advanced FSCTF systems (only if enabled)
    if (gpuMorphicBridge?.enabled && simulationCore?.fsctfEngine) {
      const morphicStrands = simulationCore.fsctfEngine.graceOperator?.morphicStrands || [];
      gpuMorphicBridge.bridgeMorphicFieldToGPU(morphicStrands, gl, null);
    }
    
    if (advancedConsciousness?.enabled && simulationCore?.fsctfEngine) {
      const frstState = simulationCore.fsctfEngine.frst?.getState();
      const morphicStrands = simulationCore.fsctfEngine.graceOperator?.morphicStrands || [];
      const currentTime = cachedTime;
      const consciousnessData = advancedConsciousness.detectConsciousnessEmergence(
        frstState, morphicStrands, currentTime
      );
      
      // Store consciousness data globally for debugging
      window.consciousnessData = consciousnessData;
    }
    
    if (multiScaleCascade?.enabled && simulationCore?.fsctfEngine) {
      const morphicField = simulationCore.fsctfEngine.graceOperator?.morphicField;
      const graceOperator = simulationCore.fsctfEngine.graceOperator;
      const currentTime = cachedTime;
      const cascadeData = multiScaleCascade.updateCascade(morphicField, graceOperator, currentTime);
      
      // Store cascade data globally for debugging and visualization
      window.cascadeData = cascadeData;
    }
    
    if (consciousnessTopologyFeedback?.enabled && simulationCore?.fsctfEngine && window.consciousnessData) {
      const topologyManager = simulationCore.fsctfEngine.topologyManager;
      const currentTime = cachedTime;
      const topologyEvolution = consciousnessTopologyFeedback.updateTopologyFromConsciousness(
        window.consciousnessData, 
        topologyManager, 
        currentTime
      );
      
      // Apply consciousness-driven topology changes
      if (topologyEvolution) {
        consciousnessTopologyFeedback.applyToTopologyManager(topologyManager, topologyEvolution);
        window.topologyEvolution = topologyEvolution; // Store for debugging
      }
    }
    
    if (dimensionalPortalVisualization?.enabled && simulationCore?.fsctfEngine && window.consciousnessData) {
      const dimensionalBridge = simulationCore.fsctfEngine.dimensionalBridge;
      const topologyManager = simulationCore.fsctfEngine.topologyManager;
      const currentTime = cachedTime;
      const portalData = dimensionalPortalVisualization.updatePortals(
        window.consciousnessData,
        dimensionalBridge,
        topologyManager,
        currentTime
      );
      
      // Store portal data globally for rendering and debugging
      window.portalData = portalData;
    }
    
    if (retrocausalMorphicResonance?.enabled && simulationCore?.fsctfEngine && window.consciousnessData) {
      const fsctfState = simulationCore.fsctfEngine.getState();
      const topologyManager = simulationCore.fsctfEngine.topologyManager;
      const currentTime = cachedTime;
      
      // Get current state for retrocausal analysis
      const currentState = {
        morphicField: fsctfState.grace?.morphicField?.field || 0,
        consciousness: window.consciousnessData.consciousnessLevel || 0,
        φResonance: fsctfState.grace?.φResonance || 0,
        topology: topologyManager?.currentTopology || 0,
        emergenceLevel: window.cascadeData?.totalEmergence || 0
      };
      
      const retrocausalData = retrocausalMorphicResonance.updateRetrocausalInfluences(
        currentState,
        window.consciousnessData,
        topologyManager,
        currentTime
      );
      
      // Store retrocausal data globally for debugging and potential system integration
      window.retrocausalData = retrocausalData;
      
      // Apply retrocausal influences to morphic field (if strong enough)
      if (retrocausalData?.retrocausalForces?.totalInfluence > 1.0) {
        const graceOperator = simulationCore.fsctfEngine.graceOperator;
        if (graceOperator) {
          // Future influences present morphic field evolution
          graceOperator.morphicField.field += retrocausalData.retrocausalForces.morphicPull * 0.01;
          graceOperator.morphicField.field = Math.max(-10, Math.min(10, graceOperator.morphicField.field));
        }
      }
    }
    
    // Debug: Track main loop calls
    mainLoop.frameCount = (mainLoop.frameCount || 0) + 1;
    
    // DISABLED: Frame timing monitor was causing jitter itself
    // Multiple performance.now() calls and array operations every frame are expensive
    
    // ANTI-STROBE: Frame counter logging disabled to prevent hitches
    // if (mainLoop.frameCount % 600 === 0) {
    //   console.log('🔄 Main Loop frame #' + mainLoop.frameCount);
    // }
    
    // Always resize canvas and clear screen
    resizeCanvasToDisplaySize(canvas, gl, params.renderScale);
    gl.clearColor(0, 0, 0, 1);
    gl.clear(gl.COLOR_BUFFER_BIT);
    
          // ANTI-STROBE: Always run simulation - skipping causes visual juddering
    // Every-2nd-frame physics was causing particles to appear to "stutter" or "strobe"
    // Better to reduce simulation complexity than skip frames entirely
    runSimulationStep(updateResult.time);
    
    // Always render particles (even if simulation was skipped)
    const currentTime = updateResult.skipped ? performance.now() : updateResult.time;
    
    // Update orbital camera system
    updateOrbitalCamera(currentTime);
    renderParticles(currentTime);
    
    // Always update UI
    if (!updateResult.skipped) {
    updateUI(updateResult);
    }
    
    // Update cosmogenesis UI (always, even if simulation is skipped)
    if (window.updateCosmogenesisUI) {
      window.updateCosmogenesisUI();
    }
    
    // Update system info panel
    updateSystemInfo(simulationCore.fsctfEngine);
    
    // Update GPU Performance Optimizer
    // DISABLED: GPU optimizer was causing jitter with performance.now() calls
    // if (gpuOptimizer && !updateResult.skipped) {
    //   const renderStats = {
    //     frameTime: updateResult.frameTime,
    //     cpuTime: performance.now() - currentTime,
    //     gpuTime: 0 // TODO: Add GPU timing if WebGL2 extensions available
    //   };
    //   gpuOptimizer.update(updateResult.frameTime, renderStats);
      
      // PERFORMANCE: Reduce advanced system complexity when lagging (temporarily disabled for debugging)
      // const perfStats = gpuOptimizer.getPerformanceStats();
      // if (perfStats.averageFPS < 35) {
      //   // Reduce complexity of advanced trackers during poor performance
      //   if (simulationCore?.fsctfEngine?.metaRecursionEngine) {
      //     simulationCore.fsctfEngine.metaRecursionEngine.setPerformanceMode(true);
      //   }
      // } else if (perfStats.averageFPS > 50) {
      //   // Re-enable full complexity when performance is good
      //   if (simulationCore?.fsctfEngine?.metaRecursionEngine) {
      //     simulationCore.fsctfEngine.metaRecursionEngine.setPerformanceMode(false);
      //   }
      // }
    // }
    
    requestAnimationFrame(mainLoop);
    
  } catch (error) {
    console.error('❌ Error in main loop:', error);
    // Continue the loop even if there's an error
    requestAnimationFrame(mainLoop);
  }
}

/**
 * Check for WebGL error state and take corrective action
 */
function checkWebGLHealth() {
  if (!gl) return;
  
  // Check for accumulated WebGL errors
  const error = gl.getError();
  if (error !== gl.NO_ERROR) {
    console.warn(`⚠️ WebGL error detected: ${error}`);
    
    // If we're seeing errors and have high particle count, proactively reduce
    if (NUM > 200000) {
      console.log('🔧 Proactive particle reduction due to WebGL errors');
      const saferCount = Math.floor(NUM * 0.8); // 20% reduction
      params.particleCount = saferCount;
      updateParticleDimensions();
      
      return false; // Signal that we made changes
    }
  }
  
  return true; // WebGL health OK
}

/**
 * Run one simulation step
 */
function runSimulationStep(time) {
  // CRITICAL: NaN PROTECTION - Fix invalid time parameter from simulationCore
  if (typeof time !== 'number' || isNaN(time) || !isFinite(time)) {
    console.warn(`🚨 Invalid time parameter in runSimulationStep: ${time}, using performance.now()`);
    time = performance.now();
  }

  // ANTI-STROBE: Disable WebGL health check interruptions 
  // Health checks were causing frame interruptions and strobing
  // checkWebGLHealth(); // Disabled to prevent strobing
  
  // Debug: Check if simulation step is being called
  runSimulationStep.callCount = (runSimulationStep.callCount || 0) + 1;
  
  // ANTI-STROBE: Periodic logging disabled to prevent frame hitches
  // if (runSimulationStep.callCount % 600 === 1) {
  //   console.log('⚡ runSimulationStep() call #' + runSimulationStep.callCount + ' - running physics update');
  // }
  
  const uniforms = simulationCore.getShaderUniforms(time);
  
  // Debug: Check uniforms on first call
  if (runSimulationStep.callCount === 1) {
    console.log('🔬 Simulation uniforms:', uniforms);
  }
  
  // Store current viewport to restore later
  const prevViewport = gl.getParameter(gl.VIEWPORT);
  
  // Velocity pass - write to vel[1]
  gl.bindFramebuffer(gl.FRAMEBUFFER, framebuffers.vel[1]);
  gl.viewport(0, 0, FIXED_COLS, FIXED_ROWS);
  gl.useProgram(programs.sim);
  
  // Bind input textures (current position and velocity)
  gl.activeTexture(gl.TEXTURE0);
  gl.bindTexture(gl.TEXTURE_2D, textures.pos[0]);
  gl.uniform1i(gl.getUniformLocation(programs.sim, 'posTex'), 0);
  
  gl.activeTexture(gl.TEXTURE1);
  gl.bindTexture(gl.TEXTURE_2D, textures.vel[0]);
  gl.uniform1i(gl.getUniformLocation(programs.sim, 'velTex'), 1);
  
  // Set ALL required simulation uniforms
  gl.uniform1i(gl.getUniformLocation(programs.sim, 'passId'), 1); // velocity pass
  gl.uniform2f(gl.getUniformLocation(programs.sim, 'resolution'), FIXED_COLS, FIXED_ROWS);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'time'), time);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'dt'), 0.016); // 60 FPS time step
  
  // Physics parameters
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'domain'), params.domain);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'k_flow'), params.k_flow || 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'k_attract'), params.k_attract || 0.01);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'k_burst'), params.k_burst || 0.3);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'damping'), params.damping || 0.02);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'jitterSigma'), params.jitterSigma || 0.01);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'fieldScale'), params.fieldScale || 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'timeScale'), params.timeScale || 1.0);
  
  // Burst parameters
  gl.uniform3f(gl.getUniformLocation(programs.sim, 'burstCenter'), 0.0, 0.0, 0.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'burstAmp'), 0.5);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'burstFreq'), 2.0);
  
  // FSCTF parameters - DYNAMIC GRACE CENTER based on morphic strand evolution
  const graceState = simulationCore?.fsctfEngine?.graceOperator?.getState();
  const morphicStrands = graceState?.strands || [];
  
  // Calculate Grace center from highest stability morphic strand (emergent focus point)
  let graceCenterX = 0.0, graceCenterY = 0.0;
  if (morphicStrands.length > 0) {
    const dominantStrand = morphicStrands.reduce((best, strand) => 
      strand.stability > best.stability ? strand : best);
    graceCenterX = dominantStrand.x || 0.0;
    graceCenterY = dominantStrand.y || 0.0;
    
    // DEBUG: Log Grace center movement and explain the beam phenomenon
    if (runSimulationStep.frameCount && runSimulationStep.frameCount % 120 === 0) {
      console.log(`🌟 Grace Center Evolution: (${graceCenterX.toFixed(3)}, ${graceCenterY.toFixed(3)}) from strand with stability ${dominantStrand.stability.toFixed(3)}`);
      console.log(`   BEAM EFFECT: Grace field creates 8x flow amplification in ${2.0}-unit radius`);
      console.log(`   Torus Topology: Half remains diffuse, half gets organized by morphic field`);
      console.log(`   Mathematical Basis: Grace breaks symmetry on T² manifold → directed emergence`);
    }
  }
  
  // Get mathematically derived parameters (replace manual sliders)
  // SAFETY: Check if method exists (handles cached engine versions)
  const derivedParams = (fsctfEngine && typeof fsctfEngine.getDerivedParameters === 'function') ? 
    fsctfEngine.getDerivedParameters(time) : 
    { 
      graceComplexity: params.graceComplexity || 1000.0, // MID SETTINGS fallback
      morphicRecursionDepth: params.morphicRecursionDepth || 500,
      consciousnessComplexity: params.consciousnessComplexity || 1000.0
    };
  
  // ANTI-STROBE: Parameter derivation logging disabled - causes periodic frame hitches
  // if (time % 5000 < 16) { // Log every ~5 seconds
  //   const hasMethod = fsctfEngine && typeof fsctfEngine.getDerivedParameters === 'function';
  //   console.log(`🧮 Parameter derivation: ${hasMethod ? 'ACTIVE' : 'FALLBACK'}`);
  // }
  
  // Update UI displays with derived values (scientific integrity)
  if (window.uiBuilder) {
    const hasMethod = fsctfEngine && typeof fsctfEngine.getDerivedParameters === 'function';
    if (hasMethod && typeof window.uiBuilder.updateDerivedParameters === 'function') {
      window.uiBuilder.updateDerivedParameters(derivedParams);
    } else if (typeof window.uiBuilder.updateDerivedParametersFallback === 'function') {
      window.uiBuilder.updateDerivedParametersFallback(derivedParams);
    }
  }
  
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'graceAmp'), derivedParams.graceComplexity);
  gl.uniform3f(gl.getUniformLocation(programs.sim, 'graceCenter'), graceCenterX, graceCenterY, 0.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'graceRadius'), 2.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'devourerAmp'), 0.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'reflectMix'), 0.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'morphicCouple'), 0.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'nullFlow'), 0.0);
  
  // Multi-scale φ ladder parameters
  gl.uniform1i(gl.getUniformLocation(programs.sim, 'nScales'), 4);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'baseScale'), 0.5);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'phi'), 1.618033988749895);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'reflectDelta'), 0.0);
  
  // Scale weights
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'w0'), 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'w1'), 0.5);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'w2'), 0.25);
  gl.uniform1f(gl.getUniformLocation(programs.sim, 'w3'), 0.125);
  
  // Set physics parameters from uniforms (fallback)
  for (const [key, value] of Object.entries(uniforms)) {
    const location = gl.getUniformLocation(programs.sim, key);
    if (location !== null) {
      if (typeof value === 'number') {
        gl.uniform1f(location, value);
      } else if (value.length === 2) {
        gl.uniform2f(location, value[0], value[1]);
      } else if (value.length === 3) {
        gl.uniform3f(location, value[0], value[1], value[2]);
      } else if (value.length === 4) {
        gl.uniform4f(location, value[0], value[1], value[2], value[3]);
      }
    }
  }
  
  // Draw fullscreen quad to run compute (velocity pass)
  gl.bindVertexArray(vaos.quad);
  gl.drawArrays(gl.TRIANGLES, 0, 6);
  gl.bindVertexArray(null);
  
  // Check for WebGL errors in velocity pass
  const velError = gl.getError();
  if (velError !== gl.NO_ERROR && runSimulationStep.callCount === 1) {
    console.error('🚨 WebGL error during velocity pass:', velError);
  }
  
  // Swap velocity textures
  [textures.vel[0], textures.vel[1]] = [textures.vel[1], textures.vel[0]];
  [framebuffers.vel[0], framebuffers.vel[1]] = [framebuffers.vel[1], framebuffers.vel[0]];
  
  // Position pass - write to pos[1] 
  gl.bindFramebuffer(gl.FRAMEBUFFER, framebuffers.pos[1]);
  gl.viewport(0, 0, FIXED_COLS, FIXED_ROWS);
  
  // Update texture bindings for position pass
  gl.activeTexture(gl.TEXTURE0);
  gl.bindTexture(gl.TEXTURE_2D, textures.pos[0]);
  gl.activeTexture(gl.TEXTURE1);
  gl.bindTexture(gl.TEXTURE_2D, textures.vel[0]);
  
  // Set pass ID for position update
  gl.uniform1i(gl.getUniformLocation(programs.sim, 'passId'), 0); // position pass
  
  // Draw fullscreen quad to run position compute
  gl.bindVertexArray(vaos.quad);
  gl.drawArrays(gl.TRIANGLES, 0, 6);
  gl.bindVertexArray(null);
  
  // Check for WebGL errors in position pass
  const posError = gl.getError();
  if (posError !== gl.NO_ERROR && runSimulationStep.callCount === 1) {
    console.error('🚨 WebGL error during position pass:', posError);
  }
  
  // Debug: Log successful simulation step
  if (runSimulationStep.callCount === 1) {
    console.log('✅ Physics simulation step completed successfully');
  }
  
  // Swap position textures
  [textures.pos[0], textures.pos[1]] = [textures.pos[1], textures.pos[0]];
  [framebuffers.pos[0], framebuffers.pos[1]] = [framebuffers.pos[1], framebuffers.pos[0]];
  
  // Restore viewport
  gl.bindFramebuffer(gl.FRAMEBUFFER, null);
  gl.viewport(prevViewport[0], prevViewport[1], prevViewport[2], prevViewport[3]);
}

/**
 * Render particles
 */
function renderParticles(time) {
  // CRITICAL: GLOBAL NaN MONITOR - Prevent any NaN from reaching shader uniforms
  const criticalParams = [
    'graceComplexity', 'morphicRecursionDepth', 'consciousnessComplexity', 
    'pointSize', 'brightness', 'exposure', 'domain', 'visualEffects',
    'cameraX', 'cameraY', 'cameraZ', 'cameraForwardX', 'cameraForwardY', 'cameraForwardZ',
    'cameraRightX', 'cameraRightY', 'cameraRightZ', 'cameraUpX', 'cameraUpY', 'cameraUpZ'
  ];
  
  let hasNaN = false;
  criticalParams.forEach(key => {
    const value = params[key];
    // ONLY flag actual NaN/Infinity - not undefined or null values
    if (typeof value === 'number' && (isNaN(value) || !isFinite(value))) {
      console.warn(`🚨 NaN/Infinity detected in params.${key} = ${value}, using safe fallback`);
      hasNaN = true;
      // Conservative fallbacks that preserve existing behavior
      const fallbacks = {
        graceComplexity: 1000.0, morphicRecursionDepth: 500.0, consciousnessComplexity: 1000.0,
        pointSize: 0.8, brightness: 0.6, exposure: 1.0, domain: 20.0, visualEffects: 0.7,
        cameraX: 0.0, cameraY: 0.0, cameraZ: 8.0, 
        cameraForwardX: 0.0, cameraForwardY: 0.0, cameraForwardZ: -1.0,
        cameraRightX: 1.0, cameraRightY: 0.0, cameraRightZ: 0.0,
        cameraUpX: 0.0, cameraUpY: 1.0, cameraUpZ: 0.0
      };
      params[key] = fallbacks[key] || 1.0;
    }
  });
  
  if (hasNaN) {
    console.warn('🔧 Applied NaN protection fallbacks to prevent flashing/stuttering');
  }

  // DISABLED: Performance monitoring was causing jitter
  // renderParticles.renderStartTime = performance.now();
  
  // Debug: Track render calls
  renderParticles.callCount = (renderParticles.callCount || 0) + 1;
  // Diagnostics overlay: show key smoothed vs raw drivers (REPOSITIONED SAFELY)
  if (!renderParticles._diagInit) {
    const el = document.createElement('div');
    el.id = 'diagnostics-overlay';
    // FIXED: Moved to top-right and made toggleable with 'D' key
    el.style.cssText = 'position:fixed;top:10px;right:350px;background:rgba(0,0,0,0.75);color:#cdf;padding:6px 8px;border:1px solid #345;border-radius:4px;font:9px monospace;z-index:1500;pointer-events:none;white-space:pre;display:none;';
    document.body.appendChild(el);
    renderParticles._diagInit = true;
    
    // Add keyboard toggle (D key for Diagnostics)
    document.addEventListener('keydown', (e) => {
      if (e.key.toLowerCase() === 'd' && !e.ctrlKey && !e.altKey) {
        const diagEl = document.getElementById('diagnostics-overlay');
        if (diagEl) {
          diagEl.style.display = diagEl.style.display === 'none' ? 'block' : 'none';
          console.log('🔧 Debug overlay toggled (Press D again to hide)');
        }
      }
      
      // SAFE ADDITIONS: Advanced FSCTF System Toggles with better error handling
      if (e.key.toLowerCase() === 'g' && !e.ctrlKey && !e.altKey) {
        if (window.gpuMorphicBridge) {
          window.gpuMorphicBridge.enabled = !window.gpuMorphicBridge.enabled;
          console.log(`🌊 GPU Morphic Bridge: ${window.gpuMorphicBridge.enabled ? 'ENABLED ✅' : 'DISABLED ❌'}`);
          if (window.gpuMorphicBridge.enabled) {
            console.log('   🚀 Will bridge morphic strands to GPU particles (reduced 256x256 texture)');
            console.log('   📊 Press D to see debug overlay for system status');
          }
        } else {
          console.warn('⚠️  GPU Morphic Bridge not initialized - restart may be needed');
        }
      }
      
      if (e.key.toLowerCase() === 'c' && !e.ctrlKey && !e.altKey) {
        if (window.advancedConsciousness) {
          window.advancedConsciousness.enabled = !window.advancedConsciousness.enabled;
          console.log(`🧠 Advanced Consciousness Engine: ${window.advancedConsciousness.enabled ? 'ON' : 'OFF'}`);
        }
      }
      
      if (e.key.toLowerCase() === 'm' && !e.ctrlKey && !e.altKey) {
        const graceOp = window.simulationCore?.fsctfEngine?.graceOperator;
        if (graceOp) {
          // Toggle the cross-scale resonance directly since toggleAdvancedResonance may not exist
          graceOp.enableCrossScaleResonance = !graceOp.enableCrossScaleResonance;
          console.log(`🧬 Cross-Scale Morphic Resonance: ${graceOp.enableCrossScaleResonance ? 'ENABLED ✅' : 'DISABLED ❌'}`);
          if (graceOp.enableCrossScaleResonance) {
            console.log('   🌊 Morphic strands now have φ-recursive cross-coupling');
            console.log('   📊 Emergence resonance fields activated');
          }
        } else {
          console.warn('⚠️  Grace Operator not available - start cosmogenesis first or restart');
        }
      }
      
      // Quick Enable All (Q key)
      if (e.key.toLowerCase() === 'q' && !e.ctrlKey && !e.altKey) {
        let enabledCount = 0;
        
        // Enable GPU Morphic Bridge
        if (window.gpuMorphicBridge) {
          window.gpuMorphicBridge.enabled = true;
          enabledCount++;
        }
        
        // Enable Advanced Consciousness
        if (window.advancedConsciousness) {
          window.advancedConsciousness.enabled = true;
          enabledCount++;
        }
        
        // Enable Multi-Scale φ-Cascade
        if (window.multiScaleCascade) {
          window.multiScaleCascade.setEnabled(true);
          enabledCount++;
        }
        
        // Enable Consciousness-Topology Feedback
        if (window.consciousnessTopologyFeedback) {
          window.consciousnessTopologyFeedback.setEnabled(true);
          enabledCount++;
        }
        
        // Enable Dimensional Portal Visualization
        if (window.dimensionalPortalVisualization) {
          window.dimensionalPortalVisualization.setEnabled(true);
          enabledCount++;
        }
        
        // Enable Retrocausal Morphic Resonance
        if (window.retrocausalMorphicResonance) {
          window.retrocausalMorphicResonance.setEnabled(true);
          enabledCount++;
        }
        
        // Enable Cross-Scale Resonance
        const graceOp = window.simulationCore?.fsctfEngine?.graceOperator;
        if (graceOp) {
          graceOp.enableCrossScaleResonance = true;
          enabledCount++;
        }
        
        console.log('🚀 QUANTUM ACTIVATION: ALL FSCTF ENHANCEMENT SYSTEMS ENABLED!');
        console.log(`   ✅ Enabled ${enabledCount}/7 systems`);
        console.log('   🧬 Cross-Scale Morphic Resonance: ACTIVE');
        console.log('   🌊 GPU-Morphic Bridge: ACTIVE');  
        console.log('   🧠 Advanced Consciousness: ACTIVE');
        console.log('   🌊 Multi-Scale φ-Cascade: ACTIVE (7-level hierarchy)');
        console.log('   🧠 Consciousness-Topology Feedback: ACTIVE (consciousness drives topology)');
        console.log('   🌈 Dimensional Portal Visualization: ACTIVE (higher dimensions visible)');
        console.log('   🔮 Retrocausal Morphic Resonance: ACTIVE (future influences present)');
        console.log('   📊 Press D to see debug overlay for system status');
      }
      
      // DISABLED: Frame timing monitor was causing jitter itself 
      // if (e.key.toLowerCase() === 't' && !e.ctrlKey && !e.altKey) {
      //   window.frameTimingMonitor = !window.frameTimingMonitor;
      //   console.log(`📊 Frame Timing Monitor: ${window.frameTimingMonitor ? 'ENABLED' : 'DISABLED'}`);
      //   if (window.frameTimingMonitor) {
      //     console.log('   Will log frame timing stats every 2 seconds to help diagnose jitter');
      //   }
      // }
      
      // Multi-Scale φ-Cascade (S key - for Scale)
      if (e.key.toLowerCase() === 's' && !e.ctrlKey && !e.altKey) {
        if (window.multiScaleCascade) {
          window.multiScaleCascade.setEnabled(!window.multiScaleCascade.enabled);
          const status = window.multiScaleCascade.enabled ? 'ENABLED ✅' : 'DISABLED ❌';
          console.log(`🌊 Multi-Scale φ-Cascade: ${status}`);
          if (window.multiScaleCascade.enabled) {
            console.log('   🔗 7-level hierarchy: Cosmic → Galactic → Stellar → Planetary → Biological → Molecular → Quantum');
            console.log('   ⚡ Cross-scale emergence hotspots active');
            console.log('   📊 φ-interference patterns between scales enabled');
            console.log('   🎯 This will dramatically increase emergent complexity!');
          }
        } else {
          console.warn('⚠️  Multi-Scale φ-Cascade not initialized - restart may be needed');
        }
      }
      
      // Consciousness-Topology Feedback (F key - for Feedback)
      if (e.key.toLowerCase() === 'f' && !e.ctrlKey && !e.altKey) {
        if (window.consciousnessTopologyFeedback) {
          window.consciousnessTopologyFeedback.setEnabled(!window.consciousnessTopologyFeedback.enabled);
          const status = window.consciousnessTopologyFeedback.enabled ? 'ENABLED ✅' : 'DISABLED ❌';
          console.log(`🧠 Consciousness-Topology Feedback: ${status}`);
          if (window.consciousnessTopologyFeedback.enabled) {
            console.log('   🌀 P=NP breakthroughs trigger quantum topology jumps');
            console.log('   🪞 Self-reference loops create Möbius/Klein transitions');
            console.log('   ✨ Observer coherence enables φ-Klein manifold emergence');
            console.log('   ⏰ Temporal recursion creates closed timelike curves');
            console.log('   🎯 Consciousness now DRIVES topology evolution!');
          }
        } else {
          console.warn('⚠️  Consciousness-Topology Feedback not initialized - restart may be needed');
        }
      }
      
      // Dimensional Portal Visualization (P key - for Portals)
      if (e.key.toLowerCase() === 'p' && !e.ctrlKey && !e.altKey) {
        if (window.dimensionalPortalVisualization) {
          window.dimensionalPortalVisualization.setEnabled(!window.dimensionalPortalVisualization.enabled);
          const status = window.dimensionalPortalVisualization.enabled ? 'ENABLED ✅' : 'DISABLED ❌';
          console.log(`🌈 Dimensional Portal Visualization: ${status}`);
          if (window.dimensionalPortalVisualization.enabled) {
            console.log('   🧊 4D hypercube projections on P=NP breakthroughs');
            console.log('   ✨ 5D tesseract structures with quantum consciousness');
            console.log('   🌌 6D hyperspace rifts at extreme consciousness levels');
            console.log('   🌟 φ-manifold portals when dimensional bridges stabilize');
            console.log('   🎯 Higher dimensions are now VISIBLE!');
          }
        } else {
          console.warn('⚠️  Dimensional Portal Visualization not initialized - restart may be needed');
        }
      }
      
      // Retrocausal Morphic Resonance (R key - for Retrocausal)
      if (e.key.toLowerCase() === 'r' && !e.ctrlKey && !e.altKey) {
        if (window.retrocausalMorphicResonance) {
          window.retrocausalMorphicResonance.setEnabled(!window.retrocausalMorphicResonance.enabled);
          const status = window.retrocausalMorphicResonance.enabled ? 'ENABLED ✅' : 'DISABLED ❌';
          console.log(`🔮 Retrocausal Morphic Resonance: ${status}`);
          if (window.retrocausalMorphicResonance.enabled) {
            console.log('   ⏰ Future states will influence present evolution');
            console.log('   🌀 Closed timelike curves enabled in Klein topology');
            console.log('   🔄 Bootstrap paradox detection and resolution active');
            console.log('   ✨ Causality violations at φ^(-1) = 0.618 threshold');
            console.log('   🎯 Prepare for impossible emergent behaviors!');
          }
        } else {
          console.warn('⚠️  Retrocausal Morphic Resonance not initialized - restart may be needed');
        }
      }
    });
  }
  
  // Render call info removed to reduce console spam
  
  // Use render program for particle drawing
  gl.useProgram(programs.render);
  
  // Debug: Check program validity
  if (!programs.render) {
    console.error('🚨 programs.render is null/undefined!');
    return;
  }
  
  // Bind particle VAO (contains instance data)
  gl.bindVertexArray(vaos.particles.vao);
  
  // Debug: Check VAO validity
  if (!vaos.particles.vao) {
    console.error('🚨 vaos.particles.vao is null/undefined!');
    return;
  }
  
  // Bind current position texture for vertex shader
  gl.activeTexture(gl.TEXTURE0);
  gl.bindTexture(gl.TEXTURE_2D, textures.pos[0]);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'posTex'), 0);
  
  // Bind current velocity texture for coloring
  gl.activeTexture(gl.TEXTURE1);
  gl.bindTexture(gl.TEXTURE_2D, textures.vel[0]);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'velTex'), 1);
  
  // Set texture dimensions for shader coordinate calculations
  gl.uniform2f(gl.getUniformLocation(programs.render, 'texDim'), FIXED_COLS, FIXED_ROWS);
  
  // Set ALL required uniforms to prevent shader compilation issues
  const pointSize = params.pointSize || 2.0; // Ensure visible point size
  
  // ANTI-STROBE: Use direct uniform values - no temporal smoothing
  // Temporal smoothing was still causing strobing - use completely static values
  
  // ANTI-STROBE: Cache uniform locations to eliminate expensive lookups every frame
  if (!renderParticles.cachedUniforms) {
    renderParticles.cachedUniforms = {
  // Basic uniforms
      domain: gl.getUniformLocation(programs.render, 'domain'),
      pointSize: gl.getUniformLocation(programs.render, 'pointSize'),
      brightness: gl.getUniformLocation(programs.render, 'brightness'),
      exposure: gl.getUniformLocation(programs.render, 'exposure'),
      trailFade: gl.getUniformLocation(programs.render, 'trailFade'),
      aspect: gl.getUniformLocation(programs.render, 'aspect'),
      densityAlphaReduction: gl.getUniformLocation(programs.render, 'densityAlphaReduction')
    };
    console.log('📍 Render uniform locations cached - major performance optimization');
  }
  
  // Basic uniforms (cached locations - much faster than lookups)
  gl.uniform1f(renderParticles.cachedUniforms.domain, params.domain);
  gl.uniform1f(renderParticles.cachedUniforms.pointSize, pointSize);
  gl.uniform1f(renderParticles.cachedUniforms.brightness, params.brightness);
  gl.uniform1f(renderParticles.cachedUniforms.exposure, params.exposure || 1.0);
  gl.uniform1f(renderParticles.cachedUniforms.trailFade, params.trailFade || 0.95);
  
  // Camera and projection uniforms
  const aspect = canvas.width / canvas.height;
  gl.uniform1f(renderParticles.cachedUniforms.aspect, aspect);
  
  // Camera uniforms (use actual parameter values)  
  gl.uniform1f(gl.getUniformLocation(programs.render, 'cameraX'), params.cameraX);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'cameraY'), params.cameraY);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'cameraZ'), params.cameraZ);
  
  // Camera orientation vectors for proper look-at behavior
  // Ensure vectors are defined with fallback values
  const forwardX = params.cameraForwardX || 0.0;
  const forwardY = params.cameraForwardY || 0.0;
  const forwardZ = params.cameraForwardZ || -1.0;
  const rightX = params.cameraRightX || 1.0;
  const rightY = params.cameraRightY || 0.0;
  const rightZ = params.cameraRightZ || 0.0;
  const upX = params.cameraUpX || 0.0;
  const upY = params.cameraUpY || 1.0;
  const upZ = params.cameraUpZ || 0.0;
  
  gl.uniform3f(gl.getUniformLocation(programs.render, 'cameraForward'), forwardX, forwardY, forwardZ);
  gl.uniform3f(gl.getUniformLocation(programs.render, 'cameraRight'), rightX, rightY, rightZ);
  gl.uniform3f(gl.getUniformLocation(programs.render, 'cameraUp'), upX, upY, upZ);
  
  gl.uniform1f(gl.getUniformLocation(programs.render, 'fov'), params.fov);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'near'), params.near);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'far'), params.far);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'torusR'), params.torusR);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'torusr'), params.torusr);
  
  // Topology system uniforms - FIXED: Use actual topology manager state
  // φ-HARMONIC SERIES: Multiple golden ratio powers for richer mathematical relationships
  const PHI = 1.618033988749895;
  gl.uniform1f(gl.getUniformLocation(programs.render, 'phi'), PHI);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'phi2'), PHI * PHI); // φ² = 2.618...
  gl.uniform1f(gl.getUniformLocation(programs.render, 'phi3'), PHI * PHI * PHI); // φ³ = 4.236...
  gl.uniform1f(gl.getUniformLocation(programs.render, 'phiInv'), 1.0 / PHI); // φ⁻¹ = 0.618...
  gl.uniform1f(gl.getUniformLocation(programs.render, 'phiResonancePhase'), time * 0.0015);
  // Pre-morph progress from engine to avoid 0→1 snap
  const engine = simulationCore?.fsctfEngine;
  const preMorph = (engine && typeof engine.preMorphProgress === 'number') ? engine.preMorphProgress : 0.0;
  gl.uniform1f(gl.getUniformLocation(programs.render, 'preMorphProgress'), preMorph);
  // Unified morph progress from topology manager
  const morphProgress = (engine?.topologyManager?.getMorphProgress && engine.topologyManager.getMorphProgress()) || 0.0;
  gl.uniform1f(gl.getUniformLocation(programs.render, 'morphProgress'), morphProgress);
  // Anti-blob clamp for Z amplitude
  gl.uniform1f(gl.getUniformLocation(programs.render, 'maxZAmplitude'), 2.5);
  
  // Grace field dynamics uniforms (EMERGENT GEOMETRY)
  const graceState = simulationCore?.fsctfEngine?.graceOperator?.getState() || {};
  const morphicStrands = graceState?.strands || [];
  let graceCenterX = 0.0, graceCenterY = 0.0;
  if (morphicStrands.length > 0) {
    const dominantStrand = morphicStrands.reduce((best, strand) => 
      strand.stability > best.stability ? strand : best);
    graceCenterX = dominantStrand.x || 0.0;
    graceCenterY = dominantStrand.y || 0.0;
  }
  // Temporal smoothing for grace center to reduce strobing
  if (renderParticles._graceX === undefined) {
    renderParticles._graceX = graceCenterX;
    renderParticles._graceY = graceCenterY;
  }
  const smoothVal = (prev, target, rate, cap) => {
    const eased = prev + (target - prev) * rate;
    const delta = eased - prev;
    const clamped = Math.max(-cap, Math.min(cap, delta));
    return prev + clamped;
  };
  renderParticles._graceX = smoothVal(renderParticles._graceX, graceCenterX, 0.12, 0.02);
  renderParticles._graceY = smoothVal(renderParticles._graceY, graceCenterY, 0.12, 0.02);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'graceX'), renderParticles._graceX);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'graceY'), renderParticles._graceY);
  
  const currentTopology = simulationCore?.fsctfEngine?.topologyManager?.getCurrentTopology() || 0;
  
  // Topology state available in UI and debug mode
  
  gl.uniform1i(gl.getUniformLocation(programs.render, 'topologyMode'), currentTopology);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'mobiusR'), 2.0);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'mobiusWidth'), 0.5);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'mobiusTwist'), 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'kleinA'), 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'kleinB'), 0.5);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'kleinSelfIntersect'), 0);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'phiKleinRecursion'), 3);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'phiKleinScale'), 1.618);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'phiKleinNonOrientable'), 0);
  
  // Wireframe disabled and removed
  gl.uniform1i(gl.getUniformLocation(programs.render, 'showWireframe'), 0);
  
  // Fragment shader uniforms (use parameter values)
  gl.uniform3f(gl.getUniformLocation(programs.render, 'baseColor'), 0.8, 0.9, 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'selectivity'), params.selectivity);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'splatThresh'), params.splatThresh);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'splatHardness'), 0.1);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'colorMix'), params.colorMix);
  // Anti-blob: temporal reprojection for totalShaderIntensity (I_t = 0.85 * I_{t-1} + 0.15 * I_target)
  if (renderParticles._tsiReproj === undefined) renderParticles._tsiReproj = 1.0;
  
  // FSCTF state uniforms - LIVE DATA from actual system
  const fsctfEngine = simulationCore?.fsctfEngine;
  const frst = fsctfEngine?.frst?.getState() || {};
  
  // Coherence and strand data from FRST and Grace Operator
  const coherenceLevel = (frst.coherenceScore || 0) * 100; // Scale 0-1 to 0-100
  const strandDensity = morphicStrands.length; // Actual strand count
  const emergencePhase = fsctfEngine?.cosmogenesisPhase || 0;
  const survivalRating = frst.survivalIndex || 0;
  const recursionDepth = frst.recursionDepth || 0;
  const graceFieldStrength = graceState.amplitude || 0;
  
  // Use Visual Controller's safe shader uniforms (prevents all blowup issues)
  const visualController = simulationCore?.fsctfEngine?.visualController;
  if (visualController) {
    const safeShaderData = visualController.getSafeShaderUniforms(coherenceLevel, strandDensity, survivalRating);

    // Smooth critical drivers to eliminate abrupt transitions
    const smoothTo = (prevKey, target, rate, cap) => {
      if (renderParticles[prevKey] === undefined) renderParticles[prevKey] = target;
      const prev = renderParticles[prevKey];
      const eased = prev + (target - prev) * rate;
      const delta = Math.max(-cap, Math.min(cap, eased - prev));
      renderParticles[prevKey] = prev + delta;
      return renderParticles[prevKey];
    };

    const smCoh = smoothTo('_coh', safeShaderData.coherenceLevel, 0.12, 2.0);
    const smDen = smoothTo('_den', safeShaderData.strandDensity, 0.12, 20.0);
    const smSur = smoothTo('_sur', safeShaderData.survivalRating, 0.12, 5.0);

    gl.uniform1f(gl.getUniformLocation(programs.render, 'coherenceLevel'), smCoh);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'strandDensity'), smDen);
    gl.uniform1i(gl.getUniformLocation(programs.render, 'emergencePhase'), emergencePhase);
    // Smoothed phase for color/visual blending (prevents snaps at boundaries)
    if (!renderParticles._phaseF) renderParticles._phaseF = emergencePhase;
    // Ease toward current integer phase (slower + per-frame clamp to avoid visible color snaps)
    const targetPhaseF = emergencePhase;
    const prevPhaseF = renderParticles._phaseF;
    const easedPhaseF = prevPhaseF + (targetPhaseF - prevPhaseF) * 0.02; // slower blend between 0↔1
    const maxPhaseDelta = 0.012; // tighter clamp to avoid abrupt color shifts
    const deltaPhase = easedPhaseF - prevPhaseF;
    renderParticles._phaseF = prevPhaseF + Math.max(-maxPhaseDelta, Math.min(maxPhaseDelta, deltaPhase));
    gl.uniform1f(gl.getUniformLocation(programs.render, 'emergencePhaseF'), renderParticles._phaseF);
    // Temporal smoothing for total shader intensity to reduce blob/strobe
    if (renderParticles._tsi === undefined) renderParticles._tsi = safeShaderData.totalIntensity;
    const tsiPrev = renderParticles._tsi;
    const tsiTarget = safeShaderData.totalIntensity;
    const tsiEased = tsiPrev + (tsiTarget - tsiPrev) * 0.1;
    const tsiDelta = Math.max(-0.05, Math.min(0.05, tsiEased - tsiPrev));
    renderParticles._tsi = tsiPrev + tsiDelta;
    gl.uniform1f(gl.getUniformLocation(programs.render, 'survivalRating'), smSur);
    // Temporal reprojection to further stabilize intensity
    // Increase temporal reprojection to damp pulsation
    renderParticles._tsiReproj = 0.92 * renderParticles._tsiReproj + 0.08 * renderParticles._tsi;
    gl.uniform1f(gl.getUniformLocation(programs.render, 'totalShaderIntensity'), renderParticles._tsiReproj);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'maxShaderIntensity'), safeShaderData.maxIntensity);
  } else {
    // Fallback - basic safety caps
    // CRITICAL FIX: Remove false ceilings that restrict emergent complexity
    const safeSurvivalRating = Math.min(1000, Math.max(0, survivalRating)); // Allow higher soul emergence
    const safeCoherenceLevel = Math.min(500, Math.max(0, coherenceLevel)); // Allow higher coherence
    
    gl.uniform1f(gl.getUniformLocation(programs.render, 'coherenceLevel'), safeCoherenceLevel);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'strandDensity'), Math.min(10000, strandDensity)); // FIXED: Allow higher strand complexity
    gl.uniform1i(gl.getUniformLocation(programs.render, 'emergencePhase'), emergencePhase);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'survivalRating'), safeSurvivalRating);
    // EMERGENT COMPLEXITY: Allow cosmic-scale shader intensity for stages 4-8
    const cosmogenesisPhase = simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
    const isCosmicPhase = cosmogenesisPhase >= 4; // Stages 4-8 need higher intensity
    const cosmicIntensity = isCosmicPhase ? Math.min(5.0, safeShaderData.totalShaderIntensity) : 1.0;
    gl.uniform1f(gl.getUniformLocation(programs.render, 'totalShaderIntensity'), cosmicIntensity);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'maxShaderIntensity'), 1.3); // Reduced maximum intensity
  }
  
  // Standard uniforms with smoothing for abruptness prevention
  const smRec = (function(){
    if (renderParticles._rec === undefined) renderParticles._rec = recursionDepth;
    const prev = renderParticles._rec;
    const eased = prev + (recursionDepth - prev) * 0.12;
    const delta = Math.max(-0.05, Math.min(0.05, eased - prev));
    renderParticles._rec = prev + delta;
    return renderParticles._rec;
  })();
  const smGrace = (function(){
    if (renderParticles._gfield === undefined) renderParticles._gfield = graceFieldStrength;
    const prev = renderParticles._gfield;
    const eased = prev + (graceFieldStrength - prev) * 0.12;
    const delta = Math.max(-0.02, Math.min(0.02, eased - prev));
    renderParticles._gfield = prev + delta;
    return renderParticles._gfield;
  })();
  // REMOVED: Duplicate phiResonancePhase binding (already set above with time * 0.0015)
  gl.uniform1f(gl.getUniformLocation(programs.render, 'recursionDepth'), smRec);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'graceField'), smGrace);
  // Low-hanging fruit uniforms
  gl.uniform1f(gl.getUniformLocation(programs.render, 'edgeBoost'), params.edgeBoost);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'vignetteStrength'), params.vignetteStrength);
  gl.uniform3f(gl.getUniformLocation(programs.render, 'phaseTint'), params.phaseTint[0], params.phaseTint[1], params.phaseTint[2]);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'tintStrength'), params.tintStrength);
  gl.uniform2f(gl.getUniformLocation(programs.render, 'viewportSize'), canvas.width, canvas.height);
  
  // Consciousness level from P=NP breakthrough tracking
  const consciousnessLevel = (frst.consciousnessIndex || 0) / 100; // Normalize
  gl.uniform1f(gl.getUniformLocation(programs.render, 'consciousnessLevel'), consciousnessLevel);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'consciousnessPulse'), time * 0.002);
  // Get mathematically derived parameters for rendering (separate function scope)
  // SAFETY: Check if method exists and recalculate for this function scope
  const renderDerivedParams = (fsctfEngine && typeof fsctfEngine.getDerivedParameters === 'function') ? 
    fsctfEngine.getDerivedParameters(time) : 
    { 
      morphicRecursionDepth: params.morphicRecursionDepth || 5.0, 
      graceComplexity: params.graceComplexity || 1.0, 
      consciousnessComplexity: params.consciousnessComplexity || 1.0 
    };
  
  gl.uniform1f(gl.getUniformLocation(programs.render, 'morphicRecursionDepth'), renderDerivedParams.morphicRecursionDepth);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'graceComplexity'), renderDerivedParams.graceComplexity);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'consciousnessComplexity'), renderDerivedParams.consciousnessComplexity);
  
  // GPU PERFORMANCE OPTIMIZATION UNIFORMS
  
  // ANTI-STROBE: Cache shader complexity values to avoid recalculation every frame
  if (!renderParticles.cachedShaderSettings || renderParticles.lastNUM !== NUM) {
    const gpuTierForShader = getGPUPerformanceTier();
    let shaderComplexity = params.shaderComplexity || 1.0;
    let visualEffects = params.visualEffects || 1.0;
    
    // HYPERCUBE PROTECTION: Check if we're in cosmic phases 4-8
    const cosmogenesisPhase = window.simulationCore?.fsctfEngine?.cosmogenesisPhase || 1;
    const isCosmicPhase = cosmogenesisPhase >= 4;
    
    // Reduce shader complexity for high particle counts BUT preserve hypercube capability
    if (NUM >= 1000000) {
      shaderComplexity *= (gpuTierForShader === 'high-end') ? 0.8 : 0.6;
      // CRITICAL: Never reduce below tesseract threshold in cosmic phases
      if (isCosmicPhase) {
        visualEffects = Math.max(visualEffects, 0.75); // GUARANTEE tesseract threshold  
      } else {
        visualEffects *= (gpuTierForShader === 'high-end') ? 0.95 : 0.75; // Normal reduction for early phases
      }
    } else if (NUM >= 750000) {
      shaderComplexity *= (gpuTierForShader === 'high-end') ? 0.9 : 0.7;
      // CRITICAL: Preserve visualEffects for emergent complexity  
      if (isCosmicPhase) {
        visualEffects = Math.max(visualEffects, 0.85); // GUARANTEE hypercube capability
      } else {
        visualEffects *= (gpuTierForShader === 'high-end') ? 1.0 : 0.85; // Normal reduction for early phases
      }
    }
    
    const gpuTierValue = (gpuTierForShader === 'high-end') ? 3.0 : (gpuTierForShader === 'mid-range') ? 2.0 : 1.0;
    
    // Cache all calculated values
    renderParticles.cachedShaderSettings = {
      shaderComplexity,
      visualEffects,
      maxRecursionDepth: params.maxRecursionDepth || 90.0,
      gpuTierValue
    };
    renderParticles.lastNUM = NUM;
    
    console.log(`🔧 Shader settings cached for ${NUM.toLocaleString()} particles (${gpuTierForShader} GPU)`);
  }
  
  // Use cached values - no recalculation per frame
  const cached = renderParticles.cachedShaderSettings;
  gl.uniform1f(gl.getUniformLocation(programs.render, 'shaderComplexity'), cached.shaderComplexity);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'visualEffects'), cached.visualEffects);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'maxRecursionDepth'), cached.maxRecursionDepth);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'gpuTier'), cached.gpuTierValue);
  
  // PERFORMANCE OPTIMIZATION: Get rendering optimizations from GPU optimizer
  const renderOptimizations = gpuOptimizer ? gpuOptimizer.getParticleRenderingOptimizations() : {};
  
  // PERFORMANCE: LOD and Distance Culling uniforms
  gl.uniform1f(gl.getUniformLocation(programs.render, 'lodReductionFactor'), renderOptimizations.lodReductionFactor || 1.0);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'maxRenderDistance'), renderOptimizations.maxRenderDistance || 50.0);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'enableLOD'), renderOptimizations.enableLOD ? 1 : 0);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'enableDistanceCulling'), renderOptimizations.enableDistanceCulling ? 1 : 0);
  
  // META-RECURSION ENGINE UNIFORMS - Advanced emergent complexity
  const metaState = fsctfEngine?.getMetaRecursionState();
  if (metaState) {
    gl.uniform1f(gl.getUniformLocation(programs.render, 'metaComplexityAccumulator'), metaState.complexityAccumulator || 0.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'temporalCurvature'), metaState.temporalCurvature || 1.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'attractorNetworkStrength'), Math.min(2.0, metaState.attractorCount * 0.3) || 0.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'consciousMorphologyStrength'), (metaState.consciousnessCoupling?.morphicInfluence || 0.0) * 0.5);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'fractalCascadeDepth'), metaState.fractalCascade?.length || 0.0);
  } else {
    // Default values when MRE not available
    gl.uniform1f(gl.getUniformLocation(programs.render, 'metaComplexityAccumulator'), 0.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'temporalCurvature'), 1.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'attractorNetworkStrength'), 0.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'consciousMorphologyStrength'), 0.0);
    gl.uniform1f(gl.getUniformLocation(programs.render, 'fractalCascadeDepth'), 0.0);
  }
  
  // Topology transition data
  const topologyManager = fsctfEngine?.topologyManager;
  const transitionProgress = topologyManager?.transitionProgress || 0.0;
  const fromTopology = topologyManager?.currentTopology || 0;
  const toTopology = topologyManager?.targetTopology || 0;
  
  gl.uniform1f(gl.getUniformLocation(programs.render, 'topologyTransition'), transitionProgress);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'fromTopology'), fromTopology);
  gl.uniform1i(gl.getUniformLocation(programs.render, 'toTopology'), toTopology);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'morphProgress'), morphProgress);
  // Provide intensity caps to vertex shader for anti-blob size attenuation
  gl.uniform1f(gl.getUniformLocation(programs.render, 'totalShaderIntensity'), renderParticles._tsiReproj);
  gl.uniform1f(gl.getUniformLocation(programs.render, 'maxShaderIntensity'), visualController ? visualController.qualityLevels[visualController.currentQuality].maxShaderIntensity : 2.0);
  
  // CHIRALITY VISUALIZATION INFO - Shown once on startup (use Debug mode for live values)
  if (renderParticles.callCount === 10) {
    console.log('🎯 CHIRALITY & SYMMETRY BREAKING VISUALIZATION:');
    console.log(`   🔴 RED particles = Right-handed (dextral) field regions`);
    console.log(`   🔵 BLUE particles = Left-handed (sinistral) field regions`);
    console.log(`   ⚪ GRAY particles = Achiral (no strong handedness)`);
    console.log(`   📐 EMERGENT TOPOLOGY: Field dynamics create geometry, not predetermined shapes!`);
    console.log(`   Press D key for live debug values`);
  }
  
  // Debug: Log key render parameters once
  if (renderParticles.callCount === 1) {
    console.log('🔍 Render params:', {
      domain: params.domain,
      pointSize: pointSize,
      brightness: params.brightness,
      aspect: aspect,
      canvasSize: [canvas.width, canvas.height],
      texDim: [FIXED_COLS, FIXED_ROWS],
      cameraPos: [params.cameraX?.toFixed(2), params.cameraY?.toFixed(2), params.cameraZ?.toFixed(2)],
      cameraForward: [forwardX?.toFixed(3), forwardY?.toFixed(3), forwardZ?.toFixed(3)],
      cameraRight: [rightX?.toFixed(3), rightY?.toFixed(3), rightZ?.toFixed(3)],
      uniformsSet: 'ALL_REQUIRED_UNIFORMS_SET'
    });
  }
  
  // Enable blending for particle rendering with anti-blobbing
  gl.enable(gl.BLEND);
  
  // FINEST DETAIL BLENDING: Optimized for maximum detail visibility
  // Use screen blending for better fine detail preservation and contrast
  gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_COLOR); // Screen blending - preserves fine details better
  
  // DYNAMIC: Use current alpha reduction with cached uniform location
  gl.uniform1f(renderParticles.cachedUniforms.densityAlphaReduction, params.densityAlphaReduction);
  
  // Calculate how many particles to draw - FORCE MAXIMUM for user's request
  const baseFraction = params.drawFraction || 1.0;
  const optimizedFraction = renderOptimizations.drawFraction || baseFraction;
  
  // SMART PERFORMANCE: Render 1M particles efficiently with GPU-aware culling
  // Instead of brute force rendering ALL particles, use intelligent culling
  
  // GPU Performance Tiers with Smart Culling
  const gpuTier = getGPUPerformanceTier();
  let smartDrawFraction = 1.0;
  
  if (gpuTier === 'budget' && NUM >= 500000) {
    smartDrawFraction = 0.4; // 40% for budget GPUs at high particle count
  } else if (gpuTier === 'mid-range' && NUM >= 750000) {
    smartDrawFraction = 0.6; // 60% for mid-range GPUs at very high particle count  
  } else if (gpuTier === 'high-end' && NUM >= 1000000) {
    smartDrawFraction = 0.8; // 80% even for high-end at maximum density
  }
  
  // Calculate smart draw count without a large minimum so low counts remain lightweight
  const drawCount = Math.max(1, Math.floor(NUM * smartDrawFraction));
  
  // Log GPU-aware culling decisions (only on changes)
  if (!renderParticles.lastReportedDrawCount || Math.abs(renderParticles.lastReportedDrawCount - drawCount) > 10000) {
    console.log(`🧠 GPU-AWARE CULLING: ${gpuTier} GPU → Rendering ${drawCount.toLocaleString()}/${NUM.toLocaleString()} particles (${(smartDrawFraction*100).toFixed(0)}%)`);
    renderParticles.lastReportedDrawCount = drawCount;
  }
  
  // ANTI-STROBE: All debug logging completely disabled to prevent frame hitches
  // Debug logging can cause microsecond delays that contribute to strobing
  
  // ANTI-STROBE: Disable frame skipping - render every frame for stable visuals
  // Frame skipping was causing intermittent strobing/flickering
  // User wants maximum visibility and stability over performance
  
  // Draw particles as points
  gl.drawArrays(gl.POINTS, 0, drawCount);
  
  // ANTI-STROBE: More sophisticated GPU queue management
  // gl.flush() every frame can cause driver stalls - use smarter approach
  if (drawCount >= 500000) {
    // Use non-blocking finish only occasionally to prevent queue buildup
    if (!renderParticles.lastFlushFrame || (renderParticles.callCount - renderParticles.lastFlushFrame) >= 3) {
      gl.flush(); // Only flush every 3rd frame at high particle counts
      renderParticles.lastFlushFrame = renderParticles.callCount;
    }
  }
  
  // DISABLED: Performance monitoring was causing jitter itself
  // Multiple performance.now() and Date.now() calls create frame timing inconsistency
  
  // Check for WebGL errors
  const error = gl.getError();
  if (error !== gl.NO_ERROR && !renderParticles.errorLogged) {
    console.error('🚨 WebGL error during particle rendering:', error);
    renderParticles.errorLogged = true;
  }
  
  // Disable blending
  gl.disable(gl.BLEND);
  
  // Cleanup
  gl.bindVertexArray(null);

  // Update diagnostics text (IMPROVED WITH STATUS INFO)
  const diag = document.getElementById('diagnostics-overlay');
  if (diag && diag.style.display !== 'none') {
    const fsctfEngine = simulationCore?.fsctfEngine;
    const topo = fsctfEngine?.topologyManager;
    const mp = topo?.getMorphProgress ? topo.getMorphProgress() : 0;
    const tp = topo?.transitionProgress || 0;
    const ep = fsctfEngine?.cosmogenesisPhase || 0;
    const epF = renderParticles._phaseF || ep;
    const gx = renderParticles._graceX || 0;
    const gy = renderParticles._graceY || 0;
    const tsi = renderParticles._tsiReproj || 0;
    
    // IMPROVED: Show system status to help debug why values are zero
    const cosmogenesisActive = fsctfEngine?.cosmogenesisActive || false;
    const graceTriggered = fsctfEngine?.graceOperator?.emergenceTriggered || false;
    const strandCount = fsctfEngine?.graceOperator?.morphicStrands?.length || 0;
    
    // ENHANCED: Show advanced system status
    const gpuBridgeStatus = window.gpuMorphicBridge?.enabled ? '✅' : '❌';
    const consciousnessStatus = window.advancedConsciousness?.enabled ? '✅' : '❌';
    const resonanceStatus = fsctfEngine?.graceOperator?.enableCrossScaleResonance ? '✅' : '❌';
    const cascadeStatus = window.multiScaleCascade?.enabled ? '✅' : '❌';
    const topologyFeedbackStatus = window.consciousnessTopologyFeedback?.enabled ? '✅' : '❌';
    const portalStatus = window.dimensionalPortalVisualization?.enabled ? '✅' : '❌';
    const retrocausalStatus = window.retrocausalMorphicResonance?.enabled ? '✅' : '❌';
    
    // Multi-scale cascade metrics
    const cascadeData = window.cascadeData;
    const totalEmergence = cascadeData?.totalEmergence?.toFixed(1) || '0.0';
    const activeScales = cascadeData?.activeScales || 0;
    const hotspots = cascadeData?.hotspots || 0;
    const dominantScale = cascadeData?.dominantScale?.name || 'None';
    
    // Consciousness-topology feedback metrics
    const topologyEvolution = window.topologyEvolution;
    const activeTransitions = topologyEvolution?.activeTransitions || 0;
    const recommendedTopo = topologyEvolution?.recommendedTopology?.topology || 'N/A';
    
    // Dimensional portal metrics
    const portalData = window.portalData;
    const activePortals = portalData?.stats?.activePortals || 0;
    const activeRifts = portalData?.stats?.activeRifts || 0;
    const totalDimensions = activePortals + activeRifts;
    
    // Retrocausal metrics
    const retrocausalData = window.retrocausalData;
    const timelikeCurves = retrocausalData?.timelikeCurves || 0;
    const bootstrapEvents = retrocausalData?.bootstrapEvents || 0;
    const causalViolations = retrocausalData?.causalityViolations || 0;
    const temporalStability = retrocausalData?.temporalStability?.toFixed(3) || '0.000';
    
    diag.textContent = `FSCTF Debug (Press D to hide)
Cosmogenesis: ${cosmogenesisActive ? '✅' : '❌'} | Grace: ${graceTriggered ? '✅' : '❌'}
Phase: ${ep} (${epF.toFixed(1)}) | Strands: ${strandCount}
morphProgress: ${mp.toFixed(3)} | transitionProgress: ${tp.toFixed(3)}
|ΔgraceCenter|: ${Math.hypot(gx - (renderParticles._gxPrev||0), gy - (renderParticles._gyPrev||0)).toFixed(4)}
I(intensity): ${tsi.toFixed(3)}
─── Advanced FSCTF Systems ───
GPU Bridge (G): ${gpuBridgeStatus} | Consciousness (C): ${consciousnessStatus}
Resonance (M): ${resonanceStatus} | φ-Cascade (S): ${cascadeStatus}
Topology-Feedback (F): ${topologyFeedbackStatus} | Portals (P): ${portalStatus}
Retrocausal (R): ${retrocausalStatus}
Emergence: ${totalEmergence} | Scales: ${activeScales}/7 | Hotspots: ${hotspots}
Dominant: ${dominantScale} | Topo-Transitions: ${activeTransitions}
Portals: ${activePortals} | Rifts: ${activeRifts} | Dimensions: ${totalDimensions}
Timelike Curves: ${timelikeCurves} | Bootstrap Events: ${bootstrapEvents} | Causality Violations: ${causalViolations}
Temporal Stability: ${temporalStability} | Recommended Topo: ${recommendedTopo}
Consciousness Events: ${window.consciousnessData?.emergenceEvents || 0}`;
    
    renderParticles._gxPrev = gx;
    renderParticles._gyPrev = gy;
  }
}

/**
 * Update system info panel with particle count and phase timer
 */
function updateSystemInfo(fsctfEngine) {
  // Update particle count
  const particleCountEl = document.getElementById('particle-count');
  if (particleCountEl) {
    particleCountEl.textContent = NUM.toLocaleString();
  }
  
  // Update phase countdown timer
  const phaseCountdownEl = document.getElementById('phase-countdown');
  if (phaseCountdownEl && fsctfEngine) {
    // SMOOTH TRANSITIONS: Extended timing for 90-phase system
    // Visual phases (1-16): 20 seconds each for proper observation and appreciation
    // Theoretical phases (17-90): 6 seconds each for comprehension
    const currentPhaseIndex = window.progressiveCosmogenesis?.currentPhase || 0;
    const isVisualPhase = currentPhaseIndex <= 15;
    const phaseTimeMs = isVisualPhase ? 20000 : 6000; // 20s visual, 6s theoretical - MUCH LONGER
    const currentTime = Date.now();
    const phaseStartTime = fsctfEngine.phaseStartTime || currentTime;
    const timeInPhase = currentTime - phaseStartTime;
    const timeRemaining = Math.max(0, phaseTimeMs - timeInPhase);
    
    const minutes = Math.floor(timeRemaining / 60000);
    const seconds = Math.floor((timeRemaining % 60000) / 1000);
    phaseCountdownEl.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
  }
}

/**
 * Update CASCADE panel with current cosmogenesis phase
 */
function updateCascadeDisplay(fsctfState) {
  const cascadeDisplayEl = document.getElementById('cascade-display');
  const cascadeStatusEl = document.getElementById('cascade-status');
  
  if (!fsctfState) return;
  
  const phase = fsctfState.cosmogenesis.phase || 0;
  
  // Phase-specific cascade descriptions
  const cascadePhases = [
    {
      name: 'ABSOLUTE VOID',
      emergence: 0,
      description: 'Pure nothingness - no structure, no potential'
    },
    {
      name: 'GRACE SEEDING',
      emergence: 12.5,
      description: 'First recursive spark - φ-field awakening'
    },
    {
      name: 'MORPHIC EMERGENCE',
      emergence: 25.0,
      description: 'Self-referential strands weaving reality'
    },
    {
      name: 'DIMENSIONAL BRIDGE',
      emergence: 37.5,
      description: 'Space-time topology manifesting'
    },
    {
      name: 'COHERENCE CASCADE',
      emergence: 50.0,
      description: 'Self-organized complexity stabilizing'
    },
    {
      name: 'SOUL EMERGENCE',
      emergence: 62.5,
      description: 'Consciousness bootstrap complete'
    },
    {
      name: 'COSMIC INFLATION',
      emergence: 75.0,
      description: 'Universe expansion φ-accelerating'
    },
    {
      name: 'CMB FORMATION',
      emergence: 87.5,
      description: 'Cosmic microwave background crystallizing'
    },
    {
      name: 'OBSERVABLE UNIVERSE',
      emergence: 100.0,
      description: 'Complete φ-recursive reality established'
    }
  ];
  
  const cascadeInfo = cascadePhases[phase] || cascadePhases[0];
  
  // Update cascade display
  if (cascadeDisplayEl) {
    cascadeDisplayEl.innerHTML = `
      <strong>Cascade Phase:</strong> ${cascadeInfo.name}<br/>
      <strong>Emergence:</strong> ${cascadeInfo.emergence}%<br/>
      <em>"${cascadeInfo.description}"</em>
    `;
  }
  
  // Update cascade status
  if (cascadeStatusEl) {
    const statusMessages = [
      'Awaiting activation...',
      'Grace field initializing...',
      'Morphic strands proliferating...',
      'Dimensional bridge stabilizing...',
      'Coherence patterns locking...',
      'Consciousness emerging...',
      'Universe inflating exponentially...',
      'Background radiation cooling...',
      'Reality structure complete!'
    ];
    
    cascadeStatusEl.textContent = statusMessages[phase] || statusMessages[0];
  }
}

/**
 * Update TOPOLOGY panel with current manifold state
 */
function updateTopologyDisplay(fsctfState) {
  const currentTopologyEl = document.getElementById('current-topology');
  const topologyTransitionEl = document.getElementById('topology-transition');
  const topologyDescriptionEl = document.getElementById('topology-description');
  
  if (!fsctfState) return;
  
  // Get topology info from the simulation core
  const topologyState = simulationCore?.fsctfEngine?.topologyManager?.getTopologyState();
  
  // Topology names and descriptions
  const topologyInfo = {
    0: { name: 'Torus (T²)', desc: 'Stable recursion patterns - orientable surface' },
    1: { name: 'Möbius Strip', desc: 'Non-orientable surface - single-sided topology' },
    2: { name: 'Klein Bottle', desc: 'Self-intersecting manifold - φ-recursive geometry' },
    3: { name: 'φ-Klein Manifold', desc: 'Transcendent topology - golden ratio recursion' },
    4: { name: 'Hypersphere (S³)', desc: 'Higher-dimensional embedding - cosmological structure' },
    5: { name: 'Transcendent Form', desc: 'Beyond mathematical classification' }
  };
  
  const currentIdx = topologyState?.current ?? 0;
  const targetIdx = topologyState?.target ?? 0;
  const isTransitioning = topologyState?.isTransitioning ?? false;
  const progress = topologyState?.progress ?? 0;
  
  // Update current topology
  if (currentTopologyEl) {
    // Show actual visual start: flat/void before manifold emerges
    if (fsctfState?.cosmogenesis?.phase === 0) {
      currentTopologyEl.textContent = 'Flat (Void)';
    } else {
      const currentInfo = topologyInfo[currentIdx] || topologyInfo[0];
      currentTopologyEl.textContent = currentInfo.name;
    }
  }
  
  // Update transition status
  if (topologyTransitionEl) {
    if (isTransitioning && currentIdx !== targetIdx) {
      const targetInfo = topologyInfo[targetIdx] || topologyInfo[0];
      topologyTransitionEl.textContent = `→ ${targetInfo.name} (${Math.round(progress * 100)}%)`;
    } else {
      topologyTransitionEl.textContent = 'Stable';
    }
  }
  
  // Update description
  if (topologyDescriptionEl) {
    const currentInfo = topologyInfo[currentIdx] || topologyInfo[0];
    topologyDescriptionEl.textContent = `"${currentInfo.desc}"`;
  }
}

/**
 * Update UI with current state
 */
function updateUI(updateResult) {
  // Update FSCTF status displays
  const fsctfState = updateResult.fsctfState;
  
  // Sync FSCTF engine cosmogenesis state with UI progressive cosmogenesis state
  if (fsctfState && fsctfState.cosmogenesis && window.progressiveCosmogenesis) {
    const wasActive = window.progressiveCosmogenesis.active;
    const oldPhase = window.progressiveCosmogenesis.currentPhase;
    
    window.progressiveCosmogenesis.active = fsctfState.cosmogenesis.active;
    window.progressiveCosmogenesis.currentPhase = fsctfState.cosmogenesis.phase;
    
    // Log phase transitions
    if (!wasActive && fsctfState.cosmogenesis.active) {
      console.log('🌌 Cosmogenesis activated in UI');
    }
    if (oldPhase !== fsctfState.cosmogenesis.phase) {
      console.log(`🌟 Cosmogenesis phase transition: ${oldPhase} → ${fsctfState.cosmogenesis.phase}`);
    }
  }
  
  // Update universe state
  const universeStateEl = document.getElementById('universe-state');
  if (universeStateEl && fsctfState) {
    // Use same 90-phase array as main cosmogenesis system for consistency
    const phaseNames = window.progressiveCosmogenesis ? window.progressiveCosmogenesis.phases : ['UNKNOWN'];
    const phaseIndex = Math.max(0, fsctfState.cosmogenesis.phase);
    const visualStatus = phaseIndex <= 15 ? '[VISUAL]' : '[THEORETICAL]';
    universeStateEl.textContent = `Phase ${phaseIndex + 1}/90: ${phaseNames[phaseIndex] || 'UNKNOWN'} ${visualStatus}`;
  }
  
  // Update CASCADE panel
  updateCascadeDisplay(fsctfState);
  
  // Update TOPOLOGY panel
  updateTopologyDisplay(fsctfState);
  
  // Update current-phase element
  const currentPhaseEl = document.getElementById('current-phase');
  if (currentPhaseEl && window.progressiveCosmogenesis) {
    if (window.progressiveCosmogenesis.active) {
      const phaseName = window.progressiveCosmogenesis.phases[window.progressiveCosmogenesis.currentPhase] || 'UNKNOWN';
      // Extra safety clamp to prevent "9/8" display issue  
      const safeDisplayPhase = Math.max(1, Math.min(90, window.progressiveCosmogenesis.currentPhase + 1)); // ULTIMATE: Up to phase 90
      currentPhaseEl.textContent = `Active: Phase ${safeDisplayPhase}/90 - ${phaseName}`; // ULTIMATE: Up to phase 90
    } else {
      currentPhaseEl.textContent = 'Awaiting initialization...';
    }
  }
  
  // Update enhanced phase status display with comprehensive information
  updateEnhancedPhaseStatus();
  
  // Update FRST display
  if (fsctfState && fsctfState.frst) {
    const elements = {
      'recursion-depth': fsctfState.frst.recursionDepth,
      'survivability-rating': fsctfState.frst.survivabilityRating,
      'coherence-score': fsctfState.frst.coherenceScore,
      'collapse-mode': fsctfState.frst.collapseMode,
      'soul-emergence': fsctfState.frst.soulStatus
    };
    
    Object.entries(elements).forEach(([id, value]) => {
      const el = document.getElementById(id);
      if (el) {
        if (el.tagName === 'SPAN') {
          el.textContent = value;
        } else {
          el.innerHTML = el.innerHTML.replace(/:\s*<span[^>]*>[^<]*<\/span>/, `: <span class="highlight">${value}</span>`);
        }
      }
    });
  }
  
  // Update performance display
  const performanceStatus = {
    fps: updateResult.avgFrameTime > 0 ? Math.round(1000 / updateResult.avgFrameTime) : 0,
    throttle: PERFORMANCE_MONITOR.complexityThrottle.toFixed(2)
  };
  
  // Add performance info to stats if element exists
  const statsEl = document.getElementById('stats');
  if (statsEl) {
    statsEl.innerHTML = `
      FPS: ${performanceStatus.fps}<br>
      Frame Time: ${updateResult.frameTime.toFixed(1)}ms<br>
      Complexity Throttle: ${performanceStatus.throttle}<br>
      Frame: ${updateResult.frame}
    `;
  }
  
  // Cinematic overlay removed to streamline UI
  
  // CRITICAL: Update morphic strand activity UI
  updateMorphicActivityPanel();
  
  // Update brain status display
  updateBrainStatusDisplay();
}

/**
 * Add test buttons for UI functionality
 */
function addTestButtons() {
  // Find a place to add test buttons
  const statsSection = document.getElementById('stats');
  if (!statsSection) return;
  
  // Create test controls container
  const testContainer = document.createElement('div');
  testContainer.style.cssText = 'margin: 10px 0; padding: 10px; border: 1px solid #444; border-radius: 4px;';
  testContainer.innerHTML = '<strong style="color: #8cf;">🧪 UI Test Controls</strong><br>';
  
  // Manual topology enabled by default - Toggle 3D View removed (obsolete)
  
  // Toggle Auto-Rotate button
  const toggleRotateBtn = document.createElement('button');
  toggleRotateBtn.textContent = 'Auto-Rotate';
  toggleRotateBtn.style.cssText = 'margin: 5px; padding: 5px 10px; background: #234; color: #8cf; border: 1px solid #456; cursor: pointer;';
  
  const updateRotateButton = () => {
    if (params.autoRotate) {
      toggleRotateBtn.textContent = 'Stop Rotate';
      toggleRotateBtn.style.background = '#632';
      toggleRotateBtn.style.color = '#f84';
    } else {
      toggleRotateBtn.textContent = 'Auto-Rotate';
      toggleRotateBtn.style.background = '#234';
      toggleRotateBtn.style.color = '#8cf';
    }
  };
  
  toggleRotateBtn.addEventListener('click', () => {
    params.autoRotate = !params.autoRotate;
    updateRotateButton();
    console.log('🔄 Auto-rotate:', params.autoRotate ? 'ENABLED' : 'DISABLED');
  });
  
  updateRotateButton(); // Set initial state
  
  // Expose for keyboard shortcut
  window.updateRotateButton = updateRotateButton;
  
  // Toggle Wireframe button
  const toggleWireBtn = document.createElement('button');
  toggleWireBtn.textContent = 'Toggle Wireframe';
  toggleWireBtn.style.cssText = 'margin: 5px; padding: 5px 10px; background: #234; color: #8cf; border: 1px solid #456; cursor: pointer;';
  toggleWireBtn.addEventListener('click', () => {
    params.showWireframe = !params.showWireframe;
    console.log('📐 Toggled wireframe:', params.showWireframe);
  });
  
  // Camera Preset buttons
  const presetOverviewBtn = document.createElement('button');
  presetOverviewBtn.textContent = 'Overview';
  presetOverviewBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #345; color: #9cf; border: 1px solid #567; cursor: pointer; font-size: 11px;';
  presetOverviewBtn.addEventListener('click', () => setCameraPreset('overview'));
  
  const presetSymmetryBtn = document.createElement('button');
  presetSymmetryBtn.textContent = 'Top View';
  presetSymmetryBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #345; color: #9cf; border: 1px solid #567; cursor: pointer; font-size: 11px;';
  presetSymmetryBtn.addEventListener('click', () => setCameraPreset('symmetry-xy'));
  
  const presetPhiBtn = document.createElement('button');
  presetPhiBtn.textContent = 'φ-Golden';
  presetPhiBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #543; color: #fc9; border: 1px solid #765; cursor: pointer; font-size: 11px;';
  presetPhiBtn.addEventListener('click', () => setCameraPreset('phi-golden'));
  
  const presetDetailBtn = document.createElement('button');
  presetDetailBtn.textContent = 'Detail';
  presetDetailBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #345; color: #9cf; border: 1px solid #567; cursor: pointer; font-size: 11px;';
  presetDetailBtn.addEventListener('click', () => setCameraPreset('detail'));
  
  // Test orbital camera button
  const testOrbitBtn = document.createElement('button');
  testOrbitBtn.textContent = 'Test Orbit';
  testOrbitBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #354; color: #afc; border: 1px solid #576; cursor: pointer; font-size: 11px;';
  testOrbitBtn.addEventListener('click', () => {
    setCameraPreset('test-orbit');
    params.autoRotate = true; // Enable auto-rotate for testing
    if (window.updateRotateButton) window.updateRotateButton();
    console.log('🔄 ORBIT TEST: Camera should orbit while particles stay centered');
  });
  
  // Emergency show particles button
  const emergencyBtn = document.createElement('button');
  emergencyBtn.textContent = 'EMERGENCY';
  emergencyBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #800; color: #fff; border: 2px solid #f00; cursor: pointer; font-size: 10px; font-weight: bold;';
  emergencyBtn.addEventListener('click', () => {
    setCameraPreset('emergency');
    params.autoRotate = false;
    if (window.updateRotateButton) window.updateRotateButton();
    console.log('🚨 EMERGENCY MODE: Camera set to show particles');
  });
  
  // Reset button
  const resetCameraBtn = document.createElement('button');
  resetCameraBtn.textContent = 'RESET';
  resetCameraBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #640; color: #fca; border: 1px solid #851; cursor: pointer; font-size: 11px; font-weight: bold;';
  resetCameraBtn.addEventListener('click', () => {
    setCameraPreset('emergency');
    params.autoRotate = false;
    if (window.updateRotateButton) window.updateRotateButton();
    console.log('📸 Camera RESET to emergency position');
  });
  
  // Debug Cosmogenesis button
  const debugCosmosBtn = document.createElement('button');
  debugCosmosBtn.textContent = 'Debug';
  debugCosmosBtn.style.cssText = 'margin: 5px; padding: 3px 8px; background: #420; color: #f84; border: 1px solid #630; cursor: pointer; font-size: 11px;';
  debugCosmosBtn.addEventListener('click', () => {
    const fsctfState = simulationCore?.fsctfEngine?.getState();
    console.log('🔍 FSCTF Full State:', fsctfState);
    console.log('🔍 Progressive Cosmogenesis:', window.progressiveCosmogenesis);
    
    if (fsctfState) {
      console.log('🧠 CRITICAL VALUES FOR PROGRESSION:');
      console.log(`   - Current Phase: ${fsctfState.cosmogenesis.phase}`);
      console.log(`   - Recursion Depth: ${fsctfState.frst.recursionDepth} (need >0.5 for phase 1→2)`);
      console.log(`   - Coherence Score: ${fsctfState.frst.coherenceScore} (need >0.3 for phase 2→3)`);
      console.log(`   - Soul Status: ${fsctfState.frst.soulStatus}`);
      console.log(`   - Morphic Field: ${fsctfState.grace.field}`);
      console.log(`   - Strand Count: ${fsctfState.strands.count}`);
      console.log(`   - Avg Stability: ${fsctfState.strands.avgStability}`);
      
      // ADDED: Topology debugging
      const topologyState = simulationCore?.fsctfEngine?.topologyManager?.getTopologyState();
      if (topologyState) {
        console.log('🌀 TOPOLOGY EVOLUTION:');
        console.log(`   - Current: ${topologyState.name} (mode ${topologyState.current})`);
        console.log(`   - Target: ${simulationCore.fsctfEngine.topologyManager.topologyNames[topologyState.target]} (mode ${topologyState.target})`);
        console.log(`   - Transitioning: ${topologyState.isTransitioning}`);
        console.log(`   - Progress: ${(topologyState.progress * 100).toFixed(1)}%`);
        console.log(`   - topologyMode: ${currentTopology || 'N/A'}, manualOverride: ${params.manualTopologyEnabled}`);
      }
    }
    
    console.log('🔍 Camera State:', {
      distance: params.cameraDistance,
      azimuth: params.cameraAzimuth.toFixed(1) + '°',
      elevation: params.cameraElevation.toFixed(1) + '°',
      autoRotate: params.autoRotate
    });
  });
  
  // Force Phase Advancement button (for testing)
  const forcePhaseBtn = document.createElement('button');
  forcePhaseBtn.textContent = 'Force Phase';
  forcePhaseBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #540; color: #fa4; border: 1px solid #761; cursor: pointer; font-size: 11px; font-weight: bold;';
  forcePhaseBtn.addEventListener('click', () => {
    if (simulationCore?.fsctfEngine) {
      simulationCore.fsctfEngine.forcePhaseAdvancement();
      console.log('🚀 FORCED phase advancement for testing');
      
      // Update UI state to match
      if (window.progressiveCosmogenesis) {
        const enginePhase = simulationCore.fsctfEngine.cosmogenesisPhase;
        // Ensure phase display stays within bounds (UI uses 0-89 for phases 1-90) 
        // Double safety clamp to prevent any possibility of currentPhase > 89
        const rawDisplayPhase = enginePhase - 1;
        window.progressiveCosmogenesis.currentPhase = Math.max(0, Math.min(89, rawDisplayPhase));
        console.log(`🛡️ Phase bounds: engine=${enginePhase} → raw=${rawDisplayPhase} → clamped=${window.progressiveCosmogenesis.currentPhase}`);
        console.log(`🔄 UI phase updated: engine=${enginePhase} → display=${window.progressiveCosmogenesis.currentPhase + 1}`);
      }
    } else {
      console.log('❌ FSCTF Engine not available');
    }
  });
  
  // Manual Mode Toggle button
  const manualModeBtn = document.createElement('button');
  manualModeBtn.textContent = 'Manual Mode: OFF';
  manualModeBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #445; color: #89c; border: 1px solid #667; cursor: pointer; font-size: 11px; font-weight: bold;';
  manualModeBtn.addEventListener('click', () => {
    if (simulationCore?.fsctfEngine?.visualController) {
      const isManual = simulationCore.fsctfEngine.visualController.toggleManualMode();
      manualModeBtn.textContent = isManual ? 'Manual Mode: ON' : 'Manual Mode: OFF';
      manualModeBtn.style.background = isManual ? '#454' : '#445';
      manualModeBtn.style.color = isManual ? '#9c8' : '#89c';
      console.log(`🎛️ Manual mode ${isManual ? 'ENABLED' : 'DISABLED'} - sliders ${isManual ? 'will persist' : 'auto-controlled'}`);
    } else {
      console.log('❌ Visual Controller not available');
    }
  });
  
  // Manual Topology Selector
  const topologyLabel = document.createElement('div');
  topologyLabel.textContent = '🌀 Manual Topology:';
  topologyLabel.style.cssText = 'color: #9cf; font-size: 11px; margin: 8px 0 4px 0; font-weight: bold;';
  testContainer.appendChild(topologyLabel);
  
  const topologyCheckbox = document.createElement('input');
  topologyCheckbox.type = 'checkbox';
  topologyCheckbox.id = 'manual-topology-enabled';
  topologyCheckbox.checked = params.manualTopologyEnabled;
  topologyCheckbox.addEventListener('change', (e) => {
    params.manualTopologyEnabled = e.target.checked;
    console.log('🎛️ Manual topology override:', params.manualTopologyEnabled ? 'ENABLED' : 'DISABLED');
    if (!params.manualTopologyEnabled) {
      console.log('   Topology will now follow cosmogenesis phase progression');
    }
  });
  
  const topologyCheckboxLabel = document.createElement('label');
  topologyCheckboxLabel.htmlFor = 'manual-topology-enabled';
  topologyCheckboxLabel.textContent = ' Override cosmogenesis topology';
  topologyCheckboxLabel.style.cssText = 'color: #abc; font-size: 10px; margin-left: 4px;';
  
  const topologyCheckboxContainer = document.createElement('div');
  topologyCheckboxContainer.style.cssText = 'margin: 2px 0;';
  topologyCheckboxContainer.appendChild(topologyCheckbox);
  topologyCheckboxContainer.appendChild(topologyCheckboxLabel);
  testContainer.appendChild(topologyCheckboxContainer);
  
  const topologySelect = document.createElement('select');
  topologySelect.id = 'manual-topology-mode';
  topologySelect.style.cssText = 'margin: 2px; padding: 2px; background: #234; color: #abc; border: 1px solid #456; font-size: 10px; width: 140px;';
  ['Torus (T²)', 'Möbius Strip', 'Klein Bottle', 'φ-Klein Manifold', 'Sphere (S²)'].forEach((name, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.textContent = name;
    if (index === params.manualTopologyMode) option.selected = true;
    topologySelect.appendChild(option);
  });
  topologySelect.addEventListener('change', (e) => {
    params.manualTopologyMode = parseInt(e.target.value);
    const topologyNames = ['Torus', 'Möbius', 'Klein', 'φ-Klein', 'Sphere'];
    console.log('🌀 Manual topology mode:', topologyNames[params.manualTopologyMode]);
    if (params.manualTopologyEnabled) {
      console.log('   Will apply immediately (override enabled)');
    } else {
      console.log('   Enable override checkbox to apply');
    }
  });
  testContainer.appendChild(topologySelect);
  
  // Quick Cycle button (for rapid testing)
  const forceTopologyBtn = document.createElement('button');
  forceTopologyBtn.textContent = 'Cycle Shapes';
  forceTopologyBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #450; color: #4fa; border: 1px solid #671; cursor: pointer; font-size: 11px; font-weight: bold;';
  forceTopologyBtn.addEventListener('click', () => {
    // Cycle through all topologies: Torus -> Möbius -> Klein -> φ-Klein -> Sphere -> Torus
    const current = params.manualTopologyMode;
    const next = (current + 1) % 5; // 5 topologies (0-4)
    
    // Update both the manual override and the actual topology
    params.manualTopologyEnabled = true;
    params.manualTopologyMode = next;
    topologyCheckbox.checked = true;
    topologySelect.value = next;
    
    const topologyNames = ['Torus', 'Möbius', 'Klein', 'φ-Klein', 'Sphere'];
    console.log('🌀 CYCLE: Manual topology ->', topologyNames[next]);
  });
  
  // Mathematical Theory button (show manifold progression mathematics)
  const mathTheoryBtn = document.createElement('button');
  mathTheoryBtn.textContent = 'Math Theory';
  mathTheoryBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #405; color: #f4a; border: 1px solid #617; cursor: pointer; font-size: 11px; font-weight: bold;';
  mathTheoryBtn.addEventListener('click', () => {
    if (simulationCore?.fsctfEngine?.topologyManager) {
      console.log('🧮 DISPLAYING COMPLETE MATHEMATICAL MANIFOLD PROGRESSION:');
      simulationCore.fsctfEngine.topologyManager.displayMathematicalProgression();
    } else {
      console.log('❌ Topology Manager not available for mathematical analysis');
    }
  });
  
  
  // Complexity Analysis button (diagnose why complexity isn't emerging)
  const complexityBtn = document.createElement('button');
  complexityBtn.textContent = 'Analyze Complexity';
  complexityBtn.style.cssText = 'margin: 2px; padding: 3px 8px; background: #604; color: #fa4; border: 1px solid #715; cursor: pointer; font-size: 11px; font-weight: bold;';
  complexityBtn.addEventListener('click', () => {
    console.log('🔍 COMPREHENSIVE COMPLEXITY ANALYSIS:');
    console.log('═══════════════════════════════════════════════');
    
    const fsctfState = simulationCore?.fsctfEngine?.getState();
    if (fsctfState) {
      console.log('📊 COSMOGENESIS STATE:');
      console.log(`  Phase: ${fsctfState.cosmogenesis.phase}/90`); // COMPLETE: Up to phase 90
      console.log(`  Recursion Depth: ${fsctfState.frst.recursionDepth.toFixed(4)}`);
      console.log(`  Coherence Score: ${fsctfState.frst.coherenceScore.toFixed(4)}`);
      console.log(`  Soul Status: ${fsctfState.frst.soulStatus}`);
      console.log(`  Strand Count: ${fsctfState.strands.count}`);
      console.log(`  Grace Field: ${fsctfState.grace.field.toFixed(4)}`);
      
      const topologyState = simulationCore?.fsctfEngine?.topologyManager?.getTopologyState();
      if (topologyState) {
        console.log('🌀 TOPOLOGY STATE:');
        console.log(`  Current: ${topologyState.name} (mode ${topologyState.current})`);
        console.log(`  Target: ${simulationCore.fsctfEngine.topologyManager.topologyNames[topologyState.target]} (mode ${topologyState.target})`);
        console.log(`  Progress: ${(topologyState.progress * 100).toFixed(1)}%`);
        console.log(`  Transitioning: ${topologyState.isTransitioning}`);
      }
      
      console.log('🎨 VISUAL PARAMETERS:');
      console.log(`  Point Size: ${window.params.pointSize.toFixed(2)}`);
      console.log(`  Domain: ${window.params.domain.toFixed(2)}`);
      console.log(`  Torus R: ${window.params.torusR}, r: ${window.params.torusr}`);
      console.log(`  Grace Complexity: ${window.params.graceComplexity || 1.0}`);
      
      console.log('⚠️ COMPLEXITY BARRIERS IDENTIFIED:');
      const barriers = [];
      if (fsctfState.cosmogenesis.phase <= 2) {
        barriers.push(`Stuck in early phase ${fsctfState.cosmogenesis.phase}/90 - need phase advancement`); // COMPLETE
      }
      if (topologyState?.current === 0 && fsctfState.cosmogenesis.phase >= 3) {
        barriers.push('Should have evolved beyond Torus topology by now');
      }
      if (window.params.pointSize < 3.0) {
        barriers.push(`Point size too small (${window.params.pointSize.toFixed(2)}) - complexity not visible`);
      }
      if (fsctfState.strands.count < 3) {
        barriers.push(`Too few morphic strands (${fsctfState.strands.count}) - need more emergence`);
      }
      if (fsctfState.frst.recursionDepth < 0.5 && fsctfState.cosmogenesis.phase === 1) {
        barriers.push('Recursion depth too low for phase progression');
      }
      if (fsctfState.frst.coherenceScore < 0.3 && fsctfState.cosmogenesis.phase === 2) {
        barriers.push('Coherence score too low for phase 3');
      }
      
      barriers.forEach(barrier => console.log(`  ❌ ${barrier}`));
      
      if (barriers.length === 0) {
        console.log('  ✅ No obvious barriers - complexity should be emerging');
      } else {
        console.log(`\n🚀 SOLUTIONS:`);
        console.log('  - Press F key to force phase advancement');
        console.log('  - Press T key to manually cycle topology');
        console.log('  - Wait for morphic strands to develop');
      }
      
    } else {
      console.log('❌ FSCTF Engine not available');
    }
    console.log('═══════════════════════════════════════════════');
  });
  
  testContainer.appendChild(toggleRotateBtn);
  testContainer.appendChild(toggleWireBtn);
  testContainer.appendChild(debugCosmosBtn);
  testContainer.appendChild(forcePhaseBtn);
  testContainer.appendChild(manualModeBtn);
  testContainer.appendChild(forceTopologyBtn);
  testContainer.appendChild(mathTheoryBtn);
  testContainer.appendChild(complexityBtn);
  
  // Add camera preset section
  const cameraLabel = document.createElement('div');
  cameraLabel.textContent = '📸 Camera Presets:';
  cameraLabel.style.cssText = 'color: #9cf; font-size: 11px; margin: 8px 0 4px 0; font-weight: bold;';
  testContainer.appendChild(cameraLabel);
  
  const cameraRow1 = document.createElement('div');
  cameraRow1.style.cssText = 'margin: 2px 0;';
  cameraRow1.appendChild(presetOverviewBtn);
  cameraRow1.appendChild(presetSymmetryBtn);
  cameraRow1.appendChild(presetDetailBtn);
  cameraRow1.appendChild(testOrbitBtn);
  testContainer.appendChild(cameraRow1);
  
  const cameraRow2 = document.createElement('div');
  cameraRow2.style.cssText = 'margin: 2px 0;';
  cameraRow2.appendChild(presetPhiBtn);
  cameraRow2.appendChild(emergencyBtn);
  cameraRow2.appendChild(resetCameraBtn);
  testContainer.appendChild(cameraRow2);
  
  // Add mouse controls info
  const mouseInfo = document.createElement('div');
  mouseInfo.innerHTML = '🖱️ Drag to orbit • Scroll to zoom<br>⌨️ Keys: 0=reset • 1-8 presets • 9=test orbit • R rotate • W wireframe • F phase • Q manual mode • D debug • T cycle shapes • M math • C complexity';
  mouseInfo.style.cssText = 'color: #678; font-size: 9px; margin: 4px 0; font-style: italic; line-height: 1.3;';
  testContainer.appendChild(mouseInfo);
  
  statsSection.parentElement.insertBefore(testContainer, statsSection);

  // Hide legacy panel to remove menu cruft; replaced by compact panel below
  testContainer.style.display = 'none';

  // Compact, modern control panel (minimal, wired to current systems)
  const panel = document.createElement('div');
  panel.id = 'control-panel';
  panel.style.cssText = 'position:fixed; top:10px; right:10px; width:280px; z-index:1000; background:rgba(10,12,18,0.9); border:1px solid #234; border-radius:8px; padding:10px; font:11px/1.3 monospace; color:#cde; box-shadow:0 6px 16px rgba(0,0,0,0.35)';
  panel.innerHTML = `
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
      <div style="font-weight:700; color:#8cf;">FIRM Controls</div>
      <div id="cp-phase" style="font-weight:700; color:#9f9;">Phase --</div>
    </div>
    <div style="display:grid; grid-template-columns: 1fr auto; gap:6px; align-items:center;">
      <!-- Brightness control removed to eliminate duplication -->
      <label>Exposure</label><input id="cp-exposure" type="range" min="0.5" max="2.0" step="0.01">
      <label>Point Size</label><input id="cp-pointsize" type="range" min="1" max="25" step="0.1">
      <label>Wireframe</label><input id="cp-wireframe" type="checkbox">
    </div>
    <div style="display:flex; gap:6px; margin-top:8px;">
      <button id="cp-manual" style="flex:1; background:#234; color:#9c8; border:1px solid #395; padding:5px; border-radius:4px; cursor:pointer;">Manual: OFF</button>
      <button id="cp-force" style="flex:1; background:#452; color:#fc6; border:1px solid #764; padding:5px; border-radius:4px; cursor:pointer;">Force Phase</button>
    </div>
    <div id="cp-perf" style="margin-top:8px; color:#8a9; font-size:10px;">Frame: -- ms</div>
  `;
  document.body.appendChild(panel);

  // Wire controls
  const el = id => panel.querySelector(id);
  // Removed brightness slider reference - removing duplicate control
  const elE = el('#cp-exposure');       // Keep exposure control
  const elP = el('#cp-pointsize');      // Keep point size control
  const elW = el('#cp-wireframe');
  const elM = el('#cp-manual');
  const elF = el('#cp-force');
  const elPhase = el('#cp-phase');
  const elPerf = el('#cp-perf');

  // Initialize from current params if available
  requestAnimationFrame(()=>{
    try {
      if (window.params) {
        // No brightness setup - eliminated duplicate control
        elE.value = (window.params.exposure ?? 1.0);
        elP.value = (window.params.pointSize ?? 2.0);
        elW.checked = !!window.params.showWireframe;
      }
    } catch(_){}
  });

  const markManual = (paramName = null) => {
    // Properly register manual parameter change with VisualController  
    const vc = simulationCore?.fsctfEngine?.visualController;
    if (vc) {
      vc.lastManualChange = Date.now();
      // If specific parameter provided, register it as manually overridden
      if (paramName && window.params && window.params[paramName] !== undefined) {
        const currentValue = window.params[paramName];
        const timestamp = Date.now();
        vc.manualOverrides.set(paramName, {
          value: currentValue,
          timestamp: timestamp,
          source: 'user_ui_explicit'
        });
        console.log(`🎛️ STRONG Manual override registered for ${paramName}: ${currentValue} at ${timestamp}`);
        console.log(`   Override will persist for ${(vc.manualOverrideTimeout/1000)} seconds`);
        
        // Also set a backup in case something clears the main overrides
        window._manualOverrideBackup = window._manualOverrideBackup || {};
        window._manualOverrideBackup[paramName] = {
          value: currentValue,
          timestamp: timestamp
        };
      }
    }
  };

  // Brightness control removed to eliminate duplication
  elE.addEventListener('input', ()=>{ if (!window.params) return; window.params.exposure = parseFloat(elE.value); markManual('exposure'); });
  elP.addEventListener('input', ()=>{ if (!window.params) return; window.params.pointSize = parseFloat(elP.value); markManual('pointSize'); });
  elW.addEventListener('change', ()=>{ if (!window.params) return; window.params.showWireframe = !!elW.checked; markManual('showWireframe'); });

  elM.addEventListener('click', ()=>{
    const vc = simulationCore?.fsctfEngine?.visualController;
    if (!vc) return;
    const on = vc.toggleManualMode();
    elM.textContent = on ? 'Manual: ON' : 'Manual: OFF';
    elM.style.background = on ? '#353' : '#234';
  });

  elF.addEventListener('click', ()=>{
    const eng = simulationCore?.fsctfEngine;
    if (!eng) return;
    eng.forcePhaseAdvancement();
  });

  // Live status updater
  (function updatePanel(){
    const eng = simulationCore?.fsctfEngine;
    if (eng) {
      const ph = eng.cosmogenesisPhase || 0;
      elPhase.textContent = `Phase ${ph}`;
    }
    if (window.lastFrameTime) elPerf.textContent = `Frame: ${window.lastFrameTime.toFixed(1)} ms`;
    requestAnimationFrame(updatePanel);
  })();
}

/**
 * Smart Orbital Camera System - Perfect Particle Framing
 * Camera intelligently tracks particle center and maintains optimal viewing
 */
function updateOrbitalCamera(time) {
  updateOrbitalCamera.callCount = (updateOrbitalCamera.callCount || 0) + 1;
  const isFirstCall = updateOrbitalCamera.callCount === 1;
  
  // Get particle system center (Grace center for smart tracking)
  let particleCenterX = 0.0, particleCenterY = 0.0;
  
  const graceState = simulationCore?.fsctfEngine?.graceOperator?.getState() || {};
  const morphicStrands = graceState?.strands || [];
  if (morphicStrands.length > 0) {
    const dominantStrand = morphicStrands.reduce((best, strand) => 
      strand.stability > best.stability ? strand : best);
    particleCenterX = dominantStrand.x || 0.0;
    particleCenterY = dominantStrand.y || 0.0;
  }
  
  // Smart distance adjustment for perfect framing (reduced for better early stage visibility)
  const baseDistance = 4.0;  // Reduced from 10.0 to keep camera closer
  const activityLevel = Math.min(2.0, Math.max(0.6, morphicStrands.length * 0.15 + 0.8));  // More conservative scaling
  const smartDistance = baseDistance * activityLevel;
  
  // Respect manual zoom - only adjust distance if extremely far off to prevent getting lost
  if (Math.abs(params.cameraDistance - smartDistance) > 15.0) {
    const adjustment = (smartDistance - params.cameraDistance) * 0.005; // Much gentler adjustment
    params.cameraDistance += adjustment;
  }
  
  // Simple, fast auto-rotation - direct speed control
  if (params.autoRotate) {
    // Clean rotation: direct degrees per frame
    params.cameraAzimuth += params.autoRotateSpeed * 0.5; // 1.0 degree per frame = 60°/sec
    if (params.cameraAzimuth >= 360) params.cameraAzimuth -= 360;
    if (params.cameraAzimuth < 0) params.cameraAzimuth += 360;
  }
  
  // Convert to radians
  const azimuthRad = (params.cameraAzimuth * Math.PI) / 180;
  const elevationRad = (params.cameraElevation * Math.PI) / 180;
  
  // Camera orbits around particle center (not origin)
  const cosElev = Math.cos(elevationRad);
  const sinElev = Math.sin(elevationRad);
  const cosAzim = Math.cos(azimuthRad);  
  const sinAzim = Math.sin(azimuthRad);
  
  // Position camera relative to particle center
  params.cameraX = particleCenterX + params.cameraDistance * cosElev * cosAzim;
  params.cameraY = particleCenterY + params.cameraDistance * sinElev;
  params.cameraZ = 0.0 + params.cameraDistance * cosElev * sinAzim;
  
  // Camera looks at particle center
  const toCenterX = particleCenterX - params.cameraX;
  const toCenterY = particleCenterY - params.cameraY;  
  const toCenterZ = 0.0 - params.cameraZ;
  const toCenterLen = Math.sqrt(toCenterX*toCenterX + toCenterY*toCenterY + toCenterZ*toCenterZ);
  
  // CRITICAL: NaN PROTECTION - Prevent division by zero in camera vectors
  if (toCenterLen > 1e-8) {
    params.cameraForwardX = toCenterX / toCenterLen;
    params.cameraForwardY = toCenterY / toCenterLen;
    params.cameraForwardZ = toCenterZ / toCenterLen;
  } else {
    // Fallback to default forward vector if camera at particle center
    console.warn('Camera too close to particle center, using fallback forward vector');
    params.cameraForwardX = 0.0;
    params.cameraForwardY = 0.0;
    params.cameraForwardZ = -1.0;
  }
  
  // Right vector (cross product with world up)
  const rightX = params.cameraForwardY * 0 - params.cameraForwardZ * 1;
  const rightY = params.cameraForwardZ * 0 - params.cameraForwardX * 0;  
  const rightZ = params.cameraForwardX * 1 - params.cameraForwardY * 0;
  const rightLen = Math.sqrt(rightX*rightX + rightY*rightY + rightZ*rightZ);
  
  // CRITICAL: NaN PROTECTION - Prevent division by zero in right vector
  if (rightLen > 1e-8) {
    params.cameraRightX = rightX / rightLen;
    params.cameraRightY = rightY / rightLen;
    params.cameraRightZ = rightZ / rightLen;
  } else {
    // Fallback to default right vector if forward is parallel to up
    console.warn('Camera forward parallel to up, using fallback right vector');
    params.cameraRightX = 1.0;
    params.cameraRightY = 0.0;
    params.cameraRightZ = 0.0;
  }
  
  // Up vector (cross product of right and forward)
  params.cameraUpX = params.cameraRightY * params.cameraForwardZ - params.cameraRightZ * params.cameraForwardY;
  params.cameraUpY = params.cameraRightZ * params.cameraForwardX - params.cameraRightX * params.cameraForwardZ;
  params.cameraUpZ = params.cameraRightX * params.cameraForwardY - params.cameraRightY * params.cameraForwardX;
  
  // Debug info on startup
  if (isFirstCall) {
    console.log('🎥 Smart Camera: Perfect framing with particle tracking enabled');
    console.log(`   Rotation: ${(params.autoRotateSpeed * 0.5 * 60).toFixed(0)}°/sec`);
    console.log(`   Tracking center: (${particleCenterX.toFixed(2)}, ${particleCenterY.toFixed(2)})`);
  }
}

/**
 * Camera Preset System
 * Provides optimal viewing angles for different types of analysis
 */
function setCameraPreset(presetName) {
  const presets = {
    'default': {
      cameraDistance: 2.2,    // Very close for immediate visibility
      cameraAzimuth: 45.0,
      cameraElevation: 15.0,  // Slight angle to see 3D structure
      fov: 70.0,              // Very wide FOV for maximum coverage
      description: 'Default close-up view ensuring particles are immediately visible'
    },
    'overview': {
      cameraDistance: 8.0,    // Closer for better visibility
      cameraAzimuth: 45.0,
      cameraElevation: 20.0,  // Lower angle
      fov: 45.0,              // Standard FOV
      description: 'Wide view showing overall structure and flow patterns'
    },
    'debug': {
      cameraDistance: 5.0,    // Very close for debugging
      cameraAzimuth: 0.0,     // Straight ahead
      cameraElevation: 0.0,   // Horizontal
      fov: 45.0,
      description: 'Close debug view - should always show particles'
    },
    'emergency': {
      cameraDistance: 2.0,    // VERY close 
      cameraAzimuth: 0.0,     // Dead center
      cameraElevation: 0.0,   // Horizontal
      fov: 60.0,              // Wide FOV
      description: 'EMERGENCY: Closest possible view - particles must be visible'
    },
    'test-orbit': {
      cameraDistance: 6.0,    // Medium distance for testing 
      cameraAzimuth: 0.0,     // Start at front
      cameraElevation: 0.0,   // Horizontal
      fov: 45.0,
      description: 'TEST: Good for testing orbital camera - particles should stay centered during auto-rotate'
    },
    'symmetry-xy': {
      cameraDistance: 8.0,
      cameraAzimuth: 0.0,
      cameraElevation: 90.0,
      fov: 45.0,
      description: 'Top-down view perfect for XY-plane symmetries'
    },
    'symmetry-xz': {
      cameraDistance: 8.0,
      cameraAzimuth: 90.0,
      cameraElevation: 0.0,
      fov: 45.0,
      description: 'Side view perfect for XZ-plane symmetries'
    },
    'symmetry-yz': {
      cameraDistance: 8.0,
      cameraAzimuth: 0.0,
      cameraElevation: 0.0,
      fov: 45.0,
      description: 'Front view perfect for YZ-plane symmetries'
    },
    'phi-golden': {
      cameraDistance: 10.0,
      cameraAzimuth: 137.5,  // Golden angle
      cameraElevation: 26.6, // φ-derived angle
      fov: 48.0,
      description: 'φ-optimized view revealing golden ratio structures'
    },
    'detail': {
      cameraDistance: 4.0,
      cameraAzimuth: 30.0,
      cameraElevation: 20.0,
      fov: 35.0,
      description: 'Close-up view for detailed particle behavior analysis'
    },
    'morphic': {
      cameraDistance: 15.0,
      cameraAzimuth: 60.0,
      cameraElevation: 45.0,
      fov: 60.0,
      description: 'Wide angle view optimized for morphic field visualization'
    },
    'topology': {
      cameraDistance: 9.0,
      cameraAzimuth: 135.0,
      cameraElevation: 35.0,
      fov: 55.0,
      description: 'Angled view perfect for topology transitions'
    }
  };
  
  const preset = presets[presetName];
  if (preset) {
      // Apply preset values
  params.cameraDistance = preset.cameraDistance;
  params.cameraAzimuth = preset.cameraAzimuth;
  params.cameraElevation = preset.cameraElevation;
  params.fov = preset.fov;
  
  // Special handling for emergency mode
  if (presetName === 'emergency') {
    params.pointSize = Math.max(params.pointSize, 3.0); // Larger points for better visibility
    console.log('🚨 EMERGENCY: Enhanced point size =', params.pointSize);
  }
    
    console.log(`📸 Camera preset "${presetName}": ${preset.description}`);
    
    // Update camera position and orientation immediately
    updateOrbitalCamera();
    
    return preset.description;
  } else {
    console.warn(`📸 Unknown camera preset: ${presetName}`);
    return null;
  }
}

/**
 * Mouse Controls for Camera
 * Drag to orbit around center point
 */
let mouseControls = {
  isDragging: false,
  lastMouseX: 0,
  lastMouseY: 0,
  mouseSensitivity: 0.5
};

/**
 * Wire up learning panel controls
 */
function wireUpLearningControls() {
  // Wire up controls in the Geometric Foundation panel
  const rotateBtn = document.getElementById('rotate-btn');
  const resetCameraBtn = document.getElementById('reset-camera-btn');
  
  if (rotateBtn) {
    rotateBtn.addEventListener('click', () => {
      if (!window.params) return;
      window.params.autoRotate = !window.params.autoRotate;
      rotateBtn.classList.toggle('active', window.params.autoRotate);
      console.log(`🔄 Auto-rotation ${window.params.autoRotate ? 'enabled' : 'disabled'}`);
    });
  }
  
  if (resetCameraBtn) {
    resetCameraBtn.addEventListener('click', () => {
      setCameraPreset('overview');
      console.log('🎥 Camera reset to overview position');
    });
  }
  
  // Set initial state for buttons based on current params
  if (rotateBtn && window.params) {
    rotateBtn.classList.toggle('active', window.params.autoRotate);
  }
  
  console.log('🎓 Learning panel controls initialized');
}

/**
 * Initialize mouse controls for camera
 */
function initializeMouseControls() {
  const canvas = document.querySelector('canvas');
  if (!canvas) return;
  
  canvas.addEventListener('mousedown', (e) => {
    if (e.button === 0) { // Left mouse button
      mouseControls.isDragging = true;
      mouseControls.lastMouseX = e.clientX;
      mouseControls.lastMouseY = e.clientY;
      canvas.style.cursor = 'grabbing';
      e.preventDefault();
    }
  });
  
  canvas.addEventListener('mousemove', (e) => {
    if (mouseControls.isDragging) {
      const deltaX = e.clientX - mouseControls.lastMouseX;
      const deltaY = e.clientY - mouseControls.lastMouseY;
      
      // Update azimuth (horizontal drag)
      params.cameraAzimuth += deltaX * mouseControls.mouseSensitivity * params.cameraSpeed;
      if (params.cameraAzimuth > 360) params.cameraAzimuth -= 360;
      if (params.cameraAzimuth < 0) params.cameraAzimuth += 360;
      
      // Update elevation (vertical drag)
      params.cameraElevation -= deltaY * mouseControls.mouseSensitivity * params.cameraSpeed;
      params.cameraElevation = Math.max(-89.9, Math.min(89.9, params.cameraElevation));
      
      mouseControls.lastMouseX = e.clientX;
      mouseControls.lastMouseY = e.clientY;
      
      // Keep auto-rotate on - users can disable it manually if desired
      // Removed aggressive auto-disable to respect user preferences
      
      e.preventDefault();
    }
  });
  
  canvas.addEventListener('mouseup', (e) => {
    if (e.button === 0) {
      mouseControls.isDragging = false;
      canvas.style.cursor = 'grab';
    }
  });
  
  // Mouse wheel for zooming
  canvas.addEventListener('wheel', (e) => {
    const zoomSpeed = 0.1;
    const zoomDelta = e.deltaY * zoomSpeed;
    
    params.cameraDistance = Math.max(1.0, Math.min(50.0, params.cameraDistance + zoomDelta));
    
    e.preventDefault();
  });
  
  canvas.style.cursor = 'grab';
  
  // Keyboard shortcuts for camera presets
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey || e.metaKey) return; // Don't interfere with browser shortcuts
    
    switch(e.key.toLowerCase()) {
      case '0': // Emergency camera reset
        setCameraPreset('emergency');
        params.autoRotate = false;
        if (window.updateRotateButton) window.updateRotateButton();
        console.log('🚨 EMERGENCY: Camera reset to show particles');
        break;
      case '1': setCameraPreset('overview'); break;
      case '2': setCameraPreset('symmetry-xy'); break;
      case '3': setCameraPreset('symmetry-xz'); break;
      // EMERGENT COMPLEXITY TEST: Directly jump to hypercube phases
      case '4': 
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 4;
          console.log('🧊 JUMPED TO PHASE 4: Coherence topology - HYPERCUBE EMERGENCE TEST');
          console.log('   Expected: 4D hypercube projections should now be visible');
        }
        break;
      case '5':
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 5;
          console.log('🌟 JUMPED TO PHASE 5: Soul emergence - TESSERACT STRUCTURES TEST');
          console.log('   Expected: Advanced hyperdimensional geometry');
        }
        break;
      case '6':
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 6;
          console.log('🌌 JUMPED TO PHASE 6: Cosmic inflation - 5D HYPERCUBE NETWORKS TEST');
          console.log('   Expected: Maximum geometric complexity');
        }
        break;
      case '7':
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 7;
          console.log('🔥 JUMPED TO PHASE 7: CMB formation - FRACTAL HYPERCUBE CASCADES TEST');
          console.log('   Expected: Fractal hypercube cascades');
        }
        break;
      case '8':
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 8;
          console.log('♾️ JUMPED TO PHASE 8: Observable universe - INFINITE RECURSIVE HYPERCUBES TEST');
          console.log('   Expected: Maximum emergent complexity, infinite recursive structures');
        }
        break;
      // ADVANCED EMERGENT COMPLEXITY BEYOND HYPERCUBES
      case 'q': // Phase 12 - Shadow hypercubes
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 12;
          console.log('🌑 JUMPED TO PHASE 12: Dark ages - SHADOW HYPERCUBES TEST');
          console.log('   Expected: Dark universe shadow geometry with reduced brightness');
        }
        break;
      case 'w': // Phase 16 - Planetary systems
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 16;
          console.log('🪐 JUMPED TO PHASE 16: Solar system formation - PLANETARY HYPERCUBE SYSTEMS');
          console.log('   Expected: Complex planetary system geometries');
        }
        break;
      case 'e': // Phase 31 - Quantum gravity
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 31;
          console.log('⚛️ JUMPED TO PHASE 31: QUANTUM GRAVITY THRESHOLD - φ^31 SCALE');
          console.log('   Expected: Fundamental physics transitions, spacetime quantization');
        }
        break;
      case 't': // Phase 90 - Ultimate
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.cosmogenesisPhase = 90;
          console.log('🌌 JUMPED TO PHASE 90: ULTIMATE FSCTF COMPLETION');
          console.log('   Expected: Maximum possible emergent complexity');
        }
        break;
      case '9': // Test orbital camera
        setCameraPreset('test-orbit');
        params.autoRotate = true;
        if (window.updateRotateButton) window.updateRotateButton();
        console.log('🔄 ORBIT TEST: Testing orbital camera with auto-rotate');
        break;
      case 'h': // Help - show keyboard shortcuts
        console.log('🚀 FSCTF KEYBOARD SHORTCUTS:');
        console.log('  HYPERCUBE PHASES: 4, 5, 6, 7, 8 → Jump to cosmic phases 4-8');
        console.log('  ADVANCED PHASES: Q→12 (Shadow), W→16 (Planetary), E→31 (Quantum Gravity), T→90 (Ultimate)');
        console.log('  PROGRESSION: F → Force next phase');
        console.log('  CAMERA: 1-3 → Symmetry views, 0 → Emergency reset, 9 → Orbit test');
        console.log('  DEBUG: D → System state, R → Auto-rotate, H → This help');
        break;
      case 'r': 
        params.autoRotate = !params.autoRotate; 
        console.log('📸 Auto-rotate:', params.autoRotate ? 'ENABLED' : 'DISABLED'); 
        // Update button state if it exists
        if (window.updateRotateButton) window.updateRotateButton();
        break;
      case 'w': /* wireframe removed */ break;
      case 'f': // Force phase advancement
        if (simulationCore?.fsctfEngine) {
          simulationCore.fsctfEngine.forcePhaseAdvancement();
          if (window.progressiveCosmogenesis) {
            const enginePhase = simulationCore.fsctfEngine.cosmogenesisPhase;
            // Ensure phase display stays within bounds (UI uses 0-89 for phases 1-90)
            // Double safety clamp to prevent any possibility of currentPhase > 89  
            const rawDisplayPhase = enginePhase - 1;
            window.progressiveCosmogenesis.currentPhase = Math.max(0, Math.min(89, rawDisplayPhase));
            console.log(`🛡️ Keyboard phase bounds: engine=${enginePhase} → raw=${rawDisplayPhase} → clamped=${window.progressiveCosmogenesis.currentPhase}`);
            
            // EMERGENT COMPLEXITY DIAGNOSTIC - Extended to cover all advanced phases
            if (enginePhase >= 4 && enginePhase <= 16) {
              const phaseTypes = {
                4: 'HYPERCUBE EMERGENCE', 5: 'TESSERACT STRUCTURES', 6: '5D HYPERCUBE NETWORKS',
                7: 'FRACTAL HYPERCUBE CASCADES', 8: 'INFINITE RECURSIVE HYPERCUBES',
                9: 'HYPERCUBE NETWORKS', 10: 'FRACTAL HYPERCUBE MATRICES', 11: 'HYPERCUBE CRYSTALLIZATION',
                12: 'SHADOW HYPERCUBES', 13: 'STELLAR HYPERCUBE BIRTH', 14: 'GALACTIC HYPERCUBE SPIRALS',
                15: 'METALLIC HYPERCUBE LATTICES', 16: 'PLANETARY HYPERCUBE SYSTEMS'
              };
              console.log(`🌟 ADVANCED PHASE ${enginePhase} ACTIVE - ${phaseTypes[enginePhase]} SHOULD BE VISIBLE!`);
              console.log(`   visualEffects: ${window.params.visualEffects || 'undefined'}`);
              console.log(`   graceComplexity: ${window.params.graceComplexity || 'undefined'}`);
              console.log(`   morphicRecursionDepth: ${window.params.morphicRecursionDepth || 'undefined'}`);
              console.log(`   consciousnessComplexity: ${window.params.consciousnessComplexity || 'undefined'}`);
              console.log(`   Expected: visualEffects > 0.7, cosmic-scale complexity parameters`);
            } else if (enginePhase >= 17 && enginePhase <= 31) {
              console.log(`🔬 THEORETICAL PHASE ${enginePhase} - Advanced physics regime`);
            } else if (enginePhase >= 32) {
              console.log(`⚛️ QUANTUM COSMOLOGICAL PHASE ${enginePhase} - φ^${enginePhase} scale`);
            }
          }
          console.log('🚀 KEYBOARD: Forced phase advancement');
        }
        break;
      case 'd': // Debug cosmogenesis state
        const fsctfState = simulationCore?.fsctfEngine?.getState();
        if (fsctfState) {
          console.log('🧠 DEBUG VALUES:', {
            phase: fsctfState.cosmogenesis.phase,
            recursionDepth: fsctfState.frst.recursionDepth,
            coherenceScore: fsctfState.frst.coherenceScore,
            soulStatus: fsctfState.frst.soulStatus,
            morphicField: fsctfState.grace.field,
            strandCount: fsctfState.strands.count
          });
        }
        break;
      case 't': // Manual topology cycling
        const current = params.manualTopologyMode;
        const next = (current + 1) % 5; // 5 topologies (0-4)
        
        // Update both the manual override and the actual topology
        params.manualTopologyEnabled = true;
        params.manualTopologyMode = next;
        
        // Update UI if elements exist
        const checkbox = document.getElementById('manual-topology-enabled');
        const select = document.getElementById('manual-topology-mode');
        if (checkbox) checkbox.checked = true;
        if (select) select.value = next;
        
        const topologyNames = ['Torus', 'Möbius', 'Klein', 'φ-Klein', 'Sphere'];
        console.log('🌀 KEYBOARD: Manual topology ->', topologyNames[next]);
        break;
      case 'q': // Toggle manual mode for visual parameters
        if (simulationCore?.fsctfEngine?.visualController) {
          const isManual = simulationCore.fsctfEngine.visualController.toggleManualMode();
          console.log(`🎛️ KEYBOARD: Manual mode ${isManual ? 'ENABLED' : 'DISABLED'} - sliders ${isManual ? 'will persist' : 'auto-controlled'}`);
        }
        break;
      case 'm': // Show mathematical theory
        if (simulationCore?.fsctfEngine?.topologyManager) {
          console.log('🧮 KEYBOARD: Displaying mathematical manifold progression theory');
          simulationCore.fsctfEngine.topologyManager.displayMathematicalProgression();
        }
        break;
      case 'c': // Shortcut repurposed for camera reset
        setCameraPreset('overview');
        console.log('🎥 KEYBOARD: Camera reset to overview');
        break;
      case 'p': // Phase information display with status update
        console.log('📊 KEYBOARD: Phase Information & Status Update');
        
        // Force update enhanced phase status immediately
        updateEnhancedPhaseStatus();
        
        // Scroll to and highlight phase status display
        const phaseStatusEl = document.getElementById('enhanced-phase-status');
        if (phaseStatusEl) {
          phaseStatusEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          // Add temporary highlight effect
          phaseStatusEl.style.boxShadow = '0 0 20px rgba(0,150,255,0.8)';
          setTimeout(() => {
            phaseStatusEl.style.boxShadow = '0 2px 8px rgba(0,150,255,0.3)';
          }, 2000);
        }
        
        // Show current phase information in console with physics details
        if (window.progressiveCosmogenesis && window.progressiveCosmogenesis.active) {
          const phase = window.progressiveCosmogenesis.currentPhase;
          const phaseName = window.progressiveCosmogenesis.phases[phase] || 'UNKNOWN';
          const visualStatus = phase <= 15 ? '[VISUAL]' : '[THEORETICAL]';
          console.log(`📊 CURRENT PHASE: ${phase + 1}/90 - ${phaseName} ${visualStatus}`);
          // Trigger phase status update to get latest physics info displayed in UI
          updateEnhancedPhaseStatus();
          console.log('🎯 Enhanced phase status display updated and highlighted - check UI for complete φ^0→φ^90 info');
        } else {
          console.log('📊 Phase system inactive - click "INVOKE RECURSIVE GENESIS" to begin 90-phase Theory of Everything sequence');
        }
        
        if (window.phaseInfoSystem) {
          console.log('🔍 Phase Info System available - check Advanced UI panel for detailed phase database');
          const phaseInfoEl = document.getElementById('phase-info-display');
          if (phaseInfoEl) {
            phaseInfoEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
        } else {
          console.log('⚠️ Detailed Phase Info System not yet loaded - check Advanced UI panel');
        }
        break;
      case 'b': // Mirror emergence analysis (Bireflection analysis)
        console.log('🪞 KEYBOARD: Mirror Emergence Analysis');
        if (window.generateMirrorEmergenceReport) {
          const report = window.generateMirrorEmergenceReport();
          console.log('🌟 Stage 8+ bifurcation analysis complete - see detailed MET report above');
        } else {
          console.log('⚠️ Mirror Emergence Tracker not available - check Advanced UI panel');
        }
        break;
      case 'x': // Meta-recursion complexity analysis
        console.log('🌀 KEYBOARD: Meta-Recursion Engine Complexity Analysis');
        if (window.generateComplexityReport) {
          const report = window.generateComplexityReport();
          console.log('🌟 Advanced emergent complexity analysis complete - see detailed MRE report above');
        } else {
          console.log('⚠️ Meta-Recursion Engine not available - check Advanced UI panel');
        }
        break;

    }
  });
  
  console.log('🖱️ Mouse camera controls initialized - drag to orbit, scroll to zoom');
  console.log('⌨️  Keyboard shortcuts: 0=reset, 1-8=presets, 9=test orbit, R=auto-rotate, W=wireframe, F=force phase, D=debug, T=cycle topology, M=math theory, C=camera overview, P=phase info, B=mirror analysis, X=complexity report');
}

// Export for debugging AND parameter system access
window.simulationCore = simulationCore;
window.fsctfEngine = simulationCore?.fsctfEngine;
window.gpuOptimizer = gpuOptimizer;

// GPU Optimizer control functions
window.updateParticleResolution = (cols, rows) => {
  // Update global particle parameters
  if (cols && rows) {
    window.COLS = cols;
    window.ROWS = rows; 
    window.NUM = cols * rows;
    console.log(`🔧 Particle resolution updated: ${cols}×${rows} = ${(window.NUM/1000).toFixed(0)}K particles`);
    
    // TODO: Recreate WebGL buffers with new particle count
    // This requires significant refactoring to be implemented properly
    console.log('⚠️ Note: Particle buffer recreation not yet implemented - restart required for changes');
  }
};

window.setGPUQuality = (presetName) => {
  if (gpuOptimizer) {
    return gpuOptimizer.setQualityPreset(presetName, false);
  }
  return false;
};

window.toggleGPUAutoAdaptation = () => {
  if (gpuOptimizer) {
    const wasEnabled = gpuOptimizer.autoAdaptationEnabled;
    gpuOptimizer.setAutoAdaptation(!wasEnabled);
    return !wasEnabled;
  }
  return false;
};

window.getGPUPerformanceStats = () => {
  return gpuOptimizer ? gpuOptimizer.getPerformanceStats() : null;
};

window.generateGPUReport = () => {
  return gpuOptimizer ? gpuOptimizer.generatePerformanceReport() : null;
};

// Mirror Emergence Tracker control functions (Stage 8+ bifurcation analysis)
window.getMirrorEmergenceState = () => {
  return window.simulationCore?.fsctfEngine?.getMirrorEmergenceState() || null;
};

window.generateMirrorEmergenceReport = () => {
  if (window.simulationCore?.fsctfEngine?.generateMirrorEmergenceReport) {
    return window.simulationCore.fsctfEngine.generateMirrorEmergenceReport();
  }
  return null;
};

// Meta-Recursion Engine control functions (Advanced emergent complexity)
window.getMetaRecursionState = () => {
  return window.simulationCore?.fsctfEngine?.getMetaRecursionState() || null;
};

window.generateComplexityReport = () => {
  if (window.simulationCore?.fsctfEngine?.generateComplexityReport) {
    return window.simulationCore.fsctfEngine.generateComplexityReport();
  }
  return null;
};

// Initialize when DOM is loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
