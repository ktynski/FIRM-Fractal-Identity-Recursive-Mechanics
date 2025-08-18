#version 300 es
precision highp float;
layout(location=0) out vec4 out0;
in vec2 v_uv;
uniform sampler2D posTex;
uniform sampler2D velTex;
uniform sampler2D trackUV; // RG: integer texel coords
uniform vec2 texDim; // cols, rows
void main(){
  int i = int(float(textureSize(trackUV,0).x) * v_uv.x);
  // sample trackUV as nearest
  vec2 uvInt = texelFetch(trackUV, ivec2(i,0), 0).rg;
  ivec2 uv = ivec2(int(uvInt.x), int(uvInt.y));
  vec2 p = texelFetch(posTex, uv, 0).xy;
  vec2 v = texelFetch(velTex, uv, 0).xy;
  out0 = vec4(p, v);
}