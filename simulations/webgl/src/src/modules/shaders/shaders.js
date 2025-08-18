/**
 * Shader Management Module
 * Loads and manages all GLSL shaders for the FSCTF system
 */

// Store for all loaded shaders
const shaderCache = new Map();

// Add shader program caching
const programCache = new Map();

/**
 * Load a shader from a separate file
 * @param {string} path - Path to the shader file
 * @returns {Promise<string>} The shader source code
 */
async function loadShader(path) {
  // Add cache busting to shader URLs
  const cacheBustedPath = path + '?v=45';
  
  if (shaderCache.has(cacheBustedPath)) {
    return shaderCache.get(cacheBustedPath);
  }
  
  try {
    const response = await fetch(cacheBustedPath);
    if (!response.ok) {
      throw new Error(`Failed to load shader: ${path}`);
    }
    const source = await response.text();
    shaderCache.set(cacheBustedPath, source);
    return source;
  } catch (error) {
    console.error(`Error loading shader ${path}:`, error);
    throw error;
  }
}

/**
 * Include a shader file in another shader (simple #include replacement)
 * @param {string} shaderSource - The main shader source
 * @param {Map<string, string>} includes - Map of include names to source code
 * @returns {string} The shader source with includes resolved
 */
function resolveIncludes(shaderSource, includes = new Map()) {
  let result = shaderSource;
  
  // Simple #include replacement
  for (const [includeName, includeSource] of includes) {
    const includePattern = new RegExp(`#include\\s+"${includeName}"`, 'g');
    result = result.replace(includePattern, includeSource);
  }
  
  return result;
}

/**
 * Load all shaders and their dependencies
 * @returns {Promise<Object>} Object containing all shader sources
 */
export async function loadAllShaders() {
  const basePath = './modules/shaders/';
  
  try {
    // Load noise utility first (it's included in other shaders)
    const noise = await loadShader(basePath + 'noise.glsl');
    
    // Load all shader sources
    const [
      quadVS,
      simFSTemplate,
      renderVSTemplate,
      renderFSTemplate,
      reduceFSTemplate,
      decayFSTemplate,
      presentFSTemplate,
      corrFSTemplate,
      frstFSTemplate
    ] = await Promise.all([
      loadShader(basePath + 'quad.vert'),
      loadShader(basePath + 'sim.frag'),
      loadShader(basePath + 'render.vert'),
      loadShader(basePath + 'render.frag'),
      loadShader(basePath + 'reduce.frag'),
      loadShader(basePath + 'decay.frag'),
      loadShader(basePath + 'present.frag'),
      loadShader(basePath + 'corr.frag'),
      loadShader(basePath + 'frst.frag')
    ]);
    
    // Create includes map for noise
    const includes = new Map([['noise.glsl', noise]]);
    
    // Resolve includes in shaders that need them
    const simFS = resolveIncludes(simFSTemplate, includes);
    const renderVS = resolveIncludes(renderVSTemplate, includes);
    const renderFS = resolveIncludes(renderFSTemplate, includes);
    const reduceFS = resolveIncludes(reduceFSTemplate, includes);
    const decayFS = resolveIncludes(decayFSTemplate, includes);
    const presentFS = resolveIncludes(presentFSTemplate, includes);
    const corrFS = resolveIncludes(corrFSTemplate, includes);
    const frstFS = resolveIncludes(frstFSTemplate, includes);
    
    return {
      quadVS,
      simFS,
      renderVS,
      renderFS,
      reduceFS,
      decayFS,
      presentFS,
      corrFS,
      frstFS,
      // Utility
      noise
    };
  } catch (error) {
    console.error('Failed to load shaders:', error);
    throw error;
  }
}

/**
 * Create a WebGL shader program
 * @param {WebGL2RenderingContext} gl - WebGL context
 * @param {string} vertexSource - Vertex shader source
 * @param {string} fragmentSource - Fragment shader source
 * @returns {WebGLProgram} The compiled shader program
 */
export function createShaderProgram(gl, vertexSource, fragmentSource) {
  const vertexShader = gl.createShader(gl.VERTEX_SHADER);
  gl.shaderSource(vertexShader, vertexSource);
  gl.compileShader(vertexShader);
  
  if (!gl.getShaderParameter(vertexShader, gl.COMPILE_STATUS)) {
    const error = gl.getShaderInfoLog(vertexShader);
    gl.deleteShader(vertexShader);
    throw new Error(`Vertex shader compilation error: ${error}`);
  }
  
  const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
  gl.shaderSource(fragmentShader, fragmentSource);
  gl.compileShader(fragmentShader);
  
  if (!gl.getShaderParameter(fragmentShader, gl.COMPILE_STATUS)) {
    const error = gl.getShaderInfoLog(fragmentShader);
    gl.deleteShader(vertexShader);
    gl.deleteShader(fragmentShader);
    throw new Error(`Fragment shader compilation error: ${error}`);
  }
  
  const program = gl.createProgram();
  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);
  
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    const error = gl.getProgramInfoLog(program);
    gl.deleteProgram(program);
    gl.deleteShader(vertexShader);
    gl.deleteShader(fragmentShader);
    throw new Error(`Shader program linking error: ${error}`);
  }
  
  // Clean up shaders (they're now part of the program)
  gl.deleteShader(vertexShader);
  gl.deleteShader(fragmentShader);
  
  return program;
}

/**
 * Create and cache a WebGL program
 */
export async function createCachedProgram(gl, vsSrc, fsSrc, cacheKey) {
  if (programCache.has(cacheKey)) {
    return programCache.get(cacheKey);
  }
  
  const program = createShaderProgram(gl, vsSrc, fsSrc);
  programCache.set(cacheKey, program);
  return program;
}

/**
 * Precompile all shader combinations at startup
 */
export async function precompileShaders(gl) {
  const shaders = await loadAllShaders();
  
  // Precompile common combinations
  const commonPrograms = [
    { key: 'render', vs: shaders.renderVS, fs: shaders.renderFS },
    { key: 'sim', vs: shaders.quadVS, fs: shaders.simFS },
    { key: 'present', vs: shaders.quadVS, fs: shaders.presentFS }
  ];
  
  for (const prog of commonPrograms) {
    await createCachedProgram(gl, prog.vs, prog.fs, prog.key);
  }
  
  console.log('🚀 Shader precompilation complete');
}

/**
 * Uniform buffer object for batching shader parameters
 */
export class UniformBufferManager {
  constructor(gl) {
    this.gl = gl;
    this.uniformBuffers = new Map();
    this.currentFrame = 0;
  }
  
  createUniformBuffer(name, data, usage = gl.DYNAMIC_DRAW) {
    const buffer = this.gl.createBuffer();
    this.gl.bindBuffer(this.gl.UNIFORM_BUFFER, buffer);
    this.gl.bufferData(this.gl.UNIFORM_BUFFER, data, usage);
    
    this.uniformBuffers.set(name, {
      buffer,
      data: new Float32Array(data),
      lastUpdate: -1
    });
    
    return buffer;
  }
  
  updateUniformBuffer(name, newData, forceUpdate = false) {
    const uniform = this.uniformBuffers.get(name);
    if (!uniform) return;
    
    // Only update if data changed or forced
    if (forceUpdate || !this.arraysEqual(uniform.data, newData)) {
      this.gl.bindBuffer(this.gl.UNIFORM_BUFFER, uniform.buffer);
      this.gl.bufferSubData(this.gl.UNIFORM_BUFFER, 0, newData);
      uniform.data.set(newData);
      uniform.lastUpdate = this.currentFrame;
    }
  }
  
  arraysEqual(a, b) {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  }
}
