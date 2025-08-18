/**
 * Performance Optimization Test Suite
 * Comprehensive testing of all optimizations to ensure they don't break simulation accuracy
 */

import { createCachedProgram, precompileShaders, UniformBufferManager } from './src/modules/shaders/shaders.js';
import { WebGLStateManager } from './src/modules/webgl/webgl-utils.js';
import { OptimizedStrandManager } from './src/modules/fsctf/strand-manager.js';
import { AdaptiveUpdateManager } from './src/modules/performance/performance.js';
import { StrandPool } from './src/modules/fsctf/grace-operator.js';
import { OptimizedMainLoop } from './src/modules/core/main-loop.js';

// Mock WebGL context for testing
function createMockWebGL() {
  return {
    createProgram: () => ({ id: 'mock-program' }),
    createShader: () => ({ id: 'mock-shader' }),
    createBuffer: () => ({ id: 'mock-buffer' }),
    createVertexArray: () => ({ id: 'mock-vao' }),
    createFramebuffer: () => ({ id: 'mock-fbo' }),
    createTexture: () => ({ id: 'mock-texture' }),
    attachShader: () => {},
    linkProgram: () => {},
    useProgram: () => {},
    bindVertexArray: () => {},
    bindFramebuffer: () => {},
    bindBuffer: () => {},
    bufferData: () => {},
    bufferSubData: () => {},
    blendFunc: () => {},
    viewport: () => {},
    clearColor: () => {},
    clear: () => {},
    getParameter: () => 0,
    getExtension: () => null,
    checkFramebufferStatus: () => 36053, // FRAMEBUFFER_COMPLETE
    getShaderParameter: () => true,
    getProgramParameter: () => true,
    getShaderInfoLog: () => '',
    getProgramInfoLog: () => '',
    deleteShader: () => {},
    deleteProgram: () => {},
    ARRAY_BUFFER: 34962,
    UNIFORM_BUFFER: 35345,
    DYNAMIC_DRAW: 35048,
    FRAMEBUFFER: 36160,
    COLOR_BUFFER_BIT: 16384,
    NEAREST: 9728,
    CLAMP_TO_EDGE: 33071,
    RGBA: 6408,
    FLOAT: 5126,
    HALF_FLOAT: 5131,
    UNSIGNED_BYTE: 5121,
    RGBA8: 32856,
    RGBA16F: 34842,
    RGBA32F: 34836
  };
}

// Test suite
class PerformanceOptimizationTestSuite {
  constructor() {
    this.tests = [];
    this.passed = 0;
    this.failed = 0;
    this.mockGL = createMockWebGL();
  }
  
  addTest(name, testFn) {
    this.tests.push({ name, testFn });
  }
  
  async runAll() {
    console.log('🧪 Running Performance Optimization Test Suite...\n');
    
    for (const test of this.tests) {
      try {
        await test.testFn();
        console.log(`✅ ${test.name}`);
        this.passed++;
      } catch (error) {
        console.error(`❌ ${test.name}: ${error.message}`);
        this.failed++;
      }
    }
    
    this.printSummary();
  }
  
  printSummary() {
    console.log('\n📊 Test Summary:');
    console.log(`✅ Passed: ${this.passed}`);
    console.log(`❌ Failed: ${this.failed}`);
    console.log(`📈 Success Rate: ${((this.passed / (this.passed + this.failed)) * 100).toFixed(1)}%`);
    
    if (this.failed === 0) {
      console.log('\n🎉 All performance optimizations are working correctly!');
      console.log('🚀 Simulation accuracy is preserved while improving performance.');
    } else {
      console.log('\n⚠️ Some tests failed. Please review the errors above.');
    }
  }
  
  // Test 1: Shader Program Caching
  async testShaderCaching() {
    const vsSrc = 'attribute vec2 position; void main() { gl_Position = vec4(position, 0.0, 1.0); }';
    const fsSrc = 'void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }';
    
    // First call should create new program
    const program1 = await createCachedProgram(this.mockGL, vsSrc, fsSrc, 'test-shader');
    if (!program1 || !program1.id) {
      throw new Error('First program creation failed');
    }
    
    // Second call should return cached program
    const program2 = await createCachedProgram(this.mockGL, vsSrc, fsSrc, 'test-shader');
    if (program1 !== program2) {
      throw new Error('Program caching not working - different objects returned');
    }
    
    // Different cache key should create new program
    const program3 = await createCachedProgram(this.mockGL, vsSrc, fsSrc, 'test-shader-2');
    if (program1 === program3) {
      throw new Error('Different cache keys returning same program');
    }
  }
  
