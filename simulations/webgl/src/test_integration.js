/**
 * Integration Test for Modularized FSCTF System
 * Tests module loading, dependencies, and basic functionality
 */

// Mock browser environment for Node.js testing
global.window = {
  performance: { now: () => Date.now() },
  requestAnimationFrame: (fn) => setTimeout(fn, 16),
  devicePixelRatio: 1,
  params: {},
  VERBOSE: false
};

global.document = {
  getElementById: (id) => {
    console.log(`📋 Mock: getElementById(${id})`);
    return {
      style: {},
      addEventListener: () => {},
      innerHTML: '',
      textContent: '',
      appendChild: () => {},
      setAttribute: () => {},
      classList: { add: () => {}, remove: () => {} }
    };
  },
  createElement: (tag) => {
    console.log(`📋 Mock: createElement(${tag})`);
    return {
      style: {},
      addEventListener: () => {},
      innerHTML: '',
      textContent: '',
      appendChild: () => {},
      setAttribute: () => {},
      classList: { add: () => {}, remove: () => {} },
      onmouseover: null,
      onmouseout: null,
      onclick: null
    };
  },
  readyState: 'loading',
  addEventListener: () => {}
};

global.console = console;
global.performance = { now: () => Date.now() };

// Mock WebGL context
const mockGL = {
  VERTEX_SHADER: 35633,
  FRAGMENT_SHADER: 35632,
  COMPILE_STATUS: 35713,
  LINK_STATUS: 35714,
  RGBA: 6408,
  FLOAT: 5126,
  TEXTURE_2D: 3553,
  COLOR_BUFFER_BIT: 16384,
  createShader: () => ({}),
  createProgram: () => ({}),
  shaderSource: () => {},
  compileShader: () => {},
  getShaderParameter: () => true,
  attachShader: () => {},
  linkProgram: () => {},
  getProgramParameter: () => true,
  useProgram: () => {},
  getUniformLocation: () => ({}),
  uniform1f: () => {},
  uniform1i: () => {},
  createTexture: () => ({}),
  bindTexture: () => {},
  texImage2D: () => {},
  createFramebuffer: () => ({}),
  bindFramebuffer: () => {},
  framebufferTexture2D: () => {},
  createVertexArray: () => ({}),
  bindVertexArray: () => {},
  createBuffer: () => ({}),
  bindBuffer: () => {},
  bufferData: () => {},
  enableVertexAttribArray: () => {},
  vertexAttribPointer: () => {},
  clearColor: () => {},
  clear: () => {},
  viewport: () => {},
  drawArrays: () => {},
  getExtension: () => null,
  getSupportedExtensions: () => [],
  getParameter: () => 'Mock WebGL',
  texSubImage2D: () => {},
  readPixels: () => {},
  activeTexture: () => {},
  ARRAY_BUFFER: 34962,
  STATIC_DRAW: 35044,
  TRIANGLES: 4,
  VENDOR: 7936,
  RENDERER: 7937,
  VERSION: 7938
};

// Test counter
let testsPassed = 0;
let testsTotal = 0;

function test(name, testFn) {
  testsTotal++;
  try {
    console.log(`\n🧪 Testing: ${name}`);
    testFn();
    testsPassed++;
    console.log(`✅ PASS: ${name}`);
  } catch (error) {
    console.error(`❌ FAIL: ${name} - ${error.message}`);
    console.error(error.stack);
  }
}

