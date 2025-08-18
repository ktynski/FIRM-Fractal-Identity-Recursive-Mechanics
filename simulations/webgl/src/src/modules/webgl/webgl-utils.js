/**
 * WebGL Utilities Module
 * Common WebGL setup, texture management, and utility functions
 */

/**
 * Initialize WebGL2 context with error handling
 * @param {HTMLCanvasElement} canvas - The canvas element
 * @returns {WebGL2RenderingContext} WebGL2 context
 */
export function initWebGL2(canvas) {
  // MAXIMUM QUALITY SETTINGS for finest detail rendering
  const gl = canvas.getContext('webgl2', { 
    antialias: true,           // ENABLE: Smooth antialiasing for fine details
    alpha: false,              // Keep false for performance 
    depth: true,               // Enable depth buffer for 3D precision
    stencil: false,            // Disable stencil for performance
    preserveDrawingBuffer: false,  // False for performance
    premultipliedAlpha: false, // Better color precision
    powerPreference: 'high-performance' // Force high-performance GPU
  });
  
  if (!gl) {
    throw new Error('WebGL2 is not supported by this browser');
  }
  
  // Check for required extensions
  const extCBF = gl.getExtension('EXT_color_buffer_float');
  const extCBHF = gl.getExtension('EXT_color_buffer_half_float');
  
  const HAS_EXT_CBF = !!extCBF;
  const HAS_EXT_CBHF = !!extCBHF;
  
  if (!HAS_EXT_CBF && !HAS_EXT_CBHF) {
    console.warn('No float render targets available; using fallback RGBA8 mode');
  }
  
  // Set up context loss handling
  canvas.addEventListener('webglcontextlost', (e) => {
    e.preventDefault();
    console.warn('WebGL context lost; entering safe void mode');
    window.__ctxLost = true;
  }, false);
  
  canvas.addEventListener('webglcontextrestored', () => {
    console.log('WebGL context restored; reloading to safely reinitialize resources');
    window.location.reload();
  }, false);
  
  // Basic setup
  gl.disable(gl.DEPTH_TEST);
  gl.disable(gl.CULL_FACE);
  
  return gl;
}

/**
 * Create a Float or Half-Float RGBA texture
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @param {number} width - Texture width
 * @param {number} height - Texture height
 * @param {boolean} useFloat32 - Whether to use 32-bit floats (vs 16-bit)
 * @returns {WebGLTexture} The created texture
 */
export function createFloatTexture(gl, width, height, useFloat32 = true) {
  const tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, tex);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  
  const hasFloatExtension = !!gl.getExtension('EXT_color_buffer_float');
  
  if (hasFloatExtension && useFloat32) {
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA32F, width, height, 0, gl.RGBA, gl.FLOAT, null);
  } else if (gl.getExtension('EXT_color_buffer_half_float')) {
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA16F, width, height, 0, gl.RGBA, gl.HALF_FLOAT, null);
  } else {
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, width, height, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
  }
  
  return tex;
}

/**
 * Create a framebuffer and attach a texture
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @param {WebGLTexture} tex - Texture to attach
 * @returns {WebGLFramebuffer} The created framebuffer
 */
export function createFramebuffer(gl, tex) {
  const fbo = gl.createFramebuffer();
  gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
  gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tex, 0);
  
  const status = gl.checkFramebufferStatus(gl.FRAMEBUFFER);
  if (status !== gl.FRAMEBUFFER_COMPLETE) {
    throw new Error(`Framebuffer incomplete: ${status}`);
  }
  
  gl.bindFramebuffer(gl.FRAMEBUFFER, null);
  return fbo;
}

/**
 * Resize canvas to match display size
 * @param {HTMLCanvasElement} canvas - The canvas element
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @param {number} multiplier - Resolution multiplier (default: devicePixelRatio)
 */
export function resizeCanvasToDisplaySize(canvas, gl, multiplier = (window.devicePixelRatio || 1) * 2.0) { // INCREASED: 2x resolution for finest details
  const width = Math.floor(canvas.clientWidth * multiplier);
  const height = Math.floor(canvas.clientHeight * multiplier);
  
  if (canvas.width !== width || canvas.height !== height) {
    canvas.width = width;
    canvas.height = height;
    gl.viewport(0, 0, width, height);
  }
}

/**
 * Create a fullscreen quad vertex array object
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @returns {WebGLVertexArrayObject} The VAO for fullscreen quad
 */
