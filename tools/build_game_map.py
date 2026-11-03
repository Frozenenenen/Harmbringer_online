"""Builds the game heightmap (data/heightmap.js) on the UTM 32N campaign grid.

Source: design/source/heightmap_wgs84_15s.png (old 8-bit map, 15 arc-second lat/lon grid, 1704 x 920,
gray 29 = sea level, capped at 450 m). It is resampled onto a hex-friendly UTM grid:
  - columns: the campaign grid of worldmap.py (2017 points, ~247 m apart, west -> east)
  - rows: column spacing / (sqrt(3)/2), because hex rows are sqrt(3)/1.5 times further apart than
    hex columns. So one hex tile has the same size in meters in both directions.
Tile (q, r) is a hex center: E = e_min + q * colM, N = n_max - (r + 0.5 * (q & 1)) * rowM.
The height raster is sampled at N = n_max - (r + 0.25) * rowM (mean of even and odd columns),
matching the landscape mesh in index.html.

Heights above the 450 m cap (Harz) are reconstructed from known summit and village heights
(HARZ_POINTS, thin-plate spline plus fractal noise) until a real elevation model is available.
Output is 16 bit: meters = value * 0.02 - 100.

Also usable as a helper:  python tools/build_game_map.py --tile 53.1773 9.9196  -> prints q, r
"""
import argparse, base64, math, os
import numpy as np
from PIL import Image
from geo import to_utm, from_utm_np
from worldmap import layout

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "design", "source", "heightmap_wgs84_15s.png")
OLD_LON0, OLD_LAT0, OLD_PER_DEG = 7.1529, 54.8190, 240.0

def grid():
    L = layout()
    col_m = L["res"]
    row_m = col_m / (math.sqrt(3) / 2)
    rows = int((L["n_max"] - L["n_min"]) / row_m) + 1
    return dict(width=L["width"], height=rows, e_min=L["e_min"], n_max=L["n_max"], col_m=col_m, row_m=row_m)

def to_tile(lat, lon, G=None):
    G = G or grid()
    e, n = to_utm(lat, lon)
    q = round((e - G["e_min"]) / G["col_m"])
    r = round((G["n_max"] - n) / G["row_m"] - 0.5 * (q & 1))
    return q, r

# Approximate heights (m) inside the capped Harz plateau. Placeholder for a real DEM (e.g. SRTM).
HARZ_POINTS = [
    ("Brocken", 51.7991, 10.6156, 1141), ("Heinrichshöhe", 51.7920, 10.6290, 1044), ("Königsberg", 51.8037, 10.6038, 1033),
    ("Wurmberg", 51.7600, 10.6230, 971), ("Bruchberg", 51.7836, 10.4625, 927), ("Achtermannshöhe", 51.7550, 10.5550, 925),
    ("Hohneklippen", 51.8130, 10.6600, 908), ("Sonnenberg", 51.7500, 10.5000, 853), ("Acker", 51.7180, 10.4650, 865),
    ("Hanskühnenburg", 51.7243, 10.4103, 811), ("Torfhaus", 51.8040, 10.5360, 800), ("Großer Knollen", 51.6360, 10.4620, 687),
    ("Ravensberg", 51.6500, 10.4600, 659), ("Rammelsberg", 51.8890, 10.4180, 635), ("Schierke", 51.7660, 10.6650, 620),
    ("St. Andreasberg", 51.7110, 10.5170, 620), ("Hahnenklee", 51.8580, 10.3370, 600), ("Braunlage", 51.7260, 10.6100, 560),
    ("Clausthal", 51.8050, 10.3360, 560), ("Benneckenstein", 51.6650, 10.7170, 560), ("Ramberg", 51.6930, 11.0380, 582),
    ("Auerberg", 51.5900, 11.0300, 580), ("Elend", 51.7450, 10.6880, 500), ("Altenau", 51.8000, 10.4450, 480),
    ("Hasselfelde", 51.6900, 10.8540, 460),
]
CAP_M = 449.0

