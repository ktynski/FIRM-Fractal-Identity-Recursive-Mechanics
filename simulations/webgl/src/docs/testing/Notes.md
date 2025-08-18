got it. let’s rebuild Scale Space in WebGL—faithful to your emergence knobs (entropy ↔ curl, free energy ↔ spawn/drive) and with a clean, extensible GPU core.

High-level design (what maps to what)
	•	State: particles with position p and velocity v in a continuous field.
	•	Drive (free energy): spawn rate S, burst injectors, audio energy.
	•	Dissipation (entropy sink): velocity damping D, curl jitter J.
	•	Order field: divergence-free curl noise flow (prevents blow-ups, preserves structure).
	•	Emergence tension: κ = S / (D + J) steered toward a target τ (your “dynamic tension”).

We’ll run a GPGPU simulation (ping-pong framebuffers) for millions of particles, then render them as glowing filaments. Everything below is WebGL2 + GLSL, with minimal deps (Three.js optional but not required).

Core equations (sim step)

For each particle i:
	•	Flow field: u(p,t) = curl(noise(p·α + t·β))
	•	Forces: F = k_flow·u + k_attract·A(p) + k_burst·B(t,p)
	•	Velocity: v ← (1−D)·v + dt·F + σ·ξ (σ sets micro-jitter = entropy floor)
	•	Position: p ← p + dt·v  (wrap or fold at bounds)
	•	Respawn: if |p| out of domain or |v| > vmax → re-seed from emitter

Dynamic tension controller (keeps you in the “cymatic” band):
	•	Measure energy E = ⟨|v|²⟩
	•	Update scalars toward τ:
k_flow ← k_flow·exp(η(τ − κ)), where κ = S/(D+J), J≈σ
or simpler: auto-adjust S (spawn) and D (damping) to keep E in a target window.

Project layout

/src
  index.html
  main.js
  gl/
    sim.vert         // full-screen tri
    sim.frag         // updates RGBA32F position/velocity
    render.vert      // transform feedback or instanced
    render.frag      // glowing ribbon/point
    noise.glsl       // simplex + curl
  lib/
    twgl.min.js      // or three.min.js (your call)
  presets/
    default.json     // τ, k_flow, D, σ, S, burst config

Minimal, working shaders (drop-in)

gl/noise.glsl (curl from simplex)

// --- noise.glsl ---
precision highp float;

vec3 hash3(vec3 p){ p = vec3(dot(p,vec3(127.1,311.7, 74.7)),
                             dot(p,vec3(269.5,183.3,246.1)),
                             dot(p,vec3(113.5,271.9,124.6)));
  return -1.0 + 2.0*fract(sin(p)*43758.5453123);
}

// Simplex-ish 3D noise, fast & adequate for flow
float n3(vec3 p){
  const float K1=0.333333333, K2=0.166666667;
  vec3 i=floor(p+dot(p,vec3(K1)));
  vec3 x0=p-i+dot(i,vec3(K2));
  vec3 g=step(vec3(0.0),x0.yzx-x0.xyz);
  vec3 l=1.0-g; vec3 i1=min(g,1.0-l.zxy); vec3 i2=max(g,1.0-l.zxy);
  vec3 x1=x0-i1+K2, x2=x0-i2+2.0*K2, x3=x0-1.0+3.0*K2;

  vec4 w=vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3));
  vec4 m=max(0.6-w,0.0); m=m*m; m=m*m;

  vec3 g0=hash3(i+vec3(0.0));
  vec3 g1=hash3(i+i1);
  vec3 g2=hash3(i+i2);
  vec3 g3=hash3(i+vec3(1.0));

  return dot(m, vec4(dot(g0,x0), dot(g1,x1), dot(g2,x2), dot(g3,x3)));
}

