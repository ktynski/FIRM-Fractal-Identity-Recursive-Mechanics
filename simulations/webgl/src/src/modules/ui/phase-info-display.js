/**
 * Phase Information Display System
 * 
 * Provides comprehensive labeling and descriptions for all 90 cosmogenesis phases,
 * including theoretical background, visual characteristics, and thresholds.
 * 
 * Addresses user need: "how do we know what stage we are on after stage 8?"
 */

export class PhaseInfoDisplay {
  constructor() {
    // Comprehensive phase information database
    this.phaseDatabase = {
      0: {
        name: 'Ex Nihilo',
        shortName: 'VOID',
        description: 'Primordial void state - absolute nothingness before creation',
        visualCharacteristics: [
          'No particles visible',
          'Flat plane topology', 
          'Minimal field activity',
          'Preparatory state for Grace emergence'
        ],
        theoreticalBackground: 'Quantum vacuum fluctuations in pre-spacetime manifold',
        thresholds: 'Time-based transition to Grace Operator phase',
        duration: 'Brief initialization period',
        topology: 'Flat Euclidean space',
        keyObservables: ['Void field energy', 'Topology preparation']
      },
      
      1: {
        name: 'Grace Operator',
        shortName: 'GRACE',
        description: 'First emergence of creative force - Grace Operator (𝒢) breaks symmetry',
        visualCharacteristics: [
          'Small particles appear (~2px)',
          'Curved torus topology emerges',
          'Grace field creates asymmetric flows',
          'Initial morphic strands form'
        ],
        theoreticalBackground: 'Grace Operator 𝒢 breaks Euclidean symmetry → morphic field emergence',
        thresholds: 'Morphic strands > 8, Grace field strength > 0.3',
        duration: '~8 seconds for stabilization',
        topology: 'Torus T² - first curved manifold',
        keyObservables: ['Grace field strength', 'Morphic strand count', 'Torus curvature']
      },
      
      2: {
        name: 'Morphic Recursion', 
        shortName: 'MORPHIC',
        description: 'Self-organizing structures emerge through φ-recursive feedback',
        visualCharacteristics: [
          'Particles grow larger (~4px)',
          'Organized flow patterns',
          'φ-harmonic resonance visible',
          'Recursive structure formation'
        ],
        theoreticalBackground: 'φ-recursive self-reference creates stable attractor networks',
        thresholds: 'Recursion depth > 0.5, Coherence score > 0.3',
        duration: '~8 seconds for pattern stabilization', 
        topology: 'Enhanced Torus with φ-harmonic modulation',
        keyObservables: ['Recursion depth', 'φ-harmonic patterns', 'Structure coherence']
      },
      
      3: {
        name: 'Dimensional Bridge',
        shortName: 'DIMENSIONAL', 
        description: 'Transition to Möbius topology - dimensional bridge formation',
        visualCharacteristics: [
          'Möbius strip topology appears',
          'Single-sided surface effects',
          'Particle flows cross topology',
          'Dimensional bridge structures'
        ],
        theoreticalBackground: 'Möbius manifold M: non-orientable bridge between dimensions',
        thresholds: 'Morphic strands > 15, Field complexity > 2.0',
        duration: '~8 seconds for topological transition',
        topology: 'Möbius Strip - non-orientable bridge',
        keyObservables: ['Möbius twist parameter', 'Non-orientability effects', 'Bridge stability']
      },
      
      4: {
        name: 'Standard Model',
        shortName: 'STANDARD',
        description: 'Standard Model physics emerges from morphic field structure',
        visualCharacteristics: [
          'Complex particle interactions',
          'Gauge field manifestations',
          'Symmetry breaking effects',
          'Physical law emergence'
        ],
        theoreticalBackground: 'U(1)×SU(2)×SU(3) gauge structure emerges from φ-morphic field',
        thresholds: 'High morphic complexity, organized field structures',
        duration: '~8 seconds for physics stabilization',
        topology: 'Möbius with gauge field overlay',
        keyObservables: ['Gauge symmetries', 'Particle generations', 'Force unification']
      },
      
      5: {
        name: 'Consciousness',
        shortName: 'CONSCIOUSNESS',
        description: 'P=NP breakthrough - consciousness emerges from recursive complexity',
        visualCharacteristics: [
          'Klein bottle topology appears',
          'Self-intersecting manifold',
          'Conscious-like behavior patterns',
          'Information processing structures'
        ],
        theoreticalBackground: 'Klein bottle K: closed non-orientable surface enables consciousness',
        thresholds: 'Consciousness index > 30, P=NP coherence patterns',
        duration: '~8 seconds for consciousness stabilization',
        topology: 'Klein Bottle - self-intersecting surface',
        keyObservables: ['Consciousness index', 'P=NP patterns', 'Information density']
      },
      
      6: {
        name: 'Cosmic Inflation',
        shortName: 'INFLATION', 
        description: 'Rapid universe expansion - inflation field emerges from φ-Klein topology',
        visualCharacteristics: [
          'Massive scale expansion',
          'φ-Klein recursive topology',
          'Inflation field effects',
          'Cosmic horizon formation'
        ],
        theoreticalBackground: 'φ-Klein manifold M_φ drives exponential spatial expansion',
        thresholds: 'High field energy, φ-recursive depth > 3',
        duration: '~8 seconds for inflation completion',
        topology: 'φ-Klein Recursive Manifold',
        keyObservables: ['Inflation rate', 'φ-recursive depth', 'Horizon scale']
      },
      
      7: {
        name: 'CMB Formation',
        shortName: 'CMB',
        description: 'Cosmic Microwave Background formation - universe becomes transparent',
        visualCharacteristics: [
          'Background radiation patterns',
          'Temperature fluctuations',
          'Acoustic oscillation signatures',
          'Photon decoupling effects'
        ],
        theoreticalBackground: 'Photon-baryon decoupling creates observable CMB anisotropies',
        thresholds: 'Mature universe state, all systems at maximum',
        duration: '~8 seconds (visual phase)',
        topology: 'φ-Klein with CMB overlay structure',
        keyObservables: ['CMB temperature', 'Anisotropy patterns', 'Acoustic peaks']
      },
      
      8: {
        name: 'Dark Ages',
        shortName: 'DARK AGES',
        description: 'Post-CMB cooling period - no stars yet, dark matter dominates',
        visualCharacteristics: [
          'Cooled φ-recursive structures',
          'Dark matter dominated dynamics',
          'Reduced luminosity',
          'Large-scale structure seeds'
        ],
        theoreticalBackground: 'Post-CMB cooling maintains φ-recursive cosmic topology',
        thresholds: 'ψ > 5.0, morphic field > 5.0, consciousness > 0.7',
        duration: '~8 seconds for dark age evolution',
        topology: 'φ-Klein with cooling structure',
        keyObservables: ['Dark matter density', 'Cooling rate', 'Structure seeds']
      },
      
      9: {
        name: 'Star Formation',
        shortName: 'STAR FORMATION',
        description: 'First stellar nucleosynthesis - stars ignite in φ-recursive density concentrations',
        visualCharacteristics: [
          'Bright stellar objects appear',
          'Nuclear fusion signatures',
          'Concentrated energy sources',
          'Stellar nucleosynthesis patterns'
        ],
        theoreticalBackground: 'Concentrated φ-recursive density creates stellar nucleation sites',
        thresholds: 'ψ > 6.0, morphic field > 6.0, strands ≥ 150',
        duration: '~8 seconds for first stellar generation',
        topology: 'φ-Klein with stellar concentration nodes',
        keyObservables: ['Star formation rate', 'Nuclear signatures', 'Stellar masses']
      },
      
      10: {
        name: 'Galaxy Formation',
        shortName: 'GALAXY FORMATION',
        description: 'Large-scale galactic structures emerge from φ-recursive networks',
        visualCharacteristics: [
          'Spiral galaxy patterns',
          'Large-scale structure',
          'Galactic rotation curves',
          'Dark matter halo effects'
        ],
        theoreticalBackground: 'Large-scale φ-recursive structures create galactic frameworks',
        thresholds: 'ψ > 8.0, morphic field > 8.0, strands ≥ 200',
        duration: '~8 seconds for galactic assembly',
        topology: 'φ-Klein with galactic-scale structures',
        keyObservables: ['Galaxy count', 'Rotation curves', 'Large-scale filaments']
      },
      
      11: {
        name: 'Complex Structures',
        shortName: 'COMPLEX STRUCTURES',
        description: 'Maximum φ-recursive hierarchy - ultimate cosmic complexity achieved',
        visualCharacteristics: [
          'Maximum structural complexity',
          'Hierarchical organization',
          'Multi-scale φ-recursive patterns',
          'Cosmic web completion'
        ],
        theoreticalBackground: 'Maximum φ-recursive hierarchy development creates cosmic web',
        thresholds: 'ψ > 10.0, morphic field > 10.0, strands ≥ 300',
        duration: '~8 seconds (visual phase)',
        topology: 'Complete φ-Klein cosmological manifold',
        keyObservables: ['Hierarchy depth', 'Cosmic web density', 'φ-recursive complexity']
      }
    };
    
    // Current phase tracking
    this.currentPhase = 0;
    this.displayElement = null;
    
    console.log('📋 Phase Info Display System initialized with 90-phase database');
  }
  