export function createFullscreenQuad(gl) {
  // Two-triangle fullscreen quad for TRIANGLES mode (6 vertices)
  // Triangle 1: (-1,-1) -> (1,-1) -> (-1,1)
  // Triangle 2: (1,-1) -> (1,1) -> (-1,1)
  const quadData = new Float32Array([
    -1, -1,   1, -1,   -1,  1,
     1, -1,   1,  1,   -1,  1
  ]);
  const quadBuf = gl.createBuffer();
  const quadVAO = gl.createVertexArray();
  
  gl.bindVertexArray(quadVAO);
  gl.bindBuffer(gl.ARRAY_BUFFER, quadBuf);
  gl.bufferData(gl.ARRAY_BUFFER, quadData, gl.STATIC_DRAW);
  gl.enableVertexAttribArray(0);
  gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
  gl.bindVertexArray(null);
  
  return quadVAO;
}

/**
 * Create particle instance data for rendering
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @param {number} numParticles - Number of particles
 * @returns {Object} VAO and buffer for particle rendering
 */
export function createParticleInstanceData(gl, numParticles) {
  const ids = new Float32Array(numParticles);
  for (let i = 0; i < numParticles; i++) {
    ids[i] = i;
  }
  
  const instanceBuf = gl.createBuffer();
  const instanceVAO = gl.createVertexArray();
  
  gl.bindVertexArray(instanceVAO);
  gl.bindBuffer(gl.ARRAY_BUFFER, instanceBuf);
  gl.bufferData(gl.ARRAY_BUFFER, ids, gl.STATIC_DRAW);
  gl.enableVertexAttribArray(0);
  gl.vertexAttribPointer(0, 1, gl.FLOAT, false, 0, 0);
  gl.bindVertexArray(null);
  
  return { vao: instanceVAO, buffer: instanceBuf };
}

/**
 * Create a WebGL shader
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @param {number} type - Shader type (gl.VERTEX_SHADER or gl.FRAGMENT_SHADER)
 * @param {string} source - Shader source code
 * @returns {WebGLShader} Compiled shader
 */
export function createShader(gl, type, source) {
  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    const error = gl.getShaderInfoLog(shader);
    gl.deleteShader(shader);
    throw new Error(`Shader compilation error: ${error}`);
  }
  
  return shader;
}

/**
 * Create a WebGL program from vertex and fragment shader sources
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @param {string} vsSrc - Vertex shader source
 * @param {string} fsSrc - Fragment shader source
 * @returns {WebGLProgram} Linked program
 */
export function createProgram(gl, vsSrc, fsSrc) {
  const vs = createShader(gl, gl.VERTEX_SHADER, vsSrc);
  const fs = createShader(gl, gl.FRAGMENT_SHADER, fsSrc);
  
  const program = gl.createProgram();
  gl.attachShader(program, vs);
  gl.attachShader(program, fs);
  gl.linkProgram(program);
  
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    const error = gl.getProgramInfoLog(program);
    gl.deleteProgram(program);
    gl.deleteShader(vs);
    gl.deleteShader(fs);
    throw new Error(`Program linking error: ${error}`);
  }
  
  // Clean up shaders
  gl.deleteShader(vs);
  gl.deleteShader(fs);
  
  return program;
}

/**
 * Get memory usage information if available
 * @param {WebGL2RenderingContext} gl - WebGL2 context
 * @returns {Object|null} Memory info or null if not available
 */
export function getMemoryInfo(gl) {
  const ext = gl.getExtension('WEBGL_debug_renderer_info');
  if (!ext) return null;
  
  return {
    vendor: gl.getParameter(ext.UNMASKED_VENDOR_WEBGL),
    renderer: gl.getParameter(ext.UNMASKED_RENDERER_WEBGL)
  };
}

/**
 * WebGL state manager to minimize state changes
 */
export class WebGLStateManager {
  constructor(gl) {
    this.gl = gl;
    this.currentProgram = null;
    this.currentVAO = null;
    this.currentFramebuffer = null;
    this.currentBlendMode = null;
  }
  
  useProgram(program) {
    if (this.currentProgram !== program) {
      this.gl.useProgram(program);
      this.currentProgram = program;
    }
  }
  
  bindVertexArray(vao) {
    if (this.currentVAO !== vao) {
      this.gl.bindVertexArray(vao);
      this.currentVAO = vao;
    }
  }
  
  bindFramebuffer(framebuffer) {
    if (this.currentFramebuffer !== framebuffer) {
      this.gl.bindFramebuffer(this.gl.FRAMEBUFFER, framebuffer);
      this.currentFramebuffer = framebuffer;
    }
  }
  
  setBlendMode(src, dst) {
    const mode = `${src}-${dst}`;
    if (this.currentBlendMode !== mode) {
      this.gl.blendFunc(src, dst);
      this.currentBlendMode = mode;
    }
  }
}
