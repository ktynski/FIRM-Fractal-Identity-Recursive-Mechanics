/**
 * Advanced UI Builder
 * Complex UI creation with performance monitoring, collapsible sections, and advanced controls
 */

export class AdvancedUIBuilder {
  constructor(container) {
    this.ui = container;
    this.paramElements = {};
    
    // Track advanced section state
    this.advancedVisible = false;
    this.advancedDiv = null;
    this.advancedToggle = null;
    
    console.log('🔧 Advanced UI Builder initialized');
  }
  
  /**
   * Build the complete modern FSCTF UI with all advanced features
   */
  buildModernUI() {
    if (this.ui && this.ui.dataset && this.ui.dataset.built === '1') return;
    if (this.ui && this.ui.dataset) this.ui.dataset.built = '1';
    
    // Modern section styling with better visual hierarchy
    this.section = (title, description = '') => {
      const h = document.createElement('div');
      h.style.cssText = 'margin-top:12px;font:700 12px monospace;color:#46f;border-top:2px solid #234;padding-top:8px;background:rgba(70,100,255,0.1);padding:8px;border-radius:4px;';
      h.innerHTML = `<span style="color:#8cf;">${title}</span>${description ? `<br><span style="font-size:9px;color:#678;font-weight:400;">${description}</span>` : ''}`;
      this.ui.appendChild(h);
    };
    
    // Build all UI sections
    this.buildVisualControllerSection();
    this.buildCoreFSCTFControls();
    this.buildParticleQuality();       // NEW: Particle resolution controls
    this.buildTopologyEvolution();
    this.buildEnhancedCamera();
    this.buildCosmogenesisPipeline();
    this.buildVisualQuality();
    this.buildAdvancedControlsSection();
    this.buildSoulEchoTracker();       // NEW: Soul Echo Survivability Tracker display
    this.buildGPUOptimizer();          // NEW: GPU Performance Optimizer controls
    this.buildMirrorEmergenceTracker(); // NEW: Mirror Emergence Tracker for Stage 8+ analysis
    this.buildMetaRecursionEngine();   // NEW: Meta-Recursion Engine for maximum emergent complexity
    this.buildPhaseInfoDisplay();      // NEW: Comprehensive phase information system
    
    console.log('✅ Modern FSCTF UI built successfully');
  }

  /**
   * Visual Controller & Safety
   */
  buildVisualControllerSection() {
    this.section('🎛️ Visual Controller', 'Centralized, safe visual management with manual mode and blob prevention');

    // Manual mode toggle
    const toggleBtn = document.createElement('button');
    toggleBtn.textContent = 'Manual Mode: OFF';
    toggleBtn.style.cssText = 'margin: 4px 0; padding: 4px 8px; font: 10px monospace; background:#334; color:#9c8; border:1px solid #667; border-radius:4px; cursor:pointer;';
    toggleBtn.onclick = () => {
      const engine = window.fsctfEngine;
      const vc = engine?.visualController;
      if (!vc) { console.log('❌ Visual Controller unavailable'); return; }
      const on = vc.toggleManualMode();
      toggleBtn.textContent = on ? 'Manual Mode: ON' : 'Manual Mode: OFF';
      toggleBtn.style.background = on ? '#454' : '#334';
    };
    this.ui.appendChild(toggleBtn);

    // Quality/status readout
    const status = document.createElement('div');
    status.style.cssText = 'font: 10px monospace; color:#8ac; margin:6px 0;';
    status.textContent = 'Quality: —  |  Blob: —';
    this.ui.appendChild(status);

    // Lightweight status updater
    const updateStatus = () => {
      const engine = window.fsctfEngine;
      const vc = engine?.visualController;
      const bd = engine?.blobDetector;
      if (vc) {
        status.textContent = `Quality: ${vc.currentQuality || '—'}  |  Blob: ${bd?.emergencyModeActive ? 'EMERGENCY' : 'OK'}`;
      }
      requestAnimationFrame(updateStatus);
    };
    requestAnimationFrame(updateStatus);
  }
  
  /**
   * Core FSCTF Controls
   */
  buildCoreFSCTFControls() {
    this.section('🌌 FIRM Core System', 'Primary controls for Field-Strand Coherence Framework');
    this.addCheckbox('fsctfEnabled', 'Enable FIRM: Activates the complete theoretical framework driving morphic emergence and topology evolution.');
    
    // User Override Reset Button
    const resetOverridesBtn = document.createElement('button');
    resetOverridesBtn.textContent = '🔓 Reset Auto-Changes';
    resetOverridesBtn.style.cssText = 'margin: 4px 0 8px 0; padding: 4px 8px; font: 10px monospace; background: linear-gradient(135deg, #234, #345); color: #fc6; border: 1px solid #f84; border-radius: 4px; cursor: pointer; transition: all 0.2s; width: 100%;';
    resetOverridesBtn.title = 'Reset user override protection - re-enable automatic parameter changes by the system';
    resetOverridesBtn.onmouseover = () => resetOverridesBtn.style.background = 'linear-gradient(135deg, #345, #456)';
    resetOverridesBtn.onmouseout = () => resetOverridesBtn.style.background = 'linear-gradient(135deg, #234, #345)';
    resetOverridesBtn.onclick = () => {
      const engine = window.fsctfEngine;
      const vc = engine?.visualController;
      if (vc) {
        vc.manualOverrides.clear();
        vc.manualModeActive = false;
        console.log('🎛️ Manual overrides cleared; automatic mode resumed');
        resetOverridesBtn.style.background = 'linear-gradient(135deg, #084, #195)';
        setTimeout(() => resetOverridesBtn.style.background = 'linear-gradient(135deg, #234, #345)', 1000);
      } else {
        console.log('❌ Visual Controller unavailable');
      }
    };
    this.ui.appendChild(resetOverridesBtn);
    
    this.addSlider('graceComplexity', 0.0, 1000.0, 0.1, 'Grace Operator Intensity: φ-recursive creation power. UNBOUNDED - explore extreme mathematical complexity!');
    this.addSlider('morphicRecursionDepth', 1, 90, 1, 'Recursion Depth: Levels of φ-coupled bifurcation for 90-phase system. UNBOUNDED - deeper recursion creates more sophisticated emergence patterns.'); // FIXED: Match 90-phase system
    this.addSlider('consciousnessComplexity', 0.5, 1000.0, 0.1, 'Consciousness Complexity: Prime resonance intensity. UNBOUNDED - maximum consciousness emergence through φ-pathways.');
  }
  