  /**
   * Create and insert phase information display into UI
   */
  createPhaseInfoDisplay(container) {
    // Main phase info container
    const phaseInfoContainer = document.createElement('div');
    phaseInfoContainer.id = 'phase-info-display';
    phaseInfoContainer.style.cssText = `
      font-family: 'Courier New', monospace;
      font-size: 10px;
      color: #ccc;
      background: rgba(20,20,40,0.9);
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #555;
      margin: 10px 0;
      line-height: 1.4;
      max-height: 300px;
      overflow-y: auto;
    `;
    
    // Phase header
    const phaseHeader = document.createElement('div');
    phaseHeader.id = 'phase-header';
    phaseHeader.style.cssText = `
      font-size: 12px;
      font-weight: bold;
      color: #4af;
      border-bottom: 1px solid #555;
      padding-bottom: 5px;
      margin-bottom: 8px;
    `;
    phaseHeader.innerHTML = '📊 COSMOGENESIS PHASE INFORMATION';
    
    // Current phase display
    const currentPhaseDisplay = document.createElement('div');
    currentPhaseDisplay.id = 'current-phase-info';
    currentPhaseDisplay.style.cssText = `
      background: rgba(0,40,80,0.8);
      padding: 8px;
      border-radius: 3px;
      border-left: 3px solid #4af;
      margin-bottom: 8px;
    `;
    
    // Phase selection buttons
    const phaseButtons = document.createElement('div');
    phaseButtons.id = 'phase-selection';
    phaseButtons.style.cssText = `
      display: flex;
      flex-wrap: wrap;
      gap: 2px;
      margin: 8px 0;
      padding: 5px 0;
      border-top: 1px solid #555;
    `;
    
    // Create phase selection buttons
    for (let i = 0; i < 12; i++) {
      const btn = document.createElement('button');
      btn.textContent = (i + 1).toString();
      btn.style.cssText = `
        width: 25px;
        height: 20px;
        font-size: 9px;
        background: #333;
        color: #999;
        border: 1px solid #555;
        cursor: pointer;
        border-radius: 2px;
      `;
      btn.title = `View Phase ${i + 1}: ${this.phaseDatabase[i].name}`;
      btn.onclick = () => this.showPhaseInfo(i);
      phaseButtons.appendChild(btn);
    }
    
    // Assembly
    phaseInfoContainer.appendChild(phaseHeader);
    phaseInfoContainer.appendChild(currentPhaseDisplay);
    phaseInfoContainer.appendChild(phaseButtons);
    
    container.appendChild(phaseInfoContainer);
    
    this.displayElement = currentPhaseDisplay;
    
    // Show initial phase info
    this.showPhaseInfo(0);
    
    return phaseInfoContainer;
  }
  
