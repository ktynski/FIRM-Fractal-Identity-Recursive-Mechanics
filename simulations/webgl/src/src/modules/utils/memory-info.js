/**
 * Memory Information Utilities
 * Memory usage tracking and GPU memory information
 */

export class MemoryInfo {
  constructor() {
    this.lastCheck = 0;
    this.checkInterval = 5000; // Check every 5 seconds
    this.memoryHistory = [];
    this.maxHistorySize = 100;
    
    console.log('📊 Memory Info utilities initialized');
  }
  
  /**
   * Get comprehensive memory information
   */
  getMemoryInfo() {
    const info = {
      timestamp: Date.now(),
      heapUsed: 0,
      heapTotal: 0,
      heapLimit: 0,
      external: 0,
      webgl: this.getWebGLMemoryInfo(),
      jsHeap: this.getJSHeapInfo(),
      performance: this.getPerformanceInfo()
    };
    
    // Node.js memory (if available)
    if (typeof process !== 'undefined' && process.memoryUsage) {
      const nodeMemory = process.memoryUsage();
      info.heapUsed = nodeMemory.heapUsed;
      info.heapTotal = nodeMemory.heapTotal;
      info.external = nodeMemory.external;
      info.rss = nodeMemory.rss;
    }
    
    // Add to history
    this.memoryHistory.push(info);
    if (this.memoryHistory.length > this.maxHistorySize) {
      this.memoryHistory.shift();
    }
    
    return info;
  }
  
  /**
   * Get WebGL memory information
   */
  getWebGLMemoryInfo() {
    const gl = window.gl;
    if (!gl) return { available: false };
    
    const info = {
      available: true,
      vendor: gl.getParameter(gl.VENDOR),
      renderer: gl.getParameter(gl.RENDERER),
      version: gl.getParameter(gl.VERSION),
      maxTextureSize: gl.getParameter(gl.MAX_TEXTURE_SIZE),
      maxCombinedTextureImageUnits: gl.getParameter(gl.MAX_COMBINED_TEXTURE_IMAGE_UNITS),
      maxVertexTextureImageUnits: gl.getParameter(gl.MAX_VERTEX_TEXTURE_IMAGE_UNITS),
      maxFragmentUniformVectors: gl.getParameter(gl.MAX_FRAGMENT_UNIFORM_VECTORS),
      maxVaryingVectors: gl.getParameter(gl.MAX_VARYING_VECTORS),
      extensions: gl.getSupportedExtensions()
    };
    
    // Memory extension info (if available)
    const memoryExt = gl.getExtension('WEBGL_debug_renderer_info');
    if (memoryExt) {
      info.unmaskedVendor = gl.getParameter(memoryExt.UNMASKED_VENDOR_WEBGL);
      info.unmaskedRenderer = gl.getParameter(memoryExt.UNMASKED_RENDERER_WEBGL);
    }
    
    return info;
  }
  
  /**
   * Get JavaScript heap information (Chrome specific)
   */
  getJSHeapInfo() {
    if (!window.performance || !window.performance.memory) {
      return { available: false };
    }
    
    const memory = window.performance.memory;
    return {
      available: true,
      usedJSHeapSize: memory.usedJSHeapSize,
      totalJSHeapSize: memory.totalJSHeapSize,
      jsHeapSizeLimit: memory.jsHeapSizeLimit,
      usedPercent: (memory.usedJSHeapSize / memory.jsHeapSizeLimit) * 100
    };
  }
  
  /**
   * Get general performance information
   */
  getPerformanceInfo() {
    const info = {
      timestamp: performance.now(),
      timeOrigin: performance.timeOrigin || 0,
      navigationStart: 0
    };
    
    // Navigation timing (if available)
    if (window.performance.navigation) {
      info.navigationStart = window.performance.navigation.timing?.navigationStart || 0;
      info.loadEventEnd = window.performance.navigation.timing?.loadEventEnd || 0;
      info.domContentLoadedEventEnd = window.performance.navigation.timing?.domContentLoadedEventEnd || 0;
    }
    
    // Resource timing entries count
    if (window.performance.getEntriesByType) {
      info.resourceEntries = window.performance.getEntriesByType('resource').length;
      info.measureEntries = window.performance.getEntriesByType('measure').length;
      info.markEntries = window.performance.getEntriesByType('mark').length;
    }
    
    return info;
  }
  
  /**
   * Check if memory usage is concerning
   */
  isMemoryPressureHigh() {
    const jsHeap = this.getJSHeapInfo();
    if (!jsHeap.available) return false;
    
    // Consider high if using more than 80% of available heap
    return jsHeap.usedPercent > 80;
  }
  