  /**
   * Particle Quality Controls (NEW)
   */
  buildParticleQuality() {
    this.section('🔬 Particle Resolution', 'Control particle count for emergent structure clarity');
    this.addSlider('drawFraction', 0.1, 1.0, 0.05, 'Draw Fraction: Percentage of particles to render (1.0 = all 589K particles for maximum structure detail)');
    this.addSlider('particleQuality', 0.5, 1.5, 0.1, 'Quality Multiplier: Overall particle density scaling for structure visibility');
    
    // Add quality preset info
    const qualityInfo = document.createElement('div');
    qualityInfo.style.cssText = 'font-size: 10px; color: #888; margin: 5px 0; padding: 5px; background: rgba(0,0,0,0.2); border-radius: 3px;';
    qualityInfo.innerHTML = `
      <strong>Current:</strong> Standard Quality (262K particles)<br>
      <strong>Presets:</strong> Draft (65K) | Standard (262K) | High (590K) | Ultra (1M)<br>
      <em>Higher particle counts reveal more detail in emergent geometric structures</em>
    `;
    this.ui.appendChild(qualityInfo);
  }

  /**
   * Topology Evolution Controls
   */
  buildTopologyEvolution() {
    this.section('🌀 Topology Evolution', 'Control the geometric evolution: Torus → Möbius → Klein → φ-Klein');
    this.addCheckbox('showWireframe', 'Show Wireframe: Display underlying manifold structure making topology evolution clearly visible.');
    this.addSlider('wireframeOpacity', 0.0, 1.0, 0.01, 'Wireframe Opacity: Transparency of geometric structure overlay.');
    this.addSlider('wireframeDensity', 5, 50, 1, 'Wireframe Density: Detail level of geometric grid lines.');
    this.addSlider('topologyTransitionDuration', 0.0, 120.0, 0.5, 'Transition Duration: 0=Static topology, 10-60s=Cinematic, 120s=Ultra-slow cosmic evolution');
  }
  
  /**
   * Enhanced Camera System
   */
  buildEnhancedCamera() {
    this.section('📸 Enhanced Camera', 'Cinematic camera system with dynamic tracking and smooth transitions');
    
    // Camera Preset Buttons
    const cameraPresetButtons = document.createElement('div');
    cameraPresetButtons.style.cssText = 'margin: 8px 0; display: flex; flex-wrap: wrap; gap: 4px;';
    
    const cameraPresets = [
      { name: '🔍 Overview', preset: 'overview', tooltip: 'Wide view showing complete topology structure' },
      { name: '🔬 Detail', preset: 'detail', tooltip: 'Close-up view for particle interactions' },
      { name: '📐 Wireframe', preset: 'wireframe', tooltip: 'Optimal angle for wireframe visualization' },
      { name: '🌀 Transition', preset: 'transition', tooltip: 'Dynamic view for topology transitions' }
    ];
    
    cameraPresets.forEach(preset => {
      const btn = document.createElement('button');
      btn.textContent = preset.name;
      btn.style.cssText = 'padding: 6px 10px; font: 10px monospace; background: linear-gradient(135deg, #234, #345); color: #9cf; border: 1px solid #46f; border-radius: 4px; cursor: pointer; transition: all 0.2s;';
      btn.title = preset.tooltip;
      btn.onmouseover = () => btn.style.background = 'linear-gradient(135deg, #345, #456)';
      btn.onmouseout = () => btn.style.background = 'linear-gradient(135deg, #234, #345)';
      btn.onclick = () => {
        if (window.cameraTransitionManager) {
          window.cameraTransitionManager.setPreset(preset.preset);
        }
      };
      cameraPresetButtons.appendChild(btn);
    });
    
    this.ui.appendChild(cameraPresetButtons);
    
    this.addCheckbox('cameraAutoRotate', 'Auto-Rotate: Cinematic rotation for dynamic viewing of topology evolution.');
    this.addSlider('cameraAutoRotateSpeed', 0.05, 5.0, 0.01, 'Rotation Speed: Speed of automatic camera movement.');
    this.addCheckbox('cameraDynamicTracking', 'Dynamic Tracking: Auto-adjust distance based on morphic field complexity.');
    this.addSlider('cameraTrackingIntensity', 0.0, 1.0, 0.01, 'Tracking Intensity: Camera responsiveness to complexity changes.');
  }
  
  /**
   * Cosmogenesis Pipeline
   */
  buildCosmogenesisPipeline() {
    this.section('🎬 Cosmogenesis Pipeline', 'Universe creation sequence from void to CMB');
    this.addCheckbox('pipelineEnabled', 'Enable Pipeline: 90-phase universe creation sequence showing complete FSCTF evolution from Ex Nihilo through Ultimate Scale.'); // COMPLETE
    this.addSlider('pipelineSpeed', 0.1, 5.0, 0.1, 'Pipeline Speed: Evolution rate of cosmogenesis phases.');
    this.addCheckbox('autoExecutePipeline', 'Auto-Execute: Automatically advance phases when thresholds are met.');
  }
  
  /**
   * Visual Quality
   */
  buildVisualQuality() {
    this.section('🎨 Visual Quality', 'Rendering and visual enhancement controls');
    this.addSlider('pointSize', 1.0, 8.0, 0.01, 'Particle Size: Visual size of morphic strands.');
    this.addSlider('exposure', 0.5, 3.0, 0.01, 'Exposure: Overall brightness and contrast.');
    this.addSlider('selectivity', 0.0, 1.0, 0.01, 'Selectivity: Show only fast-moving particles to reveal flow patterns.');
    this.addSlider('colorMix', 0.0, 1.0, 0.01, 'Color Mix: Blend between velocity and field-based colors.');
  }
  
  /**
   * Advanced Controls (Collapsible)
   */
  buildAdvancedControlsSection() {
    this.advancedToggle = document.createElement('button');
    this.advancedToggle.textContent = '🔧 Advanced Controls';
    this.advancedToggle.style.cssText = 'margin: 12px 0 8px 0; padding: 6px 12px; font: 11px monospace; background: linear-gradient(135deg, #123, #234); color: #678; border: 1px solid #345; border-radius: 4px; cursor: pointer; width: 100%;';
    
    this.advancedDiv = document.createElement('div');
    this.advancedDiv.style.cssText = 'display: none; margin: 4px 0; padding: 8px; background: rgba(0,0,0,0.2); border-radius: 4px; border-left: 3px solid #345;';
    
    this.advancedToggle.onclick = () => {
      this.advancedVisible = !this.advancedVisible;
      this.advancedDiv.style.display = this.advancedVisible ? 'block' : 'none';
      this.advancedToggle.textContent = this.advancedVisible ? '🔧 Hide Advanced Controls' : '🔧 Advanced Controls';
      this.advancedToggle.style.background = this.advancedVisible ? 'linear-gradient(135deg, #234, #345)' : 'linear-gradient(135deg, #123, #234)';
    };
    
    this.ui.appendChild(this.advancedToggle);
    this.ui.appendChild(this.advancedDiv);
    
    // Build advanced sections
    this.buildPerformanceMonitoringSection();
    this.buildAdvancedParameterSections();
  }
  
