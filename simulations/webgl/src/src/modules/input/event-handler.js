/**
 * Event Handler System
 * Manages canvas and WebGL context events
 */

export class EventHandler {
  constructor(canvas, gl) {
    this.canvas = canvas;
    this.gl = gl;
    this.contextLost = false;
    this.pointerState = {
      isDown: false,
      lastX: 0,
      lastY: 0,
      dragSensitivity: 0.01
    };
    
    this.setupEventListeners();
    console.log('🎮 Event Handler System initialized');
  }
  
  /**
   * Setup all event listeners
   */
  setupEventListeners() {
    // WebGL context events
    this.setupContextEvents();
    
    // Pointer/mouse events
    this.setupPointerEvents();
    
    // Keyboard events
    this.setupKeyboardEvents();
    
    // Window events
    this.setupWindowEvents();
  }
  
  /**
   * Setup WebGL context event handlers
   */
  setupContextEvents() {
    // Context lost event
    this.canvas.addEventListener('webglcontextlost', (event) => {
      event.preventDefault();
      this.contextLost = true;
      console.error('❌ WebGL context lost! Pausing simulation...');
      
      // Update UI to show context lost state
      this.showContextLostMessage();
    });
    
    // Context restored event
    this.canvas.addEventListener('webglcontextrestored', () => {
      this.contextLost = false;
      console.log('✅ WebGL context restored! Reinitializing...');
      
      // Trigger reinitialization
      if (window.reinitializeWebGL) {
        window.reinitializeWebGL();
      }
      
      this.hideContextLostMessage();
    });
  }
  
  /**
   * Setup pointer/mouse event handlers
   */
  setupPointerEvents() {
    // Pointer down
    this.canvas.addEventListener('pointerdown', (event) => {
      this.pointerState.isDown = true;
      this.pointerState.lastX = event.clientX;
      this.pointerState.lastY = event.clientY;
      
      // Prevent default to avoid text selection
      event.preventDefault();
    });
    
    // Pointer move (camera rotation)
    this.canvas.addEventListener('pointermove', (event) => {
      if (!this.pointerState.isDown) return;
      if (!window.params) return;
      
      const deltaX = event.clientX - this.pointerState.lastX;
      const deltaY = event.clientY - this.pointerState.lastY;
      
      // Update camera rotation
      window.params.cameraRotY += deltaX * this.pointerState.dragSensitivity;
      window.params.cameraRotX += deltaY * this.pointerState.dragSensitivity;
      
      // Clamp vertical rotation to avoid flipping
      window.params.cameraRotX = Math.max(-Math.PI/2, Math.min(Math.PI/2, window.params.cameraRotX));
      
      this.pointerState.lastX = event.clientX;
      this.pointerState.lastY = event.clientY;
      
      event.preventDefault();
    });
    
    // Pointer up
    this.canvas.addEventListener('pointerup', (event) => {
      this.pointerState.isDown = false;
      event.preventDefault();
    });
    
    // Wheel event for zooming
    this.canvas.addEventListener('wheel', (event) => {
      if (!window.params) return;
      
      const zoomSpeed = 0.1;
      const zoomDelta = event.deltaY > 0 ? zoomSpeed : -zoomSpeed;
      
      window.params.cameraZ = Math.max(1.0, Math.min(50.0, window.params.cameraZ + zoomDelta));
      
      event.preventDefault();
    });
    
    // Double click to reset camera
    this.canvas.addEventListener('dblclick', (event) => {
      this.resetCamera();
      event.preventDefault();
    });
  }
  
  /**
   * Setup keyboard event handlers
   */
  setupKeyboardEvents() {
    document.addEventListener('keydown', (event) => {
      this.handleKeyDown(event);
    });
    
    document.addEventListener('keyup', (event) => {
      this.handleKeyUp(event);
    });
  }
  