// Numerical curl of a vector noise field F = (n, n shifted, n shifted)
vec3 curlNoise(vec3 p, float t){
  float e = 0.1;
  vec3 q1 = vec3(n3(p + vec3(1.0,0.0,0.0)+t),
                 n3(p + vec3(0.0,1.0,0.0)+t*1.1),
                 n3(p + vec3(0.0,0.0,1.0)+t*1.3));
  vec3 q2 = vec3(n3(p - vec3(1.0,0.0,0.0)+t),
                 n3(p - vec3(0.0,1.0,0.0)+t*1.1),
                 n3(p - vec3(0.0,0.0,1.0)+t*1.3));

  vec3 dqdx = (q1 - q2)/(2.0);
  // Build a fake vector field F then take curl numerically
  // F = (n(x,y,z), n(y,z,x), n(z,x,y))
  vec3 Fx1 = vec3(n3(p+vec3(e,0,0)+t), n3(p.yzx+vec3(e,0,0)+t), n3(p.zxy+vec3(e,0,0)+t));
  vec3 Fx2 = vec3(n3(p-vec3(e,0,0)+t), n3(p.yzx-vec3(e,0,0)+t), n3(p.zxy-vec3(e,0,0)+t));
  vec3 Fy1 = vec3(n3(p+vec3(0,e,0)+t*1.01), n3(p.yzx+vec3(0,e,0)+t*1.01), n3(p.zxy+vec3(0,e,0)+t*1.01));
  vec3 Fy2 = vec3(n3(p-vec3(0,e,0)+t*1.01), n3(p.yzx-vec3(0,e,0)+t*1.01), n3(p.zxy-vec3(0,e,0)+t*1.01));
  vec3 Fz1 = vec3(n3(p+vec3(0,0,e)+t*0.99), n3(p.yzx+vec3(0,0,e)+t*0.99), n3(p.zxy+vec3(0,0,e)+t*0.99));
  vec3 Fz2 = vec3(n3(p-vec3(0,0,e)+t*0.99), n3(p.yzx-vec3(0,0,e)+t*0.99), n3(p.zxy-vec3(0,0,e)+t*0.99));

  vec3 dFdy = (Fy1 - Fy2)/(2.0*e);
  vec3 dFdz = (Fz1 - Fz2)/(2.0*e);
  vec3 dFdx = (Fx1 - Fx2)/(2.0*e);

  // curl(F) = (dFz/dy - dFy/dz, dFx/dz - dFz/dx, dFy/dx - dFx/dy)
  return vec3(dFdz.x - dFdy.z,
              dFdx.z - dFdz.y,
              dFdy.y - dFdx.x);
}

gl/sim.frag (update positions & velocities in RGBA32F textures)

#version 300 es
precision highp float;
out vec4 out0;
uniform sampler2D prevTex;   // RGBA: pos.xy (zw unused) on even pass, vel.xy on odd, or use two targets
uniform vec2 resolution;     // texture size (Nx, Ny)
uniform float dt;
uniform float time;
uniform vec2 domain;         // world half-extent, e.g. vec2(1.0)
uniform float k_flow, k_attract, k_burst;
uniform float damping, jitterSigma;
uniform float fieldScale, timeScale;
uniform vec2 burstCenter;    // screen-space (−1..1)
uniform float burstAmp, burstFreq;
in vec2 v_uv;

#include "noise.glsl"

// Layout: tex0 = positions, tex1 = velocities (bind separately if MRT)
uniform sampler2D posTex;
uniform sampler2D velTex;
uniform int passId; // 0: pos, 1: vel

// Helpers
float rand(vec2 co){ return fract(sin(dot(co, vec2(12.9898,78.233))) * 43758.5453); }

void main() {
  ivec2 uv = ivec2(v_uv * resolution);
  vec2 p = texelFetch(posTex, uv, 0).xy;
  vec2 v = texelFetch(velTex, uv, 0).xy;

  // Flow field (curl noise in 3D but we sample on z=0 plane)
  vec3 u = curlNoise(vec3(p*fieldScale, 0.0), time*timeScale);
  vec2 flow = u.xy;

  // Attractor (optional): gentle return to center
  vec2 A = -p;

  // Burst (cymatic injector): radial push on a time torus
  float phase = sin(time*burstFreq)*0.5+0.5; // 0..1
  vec2 dir = normalize(p - burstCenter);
  vec2 B = dir * burstAmp * smoothstep(0.0, 0.5, phase);

  // Langevin-like update
  vec2 noise = vec2(rand(p+time), rand(p-time)) * 2.0 - 1.0;
  vec2 F = k_flow*flow + k_attract*A + k_burst*B;
  v = (1.0 - damping)*v + dt*F + jitterSigma*noise;

  // Integrate
  p += dt * v;

  // Wrap
  p = mod(p + domain, 2.0*domain) - domain;

  if (passId == 0) out0 = vec4(p, 0.0, 1.0);
  else             out0 = vec4(v, 0.0, 1.0);
}

