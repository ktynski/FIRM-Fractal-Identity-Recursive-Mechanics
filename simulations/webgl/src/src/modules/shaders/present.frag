#version 300 es
/*
  Present shader
  - Tone-maps the accumulated history to the screen using simple exponential exposure
  - Optionally tints by trail magnitude as a crude order parameter (Ψ proxy)
  - Optional depth fog and frame-diff highlight to reveal evolving structure
*/
precision highp float;
layout(location=0) out vec4 out0;
in vec2 v_uv;
uniform sampler2D srcTex;
uniform sampler2D prevTex;   // previous presented frame (optional)
uniform float exposure;
uniform float psiTint; // 0..1
uniform float fogAmt;  // 0..1 depth fog amount
uniform float diffAmt; // 0..1 frame-diff overlay amount
void main(){
  vec3 c = texture(srcTex, v_uv).rgb;
  float psi = clamp(length(c), 0.0, 1.0);
  vec3 tone = 1.0 - exp(-c * exposure);
  vec3 tint = mix(tone, mix(vec3(0.85,0.92,1.0), vec3(0.3,1.0,0.6), psi), psiTint);
  // Depth fog from alpha of history as a proxy for depth layers
  float fog = fogAmt * clamp(c.b, 0.0, 1.0);
  vec3 fogged = mix(tint, vec3(0.02,0.04,0.06), fog);
  // Frame diff highlight
  vec3 prev = texture(prevTex, v_uv).rgb;
  float diff = clamp(length(tint - prev), 0.0, 1.0);
  vec3 highlight = mix(fogged, fogged + vec3(0.6,0.4,0.2) * diff, diffAmt);
  out0 = vec4(highlight, 1.0);
}