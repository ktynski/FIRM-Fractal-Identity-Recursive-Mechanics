/**
 * Metrics System - Performance and State Tracking
 * Windowed metrics collection and assertion evaluation
 */

export class MetricsSystem {
  constructor() {
    // Windowed metrics storage
    this.metricWindow = {
      E: [],      // Energy
      K: [],      // Kinetic
      PSI: [],    // Psi (particle activity)
      R: []       // Rho (correlations)
    };
    
    this.maxWindowSize = 60; // frames
    this.lastUpdateTime = 0;
    this.updateInterval = 100; // ms
    
    console.log('📊 Metrics System initialized');
  }
  
  /**
   * Add value to windowed array
   */
  pushWindow(arr, value, maxSize = this.maxWindowSize) {
    arr.push(value);
    if (arr.length > maxSize) {
      arr.shift();
    }
  }
  
  /**
   * Calculate mean of array
   */
  mean(arr) {
    if (!arr.length) return 0;
    let sum = 0;
    for (const v of arr) sum += v;
    return sum / arr.length;
  }
  
  /**
   * Update metrics with new values
   */
  updateMetrics(energy, kappa, psi, rho) {
    const now = Date.now();
    if (now - this.lastUpdateTime < this.updateInterval) return;
    
    this.pushWindow(this.metricWindow.E, energy);
    this.pushWindow(this.metricWindow.K, kappa);
    this.pushWindow(this.metricWindow.PSI, psi);
    this.pushWindow(this.metricWindow.R, rho);
    
    this.lastUpdateTime = now;
  }
  
  /**
   * Evaluate system assertions/thresholds
   */
  evaluateAssertions(params) {
    const win = params.windowTicks || 30;
    
    // Energy bounds check
    const passE = this.mean(this.metricWindow.E) >= (params.Emin || 0) && 
                  this.mean(this.metricWindow.E) <= (params.Emax || 1);
    
    // Kappa (kinetic) target check
    const passK = Math.abs(this.mean(this.metricWindow.K) - (params.tau || 0.5)) <= (params.kappaEps || 0.1);
    
    // Psi minimum check
    const passPsi = this.mean(this.metricWindow.PSI) >= (params.psiMin || 0.1);
    
    // Rho correlation check (conditional)
    const passR = (params.reflectMix > 0.5) ? 
      (this.mean(this.metricWindow.R) >= (params.rhoMin || 0.05)) : true;
    
    // A/B testing advantage check
    const passAB = (params._abDelta || 0) >= 0.05;
    
    const pass = passE && passK && passPsi && passR && passAB;
    
    return { pass, passE, passK, passPsi, passR, passAB };
  }
  
  /**
   * Get current windowed statistics
   */
  getStats() {
    return {
      energy: {
        current: this.metricWindow.E[this.metricWindow.E.length - 1] || 0,
        mean: this.mean(this.metricWindow.E),
        samples: this.metricWindow.E.length
      },
      kappa: {
        current: this.metricWindow.K[this.metricWindow.K.length - 1] || 0,
        mean: this.mean(this.metricWindow.K),
        samples: this.metricWindow.K.length
      },
      psi: {
        current: this.metricWindow.PSI[this.metricWindow.PSI.length - 1] || 0,
        mean: this.mean(this.metricWindow.PSI),
        samples: this.metricWindow.PSI.length
      },
      rho: {
        current: this.metricWindow.R[this.metricWindow.R.length - 1] || 0,
        mean: this.mean(this.metricWindow.R),
        samples: this.metricWindow.R.length
      }
    };
  }
  
  /**
   * Generate status text for UI
   */
  generateStatusText(F, E, kappa, psi, frst, rho, fsctfState) {
    const assertions = this.evaluateAssertions(window.params || {});
    const abDelta = window.params?._abDelta || 0;
    const archiveSize = window.Brain?.archive?.length || 0;
    
    // FSCTF status
    const strands = fsctfState?.strands || 0;
    const consciousness = fsctfState?.consciousness || 0;
    const emergence = fsctfState?.emergence || false;
    const fsctfIcon = emergence ? '✨' : (strands > 0 ? '🌱' : '🌑');
    
    return `${fsctfIcon} Strands=${strands} Mind=${consciousness.toFixed(3)} | F=${F.toFixed(3)} E=${E.toFixed(3)} κ=${kappa.toFixed(3)} Ψ=${psi.toFixed(3)} FRST=${frst.toFixed(3)} ρ=${rho.toFixed(3)} ΔAB=${abDelta.toFixed(3)} Arch=${archiveSize} ${assertions.pass? 'PASS':'FAIL'}`;
  }
  
  /**
   * Update stats display element
   */
  updateStatsDisplay(F, E, kappa, psi, frst, rho, fsctfState) {
    const statsEl = document.getElementById('stats');
    if (!statsEl) return;
    
    statsEl.textContent = this.generateStatusText(F, E, kappa, psi, frst, rho, fsctfState);
  }
  
  /**
   * Clear all windowed metrics
   */
  clearMetrics() {
    this.metricWindow.E = [];
    this.metricWindow.K = [];
    this.metricWindow.PSI = [];
    this.metricWindow.R = [];
    console.log('📊 Metrics cleared');
  }
  
  /**
   * Get metric history for analysis
   */
  getHistory() {
    return {
      energy: [...this.metricWindow.E],
      kappa: [...this.metricWindow.K],
      psi: [...this.metricWindow.PSI],
      rho: [...this.metricWindow.R]
    };
  }
}