gl/render.frag (glow points; upgrade to trails later)

#version 300 es
precision highp float;
out vec4 fragColor;
in vec2 v_pt; // point size attenuation coords, if used
uniform vec3 baseColor;
uniform float brightness;

void main(){
  // Soft round sprite
  vec2 uv = gl_PointCoord*2.0 - 1.0;
  float r = dot(uv,uv);
  float alpha = exp(-r*3.0);
  fragColor = vec4(baseColor * brightness * alpha, alpha);
}

main.js sketch (TWGL or raw WebGL2)
	•	Create two RGBA32F textures for pos and vel, with ping-pong FBOs.
	•	Run sim.frag twice per frame (passId=1 for vel, then passId=0 for pos).
	•	Render with instanced points; each instance reads its position from posTex via a vertex fetch (index → texel coord).
	•	Controls via lil-gui: k_flow, damping, jitterSigma, spawnRate, burstAmp, fieldScale, timeScale, τ.

I won’t paste a 300-line JS here, but the structure is:

initGL(); initTextures(N); initPrograms();
seedParticles();
function step(dt){
  // vel pass
  bind(simProg); set(passId=1); bindTex(posTex,velTex); drawFullScreen();
  swap(velTex);

  // pos pass
  bind(simProg); set(passId=0); bindTex(posTex,velTex); drawFullScreen();
  swap(posTex);

  // render
  bind(renderProg); bindVAO(points); bindTex(posTex); gl.drawArraysInstanced(GL.POINTS, ... , N);
}
requestAnimationFrame(loop);

Audio → Cymatics (optional but awesome)
	•	Use WebAudio AnalyserNode FFT.
	•	Compute band energies; map to:
	•	burstAmp (low/mid bass),
	•	fieldScale or timeScale (mids → flow complexity),
	•	spawnRate S (highs → scintillation).
	•	Close the loop: if average energy ↑, gently raise D to keep κ≈τ (so it “breathes” instead of clipping).

Looped burst scheduler (the “time torus”)

Create a deterministic cycle so visuals repeat seamlessly:
	•	T_loop seconds; internal phase φ = 2π t / T_loop.
	•	Burst centers follow Lissajous in domain:
cx = R cos(ax φ), cy = R sin(by φ + δ)
	•	Burst shape also cycles (e.g., switch between radial and tangential).

This gives the hypnotic, cymatic symmetry you saw in Niagara.

Presets (JSON)

{
  "name":"Cymatic-01",
  "tau": 1.8,
  "k_flow": 1.2, "damping": 0.08, "jitterSigma": 0.02,
  "spawnRate": 0.6,
  "fieldScale": 1.7, "timeScale": 0.35,
  "burst": { "amp": 0.9, "freq": 0.4, "radius": 0.6, "lissajous":[3,2,0.3] }
}

Trails & 3D “holographic projector” vibe (upgrade path)
	•	Trails: render to a low-res history buffer with additive decay (history = history*fade + splat(points)), then bloom.
	•	3D look: interpret “scale” as pseudo-depth—render multiple layers with z-offsets per orientation band (color by local flow angle). It reads like braided beams but stays honest to the 2D field.

Performance notes
	•	Use RG float textures for pos & vel to halve bandwidth.
	•	Keep particle count adaptive: start 512k; scale to 2–4M on desktop GPUs.
	•	Prefer gl.POINTS + history buffer for thick filaments over geometry ribbons (much cheaper).

What I can hand you next
	•	A compact starter repo with the exact shaders above wired up.
	•	A preset pack matching your Niagara feels (cymatic, cellular, storm, braid).
	•	An audio-reactive module and the looped burst scheduler.
	•	Optional Three.js wrapper if you want camera/UI scaffolding out of the box.

If you want, say the word and I’ll drop a zipped starter with everything hooked together and a couple of presets so you can iterate on the tension parameters fast.