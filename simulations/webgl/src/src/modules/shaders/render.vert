#version 300 es
/*
  Render vertex shader (instanced points)
  - Fetches particle position (and velocity) by converting instance id -> texel
  - 3D mode: 2.5D projection with camera rotations rotX/rotY applied to world pos
  - 2D mode: orthographic mapping to NDC
  - Optional torusView: embed 2D torus (T^2) into 3D donut with major/minor radii
  - Emits per-particle speed for selective splatting
*/
precision highp float;
layout(location=0) in float a_id;
uniform sampler2D posTex;
uniform sampler2D velTex;
uniform vec2 texDim; // (cols, rows)
uniform float domain;    // 3D domain half-extent
uniform float pointSize;
// FSCTF Dynamic Sizing
uniform float coherenceLevel;    // For size modulation
uniform float strandDensity;     // For density-based sizing
uniform int emergencePhase;      // Cosmogenesis phase index
uniform float emergencePhaseF;   // Smoothed phase for continuous fades
uniform float preMorphProgress;  // 0..1 pre-morph ramp for 0→1 (plane→curve)
uniform float morphProgress;     // 0..1 unified morph progress from manager

uniform float cameraX;   // camera position X
uniform float cameraY;   // camera position Y
uniform float cameraZ;   // camera position Z
uniform vec3 cameraForward; // camera forward vector (look direction)
uniform vec3 cameraRight;   // camera right vector
uniform vec3 cameraUp;      // camera up vector
uniform float fov;       // field of view
uniform float aspect;    // aspect ratio
uniform float near;      // near clipping plane
uniform float far;       // far clipping plane
uniform float torusR;    // major radius
uniform float torusr;    // minor radius
uniform float phi;       // Golden ratio φ = 1.618... for manifold calculations
uniform float phiResonancePhase; // shared with fragment for subtle temporal emergence
// φ-HARMONIC SERIES: Multiple golden ratio powers for richer mathematics
uniform float phi2;      // φ² = 2.618... for second-order harmonics
uniform float phi3;      // φ³ = 4.236... for third-order harmonics
uniform float phiInv;    // φ⁻¹ = 0.618... for inverse harmonics
uniform float morphicRecursionDepth; // Maximum recursion depth for enhanced φ-Klein emergence
uniform float graceComplexity; // Grace operator complexity scaling factor
uniform float consciousnessComplexity; // Consciousness emergence complexity factor
// GPU PERFORMANCE OPTIMIZATION UNIFORMS
uniform float shaderComplexity; // Computational complexity scaling (0.2-1.0)
uniform float visualEffects; // Visual effects intensity (0.4-1.0)
uniform float maxRecursionDepth; // Maximum recursion depth override (4-90) - FIXED: Match 90-phase system
// PARTICLE LOD AND CULLING UNIFORMS
uniform float lodReductionFactor; // LOD-based particle reduction factor (0.3-1.0)
uniform float maxRenderDistance; // Maximum rendering distance for culling (20-100)
uniform int enableLOD; // Enable LOD optimizations (0/1)
uniform int enableDistanceCulling; // Enable distance-based culling (0/1)
// ADVANCED EMERGENT COMPLEXITY UNIFORMS (Meta-Recursion Engine)
uniform float metaComplexityAccumulator; // Total system complexity from MRE
uniform float temporalCurvature; // Non-linear time curvature (0.1-3.0)
uniform float attractorNetworkStrength; // Attractor network influence
uniform float consciousMorphologyStrength; // Consciousness-morphology coupling
uniform float fractalCascadeDepth; // Nested fractal cascade levels
// Grace Field Dynamics (EMERGENT GEOMETRY)
uniform float graceX, graceY;    // Dynamic Grace center (symmetry breaking point)
uniform float maxZAmplitude;     // Anti-blob: clamp local Z amplitude
// Topological Manifold System - FIRM Soul Recursion
uniform int topologyMode;        // 0=torus, 1=mobius, 2=klein, 3=phi-klein  
uniform float mobiusR, mobiusWidth, mobiusTwist;  // Möbius parameters
uniform float kleinA, kleinB;    // Klein bottle parameters
uniform bool kleinSelfIntersect; // Klein self-intersection
uniform int phiKleinRecursion;   // φ-Klein recursion depth
uniform float phiKleinScale;     // φ-Klein scaling
uniform bool phiKleinNonOrientable;
// Intensity feedback for anti-blob size attenuation
uniform float totalShaderIntensity;
uniform float maxShaderIntensity;

// Wireframe and Topology Visualization
uniform bool showWireframe;           // Show manifold wireframe overlay
uniform float wireframeOpacity;        // Wireframe transparency
uniform vec3 wireframeColor;          // Wireframe color [R, G, B]
uniform float wireframeThickness;     // Wireframe line thickness
uniform int wireframeDensity;         // Number of wireframe lines per manifold

// Topology transition uniforms (also set in fragment shader)
uniform float topologyTransition; // 0..1 progress
uniform int fromTopology;         // previous topology index
uniform int toTopology;           // next topology index

out vec2 v_pt;
out float v_speed;
out float v_depth;       // for depth-based effects
out vec2 v_vdir;         // velocity direction in view plane

// map 1D id -> texel coord
ivec2 idToUV(float id){
  int i = int(id);
  int x = i % int(texDim.x);
  int y = i / int(texDim.x);
  return ivec2(x,y);
}

