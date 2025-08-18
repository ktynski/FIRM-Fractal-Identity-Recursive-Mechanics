#version 300 es
/*
  Simulation fragment shader
  - Runs twice per frame via ping-pong: once for velocity (passId=1) then for position (passId=0)
  - State layout: posTex.xy = position (world units), velTex.xy = velocity (world units per sec)
  - Field: curlNoise over 3D, sampled on z=0 plane for 2D simulation
  - Update: Langevin-like step with damping and additive Gaussian-ish noise
  - Boundary: toroidal wrap in world coordinates
*/
precision highp float;
layout(location=0) out vec4 out0;
in vec2 v_uv;

uniform sampler2D posTex;
uniform sampler2D velTex;
uniform vec2 resolution; // texture size
uniform float dt;
uniform float time;
uniform float domain;         // 3D domain half-extent
uniform float k_flow, k_attract, k_burst;
uniform float damping, jitterSigma;
uniform float fieldScale, timeScale;
uniform vec3 burstCenter;     // 3D burst center
uniform float burstAmp, burstFreq;
uniform int passId; // 0 pos, 1 vel

// FSCTF extensions
uniform float graceAmp;        // 0..1 entropy suppression
uniform vec3  graceCenter;     // 3D grace seed center
uniform float graceRadius;     // radius of influence (world units)
uniform float devourerAmp;     // 0..1 anti-coherent perturbation
uniform float reflectMix;      // 0..1 blend with mirrored field
uniform float morphicCouple;   // cross coupling strength (reserved)
uniform float nullFlow;        // 0..1 enable null-flow control condition


// Multi-scale φ ladder
uniform int   nScales;         // <= 4
uniform float baseScale;       // s0
uniform float phi;             // 1.61803398875
uniform float reflectDelta;    // time offset for mirrored field

#include "noise.glsl"

// Perpendicular helper
vec2 perp(vec2 v){ return vec2(-v.y, v.x); }

// Multi-scale φ-ladder flow - FULL 3D VERSION
uniform float w0, w1, w2, w3; // weights per scale
vec3 multiFlow3D(vec3 p, float t, bool isCurl) {
  vec3 f = vec3(0.0);
  float s = baseScale;
  
  if (nScales >= 1) { vec3 u0 = curlNoise(p * s, t, isCurl); f += w0 * u0; s *= phi; }
  if (nScales >= 2) { vec3 u1 = curlNoise(p * s, t + 0.1, isCurl); f += w1 * u1; s *= phi; }
  if (nScales >= 3) { vec3 u2 = curlNoise(p * s, t + 0.2, isCurl); f += w2 * u2; s *= phi; }
  if (nScales >= 4) { vec3 u3 = curlNoise(p * s, t + 0.3, isCurl); f += w3 * u3; }
  return f;
}

// Legacy 2D version for compatibility
vec2 multiFlow2D(vec2 p, float t, bool isCurl) {
  vec2 f = vec2(0.0);
  float s = baseScale;
  if (nScales >= 1) { vec3 u0 = curlNoise(vec3(p * s, 0.0), t, isCurl); f += w0 * u0.xy; s *= phi; }
  if (nScales >= 2) { vec3 u1 = curlNoise(vec3(p * s, 0.0), t, isCurl); f += w1 * u1.xy; s *= phi; }
  if (nScales >= 3) { vec3 u2 = curlNoise(vec3(p * s, 0.0), t, isCurl); f += w2 * u2.xy; s *= phi; }
  if (nScales >= 4) { vec3 u3 = curlNoise(vec3(p * s, 0.0), t, isCurl); f += w3 * u3.xy; }
  return f;
}

void main(){
  ivec2 uv = ivec2(v_uv * resolution);
  

    // === 2D MODE: Legacy flat simulation ===
    vec2 p = texelFetch(posTex, uv, 0).xy;
    vec2 v = texelFetch(velTex, uv, 0).xy;

    float t = time * timeScale;
    bool isCurl = nullFlow < 0.5;
    
    // A: original 2D flow
    vec2 flowA = multiFlow2D(p, t, isCurl);
    
    // B: bireflected (mirror x, time offset, and mirror vector back)  
    vec2 pR = vec2(-p.x, p.y);
    vec2 flowB = multiFlow2D(pR, t + reflectDelta, isCurl);
    flowB = vec2(-flowB.x, flowB.y);

    vec2 flow = mix(flowA, flowB, clamp(reflectMix, 0.0, 1.0));
    vec2 A = -p;
    float phase = sin(time*burstFreq)*0.5+0.5;
    vec2 d = p - burstCenter.xy;
    vec2 dir = (dot(d,d) > 1e-12) ? normalize(d) : vec2(0.0);
    vec2 B = dir * burstAmp * phase;                // inward when phase<0, outward when phase>0
    vec2 noise = vec2(rand(p+time), rand(p-time)) * 2.0 - 1.0;

    // 2D Grace: entropy suppression and flow amplification
    float gMask = smoothstep(graceRadius, graceRadius*0.1, length(p - graceCenter.xy));
    float jitter = mix(jitterSigma, jitterSigma * (1.0 - 0.99*graceAmp), gMask);
    float align = mix(0.0, graceAmp * 5.0, gMask);
    float flowLen = length(flow);
    vec2 flowNorm = (flowLen > 1e-6) ? (flow / flowLen) : vec2(0.0);
    vec2 flowAligned = mix(flow, flowNorm * flowLen * (1.0 + graceAmp * 8.0), align);
    
    // 2D swirling motion in Grace zones
    float swirl = gMask * graceAmp * sin(time * 2.0 + length(p - graceCenter.xy) * 10.0);
    vec2 swirlForce = vec2(-flowAligned.y, flowAligned.x) * swirl * 2.0;
    flowAligned += swirlForce;

    vec2 F = k_flow*flowAligned + k_attract*A + k_burst*B;

    // 2D Devourer: anti-coherent collapse zones
    vec2 devCenter = vec2(0.4 * sin(time * 0.5), 0.4 * cos(time * 0.7));
    vec2 sinkDir = normalize(p - devCenter);
    vec2 gradSink = -sinkDir;
    float devDist = length(p - devCenter);
    float devMask = smoothstep(0.6, 0.1, devDist);
    
    float flutter = sin(13.0*time + dot(p, vec2(7.1,5.3))) * cos(time * 3.0);
    float sinkStr = devourerAmp * (3.0 + 2.0*sin(time*0.8)) * devMask;
    
    vec2 spiralForce = vec2(-gradSink.y, gradSink.x) * flutter * sinkStr;
    vec2 Dv = sinkStr * (gradSink * 5.0 + spiralForce);
    F += Dv;

    // 2D Langevin update
    v = (1.0 - damping)*v + dt*F + jitter * noise;
    p += dt * v;
    
    // 2D toroidal boundary (T^2): wrap position in [-domain, domain]
    p = mod(p + vec2(domain), vec2(2.0*domain)) - vec2(domain);
    
    if (passId == 0) out0 = vec4(p, 0.0, 1.0);
    else out0 = vec4(v, 0.0, 1.0);
}