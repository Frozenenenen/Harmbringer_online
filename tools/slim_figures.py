"""Slims the unit figures of the old Godot project for the browser.

Source GLBs (models/Figures/<Faction>/<Name>.glb, ~10-20 MB each) carry four 2048 px textures
(color, metal/roughness, normal, emissive) and float geometry. For the browser we keep:
  - geometry unchanged in shape, but quantized (KHR_mesh_quantization): positions int16,
    normals int8, UVs uint16, indices uint16 when possible
  - only the base color texture, scaled to --tex px (JPEG)
  - a plain material (metallic 0, roughness 0.85)
Result: roughly 0.3-0.6 MB per figure.

Usage: python tools/slim_figures.py <source Figures folder> <output folder> [--tex 512]
The source is only read (the Godot project is read-only).
"""
import argparse, io, json, os, struct, sys
import numpy as np
from PIL import Image

COMP = {5120: np.int8, 5121: np.uint8, 5122: np.int16, 5123: np.uint16, 5125: np.uint32, 5126: np.float32}
NCOMP = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4}

def read_glb(path):
    f = open(path, "rb").read()
    assert f[:4] == b"glTF"
    jl = struct.unpack("<I", f[12:16])[0]
    j = json.loads(f[20:20 + jl])
    bin_off = 20 + jl
    bl = struct.unpack("<I", f[bin_off:bin_off + 4])[0]
    return j, f[bin_off + 8:bin_off + 8 + bl]

def accessor(j, b, i):
    a = j["accessors"][i]; bv = j["bufferViews"][a["bufferView"]]
    dt = np.dtype(COMP[a["componentType"]]); n = NCOMP[a["type"]]
    start = bv.get("byteOffset", 0) + a.get("byteOffset", 0)
    stride = bv.get("byteStride", 0) or dt.itemsize * n
    raw = np.frombuffer(b, np.uint8, count=stride * (a["count"] - 1) + dt.itemsize * n, offset=start)
    rows = np.lib.stride_tricks.as_strided(raw, (a["count"], dt.itemsize * n), (stride, 1))
    return np.ascontiguousarray(rows).view(dt).reshape(a["count"], n)

def image_bytes(j, b, idx):
    im = j["images"][idx]; bv = j["bufferViews"][im["bufferView"]]
    o = bv.get("byteOffset", 0)
    return b[o:o + bv["byteLength"]]

