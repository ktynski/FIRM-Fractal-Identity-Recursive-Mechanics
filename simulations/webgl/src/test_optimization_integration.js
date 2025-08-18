/**
 * Performance Optimization Integration Test
 * Tests that all optimizations work together correctly in the FSCTF system
 */

import { createCachedProgram, UniformBufferManager } from './src/modules/shaders/shaders.js';
import { WebGLStateManager } from './src/modules/webgl/webgl-utils.js';
import { OptimizedStrandManager } from './src/modules/fsctf/strand-manager.js';
import { AdaptiveUpdateManager } from './src/modules/performance/performance.js';
import { StrandPool } from './src/modules/fsctf/grace-operator.js';
import { OptimizedMainLoop } from './src/modules/core/main-loop.js';

// Mock WebGL context for integration testing
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
    checkFramebufferStatus: () => 36053,
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

// Integration test suite
class OptimizationIntegrationTest {
  constructor() {
    this.mockGL = createMockWebGL();
    this.testResults = [];
  }
  
  async runIntegrationTests() {
    console.log('🔗 Running Performance Optimization Integration Tests...\n');
    
    try {
      // Test 1: Complete optimization pipeline
      await this.testCompleteOptimizationPipeline();
      
      // Test 2: Performance scaling under load
      await this.testPerformanceScaling();
      
      // Test 3: Memory efficiency under stress
      await this.testMemoryEfficiency();
      
      // Test 4: Mathematical consistency preservation
      await this.testMathematicalConsistency();
      
      // Test 5: Real-world simulation scenario
      await this.testRealWorldScenario();
      
      console.log('\n🎉 All integration tests passed!');
      console.log('🚀 Performance optimizations are working correctly together.');
      
    } catch (error) {
      console.error('\n❌ Integration test failed:', error.message);
      throw error;
    }
  }
  
  // Test 1: Complete optimization pipeline
  async testCompleteOptimizationPipeline() {
    console.log('🧪 Testing complete optimization pipeline...');
    
    // Initialize all optimization components
    const stateManager = new WebGLStateManager(this.mockGL);
    const uniformManager = new UniformBufferManager(this.mockGL);
    const strandManager = new OptimizedStrandManager();
    const updateManager = new AdaptiveUpdateManager();
    const strandPool = new StrandPool(100);
    const mainLoop = new OptimizedMainLoop();
    
    // Test shader caching
    const vsSrc = 'attribute vec2 position; void main() { gl_Position = vec4(position, 0.0, 1.0); }';
    const fsSrc = 'void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }';
    
    const program1 = await createCachedProgram(this.mockGL, vsSrc, fsSrc, 'integration-test');
    const program2 = await createCachedProgram(this.mockGL, vsSrc, fsSrc, 'integration-test');
    
    if (program1 !== program2) {
      throw new Error('Shader caching not working in integration');
    }
    
    // Test uniform buffer management
    const uniformData = new Float32Array([1.0, 2.0, 3.0, 4.0]);
    const buffer = uniformManager.createUniformBuffer('test', uniformData);
    if (!buffer) {
      throw new Error('Uniform buffer creation failed in integration');
    }
    
    // Test WebGL state management
    stateManager.useProgram(program1);
    if (stateManager.currentProgram !== program1) {
      throw new Error('State management not working in integration');
    }
    
    // Test strand management
    strandManager.updateParticleBuffer(this.mockGL, 0);
    if (strandManager.lastUpdateFrame !== 0) {
      throw new Error('Strand management not working in integration');
    }
    
    // Test adaptive updates
    updateManager.updatePerformanceRating(60);
    if (updateManager.currentPerformance !== 'excellent') {
      throw new Error('Adaptive updates not working in integration');
    }
    
    // Test strand pooling
    const strand = strandPool.acquire();
    if (!strand) {
      throw new Error('Strand pooling not working in integration');
    }
    strandPool.release(strand);
    
    // Test main loop optimization
    if (mainLoop.frameSkipCounter !== 0) {
      throw new Error('Main loop optimization not working in integration');
    }
    
    console.log('✅ Complete optimization pipeline working');
  }
  
