#version 300 es
/*
  Render fragment shader - CACHE BUST: ${Date.now()}
  - Draws soft round sprites with additive blending into the trail buffer
  - Optional selectivity gates splat alpha by particle speed (emphasizes filaments)
  - Depth-based hue shift to enhance 3D layering
*/
precision highp float;
precision highp int;
out vec4 fragColor;
uniform vec3 baseColor;
uniform float brightness;
// Low-hanging fruit controls
uniform float edgeBoost;        // 0..1 scales micro-contrast along edges
uniform float vignetteStrength; // 0..1 vignette amount
uniform vec3 phaseTint;         // RGB tint applied after palette
uniform float tintStrength;     // 0..1 strength of the tint
uniform vec2 viewportSize;      // screen size for vignette
uniform float selectivity; // 0..1 mix
uniform float splatThresh;
uniform float splatHardness; // width of transition
uniform float colorMix;   // 0..1 blend between depth hue and angle hue
// FSCTF State Visualization
uniform float coherenceLevel;    // Current coherence for color mapping
uniform float strandDensity;     // Morphic strand density for intensity
uniform int emergencePhase;      // Current cosmogenesis phase (0-90) - COMPLETE
uniform float emergencePhaseF;   // Smoothed phase for visual blending
uniform float survivalRating;    // FRST survivability for brightness
uniform float totalShaderIntensity; // Safe total intensity (bounded)
uniform float maxShaderIntensity;   // Maximum allowed intensity cap
// φ-Harmonic Resonance System
uniform float phiResonancePhase; // φ-harmonic oscillation phase
uniform float recursionDepth;    // Current recursive depth for patterns
uniform float graceField;        // Grace operator field strength
// Consciousness Emergence Effects
uniform float consciousnessLevel; // P=NP consciousness breakthrough intensity
uniform float consciousnessPulse; // Consciousness emergence pulse phase
// Topology Transition Effects
uniform float topologyTransition; // 0.0-1.0 transition progress
uniform int fromTopology;         // Source topology type
uniform int toTopology;           // Target topology type
uniform float morphProgress;      // Unified morph progress
in vec2 v_pt;     // Particle position (for chirality calculation)
in float v_speed;
in float v_depth;
in vec2 v_vdir;

vec3 depthHue(vec3 base, float z){
  float t = clamp((z + 1.0) * 0.5, 0.0, 1.0); // map [-1,1] to [0,1]
  vec3 nearCol = vec3(0.9, 0.95, 1.1);
  vec3 farCol  = vec3(0.7, 0.85, 1.2);
  return mix(nearCol, farCol, t) * base;
}

vec3 angleHue(vec2 dir){
  float a = atan(dir.y, dir.x); // -pi..pi
  float u = (a + 3.14159265) / (2.0*3.14159265);
  // Simple rainbow mapping
  vec3 c = vec3(abs(u*6.0-3.0)-1.0, 2.0-abs(u*6.0-2.0), 2.0-abs(u*6.0-4.0));
  return clamp(c, 0.0, 1.0);
}