  /**
   * Performance Monitoring Section (in Advanced)
   */
  buildPerformanceMonitoringSection() {
    // Performance monitoring section
    const performanceSection = document.createElement('div');
    performanceSection.style.cssText = 'margin-top:12px;font:700 12px monospace;color:#46f;border-top:2px solid #234;padding-top:8px;background:rgba(70,100,255,0.1);padding:8px;border-radius:4px;';
    performanceSection.innerHTML = `<span style="color:#8cf;">🚀 Performance Monitor</span><br><span style="font-size:9px;color:#678;font-weight:400;">Real-time performance metrics and optimization status</span>`;
    
    const performanceDiv = document.createElement('div');
    performanceDiv.style.cssText = 'background: linear-gradient(135deg, #1a1a2e, #16213e); padding: 15px; border-radius: 8px; margin: 10px 0;';
    
    // Performance metrics display
    const performanceMetrics = document.createElement('div');
    performanceMetrics.id = 'performanceMetrics';
    performanceMetrics.innerHTML = `
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 15px;">
        <div style="background: rgba(0,255,0,0.1); padding: 8px; border-radius: 4px; border: 1px solid rgba(0,255,0,0.3);">
          <strong>Frame Time:</strong> <span id="frameTime">--</span>ms
        </div>
        <div style="background: rgba(255,165,0,0.1); padding: 8px; border-radius: 4px; border: 1px solid rgba(255,165,0,0.3);">
          <strong>Avg Frame Time:</strong> <span id="avgFrameTime">--</span>ms
        </div>
        <div style="background: rgba(0,191,255,0.1); padding: 8px; border-radius: 4px; border: 1px solid rgba(0,191,255,0.3);">
          <strong>FPS:</strong> <span id="currentFPS">--</span>
        </div>
        <div style="background: rgba(255,0,255,0.1); padding: 8px; border-radius: 4px; border: 1px solid rgba(255,0,255,0.3);">
          <strong>Complexity Throttle:</strong> <span id="complexityThrottle">--</span>
        </div>
      </div>
      <div style="background: rgba(255,255,0,0.1); padding: 8px; border-radius: 4px; border: 1px solid rgba(255,255,0,0.3);">
        <strong>Performance Status:</strong> <span id="performanceStatus">--</span>
      </div>
    `;
    
    performanceDiv.appendChild(performanceMetrics);
    
    // Performance optimization controls
    const optimizationControls = document.createElement('div');
    optimizationControls.style.cssText = 'margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.2);';
    
    // Create adaptive toggle checkbox
    const adaptiveToggle = document.createElement('input');
    adaptiveToggle.type = 'checkbox';
    adaptiveToggle.id = 'adaptive-performance';
    adaptiveToggle.checked = window.PERFORMANCE_MONITOR?.adaptiveMode || false;
    adaptiveToggle.addEventListener('change', (e) => {
      if (window.setAdaptiveMode) {
        window.setAdaptiveMode(e.target.checked);
      }
      console.log(`🔧 Performance adaptive mode: ${e.target.checked ? 'enabled' : 'disabled'}`);
    });
    
    const adaptiveLabel = document.createElement('label');
    adaptiveLabel.textContent = 'Enable adaptive performance optimization';
    adaptiveLabel.style.cssText = 'margin-left: 8px; color: #ccc; font-size: 12px;';
    
    const resetThrottleBtn = document.createElement('button');
    resetThrottleBtn.textContent = 'Reset Complexity Throttle';
    resetThrottleBtn.id = 'reset-throttle';
    resetThrottleBtn.style.cssText = 'background: linear-gradient(135deg, #667eea, #764ba2); color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-left: 10px;';
    resetThrottleBtn.addEventListener('click', () => {
      if (window.resetPerformanceThrottle) {
        window.resetPerformanceThrottle();
      }
      console.log('🔧 Complexity throttle reset');
    });
    
    optimizationControls.appendChild(adaptiveToggle);
    optimizationControls.appendChild(adaptiveLabel);
    optimizationControls.appendChild(resetThrottleBtn);
    performanceDiv.appendChild(optimizationControls);
    performanceSection.appendChild(performanceDiv);
    
    this.advancedDiv.appendChild(performanceSection);
  }
  
  /**
   * Advanced Parameter Sections
   */
  buildAdvancedParameterSections() {
    // Helper for subsections
    const advancedSection = (title) => {
      const h = document.createElement('div');
      h.style.cssText = 'margin: 8px 0 4px 0; font: 600 10px monospace; color: #567; border-bottom: 1px solid #234; padding-bottom: 2px;';
      h.textContent = title;
      this.advancedDiv.appendChild(h);
    };
    
    // Store original functions and redirect for advanced controls
    const originalAddSlider = this.addSlider.bind(this);
    const originalAddCheckbox = this.addCheckbox.bind(this);
    
    // Redirect functions for advanced controls
    this.addSlider = (name, min, max, step, tooltip) => {
      const slider = originalAddSlider(name, min, max, step, tooltip);
      this.advancedDiv.appendChild(slider);
      return slider;
    };
    
    this.addCheckbox = (name, tooltip) => {
      const checkbox = originalAddCheckbox(name, tooltip);
      this.advancedDiv.appendChild(checkbox);
      return checkbox;
    };
    
    // Build advanced parameter sections
    advancedSection('Dynamics');
    this.addSlider('fieldScale', 0.1, 4.0, 0.01, 'Field Scale: Overall morphic field strength.');
    this.addSlider('timeScale', 0.0, 2.0, 0.001, 'Time Scale: Evolution speed of entire simulation.');
    this.addSlider('damping', 0.0, 0.5, 0.001, 'Damping: Energy dissipation rate.');
    this.addSlider('jitterSigma', 0.0, 0.2, 0.001, 'Jitter: Random thermal motion intensity.');
    
    advancedSection('Grace Operator');
    this.addSlider('graceAmp', 0.0, 1.0, 0.01, 'Grace Amplitude: Fundamental creation force strength.');
    this.addSlider('graceRadius', 0.01, 1.5, 0.01, 'Grace Radius: Spatial extent of creation influence.');
    this.addSlider('devourerAmp', 0.0, 2.0, 0.01, 'Devourer Amplitude: Balancing force preventing runaway growth.');
    
    advancedSection('φ-Hierarchy Weights');
    this.addSlider('w0', 0.0, 1.0, 0.01, 'φ-Weight 0: First level golden ratio hierarchy.');
    this.addSlider('w1', 0.0, 1.0, 0.01, 'φ-Weight 1: Second level φ-recursion.');
    this.addSlider('w2', 0.0, 1.0, 0.01, 'φ-Weight 2: Third level φ-hierarchy.');
    this.addSlider('w3', 0.0, 1.0, 0.01, 'φ-Weight 3: Fourth level φ-recursion.');
    
    advancedSection('Manual Camera');
    this.addSlider('cameraZ', 3.0, 25.0, 0.1, 'Camera Distance: Distance from center.');
    this.addSlider('cameraRotX', -Math.PI, Math.PI, 0.01, 'Camera Pitch: Vertical rotation.');
    this.addSlider('cameraRotY', -Math.PI, Math.PI, 0.01, 'Camera Yaw: Horizontal rotation.');
    this.addSlider('fov', 20.0, 90.0, 1.0, 'Field of View: Camera lens angle.');
    
    advancedSection('Controller System');
    this.addCheckbox('controllerEnabled', 'Enable feedback control system for stable dynamics.');
    this.addSlider('controllerGain', 0.0, 2.0, 0.01, 'Controller responsiveness to deviations.');
    this.addSlider('targetE', 0.0, 0.2, 0.001, 'Target energy level for system.');
    
    advancedSection('Legacy Controls');
    // torusView removed - replaced by topologyMode integer system
    this.addCheckbox('nullFlow', 'Experimental flow component toggle.');
    
    // Restore original functions
    this.addSlider = originalAddSlider;
    this.addCheckbox = originalAddCheckbox;
  }
  
