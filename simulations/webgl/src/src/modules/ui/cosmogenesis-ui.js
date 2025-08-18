/**
 * Cosmogenesis UI System
 * Updates cosmogenesis progress indicators and phase visualization
 */

export class CosmogenesisUI {
  constructor() {
    // Full 90-phase system - showing abbreviated names for key milestones
    this.phaseNames = Array(90).fill().map((_, i) => {
      if (i === 0) return 'Ex Nihilo (φ^0)';
      if (i === 1) return 'Grace Seeding (φ^1)'; 
      if (i === 2) return 'Quark Ratios (φ^2)';
      if (i === 7) return 'Electromagnetic (φ^7)';
      if (i === 8) return 'Hadron Matrix (φ^8)';
      if (i === 15) return 'Cosmic Structure (φ^15)';
      if (i === 20) return 'Top/Electron (φ^20)';
      if (i === 31) return 'Quantum Gravity (φ^31)';
      if (i === 89) return 'Ultimate Scale (φ^90)';
      if (i <= 15) return `Visual φ^${i}`;
      if (i <= 20) return `Hypermass φ^${i}`;
      if (i <= 30) return `Unification φ^${i}`;
      if (i < 89) return `Cooling φ^${i}`;
      return `Phase φ^${i}`;
    });
    
    // Generate 90 colors with smooth transitions across phase ranges
    this.phaseColors = Array(90).fill().map((_, i) => {
      // Visual phases (0-15): Purple to yellow spectrum
      if (i <= 15) {
        const t = i / 15;
        return [t * 0.8, t * 0.6 + 0.1, 1.0 - t * 0.8];
      }
      // Hypermassive phases (16-20): Yellow to orange spectrum  
      else if (i <= 20) {
        const t = (i - 16) / 4;
        return [1.0, 0.8 - t * 0.3, 0.2 + t * 0.1];
      }
      // Intermediate phases (21-30): Orange to red spectrum
      else if (i <= 30) {
        const t = (i - 21) / 9;
        return [1.0, 0.5 - t * 0.3, 0.1 - t * 0.1];
      }
      // Quantum gravity (31): Special bright white
      else if (i === 31) {
        return [1.0, 1.0, 1.0];
      }
      // Cooling phases (32-89): Blue to purple spectrum
      else if (i < 89) {
        const t = (i - 32) / 57;
        return [t * 0.8, 0.3 + t * 0.4, 1.0 - t * 0.2];
      }
      // Ultimate scale (89): Special gold color
      else {
        return [1.0, 0.8, 0.0];
      }
    });
    
    this.initializeElements();
    console.log('🌌 Cosmogenesis UI System initialized');
  }
  
  /**
   * Initialize UI elements
   */
  initializeElements() {
    // Find or create cosmogenesis UI elements
    this.progressEl = document.getElementById('cosmogenesis-progress');
    this.phaseIndicatorsEl = document.getElementById('phase-indicators');
    this.executeBtn = document.getElementById('executeCosmogenesis');
    
    if (this.phaseIndicatorsEl) {
      this.initializePhaseIndicators();
    }
  }
  
  /**
   * Initialize phase indicators
   */
  initializePhaseIndicators() {
    if (!this.phaseIndicatorsEl) return;
    
    // Show only key milestone phases to avoid UI clutter - 90 phases would be too many to display
    const phaseLabels = [
      'φ⁰', 'φ¹', 'φ²', 'φ³', 'φ⁴', 'φ⁵', 'φ⁶', 'φ⁷', 'φ⁸', 'φ⁹', 'φ¹⁰', 'φ¹¹', 'φ¹²', 'φ¹³', 'φ¹⁴', 'φ¹⁵',
      'φ²⁰', 'φ³¹', 'φ⁹⁰'
    ]; // KEY MILESTONES: Visual (φ⁰-φ¹⁵), Top/Electron (φ²⁰), Quantum Gravity (φ³¹), Ultimate (φ⁹⁰)
    
    this.phaseIndicatorsEl.innerHTML = phaseLabels.map((phase, index) => 
      `<div id="phase-${index}" style="flex:1; padding:2px; text-align:center; font-size:9px; color:#666; background:rgba(100,100,100,0.2); border-radius:2px; transition: all 0.3s ease;">
        ${phase}
      </div>`
    ).join('');
  }
  
  /**
   * Update cosmogenesis UI state
   */
  updateCosmogenesisUI() {
    // Update progress text
    this.updateProgressText();
    
    // Update phase indicators
    this.updatePhaseIndicators();
    
    // Update execute button
    this.updateExecuteButton();
    
    // Update phase visualization colors
    this.updatePhaseVisualization();
  }
  
