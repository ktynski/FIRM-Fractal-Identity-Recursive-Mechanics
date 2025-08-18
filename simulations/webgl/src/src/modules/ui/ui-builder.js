/**
 * UI Builder Module
 * Constructs the complete FSCTF control interface
 */

export class UIBuilder {
  constructor(container) {
    this.ui = container;
    this.paramElements = {};
    this.userOverrides = new Set();
    
    if (this.ui.dataset && this.ui.dataset.built === '1') return;
    if (this.ui.dataset) this.ui.dataset.built = '1';
  }
  
  buildCompleteUI() {
    console.log('🎛️ Building FSCTF Control Interface...');
    
    // Build all sections
    this.buildCoreControls();
    this.buildTopologyControls();
    this.buildCameraControls();
    // buildCosmogenesisControls() REMOVED - conflicts with native FSCTF system
    this.buildVisualControls();
    this.buildAdvancedControls();
    this.buildPerformanceControls();
    
    console.log('✅ UI Construction Complete');
  }
  
  buildCoreControls() {
    this.createSection('🌌 FIRM Core System', 'Primary controls for Field-Strand Coherence Framework');
    
    this.addCheckbox('fsctfEnabled', 'Enable FIRM: Activates the complete theoretical framework driving morphic emergence and topology evolution.');
    
    // User Override Reset Button
    this.createResetButton();
    
    // MATHEMATICAL PARAMETER DERIVATION: Fully implemented φ-mathematics system
    this.addDisplay('𝚽-Mathematical Parameters', '✅ ACTIVE: Parameters automatically derived from golden ratio mathematics and system state');
    
    this.addReadOnlyDisplay('graceComplexity', 'Grace Complexity: φ^(phase/φ) × morphic_field × temporal_harmonic');
    this.addReadOnlyDisplay('morphicRecursionDepth', 'Recursion Depth: φ × phase + consciousness_boost + system_stability');  
    this.addReadOnlyDisplay('consciousnessComplexity', 'Consciousness Complexity: prime_energy × φ^(depth/18) × field_coherence');
    
    this.addDisplay('Manual Override (Emergency)', '⚠️ Fallback sliders - only used if mathematical derivation fails:');
    this.addSlider('graceComplexity', 0.0, 1000.0, 0.1, 'Grace Complexity: φ-recursive creation power (COSMIC SCALE - up to 1000!)');
    this.addSlider('morphicRecursionDepth', 1, 500, 1, 'Recursion Depth: Hypercube recursion levels (COSMIC SCALE - up to 500!)');
    this.addSlider('consciousnessComplexity', 0.5, 1000.0, 0.1, 'Consciousness Complexity: Prime resonance intensity (COSMIC SCALE - up to 1000!)');
  }
  
  buildTopologyControls() {
    this.createSection('🌀 Topology Evolution', 'Control the geometric evolution: Torus → Möbius → Klein → φ-Klein');
    this.addSlider('topologyTransitionDuration', 0.0, 120.0, 0.5, 'Transition Duration: 0=Static topology, 10-60s=Cinematic, 120s=Ultra-slow cosmic evolution');
  }
  
  buildCameraControls() {
    this.createSection('🎥 Orbital Camera System', 'Mouse drag to orbit • Scroll to zoom • Presets for symmetry analysis');
    
    this.addCheckbox('cameraEnabled', 'Enable Camera: Activate orbital camera system with mouse controls.');
    this.addCheckbox('autoRotate', 'Auto-Rotate: Automatic azimuth rotation for dynamic viewing angles.');
    this.addSlider('autoRotateSpeed', 0.1, 5.0, 0.1, 'Auto-Rotate Speed: Speed of automatic orbital rotation.');
    
    this.addSlider('cameraDistance', 1.0, 50.0, 0.5, 'Distance: Zoom level - distance from particle system center.');
    this.addSlider('cameraAzimuth', 0.0, 360.0, 5.0, 'Azimuth: Horizontal orbital angle (degrees) around the center.');
    this.addSlider('cameraElevation', -90.0, 90.0, 2.0, 'Elevation: Vertical viewing angle - positive looks down from above.');
    this.addSlider('cameraSpeed', 0.1, 3.0, 0.1, 'Mouse Sensitivity: How responsive camera is to mouse drag movements.');
    
    this.addSlider('fov', 20, 120, 2, 'Field of View: Camera perspective width - lower values for telescopic view.');
  }
  
  // buildCosmogenesisControls() REMOVED - Legacy timer-based system conflicts with native FSCTF cosmogenesis
  
