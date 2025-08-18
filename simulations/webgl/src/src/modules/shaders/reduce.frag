#version 300 es
/*
  Reduction fragment shader
  - Computes speed^2 per pixel from the velocity texture
  - Rendered into a small framebuffer; CPU averages to estimate E = <|v|^2>
*/
precision highp float;
layout(location=0) out vec4 out0;
in vec2 v_uv;
uniform sampler2D velTex;
void main(){
  vec2 v = texture(velTex, v_uv).xy;
  float e = dot(v,v);
  out0 = vec4(e, 0.0, 0.0, 1.0);
}