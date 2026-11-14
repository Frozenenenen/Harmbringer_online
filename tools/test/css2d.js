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
export const CSS2DRenderer = mk(); export const CSS2DObject = mk();
