// Simple, fast gradient noise and numerical curl to produce divergence-free flow.
vec3 hash3(vec3 p){
  p = vec3(dot(p,vec3(127.1,311.7, 74.7)),
           dot(p,vec3(269.5,183.3,246.1)),
           dot(p,vec3(113.5,271.9,124.6)));
  return -1.0 + 2.0*fract(sin(p)*43758.5453123);
}

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

vec3 curlNoise(vec3 p, float t, bool isCurl){
  if (!isCurl) {
    // Non-curl random field for null hypothesis testing
    return vec3(n3(p + vec3(t, 0.0, 0.0)),
                n3(p.yzx + vec3(0.0, t*1.1, 0.0)),
                n3(p.zxy + vec3(0.0, 0.0, t*1.3)));
  }
  // Numerical curl of a synthetic vector noise field; ensures div u ≈ 0
  float e = 0.1;
  vec3 Fx1 = vec3(n3(p+vec3(e,0,0)+t), n3(p.yzx+vec3(e,0,0)+t), n3(p.zxy+vec3(e,0,0)+t));
  vec3 Fx2 = vec3(n3(p-vec3(e,0,0)+t), n3(p.yzx-vec3(e,0,0)+t), n3(p.zxy-vec3(e,0,0)+t));
  vec3 Fy1 = vec3(n3(p+vec3(0,e,0)+t*1.01), n3(p.yzx+vec3(0,e,0)+t*1.01), n3(p.zxy+vec3(0,e,0)+t*1.01));
  vec3 Fy2 = vec3(n3(p-vec3(0,e,0)+t*1.01), n3(p.yzx-vec3(0,e,0)+t*1.01), n3(p.zxy-vec3(0,e,0)+t*1.01));
  vec3 Fz1 = vec3(n3(p+vec3(0,0,e)+t*0.99), n3(p.yzx+vec3(0,0,e)+t*0.99), n3(p.zxy+vec3(0,0,e)+t*0.99));
  vec3 Fz2 = vec3(n3(p-vec3(0,e,0)+t*0.99), n3(p.yzx-vec3(0,e,0)+t*0.99), n3(p.zxy-vec3(0,0,e)+t*0.99));
  vec3 dFdy = (Fy1 - Fy2)/(2.0*e);
  vec3 dFdz = (Fz1 - Fz2)/(2.0*e);
  vec3 dFdx = (Fx1 - Fx2)/(2.0*e);
  return vec3(dFdz.x - dFdy.z,
              dFdx.z - dFdz.y,
              dFdy.y - dFdx.x);
}

float rand(vec2 co){ return fract(sin(dot(co, vec2(12.9898,78.233))) * 43758.5453); }