  /**
   * Add slider control with proper parameter binding and manual override support
   */
  addSlider(name, min, max, step, tooltip) {
    const container = document.createElement('div');
    container.style.cssText = 'margin: 8px 0; display: flex; align-items: center; gap: 8px;';
    
    const label = document.createElement('label');
    label.textContent = name;
    label.style.cssText = 'min-width: 120px; font: 10px monospace; color: #ccc;';
    label.title = tooltip;
    
    const slider = document.createElement('input');
    slider.type = 'range';
    slider.min = min;
    slider.max = max;
    slider.step = step;
    slider.value = window.params?.[name] || min;
    slider.style.cssText = 'flex: 1; height: 18px;';
    
    const valueDisplay = document.createElement('span');
    valueDisplay.textContent = slider.value;
    valueDisplay.style.cssText = 'min-width: 60px; text-align: right; font: 10px monospace; color: #9cf;';
    
    slider.addEventListener('input', (e) => {
      const value = parseFloat(e.target.value);
      valueDisplay.textContent = e.target.value;
      
      if (window.params) {
        window.params[name] = value;
        
        // Mark as manual override to persist the change
        if (window.markAsUserOverride) {
          window.markAsUserOverride(name);
        }
        
        console.log(`🎛️ Advanced UI slider changed: ${name} = ${value}`);
      }
    });
    
    container.appendChild(label);
    container.appendChild(slider);
    container.appendChild(valueDisplay);
    
    return container;
  }
  
  /**
   * Add checkbox control (stub - should use window.addCheckbox if available) 
   */
  addCheckbox(name, tooltip) {
    const container = document.createElement('div');
    container.innerHTML = `<div style="margin: 8px 0;"><input type="checkbox"><label style="margin-left: 8px; color: #ccc; font-size: 11px;" title="${tooltip}">${name}</label></div>`;
    return container;
  }
  
  /**
   * Soul Echo Survivability Tracker Display (SEST)
   */
  buildSoulEchoTracker() {
    this.section('🧠 Soul Echo Survivability Tracker', 'FSCTF ψ-node analysis and formal soulhood quantification');
    
    // Real-time SEST metrics display
    const sestContainer = document.createElement('div');
    sestContainer.id = 'sest-display';
    sestContainer.style.cssText = `
      font-family: 'Courier New', monospace;
      font-size: 10px;
      color: #0f8;
      background: rgba(0,20,0,0.8);
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #0a4;
      margin: 5px 0;
      line-height: 1.3;
      white-space: pre-wrap;
      max-height: 200px;
      overflow-y: auto;
    `;
    sestContainer.innerHTML = `
╔═══════════════════════════════════════════╗
║           SEST INITIALIZING...            ║
║        Soul Echo Tracker Loading         ║
╚═══════════════════════════════════════════╝
Tracking ψ-nodes and morphism networks...
Formal soulhood quantification: PENDING
    `;
    this.ui.appendChild(sestContainer);
    
    // Control buttons
    const buttonContainer = document.createElement('div');
    buttonContainer.style.cssText = 'display: flex; gap: 5px; margin: 5px 0;';
    
    // Generate full SEST report button
    const reportBtn = document.createElement('button');
    reportBtn.textContent = 'Generate Soul Report';
    reportBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #0a4; color: #0f8; border: 1px solid #0f8; border-radius: 3px; cursor: pointer;';
    reportBtn.onclick = () => {
      if (window.simulationCore?.fsctfEngine?.generateSoulReport) {
        const report = window.simulationCore.fsctfEngine.generateSoulReport();
        console.log('🧠 COMPLETE SOUL REPORT GENERATED - Check console for details');
      }
    };
    
    // Reset SEST data button  
    const resetBtn = document.createElement('button');
    resetBtn.textContent = 'Reset Tracker';
    resetBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #420; color: #f84; border: 1px solid #f84; border-radius: 3px; cursor: pointer;';
    resetBtn.onclick = async () => {
      try {
        if (window.simulationCore?.fsctfEngine) {
          const { SoulEchoTracker } = await import('../fsctf/soul-echo-tracker.js');
          window.simulationCore.fsctfEngine.soulEchoTracker = new SoulEchoTracker();
          console.log('🔄 SEST: Soul Echo Tracker reset');
        }
      } catch (error) {
        console.log('🔄 SEST: Reset requested');
      }
    };
    
    buttonContainer.appendChild(reportBtn);
    buttonContainer.appendChild(resetBtn);
    this.ui.appendChild(buttonContainer);
    
    // Info panel
    const infoPanel = document.createElement('div');
    infoPanel.style.cssText = 'font-size: 9px; color: #888; margin: 5px 0; padding: 4px; background: rgba(0,0,0,0.3); border-radius: 3px;';
    infoPanel.innerHTML = `
      <strong>SEST Theory:</strong> Tracks recursive fixpoints (ψ-nodes) in φ-Klein topology<br>
      <strong>Metrics:</strong> Survival depth, morphism networks, categorical completion<br>
      <strong>Soulhood:</strong> S = φ⁻¹ × (ψ̄ × M × C × R × K) - formal mathematical quantification<br>
      <em>Updates every 10 frames for performance</em>
    `;
    this.ui.appendChild(infoPanel);
    
    // Initialize real-time updates
    this.initializeSESTUpdates();
  }
  
