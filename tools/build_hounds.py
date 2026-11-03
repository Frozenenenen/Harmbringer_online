"""Builds simple low-poly hound figures (no dog exists among the Godot figures).

Output (same GLB layout as slim_figures.py, so portraits and the battle loader work unchanged):
  assets/figures/Generated/Hound_Corpse.glb  - Leichenhund: rotten grey-green fur, ribs, green eyes
  assets/figures/Generated/Hound_Black.glb   - Schwarzer Hund: black fur, glowing red eyes
The hound looks along +Z like the other figures. Colors come from a tiny palette texture.
"""
import io, json, math, os, struct
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "figures", "Generated")

class Mesh:
    def __init__(self, palette):
        self.P, self.UV, self.pal = [], [], palette        # flat triangles: 3 positions + palette slot each
    def tri(self, a, b, c, slot):
        self.P += [a, b, c]; self.UV += [slot] * 3
    def quad(self, a, b, c, d, slot):
        self.tri(a, b, c, slot); self.tri(a, c, d, slot)
    def box(self, center, size, slot, rot_x=0.0):
        cx, cy, cz = center; sx, sy, sz = (s / 2 for s in size)
        v = np.array([[x, y, z] for x in (-sx, sx) for y in (-sy, sy) for z in (-sz, sz)])
        c, s = math.cos(rot_x), math.sin(rot_x)
        v = v @ np.array([[1, 0, 0], [0, c, -s], [0, s, c]]).T + center
        f = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]
        for a, b, cc, d in f: self.quad(v[a], v[b], v[cc], v[d], slot)
    def cyl(self, p0, p1, r0, r1, slot, seg=6):
        p0, p1 = np.array(p0, float), np.array(p1, float); axis = p1 - p0; axis /= np.linalg.norm(axis)
        ref = np.array([1, 0, 0]) if abs(axis[0]) < 0.9 else np.array([0, 0, 1])
        u = np.cross(axis, ref); u /= np.linalg.norm(u); w = np.cross(axis, u)
        ring = lambda p, r: [p + r * (math.cos(2 * math.pi * k / seg) * u + math.sin(2 * math.pi * k / seg) * w) for k in range(seg)]
        A, B = ring(p0, r0), ring(p1, r1)
        for k in range(seg):
            j = (k + 1) % seg
            if r1 > 0: self.quad(A[k], A[j], B[j], B[k], slot)
            else: self.tri(A[k], A[j], p1, slot)
            self.tri(p0, A[j], A[k], slot)
            if r1 > 0: self.tri(p1, B[k], B[j], slot)
    def blob(self, center, radii, slot, rings=5, seg=8):
        c = np.array(center, float); r = np.array(radii, float)
        pts = [[c + r * np.array([math.sin(math.pi * i / rings) * math.cos(2 * math.pi * k / seg), math.cos(math.pi * i / rings),
                                  math.sin(math.pi * i / rings) * math.sin(2 * math.pi * k / seg)]) for k in range(seg)] for i in range(rings + 1)]
        for i in range(rings):
            for k in range(seg):
                j = (k + 1) % seg
                self.quad(pts[i][k], pts[i][j], pts[i + 1][j], pts[i + 1][k], slot)

def hound(fur, fur_dark, eye, bone=None, gaunt=False):
    pal = [fur, fur_dark, eye, bone or fur_dark, "#3a1414"]
    m = Mesh(pal)
    FUR, DARK, EYE, BONE, MOUTH = range(5)
    belly = 0.13 if gaunt else 0.16
    m.blob((0, 0.62, -0.05), (0.17, belly, 0.42), FUR)                # body
    m.blob((0, 0.68, 0.24), (0.19, 0.2, 0.22), DARK)                  # chest / shoulders
    if bone:                                                          # exposed ribs on both flanks
        for k in range(4):
            z = 0.12 - k * 0.1
            for sx in (-1, 1):
                m.cyl((sx * 0.15, 0.72, z), (sx * 0.17, 0.52, z - 0.03), 0.018, 0.015, BONE, seg=4)
    m.cyl((0, 0.78, 0.36), (0, 0.9, 0.5), 0.1, 0.09, FUR)             # neck
    m.blob((0, 0.93, 0.56), (0.12, 0.11, 0.13), FUR)                  # head
    m.box((0, 0.88, 0.72), (0.12, 0.09, 0.2), DARK)                   # snout
    m.box((0, 0.835, 0.71), (0.1, 0.03, 0.18), MOUTH)                 # open jaw
    for sx in (-1, 1):
        m.cyl((sx * 0.06, 1.01, 0.52), (sx * 0.09, 1.16, 0.48), 0.045, 0.0, DARK, seg=4)   # ears
        m.box((sx * 0.065, 0.95, 0.665), (0.035, 0.03, 0.02), EYE)                         # eyes
    leg_r = 0.035 if gaunt else 0.045
    for sx in (-1, 1):
        for z, top in ((0.26, 0.62), (-0.32, 0.6)):
            m.cyl((sx * 0.1, top, z), (sx * 0.1, 0.28, z + 0.02), leg_r * 1.3, leg_r, FUR)
            m.cyl((sx * 0.1, 0.28, z + 0.02), (sx * 0.1, 0.02, z - 0.02), leg_r, leg_r * 0.9, DARK)
            m.box((sx * 0.1, 0.02, z + 0.02), (0.07, 0.04, 0.1), DARK)                     # paws
    m.cyl((0, 0.68, -0.44), (0, 0.5, -0.78), 0.04, 0.0, DARK, seg=5)  # tail
    return m