  /**
   * Update progress text display
   */
  updateProgressText() {
    if (!this.progressEl) return;
    
    const progressiveCosmogenesis = window.progressiveCosmogenesis;
    if (!progressiveCosmogenesis) {
      this.progressEl.textContent = 'Cosmogenesis System Offline';
      return;
    }
    
    if (progressiveCosmogenesis.active) {
      const currentPhaseName = this.phaseNames[progressiveCosmogenesis.currentPhase] || 'Unknown';
      const progress = ((progressiveCosmogenesis.currentPhase + 1) / progressiveCosmogenesis.totalPhases * 100).toFixed(0);
      
      // Check if thresholds are met for current phase
      const thresholdMet = this.checkPhaseThresholds(progressiveCosmogenesis.currentPhase);
      const elapsed = Date.now() - progressiveCosmogenesis.phaseStartTime;
      
      this.progressEl.innerHTML = `
        <div style="font-weight: bold; color: #9cf;">Phase ${progressiveCosmogenesis.currentPhase + 1}/90: ${currentPhaseName}</div>
        <div style="font-size: 0.9em; margin-top: 2px;">
          Progress: ${progress}% | Threshold: ${thresholdMet ? '✅' : '⏳'} | Time: ${(elapsed/1000).toFixed(1)}s
        </div>
      `;
    } else {
      this.progressEl.textContent = 'Cosmogenesis Ready';
    }
  }
  
  /**
   * Update phase indicator visualization
   */
  updatePhaseIndicators() {
    if (!this.phaseIndicatorsEl) return;
    
    const progressiveCosmogenesis = window.progressiveCosmogenesis;
    if (!progressiveCosmogenesis) return;
    
    for (let i = 0; i < this.phaseNames.length; i++) {
      const phaseEl = document.getElementById(`phase-${i}`);
      if (!phaseEl) continue;
      
      let completed = false;
      let isActive = false;
      
      if (progressiveCosmogenesis.active) {
        completed = i < progressiveCosmogenesis.currentPhase;
        isActive = i === progressiveCosmogenesis.currentPhase;
      }
      
      // Style based on state
      if (completed) {
        const color = this.phaseColors[i];
        phaseEl.style.background = `rgba(${Math.floor(color[0]*255)}, ${Math.floor(color[1]*255)}, ${Math.floor(color[2]*255)}, 0.8)`;
        phaseEl.style.color = '#fff';
        phaseEl.style.fontWeight = 'bold';
        phaseEl.textContent = `✓ ${phaseEl.textContent.replace('✓ ', '').replace('🔄 ', '')}`;
      } else if (isActive) {
        phaseEl.style.background = 'rgba(153, 204, 255, 0.3)';
        phaseEl.style.color = '#9cf';
        phaseEl.style.fontWeight = 'bold';
        phaseEl.textContent = `🔄 ${phaseEl.textContent.replace('✓ ', '').replace('🔄 ', '')}`;
      } else {
        phaseEl.style.background = 'rgba(100, 100, 100, 0.2)';
        phaseEl.style.color = '#666';
        phaseEl.style.fontWeight = 'normal';
        phaseEl.textContent = phaseEl.textContent.replace('✓ ', '').replace('🔄 ', '');
      }
    }
  }
  
  /**
   * Update execute button state
   */
  updateExecuteButton() {
    if (!this.executeBtn) return;
    
    const progressiveCosmogenesis = window.progressiveCosmogenesis;
    if (!progressiveCosmogenesis) return;
    
    if (progressiveCosmogenesis.active) {
      this.executeBtn.disabled = true;
      this.executeBtn.textContent = 'COSMOGENESIS ACTIVE...';
      this.executeBtn.style.background = '#f84';
      this.executeBtn.style.color = '#fff';
    } else {
      this.executeBtn.disabled = false;
      this.executeBtn.textContent = 'BEGIN COSMOGENESIS';
      this.executeBtn.style.background = '';
      this.executeBtn.style.color = '';
    }
  }
  