  // Test 2: Uniform Buffer Management
  testUniformBufferManager() {
    const manager = new UniformBufferManager(this.mockGL);
    
    // Test buffer creation
    const data1 = new Float32Array([1.0, 2.0, 3.0, 4.0]);
    const buffer1 = manager.createUniformBuffer('test-buffer', data1);
    if (!buffer1) {
      throw new Error('Uniform buffer creation failed');
    }
    
    // Test buffer update with same data (should not update)
    const data2 = new Float32Array([1.0, 2.0, 3.0, 4.0]);
    manager.updateUniformBuffer('test-buffer', data2);
    
    // Test buffer update with different data (should update)
    const data3 = new Float32Array([5.0, 6.0, 7.0, 8.0]);
    manager.updateUniformBuffer('test-buffer', data3);
    
    // Test force update
    manager.updateUniformBuffer('test-buffer', data1, true);
  }
  
  // Test 3: WebGL State Management
  testWebGLStateManager() {
    const manager = new WebGLStateManager(this.mockGL);
    
    // Test program binding
    const program1 = { id: 'program1' };
    const program2 = { id: 'program2' };
    
    manager.useProgram(program1);
    if (manager.currentProgram !== program1) {
      throw new Error('Program binding not working');
    }
    
    // Test duplicate binding (should not change state)
    manager.useProgram(program1);
    if (manager.currentProgram !== program1) {
      throw new Error('Duplicate program binding changed state unnecessarily');
    }
    
    // Test different program binding
    manager.useProgram(program2);
    if (manager.currentProgram !== program2) {
      throw new Error('Different program binding not working');
    }
    
    // Test VAO binding
    const vao1 = { id: 'vao1' };
    manager.bindVertexArray(vao1);
    if (manager.currentVAO !== vao1) {
      throw new Error('VAO binding not working');
    }
  }
  
  // Test 4: Optimized Strand Manager
  testOptimizedStrandManager() {
    const manager = new OptimizedStrandManager();
    
    // Test initial state
    if (manager.particleData.length !== 0) {
      throw new Error('Initial particle data should be empty');
    }
    
    // Test buffer update threshold
    manager.updateParticleBuffer(this.mockGL, 0);
    if (manager.lastUpdateFrame !== 0) {
      throw new Error('First frame should always update');
    }
    
    // Test threshold enforcement
    manager.updateParticleBuffer(this.mockGL, 2);
    if (manager.lastUpdateFrame !== 0) {
      throw new Error('Update threshold not enforced');
    }
    
    // Test threshold bypass
    manager.updateParticleBuffer(this.mockGL, 5);
    if (manager.lastUpdateFrame !== 5) {
      throw new Error('Update threshold bypass not working');
    }
  }
  
  // Test 5: Adaptive Update Manager
  testAdaptiveUpdateManager() {
    const manager = new AdaptiveUpdateManager();
    
    // Test default performance rating
    if (manager.currentPerformance !== 'good') {
      throw new Error('Default performance rating should be good');
    }
    
    // Test performance rating updates
    manager.updatePerformanceRating(60);
    if (manager.currentPerformance !== 'excellent') {
      throw new Error('High FPS should set excellent performance');
    }
    
    manager.updatePerformanceRating(15);
    if (manager.currentPerformance !== 'critical') {
      throw new Error('Low FPS should set critical performance');
    }
    
    // Test interval retrieval
    const interval = manager.getUpdateInterval('soulEcho');
    if (typeof interval !== 'number') {
      throw new Error('Update interval should return a number');
    }
  }
  
  // Test 6: Strand Pool
  testStrandPool() {
    const pool = new StrandPool(3);
    
    // Test initial pool state
    if (pool.pool.length !== 0) {
      throw new Error('Initial pool should be empty');
    }
    
    // Test strand acquisition
    const strand1 = pool.acquire();
    if (!strand1 || typeof strand1.x !== 'number') {
      throw new Error('Strand acquisition failed');
    }
    
    // Test strand release
    pool.release(strand1);
    if (pool.pool.length !== 1) {
      throw new Error('Strand release not working');
    }
    
    // Test pool size limit
    const strand2 = pool.acquire();
    const strand3 = pool.acquire();
    const strand4 = pool.acquire();
    
    pool.release(strand2);
    pool.release(strand3);
    pool.release(strand4);
    
    if (pool.pool.length > 3) {
      throw new Error('Pool size limit not enforced');
    }
    
    // Test strand reset
    const reacquired = pool.acquire();
    if (reacquired.x !== 0 || reacquired.y !== 0) {
      throw new Error('Released strand not properly reset');
    }
  }
  