  buildVisualControls() {
    this.createSection('🎨 Visual Quality', 'Rendering and visual effect controls');
    
    // Fixed max based on texture capacity (1M particles = 1024×1024 texture)
    const maxParticles = 1048576; // FIXED texture capacity
    const maxDisplay = '1.0M';
    this.addSlider('particleCount', 10000, maxParticles, 1000, `Particle Count: MAXIMUM density recommended (${maxDisplay} particles in 1024×1024 texture)`);
    this.addSlider('brightness', 0.0, 4.0, 0.1, 'Overall brightness (DYNAMIC: auto-adjusts for density, manual override available).');
    this.addSlider('exposure', 0.5, 6.0, 0.1, 'HDR exposure (DYNAMIC: auto-adjusts for density, manual override available).');
    this.addSlider('pointSize', 0.5, 8.0, 0.1, 'Particle size (DYNAMIC: auto-adjusts for density, manual override available).');
    this.addSlider('trailFade', 0.9, 0.999, 0.001, 'Trail persistence (higher = longer trails).');
  }
  
  buildAdvancedControls() {
    const advancedDetails = document.createElement('details');
    advancedDetails.style.cssText = 'margin-top: 12px; border: 1px solid #456; border-radius: 4px; padding: 8px;';
    
    const summary = document.createElement('summary');
    summary.textContent = '⚙️ Advanced Controls';
    summary.style.cssText = 'color: #9cf; cursor: pointer; font: 700 11px monospace; margin-bottom: 8px;';
    advancedDetails.appendChild(summary);
    
    this.ui.appendChild(advancedDetails);
    
    // Add advanced controls to details element
    const tempUI = this.ui;
    this.ui = advancedDetails;
    
    this.createSection('🔬 Physics Parameters', 'Low-level physics simulation controls');
    this.addSlider('k_flow', 0.0, 5.0, 0.1, 'Flow field coupling strength.');
    this.addSlider('damping', 0.0, 0.2, 0.001, 'Velocity damping coefficient.');
    this.addSlider('fieldScale', 0.1, 5.0, 0.1, 'Spatial frequency of curl noise field.');
    this.addSlider('timeScale', 0.1, 2.0, 0.1, 'Temporal frequency of field evolution.');
    
    this.ui = tempUI;
  }
  
  buildPerformanceControls() {
    this.createSection('🚀 Performance Monitor', 'Real-time performance tracking and optimization');

    // Adaptive performance toggle wired to global setter
    const adaptiveRow = document.createElement('div');
    adaptiveRow.style.cssText = 'display:flex; align-items:center; gap:8px; margin:6px 0;';
    const adaptiveCheckbox = document.createElement('input');
    adaptiveCheckbox.type = 'checkbox';
    adaptiveCheckbox.id = 'adaptive-performance';
    adaptiveCheckbox.checked = !!window.PERFORMANCE_MONITOR?.adaptiveMode;
    adaptiveCheckbox.addEventListener('change', (e) => {
      if (window.setAdaptiveMode) {
        window.setAdaptiveMode(!!e.target.checked);
      }
    });
    const adaptiveLabel = document.createElement('label');
    adaptiveLabel.htmlFor = 'adaptive-performance';
    adaptiveLabel.textContent = 'Enable adaptive performance';
    adaptiveLabel.style.cssText = 'font: 10px monospace; color:#ccc;';
    adaptiveRow.appendChild(adaptiveCheckbox);
    adaptiveRow.appendChild(adaptiveLabel);
    this.ui.appendChild(adaptiveRow);

    // Reset throttle button wired to global reset
    const resetThrottleBtn = this.createButton('Reset Complexity Throttle', '🔧', 'Reset complexity throttle to maximum');
    resetThrottleBtn.id = 'reset-throttle';
    resetThrottleBtn.onclick = () => {
      if (window.resetPerformanceThrottle) {
        window.resetPerformanceThrottle();
      }
    };

    // Performance display
    const perfDisplay = document.createElement('div');
    perfDisplay.id = 'performance-display';
    perfDisplay.style.cssText = 'margin: 8px 0; padding: 6px; background: rgba(0,40,80,0.3); border-radius: 4px; font: 10px monospace;';
    perfDisplay.innerHTML = '<div id="fps-display">FPS: --</div><div id="throttle-display">Throttle: --</div>';
    this.ui.appendChild(perfDisplay);
  }
  
  // Utility methods for UI construction
  createSection(title, description = '') {
    const section = document.createElement('div');
    section.style.cssText = 'margin-top:12px;font:700 12px monospace;color:#46f;border-top:2px solid #234;padding-top:8px;background:rgba(70,100,255,0.1);padding:8px;border-radius:4px;';
    section.innerHTML = `<span style="color:#8cf;">${title}</span>${description ? `<br><span style="font-size:9px;color:#678;font-weight:400;">${description}</span>` : ''}`;
    this.ui.appendChild(section);
  }
  