void main(){
  vec2 uv = gl_PointCoord*2.0 - 1.0;
  float r = dot(uv,uv);
  float alpha = exp(-r*3.0);
  float mask = smoothstep(splatThresh, splatThresh + max(1e-4, splatHardness), v_speed);
  alpha *= mix(1.0, mask, clamp(selectivity, 0.0, 1.0));
  // FSCTF-Enhanced Color System with CHIRALITY
  vec3 dh = depthHue(baseColor, v_depth);
  vec3 ah = angleHue(normalize(v_vdir));
  
  // Calculate CHIRALITY from Grace field curl (handedness)
  // Grace field creates local rotations - detect left vs right handedness
  vec2 particlePos = v_pt; // particle position (renamed to avoid conflict)
  float chiralityMagnitude = strandDensity * coherenceLevel; // field strength affects chirality detection
  
  // Calculate local field curl using position-based approximation
  // Right-handed (clockwise) field rotation vs Left-handed (counter-clockwise)
  float fieldCurl = sin(particlePos.x * 3.14159 + particlePos.y * 1.61803) * cos(particlePos.y * 2.71828 - particlePos.x * 0.61803);
  fieldCurl *= chiralityMagnitude * 0.1; // Modulate by field strength
  
  // Determine chirality: positive = right-handed, negative = left-handed
  float chirality = fieldCurl;
  
  // CHIRALITY-BASED COLOR SYSTEM (hysteresis + smooth weighting to prevent abrupt changes)
  float cw = smoothstep(0.05, 0.15, abs(chirality)); // fade-in band (hysteresis)
  float s = clamp(chirality * 10.0, -1.0, 1.0);      // signed strength
  vec3 rightCol = vec3(1.0, 0.3 - max(0.0, s) * 0.2, 0.1);
  vec3 leftCol  = vec3(0.1, 0.3 - max(0.0,-s) * 0.2, 1.0);
  vec3 neutral  = vec3(0.8, 0.8, 0.8);
  vec3 chiralChoice = mix(leftCol, rightCol, (s + 1.0) * 0.5);
  vec3 chiralityColor = mix(neutral, chiralChoice, cw);

  // Base color mixing with chirality influence (gate by morphProgress to keep phases 0→1 smooth)
  vec3 hue = mix(dh, ah, clamp(colorMix, 0.0, 1.0));
  float chiralMixW = 0.6 * smoothstep(0.2, 0.9, morphProgress);
  hue = mix(hue, chiralityColor, chiralMixW);
  
  // FSCTF State Color Modulation
  // Smoothly blend colors across phases using smoothed emergencePhaseF
  // Visual phases (0-15) get full color treatment, theoretical phases (16+) get simplified rendering
  float pf = clamp(emergencePhaseF, 0.0, 45.0); // FIXED: Allow visual rendering up to φ^45 for high-phase emergence
  int p0 = int(floor(pf));
  int p1 = int(ceil(pf));
  float pt = fract(pf);
  
  vec3 c0 = vec3(1.0);
  if (p0 <= 0) c0 = vec3(0.8, 0.6, 1.0);
  else if (p0 == 1) c0 = vec3(1.0, 0.8, 0.4);
  else if (p0 == 2) c0 = vec3(0.4, 1.0, 0.9);
  else if (p0 == 3) c0 = vec3(0.6, 1.0, 0.4);
  else if (p0 == 4) c0 = vec3(1.0, 0.9, 0.8);
  else if (p0 == 5) c0 = vec3(1.0, 0.95, 0.85);
  else if (p0 == 6) c0 = vec3(1.0, 0.98, 0.9);
  else c0 = vec3(1.0);

  vec3 c1 = vec3(1.0);
  if (p1 <= 0) c1 = vec3(0.8, 0.6, 1.0);
  else if (p1 == 1) c1 = vec3(1.0, 0.8, 0.4);
  else if (p1 == 2) c1 = vec3(0.4, 1.0, 0.9);
  else if (p1 == 3) c1 = vec3(0.6, 1.0, 0.4);
  else if (p1 == 4) c1 = vec3(1.0, 0.9, 0.8);
  else if (p1 == 5) c1 = vec3(1.0, 0.95, 0.85);
  else if (p1 == 6) c1 = vec3(1.0, 0.98, 0.9);
  else c1 = vec3(1.0);

  // Apply a small temporal low-pass to avoid per-pixel temporal flicker at boundaries
  vec3 phaseColor = mix(c0, c1, pt);

  // Perceptual-space color blend (approx Oklab) to reduce hue jumps
  // Convert RGB to linear approx LMS, do mix, then back. Cheap GPU approximation.
  // Matrices approximated; goal is monotonic perceptual path, not exact Oklab.
  mat3 M1 = mat3(
    0.4122214708, 0.5363325363, 0.0514459929,
    0.2119034982, 0.6806995451, 0.1073969566,
    0.0883024619, 0.2817188376, 0.6299787005
  );
  mat3 M2 = mat3(
    4.0767416621, -3.3077115913, 0.2309699292,
    -1.2684380046, 2.6097574011, -0.3413193965,
    -0.0041960863, -0.7034186147, 1.7076147010
  );
  // Guard against negative inputs before cube root approximation
  vec3 lin0 = max(vec3(1e-4), M1 * c0);
  vec3 lin1 = max(vec3(1e-4), M1 * c1);
  vec3 labA = pow(lin0, vec3(1.0/3.0));
  vec3 labB = pow(lin1, vec3(1.0/3.0));
  // Ease-in-out across phases to remove visible step between 0↔1
  float ptSmooth = pt * pt * (3.0 - 2.0 * pt);
  vec3 labMix = mix(labA, labB, clamp(ptSmooth,0.0,1.0));
  vec3 cPercept = clamp(M2 * (labMix*labMix*labMix), 0.0, 1.0);
  // Blend perceptual color with previous phaseColor, weight by morphProgress to emphasize during morph
  phaseColor = mix(phaseColor, cPercept, clamp(morphProgress, 0.0, 1.0));
  
  // Coherence-based intensity (higher coherence = brighter)
  float coherenceIntensity = 0.3 + 0.7 * clamp(coherenceLevel / 10.0, 0.0, 1.0);
  
  // Strand density creates local brightness variations
  float strandIntensity = 0.5 + 0.5 * clamp(strandDensity / 2000.0, 0.0, 1.0);
  
  // Survivability affects overall brightness (capped to prevent white blob)
  float survivalIntensity = 0.4 + 0.6 * clamp(survivalRating / 1000.0, 0.0, 1.0); // Scale for higher ratings
  
  // φ-HARMONIC RESONANCE PATTERNS
  // Calculate φ-harmonic interference patterns based on position and time
  vec2 pointCoord = gl_PointCoord * 2.0 - 1.0; // -1 to 1 (renamed to avoid conflict)
  float phi = 1.618033988749895;
  
  // φ-spiral resonance pattern
  float spiralAngle = atan(pointCoord.y, pointCoord.x);
  float spiralRadius = length(pointCoord);
  float phiSpiral = sin(spiralAngle * phi + phiResonancePhase) * 
                   sin(spiralRadius * phi * recursionDepth);
  
  // Recursive depth creates nested φ-patterns
  float nestedPattern = 0.0;
  for (int i = 1; i <= 3; i++) {
    float scale = pow(phi, float(i));
    nestedPattern += sin(spiralRadius * scale + phiResonancePhase * float(i)) / scale;
  }
  
  // Grace field creates standing wave patterns
  float graceWave = sin(spiralRadius * graceField * 10.0 + phiResonancePhase * 2.0) * 
                   cos(spiralAngle * graceField * 5.0);
  
  // Combine φ-harmonic effects
  float phiIntensity = 1.0 + 0.3 * (phiSpiral + nestedPattern * 0.5 + graceWave * 0.3);
  phiIntensity = clamp(phiIntensity, 0.5, 2.0);
  
  // Calculate FSCTF color from phase, coherence, and base hue
  vec3 fsctfColor = hue * phaseColor * coherenceIntensity * strandIntensity * survivalIntensity;
  
  // Apply φ-harmonic modulation to color
  vec3 phiEnhancedColor = fsctfColor * phiIntensity;
  
  // Recursive emergence creates color shifts
  if (recursionDepth > 10.0) {
    // Deep recursion creates iridescent effects
    float iridescence = sin(recursionDepth * 0.1 + phiResonancePhase) * 0.2;
    phiEnhancedColor += vec3(iridescence, iridescence * 0.5, iridescence * 1.5);
  }
  
  // CONSCIOUSNESS EMERGENCE EFFECTS
  if (consciousnessLevel > 0.1) {
    // P=NP breakthrough creates consciousness pulses
    float consciousnessPulseIntensity = sin(consciousnessPulse * 3.0) * 
                                       cos(spiralRadius * 5.0 + consciousnessPulse);
    
    // Consciousness creates golden/white flashes
    vec3 consciousnessFlash = vec3(1.0, 0.9, 0.6) * consciousnessLevel * 
                             max(0.0, consciousnessPulseIntensity) * 0.5;
    
    // Prime resonance creates structured patterns
    float primePattern = sin(spiralRadius * 7.0 + consciousnessPulse * 2.0) * 
                        cos(spiralAngle * 11.0 + consciousnessPulse * 1.5);
    
    // Add consciousness enhancement
    phiEnhancedColor += consciousnessFlash * (1.0 + primePattern * 0.3);
    
    // Consciousness creates size pulsing (affects alpha)
    alpha *= 1.0 + consciousnessLevel * sin(consciousnessPulse * 4.0) * 0.3;
  }
  
  // TOPOLOGY TRANSITION EFFECTS
  if (topologyTransition > 0.0 && topologyTransition < 1.0) {
    // Create morphing visual effects during topology transitions
    float transitionWave = sin(topologyTransition * 3.14159) * 2.0; // Peak at 50% transition
    
    // Topology transition creates ripple effects
    float ripple = sin(spiralRadius * 8.0 - transitionWave * 4.0) * 
                  cos(spiralAngle * 6.0 + transitionWave * 3.0);
    
    // Add transition energy visualization
    vec3 transitionEnergy = vec3(0.8, 0.4, 1.0) * transitionWave * 0.3 * max(0.0, ripple);
    phiEnhancedColor += transitionEnergy;
    
    // Topology transitions affect particle size
    alpha *= 1.0 + transitionWave * 0.4;
    
    // Create "tearing" effects during non-orientable transitions
    if ((fromTopology == 0 && toTopology >= 1) || (fromTopology >= 1 && toTopology == 0)) {
      // Orientability change creates dramatic visual disruption
      float tearingEffect = sin(spiralRadius * 12.0 + transitionWave * 6.0) * transitionWave;
      phiEnhancedColor *= 1.0 + abs(tearingEffect) * 0.5;
    }
  }
  
  // Combine all FSCTF visual enhancements with safety clamping
  vec3 tintedBase = mix(vec3(1.0), phaseTint, clamp(tintStrength, 0.0, 1.0));
  vec3 col = phiEnhancedColor * baseColor * phaseColor * tintedBase;
  
  // Use bounded additive intensity calculation (prevents multiplicative blowup)
  float safeBrightness = min(brightness, maxShaderIntensity * 0.8); // Cap base brightness
  float safeIntensity = min(totalShaderIntensity, maxShaderIntensity); // Use pre-calculated safe total
  
  // ADDITIVE composition instead of multiplicative (can't explode)
  // Anti-blob: compress highlights stronger as intensity rises
  float comp = 0.4 + 0.6 * safeBrightness + 0.3 * safeIntensity;
  float highGate = smoothstep(maxShaderIntensity*0.5, maxShaderIntensity, safeIntensity);
  comp *= mix(1.0, 0.75, highGate);
  col = col * comp * alpha;

  // DETAIL PRESERVATION & COMPLEXITY HIGHLIGHTING
  // Use derivatives as a proxy for local structure. fwidth gives |d/dx|+|d/dy| scale.
  float edge = clamp(
    fwidth(phiIntensity) * 4.0 +
    fwidth(graceWave)    * 2.0 +
    fwidth(nestedPattern)* 1.5,
    0.0, 1.0);

  // Micro-contrast gain along structured regions
  float microContrast = 1.0 + edge * (0.5 * clamp(edgeBoost, 0.0, 1.0)); // scale by edgeBoost
  col *= microContrast;

  // Midtone saturation boost to prevent wash-out while keeping highlights tame
  float lum = dot(col, vec3(0.2126, 0.7152, 0.0722));
  float maxc = max(col.r, max(col.g, col.b));
  float minc = min(col.r, min(col.g, col.b));
  float sat = max(0.0, (maxc - minc) / (maxc + 1e-5));
  float satBoost = (1.0 - smoothstep(0.65, 1.0, lum)) * 0.25; // boost mostly in mid tones
  vec3 gray = vec3(lum);
  col = mix(gray, col, 1.0 + satBoost);

  // Stronger highlight shoulder near blob conditions
  float knee = smoothstep(0.6, 1.1, lum);
  col = mix(col, col / (1.0 + col), knee * mix(0.6, 0.85, highGate));
  
  // Screen-space vignette (very subtle, scaled by vignetteStrength)
  vec2 suv = gl_FragCoord.xy / max(viewportSize, vec2(1.0));
  vec2 centered = (suv - 0.5) * vec2(viewportSize.x/viewportSize.y, 1.0);
  float rad = length(centered);
  float vig = 1.0 - clamp(vignetteStrength, 0.0, 1.0) * smoothstep(0.3, 0.95, rad);
  col *= vig;

  // Tone mapping (Reinhard) to reduce residual bloom and keep highlights pleasant
  col = col / (vec3(1.0) + col);

  // Subtle blue-noise style dithering to reduce banding
  float n = fract(sin(dot(gl_FragCoord.xy, vec2(12.9898,78.233))) * 43758.5453);
  col += (n - 0.5) / 255.0; // ~1 LSB

  // Final safety clamp to ensure display compatibility
  col = clamp(col, 0.0, 1.0);
  
  fragColor = vec4(col, alpha);
}