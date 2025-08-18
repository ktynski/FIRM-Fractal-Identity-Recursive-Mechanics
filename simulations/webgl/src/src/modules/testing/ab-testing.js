/**
 * A/B Testing System
 * Compares curl-based flow vs null flow to validate morphic advantage
 */

export class ABTestingSystem {
  constructor() {
    this.abCounter = 0;
    this.abSumCurl = 0;
    this.abSumNull = 0;
    this.testCycleLength = 300; // frames per A/B test cycle
    this.nullPhaseLength = 30;  // frames of null flow testing
    
    this.results = [];
    this.maxResultHistory = 10;
    
    console.log('🔬 A/B Testing System initialized');
  }
  
  /**
   * Execute A/B testing step
   */
  step(psi, frst, rho, params) {
    // Do not perturb flows during cosmogenesis progression
    if (window.progressiveCosmogenesis && window.progressiveCosmogenesis.active) return;
    
    this.abCounter = (this.abCounter + 1) % this.testCycleLength;
    
    // First 30 frames: test null flow
    if (this.abCounter < this.nullPhaseLength) { 
      params.nullFlow = true;  
      this.abSumNull += this.scoreState(psi, frst, rho); 
    } else { 
      // Remaining 270 frames: test curl flow
      params.nullFlow = false; 
      this.abSumCurl += this.scoreState(psi, frst, rho); 
    }
    
    // End of cycle - compute results
    if (this.abCounter === this.testCycleLength - 1) {
      this.completeTestCycle(params);
    }
  }
  
  /**
   * Complete A/B test cycle and store results
   */
  completeTestCycle(params) {
    const curlFrames = this.testCycleLength - this.nullPhaseLength;
    const avgCurl = this.abSumCurl / Math.max(1, curlFrames);
    const avgNull = this.abSumNull / Math.max(1, this.nullPhaseLength);
    const delta = avgCurl - avgNull;
    
    // Store result in parameters for other systems to use
    params._abDelta = delta; 
    
    // Store in history
    const result = {
      timestamp: Date.now(),
      avgCurl,
      avgNull,
      delta,
      advantage: delta > 0 ? 'curl' : 'null',
      confidence: Math.abs(delta)
    };
    
    this.results.push(result);
    if (this.results.length > this.maxResultHistory) {
      this.results.shift();
    }
    
    // Log results
    console.log(`🔬 A/B TEST COMPLETE: avgCurl=${avgCurl.toFixed(6)}, avgNull=${avgNull.toFixed(6)}, ΔAB=${delta.toFixed(6)}`);
    
    // Reset counters for next cycle
    this.abSumCurl = 0;
    this.abSumNull = 0;
  }
  
  /**
   * Score state function (matches Brain system)
   */
  scoreState(psi, frst, rho, penalty = 0) {
    // Use same scoring as Brain system if available
    if (window.Brain && window.Brain.alpha) {
      return window.Brain.alpha * psi + window.Brain.beta * frst + window.Brain.gamma * rho - window.Brain.lambda * penalty;
    }
    
    // Fallback scoring
    return 3.0 * psi + 2.0 * frst + 1.5 * rho - 0.08 * penalty;
  }
  
  /**
   * Get current test state
   */
  getState() {
    const isInNullPhase = this.abCounter < this.nullPhaseLength;
    const progress = this.abCounter / this.testCycleLength;
    
    return {
      cycleProgress: progress,
      currentPhase: isInNullPhase ? 'null' : 'curl',
      framesRemaining: this.testCycleLength - this.abCounter,
      totalResults: this.results.length,
      latestResult: this.results.length > 0 ? this.results[this.results.length - 1] : null
    };
  }
  
  /**
   * Get A/B test results history
   */
  getResults() {
    return [...this.results];
  }
  
  /**
   * Get average advantage over recent tests
   */
  getAverageAdvantage() {
    if (this.results.length === 0) return 0;
    
    const sum = this.results.reduce((acc, result) => acc + result.delta, 0);
    return sum / this.results.length;
  }
  
  /**
   * Check if curl flow has consistent advantage
   */
  hasCurlAdvantage(threshold = 0.05) {
    const recentResults = this.results.slice(-5); // Last 5 tests
    if (recentResults.length < 3) return false;
    
    return recentResults.every(result => result.delta > threshold);
  }
  
  /**
   * Reset A/B testing system
   */
  reset() {
    this.abCounter = 0;
    this.abSumCurl = 0;
    this.abSumNull = 0;
    this.results = [];
    console.log('🔬 A/B Testing System reset');
  }
  
  /**
   * Get statistics for UI display
   */
  getStats() {
    const state = this.getState();
    const avgAdvantage = this.getAverageAdvantage();
    const hasAdvantage = this.hasCurlAdvantage();
    
    return {
      phase: state.currentPhase,
      progress: (state.cycleProgress * 100).toFixed(1) + '%',
      avgDelta: avgAdvantage.toFixed(6),
      curlAdvantage: hasAdvantage,
      testsCompleted: this.results.length,
      confidence: this.results.length > 0 ? 
        this.results[this.results.length - 1].confidence.toFixed(6) : '0.000000'
    };
  }
}