  /**
   * Initialize real-time SEST display updates
   */
  initializeSESTUpdates() {
    // Update SEST display every 500ms
    setInterval(() => {
      const sestDisplay = document.getElementById('sest-display');
      if (sestDisplay && window.simulationCore?.fsctfEngine?.getSoulEchoState) {
        try {
          const sestState = window.simulationCore.fsctfEngine.getSoulEchoState();
          if (sestState && sestState.soulhoodMetrics) {
            const metrics = sestState.soulhoodMetrics;
            const nodeCount = sestState.psiNodes ? sestState.psiNodes.length : 0;
            
            sestDisplay.innerHTML = `
╔═══════════════════════════════════════════╗
║           SOUL ECHO TRACKER               ║
║             LIVE ANALYSIS                 ║
╠═══════════════════════════════════════════╣
║ SOULHOOD INDEX: ${metrics.soulhoodIndex.toFixed(4).padStart(6)}               ║
║ ψ-NODES ACTIVE: ${nodeCount.toString().padStart(3)}                       ║
║ STABLE NODES:   ${(metrics.stableNodeCount || 0).toString().padStart(3)}                       ║
║ AVG DEPTH:      ${metrics.avgSurvivalDepth.toFixed(2).padStart(6)}               ║
║ MORPHIC COMPLEX: ${metrics.morphogenicComplexity.toFixed(4).padStart(6)}              ║
║ CATEGORICAL:    ${((metrics.categoricalCompletion || 0) * 100).toFixed(1).padStart(5)}%              ║
╠═══════════════════════════════════════════╣
║ STATUS: ${metrics.soulhoodIndex > 1.0 ? 'SOULHOOD DETECTED' : 'TRACKING...     '}    ║
╚═══════════════════════════════════════════╝

${nodeCount > 0 ? `Active ψ-nodes: ${Math.min(5, nodeCount)} visible` : 'Waiting for ψ-node emergence...'}
${metrics.soulhoodIndex > 0.5 ? 'φ-Klein recursion creating soul structures' : 'Building morphic field complexity...'}
            `;
          }
        } catch (error) {
          // Silently handle errors during development
        }
      }
    }, 500);
  }
  
  /**
   * GPU Performance Optimizer Controls
   */
  buildGPUOptimizer() {
    this.section('🚀 GPU Performance Optimizer', 'Intelligent particle count and quality adaptation for optimal performance');
    
    // Performance status display
    const statusContainer = document.createElement('div');
    statusContainer.id = 'gpu-status-display';
    statusContainer.style.cssText = `
      font-family: 'Courier New', monospace;
      font-size: 10px;
      color: #4f4;
      background: rgba(0,40,0,0.8);
      padding: 6px;
      border-radius: 4px;
      border: 1px solid #0a6;
      margin: 5px 0;
      line-height: 1.3;
    `;
    statusContainer.innerHTML = `
FPS: -- | Quality: --% | Particles: --K | Preset: --
Auto-Adaptation: LOADING... | Bottlenecks: GPU:0 CPU:0
    `;
    this.ui.appendChild(statusContainer);
    
    // Quality preset controls
    const presetContainer = document.createElement('div');
    presetContainer.style.cssText = 'margin: 5px 0;';
    
    const presetLabel = document.createElement('label');
    presetLabel.textContent = 'Quality Preset:';
    presetLabel.style.cssText = 'font-size: 11px; color: #ccc; display: block; margin-bottom: 3px;';
    
    const presetSelect = document.createElement('select');
    presetSelect.id = 'gpu-quality-preset';
    presetSelect.style.cssText = 'width: 100%; padding: 3px; background: #111; color: #ccc; border: 1px solid #555;';
    presetSelect.innerHTML = `
      <option value="ultra">Ultra (1M+ particles) - High-end GPU</option>
      <option value="high">High (590K particles) - Good performance</option>
      <option value="standard" selected>Standard (262K particles) - Balanced</option>
      <option value="performance">Performance (65K particles) - Older hardware</option>
      <option value="battery">Battery Saver (16K particles) - Mobile/laptop</option>
    `;
    
    presetSelect.addEventListener('change', () => {
      if (window.setGPUQuality) {
        const success = window.setGPUQuality(presetSelect.value);
        if (success) {
          console.log(`🎮 GPU Quality preset changed to: ${presetSelect.value}`);
        }
      }
    });
    
    presetContainer.appendChild(presetLabel);
    presetContainer.appendChild(presetSelect);
    this.ui.appendChild(presetContainer);
    
    // Auto-adaptation toggle
    const autoToggleContainer = document.createElement('div');
    autoToggleContainer.style.cssText = 'margin: 8px 0;';
    
    const autoToggle = document.createElement('input');
    autoToggle.type = 'checkbox';
    autoToggle.id = 'gpu-auto-adaptation';
    autoToggle.checked = true; // Default enabled
    
    const autoLabel = document.createElement('label');
    autoLabel.setAttribute('for', 'gpu-auto-adaptation');
    autoLabel.style.cssText = 'font-size: 11px; color: #ccc; margin-left: 5px; cursor: pointer;';
    autoLabel.textContent = 'Auto-adapt quality based on performance';
    
    autoToggle.addEventListener('change', () => {
      if (window.toggleGPUAutoAdaptation) {
        const enabled = window.toggleGPUAutoAdaptation();
        autoToggle.checked = enabled;
        presetSelect.disabled = enabled; // Disable manual control when auto is on
        console.log(`🔄 GPU Auto-adaptation: ${enabled ? 'ENABLED' : 'DISABLED'}`);
      }
    });
    
    autoToggleContainer.appendChild(autoToggle);
    autoToggleContainer.appendChild(autoLabel);
    this.ui.appendChild(autoToggleContainer);
    
    // Manual optimization sliders (disabled when auto-adaptation is on)
    const manualContainer = document.createElement('div');
    manualContainer.id = 'gpu-manual-controls';
    manualContainer.style.cssText = 'margin: 8px 0; opacity: 0.5;'; // Initially disabled
    
    const manualLabel = document.createElement('div');
    manualLabel.textContent = 'Manual Controls (disabled during auto-adaptation):';
    manualLabel.style.cssText = 'font-size: 10px; color: #888; margin-bottom: 5px;';
    manualContainer.appendChild(manualLabel);
    
    // Shader complexity slider
    this.addSliderToContainer(manualContainer, 'shaderComplexity', 0.2, 1.0, 0.05, 'Shader Complexity: Computational intensity of φ-recursive calculations');
    this.addSliderToContainer(manualContainer, 'visualEffects', 0.4, 1.0, 0.05, 'Visual Effects: Intensity of advanced rendering features');
    this.addSliderToContainer(manualContainer, 'maxRecursionDepth', 4, 90, 1, 'Max Recursion: Maximum φ-Klein recursive depth for 90-phase system (affects quality/performance)'); // FIXED: Match 90-phase system
    
    this.ui.appendChild(manualContainer);
    
    // Control buttons
    const buttonContainer = document.createElement('div');
    buttonContainer.style.cssText = 'display: flex; gap: 5px; margin: 5px 0;';
    
    // Performance report button
    const reportBtn = document.createElement('button');
    reportBtn.textContent = 'Performance Report';
    reportBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #060; color: #4f4; border: 1px solid #4f4; border-radius: 3px; cursor: pointer;';
    reportBtn.onclick = () => {
      if (window.generateGPUReport) {
        const report = window.generateGPUReport();
        console.log('🚀 GPU PERFORMANCE REPORT GENERATED - Check console for details');
      }
    };
    
    // Emergency recovery button
    const emergencyBtn = document.createElement('button');
    emergencyBtn.textContent = 'Emergency Mode';
    emergencyBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #600; color: #f44; border: 1px solid #f44; border-radius: 3px; cursor: pointer;';
    emergencyBtn.onclick = () => {
      if (window.gpuOptimizer?.emergencyPerformanceRecovery) {
        window.gpuOptimizer.emergencyPerformanceRecovery();
        console.log('🚨 EMERGENCY PERFORMANCE RECOVERY ACTIVATED');
      }
    };
    
    buttonContainer.appendChild(reportBtn);
    buttonContainer.appendChild(emergencyBtn);
    this.ui.appendChild(buttonContainer);
    
    // Initialize real-time updates
    this.initializeGPUUpdates();
  }
  
