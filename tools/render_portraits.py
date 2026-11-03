"""Renders unit portraits from the slimmed figures (assets/figures, see slim_figures.py).

Small software rasterizer (numpy, no GPU): orthographic view from the front, slightly from
above and turned, textured, Lambert light. Output: WebP with transparency.

Usage:
  python tools/render_portraits.py --sheet Undead            # contact sheet of a faction (to choose figures)
  python tools/render_portraits.py                            # portraits for GAME_FIGURES -> data/portraits.js
"""
import argparse, base64, io, json, math, os, struct
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "figures")

# Game unit id -> figure file (assets/figures/...). Units without a figure keep a colored placeholder.
# Generated/: figures built by build_hounds.py (no dog exists among the Godot figures).
# Since Nov. 2026 every unit uses its own low-poly figure from build_units.py (one consistent style).
# The slimmed Godot figures stay in assets/figures/<faction>/ for reference.
from build_units import UNITS as _UNITS
GAME_FIGURES = {u: f"Generated/{u}.glb" for u in _UNITS}

# Side view for animals (the default view is nearly frontal).
PORTRAIT_YAW = {"leichenhund": -65, "schwarzer_hund": -65, "balliste": -60, "knochenballiste": -60}

def load(path):
    b = open(path, "rb").read()
    jl = struct.unpack("<I", b[12:16])[0]
    j = json.loads(b[20:20 + jl]); binb = b[20 + jl + 8:]
    v = j["bufferViews"]; a = j["accessors"]
    def arr(i, dt, n):
        bv = v[a[i]["bufferView"]]; st = bv.get("byteStride", np.dtype(dt).itemsize * n)
        raw = np.frombuffer(binb, np.uint8, count=a[i]["count"] * st, offset=bv["byteOffset"]).reshape(-1, st)
        return raw[:, :np.dtype(dt).itemsize * n].copy().view(dt).reshape(-1, n)
    node = j["nodes"][0]
    P = arr(0, np.int16, 3) / 32767.0 * node["scale"][0] + np.array(node["translation"])
    N = arr(1, np.int8, 3) / 127.0
    UV = arr(2, np.uint16, 2) / 65535.0
    idt = np.uint16 if a[3]["componentType"] == 5123 else np.uint32
    bv = v[a[3]["bufferView"]]
    I = np.frombuffer(binb, idt, count=a[3]["count"], offset=bv["byteOffset"]).reshape(-1, 3).astype(np.int64)
    tex = None
    if "images" in j:
        bvi = v[j["images"][0]["bufferView"]]
        tex = np.asarray(Image.open(io.BytesIO(binb[bvi["byteOffset"]:bvi["byteOffset"] + bvi["byteLength"]])).convert("RGB"), np.float32) / 255
    return P, N, UV, I, tex

