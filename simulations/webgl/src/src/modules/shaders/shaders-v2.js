/**
 * Shader Management Module
 * Loads and manages all GLSL shaders for the FSCTF system
 */

// Store for all loaded shaders
const shaderCache = new Map();

/**
 * Load a shader from a separate file
 * @param {string} path - Path to the shader file
 * @returns {Promise<string>} The shader source code
 */
async function loadShader(path) {
  if (shaderCache.has(path)) {
    return shaderCache.get(path);
  }
  
  try {
    const response = await fetch(path);
    if (!response.ok) {
      throw new Error(`Failed to load shader: ${path}`);
    }
    const source = await response.text();
    shaderCache.set(path, source);
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