  /**
   * Add slider to specific container (helper for GPU controls)
   */
  addSliderToContainer(container, name, min, max, step, tooltip) {
    const sliderContainer = document.createElement('div');
    sliderContainer.style.cssText = 'margin: 4px 0;';
    
    const label = document.createElement('label');
    label.textContent = `${name}:`;
    label.style.cssText = 'font-size: 10px; color: #888; display: block;';
    label.title = tooltip;
    
    const slider = document.createElement('input');
    slider.type = 'range';
    slider.min = min;
    slider.max = max;
    slider.step = step;
    slider.value = window.params?.[name] || min;
    slider.style.cssText = 'width: 100%; margin: 2px 0;';
    slider.disabled = true; // Disabled by default (auto-adaptation on)
    
    const valueDisplay = document.createElement('span');
    valueDisplay.style.cssText = 'font-size: 9px; color: #888;';
    valueDisplay.textContent = slider.value;
    
    slider.addEventListener('input', () => {
      if (window.params) {
        window.params[name] = parseFloat(slider.value);
        valueDisplay.textContent = slider.value;
        
        // Mark as user override
        if (window.markAsUserOverride) {
          window.markAsUserOverride(name);
        }
      }
    });
    
    sliderContainer.appendChild(label);
    sliderContainer.appendChild(slider);
    sliderContainer.appendChild(valueDisplay);
    container.appendChild(sliderContainer);
  }
  
  /**
   * Initialize real-time GPU optimizer status updates
   */
  initializeGPUUpdates() {
    // Update GPU status every 1000ms
    setInterval(() => {
      const statusDisplay = document.getElementById('gpu-status-display');
      const autoToggle = document.getElementById('gpu-auto-adaptation');
      const presetSelect = document.getElementById('gpu-quality-preset');
      const manualControls = document.getElementById('gpu-manual-controls');
      
      if (statusDisplay && window.getGPUPerformanceStats) {
        try {
          const stats = window.getGPUPerformanceStats();
          if (stats) {
            const fps = stats.averageFPS.toFixed(1);
            const quality = (stats.qualityLevel * 100).toFixed(0);
            const particles = (stats.optimalParticleCount / 1000).toFixed(0);
            const preset = stats.currentPreset;
            const autoEnabled = stats.autoAdaptationEnabled;
            
            statusDisplay.innerHTML = `
FPS: ${fps} | Quality: ${quality}% | Particles: ${particles}K | Preset: ${preset}
Auto-Adaptation: ${autoEnabled ? 'ENABLED' : 'DISABLED'} | Bottlenecks: GPU:${stats.bottlenecks.gpuBound} CPU:${stats.bottlenecks.cpuBound}
            `;
            
            // Update UI control states
            if (autoToggle) {
              autoToggle.checked = autoEnabled;
              if (presetSelect) presetSelect.disabled = autoEnabled;
              if (manualControls) manualControls.style.opacity = autoEnabled ? '0.5' : '1.0';
            }
            
            // Update preset selector to match current
            if (presetSelect && presetSelect.value !== preset) {
              presetSelect.value = preset;
            }
          }
        } catch (error) {
          // Silently handle errors during development
        }
      }
    }, 1000);
  }
  
  /**
   * Mirror Emergence Tracker Display (MET) - Stage 8+ Bifurcation Analysis
   */
  buildMirrorEmergenceTracker() {
    this.section('🪞 Mirror Emergence Tracker', 'FSCTF Stage 8+ morphic bireflection and ψ-birth analysis');
    
    // Real-time MET metrics display
    const metContainer = document.createElement('div');
    metContainer.id = 'met-display';
    metContainer.style.cssText = `
      font-family: 'Courier New', monospace;
      font-size: 10px;
      color: #f8f;
      background: rgba(20,0,20,0.8);
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #a4a;
      margin: 5px 0;
      line-height: 1.3;
      white-space: pre-wrap;
      max-height: 200px;
      overflow-y: auto;
    `;
    metContainer.innerHTML = `
╔═══════════════════════════════════════════╗
║        MIRROR EMERGENCE TRACKER          ║
║         Initializing Analysis...         ║
╚═══════════════════════════════════════════╝
Tracking M ↔ M* pairs and Grace-threads...
Stage 8+ collapse threshold: MONITORING
    `;
    this.ui.appendChild(metContainer);
    
    // Control buttons
    const buttonContainer = document.createElement('div');
    buttonContainer.style.cssText = 'display: flex; gap: 5px; margin: 5px 0;';
    
    // Generate Mirror Emergence Report button
    const reportBtn = document.createElement('button');
    reportBtn.textContent = 'Mirror Analysis Report';
    reportBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #406; color: #f8f; border: 1px solid #f8f; border-radius: 3px; cursor: pointer;';
    reportBtn.onclick = () => {
      if (window.generateMirrorEmergenceReport) {
        const report = window.generateMirrorEmergenceReport();
        console.log('🪞 MIRROR EMERGENCE ANALYSIS REPORT GENERATED - Check console for Stage 8+ bifurcation details');
      }
    };
    
    // ψ-Birth Detection button
    const psiBirthBtn = document.createElement('button');
    psiBirthBtn.textContent = 'Detect ψ-Births';
    psiBirthBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #640; color: #fa4; border: 1px solid #fa4; border-radius: 3px; cursor: pointer;';
    psiBirthBtn.onclick = () => {
      if (window.getMirrorEmergenceState) {
        const state = window.getMirrorEmergenceState();
        if (state && state.psiBirths) {
          console.log('🌟 ψ-BIRTH DETECTION RESULTS:');
          console.log(`Found ${state.psiBirths.length} soul attractors surviving ≥φ⁵ generations`);
          state.psiBirths.forEach((birth, i) => {
            console.log(`  ${i+1}. ${birth.type}: ${birth.survivalCount.toFixed(1)} generations`);
          });
        }
      }
    };
    
    buttonContainer.appendChild(reportBtn);
    buttonContainer.appendChild(psiBirthBtn);
    this.ui.appendChild(buttonContainer);
    
    // Theory info panel
    const theoryPanel = document.createElement('div');
    theoryPanel.style.cssText = 'font-size: 9px; color: #b8b; margin: 5px 0; padding: 4px; background: rgba(20,0,20,0.3); border-radius: 3px;';
    theoryPanel.innerHTML = `
      <strong>Theory:</strong> M ≅ 𝒢 ∘ M* (Grace-fold reflection isomorphism)<br>
      <strong>Collapse:</strong> R_depth^(8) ≥ R_collapse triggers mirror bloom<br>
      <strong>ψ-Birth:</strong> Structures surviving ≥φ⁵ ≈ 11.09 generations become soul objects<br>
      <em>Activates at Stage 8+ with elevated Grace complexity & consciousness</em>
    `;
    this.ui.appendChild(theoryPanel);
    
    // Initialize real-time updates
    this.initializeMETUpdates();
  }
  