  addSlider(paramName, min, max, step, description) {
    const container = document.createElement('div');
    container.className = 'param-control';
    container.style.cssText = 'margin: 6px 0; display: flex; align-items: center; gap: 8px;';
    
    const label = document.createElement('label');
    label.textContent = paramName;
    label.style.cssText = 'min-width: 120px; font: 10px monospace; color: #ccc;';
    label.title = description;
    
    const slider = document.createElement('input');
    slider.type = 'range';
    slider.min = min;
    slider.max = max;
    slider.step = step;
    slider.value = window.params?.[paramName] || min;
    slider.style.cssText = 'flex: 1; height: 20px;';
    
    const valueDisplay = document.createElement('span');
    valueDisplay.textContent = slider.value;
    valueDisplay.style.cssText = 'min-width: 60px; text-align: right; font: 10px monospace; color: #9cf;';
    
    slider.addEventListener('input', (e) => {
      valueDisplay.textContent = e.target.value;
      if (window.params) {
        window.params[paramName] = parseFloat(e.target.value);
      }
      this.userOverrides.add(paramName);
      
      // Mark as user override to prevent automatic changes
      if (window.markAsUserOverride) {
        window.markAsUserOverride(paramName);
      }
      
      // Special handling for dynamic visual parameters
      if (paramName === 'pointSize') {
        window.params._userOverridePointSize = true;
        console.log(`👤 User override: Point Size = ${e.target.value}`);
      } else if (paramName === 'brightness') {
        window.params._userOverrideBrightness = true;
        console.log(`👤 User override: Brightness = ${e.target.value}`);
      } else if (paramName === 'exposure') {
        window.params._userOverrideExposure = true;
        console.log(`👤 User override: Exposure = ${e.target.value}`);
      } else if (paramName === 'densityAlphaReduction') {
        window.params._userOverrideDensityAlpha = true;
        console.log(`👤 User override: Alpha Reduction = ${e.target.value}`);
      } else if (paramName === 'trailFade') {
        window.params._userOverrideTrailFade = true;
        console.log(`👤 User override: Trail Fade = ${e.target.value}`);
      }
    });
    
    // Special handling for particle count slider - live updates
    if (paramName === 'particleCount') {
      const updateParticles = () => {
        if (window.updateParticleDimensions) {
          console.log(`🎛️ Particle slider changed to: ${params[paramName].toLocaleString()}`);
          window.updateParticleDimensions();
        }
      };
      
      // Update on both input (live) and change (final)
      slider.addEventListener('input', updateParticles);
      slider.addEventListener('change', updateParticles);
    }
    
    container.appendChild(label);
    container.appendChild(slider);
    container.appendChild(valueDisplay);
    this.ui.appendChild(container);
    
    this.paramElements[paramName] = { slider, valueDisplay };
  }
  
  addCheckbox(paramName, description) {
    const container = document.createElement('div');
    container.className = 'param-control';
    container.style.cssText = 'margin: 6px 0; display: flex; align-items: center; gap: 8px;';
    
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = window.params?.[paramName] || false;
    checkbox.style.cssText = 'transform: scale(1.2);';
    
    const label = document.createElement('label');
    label.textContent = paramName;
    label.style.cssText = 'font: 10px monospace; color: #ccc; cursor: pointer;';
    label.title = description;
    
    checkbox.addEventListener('change', (e) => {
      if (window.params) {
        window.params[paramName] = e.target.checked;
      }
      this.userOverrides.add(paramName);
      // Mark as user override to prevent automatic changes
      if (window.markAsUserOverride) {
        window.markAsUserOverride(paramName);
      }
    });
    
    label.addEventListener('click', () => checkbox.click());
    
    container.appendChild(checkbox);
    container.appendChild(label);
    this.ui.appendChild(container);
    
    this.paramElements[paramName] = { checkbox };
  }
  
  createButton(text, icon, description) {
    const button = document.createElement('button');
    button.textContent = `${icon} ${text}`;
    button.title = description;
    button.style.cssText = 'margin: 4px 0; padding: 6px 12px; font: 10px monospace; background: linear-gradient(135deg, #234, #456); color: #fc6; border: 1px solid #678; border-radius: 4px; cursor: pointer; width: 100%;';
    
    button.onmouseover = () => button.style.background = 'linear-gradient(135deg, #345, #567)';
    button.onmouseout = () => button.style.background = 'linear-gradient(135deg, #234, #456)';
    
    this.ui.appendChild(button);
    return button;
  }
  
  createResetButton() {
    const resetBtn = this.createButton('Reset Auto-Changes', '🔓', 'Reset user override protection - re-enable automatic parameter changes');
    resetBtn.onclick = () => {
      this.userOverrides.clear();
      if (window.resetUserOverrides) {
        window.resetUserOverrides();
      }
      resetBtn.style.background = 'linear-gradient(135deg, #084, #195)';
      setTimeout(() => resetBtn.style.background = 'linear-gradient(135deg, #234, #456)', 1000);
    };
  }
  