def render(path, size=192, ss=2, yaw=-28, pitch=12):
    P, N, UV, I, tex = load(path)
    W = H = size * ss
    cy, sy = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
    cp, sp = math.cos(math.radians(pitch)), math.sin(math.radians(pitch))
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]); Rx = np.array([[1, 0, 0], [0, cp, -sp], [0, sp, cp]])
    R = Rx @ Ry
    V = P @ R.T; Nn = N @ R.T
    lo, hi = V.min(0), V.max(0)
    scale = 0.9 * min(W / (hi[0] - lo[0]), H / (hi[1] - lo[1]))
    cx = (lo[0] + hi[0]) / 2; cyy = (lo[1] + hi[1]) / 2
    X = (V[:, 0] - cx) * scale + W / 2
    Y = H / 2 - (V[:, 1] - cyy) * scale
    Z = V[:, 2]                                                  # larger = closer to the camera (+Z)
    color = np.zeros((H, W, 3), np.float32); depth = np.full((H, W), -np.inf, np.float32); alpha = np.zeros((H, W), np.float32)
    light = np.array([-0.4, 0.6, 0.7]); light /= np.linalg.norm(light)
    th, tw = (tex.shape[0], tex.shape[1]) if tex is not None else (1, 1)
    for t in I:
        x, y = X[t], Y[t]
        x0, x1 = int(max(0, math.floor(x.min()))), int(min(W - 1, math.ceil(x.max())))
        y0, y1 = int(max(0, math.floor(y.min()))), int(min(H - 1, math.ceil(y.max())))
        if x1 < x0 or y1 < y0: continue
        d = (y[1] - y[2]) * (x[0] - x[2]) + (x[2] - x[1]) * (y[0] - y[2])
        if abs(d) < 1e-12: continue
        gx, gy = np.meshgrid(np.arange(x0, x1 + 1) + 0.5, np.arange(y0, y1 + 1) + 0.5)
        w0 = ((y[1] - y[2]) * (gx - x[2]) + (x[2] - x[1]) * (gy - y[2])) / d
        w1 = ((y[2] - y[0]) * (gx - x[2]) + (x[0] - x[2]) * (gy - y[2])) / d
        w2 = 1 - w0 - w1
        m = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)
        if not m.any(): continue
        z = w0 * Z[t[0]] + w1 * Z[t[1]] + w2 * Z[t[2]]
        sub = depth[y0:y1 + 1, x0:x1 + 1]
        m &= z > sub
        if not m.any(): continue
        sub[m] = z[m]
        u = (w0 * UV[t[0], 0] + w1 * UV[t[1], 0] + w2 * UV[t[2], 0])[m]
        v = (w0 * UV[t[0], 1] + w1 * UV[t[1], 1] + w2 * UV[t[2], 1])[m]
        n = w0[m, None] * Nn[t[0]] + w1[m, None] * Nn[t[1]] + w2[m, None] * Nn[t[2]]
        n /= np.maximum(np.linalg.norm(n, axis=1, keepdims=True), 1e-6)
        lam = np.abs(n @ light)                                  # double sided
        if tex is not None:
            c = tex[np.clip((v * th).astype(int), 0, th - 1), np.clip((u * tw).astype(int), 0, tw - 1)]
        else:
            c = np.full((m.sum(), 3), 0.6, np.float32)
        csub = color[y0:y1 + 1, x0:x1 + 1]; csub[m] = c * (0.45 + 0.85 * lam[:, None])
        alpha[y0:y1 + 1, x0:x1 + 1][m] = 1
    img = np.dstack([np.clip(color, 0, 1), alpha])
    im = Image.fromarray((img * 255).astype(np.uint8), "RGBA").resize((size, size), Image.LANCZOS)
    return im

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", help="faction folder for a contact sheet (PNG into the scratch folder given by --out)")
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "portraits.js"))
    ap.add_argument("--size", type=int, default=160)
    a = ap.parse_args()
    if a.sheet:
        files = sorted(f for f in os.listdir(os.path.join(FIG, a.sheet)) if f.endswith(".glb"))
        cols = 6; rows = math.ceil(len(files) / cols); S = 200
        from PIL import ImageDraw
        sheet = Image.new("RGB", (cols * S, rows * (S + 18)), (110, 103, 92)); dr = ImageDraw.Draw(sheet)
        for k, f in enumerate(files):
            im = render(os.path.join(FIG, a.sheet, f), S)
            x, y = (k % cols) * S, (k // cols) * (S + 18)
            sheet.paste(im, (x, y), im); dr.text((x + 4, y + S + 2), f[:-4], fill=(255, 255, 255))
        sheet.save(a.out); print(a.out)
        raise SystemExit
    out = {}
    for unit, f in GAME_FIGURES.items():
        im = render(os.path.join(FIG, f), a.size, yaw=PORTRAIT_YAW.get(unit, -28))
        buf = io.BytesIO(); im.save(buf, "WEBP", quality=82, method=6)
        out[unit] = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
        print(f"{unit:14s} {f:40s} {len(buf.getvalue()) // 1024} KB")
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("// Unit portraits rendered from assets/figures by tools/render_portraits.py (data URIs for file://).\n")
        fh.write("window.HARMBRINGER_PORTRAITS = " + json.dumps(out) + ";\n")
    print(a.out, os.path.getsize(a.out) // 1024, "KB")