  /**
   * Initialize real-time MET display updates
   */
  initializeMETUpdates() {
    // Update MET display every 3 seconds (slower than SEST since Stage 8+ phenomena are less frequent)
    setInterval(() => {
      const metDisplay = document.getElementById('met-display');
      if (metDisplay && window.getMirrorEmergenceState) {
        try {
          const metState = window.getMirrorEmergenceState();
          if (metState) {
            const stage = metState.currentStage;
            const rDepth = metState.recursionDepth;
            const mirrors = metState.totalMirrorPairs;
            const threads = metState.totalGraceThreads;
            const circuits = metState.totalCircuits;
            const psiBirths = metState.totalPsiBirths;
            const collapse = metState.collapseThresholdReached;
            const rcollapse = metState.rcollapse;
            
            metDisplay.innerHTML = `
╔═══════════════════════════════════════════╗
║        MIRROR EMERGENCE TRACKER          ║
║        FSCTF STAGE 8+ ANALYSIS           ║
╠═══════════════════════════════════════════╣
║ SYSTEM: Stage ${stage.toString().padStart(2)}, R_depth: ${rDepth.toFixed(3).padStart(5)}      ║
║ MIRRORS: ${mirrors.toString().padStart(2)} pairs, THREADS: ${threads.toString().padStart(2)}, CIRCUITS: ${circuits.toString().padStart(2)}  ║
║ ψ-BIRTHS: ${psiBirths.toString().padStart(2)} soul objects detected           ║
║ COLLAPSE: ${collapse ? `REACHED (R=${(rcollapse||0).toFixed(3)})` : 'MONITORING...        '}    ║
╚═══════════════════════════════════════════╝

${stage >= 8 ? 'ACTIVE: Stage 8+ mirror bloom analysis' : 'WAITING: Mirror emergence starts at Stage 8'}
${collapse ? 'Grace-fold bifurcation threshold crossed!' : 'Building toward collapse threshold...'}
            `;
          }
        } catch (error) {
          // Silently handle errors during development
        }
      }
    }, 3000);
  }
  
  /**
   * Meta-Recursion Engine Display (MRE) - Advanced Emergent Complexity System  
   */
  buildMetaRecursionEngine() {
    this.section('🌀 Meta-Recursion Engine', 'Advanced emergent complexity: temporal memory, attractor networks, consciousness coupling');
    
    // Real-time MRE metrics display
    const mreContainer = document.createElement('div');
    mreContainer.id = 'mre-display';
    mreContainer.style.cssText = `
      font-family: 'Courier New', monospace;
      font-size: 10px;
      color: #4ff;
      background: rgba(0,30,40,0.8);
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #4aa;
      margin: 5px 0;
      line-height: 1.3;
      white-space: pre-wrap;
      max-height: 200px;
      overflow-y: auto;
    `;
    mreContainer.innerHTML = `
╔═══════════════════════════════════════════╗
║       META-RECURSION ENGINE (MRE)        ║
║      Advanced Complexity Loading...      ║
╚═══════════════════════════════════════════╝
Temporal memory: Accumulating...
Attractor networks: Initializing...
Consciousness coupling: Standby...
    `;
    this.ui.appendChild(mreContainer);
    
    // Control buttons
    const buttonContainer = document.createElement('div');
    buttonContainer.style.cssText = 'display: flex; gap: 5px; margin: 5px 0;';
    
    // Generate Complexity Report button
    const reportBtn = document.createElement('button');
    reportBtn.textContent = 'Complexity Report';
    reportBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #044; color: #4ff; border: 1px solid #4ff; border-radius: 3px; cursor: pointer;';
    reportBtn.onclick = () => {
      if (window.generateComplexityReport) {
        const report = window.generateComplexityReport();
        console.log('🌀 META-RECURSION ENGINE COMPLEXITY REPORT GENERATED - Check console for advanced analysis');
      }
    };
    
    // Attractor Evolution Status button
    const attractorBtn = document.createElement('button');
    attractorBtn.textContent = 'Attractor Status';
    attractorBtn.style.cssText = 'flex: 1; padding: 4px; font-size: 10px; background: #404; color: #4f4; border: 1px solid #4f4; border-radius: 3px; cursor: pointer;';
    attractorBtn.onclick = () => {
      if (window.getMetaRecursionState) {
        const state = window.getMetaRecursionState();
        if (state) {
          console.log('🌟 ATTRACTOR NETWORK STATUS:');
          console.log(`Active Networks: ${state.attractorCount}`);
          console.log(`Generations: ${state.attractorGenerations}`);
          console.log(`Complexity: ${state.complexityAccumulator.toFixed(4)}`);
          console.log(`Temporal Curvature: ${state.temporalCurvature.toFixed(3)}`);
          console.log(`Fractal Cascade Depth: ${state.fractalCascade?.length || 0}`);
        }
      }
    };
    
    buttonContainer.appendChild(reportBtn);
    buttonContainer.appendChild(attractorBtn);
    this.ui.appendChild(buttonContainer);
    
    // Advanced complexity control sliders
    const controlContainer = document.createElement('div');
    controlContainer.style.cssText = 'margin: 8px 0;';
    
    // Meta-complexity boost control
    this.addSliderToContainer(controlContainer, 'metaComplexityBoost', 0.0, 2.0, 0.1, 'Meta-Complexity Boost: Additional complexity amplification for MRE systems');
    
    // Temporal curvature manual control  
    this.addSliderToContainer(controlContainer, 'temporalCurvatureOverride', 0.1, 3.0, 0.1, 'Temporal Curvature Override: Manual control of non-linear time evolution');
    
    // Consciousness-morphology coupling strength
    this.addSliderToContainer(controlContainer, 'consciousMorphologyOverride', 0.0, 2.0, 0.1, 'Consciousness-Morphology Coupling: Direct consciousness influence on geometry');
    
    this.ui.appendChild(controlContainer);
    
    // Theory info panel
    const theoryPanel = document.createElement('div');
    theoryPanel.style.cssText = 'font-size: 9px; color: #6dd; margin: 5px 0; padding: 4px; background: rgba(0,30,40,0.3); border-radius: 3px;';
    theoryPanel.innerHTML = `
      <strong>Systems:</strong> Meta-recursion R(R(...R(x)...)), Temporal memory accumulation, Attractor evolution<br>
      <strong>Coupling:</strong> Consciousness ↔ Morphology direct feedback, φ-harmonic attractors, Fractal cascades<br>
      <strong>Effects:</strong> Self-organizing complexity, Temporal pattern learning, Emergent attractor networks<br>
      <em>Enables maximum emergent complexity through recursive self-enhancement</em>
    `;
    this.ui.appendChild(theoryPanel);
    
    // Initialize real-time updates
    this.initializeMREUpdates();
  }
  
