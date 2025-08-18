/**
 * 3D Matrix Utilities
 * Common matrix operations for 3D graphics
 */

export function createPerspectiveMatrix(fov, aspect, near, far) {
  const f = 1.0 / Math.tan(fov * 0.5);
  const rangeInv = 1.0 / (near - far);
  
  return [
    f / aspect, 0, 0, 0,
    0, f, 0, 0,
    0, 0, (near + far) * rangeInv, -1,
    0, 0, near * far * rangeInv * 2, 0
  ];
}

export function createViewMatrix(cameraX, cameraY, cameraZ, rotX, rotY) {
  const cosX = Math.cos(rotX);
  const sinX = Math.sin(rotX);
  const cosY = Math.cos(rotY);
  const sinY = Math.sin(rotY);
  
  // Rotation matrices
  const rotXMatrix = [
    1, 0, 0, 0,
    0, cosX, -sinX, 0,
    0, sinX, cosX, 0,
    0, 0, 0, 1
  ];
  
  const rotYMatrix = [
    cosY, 0, sinY, 0,
    0, 1, 0, 0,
    -sinY, 0, cosY, 0,
    0, 0, 0, 1
  ];
  
  // Translation matrix
  const translateMatrix = [
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    -cameraX, -cameraY, -cameraZ, 1
  ];
  
  // Combine: rotX * rotY * translate
  return multiplyMatrices(multiplyMatrices(rotXMatrix, rotYMatrix), translateMatrix);
}

export function multiplyMatrices(a, b) {
  const result = new Array(16);
  
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      result[i * 4 + j] = 
        a[i * 4 + 0] * b[0 * 4 + j] +
        a[i * 4 + 1] * b[1 * 4 + j] +
        a[i * 4 + 2] * b[2 * 4 + j] +
        a[i * 4 + 3] * b[3 * 4 + j];
    }
  }
  
  return result;
}

export function createIdentityMatrix() {
  return [
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1
  ];
}

export function createTranslationMatrix(x, y, z) {
  return [
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    x, y, z, 1
  ];
}

export function createScaleMatrix(sx, sy, sz) {
  return [
    sx, 0, 0, 0,
    0, sy, 0, 0,
    0, 0, sz, 0,
    0, 0, 0, 1
  ];
}

export function createRotationXMatrix(angle) {
  const cos = Math.cos(angle);
  const sin = Math.sin(angle);
  
  return [
    1, 0, 0, 0,
    0, cos, -sin, 0,
    0, sin, cos, 0,
    0, 0, 0, 1
  ];
}

export function createRotationYMatrix(angle) {
  const cos = Math.cos(angle);
  const sin = Math.sin(angle);
  
  return [
    cos, 0, sin, 0,
    0, 1, 0, 0,
    -sin, 0, cos, 0,
    0, 0, 0, 1
  ];
}

export function createRotationZMatrix(angle) {
  const cos = Math.cos(angle);
  const sin = Math.sin(angle);
  
  return [
    cos, -sin, 0, 0,
    sin, cos, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1
  ];
}