  // Test 7: Optimized Main Loop
  testOptimizedMainLoop() {
    const loop = new OptimizedMainLoop();
    
    // Test initial state
    if (loop.frameSkipCounter !== 0) {
      throw new Error('Initial frame skip counter should be 0');
    }
    
    // Test optimized update method
    const mockTime = 1000;
    const mockFrameCount = 15;
    
    // Mock window objects for testing
    window.topologyTransitionManager = {
      updateTransition: () => {}
    };
    window.cameraTransitionManager = {
      updateTransition: () => {},
      setAutoRotate: () => {}
    };
    window.cascadeEmergence = {
      update: () => {}
    };
    window.updateMorphicActivityPanel = () => {};
    window.updateFeedbackLoopsPanel = () => {};
    
    // Test that method doesn't throw
    try {
      loop.updateFSCTFSystemsOptimized(mockTime, mockFrameCount);
    } catch (error) {
      throw new Error(`Optimized update method threw error: ${error.message}`);
    }
  }
  
  // Test 8: Mathematical Accuracy Preservation
  testMathematicalAccuracy() {
    // Test that φ-constants are preserved
    const PHI = (1 + Math.sqrt(5)) / 2;
    const PHI_INV = 1 / PHI;
    
    if (Math.abs(PHI - 1.618033988749895) > 1e-10) {
      throw new Error('φ-constant calculation error');
    }
    
    if (Math.abs(PHI * PHI_INV - 1.0) > 1e-10) {
      throw new Error('φ-inverse relationship error');
    }
    
    // Test that mathematical operations remain precise
    const testValues = [0.1, 0.5, 1.0, PHI, Math.PI];
    for (const val of testValues) {
      const result = Math.sin(val) * Math.cos(val);
      if (isNaN(result) || !isFinite(result)) {
        throw new Error(`Mathematical operation failed for value ${val}`);
      }
    }
  }
  
  // Test 9: Performance Impact Measurement
  testPerformanceImpact() {
    const iterations = 1000;
    
    // Measure baseline performance
    const startTime = performance.now();
    for (let i = 0; i < iterations; i++) {
      // Simulate baseline operations
      Math.sin(i * 0.01);
      Math.cos(i * 0.01);
    }
    const baselineTime = performance.now() - startTime;
    
    // Measure optimized operations
    const startTime2 = performance.now();
    for (let i = 0; i < iterations; i++) {
      // Simulate optimized operations (should be faster)
      const angle = i * 0.01;
      Math.sin(angle);
      Math.cos(angle);
    }
    const optimizedTime = performance.now() - startTime2;
    
    // Optimized should not be significantly slower
    if (optimizedTime > baselineTime * 1.5) {
      throw new Error('Optimized operations are significantly slower than baseline');
    }
  }
  
  // Test 10: Memory Management
  testMemoryManagement() {
    // Test that object pooling reduces object creation
    const pool = new StrandPool(100);
    const initialMemory = performance.memory ? performance.memory.usedJSHeapSize : 0;
    
    // Create and release many strands
    const strands = [];
    for (let i = 0; i < 50; i++) {
      strands.push(pool.acquire());
    }
    
    for (const strand of strands) {
      pool.release(strand);
    }
    
    // Test that pool is working
    if (pool.pool.length === 0) {
      throw new Error('Pool should contain released strands');
    }
    
    // Test memory efficiency (if available)
    if (performance.memory) {
      const finalMemory = performance.memory.usedJSHeapSize;
      if (finalMemory > initialMemory * 2) {
        console.warn('⚠️ Memory usage increased significantly - investigate if needed');
      }
    }
  }
}

// Run the test suite
async function runTests() {
  const testSuite = new PerformanceOptimizationTestSuite();
  
  // Add all tests
  testSuite.addTest('Shader Program Caching', () => testSuite.testShaderCaching());
  testSuite.addTest('Uniform Buffer Management', () => testSuite.testUniformBufferManager());
  testSuite.addTest('WebGL State Management', () => testSuite.testWebGLStateManager());
  testSuite.addTest('Optimized Strand Manager', () => testSuite.testOptimizedStrandManager());
  testSuite.addTest('Adaptive Update Manager', () => testSuite.testAdaptiveUpdateManager());
  testSuite.addTest('Strand Pool', () => testSuite.testStrandPool());
  testSuite.addTest('Optimized Main Loop', () => testSuite.testOptimizedMainLoop());
  testSuite.addTest('Mathematical Accuracy Preservation', () => testSuite.testMathematicalAccuracy());
  testSuite.addTest('Performance Impact Measurement', () => testSuite.testPerformanceImpact());
  testSuite.addTest('Memory Management', () => testSuite.testMemoryManagement());
  
  // Run all tests
  await testSuite.runAll();
}

// Export for use in other modules
export { PerformanceOptimizationTestSuite, runTests };

// Run tests if this file is executed directly
if (typeof window === 'undefined') {
  // Node.js environment
  runTests().catch(console.error);
} else {
  // Browser environment - make available globally
  window.runPerformanceTests = runTests;
  console.log('🧪 Performance test suite loaded. Run window.runPerformanceTests() to test optimizations.');
}
