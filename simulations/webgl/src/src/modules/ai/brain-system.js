/**
 * Brain System - AI Parameter Optimization
 * Automatic parameter exploration and optimization using evolutionary strategies
 */

export class BrainSystem {
  constructor() {
    this.T = 0.8;                // exploration temperature
    this.momentum = 0.1;
    this.alpha = 3.0;
    this.beta = 2.0;
    this.gamma = 1.5;
    this.lambda = 0.08;
    this.K = 8;
    
    // Parameter step sizes for exploration
    this.step = {
      graceAmp: 0.35,
      devourerAmp: 0.30,
      reflectMix: 0.30,
      baseScale: 0.28,
      fieldScale: 0.25,
      timeScale: 0.22,
      damping: 0.10,
      jitterSigma: 0.08,
      k_burst: 0.32,
      burstAmp: 0.32
    };
    
    this.archive = [];
    this.maxArchive = 10;
    this.lastUpdate = 0;
    this.skipCounter = 0;
    this.emergenceMode = 'seeking';
    this.lastModeSwitch = 0;
    
    // Stateful evaluation
    this.evaluating = false;
    this.evalStartFrame = 0;
    this.evalFrames = 28;
    this.prevScore = 0;
    this.prevParamsSnapshot = null;
    this.candidate = null;
    
    // Freeze presentation and key params during eval
    this.frozenExposure = 1.0;
    this.frozenTrailFade = 0.97;
    this.frozenReflectMix = 0.0;
    
    // Anti-stall
    this.stagnation = 0;
    this.maxStagnation = 6;
    
    // Epoch curriculum
    this.epochTargets = ['psi','frst','rho','ab'];
    this.epochIdx = 0;
    this.epochSteps = 0;
    this.maxEpochSteps = 8;
    this.abMin = 0.05; // require positive morphic advantage
    
    console.log('🧠 Brain System initialized - AI parameter optimization active');
  }
  
  /**
   * Calculate state score for optimization
   */
  scoreState(psi, frst, rho, penalty = 0) {
    return this.alpha * psi + this.beta * frst + this.gamma * rho - this.lambda * penalty;
  }
  
  /**
   * Start parameter evaluation
   */
  startEvaluation(frameCounter) {
    if (this.evaluating) return false;
    
    this.evaluating = true;
    this.evalStartFrame = frameCounter;
    
    // Create parameter candidate
    this.candidate = this.generateCandidate();
    
    // Apply candidate parameters
    this.applyCandidate(this.candidate);
    
    console.log('🧪 Brain: Starting parameter evaluation');
    return true;
  }
  
  /**
   * Complete parameter evaluation
   */
  completeEvaluation(psi, frst, rho) {
    if (!this.evaluating) return;
    
    const score = this.scoreState(psi, frst, rho);
    const improvement = score - this.prevScore;
    
    if (improvement > 0) {
      // Good candidate - add to archive
      this.archive.push({
        params: { ...this.candidate },
        score: score,
        timestamp: Date.now()
      });
      
      // Keep archive size manageable
      if (this.archive.length > this.maxArchive) {
        this.archive.shift();
      }
      
      this.stagnation = 0;
      console.log(`🎯 Brain: Improvement found! Score: ${score.toFixed(3)} (+${improvement.toFixed(3)})`);
    } else {
      this.stagnation++;
      console.log(`🔄 Brain: No improvement. Score: ${score.toFixed(3)} (${improvement.toFixed(3)}), stagnation: ${this.stagnation}`);
    }
    
    this.prevScore = score;
    this.evaluating = false;
    this.candidate = null;
  }
  
  /**
   * Generate new parameter candidate
   */
  generateCandidate() {
    const candidate = {};
    
    // Use archive best if available, otherwise current params
    const base = this.getBestArchive() || window.params;
    
    // Add exploration noise
    for (const [param, stepSize] of Object.entries(this.step)) {
      if (base[param] !== undefined) {
        const noise = (Math.random() - 0.5) * 2 * stepSize * this.T;
        candidate[param] = Math.max(0, base[param] + noise);
      }
    }
    
    return candidate;
  }
  
  /**
   * Apply candidate parameters
   */
  applyCandidate(candidate) {
    if (!window.params) return;
    
    // Apply candidate parameters (respecting user manual overrides)
    const vc = window.simulationCore?.fsctfEngine?.visualController;
    for (const [param, value] of Object.entries(candidate)) {
      if (!vc?.isManuallyOverridden?.(param)) {
        window.params[param] = value;
      }
    }
  }
  
  /**
   * Get best archived parameters
   */
  getBestArchive() {
    if (this.archive.length === 0) return null;
    
    return this.archive.reduce((best, current) => 
      current.score > best.score ? current : best
    ).params;
  }
  
  /**
   * Update brain state (DISABLED during cosmogenesis for visual evolution)
   */
  update(frameCounter, psi, frst, rho) {
    // DISABLE BRAIN DURING COSMOGENESIS: Don't interfere with phase-based visual evolution
    if (window.simulationCore?.fsctfEngine?.cosmogenesisActive) {
      console.log('🧠 Brain System: DISABLED during cosmogenesis - allowing dramatic visual evolution');
      return;
    }
    
    // Check if evaluation is complete
    if (this.evaluating) {
      const evalFramesElapsed = frameCounter - this.evalStartFrame;
      if (evalFramesElapsed >= this.evalFrames) {
        this.completeEvaluation(psi, frst, rho);
      }
      return;
    }
    
    // Start new evaluation if enough time has passed
    const timeSinceLastUpdate = Date.now() - this.lastUpdate;
    if (timeSinceLastUpdate > 5000 && Math.random() < 0.1) { // 10% chance every 5 seconds
      this.startEvaluation(frameCounter);
      this.lastUpdate = Date.now();
    }
    
    // Handle stagnation
    if (this.stagnation >= this.maxStagnation) {
      this.handleStagnation();
    }
  }
  
  /**
   * Handle optimization stagnation
   */
  handleStagnation() {
    console.log('🌀 Brain: Handling stagnation - increasing exploration');
    this.T = Math.min(2.0, this.T * 1.2); // Increase exploration temperature
    this.stagnation = 0;
  }
  
  /**
   * Get brain state
   */
  getState() {
    const cosmogenesisActive = window.simulationCore?.fsctfEngine?.cosmogenesisActive;
    return {
      evaluating: this.evaluating,
      archiveSize: this.archive.length,
      stagnation: this.stagnation,
      temperature: this.T,
      emergenceMode: this.emergenceMode,
      epochIdx: this.epochIdx,
      cosmogenesisDisabled: cosmogenesisActive ? true : false,
      status: cosmogenesisActive ? 'DISABLED (Cosmogenesis Active)' : 'ACTIVE'
    };
  }
  
  /**
   * Reset brain system
   */
  reset() {
    this.evaluating = false;
    this.candidate = null;
    this.stagnation = 0;
    this.T = 0.8;
    this.archive = [];
    console.log('🧠 Brain System reset');
  }
}

