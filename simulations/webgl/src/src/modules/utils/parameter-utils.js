/**
 * Parameter Utilities
 * Helper functions for parameter management and visualization updates
 */

export class ParameterUtils {
  constructor() {
    this.paramElements = new Map(); // Track UI parameter elements
    console.log('⚙️ Parameter Utilities initialized');
  }
  
  /**
   * Register parameter UI element
   */
  registerParamElement(name, element) {
    this.paramElements.set(name, element);
  }
  
  /**
   * Clamp value between 0 and 1
   */
  clamp01(x) {
    return Math.max(0, Math.min(1, x));
  }
  
  /**
   * Softmax selection for parameter optimization
   */
  softmaxPick(scores, temperature = 1.0) {
    if (!scores || scores.length === 0) return 0;
    
    const T = Math.max(1e-6, temperature);
    const maxScore = Math.max(...scores);
    
    // Compute softmax probabilities
    const exps = scores.map(s => Math.exp((s - maxScore) / T));
    const sum = exps.reduce((a, b) => a + b, 0);
    
    // Random selection based on probabilities
    let r = Math.random() * sum;
    let acc = 0;
    
    for (let i = 0; i < exps.length; i++) {
      acc += exps[i];
      if (r <= acc) return i;
    }
    
    return scores.length - 1;
  }
  
  /**
   * Create deep copy of parameters object
   */
  copyParams(params) {
    if (!params) return {};
    return JSON.parse(JSON.stringify(params));
  }
  
  /**
   * Apply parameter set to global params
   */
  applyParams(newParams, targetParams = null) {
    const target = targetParams || window.params;
    if (!target || !newParams) return;
    
    const oldParams = { ...target };
    Object.assign(target, newParams);
    
    // Update UI visualizations if elements are registered
    this.updateParamVisualizations(oldParams, target);
  }
  
  /**
   * Update parameter visualizations in UI
   */
  updateParamVisualizations(oldParams, currentParams = null) {
    const params = currentParams || window.params;
    if (!params) return;
    
    // Update sliders and highlight changes
    for (const [name, element] of this.paramElements.entries()) {
      if (params[name] !== undefined && params[name] !== element.lastValue) {
        // Update slider/input position
        if (element.input) {
          element.input.value = params[name];
        }
        
        // Update displayed value
        if (element.val) {
          const precision = this.getDisplayPrecision(params[name]);
          element.val.textContent = params[name].toFixed(precision);
        }
        
        // Highlight changed parameters
        if (oldParams && Math.abs(params[name] - (oldParams[name] || 0)) > 0.001) {
          this.highlightParameterChange(element);
        }
        
        element.lastValue = params[name];
      }
    }
  }
  
  /**
   * Highlight parameter change with visual feedback
   */
  highlightParameterChange(element) {
    if (!element.val) return;
    
    element.val.classList.add('param-change');
    
    // Remove highlight after animation
    setTimeout(() => {
      element.val.classList.remove('param-change');
    }, 1000);
  }
  
  /**
   * Get appropriate display precision for a value
   */
  getDisplayPrecision(value) {
    const absValue = Math.abs(value);
    
    if (absValue >= 100) return 1;
    if (absValue >= 10) return 2;
    if (absValue >= 1) return 3;
    if (absValue >= 0.1) return 4;
    return 6;
  }
  
  /**
   * Interpolate between two parameter sets
   */
  interpolateParams(paramsA, paramsB, t) {
    if (!paramsA || !paramsB) return paramsA || paramsB || {};
    
    const result = {};
    const keys = new Set([...Object.keys(paramsA), ...Object.keys(paramsB)]);
    
    for (const key of keys) {
      const valueA = paramsA[key] || 0;
      const valueB = paramsB[key] || 0;
      
      if (typeof valueA === 'number' && typeof valueB === 'number') {
        result[key] = valueA + (valueB - valueA) * t;
      } else {
        result[key] = t < 0.5 ? valueA : valueB;
      }
    }
    
    return result;
  }
  
  /**
   * Validate parameter bounds
   */
  validateParams(params, bounds = null) {
    if (!params) return {};
    
    const defaultBounds = {
      graceAmp: [0, 2],
      fieldScale: [0, 3],
      timeScale: [0, 3],
      damping: [0, 0.1],
      jitterSigma: [0, 0.2],
      devourerAmp: [0, 2],
      brightness: [0, 3],
      exposure: [0, 3],
      pointSize: [0.5, 5],
      trailFade: [0.8, 1],
      cameraZ: [1, 50],
      fov: [10, 120]
    };
    
    const paramBounds = bounds || defaultBounds;
    const validated = { ...params };
    
    for (const [key, value] of Object.entries(validated)) {
      if (typeof value === 'number' && paramBounds[key]) {
        const [min, max] = paramBounds[key];
        validated[key] = Math.max(min, Math.min(max, value));
      }
    }
    
    return validated;
  }
  
  /**
   * Generate random parameter variations
   */
  generateParamVariation(baseParams, variationAmount = 0.1) {
    if (!baseParams) return {};
    
    const variation = {};
    
    for (const [key, value] of Object.entries(baseParams)) {
      if (typeof value === 'number') {
        const noise = (Math.random() - 0.5) * 2 * variationAmount;
        variation[key] = Math.max(0, value * (1 + noise));
      } else {
        variation[key] = value;
      }
    }
    
    return variation;
  }
  
  /**
   * Calculate parameter difference/distance
   */
  paramDistance(paramsA, paramsB) {
    if (!paramsA || !paramsB) return Infinity;
    
    const keys = new Set([...Object.keys(paramsA), ...Object.keys(paramsB)]);
    let distance = 0;
    
    for (const key of keys) {
      const valueA = paramsA[key] || 0;
      const valueB = paramsB[key] || 0;
      
      if (typeof valueA === 'number' && typeof valueB === 'number') {
        distance += Math.pow(valueA - valueB, 2);
      }
    }
    
    return Math.sqrt(distance);
  }
  
  /**
   * Get parameter statistics
   */
  getParamStats(params) {
    if (!params) return {};
    
    const numericParams = Object.entries(params)
      .filter(([key, value]) => typeof value === 'number')
      .map(([key, value]) => ({ key, value }));
    
    if (numericParams.length === 0) {
      return { count: 0 };
    }
    
    const values = numericParams.map(p => p.value);
    const sum = values.reduce((a, b) => a + b, 0);
    const mean = sum / values.length;
    const variance = values.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / values.length;
    
    return {
      count: numericParams.length,
      mean,
      variance,
      stddev: Math.sqrt(variance),
      min: Math.min(...values),
      max: Math.max(...values),
      range: Math.max(...values) - Math.min(...values)
    };
  }
  
  /**
   * Clean up parameter utilities
   */
  cleanup() {
    this.paramElements.clear();
    console.log('⚙️ Parameter Utilities cleanup');
  }
}
