/**
 * Performance Monitoring Module
 * Real-time frame time tracking and adaptive complexity management
 */

export const PERFORMANCE_MONITOR = {
  // ANTI-STROBE: Removed array-based tracking, using exponential moving average
  avgFrameTime: null,      // Exponential moving average of frame times
  targetFrameTime: 33.33,  // 30 FPS target for 1M particles (more realistic than 60)
  adaptiveMode: false,     // DISABLED: Always use max complexity
  complexityThrottle: 1.0, // LOCKED: Always maximum complexity
  lastThrottleAdjustment: 0
};

// Initialize with confirmation message
console.log('🚀 PERFORMANCE SYSTEM: MAX COMPLEXITY LOCKED (adaptiveMode: false, throttle: 1.0, target: 30fps)');

/**
 * Update performance metrics with current frame time
 * @param {number} frameTime - Current frame time in milliseconds
 * @returns {number} Average frame time over the history window
 */
export function updatePerformanceMetrics(frameTime) {
  // ANTI-STROBE: Use exponential moving average - zero allocations, no GC pauses
  // Array operations (push/shift/reduce) were causing micro-hitches and strobing
  
  if (!PERFORMANCE_MONITOR.avgFrameTime) {
    PERFORMANCE_MONITOR.avgFrameTime = frameTime;
  }
  
  // Exponential moving average - much faster than array operations
  const smoothingFactor = 0.1; // 10% new data, 90% history
  PERFORMANCE_MONITOR.avgFrameTime = PERFORMANCE_MONITOR.avgFrameTime * (1 - smoothingFactor) + 
    frameTime * smoothingFactor;
    
  const avgFrameTime = PERFORMANCE_MONITOR.avgFrameTime;
  
  // FORCE MAX COMPLEXITY: Always maintain 1.0 throttle regardless of performance
  PERFORMANCE_MONITOR.complexityThrottle = 1.0;
  
  // Adaptive throttling DISABLED - user requested max complexity always
  // Legacy code kept but inactive:
  if (false && PERFORMANCE_MONITOR.adaptiveMode) {
    const now = performance.now();
    const timeSinceLastAdjustment = now - PERFORMANCE_MONITOR.lastThrottleAdjustment;
    
    // Only adjust throttle every second to avoid oscillation
    if (timeSinceLastAdjustment > 1000) {
      const targetRatio = PERFORMANCE_MONITOR.targetFrameTime;
      const performanceRatio = avgFrameTime / targetRatio;
      
      if (performanceRatio > 1.2 && PERFORMANCE_MONITOR.complexityThrottle > 0.5) {
        // Performance is poor, reduce complexity
        PERFORMANCE_MONITOR.complexityThrottle *= 0.95;
        console.log(`🔧 Performance optimization: Reducing complexity throttle to ${PERFORMANCE_MONITOR.complexityThrottle.toFixed(2)}`);
        PERFORMANCE_MONITOR.lastThrottleAdjustment = now;
      } else if (performanceRatio < 0.8 && PERFORMANCE_MONITOR.complexityThrottle < 1.0) {
        // Performance is good, can increase complexity
        PERFORMANCE_MONITOR.complexityThrottle = Math.min(1.0, PERFORMANCE_MONITOR.complexityThrottle * 1.02);
        console.log(`🔧 Performance optimization: Increasing complexity throttle to ${PERFORMANCE_MONITOR.complexityThrottle.toFixed(2)}`);
        PERFORMANCE_MONITOR.lastThrottleAdjustment = now;
      }
    }
  }
  
  return avgFrameTime;
}

/**
 * Get current performance status
 * @returns {Object} Performance status with rating and metrics
 */
export function getPerformanceStatus() {
  if (PERFORMANCE_MONITOR.frameTimeHistory.length === 0) {
    return {
      rating: 'unknown',
      fps: 0,
      avgFrameTime: 0,
      throttle: PERFORMANCE_MONITOR.complexityThrottle
    };
  }
  
  const avgFrameTime = PERFORMANCE_MONITOR.frameTimeHistory.reduce((sum, time) => sum + time, 0) 
    / PERFORMANCE_MONITOR.frameTimeHistory.length;
  const fps = avgFrameTime > 0 ? 1000 / avgFrameTime : 0;
  
  let rating = 'poor';
  if (fps >= 55) rating = 'excellent';
  else if (fps >= 45) rating = 'good';
  else if (fps >= 30) rating = 'fair';
  
  return {
    rating,
    fps,
    avgFrameTime,
    throttle: PERFORMANCE_MONITOR.complexityThrottle
  };
}

/**
 * Reset performance throttle to maximum complexity (ALWAYS MAX)
 */
export function resetPerformanceThrottle() {
  PERFORMANCE_MONITOR.complexityThrottle = 1.0; // Always max
  PERFORMANCE_MONITOR.lastThrottleAdjustment = performance.now();
  console.log('🔧 Complexity throttle: LOCKED AT MAXIMUM (1.0)');
}

/**
 * Enable or disable adaptive performance mode (DISABLED - ALWAYS MAX COMPLEXITY)
 * @param {boolean} enabled - Whether to enable adaptive performance (ignored)
 */
export function setAdaptiveMode(enabled) {
  PERFORMANCE_MONITOR.adaptiveMode = false; // Always disabled
  PERFORMANCE_MONITOR.complexityThrottle = 1.0; // Always max
  console.log(`🔧 Performance adaptive mode: DISABLED (max complexity locked)`);
}

/**
 * Adaptive update frequency manager
 */
export class AdaptiveUpdateManager {
  constructor() {
    this.updateIntervals = {
      critical: { soulEcho: 30, metaRecursion: 60, strandCleanup: 120 },
      poor: { soulEcho: 20, metaRecursion: 40, strandCleanup: 80 },
      fair: { soulEcho: 15, metaRecursion: 30, strandCleanup: 60 },
      good: { soulEcho: 10, metaRecursion: 20, strandCleanup: 40 },
      excellent: { soulEcho: 5, metaRecursion: 10, strandCleanup: 20 }
    };
    this.currentPerformance = 'good';
  }
  
  getUpdateInterval(systemName) {
    const intervals = this.updateIntervals[this.currentPerformance];
    return intervals[systemName] || intervals.good;
  }
  
  updatePerformanceRating(fps) {
    if (fps >= 55) this.currentPerformance = 'excellent';
    else if (fps >= 45) this.currentPerformance = 'good';
    else if (fps >= 30) this.currentPerformance = 'fair';
    else if (fps >= 20) this.currentPerformance = 'poor';
    else this.currentPerformance = 'critical';
  }
}