def node_matrices(j):
    """World matrix per mesh node (scene graph flattened)."""
    def local(n):
        if "matrix" in n: return np.array(n["matrix"], dtype=np.float64).reshape(4, 4).T
        t = np.array(n.get("translation", [0, 0, 0])); r = n.get("rotation", [0, 0, 0, 1]); s = np.array(n.get("scale", [1, 1, 1]))
        x, y, z, w = r
        R = np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                      [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                      [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
        M = np.eye(4); M[:3, :3] = R * s; M[:3, 3] = t; return M
    out = []
    def walk(i, P):
        n = j["nodes"][i]; M = P @ local(n)
        if "mesh" in n: out.append((n["mesh"], M))
        for c in n.get("children", []): walk(c, M)
    scene = j["scenes"][j.get("scene", 0)]
    for i in scene["nodes"]: walk(i, np.eye(4))
    return out

def slim(src, dst, tex_px):
    j, b = read_glb(src)
    P, N, UV, IDX, base = [], [], [], [], 0
    tex_img = None
    for mi, M in node_matrices(j):
        for prim in j["meshes"][mi]["primitives"]:
            at = prim["attributes"]
            p = accessor(j, b, at["POSITION"]).astype(np.float64)
            p = (np.c_[p, np.ones(len(p))] @ M.T)[:, :3]
            nrm = accessor(j, b, at["NORMAL"]).astype(np.float64) @ np.linalg.inv(M[:3, :3])
            nrm /= np.maximum(np.linalg.norm(nrm, axis=1, keepdims=True), 1e-9)
            uv = accessor(j, b, at["TEXCOORD_0"]).astype(np.float64) if "TEXCOORD_0" in at else np.zeros((len(p), 2))
            idx = accessor(j, b, prim["indices"]).ravel().astype(np.int64) if "indices" in prim else np.arange(len(p))
            P.append(p); N.append(nrm); UV.append(uv); IDX.append(idx + base); base += len(p)
            mat = j["materials"][prim.get("material", 0)] if "materials" in j else {}
            bct = mat.get("pbrMetallicRoughness", {}).get("baseColorTexture")
            if bct is not None and tex_img is None:
                tex_img = Image.open(io.BytesIO(image_bytes(j, b, j["textures"][bct["index"]]["source"]))).convert("RGB")
    P, N, UV, IDX = np.vstack(P), np.vstack(N), np.vstack(UV), np.concatenate(IDX)
    # Quantize: positions to int16 in a [-1, 1] box (node scale/offset restores size), normals int8, UVs uint16.
    lo, hi = P.min(0), P.max(0); center = (lo + hi) / 2; half = max((hi - lo).max() / 2, 1e-9)
    qp = np.round((P - center) / half * 32767).astype(np.int16)
    qn = np.round(np.clip(N, -1, 1) * 127).astype(np.int8)
    uvc = np.clip(UV, 0, 1)                                   # source UVs are inside the atlas
    quv = np.round(uvc * 65535).astype(np.uint16)
    idx_t = np.uint16 if base < 65536 else np.uint32
    chunks, views = [], []
    def add(arr, target=None, stride=None):
        data = arr.tobytes()
        off = sum(len(c) for c in chunks)
        chunks.append(data + b"\0" * ((-len(data)) % 4))
        v = {"buffer": 0, "byteOffset": off, "byteLength": len(data)}
        if target: v["target"] = target
        if stride: v["byteStride"] = stride
        views.append(v); return len(views) - 1
    pos4 = np.c_[qp, np.zeros(len(qp), np.int16)]          # pad to 8 bytes per vertex (alignment)
    nrm4 = np.c_[qn, np.zeros(len(qn), np.int8)]
    v_pos = add(pos4, 34962, 8); v_nrm = add(nrm4, 34962, 4); v_uv = add(quv, 34962, 4); v_idx = add(IDX.astype(idx_t), 34963)
    accs = [
        {"bufferView": v_pos, "componentType": 5122, "normalized": True, "count": len(qp), "type": "VEC3",
         "min": qp.min(0).tolist(), "max": qp.max(0).tolist()},   # normalized accessors: min/max in raw int units
        {"bufferView": v_nrm, "componentType": 5120, "normalized": True, "count": len(qn), "type": "VEC3"},
        {"bufferView": v_uv, "componentType": 5123, "normalized": True, "count": len(quv), "type": "VEC2"},
        {"bufferView": v_idx, "componentType": 5123 if idx_t is np.uint16 else 5125, "count": len(IDX), "type": "SCALAR"},
    ]
    gj = {"asset": {"version": "2.0", "generator": "Harmbringer slim_figures.py"},
          "extensionsUsed": ["KHR_mesh_quantization"], "extensionsRequired": ["KHR_mesh_quantization"],
          "scene": 0, "scenes": [{"nodes": [0]}],
          "nodes": [{"mesh": 0, "translation": center.tolist(), "scale": [half, half, half]}],
          "meshes": [{"primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2}, "indices": 3, "material": 0}]}],
          "materials": [{"pbrMetallicRoughness": {"metallicFactor": 0.0, "roughnessFactor": 0.85}, "doubleSided": True}],
          "accessors": accs}
    if tex_img is not None:
        buf = io.BytesIO(); tex_img.resize((tex_px, tex_px), Image.LANCZOS).save(buf, "JPEG", quality=85, optimize=True)
        v_img = add(np.frombuffer(buf.getvalue(), np.uint8))
        gj["images"] = [{"bufferView": v_img, "mimeType": "image/jpeg"}]
        gj["samplers"] = [{"magFilter": 9729, "minFilter": 9987}]
        gj["textures"] = [{"source": 0, "sampler": 0}]
        gj["materials"][0]["pbrMetallicRoughness"]["baseColorTexture"] = {"index": 0}
    binb = b"".join(chunks); gj["buffers"] = [{"byteLength": len(binb)}]; gj["bufferViews"] = views
    js = json.dumps(gj, separators=(",", ":")).encode(); js += b" " * ((-len(js)) % 4)
    out = b"glTF" + struct.pack("<II", 2, 12 + 8 + len(js) + 8 + len(binb))
    out += struct.pack("<I", len(js)) + b"JSON" + js + struct.pack("<I", len(binb)) + b"BIN\0" + binb
    open(dst, "wb").write(out)
    return len(IDX) // 3, (hi - lo).tolist()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst"); ap.add_argument("--tex", type=int, default=512)
    a = ap.parse_args()
    report = []
    for root, _, files in os.walk(a.src):
        for fn in sorted(files):
            if not fn.lower().endswith(".glb"): continue
            rel = os.path.relpath(os.path.join(root, fn), a.src)
            out = os.path.join(a.dst, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            try:
                tris, size = slim(os.path.join(root, fn), out, a.tex)
                report.append((rel, os.path.getsize(os.path.join(root, fn)), os.path.getsize(out), tris, size))
                print(f"{rel:50s} {os.path.getsize(os.path.join(root, fn)) / 1e6:6.1f} MB -> {os.path.getsize(out) / 1e6:5.2f} MB, {tris} Dreiecke")
            except Exception as e:
                print(f"{rel}: FEHLER {e}", file=sys.stderr)
    json.dump([dict(file=r[0].replace(os.sep, "/"), source_bytes=r[1], bytes=r[2], triangles=r[3], size=r[4]) for r in report],
              open(os.path.join(a.dst, "figures.json"), "w"), indent=1)