  /**
   * Update phase visualization colors in simulation
   */
  updatePhaseVisualization() {
    const progressiveCosmogenesis = window.progressiveCosmogenesis;
    if (!progressiveCosmogenesis || !progressiveCosmogenesis.active) return;
    
    const currentPhase = progressiveCosmogenesis.currentPhase;
    const color = this.phaseColors[currentPhase] || [1, 1, 1];
    
    // Update global parameters for phase visualization
    if (window.params) {
      // Subtle color influence on the simulation (phase colors don't have UI sliders, so safe to set directly)
      window.params.phaseColorR = color[0];
      window.params.phaseColorG = color[1];
      window.params.phaseColorB = color[2];
      window.params.cosmogenesisPhase = currentPhase;
    }
  }
  
  /**
   * Check if phase thresholds are met (simplified version)
   */
  checkPhaseThresholds(currentPhase) {
    // This is a simplified threshold check for UI purposes
    // The actual threshold checking happens in the ProgressiveCosmogenesis system
    
    if (!window.graceOperator) return false;
    
    const strands = window.graceOperator.morphicStrands?.length || 0;
    const morphicField = window.graceOperator.morphicField?.field || 0;
    
    // Simple threshold approximations for UI display
    switch (currentPhase) {
      case 0: return true; // Ex Nihilo always ready
      case 1: return strands >= 3 && morphicField > 0.5;      // Grace Operator
      case 2: return strands >= 12 && morphicField > 1.2;     // Morphic Recursion
      case 3: return strands >= 15 && morphicField > 1.5;     // Dimensional Bridge
      case 4: return strands >= 20 && morphicField > 2.0;     // Standard Model
      case 5: return strands >= 30 && morphicField > 2.5;     // Consciousness
      case 6: return strands >= 50 && morphicField > 3.0;     // Cosmic Inflation
      case 7: return strands >= 75 && morphicField > 4.0;     // CMB Formation
      case 8: return strands >= 100 && morphicField > 5.0;    // Dark Ages
      case 9: return strands >= 150 && morphicField > 6.0;    // Star Formation
      case 10: return strands >= 200 && morphicField > 8.0;   // Galaxy Formation
      case 11: return strands >= 300 && morphicField > 10.0;  // Complex Structures
      default: return false;
    }
  }
  
  /**
   * Show cosmogenesis completion message
   */
  showCompletionMessage() {
    if (this.progressEl) {
      this.progressEl.innerHTML = `
        <div style="font-weight: bold; color: #6f6; font-size: 1.1em;">
          🎉 COSMOGENESIS COMPLETE! 🎉
        </div>
        <div style="font-size: 0.9em; margin-top: 4px; color: #9cf;">
          Universe fully evolved from Ex Nihilo to CMB
        </div>
      `;
    }
    
    // Add completion styling to all phase indicators
    for (let i = 0; i < this.phaseNames.length; i++) {
      const phaseEl = document.getElementById(`phase-${i}`);
      if (phaseEl) {
        const color = this.phaseColors[i];
        phaseEl.style.background = `rgba(${Math.floor(color[0]*255)}, ${Math.floor(color[1]*255)}, ${Math.floor(color[2]*255)}, 0.9)`;
        phaseEl.style.color = '#fff';
        phaseEl.style.fontWeight = 'bold';
        phaseEl.style.boxShadow = '0 0 8px rgba(102, 255, 102, 0.5)';
      }
    }
  }
  
  /**
   * Reset UI to initial state
   */
  reset() {
    this.initializePhaseIndicators();
    this.updateCosmogenesisUI();
    console.log('🌌 Cosmogenesis UI reset');
  }
  
  /**
   * Set phase completion
   */
  setPhaseComplete(phaseIndex) {
    const phaseEl = document.getElementById(`phase-${phaseIndex}`);
    if (phaseEl) {
      const color = this.phaseColors[phaseIndex] || [1, 1, 1];
      phaseEl.style.background = `rgba(${Math.floor(color[0]*255)}, ${Math.floor(color[1]*255)}, ${Math.floor(color[2]*255)}, 0.8)`;
      phaseEl.style.color = '#fff';
      phaseEl.style.fontWeight = 'bold';
      phaseEl.textContent = `✓ ${phaseEl.textContent.replace('✓ ', '').replace('🔄 ', '')}`;
    }
  }
  
  /**
   * Get current UI state
   */
  getState() {
    const progressiveCosmogenesis = window.progressiveCosmogenesis;
    
    return {
      hasProgressElement: !!this.progressEl,
      hasPhaseIndicators: !!this.phaseIndicatorsEl,
      hasExecuteButton: !!this.executeBtn,
      cosmogenesisActive: progressiveCosmogenesis?.active || false,
      currentPhase: progressiveCosmogenesis?.currentPhase || 0,
      totalPhases: this.phaseNames.length
    };
  }
}