  /**
   * Setup window event handlers
   */
  setupWindowEvents() {
    // Window resize
    window.addEventListener('resize', () => {
      this.handleResize();
    });
    
    // Visibility change (pause when tab is hidden)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        console.log('⏸️ Tab hidden - pausing simulation');
        if (window.pauseSimulation) {
          window.pauseSimulation();
        }
      } else {
        console.log('▶️ Tab visible - resuming simulation');
        if (window.resumeSimulation) {
          window.resumeSimulation();
        }
      }
    });
  }
  
  /**
   * Handle key down events
   */
  handleKeyDown(event) {
    if (!window.params) return;
    
    switch(event.code) {
      case 'Space':
        // Toggle pause
        if (window.togglePause) {
          window.togglePause();
        }
        event.preventDefault();
        break;
        
      case 'KeyR':
        // Reset camera
        if (event.ctrlKey || event.metaKey) {
          this.resetCamera();
          event.preventDefault();
        }
        break;
        
      case 'KeyF':
        // Toggle fullscreen
        if (event.ctrlKey || event.metaKey) {
          this.toggleFullscreen();
          event.preventDefault();
        }
        break;
        
      case 'KeyV':
        // Toggle verbose logging
        if (event.ctrlKey || event.metaKey) {
          if (window.setVerbose) {
            const newVerbose = !window.VERBOSE;
            window.setVerbose(newVerbose);
            console.log(`🔧 Verbose logging ${newVerbose ? 'enabled' : 'disabled'}`);
          }
          event.preventDefault();
        }
        break;
        
      case 'Escape':
        // Exit fullscreen or close menus
        if (document.fullscreenElement) {
          document.exitFullscreen();
        }
        break;
    }
  }
  
  /**
   * Handle key up events
   */
  handleKeyUp(event) {
    // Currently no key up handling needed
  }
  
  /**
   * Handle window resize
   */
  handleResize() {
    // Debounce resize events
    clearTimeout(this.resizeTimeout);
    this.resizeTimeout = setTimeout(() => {
      if (window.resizeCanvasToDisplaySize) {
        window.resizeCanvasToDisplaySize();
      }
      console.log('🔄 Canvas resized to display size');
    }, 100);
  }
  
  /**
   * Reset camera to default position
   */
  resetCamera() {
    if (!window.params) return;
    
    window.params.cameraX = 0.0;
    window.params.cameraY = 0.0;
    window.params.cameraZ = 8.0;
    window.params.cameraRotX = 0.6;
    window.params.cameraRotY = 0.3;
    window.params.fov = 45.0;
    
    console.log('📸 Camera reset to default position');
  }
  
  /**
   * Toggle fullscreen mode
   */
  toggleFullscreen() {
    if (!document.fullscreenElement) {
      this.canvas.requestFullscreen().catch(err => {
        console.error('❌ Failed to enter fullscreen:', err);
      });
    } else {
      document.exitFullscreen();
    }
  }
  
  /**
   * Show context lost message
   */
  showContextLostMessage() {
    let messageEl = document.getElementById('context-lost-message');
    if (!messageEl) {
      messageEl = document.createElement('div');
      messageEl.id = 'context-lost-message';
      messageEl.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 0, 0, 0.9);
        color: white;
        padding: 20px;
        border-radius: 8px;
        font-family: monospace;
        font-size: 16px;
        text-align: center;
        z-index: 10000;
      `;
      messageEl.innerHTML = `
        <h3>⚠️ WebGL Context Lost</h3>
        <p>The graphics context has been lost. This usually happens when:</p>
        <ul style="text-align: left;">
          <li>GPU driver crashed</li>
          <li>System is under high GPU load</li>
          <li>Browser tab was inactive for too long</li>
        </ul>
        <p>The simulation will resume automatically when the context is restored.</p>
      `;
      document.body.appendChild(messageEl);
    }
  }
  
  /**
   * Hide context lost message
   */
  hideContextLostMessage() {
    const messageEl = document.getElementById('context-lost-message');
    if (messageEl) {
      messageEl.remove();
    }
  }
  
  /**
   * Get current pointer state
   */
  getPointerState() {
    return { ...this.pointerState };
  }
  
  /**
   * Check if WebGL context is lost
   */
  isContextLost() {
    return this.contextLost;
  }
  
  /**
   * Cleanup event listeners
   */
  cleanup() {
    // Remove all event listeners
    // This would need to be implemented if we need to destroy the event handler
    console.log('🧹 Event handler cleanup');
  }
}