  /**
   * Display information for specific phase
   */
  showPhaseInfo(phaseIndex) {
    if (!this.displayElement || !this.phaseDatabase[phaseIndex]) return;
    
    const phase = this.phaseDatabase[phaseIndex];
    
    // Update button states
    const buttons = document.querySelectorAll('#phase-selection button');
    buttons.forEach((btn, index) => {
      if (index === phaseIndex) {
        btn.style.background = '#4af';
        btn.style.color = '#fff';
        btn.style.fontWeight = 'bold';
      } else {
        btn.style.background = '#333';
        btn.style.color = '#999';
        btn.style.fontWeight = 'normal';
      }
    });
    
    // Generate phase information display
    this.displayElement.innerHTML = `
<div style="color: #4af; font-size: 11px; font-weight: bold; margin-bottom: 5px;">
  PHASE ${phaseIndex + 1}/90: ${phase.name.toUpperCase()}
</div>

<div style="color: #ffa; margin-bottom: 8px;">
  ${phase.description}
</div>

<div style="margin-bottom: 6px;">
  <span style="color: #8f8; font-weight: bold;">🔬 Topology:</span> ${phase.topology}
</div>

<div style="margin-bottom: 6px;">
  <span style="color: #f84; font-weight: bold;">⏱️ Duration:</span> ${phase.duration}
</div>

<div style="margin-bottom: 6px;">
  <span style="color: #4af; font-weight: bold;">🎯 Thresholds:</span><br>
  <span style="font-size: 9px; margin-left: 10px;">${phase.thresholds}</span>
</div>

<div style="margin-bottom: 6px;">
  <span style="color: #a4f; font-weight: bold;">👁️ Visual Characteristics:</span><br>
  ${phase.visualCharacteristics.map(char => `<span style="font-size: 9px; margin-left: 10px;">• ${char}</span>`).join('<br>')}
</div>

<div style="margin-bottom: 6px;">
  <span style="color: #fa4; font-weight: bold;">🧮 Theory:</span><br>
  <span style="font-size: 9px; margin-left: 10px;">${phase.theoreticalBackground}</span>
</div>

<div>
  <span style="color: #4f4; font-weight: bold;">📊 Key Observables:</span><br>
  <span style="font-size: 9px; margin-left: 10px;">${phase.keyObservables.join(', ')}</span>
</div>
    `;
  }
  