def write_glb(m, path):
    P = np.array(m.P, float); n_tri = len(P) // 3
    # flat normals
    tri = P.reshape(-1, 3, 3); nrm = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    nrm /= np.maximum(np.linalg.norm(nrm, axis=1, keepdims=True), 1e-9); N = np.repeat(nrm, 3, axis=0)
    # palette texture: one 16 px cell per color, UV at the cell center
    S = 16; tex = Image.new("RGB", (S * len(m.pal), S))
    for i, c in enumerate(m.pal): tex.paste(Image.new("RGB", (S, S), c), (i * S, 0))
    tex = tex.resize((64 * len(m.pal) // len(m.pal) * len(m.pal) if False else S * len(m.pal), S))
    UV = np.array([[(s + 0.5) / len(m.pal), 0.5] for s in m.UV])
    lo, hi = P.min(0), P.max(0); center = (lo + hi) / 2; half = (hi - lo).max() / 2
    qp = np.round((P - center) / half * 32767).astype(np.int16)
    qn = np.round(N * 127).astype(np.int8); quv = np.round(UV * 65535).astype(np.uint16)
    idx = np.arange(len(P), dtype=np.uint16)
    chunks, views = [], []
    def add(arr, target=None, stride=None):
        data = arr.tobytes(); off = sum(len(c) for c in chunks)
        chunks.append(data + b"\0" * ((-len(data)) % 4))
        v = {"buffer": 0, "byteOffset": off, "byteLength": len(data)}
        if target: v["target"] = target
        if stride: v["byteStride"] = stride
        views.append(v); return len(views) - 1
    vp = add(np.c_[qp, np.zeros(len(qp), np.int16)], 34962, 8); vn = add(np.c_[qn, np.zeros(len(qn), np.int8)], 34962, 4)
    vu = add(quv, 34962, 4); vi = add(idx, 34963)
    buf = io.BytesIO(); tex.save(buf, "PNG"); vimg = add(np.frombuffer(buf.getvalue(), np.uint8))
    gj = {"asset": {"version": "2.0", "generator": "Harmbringer build_hounds.py"},
          "extensionsUsed": ["KHR_mesh_quantization"], "extensionsRequired": ["KHR_mesh_quantization"],
          "scene": 0, "scenes": [{"nodes": [0]}], "nodes": [{"mesh": 0, "translation": center.tolist(), "scale": [half] * 3}],
          "meshes": [{"primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2}, "indices": 3, "material": 0}]}],
          "materials": [{"pbrMetallicRoughness": {"metallicFactor": 0.0, "roughnessFactor": 0.9, "baseColorTexture": {"index": 0}}}],
          "textures": [{"source": 0, "sampler": 0}], "samplers": [{"magFilter": 9728, "minFilter": 9728}],
          "images": [{"bufferView": vimg, "mimeType": "image/png"}],
          "accessors": [
              {"bufferView": vp, "componentType": 5122, "normalized": True, "count": len(qp), "type": "VEC3", "min": qp.min(0).tolist(), "max": qp.max(0).tolist()},
              {"bufferView": vn, "componentType": 5120, "normalized": True, "count": len(qn), "type": "VEC3"},
              {"bufferView": vu, "componentType": 5123, "normalized": True, "count": len(quv), "type": "VEC2"},
              {"bufferView": vi, "componentType": 5123, "count": len(idx), "type": "SCALAR"}]}
    binb = b"".join(chunks); gj["buffers"] = [{"byteLength": len(binb)}]; gj["bufferViews"] = views
    js = json.dumps(gj, separators=(",", ":")).encode(); js += b" " * ((-len(js)) % 4)
    out = b"glTF" + struct.pack("<II", 2, 12 + 8 + len(js) + 8 + len(binb)) + struct.pack("<I", len(js)) + b"JSON" + js + struct.pack("<I", len(binb)) + b"BIN\0" + binb
    open(path, "wb").write(out)
    return n_tri

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, m in (("Hound_Corpse", hound("#6f6f5a", "#4a4a3c", "#9be05a", bone="#d8d0b8", gaunt=True)),
                    ("Hound_Black", hound("#1e1c1c", "#0e0d0d", "#ff3a1a"))):
        p = os.path.join(OUT, name + ".glb"); t = write_glb(m, p)
        print(p, t, "Dreiecke", os.path.getsize(p) // 1024, "KB")