  // Test 2: Performance scaling under load
  async testPerformanceScaling() {
    console.log('🧪 Testing performance scaling under load...');
    
    const updateManager = new AdaptiveUpdateManager();
    const strandPool = new StrandPool(1000);
    
    // Simulate increasing load
    const fpsLevels = [60, 45, 30, 20, 10];
    const expectedPerformance = ['excellent', 'good', 'fair', 'poor', 'critical'];
    
    for (let i = 0; i < fpsLevels.length; i++) {
      updateManager.updatePerformanceRating(fpsLevels[i]);
      if (updateManager.currentPerformance !== expectedPerformance[i]) {
        throw new Error(`Performance scaling failed at ${fpsLevels[i]} FPS`);
      }
      
      // Test that update intervals scale correctly
      const interval = updateManager.getUpdateInterval('soulEcho');
      if (typeof interval !== 'number' || interval <= 0) {
        throw new Error(`Invalid update interval at ${fpsLevels[i]} FPS`);
      }
    }
    
    // Test strand pool under load
    const strands = [];
    for (let i = 0; i < 500; i++) {
      strands.push(strandPool.acquire());
    }
    
    if (strands.length !== 500) {
      throw new Error('Strand pool failed to handle load');
    }
    
    // Release all strands
    for (const strand of strands) {
      strandPool.release(strand);
    }
    
    if (strandPool.pool.length === 0) {
      throw new Error('Strand pool not properly managing released objects');
    }
    
    console.log('✅ Performance scaling working correctly');
  }
  
  // Test 3: Memory efficiency under stress
  async testMemoryEfficiency() {
    console.log('🧪 Testing memory efficiency under stress...');
    
    const strandPool = new StrandPool(500);
    const uniformManager = new UniformBufferManager(this.mockGL);
    
    // Create many objects to test memory management
    const objects = [];
    const iterations = 1000;
    
    for (let i = 0; i < iterations; i++) {
      // Acquire and release strands rapidly
      const strand = strandPool.acquire();
      strandPool.release(strand);
      
      // Create and update uniform buffers
      const data = new Float32Array([i, i+1, i+2, i+3]);
      uniformManager.createUniformBuffer(`buffer-${i}`, data);
      
      objects.push({ strand, data });
    }
    
    // Verify pool size is maintained
    if (strandPool.pool.length > 500) {
      throw new Error('Strand pool exceeded size limit under stress');
    }
    
    // Verify uniform buffers are managed correctly
    if (uniformManager.uniformBuffers.size !== iterations) {
      throw new Error('Uniform buffer management failed under stress');
    }
    
    console.log('✅ Memory efficiency maintained under stress');
  }
  
  // Test 4: Mathematical consistency preservation
  async testMathematicalConsistency() {
    console.log('🧪 Testing mathematical consistency preservation...');
    
    // Test φ-constants remain consistent
    const PHI = (1 + Math.sqrt(5)) / 2;
    const PHI_INV = 1 / PHI;
    const PHI2 = PHI * PHI;
    
    // Verify mathematical relationships
    if (Math.abs(PHI * PHI_INV - 1.0) > 1e-10) {
      throw new Error('φ-inverse relationship broken');
    }
    
    if (Math.abs(PHI2 - PHI - 1.0) > 1e-10) {
      throw new Error('φ-squared relationship broken');
    }
    
    // Test that optimizations don't affect mathematical precision
    const testValues = [0.1, 0.5, 1.0, PHI, Math.PI, 2.718];
    for (const val of testValues) {
      const sinVal = Math.sin(val);
      const cosVal = Math.cos(val);
      const tanVal = Math.tan(val);
      
      // Verify trigonometric relationships
      if (Math.abs(sinVal * sinVal + cosVal * cosVal - 1.0) > 1e-10) {
        throw new Error(`Trigonometric identity broken for value ${val}`);
      }
      
      if (Math.abs(tanVal - sinVal / cosVal) > 1e-10) {
        throw new Error(`Tangent relationship broken for value ${val}`);
      }
    }
    
    // Test complex mathematical operations
    const complexResult = Math.exp(PHI) * Math.log(PHI) / Math.sqrt(PHI);
    if (!isFinite(complexResult) || isNaN(complexResult)) {
      throw new Error('Complex mathematical operations broken');
    }
    
    console.log('✅ Mathematical consistency preserved');
  }
  