def reconstruct_harz(m, G):
    """Raises capped cells (>= CAP_M) by inverse distance weighting between the plateau edge (450 m)
    and HARZ_POINTS. Returns the new array."""
    capped = m >= CAP_M
    if not capped.any(): return m
    edge = capped & ~(np.roll(capped, 1, 0) & np.roll(capped, -1, 0) & np.roll(capped, 1, 1) & np.roll(capped, -1, 1))
    ey, ex = np.nonzero(edge)
    pts = [(x * G["col_m"], y * G["row_m"], 450.0) for y, x in zip(ey[::2], ex[::2])]
    for name, la, lo, h in HARZ_POINTS:
        q, r = to_tile(la, lo, G)
        if 0 <= r < m.shape[0] and 0 <= q < m.shape[1] and capped[r, q]:
            pts.append((q * G["col_m"], r * G["row_m"], float(h)))
    P = np.array(pts)
    cy, cx = np.nonzero(capped)
    # Smooth thin-plate spline through edge and summits (km units keep the system well conditioned).
    from scipy.interpolate import RBFInterpolator
    rbf = RBFInterpolator(P[:, :2] / 1000, P[:, 2], kernel="thin_plate_spline", smoothing=2.0, neighbors=120)
    h = rbf(np.column_stack([cx * G["col_m"], cy * G["row_m"]]) / 1000)
    # Ridges and valleys: fractal noise, stronger the higher the cell rises above the plateau.
    rng = np.random.default_rng(3)
    noise = np.zeros(m.shape)
    for k, amp in ((24, 1.0), (12, 0.5), (6, 0.25)):
        small = rng.random((m.shape[0] // k + 2, m.shape[1] // k + 2))
        noise += amp * np.asarray(Image.fromarray(small.astype(np.float32), "F").resize((m.shape[1] + 2 * k, m.shape[0] + 2 * k), Image.BICUBIC))[k:k + m.shape[0], k:k + m.shape[1]]
    noise = noise / 1.75 - 0.5
    rise = np.maximum(h - 450.0, 0)
    out = m.copy()
    out[cy, cx] = np.maximum(CAP_M, h + noise[cy, cx] * (40 + 0.35 * rise))
    return out

def old_tile_to_latlon(q, r):
    return OLD_LAT0 - r / OLD_PER_DEG, OLD_LON0 + q / OLD_PER_DEG

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--tile", nargs=2, type=float, metavar=("LAT", "LON"), help="only print the game tile of a position")
    a = ap.parse_args()
    G = grid()
    if a.tile:
        print(*to_tile(a.tile[0], a.tile[1], G)); raise SystemExit
    old = np.asarray(Image.open(SRC).convert("L"), dtype=np.float32)
    oh, ow = old.shape
    E = G["e_min"] + np.arange(G["width"]) * G["col_m"]
    N = G["n_max"] - (np.arange(G["height"]) + 0.25) * G["row_m"]
    EE, NN = np.meshgrid(E, N)
    lat, lon = from_utm_np(EE, NN)
    # Bilinear in the old grid; outside its lat/lon box the edge values are extended.
    px = np.clip((lon - OLD_LON0) * OLD_PER_DEG, 0, ow - 1); py = np.clip((OLD_LAT0 - lat) * OLD_PER_DEG, 0, oh - 1)
    x0 = np.minimum(np.floor(px).astype(int), ow - 2); y0 = np.minimum(np.floor(py).astype(int), oh - 2)
    fx, fy = px - x0, py - y0
    g = (old[y0, x0] * (1 - fx) * (1 - fy) + old[y0, x0 + 1] * fx * (1 - fy) +
         old[y0 + 1, x0] * (1 - fx) * fy + old[y0 + 1, x0 + 1] * fx * fy)
    m = g * 508.0 / 255.0 - 58.0                       # meters (bilinear, so no 2 m terraces)
    m = reconstruct_harz(m, G)
    v = np.clip(np.round((m + 100.0) / 0.02), 0, 65535).astype("<u2")
    path = os.path.join(ROOT, "data", "heightmap.js")
    with open(path, "w") as f:
        f.write("// Harmbringer heightmap on the campaign grid (ETRS89 / UTM 32N), built by tools/build_game_map.py.\n"
                f"// {G['width']} x {G['height']} hex tiles, column spacing {G['col_m']:.3f} m, row spacing {G['row_m']:.3f} m.\n"
                "// 16 bit little-endian, row-major, row 0 = north. meters = value * scale + offset.\n"
                "// Harz above 450 m: reconstructed from summit heights (approximation, see tools/build_game_map.py).\n")
        f.write(f'window.HARMBRINGER_HEIGHTMAP = {{ width: {G["width"]}, height: {G["height"]}, format: "u16", scale: 0.02, offset: -100, '
                f'utm: {{ eMin: {G["e_min"]:.3f}, nMax: {G["n_max"]:.3f}, colMeters: {G["col_m"]:.4f}, rowMeters: {G["row_m"]:.4f} }}, '
                f'data: "{base64.b64encode(v.tobytes()).decode()}" }};\n')
    print(path, G["width"], "x", G["height"], os.path.getsize(path) // 1024, "KB; max", round(float(m.max())), "m")
