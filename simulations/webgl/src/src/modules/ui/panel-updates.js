/**
 * UI Panel Updates System
 * Updates various information panels in the FSCTF interface
 */

export class PanelUpdates {
  constructor() {
    this.updateIntervals = {
      morphicActivity: 500,     // Update every 500ms
      feedbackLoops: 1000,      // Update every 1000ms
      topology: 250             // Update every 250ms
    };
    
    this.lastUpdates = {
      morphicActivity: 0,
      feedbackLoops: 0,
      topology: 0
    };
    
    // Tracking variables for rate calculations
    this.morphicTracking = {
      lastTime: null,
      lastStrandCount: null
    };
    
    console.log('📊 Panel Updates System initialized');
  }
  
  /**
   * Update all panels if needed
   */
  updateAllPanels() {
    const now = Date.now();
    
    if (now - this.lastUpdates.morphicActivity >= this.updateIntervals.morphicActivity) {
      this.updateMorphicActivityPanel();
      this.lastUpdates.morphicActivity = now;
    }
    
    if (now - this.lastUpdates.feedbackLoops >= this.updateIntervals.feedbackLoops) {
      this.updateFeedbackLoopsPanel();
      this.lastUpdates.feedbackLoops = now;
    }
    
    if (now - this.lastUpdates.topology >= this.updateIntervals.topology) {
      this.updateTopologyStatus();
      this.lastUpdates.topology = now;
    }
  }
  
  /**
   * Update morphic activity panel
   */
  updateMorphicActivityPanel() {
    const graceOperator = window.graceOperator;
    if (!graceOperator) return;
    
    const strands = graceOperator.morphicStrands || [];
    const field = graceOperator.morphicField?.field || 0;
    
    // Calculate strand statistics
    const stableCounts = { stable: 0, metastable: 0, unstable: 0, chaotic: 0 };
    strands.forEach(strand => {
      const stability = typeof strand.stability === 'object' ? 
        strand.stability.stability : strand.stability;
      if (stableCounts.hasOwnProperty(stability)) {
        stableCounts[stability]++;
      }
    });
    
    // Calculate creation rate
    const currentTime = Date.now();
    const creationRate = this.calculateCreationRate(currentTime, strands.length);
    
    // Update UI elements
    this.updateElement('active-strands', strands.length.toLocaleString());
    this.updateElement('creation-rate', Math.max(0, creationRate).toFixed(1));
    this.updateElement('field-strength', field.toFixed(3));
    this.updateElement('stable-count', stableCounts.stable);
    this.updateElement('meta-count', stableCounts.metastable);
    this.updateElement('unstable-count', stableCounts.unstable + stableCounts.chaotic);
    
    // Update overall activity indicator
    const totalActivity = field + (strands.length * 0.01);
    const activityEl = document.getElementById('morphic-activity-indicator');
    if (activityEl) {
      const intensity = Math.min(1, totalActivity / 10);
      activityEl.style.opacity = (0.3 + intensity * 0.7).toString();
      activityEl.style.backgroundColor = `rgba(153, 204, 255, ${intensity})`;
    }
  }
  
  /**
   * Calculate strand creation rate
   */
  calculateCreationRate(currentTime, currentStrandCount) {
    if (!this.morphicTracking.lastTime) {
      this.morphicTracking.lastTime = currentTime;
      this.morphicTracking.lastStrandCount = currentStrandCount;
      return 0;
    }
    
    const deltaTime = (currentTime - this.morphicTracking.lastTime) / 1000;
    const deltaStrands = currentStrandCount - this.morphicTracking.lastStrandCount;
    const creationRate = deltaTime > 0 ? deltaStrands / deltaTime : 0;
    
    this.morphicTracking.lastTime = currentTime;
    this.morphicTracking.lastStrandCount = currentStrandCount;
    
    return creationRate;
  }
  
  /**
   * Update feedback loops panel
   */
  updateFeedbackLoopsPanel() {
    const cascadeEmergence = window.cascadeEmergence;
    if (!cascadeEmergence) return;
    
    // Get feedback loop data
    const feedbackLoops = cascadeEmergence.feedbackLoops || [];
    const activeLoops = feedbackLoops.filter(loop => loop.strength > 0.1).length;
    
    // Calculate self-reference strength
    const selfReferenceStrength = this.calculateSelfReferenceStrength();
    
    // Calculate average loop strength
    const avgLoopStrength = feedbackLoops.length > 0 ? 
      feedbackLoops.reduce((sum, loop) => sum + loop.strength, 0) / feedbackLoops.length : 0;
    
    // Calculate φ-resonance
    const phiResonance = this.calculatePhiResonance();
    
    // Update UI elements
    this.updateElement('feedback-loop-count', activeLoops);
    this.updateElement('self-reference-strength', Math.max(0, selfReferenceStrength).toFixed(3));
    this.updateElement('loop-strength', Math.max(0, avgLoopStrength).toFixed(3));
    this.updateElement('phi-resonance', Math.abs(phiResonance).toFixed(3));
    
    // Update feedback loop activity indicator
    const loopActivityEl = document.getElementById('feedback-activity-indicator');
    if (loopActivityEl) {
      const intensity = Math.min(1, avgLoopStrength);
      loopActivityEl.style.opacity = (0.3 + intensity * 0.7).toString();
      loopActivityEl.style.backgroundColor = intensity > 0.5 ? 
        `rgba(255, 153, 102, ${intensity})` : `rgba(153, 204, 255, ${intensity})`;
    }
  }
  
