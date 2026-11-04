"""Bereitet die Daten der Browser-Weltkarte vor (liest die Textur-Sammlung nur, schreibt nichts hinein).

Eingaben:
  - alte Höhenkarte (Maps/Heightmap.png, 1704x920, 8 Bit, Grad-Raster, ab 450 m gekappt)
    -> wird ins neue UTM-Raster (worldmap.py) umgerechnet. Später durch die echte 16-Bit-Höhenkarte ersetzen.
  - Bodentexturen (Textures/Tiles/*/<Name>.png, 1024 px) -> 512-px-JPEGs fürs Web
Ausgabe (web/worldmap/):
  - terrain.png  RGBA: R/G = Höhe 16 Bit (hi/lo), B = Bodentyp-ID, A = 255
  - tex_<id>.jpg Bodentexturen, water.jpg, water_normal.jpg
  - map.json     Kennwerte, Bodentypen mit Durchschnittsfarbe, Orte, Begegnungen
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageFilter
from geo import from_utm_np, to_utm
from worldmap import layout, H_MIN, H_MAX, to_map
from campaign_data import PLACES, encounters

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--assets", required=True, help="Ordner mit Textures/ und Maps/ (wird nur gelesen)")
ap.add_argument("--dem", help="dem_utm32.tif aus worldmap.py/GDAL (Float32, exakt im Kartenraster). Ohne: alte 8-Bit-Karte umrechnen")
args = ap.parse_args()
SRC = args.assets
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "prototypes", "worldmap", "worldmap")
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(ROOT, "tools", "worldmap_out"), exist_ok=True)
L = layout()
W, H = L["width"], L["height"]

# ---------- 1. Höhe ----------
E = L["e_min"] + np.arange(W) * L["res"]
N = L["n_max"] - np.arange(H) * L["res"]
EE, NN = np.meshgrid(E, N)
lat, lon = from_utm_np(EE, NN)
if args.dem:
    # Echte Höhenkarte: liegt durch gdalwarp bereits exakt im Kartenraster
    h = np.asarray(Image.open(args.dem), dtype=np.float32)
    assert h.shape == (H, W), f"{args.dem}: {h.shape} statt {(H, W)} – mit den Befehlen aus worldmap.py erzeugen"
    inside = h > -9000
    h = np.where(inside, h, -40.0).astype(np.float32)
    SOURCE = f"Höhenmodell {os.path.basename(args.dem)} (16 Bit)"
else:
    # Übergang: alte 8-Bit-Karte (Grad-Raster, ab 450 m gekappt) ins UTM-Raster umrechnen
    old = np.asarray(Image.open(f"{SRC}/Maps/Heightmap.png").convert("L"), dtype=np.float32)
    old_m = old * 508.0 / 255.0 - 58.0
    oh, ow = old_m.shape
    px = (lon - 7.1529) * 240.0
    py = (54.8190 - lat) * 240.0
    inside = (px >= 0) & (py >= 0) & (px <= ow - 1) & (py <= oh - 1)
    x0 = np.clip(np.floor(px).astype(int), 0, ow - 2); y0 = np.clip(np.floor(py).astype(int), 0, oh - 2)
    fx = np.clip(px - x0, 0, 1); fy = np.clip(py - y0, 0, 1)
    h = (old_m[y0, x0] * (1-fx) * (1-fy) + old_m[y0, x0+1] * fx * (1-fy) +
         old_m[y0+1, x0] * (1-fx) * fy + old_m[y0+1, x0+1] * fx * fy).astype(np.float32)
    def blur(a, k=(0.06, 0.24, 0.40, 0.24, 0.06)):
        out = sum(w * np.roll(a, i - 2, 0) for i, w in enumerate(k))
        return sum(w * np.roll(out, i - 2, 1) for i, w in enumerate(k))
    h = blur(h)                                          # 2-m-Treppen der 8-Bit-Quelle glätten
    SOURCE = "Alte 8-Bit-Höhenkarte (ab 450 m gekappt), ins UTM-Raster umgerechnet"

# ---------- 2. Bodentypen (Platzhalter-Heuristik, bis echte Landbedeckung aus QGIS kommt) ----------
TYPES = [  # id, Name, Textur, Bedeutung auf der Karte
    (0, "Sand", "Sand/Sand.png", "Küste, Dünen, Watt"),
    (1, "WetEarth", "WetEarth/WetEarth.png", "Marsch, Flussauen"),
    (2, "GrassShort", "GrassShort/GrassShort.png", "Wiese, Weide"),
    (3, "DryEarth", "DryEarth/DryEarth.png", "Acker (Börde)"),
    (4, "Heather", "Heather/Heather.png", "Heide"),
    (5, "Bog", "Bog/Bog.png", "Hochmoor"),
    (6, "Swamp", "Swamp/Swamp.png", "Bruch, Niedermoor"),
    (7, "GrassTall", "GrassTall/GrassTall.png", "Wald, Dickicht (Platzhalter)"),
    (8, "RawStone", "RawStone/RawStone.png", "Geröll, Bergland"),
    (9, "Mud", "Mud/Mud.png", "Schlick"),
]
rng = np.random.default_rng(7)
def noise(scale, octaves=3):
    """Wertrauschen 0..1 in Kartenauflösung (glatt, über Bildskalierung)."""
    acc = np.zeros((H, W), np.float32); amp = 1.0; tot = 0
    for o in range(octaves):
        s = max(2, int(W / scale * 2**o))
        small = rng.random((max(2, int(s * H / W)), s)).astype(np.float32)
        acc += amp * np.asarray(Image.fromarray(small, mode="F").resize((W, H), Image.BILINEAR)); tot += amp; amp *= 0.5
    return np.clip(acc / tot, 0, 1)
n1, n2, n3 = noise(40), noise(25), noise(90)
gy, gx = np.gradient(h, L["res"])
slope = np.degrees(np.arctan(np.hypot(gx, gy)))
lat_c = lat
def near(la, lo, km):
    e, n = to_utm(la, lo); return np.hypot(EE - e, NN - n) < km * 1000
def dist_km(la, lo):
    e, n = to_utm(la, lo); return np.hypot(EE - e, NN - n) / 1000
heide = np.exp(-(dist_km(53.08, 10.0) / 45) ** 2)                  # Lüneburger Heide, weich auslaufend
south = 1 / (1 + np.exp(-(52.45 - lat_c) * 5))                     # Lössbörden im Süden, weicher Übergang
t = np.full((H, W), 2, np.uint8)                                    # Standard: Wiese
t[(h > 40) & (n1 > 0.56)] = 7                                       # Wälder auf der Geest
t[(h > 60) & (h < 170) & (n2 + 0.45 * south > 0.85)] = 3            # Börde-Äcker
t[(h > 20) & (n2 * 0.6 + heide * 0.9 > 0.72)] = 4                   # Heide um Wilsede/Soltau
t[(lat_c > 52.6) & (h > 30) & (n3 > 0.72)] = 4                      # verstreute Heiden
t[(h < 25) & (h > 1) & (slope < 0.15) & (lat_c > 52.4) & (n1 > 0.58)] = 5   # Hochmoore
t[(h < 15) & (h > 1) & (slope < 0.1) & (n2 > 0.62)] = 6             # Brüche
t[(h <= 4) & (h > 0.5)] = 1                             # Marsch
t[(h > 250)] = 7                                        # Mittelgebirge bewaldet
t[(h > 380) | ((slope > 4.0) & (h > 120))] = 8                        # Geröll: Harz-Höhen, Steilhänge
t[(h <= 0.5) & (h > -3)] = 0                            # Strand / Watt
t[(h <= -3) & (h > -12)] = 9                            # Schlick im Flachwasser
t[h <= -12] = 0                                         # tieferer Meeresgrund: Sand
t[~inside] = 255                                        # keine Daten in der alten Karte -> Kartenrand

# ---------- 3. Kodieren: R/G = Höhe 16 Bit, B = Typ ----------
q = np.clip((h - H_MIN) / (H_MAX - H_MIN) * 65535.0 + 0.5, 0, 65535).astype(np.uint16)
rgba = np.zeros((H, W, 4), np.uint8)
rgba[..., 0] = q >> 8; rgba[..., 1] = q & 255; rgba[..., 2] = t; rgba[..., 3] = 255
Image.fromarray(rgba, "RGBA").save(f"{OUT}/terrain.png", optimize=True)

# ---------- 4. Texturen ----------
types_out = []
for tid, name, rel, info in TYPES:
    im = Image.open(f"{SRC}/Textures/Tiles/{rel}").convert("RGB").resize((512, 512), Image.LANCZOS)
    im.save(f"{OUT}/tex_{tid}.jpg", quality=85)
    avg = np.asarray(im, np.float32).reshape(-1, 3).mean(0)
    types_out.append(dict(id=tid, name=name, info=info, avg=[round(float(c)) for c in avg],
                          share=round(float((t == tid).mean()) * 100, 1)))
for src, dst in (("World/Water.jpg", "water.jpg"), ("World/Water_normal.jpg", "water_normal.jpg")):
    Image.open(f"{SRC}/Textures/{src}").convert("RGB").save(f"{OUT}/{dst}", quality=88)

# ---------- 5. Metadaten ----------
def pt(la, lo):
    m = to_map(la, lo, L); return [round(m["px"], 2), round(m["py"], 2)]
meta = dict(width=W, height=H, res_m=L["res"], h_min=H_MIN, h_max=H_MAX,
            utm=dict(e_min=L["e_min"], n_max=L["n_max"]),
            types=types_out,
            places=[dict(name=n, lat=la, lon=lo, info=i, p=pt(la, lo)) for n, la, lo, i in PLACES],
            encounters=[dict(name=e["EncounterName"], pantheon=e["IsPantheon"], phase=e["Phase"], p=pt(e["Lat"], e["Lon"])) for e in encounters],
            source=SOURCE + "; Bodentypen = Platzhalter-Heuristik")
json.dump(meta, open(f"{OUT}/map.json", "w"), ensure_ascii=False)
print("terrain.png", os.path.getsize(f"{OUT}/terrain.png") // 1024, "KB;",
      "Höhe", round(float(h.min()), 1), "bis", round(float(h.max()), 1), "m;",
      "Typen", {x["name"]: x["share"] for x in types_out})
# Vorschau (nur zur Kontrolle)
pal = np.zeros((256, 3), np.uint8); pal[:len(types_out)] = [x["avg"] for x in types_out]; pal[255] = (28, 24, 20)
prev = pal[t].astype(np.float32)
shade = np.clip(1 + (np.roll(h, 1, 1) - h) * 0.08, 0.6, 1.4)[..., None]
prev = np.where((h <= 0)[..., None], np.array([40, 70, 100]), prev * shade)
Image.fromarray(np.clip(prev, 0, 255).astype(np.uint8)).resize((1008, 914)).save(os.path.join(ROOT, "tools", "worldmap_out", "preview.png"))