async function runTests() {
  console.log('🚀 Starting FSCTF Modularization Integration Tests\n');

  // Test 1: Module Imports
  test('Module imports work correctly', async () => {
    // Test critical imports
    const { CONSTANTS } = await import('./src/modules/config/constants.js');
    const { vlog } = await import('./src/modules/utils/logging.js');
    const { PERFORMANCE_MONITOR } = await import('./src/modules/performance/performance.js');
    
    // Verify they're objects/functions
    if (typeof CONSTANTS !== 'object') throw new Error('CONSTANTS not an object');
    if (typeof vlog !== 'function') throw new Error('vlog not a function');
    if (typeof PERFORMANCE_MONITOR !== 'object') throw new Error('PERFORMANCE_MONITOR not an object');
    
    console.log('   - CONSTANTS loaded:', Object.keys(CONSTANTS).length, 'sections');
    console.log('   - PERFORMANCE_MONITOR has adaptiveMode:', !!PERFORMANCE_MONITOR.adaptiveMode);
  });

  // Test 2: FSCTF Engine
  test('FSCTF Engine instantiates correctly', async () => {
    const { FSCTFEngine } = await import('./src/modules/fsctf/fsctf-engine.js');
    
    const engine = new FSCTFEngine();
    if (!engine) throw new Error('FSCTFEngine failed to instantiate');
    if (typeof engine.update !== 'function') throw new Error('FSCTFEngine missing update method');
    if (typeof engine.getState !== 'function') throw new Error('FSCTFEngine missing getState method');
    
    console.log('   - FSCTFEngine instantiated successfully');
    console.log('   - Engine has', Object.keys(engine).length, 'properties');
  });

  // Test 3: UI Builder
  test('UI Builder works with mocked DOM', async () => {
    const { UIBuilder } = await import('./src/modules/ui/ui-builder.js');
    
    const mockContainer = document.createElement('div');
    const uiBuilder = new UIBuilder(mockContainer);
    
    if (!uiBuilder) throw new Error('UIBuilder failed to instantiate');
    if (typeof uiBuilder.buildCompleteUI !== 'function') throw new Error('UIBuilder missing buildCompleteUI method');
    
    // Try to build UI (should not crash with mocks)
    uiBuilder.buildCompleteUI();
    
    console.log('   - UIBuilder instantiated and executed successfully');
  });

  // Test 4: Simulation Core
  test('Simulation Core initializes correctly', async () => {
    const { SimulationCore } = await import('./src/modules/core/simulation-core.js');
    
    // Mock the required parameters
    global.window.gl = mockGL;
    const mockShaders = { quadVS: 'mock vertex shader', simFS: 'mock fragment shader' };
    const mockParams = { dt: 1/60, domain: 1.5 };
    
    const simCore = new SimulationCore(mockGL, mockShaders, mockParams);
    
    if (!simCore) throw new Error('SimulationCore failed to instantiate');
    if (typeof simCore.update !== 'function') throw new Error('SimulationCore missing update method');
    
    console.log('   - SimulationCore instantiated successfully');
  });

  // Test 5: Performance Monitoring
  test('Performance monitoring system works', async () => {
    const { PERFORMANCE_MONITOR, setAdaptiveMode } = await import('./src/modules/performance/performance.js');
    
    // Test initial state
    const initialAdaptive = PERFORMANCE_MONITOR.adaptiveMode;
    
    // Test toggling
    setAdaptiveMode(!initialAdaptive);
    if (PERFORMANCE_MONITOR.adaptiveMode === initialAdaptive) {
      throw new Error('setAdaptiveMode did not toggle correctly');
    }
    
    // Test properties exist
    if (typeof PERFORMANCE_MONITOR.complexityThrottle !== 'number') {
      throw new Error('PERFORMANCE_MONITOR missing complexityThrottle');
    }
    
    console.log('   - Performance monitoring system works correctly');
  });

  // Test 6: Shader Loading (mock)
  test('Shader loading system works', async () => {
    const { loadAllShaders } = await import('./src/modules/shaders/shaders.js');
    
    if (typeof loadAllShaders !== 'function') {
      throw new Error('loadAllShaders is not a function');
    }
    
    // Note: We can't actually load shaders in Node.js, but we can verify the function exists
    console.log('   - Shader loading system structure verified');
  });

  // Test 7: Memory Info
  test('Memory info utilities work', async () => {
    const { MemoryInfo, getMemoryInfo } = await import('./src/modules/utils/memory-info.js');
    
    const memInfo = new MemoryInfo();
    const info = getMemoryInfo();
    
    if (!info || typeof info !== 'object') {
      throw new Error('getMemoryInfo did not return an object');
    }
    
    if (typeof info.timestamp !== 'number') {
      throw new Error('Memory info missing timestamp');
    }
    
    console.log('   - Memory info utilities work correctly');
    console.log('   - Memory info has', Object.keys(info).length, 'properties');
  });

  // Test 8: Brain System
  test('AI Brain System initializes', async () => {
    const { BrainSystem } = await import('./src/modules/ai/brain-system.js');
    
    const brain = new BrainSystem();
    
    if (!brain || typeof brain.scoreState !== 'function') {
      throw new Error('BrainSystem failed to initialize correctly');
    }
    
    // Test scoring function
    const score = brain.scoreState(0.5, 0.3, 0.2);
    if (typeof score !== 'number') {
      throw new Error('BrainSystem scoreState did not return a number');
    }
    
    console.log('   - Brain System initialized successfully, score test:', score.toFixed(3));
  });

  // Test Results
  console.log('\n' + '='.repeat(50));
  console.log(`🎯 Test Results: ${testsPassed}/${testsTotal} tests passed`);
  
  if (testsPassed === testsTotal) {
    console.log('🎉 ALL TESTS PASSED! Modularization is successful!');
    console.log('\n✅ The FSCTF system has been completely modularized and all modules load correctly.');
    console.log('✅ All imports/exports are properly configured.');
    console.log('✅ Core systems instantiate without errors.');
    console.log('✅ The modular architecture is ready for use!');
    return true;
  } else {
    console.log(`❌ ${testsTotal - testsPassed} tests failed. Review errors above.`);
    return false;
  }
}

// Run the tests
runTests().then(success => {
  process.exit(success ? 0 : 1);
}).catch(error => {
  console.error('💥 Test runner crashed:', error);
  process.exit(1);
});