  /**
   * Calculate self-reference strength
   */
  calculateSelfReferenceStrength() {
    const frstTracker = window.frstTracker;
    const graceOperator = window.graceOperator;
    
    if (!frstTracker || !graceOperator) return 0;
    
    const coherence = frstTracker.coherenceScore || 0;
    const field = graceOperator.morphicField?.field || 0;
    
    return (coherence * field) / 10.0;
  }
  
  /**
   * Calculate φ-resonance from FRST metrics
   */
  calculatePhiResonance() {
    const frstTracker = window.frstTracker;
    if (!frstTracker) return 0;
    
    const recursionDepth = frstTracker.recursionDepth || 0;
    const coherenceScore = frstTracker.coherenceScore || 0;
    
    return Math.sin(recursionDepth * 0.1) * coherenceScore * 0.1;
  }
  
  /**
   * Update topology status display
   */
  updateTopologyStatus() {
    const topologyManager = window.topologyTransitionManager;
    if (!topologyManager) return;
    
    const state = topologyManager.getTopologyState();
    
    // Update topology name and phase
    this.updateElement('current-topology', state.currentTopology || 'Unknown');
    this.updateElement('topology-phase', state.phase || 'Inactive');
    
    // Update transition progress
    if (state.isTransitioning) {
      const progress = ((state.transitionProgress || 0) * 100).toFixed(1);
      this.updateElement('transition-progress', `${progress}%`);
      
      const progressBar = document.getElementById('topology-progress-bar');
      if (progressBar) {
        progressBar.style.width = `${progress}%`;
        progressBar.style.opacity = '1';
      }
    } else {
      this.updateElement('transition-progress', 'Stable');
      
      const progressBar = document.getElementById('topology-progress-bar');
      if (progressBar) {
        progressBar.style.width = '0%';
        progressBar.style.opacity = '0.3';
      }
    }
    
    // Update complexity indicator
    const complexity = state.complexity || 0;
    this.updateElement('topology-complexity', complexity.toFixed(2));
    
    // Visual indicator based on topology type
    const topologyIndicator = document.getElementById('topology-indicator');
    if (topologyIndicator) {
      const colors = {
        'Torus': 'rgba(100, 150, 255, 0.8)',
        'Möbius': 'rgba(255, 150, 100, 0.8)',
        'Klein': 'rgba(150, 255, 100, 0.8)',
        'φ-Klein': 'rgba(255, 200, 50, 0.8)'
      };
      
      topologyIndicator.style.backgroundColor = colors[state.currentTopology] || 'rgba(150, 150, 150, 0.8)';
      topologyIndicator.style.transform = state.isTransitioning ? 'scale(1.1)' : 'scale(1.0)';
    }
  }
  
  /**
   * Helper method to update UI element text content
   */
  updateElement(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
      element.textContent = value;
    }
  }
  
  /**
   * Force update all panels immediately
   */
  forceUpdateAll() {
    this.updateMorphicActivityPanel();
    this.updateFeedbackLoopsPanel();
    this.updateTopologyStatus();
    console.log('📊 All panels force updated');
  }
  
  /**
   * Set update intervals
   */
  setUpdateIntervals(intervals) {
    Object.assign(this.updateIntervals, intervals);
    console.log('📊 Update intervals changed:', this.updateIntervals);
  }
  
  /**
   * Get panel update statistics
   */
  getStats() {
    const now = Date.now();
    
    return {
      lastUpdates: { ...this.lastUpdates },
      intervals: { ...this.updateIntervals },
      timeSinceLastUpdate: {
        morphicActivity: now - this.lastUpdates.morphicActivity,
        feedbackLoops: now - this.lastUpdates.feedbackLoops,
        topology: now - this.lastUpdates.topology
      }
    };
  }
  
  /**
   * Reset tracking data
   */
  resetTracking() {
    this.morphicTracking.lastTime = null;
    this.morphicTracking.lastStrandCount = null;
    
    const now = Date.now();
    this.lastUpdates.morphicActivity = now;
    this.lastUpdates.feedbackLoops = now;
    this.lastUpdates.topology = now;
    
    console.log('📊 Panel tracking data reset');
  }
}