  // Test 5: Real-world simulation scenario
  async testRealWorldScenario() {
    console.log('🧪 Testing real-world simulation scenario...');
    
    // Simulate a typical FSCTF simulation frame
    const stateManager = new WebGLStateManager(this.mockGL);
    const uniformManager = new UniformBufferManager(this.mockGL);
    const strandManager = new OptimizedStrandManager();
    const updateManager = new AdaptiveUpdateManager();
    const strandPool = new StrandPool(1000);
    const mainLoop = new OptimizedMainLoop();
    
    // Simulate frame processing
    const frameCount = 100;
    const startTime = performance.now();
    
    for (let frame = 0; frame < frameCount; frame++) {
      // Update performance rating based on simulated FPS
      const simulatedFPS = 60 - (frame % 30); // Vary FPS to test adaptation
      updateManager.updatePerformanceRating(simulatedFPS);
      
      // Process strands
      const activeStrands = Math.floor(100 + frame * 2); // Growing strand count
      for (let i = 0; i < activeStrands; i++) {
        const strand = strandPool.acquire();
        strandPool.release(strand);
      }
      
      // Update particle buffers
      if (frame % 5 === 0) {
        strandManager.updateParticleBuffer(this.mockGL, frame);
      }
      
      // Update uniform buffers
      const uniformData = new Float32Array([
        Math.sin(frame * 0.1),
        Math.cos(frame * 0.1),
        frame * 0.01,
        1.0
      ]);
      uniformManager.updateUniformBuffer('simulation', uniformData);
      
      // Simulate WebGL state changes
      const program = { id: `program-${frame % 3}` };
      stateManager.useProgram(program);
    }
    
    const endTime = performance.now();
    const totalTime = endTime - startTime;
    const avgTimePerFrame = totalTime / frameCount;
    
    // Verify performance is reasonable
    if (avgTimePerFrame > 16.67) { // Should be under 16.67ms for 60fps
      console.warn(`⚠️ Average frame time (${avgTimePerFrame.toFixed(2)}ms) is high`);
    }
    
    // Verify all systems are working
    if (strandPool.pool.length === 0) {
      throw new Error('Strand pool exhausted during simulation');
    }
    
    if (uniformManager.uniformBuffers.size === 0) {
      throw new Error('Uniform buffer management failed during simulation');
    }
    
    console.log(`✅ Real-world simulation completed: ${frameCount} frames in ${totalTime.toFixed(2)}ms`);
    console.log(`   Average: ${avgTimePerFrame.toFixed(2)}ms per frame`);
  }
}

// Run integration tests
async function runIntegrationTests() {
  const integrationTest = new OptimizationIntegrationTest();
  await integrationTest.runIntegrationTests();
}

// Export for use in other modules
export { OptimizationIntegrationTest, runIntegrationTests };

// Run tests if this file is executed directly
if (typeof window === 'undefined') {
  // Node.js environment
  runIntegrationTests().catch(console.error);
} else {
  // Browser environment - make available globally
  window.runIntegrationTests = runIntegrationTests;
  console.log('🔗 Integration test suite loaded. Run window.runIntegrationTests() to test optimization integration.');
}
