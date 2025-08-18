#version 300 es
/*
  Trail decay shader
  - Applies exponential decay to previous frame's history buffer
  - historyOut = historyIn * fade
*/
precision highp float;
layout(location=0) out vec4 out0;
in vec2 v_uv;
uniform sampler2D srcTex;
uniform float fade;
void main(){
  vec4 c = texture(srcTex, v_uv);
  out0 = c * fade;
}