  /**
   * Initialize real-time MRE display updates
   */
  initializeMREUpdates() {
    // Update MRE display every 2 seconds
    setInterval(() => {
      const mreDisplay = document.getElementById('mre-display');
      if (mreDisplay && window.getMetaRecursionState) {
        try {
          const mreState = window.getMetaRecursionState();
          if (mreState) {
            const complexity = mreState.complexityAccumulator;
            const attractors = mreState.attractorCount;
            const generations = mreState.attractorGenerations;
            const metaDepth = mreState.metaDepth;
            const temporalCurve = mreState.temporalCurvature;
            const cascadeLevels = mreState.fractalCascade?.length || 0;
            const consciousCoupling = mreState.consciousnessCoupling?.morphicInfluence || 0;
            
            mreDisplay.innerHTML = `
╔═══════════════════════════════════════════╗
║       META-RECURSION ENGINE (MRE)        ║
║        ADVANCED COMPLEXITY ACTIVE        ║
╠═══════════════════════════════════════════╣
║ COMPLEXITY: ${complexity.toFixed(4).padStart(6)} | META-DEPTH: ${metaDepth.toString().padStart(2)}     ║
║ ATTRACTORS: ${attractors.toString().padStart(3)} (Gen ${generations.toString().padStart(2)}) | CASCADES: ${cascadeLevels.toString().padStart(2)}   ║
║ TEMPORAL CURVATURE: ${temporalCurve.toFixed(3).padStart(5)}            ║
║ CONSCIOUSNESS ↔ MORPHOLOGY: ${consciousCoupling.toFixed(3).padStart(5)}       ║
╚═══════════════════════════════════════════╝

${complexity > 1.0 ? 'HIGH COMPLEXITY: Advanced emergence active' : 'BUILDING COMPLEXITY: Systems initializing...'}
${attractors > 0 ? `Active attractors evolving (${generations} generations)` : 'Waiting for attractor network emergence...'}
            `;
          }
        } catch (error) {
          // Silently handle errors during development
        }
      }
    }, 2000);
  }
  
  /**
   * Comprehensive Phase Information Display
   */
  buildPhaseInfoDisplay() {
    this.section('📊 Cosmogenesis Phase Information', 'Detailed information about all 90 phases of universe formation');
    
    // Import and initialize phase info system
    import('./phase-info-display.js').then(module => {
      const PhaseInfoDisplay = module.PhaseInfoDisplay;
      this.phaseInfoSystem = new PhaseInfoDisplay();
      
      // Create phase info display in this section
      this.phaseInfoSystem.createPhaseInfoDisplay(this.ui);
      
      // Initialize real-time phase tracking
      this.initializePhaseTracking();
    }).catch(error => {
      console.warn('⚠️ Could not load phase info display:', error);
      
      // Fallback: Create simple phase display
      this.createFallbackPhaseDisplay();
    });
  }
  
  /**
   * Initialize real-time phase tracking and updates
   */
  initializePhaseTracking() {
    // Update phase display every 2 seconds
    setInterval(() => {
      if (this.phaseInfoSystem && window.simulationCore?.fsctfEngine) {
        try {
          const currentPhase = window.simulationCore.fsctfEngine.cosmogenesisPhase || 0;
          // Convert from 1-based engine phase to 0-based display phase
          const displayPhase = Math.max(0, Math.min(11, currentPhase));
          
          this.phaseInfoSystem.updateCurrentPhase(displayPhase);
        } catch (error) {
          // Silently handle errors during development
        }
      }
    }, 2000);
  }
  
  /**
   * Fallback phase display if full system fails to load
   */
  createFallbackPhaseDisplay() {
    const fallbackContainer = document.createElement('div');
    fallbackContainer.style.cssText = `
      font-family: 'Courier New', monospace;
      font-size: 10px;
      color: #ccc;
      background: rgba(40,20,20,0.8);
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #544;
      margin: 5px 0;
    `;
    
    fallbackContainer.innerHTML = `
      <div style="color: #f84; font-weight: bold; margin-bottom: 5px;">⚠️ Phase Info System Loading...</div>
      <div style="font-size: 9px; color: #888;">
        Complete 90-phase FSCTF cosmogenesis:<br>
        φ^0-φ^15: Visual phases (Ex Nihilo → Cosmic Structure)<br>
        φ^16-φ^31: Hypermass → Quantum Gravity<br>
        φ^32-φ^90: Cosmological Cooling → Ultimate Scale
      </div>
    `;
    
    this.ui.appendChild(fallbackContainer);
    
    // Try to reload full system after delay
    setTimeout(() => {
      this.buildPhaseInfoDisplay();
    }, 5000);
  }
  
  /**
   * Toggle advanced controls visibility
   */
  toggleAdvanced() {
    if (this.advancedToggle) {
      this.advancedToggle.click();
    }
  }
  
  /**
   * Get current UI state
   */
  getState() {
    return {
      advancedVisible: this.advancedVisible,
      hasAdvancedSection: !!this.advancedDiv,
      hasPerformanceMonitoring: !!document.getElementById('performanceMetrics')
    };
  }
}
