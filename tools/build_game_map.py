"""Builds the game heightmap (data/heightmap.js) on the UTM 32N campaign grid.

Source: design/source/heightmap_wgs84_15s.png (old 8-bit map, 15 arc-second lat/lon grid, 1704 x 920,
gray 29 = sea level, capped at 450 m). It is resampled onto a hex-friendly UTM grid:
  - columns: the campaign grid of worldmap.py (2017 points, ~247 m apart, west -> east)
  - rows: column spacing / (sqrt(3)/2), because hex rows are sqrt(3)/1.5 times further apart than
    hex columns. So one hex tile has the same size in meters in both directions.
Tile (q, r) is a hex center: E = e_min + q * colM, N = n_max - (r + 0.5 * (q & 1)) * rowM.
The height raster is sampled at N = n_max - (r + 0.25) * rowM (mean of even and odd columns),
matching the landscape mesh in index.html.

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
    g = np.clip(np.round(g), 0, 255).astype(np.uint8)
    path = os.path.join(ROOT, "data", "heightmap.js")
    with open(path, "w") as f:
        f.write("// Harmbringer heightmap on the campaign grid (ETRS89 / UTM 32N), built by tools/build_game_map.py.\n"
                f"// {G['width']} x {G['height']} hex tiles, column spacing {G['col_m']:.3f} m, row spacing {G['row_m']:.3f} m.\n"
                "// 8-bit gray, row-major, row 0 = north. Gray 29 = sea level, 255 = capped (450 m).\n"
                "// Decode: Uint8Array.from(atob(HARMBRINGER_HEIGHTMAP.data), c => c.charCodeAt(0))\n")
        f.write(f'window.HARMBRINGER_HEIGHTMAP = {{ width: {G["width"]}, height: {G["height"]}, seaLevel: 29, '
                f'utm: {{ eMin: {G["e_min"]:.3f}, nMax: {G["n_max"]:.3f}, colMeters: {G["col_m"]:.4f}, rowMeters: {G["row_m"]:.4f} }}, '
                f'data: "{base64.b64encode(g.tobytes()).decode()}" }};\n')
    print(path, G["width"], "x", G["height"], os.path.getsize(path) // 1024, "KB")
