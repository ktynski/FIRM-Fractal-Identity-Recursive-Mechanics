// Performance Test Script for ExNahiloWebGL
// Run this in the browser console to test performance improvements

console.log('🧪 Starting ExNahiloWebGL Performance Test...');

// Performance test configuration
const TEST_CONFIG = {
  duration: 10000, // 10 seconds
  sampleInterval: 100, // Sample every 100ms
  warmupFrames: 60 // Wait 60 frames to warm up
};

class PerformanceTester {
  constructor() {
    this.results = [];
    this.startTime = 0;
    this.frameCount = 0;
    this.isRunning = false;
  }

  start() {
    if (this.isRunning) {
      console.log('⚠️ Test already running');
      return;
    }

    console.log('🚀 Starting performance test...');
    this.isRunning = true;
    this.results = [];
    this.frameCount = 0;
    this.startTime = performance.now();

    // Wait for warmup
    setTimeout(() => {
      this.runTest();
    }, TEST_CONFIG.warmupFrames * 16.67); // 60 FPS = 16.67ms per frame
  }

  runTest() {
    if (!this.isRunning) return;

    const currentTime = performance.now();
    const elapsed = currentTime - this.startTime;

    if (elapsed >= TEST_CONFIG.duration) {
      this.finish();
      return;
    }

    // Sample performance metrics
    if (window.PERFORMANCE_MONITOR) {
      const frameTime = window.PERFORMANCE_MONITOR.frameTimeHistory.length > 0 ? 
        window.PERFORMANCE_MONITOR.frameTimeHistory[window.PERFORMANCE_MONITOR.frameTimeHistory.length - 1] : 0;
      const throttle = window.PERFORMANCE_MONITOR.complexityThrottle;
      
      this.results.push({
        time: elapsed,
        frameTime: frameTime,
        throttle: throttle,
        fps: frameTime > 0 ? 1000 / frameTime : 0
      });
    }

    this.frameCount++;
    setTimeout(() => this.runTest(), TEST_CONFIG.sampleInterval);
  }

  finish() {
    this.isRunning = false;
    this.analyzeResults();
  }

  analyzeResults() {
    if (this.results.length === 0) {
      console.log('❌ No performance data collected');
      return;
    }

    const frameTimes = this.results.map(r => r.fps).filter(fps => fps > 0);
    const throttles = this.results.map(r => r.throttle);

    const avgFPS = frameTimes.reduce((a, b) => a + b, 0) / frameTimes.length;
    const minFPS = Math.min(...frameTimes);
    const maxFPS = Math.max(...frameTimes);
    const avgThrottle = throttles.reduce((a, b) => a + b, 0) / throttles.length;

    console.log('📊 Performance Test Results:');
    console.log(`⏱️  Test Duration: ${TEST_CONFIG.duration / 1000}s`);
    console.log(`📈 Frames Sampled: ${this.results.length}`);
    console.log(`🎯 Average FPS: ${avgFPS.toFixed(1)}`);
    console.log(`📉 Min FPS: ${minFPS.toFixed(1)}`);
    console.log(`📈 Max FPS: ${maxFPS.toFixed(1)}`);
    console.log(`🔧 Average Throttle: ${avgThrottle.toFixed(2)}`);
    
    // Performance rating
    let rating = '🔴 Poor';
    if (avgFPS >= 55) rating = '🟢 Excellent';
    else if (avgFPS >= 45) rating = '🟡 Good';
    else if (avgFPS >= 30) rating = '🟠 Fair';
    
    console.log(`🏆 Performance Rating: ${rating}`);
    
    // Recommendations
    if (avgFPS < 30) {
      console.log('💡 Recommendations:');
      console.log('   - Reduce complexity scaling frequency');
      console.log('   - Lower maximum complexity limits');
      console.log('   - Enable adaptive performance mode');
    } else if (avgFPS < 45) {
      console.log('💡 Recommendations:');
      console.log('   - Consider reducing some complexity operations');
      console.log('   - Monitor memory usage');
    } else {
      console.log('💡 Performance is good! Consider increasing complexity for more visual effects.');
    }
  }

  stop() {
    this.isRunning = false;
    console.log('⏹️ Performance test stopped');
  }
}

// Create global tester instance
window.performanceTester = new PerformanceTester();

// Add test commands to global scope
window.runPerformanceTest = () => window.performanceTester.start();
window.stopPerformanceTest = () => window.performanceTester.stop();

console.log('✅ Performance test script loaded!');
console.log('Commands:');
console.log('  runPerformanceTest()  - Start 10-second performance test');
console.log('  stopPerformanceTest() - Stop current test');
console.log('  performanceTester     - Access tester instance directly');
