"""Weltkarte: berechnet Ausschnitt, Auflösung, Höhenkodierung und GDAL-Befehle.

Aufruf:  python worldmap.py            -> schreibt worldmap/worldmap_meta.json und worldmap/build_heightmap.bat/.sh
Danach die .bat (Windows, OSGeo4W-Shell aus QGIS) oder .sh ausführen. Sie erzeugt aus einem Höhenmodell
(GeoTIFF, WGS84) das Höhenraster im Kartenausschnitt; build_webmap.py macht daraus die Browser-Daten.
"""
import json, math, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # Repo-Wurzel
from geo import to_utm, from_utm

# ---------------- Einstellungen ----------------
LON_W, LON_E = 7.1529, 14.2529          # Kartenausschnitt (wie bisherige Höhenkarte)
LAT_S, LAT_N = 50.9856, 54.8190
WIDTH = 2017                             # Breite in Höhenpunkten (63*32+1; Höhe wird auf Vielfache von 63 gerundet)
QUADS = 63                               # Quads pro Komponente (1 Section, 63x63)
H_MIN, H_MAX = -100.0, 1200.0            # feste Höhenspanne in Metern (Ostsee/Nordsee-Senken bis Brocken 1141 m)
DEM_IN = "dem_wgs84.tif"                 # Eingabe: Höhenmodell in WGS84 (z. B. SRTM15+ von OpenTopography), mit 0,5° Rand
# ------------------------------------------------

def bounds():
    """Umschließendes UTM-Rechteck des geografischen Ausschnitts (Ränder dicht abgetastet)."""
    pts = []
    for i in range(201):
        f = i / 200
        lon = LON_W + f * (LON_E - LON_W); lat = LAT_S + f * (LAT_N - LAT_S)
        pts += [to_utm(LAT_N, lon), to_utm(LAT_S, lon), to_utm(lat, LON_W), to_utm(lat, LON_E)]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return min(xs), max(xs), min(ys), max(ys)

def layout():
    e0, e1, n0, n1 = bounds()
    res = (e1 - e0) / (WIDTH - 1)                         # Meter pro Vertex
    rows = math.ceil((n1 - n0) / res)                     # nötige Höhe in Quads
    height = math.ceil(rows / QUADS) * QUADS + 1          # auf ganze Komponenten aufrunden
    pad = ((height - 1) * res - (n1 - n0)) / 2            # Rest gleichmäßig oben/unten
    return dict(e_min=e0, e_max=e1, n_min=n0 - pad, n_max=n1 + pad, res=res, width=WIDTH, height=height)

def to_map(lat, lon, L):
    """Geografisch -> Kartenkoordinaten: Pixel (x nach Osten, y nach Süden) und km ab NW-Ecke."""
    E, N = to_utm(lat, lon)
    px, py = (E - L["e_min"]) / L["res"], (L["n_max"] - N) / L["res"]
    return dict(px=px, py=py, km_e=(E - L["e_min"]) / 1000, km_s=(L["n_max"] - N) / 1000)

def sea_level_16bit():
    """Meeresspiegel als 16-Bit-Wert der Höhenkodierung."""
    return round((0 - H_MIN) / (H_MAX - H_MIN) * 65535)

def gdal_commands(L):
    # Jedes Pixel ist ein Vertex (Mittelpunkt). GDAL: -te sind Pixelkanten -> um einen halben Pixel erweitern
    h = L["res"] / 2
    te = f'{L["e_min"]-h:.3f} {L["n_min"]-h:.3f} {L["e_max"]+h:.3f} {L["n_max"]+h:.3f}'
    return [
        f'gdalwarp -overwrite -t_srs EPSG:25832 -te {te} -tr {L["res"]:.6f} {L["res"]:.6f} -r cubic '
        f'-dstnodata -9999 -ot Float32 -co COMPRESS=NONE {DEM_IN} dem_utm32.tif',
    ]

if __name__ == "__main__":
    L = layout()
    OUTD = os.path.join(ROOT, "tools", "worldmap_out"); os.makedirs(OUTD, exist_ok=True)
    cmds = gdal_commands(L)
    open(os.path.join(OUTD, "build_heightmap.bat"), "w", newline="\r\n").write(
        "@echo off\nREM In der OSGeo4W-Shell (QGIS) im Ordner mit dem_wgs84.tif ausfuehren\n" + "\n".join(cmds) + "\necho Fertig: dem_utm32.tif - weiter mit: python build_webmap.py --dem dem_utm32.tif\n")
    open(os.path.join(OUTD, "build_heightmap.sh"), "w").write("#!/bin/sh\nset -e\n" + "\n".join(cmds) + "\necho 'Fertig: dem_utm32.tif - weiter mit: python build_webmap.py --dem dem_utm32.tif'\n")
    meta = dict(crs="EPSG:25832 (ETRS89 / UTM 32N)", geo_bounds=dict(lon=[LON_W, LON_E], lat=[LAT_S, LAT_N]),
                layout={k: (round(v, 3) if isinstance(v, float) else v) for k, v in L.items()},
                height_range_m=[H_MIN, H_MAX],
                sea_level_16bit=sea_level_16bit(), gdal=cmds)
    json.dump(meta, open(os.path.join(OUTD, "worldmap_meta.json"), "w"), indent=2, ensure_ascii=False)
    print(json.dumps(meta, indent=2, ensure_ascii=False))
    # Plausibilität: Verzerrung der alten Pixelkarte
    w_km = (L["e_max"] - L["e_min"]) / 1000; h_km = (to_utm(LAT_N, 10.75)[1] - to_utm(LAT_S, 10.75)[1]) / 1000
    print(f"Ausdehnung ~{w_km:.0f} x {h_km:.0f} km; alte Karte 1704x920 px -> Seitenverhältnis {1704/920:.2f} statt {w_km/h_km:.2f}")
