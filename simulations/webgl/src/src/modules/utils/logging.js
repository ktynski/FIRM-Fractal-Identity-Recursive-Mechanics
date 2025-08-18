/**
 * Logging Utilities
 * Verbose and warning logging functions
 */

// Global verbose flag
let VERBOSE = false;

/**
 * Set verbose logging mode
 * @param {boolean} enabled - Whether to enable verbose logging
 */
export function setVerbose(enabled) {
  VERBOSE = enabled;
  console.log(`🔧 Verbose logging ${enabled ? 'enabled' : 'disabled'}`);
}

/**
 * Get current verbose state
 * @returns {boolean} Current verbose state
 */
export function isVerbose() {
  return VERBOSE;
}

/**
 * Verbose log - only logs if verbose mode is enabled
 */
export function vlog() {
  if (VERBOSE) {
    console.log.apply(console, arguments);
  }
}

/**
 * Verbose warning - only logs if verbose mode is enabled
 */
export function vwarn() {
  if (VERBOSE) {
    console.warn.apply(console, arguments);
  }
}

/**
 * Always log (for important messages that ignore verbose setting)
 */
export function alog() {
  console.log.apply(console, arguments);
}

/**
 * Always warn (for important warnings that ignore verbose setting)
 */
export function awarn() {
  console.warn.apply(console, arguments);
}

/**
 * Performance log with timing
 * @param {string} label - Label for the operation
 * @param {function} fn - Function to execute and time
 * @returns {*} Result of the function
 */
export function perfLog(label, fn) {
  const start = performance.now();
  const result = fn();
  const elapsed = performance.now() - start;
  
  if (VERBOSE || elapsed > 10) { // Always log if slow
    console.log(`⏱️ ${label}: ${elapsed.toFixed(2)}ms`);
  }
  
  return result;
}

/**
 * Frame rate logging helper
 */
export class FrameLogger {
  constructor(interval = 1000) {
    this.frameCount = 0;
    this.lastTime = performance.now();
    this.interval = interval;
    this.fps = 0;
  }
  
  tick() {
    this.frameCount++;
    const now = performance.now();
    
    if (now - this.lastTime >= this.interval) {
      this.fps = (this.frameCount * 1000) / (now - this.lastTime);
      
      if (VERBOSE) {
        console.log(`📊 FPS: ${this.fps.toFixed(1)}`);
      }
      
      this.frameCount = 0;
      this.lastTime = now;
    }
    
    return this.fps;
  }
  
  getFPS() {
    return this.fps;
  }
}

// Export VERBOSE for external access
export { VERBOSE };
