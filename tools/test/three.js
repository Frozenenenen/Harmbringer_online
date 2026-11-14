// Universal no-op stand-in for three.js (logic smoke test only).
function mk(){
  const store = new Map();
  const f = function(){};
  return new Proxy(f, {
    get(t,k){
      if (store.has(k)) return store.get(k);
      if (k === Symbol.toPrimitive) return () => 0;
      if (k === Symbol.iterator) return function*(){};
      if (k === 'then') return undefined;
      if (k === 'length' || k === 'x' || k === 'y' || k === 'z' || k === 'w') return 0;
      if (k === 'children') { const a=[]; store.set(k,a); return a; }
      if (k === 'userData') { const o={}; store.set(k,o); return o; }
      if (k === 'domElement') { const c=document.createElement('canvas'); store.set(k,c); return c; }
      if (k === 'style') { const o={}; store.set(k,o); return o; }
      if (k === 'element') { const d=document.createElement('div'); store.set(k,d); return d; }
      if (k === 'intersectObjects' || k === 'intersectObject') return () => [];
      if (k === 'toFixed') return () => '0';
      if (k === 'getHexString' || k === 'getStyle') return () => '000000';
      const v = mk(); store.set(k, v); return v;
    },
    set(t,k,v){ store.set(k,v); return true; },
    apply(){ return mk(); },
    construct(t, args){ const p = mk(); if (args[0] && typeof args[0]==='object' && args[0].nodeType) p.element = args[0]; return p; },
  });
}
export const BoxGeometry = mk();
export const BufferAttribute = mk();
export const BufferGeometry = mk();
export const CapsuleGeometry = mk();
export const Color = mk();
export const ConeGeometry = mk();
export const CylinderGeometry = mk();
export const DataArrayTexture = mk();
export const DataTexture = mk();
export const DirectionalLight = mk();
export const DodecahedronGeometry = mk();
export const ExtrudeGeometry = mk();
export const Float32BufferAttribute = mk();
export const FloatType = mk();
export const FogExp2 = mk();
export const GLSL3 = mk();
export const Group = mk();
export const HemisphereLight = mk();
export const IcosahedronGeometry = mk();
export const InstancedMesh = mk();
export const LinearFilter = mk();
export const LinearMipmapLinearFilter = mk();
export const Matrix4 = mk();
export const Mesh = mk();
export const MeshBasicMaterial = mk();
export const MeshStandardMaterial = mk();
export const NearestFilter = mk();
export const Object3D = mk();
export const OctahedronGeometry = mk();
export const PerspectiveCamera = mk();
export const PlaneGeometry = mk();
export const Quaternion = mk();
export const RGBAFormat = mk();
export const Raycaster = mk();
export const RedFormat = mk();
export const RepeatWrapping = mk();
export const Scene = mk();
export const ShaderMaterial = mk();
export const Shape = mk();
export const SphereGeometry = mk();
export const TorusGeometry = mk();
export const RingGeometry = mk();
export const UnsignedByteType = mk();
export const Vector2 = mk();
export const Vector3 = mk();
export const WebGLRenderer = mk();