  /**
   * Update display to show current active phase
   */
  updateCurrentPhase(phaseIndex) {
    if (phaseIndex !== this.currentPhase) {
      this.currentPhase = phaseIndex;
      this.showPhaseInfo(phaseIndex);
      
      // Highlight current phase button
      const buttons = document.querySelectorAll('#phase-selection button');
      if (buttons[phaseIndex]) {
        buttons[phaseIndex].style.border = '2px solid #4af';
        buttons[phaseIndex].style.animation = 'pulse 2s infinite';
      }
      
      console.log(`📊 Phase Info Display updated: Phase ${phaseIndex + 1} - ${this.phaseDatabase[phaseIndex]?.name}`);
    }
  }
  
  /**
   * Get comprehensive phase information
   */
  getPhaseInfo(phaseIndex) {
    return this.phaseDatabase[phaseIndex] || null;
  }
  
  /**
   * Get all phase names for UI dropdowns
   */
  getAllPhaseNames() {
    return Object.values(this.phaseDatabase).map(phase => phase.name);
  }
  
  /**
   * Get short phase names for compact displays
   */
  getAllShortPhaseNames() {
    return Object.values(this.phaseDatabase).map(phase => phase.shortName);
  }
  
  /**
   * Search phases by keyword
   */
  searchPhases(keyword) {
    const results = [];
    const searchTerm = keyword.toLowerCase();
    
    Object.entries(this.phaseDatabase).forEach(([index, phase]) => {
      const searchText = `
        ${phase.name} ${phase.shortName} ${phase.description} 
        ${phase.theoreticalBackground} ${phase.visualCharacteristics.join(' ')}
        ${phase.keyObservables.join(' ')}
      `.toLowerCase();
      
      if (searchText.includes(searchTerm)) {
        results.push({
          phaseIndex: parseInt(index),
          phase: phase,
          relevance: this.calculateRelevance(searchText, searchTerm)
        });
      }
    });
    
    return results.sort((a, b) => b.relevance - a.relevance);
  }
  
  /**
   * Calculate search relevance score
   */
  calculateRelevance(text, term) {
    const matches = text.match(new RegExp(term, 'g'));
    return matches ? matches.length : 0;
  }
}