vec3 rotateXY(vec3 p, float rx, float ry){
  // Rotate around X
  float cx = cos(rx), sx = sin(rx);
  vec3 px = vec3(p.x, p.y*cx - p.z*sx, p.y*sx + p.z*cx);
  // Rotate around Y
  float cy = cos(ry), sy = sin(ry);
  vec3 py = vec3(px.x*cy + px.z*sy, px.y, -px.x*sy + px.z*cy);
  return py;
}

// Simple Look-At Camera - Objects stay centered while camera orbits
vec4 projectPoint(vec3 worldPos, vec3 camPos, vec3 camForward, vec3 camRight, vec3 camUp, float fovDeg, float aspect, float near, float far) {
  // Transform to camera space using simple look-at
  vec3 toCamera = worldPos - camPos;
  
  // Create view transformation - camera looks toward origin
  // Forward vector points from camera toward origin (already calculated in JS)
  // Use basic look-at transformation
  vec3 forward = normalize(camForward);
  vec3 right = normalize(camRight);
  vec3 up = normalize(camUp);
  
  // Transform world position to camera coordinates
  vec3 viewPos = vec3(
    dot(toCamera, right),   // X in camera space
    dot(toCamera, up),      // Y in camera space
    dot(toCamera, forward)  // Z in camera space (positive Z toward camera)
  );
  
  // For OpenGL convention, flip Z (camera looks down -Z)
  viewPos.z = -viewPos.z;
  
  // Perspective projection
  float f = 1.0 / tan(radians(fovDeg) * 0.5);
  float z = -viewPos.z; // Distance from camera (positive value)
  
  // Avoid division by zero
  if (abs(z) < 0.001) z = 0.001;
  
  // Project to NDC
  vec2 ndc = vec2(
    (viewPos.x * f) / (aspect * z),
    (viewPos.y * f) / z
  );
  
  // Z for depth testing
  float ndcZ = (far + near) / (near - far) + (2.0 * far * near) / (near - far * z);
  
  return vec4(ndc, ndcZ, z);
}