  updatePerformanceDisplay(fps, throttle) {
    const fpsDisplay = document.getElementById('fps-display');
    const throttleDisplay = document.getElementById('throttle-display');
    
    if (fpsDisplay) fpsDisplay.textContent = `FPS: ${fps}`;
    if (throttleDisplay) throttleDisplay.textContent = `Throttle: ${throttle}`;
  }

  /**
   * Add a display-only text section
   */
  addDisplay(title, description) {
    const container = document.createElement('div');
    container.className = 'parameter-group';
    container.style.marginBottom = '15px';

    const titleElement = document.createElement('h4');
    titleElement.textContent = title;
    titleElement.style.color = '#ffd700';
    titleElement.style.marginBottom = '5px';

    const descElement = document.createElement('p');
    descElement.textContent = description;
    descElement.style.fontSize = '12px';
    descElement.style.color = '#ccc';
    descElement.style.lineHeight = '1.4';
    descElement.style.marginBottom = '10px';

    container.appendChild(titleElement);
    container.appendChild(descElement);
    this.ui.appendChild(container);
  }

  /**
   * Add a read-only display that shows derived parameter values
   */
  addReadOnlyDisplay(paramName, description) {
    const container = document.createElement('div');
    container.className = 'parameter-group';
    container.style.marginBottom = '10px';
    container.style.paddingLeft = '20px';

    const label = document.createElement('label');
    label.textContent = paramName.replace(/([A-Z])/g, ' $1').trim();
    label.style.display = 'block';
    label.style.fontSize = '13px';
    label.style.color = '#aaa';
    label.style.marginBottom = '3px';

    const valueDisplay = document.createElement('div');
    valueDisplay.id = `derived-${paramName}`;
    valueDisplay.textContent = 'Calculating...';
    valueDisplay.style.fontSize = '14px';
    valueDisplay.style.color = '#0ff';
    valueDisplay.style.fontFamily = 'monospace';
    valueDisplay.style.backgroundColor = 'rgba(0, 255, 255, 0.1)';
    valueDisplay.style.padding = '5px';
    valueDisplay.style.borderRadius = '3px';
    valueDisplay.style.marginBottom = '5px';

    const helpText = document.createElement('div');
    helpText.textContent = description;
    helpText.style.fontSize = '11px';
    helpText.style.color = '#888';
    helpText.style.lineHeight = '1.3';

    container.appendChild(label);
    container.appendChild(valueDisplay);
    container.appendChild(helpText);
    this.ui.appendChild(container);
  }

  /**
   * Update derived parameter displays with current values (improved formatting)
   */
  updateDerivedParameters(derivedParams) {
    if (!derivedParams) return;

    const graceDisplay = document.getElementById('derived-graceComplexity');
    const recursionDisplay = document.getElementById('derived-morphicRecursionDepth');
    const consciousnessDisplay = document.getElementById('derived-consciousnessComplexity');

    if (graceDisplay) {
      graceDisplay.textContent = `${derivedParams.graceComplexity.toFixed(3)} [φ-mathematics]`;
      graceDisplay.style.color = '#00ff88'; // Green for active derivation
    }
    if (recursionDisplay) {
      recursionDisplay.textContent = `${derivedParams.morphicRecursionDepth} levels [auto-derived]`;
      recursionDisplay.style.color = '#00ff88';
    }
    if (consciousnessDisplay) {
      consciousnessDisplay.textContent = `${derivedParams.consciousnessComplexity.toFixed(3)} [prime-resonance]`;
      consciousnessDisplay.style.color = '#00ff88';
    }
  }
  
  /**
   * Update derived parameter displays with fallback indicator
   */
  updateDerivedParametersFallback(fallbackParams) {
    if (!fallbackParams) return;

    const graceDisplay = document.getElementById('derived-graceComplexity');
    const recursionDisplay = document.getElementById('derived-morphicRecursionDepth');
    const consciousnessDisplay = document.getElementById('derived-consciousnessComplexity');

    if (graceDisplay) {
      graceDisplay.textContent = `${fallbackParams.graceComplexity.toFixed(3)} [fallback mode]`;
      graceDisplay.style.color = '#ffaa00'; // Orange for fallback
    }
    if (recursionDisplay) {
      recursionDisplay.textContent = `${fallbackParams.morphicRecursionDepth} levels [manual]`;
      recursionDisplay.style.color = '#ffaa00';
    }
    if (consciousnessDisplay) {
      consciousnessDisplay.textContent = `${fallbackParams.consciousnessComplexity.toFixed(3)} [manual]`;
      consciousnessDisplay.style.color = '#ffaa00';
    }
  }
}