  /**
   * Get memory pressure level (0-1)
   */
  getMemoryPressure() {
    const jsHeap = this.getJSHeapInfo();
    if (!jsHeap.available) return 0;
    
    return Math.min(1, jsHeap.usedPercent / 100);
  }
  
  /**
   * Format bytes to human readable format
   */
  formatBytes(bytes) {
    if (bytes === 0) return '0 B';
    
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }
  
  /**
   * Get memory usage summary string
   */
  getMemorySummary() {
    const info = this.getMemoryInfo();
    const jsHeap = info.jsHeap;
    
    if (!jsHeap.available) {
      return 'Memory info not available';
    }
    
    return `JS Heap: ${this.formatBytes(jsHeap.usedJSHeapSize)} / ${this.formatBytes(jsHeap.jsHeapSizeLimit)} (${jsHeap.usedPercent.toFixed(1)}%)`;
  }
  
  /**
   * Log memory information to console
   */
  logMemoryInfo() {
    const info = this.getMemoryInfo();
    
    console.group('🧠 Memory Information');
    
    if (info.jsHeap.available) {
      console.log('JS Heap:', this.formatBytes(info.jsHeap.usedJSHeapSize), '/', this.formatBytes(info.jsHeap.jsHeapSizeLimit));
      console.log('Usage:', info.jsHeap.usedPercent.toFixed(1) + '%');
    }
    
    if (info.webgl.available) {
      console.log('WebGL Renderer:', info.webgl.renderer);
      console.log('Max Texture Size:', info.webgl.maxTextureSize);
      console.log('Extensions:', info.webgl.extensions.length);
    }
    
    if (info.heapUsed > 0) {
      console.log('Node Heap Used:', this.formatBytes(info.heapUsed));
      console.log('Node Heap Total:', this.formatBytes(info.heapTotal));
    }
    
    console.groupEnd();
  }
  
  /**
   * Start periodic memory monitoring
   */
  startMonitoring(interval = 30000) { // Default 30 seconds
    this.stopMonitoring(); // Clear any existing interval
    
    this.monitoringInterval = setInterval(() => {
      const pressure = this.getMemoryPressure();
      
      if (pressure > 0.8) {
        console.warn('⚠️ High memory pressure:', pressure.toFixed(2));
        this.logMemoryInfo();
      } else if (pressure > 0.6) {
        console.log('📈 Moderate memory usage:', pressure.toFixed(2));
      }
    }, interval);
    
    console.log('📊 Memory monitoring started');
  }
  
  /**
   * Stop memory monitoring
   */
  stopMonitoring() {
    if (this.monitoringInterval) {
      clearInterval(this.monitoringInterval);
      this.monitoringInterval = null;
      console.log('📊 Memory monitoring stopped');
    }
  }
  
  /**
   * Get memory history
   */
  getHistory() {
    return [...this.memoryHistory];
  }
  
  /**
   * Clear memory history
   */
  clearHistory() {
    this.memoryHistory = [];
    console.log('📊 Memory history cleared');
  }
  
  /**
   * Trigger garbage collection if available
   */
  suggestGarbageCollection() {
    if (window.gc && typeof window.gc === 'function') {
      console.log('🗑️ Triggering garbage collection...');
      window.gc();
      return true;
    } else {
      console.log('🗑️ Garbage collection not available');
      return false;
    }
  }
  
  /**
   * Check for memory leaks by comparing current vs baseline
   */
  checkForLeaks(baselineInfo) {
    const currentInfo = this.getMemoryInfo();
    
    if (!currentInfo.jsHeap.available || !baselineInfo?.jsHeap?.available) {
      return { available: false };
    }
    
    const heapGrowth = currentInfo.jsHeap.usedJSHeapSize - baselineInfo.jsHeap.usedJSHeapSize;
    const growthPercent = (heapGrowth / baselineInfo.jsHeap.usedJSHeapSize) * 100;
    
    return {
      available: true,
      heapGrowth: heapGrowth,
      growthPercent: growthPercent,
      isPossibleLeak: growthPercent > 50, // Growth >50% might indicate leak
      summary: `Heap grew by ${this.formatBytes(heapGrowth)} (${growthPercent.toFixed(1)}%)`
    };
  }
}

// Create and export default instance
export const memoryInfo = new MemoryInfo();

// Export the getMemoryInfo function for compatibility
export function getMemoryInfo() {
  return memoryInfo.getMemoryInfo();
}