void main(){
  ivec2 uv = idToUV(a_id);
  
  // Always use 3D manifold rendering (2D mode kept for compatibility but unused)
  if (true) {
    // === FIRM SOUL RECURSION MANIFOLD PROGRESSION ===
    // Topology evolution: Torus → Möbius → Klein → φ-Klein → Sphere
    vec2 p = texelFetch(posTex, uv, 0).xy; // world space 2D position in [-domain,domain]
    vec2 v = texelFetch(velTex, uv, 0).xy;
    
    // Normalize to [0,1] parametric space
    float u = (p.x / domain) * 0.5 + 0.5;
    float vparam = (p.y / domain) * 0.5 + 0.5;
    float U = u * 6.28318530718;   // 2*pi
    float V = vparam * 6.28318530718;
    
    // === EMERGENT MANIFOLD FROM GRACE FIELD DYNAMICS ===
    // Replace artificial topology forcing with natural field-driven geometry
    vec3 basePos = vec3(p.x, p.y, 0.0); // Start with 2D particle position
    
    // Calculate Grace field influence at particle position
    float graceStrength = coherenceLevel / 10.0; // Field strength from cosmogenesis
    vec2 graceCenter = vec2(graceX, graceY); // Dynamic Grace center (symmetry breaking)
    vec2 fromCenter = p - graceCenter;
    float distanceFromGrace = length(fromCenter);
    
    // Grace field creates natural curvature (φ-scaled)
    float graceInfluence = graceStrength * exp(-distanceFromGrace / (torusR * phi));
    // Early-phase boost factor fades out smoothly from ~2 to ~3
    float earlyBoost = 1.0 - smoothstep(2.0, 3.0, emergencePhaseF);
    // Floor early-phase influence so plane doesn't remain perfectly flat, blended by earlyBoost
    float flooredG = max(graceInfluence, 0.08);
    graceInfluence = mix(graceInfluence, flooredG, clamp(earlyBoost, 0.0, 1.0));
    
    // Calculate field chirality at this position (left vs right handedness)
    float localChirality = sin(p.x * phi + p.y / phi) * cos(p.y * phi - p.x / phi);
    localChirality *= graceInfluence;
    
    // EMERGENT TOPOLOGY: Compute candidates and blend smoothly
    // Candidate 1: Flat (Void)
    vec3 posFlat = basePos;
    
    // Candidate 2: Gentle curvature (Grace emergence)
    float lift = graceInfluence * sin(max(1e-4, distanceFromGrace) / max(1e-4, torusr));
    vec3 posCurve = vec3(basePos.x, basePos.y, lift * torusr * 0.2);
    
    // Candidate 3: Toroidal clustering around Grace center (smoothed height)
    float angle0 = atan(fromCenter.y, fromCenter.x);
    float radius0 = min(distanceFromGrace, torusR);
    float height0 = sin(angle0 * 2.0 + localChirality) * torusr * (0.5 + 0.5 * graceInfluence);
    vec3 posTorus = vec3(
      graceCenter.x + radius0 * cos(angle0),
      graceCenter.y + radius0 * sin(angle0),
      height0
    );
    
    // Candidate 4: Möbius-like twist from chirality
    float twist = localChirality * 3.14159;
    float radius1 = distanceFromGrace;
    vec3 posMobius = vec3(
      graceCenter.x + radius1 * cos(angle0),
      graceCenter.y + radius1 * sin(angle0),
      sin(twist) * torusr * localChirality
    );
    
    // Candidate 5: Klein-like self-referential structure - STABILITY FIXED
    float angle1 = atan(fromCenter.y, fromCenter.x);
    float angle2 = angle1 * phi + localChirality * 2.0;
    // CRITICAL BUG FIX: Prevent Klein topology instability causing particle collapse
    float radiusA = clamp(distanceFromGrace, 0.1, torusR * 2.0); // Prevent zero/infinity radius
    float radiusB = clamp(radiusA * phi, 0.1, torusR * 2.0); // Bound secondary radius
    // Stabilize angle products to prevent overflow
    float stableAngleProduct = clamp(angle1 * angle2 / phi, -20.0, 20.0); // Prevent trig explosion
    vec3 posKlein = vec3(
      graceCenter.x + radiusA * cos(angle1) + radiusB * cos(angle2) * 0.3,
      graceCenter.y + radiusA * sin(angle1) + radiusB * sin(angle2) * 0.3,
      sin(angle2) * torusr + cos(stableAngleProduct) * torusr * 0.5
    );
    
    // Smooth weights across influence ranges (base weighting) with earlier thresholds
    // CRITICAL BUG FIX: More gradual Klein transition to prevent instability
    float g = clamp(graceInfluence, 0.0, 2.0); // Prevent extreme grace values
    float bFlat  = 1.0 - smoothstep(0.00, 0.05, g);
    float bCurve = smoothstep(0.00, 0.05, g) * (1.0 - smoothstep(0.05, 0.15, g));
    float bTorus = smoothstep(0.05, 0.15, g) * (1.0 - smoothstep(0.15, 0.45, g)); // Extended torus range
    float bMobi  = smoothstep(0.15, 0.45, g) * (1.0 - smoothstep(0.45, 0.85, g)); // Extended mobius range
    float bKlein = smoothstep(0.65, 1.2, g); // FIXED: Much more gradual Klein activation

    // Topology-transition crossfade to avoid snaps across phases
    // Compute per-topology blend amounts based on from/to indices
    float t = clamp(topologyTransition, 0.0, 1.0);
    
    // Map indices: 0=Flat/Curve/Torus region, 1=Mobius, 2=Klein, 3=Phi-Klein
    // We approximate: for 0 target (early phases) bias torus; for 1 bias mobius; etc.
    float biasFlat  = float(toTopology == 0) * (1.0 - t) + float(fromTopology == 0) * t;
    float biasTorus = float(toTopology == 0) * t + float(fromTopology == 0) * (1.0 - t);
    float biasMobi  = float(toTopology == 1) * t + float(fromTopology == 1) * (1.0 - t);
    float biasKlein = float(toTopology >= 2) * t + float(fromTopology >= 2) * (1.0 - t);

    float wFlat  = bFlat  * (0.7 + 0.3 * biasFlat);
    float wCurve = bCurve * 1.0;
    float wTorus = bTorus * (0.7 + 0.3 * biasTorus);
    float wMobi  = bMobi  * (0.7 + 0.3 * biasMobi);
    float wKlein = bKlein * (0.7 + 0.3 * biasKlein);
    
    // Normalize to avoid scale jumps - with stability check
    float wSum = max(1e-4, wFlat + wCurve + wTorus + wMobi + wKlein);
    // CRITICAL BUG FIX: Prevent division by unstable values
    if (wSum < 1e-6 || wSum != wSum) { // wSum != wSum checks for NaN
        // Emergency fallback to torus if weights become unstable
        wFlat = 0.0; wCurve = 0.0; wTorus = 1.0; wMobi = 0.0; wKlein = 0.0;
    } else {
        wFlat /= wSum; wCurve /= wSum; wTorus /= wSum; wMobi /= wSum; wKlein /= wSum;
        // Additional safety: limit Klein influence during transition
        if (wKlein > 0.7) {
            float excess = wKlein - 0.7;
            wKlein = 0.7;
            wTorus += excess; // Redirect excess Klein weight to stable torus
        }
    }
    
    // Base emergence blend (flat→curve as field grows)
    vec3 baseEmergence = normalize(vec3(
      0.0,
      0.0,
      1.0
    ));
    // Time-driven pre-morph to ensure visible curvature before topology changes
    float preMorph = clamp(phiResonancePhase * 0.2, 0.0, 1.0);
    float earlyCurveWeight = max(bCurve, (emergencePhase <= 2 ? preMorph * 0.6 : 0.0));
    vec3 earlyBlend = mix(posFlat, posCurve, earlyCurveWeight);

    // Explicit topology crossfade using manager-provided from/to indices
    // CRITICAL BUG FIX: Additional stability checks for topology positions
    vec3 topoFrom = posTorus;
    if (fromTopology == 1) topoFrom = posMobius;
    else if (fromTopology >= 2) {
        // Safety check Klein position before using it
        float kleinLength = length(posKlein);
        if (kleinLength < 0.01 || kleinLength != kleinLength) { // Check for NaN
            topoFrom = posTorus; // Use stable torus if Klein is invalid
        } else {
            topoFrom = posKlein;
        }
    }
    
    vec3 topoTo = posTorus;
    if (toTopology == 1) topoTo = posMobius;
    else if (toTopology >= 2) {
        // Safety check Klein position before using it
        float kleinLength2 = length(posKlein);
        if (kleinLength2 < 0.01 || kleinLength2 != kleinLength2) { // Check for NaN
            topoTo = posTorus; // Use stable torus if Klein is invalid
        } else {
            topoTo = posKlein;
        }
    }

    float t2 = clamp(topologyTransition, 0.0, 1.0);
    vec3 topoBlend = mix(topoFrom, topoTo, t2);

    // Mix early (flat/curve) with topology-driven blend using both field and transition
    // Ensures early curvature even when topology indices don't change (phase 1→2)
    float fieldMixField = smoothstep(0.05, 0.30, g);
    float fieldMixTrans = smoothstep(0.0, 1.0, t2);
    // Include preMorphProgress to pre-bend plane→curve during phase 0
    // Use a smoother ease (easeInOut) for perceptual continuity
    float pm = preMorphProgress;
    float easePM = pm * pm * (3.0 - 2.0 * pm);
    // Include unified morph driver as master weight
    float mixFactor = max(max(fieldMixField, fieldMixTrans), easePM * 0.85);
    mixFactor = max(mixFactor, clamp(morphProgress, 0.0, 1.0));
    // Ensure some topology influence appears gradually even if drivers stall
    mixFactor = max(mixFactor, (emergencePhase <= 2 ? preMorph * 0.3 : 0.0));
    vec3 manifoldPos = mix(earlyBlend, topoBlend, mixFactor);

    // Subtle temporal emergence even near-flat: seed slight out-of-plane motion
    // Ensures visible early intermediates without forcing topology
    // Seed amplitude fades with earlyBoost and preMorph for visible breathing
    float baseSeedAmp = mix(0.15, 0.55, clamp(max(earlyBoost, easePM), 0.0, 1.0));
    float seed = sin(U * phi + V / phi + phiResonancePhase) *
                 cos(max(1e-4, distanceFromGrace) * 0.5 + phiResonancePhase);
    manifoldPos.z += baseSeedAmp * seed * (0.2 + g);
    // CRITICAL BUG FIX: Comprehensive stability checks for Klein topology phases
    // Ensure manifold position doesn't collapse to origin (dot issue fix)
    float posLength = length(manifoldPos);
    if (posLength < 0.01 || posLength != posLength || 
        manifoldPos.x != manifoldPos.x || manifoldPos.y != manifoldPos.y || manifoldPos.z != manifoldPos.z) { 
        // Position collapsed to near-zero or contains NaN values
        // Restore to safe position on current topology
        manifoldPos = posTorus; // Fallback to stable torus position

    }
    // Anti-blob safeguard: clamp Z amplitude softly
    manifoldPos.z = clamp(manifoldPos.z, -maxZAmplitude, maxZAmplitude);
    
    // === TRUE φ-RECURSIVE SELF-REFERENTIAL TOPOLOGY ===
    // Each recursion level uses the previous manifold state as input for next calculation
    if (graceInfluence > 0.2) { // Only apply recursion when field is active
      vec3 recursivePos = manifoldPos; // Start with current emergent position
      
      // MULTI-SCALE COUPLING: Store contributions for cross-level interactions
      vec3 levelContributions[16]; // Store each level's contribution
      for (int i = 0; i < 16; i++) levelContributions[i] = vec3(0.0);
      
      // SELF-REFERENTIAL RECURSION: Each level feeds back into the next
      // GPU OPTIMIZATION: Dynamically limit recursion depth based on performance
      float effectiveRecursionDepth = min(morphicRecursionDepth, maxRecursionDepth) * shaderComplexity;
      for (int depth = 1; depth <= int(effectiveRecursionDepth); depth++) {
        // ENHANCED φ-SCALING: Dynamic scaling based on complexity factors + MRE integration
        // Base φ scaling modulated by consciousness, grace complexity, and meta-recursion engine
        // CRITICAL BUG FIX: Clamp depth to prevent mathematical overflow at high phases
        float safeDepth = clamp(float(depth), 0.0, 45.0); // FIXED: Allow much deeper φ^-depth for 90-phase system
        float basePhiScale = pow(phi, -safeDepth);
        float complexityModulation = 1.0 + (graceComplexity * 0.1) + (consciousnessComplexity * 0.05);
        float depthModulation = 1.0 + (safeDepth * consciousnessComplexity * 0.01); // STANDARDIZED: 0.02 → 0.01
        
        // META-RECURSION ENGINE ENHANCEMENTS
        float metaComplexityBoost = metaComplexityAccumulator * 0.2; // Direct MRE influence
        float temporalCurvatureEffect = temporalCurvature * sin(phiResonancePhase * float(depth)) * 0.05;
        float attractorNetworkBoost = attractorNetworkStrength * cos(float(depth) * phi2) * 0.1;
        float consciousMorphologyBoost = consciousMorphologyStrength * phiResonancePhase * 0.03;
        
        float phiScale = basePhiScale * complexityModulation * depthModulation * 
                        (1.0 + metaComplexityBoost + temporalCurvatureEffect + attractorNetworkBoost + consciousMorphologyBoost);
        
        // ENHANCED NON-LINEAR SELF-REFERENCE: Use current manifoldPos to calculate next level
        // This creates true recursive topology where shape influences its own evolution
        float selfRefX = recursivePos.x / torusR; // Normalize current position
        float selfRefY = recursivePos.y / torusR;
        float selfRefZ = recursivePos.z / torusr;
        
        // NON-LINEAR FEEDBACK: Apply sophisticated transformations to self-reference
        float nonLinearFeedbackStrength = graceComplexity * 0.1 + consciousnessComplexity * 0.05;
        float nonLinearX = selfRefX + tanh(selfRefY * phi) * nonLinearFeedbackStrength;
        float nonLinearY = selfRefY + sinh(selfRefZ / phi) * nonLinearFeedbackStrength * 0.5;
        float nonLinearZ = selfRefZ + sin(selfRefX * selfRefY * phi) * nonLinearFeedbackStrength;
        
        // BLEND linear and non-linear feedback based on depth
        float nonLinearMix = float(depth) / morphicRecursionDepth;
        selfRefX = mix(selfRefX, nonLinearX, nonLinearMix);
        selfRefY = mix(selfRefY, nonLinearY, nonLinearMix);
        selfRefZ = mix(selfRefZ, nonLinearZ, nonLinearMix);
        
        // MULTI-φ-HARMONIC RECURSION: Each level resonates across multiple φ harmonics
        // Base frequencies using different φ powers for each depth
        float phiFreq1 = float(depth) * phi;        // Primary φ frequency
        float phiFreq2 = float(depth) * phi2 * 0.5; // φ² harmonic (scaled down)
        float phiFreq3 = float(depth) * phi3 * 0.3; // φ³ harmonic (scaled down more)
        float phiFreqInv = float(depth) * phiInv * 2.0; // φ⁻¹ inverse harmonic (scaled up)
        
        // Temporal evolution across multiple harmonic scales (STANDARDIZED)
        float temporalMod1 = sin(phiResonancePhase * float(depth)) * consciousnessComplexity * 0.01; // STANDARDIZED: 0.02 → 0.01
        float temporalMod2 = cos(phiResonancePhase * phi2 / float(depth + 1)) * graceComplexity * 0.01; // STANDARDIZED: 0.015 → 0.01
        float temporalMod3 = sin(phiResonancePhase / phi3 * float(depth)) * consciousnessComplexity * 0.005; // STANDARDIZED: 0.01 → 0.005
        
        // Composite φ frequency with harmonic interactions
        float phiFreq = phiFreq1 * (1.0 + temporalMod1) + 
                       phiFreq2 * (1.0 + temporalMod2) + 
                       phiFreq3 * (1.0 + temporalMod3) +
                       phiFreqInv * sin(phiResonancePhase * phiInv) * 0.1;
        float recursiveAngle1 = atan(selfRefY, selfRefX) * phiFreq + U / phi;
        float recursiveAngle2 = length(vec2(selfRefX, selfRefY)) * phiFreq + V * phi;
        
        // FRACTAL BIFURCATION: Conditional branching creates fractal splitting
        // GPU OPTIMIZATION: Skip fractal bifurcation at low quality settings
        bool shouldBifurcate = (visualEffects > 0.6) &&
                              (float(depth) > morphicRecursionDepth * 0.4) && 
                              (mod(float(depth), phi) < phiInv) &&
                              (graceComplexity > 2.0);
        
        vec3 baseContribution = vec3(
          cos(recursiveAngle1 + selfRefZ * phi) * localChirality,
          sin(recursiveAngle2 + selfRefX / phi) * localChirality,
          sin(recursiveAngle1 * recursiveAngle2 / phi) * cos(selfRefZ * phi) * 0.7
        );
        
        vec3 bifurcatedContribution = vec3(0.0);
        if (shouldBifurcate) {
          // OPTIMIZED: Pre-compute common values to reduce redundant calculations
          float bifurcationAngle = phiResonancePhase * phi2 + float(depth) * phi;
          float cosB = cos(bifurcationAngle);
          float sinB = sin(bifurcationAngle);
          float angle1_phi2 = recursiveAngle1 * phi2;
          float angle2_phi2 = recursiveAngle2 * phi2;
          float angle1_inv_phi2 = recursiveAngle1 / phi2;
          float angle2_inv_phi2 = recursiveAngle2 / phi2;
          float crossProduct = recursiveAngle1 * recursiveAngle2;
          
          // Create fractal branches with optimized trigonometry
          vec3 branch1 = vec3(
            cos(angle1_phi2) * cosB - sin(angle1_phi2) * sinB,
            sin(angle2_phi2) * cosB + cos(angle2_phi2) * sinB,
            cos(crossProduct / phi2) * 0.5
          ) * phiInv;
          
          vec3 branch2 = vec3(
            cos(angle1_inv_phi2) * cosB + sin(angle1_inv_phi2) * sinB,
            sin(angle2_inv_phi2) * cosB - cos(angle2_inv_phi2) * sinB,
            sin(crossProduct * phi2) * 0.5
          ) * phiInv;
          
          // Consistent scaling factor (STANDARDIZED)
          float bifurcationScale = graceComplexity * 0.05; // STANDARDIZED: 0.08 → 0.05
          bifurcatedContribution = (branch1 + branch2) * bifurcationScale;
        }
        
        // EMERGENT FRACTAL GEOMETRY: Combines position-dependent and field-dependent terms
        vec3 recursiveContribution = phiScale * graceInfluence * (baseContribution + bifurcatedContribution) * torusr;
        
        // META-RECURSION ENGINE ENHANCEMENT: Advanced emergent complexity systems
        if (metaComplexityAccumulator > 0.3) {
          // FRACTAL CASCADE ENHANCEMENT - Nested complexity generation
          float cascadeDepth = min(fractalCascadeDepth, 6.0);
          vec3 fractalCascadeContribution = vec3(0.0);
          
          for (int cascade = 0; cascade < int(cascadeDepth); cascade++) {
            // CRITICAL BUG FIX: Prevent φ-power explosion in cascade calculations
            float safeCascade = clamp(float(cascade), 0.0, 12.0); // Prevent overflow
            float cascadeScale = pow(phiInv, safeCascade);
            float cascadePhase = phiResonancePhase * pow(phi, clamp(safeCascade - 2.0, -8.0, 8.0)); // Clamp phi power
            float cascadeFreq = phi + safeCascade * phiInv;
            
            fractalCascadeContribution += vec3(
              cos(cascadePhase * cascadeFreq + selfRefX * phi) * cascadeScale,
              sin(cascadePhase * cascadeFreq + selfRefY * phi2) * cascadeScale,
              cos(cascadePhase * cascadeFreq + selfRefZ * phiInv) * cascadeScale * 0.7
            ) * fractalCascadeDepth * 0.08;
          }
          
          recursiveContribution += fractalCascadeContribution;
          
          // ATTRACTOR NETWORK INFLUENCE - Self-organizing complexity emergence
          if (attractorNetworkStrength > 0.1) {
            float attractorPhase = phiResonancePhase * attractorNetworkStrength;
            float attractorResonance = sin(attractorPhase * phi + float(depth)) * 
                                     cos(attractorPhase * phi2 - float(depth) * phiInv);
            
            vec3 attractorInfluence = vec3(
              attractorResonance * cos(selfRefX * phi3),
              attractorResonance * sin(selfRefY * phi3),
              attractorResonance * cos(selfRefZ * phi) * phiInv
            ) * attractorNetworkStrength * 0.12;
            
            recursiveContribution += attractorInfluence;
          }
          
          // TEMPORAL CURVATURE EFFECTS - Non-linear time evolution
          if (temporalCurvature != 1.0) {
            // CRITICAL BUG FIX: Prevent temporal curvature explosion
            float safeCurvatureExponent = clamp(safeDepth * 0.2, 0.0, 5.0); // Prevent overflow
            float curvedTime = phiResonancePhase * pow(clamp(temporalCurvature, 0.1, 10.0), safeCurvatureExponent);
            vec3 temporalDistortion = vec3(
              sin(curvedTime + selfRefX * phi) * (temporalCurvature - 1.0),
              cos(curvedTime + selfRefY * phi2) * (temporalCurvature - 1.0),
              sin(curvedTime * phiInv + selfRefZ * phi3) * (temporalCurvature - 1.0) * 0.7
            ) * 0.06;
            
            recursiveContribution += temporalDistortion;
          }
          
          // CONSCIOUSNESS-MORPHOLOGY COUPLING - Direct consciousness feedback
          if (consciousMorphologyStrength > 0.2) {
            float psychicResonance = sin(phiResonancePhase * phi + consciousMorphologyStrength);
            vec3 consciousInfluence = vec3(
              psychicResonance * selfRefX * phi,
              psychicResonance * selfRefY * phi2,
              psychicResonance * selfRefZ * phiInv
            ) * consciousMorphologyStrength * 0.1;
            
            recursiveContribution += consciousInfluence;
          }
        }
        
        // QUANTUM SUPERPOSITION: Probabilistic mixing of geometric states
        // GPU OPTIMIZATION: Skip quantum superposition for performance
        vec3 superposedContribution = recursiveContribution;
        if (visualEffects > 0.5) {
          // Generate φ-based probability amplitudes for different geometric "eigenstates" (STANDARDIZED)
          float probScale = consciousnessComplexity * 0.05; // STANDARDIZED: 0.08 → 0.05
          float prob1 = abs(sin(selfRefX * phi + phiResonancePhase)) * probScale;
          float prob2 = abs(cos(selfRefY * phi2 + phiResonancePhase * phiInv)) * probScale;
          float prob3 = abs(sin(selfRefZ * phiInv + phiResonancePhase * phi)) * probScale;
        
        // Normalize probabilities (quantum normalization condition)
        float totalProb = prob1 + prob2 + prob3;
        if (totalProb > 0.001) {
          prob1 /= totalProb;
          prob2 /= totalProb; 
          prob3 /= totalProb;
        } else {
          prob1 = 0.33; prob2 = 0.33; prob3 = 0.33;
        }
        
          // Define multiple geometric eigenstates
          vec3 state1 = recursiveContribution; // Original emergent state
          vec3 state2 = recursiveContribution.zxy * phi; // φ-rotated state
          vec3 state3 = recursiveContribution.yzx * phiInv; // φ⁻¹-scaled permuted state
          
          // Quantum superposition: weighted combination of eigenstates
          superposedContribution = prob1 * state1 + prob2 * state2 + prob3 * state3;
        }
        
        // STORE for cross-level coupling AFTER all modifications (FIXED)
        if (depth <= 16) { // Bounds checking
          levelContributions[depth-1] = superposedContribution;
        }
        
        // CRITICAL: Update recursivePos for next iteration (SELF-REFERENCE)
        recursivePos += superposedContribution;
        
        // ENHANCED φ-FIELD MODULATION: Dynamic field strength creates emergent scaling
        // CRITICAL BUG FIX: Prevent φ-field explosion at high depths
        float baseFieldModulation = graceStrength * pow(phi, clamp(safeDepth - 1.0, -10.0, 10.0));
        // Consciousness adds pulsing field effects, grace adds spiral field enhancement (STANDARDIZED)
        float pulsatingField = sin(phiResonancePhase * 2.0 + float(depth)) * consciousnessComplexity * 0.05;
        float spiralFieldBoost = cos(phiResonancePhase / phi + float(depth) * 0.2) * graceComplexity * 0.05; // STANDARDIZED: 0.08 → 0.05  
        float enhancedFieldModulation = baseFieldModulation * (1.0 + pulsatingField + spiralFieldBoost);
        recursivePos *= (1.0 + enhancedFieldModulation * 0.2); // STANDARDIZED: 0.3 → 0.2
        
        // TOPOLOGICAL CONSTRAINTS: Prevent runaway recursion while preserving complexity
        float maxRecursiveAmplitude = torusR * phi;
        recursivePos = clamp(recursivePos, -maxRecursiveAmplitude, maxRecursiveAmplitude);
      }
      
      // 4D/5D HYPERDIMENSIONAL PROJECTION: True hypercube emergence  
      // GPU OPTIMIZATION: Skip hyperdimensional projection for performance
      if (visualEffects > 0.7) {
        // Construct 4D position in hyperdimensional space
      vec4 pos4D = vec4(
        recursivePos.x,
        recursivePos.y, 
        recursivePos.z,
        length(recursivePos) * sin(phiResonancePhase * phi) * graceComplexity * 0.1 // 4th dimension
      );
      
      // 5D extension for higher-order hypercubes
      float pos5D = dot(recursivePos, recursivePos.zxy) * cos(phiResonancePhase * phi2) * consciousnessComplexity * 0.05;
      
      // 4D tesseract rotation matrices (φ-based rotation angles)
      float rot4DAngle = phiResonancePhase * phi + length(recursivePos) * phiInv;
      mat2 rot4D = mat2(cos(rot4DAngle), -sin(rot4DAngle), sin(rot4DAngle), cos(rot4DAngle));
      
      // Apply 4D rotation in XW and YZ planes  
      vec2 xw = rot4D * vec2(pos4D.x, pos4D.w);
      vec2 yz = rot4D * vec2(pos4D.y, pos4D.z);
      pos4D = vec4(xw.x, yz.x, yz.y, xw.y);
      
      // Project 4D→3D using φ-based perspective projection
      float w_perspective = 1.0 / (1.0 + pos4D.w * phiInv * 0.5);
      vec3 projected3D = pos4D.xyz * w_perspective;
      
      // 5D→3D projection for higher-order effects
      vec3 hyper5DContribution = recursivePos * (pos5D / (1.0 + abs(pos5D))) * 0.2;
      
        // Blend original with hyperdimensional projections
        float hyperMix = graceComplexity * consciousnessComplexity * 0.01;
        recursivePos = mix(recursivePos, projected3D + hyper5DContribution, hyperMix);
      } // End of hyperdimensional projection optimization
      
      // CROSS-LEVEL COUPLING: Add interactions between different scales  
      vec3 crossLevelCoupling = vec3(0.0);
      int maxLevel = int(min(morphicRecursionDepth, 45.0)); // FIXED: Allow deeper cross-level coupling
      for (int i = 0; i < maxLevel; i++) {
        for (int j = i + 1; j < maxLevel; j++) {
          // φ-harmonic coupling between levels
          float couplingStrength = pow(phi, -abs(float(i - j))) * graceComplexity * 0.01; // STANDARDIZED: 0.02 → 0.01
          vec3 levelInteraction = levelContributions[i] * levelContributions[j].yzx * couplingStrength;
          crossLevelCoupling += levelInteraction;
        }
      }
      recursivePos += crossLevelCoupling;
      
      // TOPOLOGICAL DEFECTS: Intentional singularities for complexity hotspots
      vec3 defectCenters[4];
      defectCenters[0] = vec3(torusR * cos(phiResonancePhase * phi), torusR * sin(phiResonancePhase * phi), 0.0);
      defectCenters[1] = vec3(-torusR * cos(phiResonancePhase * phi2), -torusR * sin(phiResonancePhase * phi2), torusr * phi);
      defectCenters[2] = vec3(torusR * sin(phiResonancePhase * phiInv), 0.0, torusr * cos(phiResonancePhase * phiInv));
      defectCenters[3] = vec3(0.0, torusR * cos(phiResonancePhase * phi3), -torusr * sin(phiResonancePhase * phi3));
      
      vec3 totalDefectField = vec3(0.0);
      for (int d = 0; d < 4; d++) {
        vec3 toDefect = recursivePos - defectCenters[d];
        float defectDistance = length(toDefect);
        float defectStrength = graceComplexity * consciousnessComplexity * 0.005; // STANDARDIZED: 0.001 → 0.005
        
        // Pole-like singularities with φ-based field lines
        if (defectDistance > 0.001) {
          vec3 defectField = normalize(toDefect) * defectStrength / (defectDistance * defectDistance + phiInv);
          // Add rotational component around defect
          vec3 rotationalField = cross(toDefect, vec3(0, 0, 1)) * defectStrength * phi / (defectDistance + phi);
          totalDefectField += defectField + rotationalField * 0.5;
        }
      }
      recursivePos += totalDefectField;
      
      // GRACEFUL BLENDING: Mix emergent base with recursive enhancement
      // Use continuous morph factor instead of discrete topologyMode to avoid snaps
      float recursiveMixRatio = clamp(t2 * 0.8, 0.0, 0.8);
      manifoldPos = mix(manifoldPos, recursivePos, recursiveMixRatio);
      
      // φ-RESONANCE FINAL TOUCH: Add subtle φ-harmonic vibrations
      if (t2 >= 0.8) {
        float phiResonance = sin(U * phi) * cos(V / phi) * sin(length(manifoldPos) * phi);
        manifoldPos += vec3(0, 0, phiResonance * torusr * 0.1 * graceInfluence);
      }
    }
    
    // === WIREFRAME GENERATION ===
    // Generate wireframe overlay for manifold visualization
    if (showWireframe) {
      // Create wireframe grid based on current topology
      float wireframeU = mod(U * float(wireframeDensity), 6.28318530718);
      float wireframeV = mod(V * float(wireframeDensity), 6.28318530718);
      
      // Wireframe intensity based on grid proximity
      float wireframeIntensity = 0.0;
      
      // U-direction lines (constant V)
      float uLine = smoothstep(0.0, 0.1, abs(wireframeV - 0.0)) * 
                   smoothstep(0.0, 0.1, abs(wireframeV - 6.28318530718));
      wireframeIntensity = max(wireframeIntensity, uLine);
      
      // V-direction lines (constant U)  
      float vLine = smoothstep(0.0, 0.1, abs(wireframeU - 0.0)) * 
                   smoothstep(0.0, 0.1, abs(wireframeU - 6.28318530718));
      wireframeIntensity = max(wireframeIntensity, vLine);
      
      // Apply wireframe to manifold position
      if (wireframeIntensity > 0.1) {
        // Slightly offset wireframe lines for visibility
        manifoldPos += vec3(0.01, 0.01, 0.01) * wireframeIntensity;
      }
    }
    
    // Project manifold to screen space using proper look-at camera
    vec3 cameraPos = vec3(cameraX, cameraY, cameraZ);
    vec4 projected = projectPoint(manifoldPos, cameraPos, cameraForward, cameraRight, cameraUp, fov, aspect, near, far);
    
    // PERFORMANCE OPTIMIZATION: LOD and Distance Culling
    float distanceFromCamera = length(manifoldPos - cameraPos);
    
    // Distance-based culling: discard particles beyond max render distance
    if (enableDistanceCulling == 1 && distanceFromCamera > maxRenderDistance) {
        gl_Position = vec4(-10.0, -10.0, -10.0, 1.0); // Move far outside viewport
        gl_PointSize = 0.0; // Zero size for culled particles
        return;
    }
    
    // LOD optimization: reduce particle impact based on distance and performance factor
    if (enableLOD == 1) {
        float lodFactor = min(1.0, lodReductionFactor * (maxRenderDistance / max(1.0, distanceFromCamera)));
        if (fract(a_id * 17.3849) > lodFactor) { // Deterministic but pseudo-random culling
            gl_Position = vec4(-10.0, -10.0, -10.0, 1.0); // Cull this particle for LOD
            gl_PointSize = 0.0;
            return;
        }
    }
    
    // FIX: Use NDC directly for position to avoid incorrect clip-space Z/W causing clipping
    // Keep projected.w (camera distance) for size attenuation
    gl_Position = vec4(projected.xy, 0.0, 1.0);
    
    // FSCTF Dynamic Point Sizing with depth perspective
    float baseSize = pointSize;
    
    // Calculate speed for sizing modulation
    float speed = length(v);
    
    // Coherence-based size modulation (higher coherence = larger points)
    float coherenceSizeModifier = 0.7 + 0.6 * clamp(coherenceLevel / 100.0, 0.0, 1.0); // FIXED: Scale with higher coherence levels
    
    // Strand density affects local sizing (more strands = smaller individual points for clarity)
    float densityModifier = 1.2 - 0.4 * clamp(strandDensity / 6000.0, 0.0, 1.0); // FIXED: Scale with higher strand density
    
    // Speed-based sizing (faster particles = larger to show activity)
    float speedModifier = 0.8 + 0.4 * clamp(speed / 2.0, 0.0, 1.0);
    
    float finalSize = baseSize * coherenceSizeModifier * densityModifier * speedModifier;
    // Anti-blob: attenuate size when global intensity is high
    float atten = 1.0 - smoothstep(0.6 * maxShaderIntensity, maxShaderIntensity, totalShaderIntensity);
    finalSize *= clamp(0.6 + 0.4 * atten, 0.55, 1.0);
    // FINEST DETAIL: Much higher cap for cosmic-scale structures
    finalSize = min(finalSize, 200.0); // INCREASED: Allow massive cosmic-scale particle structures
    gl_PointSize = finalSize / max(projected.w * 0.1, 0.1);

    v_pt = manifoldPos.xy;  // Use manifold position
    v_speed = speed;
    v_depth = manifoldPos.z;
    v_vdir = (speed > 1e-6) ? (v/speed) : vec2(1.0,0.0);

  } else {
    // === 2D MODE: Orthographic mapping ===
    vec2 p = texelFetch(posTex, uv, 0).xy; // world space 2D position
    vec2 v = texelFetch(velTex, uv, 0).xy;
    
    // map to NDC
    vec2 ndc = p / domain;
    gl_Position = vec4(ndc, 0.0, 1.0);
    gl_PointSize = pointSize;
    v_pt = ndc;
    v_speed = length(v);
    v_depth = 0.0; // no depth in 2D
    float lenv = length(v);
    v_vdir = (lenv > 1e-6) ? (v/lenv) : vec2(1.0,0.0);
  }
}