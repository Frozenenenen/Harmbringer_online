"""Builds every game unit as a simple low-poly figure in one consistent style.

Figures are assembled from primitives (cylinders, cones, boxes, blobs) with a small palette
texture, written in the same GLB layout as slim_figures.py. Real proportions: a human is
about 1.8 units tall and looks along +Z. The game scales all figures by the same factor,
so dwarves, hounds, wisps and giants keep their relative size.

Usage: python tools/build_units.py            -> assets/figures/Generated/<unit>.glb
Then:  python tools/render_portraits.py && python tools/build_game_figures.py
"""
import math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_hounds import Mesh as _Mesh, write_glb, hound

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "figures", "Generated")

class Mesh(_Mesh):
    """Palette slots by color: every primitive takes a hex color."""
    def __init__(self):
        super().__init__([])
    def slot(self, c):
        if c not in self.pal: self.pal.append(c)
        return self.pal.index(c)
    def B(self, center, size, c, rot_x=0.0): self.box(center, size, self.slot(c), rot_x)
    def C(self, p0, p1, r0, r1, c, seg=6): self.cyl(p0, p1, r0, r1, self.slot(c), seg)
    def O(self, center, radii, c, rings=5, seg=8): self.blob(center, radii, self.slot(c), rings, seg)

# ---------------------------------------------------------------- body parts
R_HAND, L_HAND = (0.27, 0.92, 0.12), (-0.27, 0.92, 0.12)

def legs(m, col, boot, spread=0.09, top=0.86, r=0.065):
    for sx in (-1, 1):
        m.C((sx * spread, top, 0), (sx * spread * 1.1, 0.07, 0.02), r * 1.1, r * 0.85, col)
        m.B((sx * spread * 1.1, 0.04, 0.05), (0.1, 0.08, 0.18), boot)

def torso(m, col, w=0.36, h=0.52, d=0.22, y0=0.86, belt=None):
    m.B((0, y0 + h / 2, 0), (w, h, d), col)
    if belt: m.B((0, y0 + 0.05, 0), (w + 0.02, 0.06, d + 0.02), belt)

def arms(m, col, hand, w=0.36, y=1.32, r=(0.27, 0.92, 0.12), l=(-0.27, 0.92, 0.12), rr=0.055):
    for sx, h in ((1, r), (-1, l)):
        m.C((sx * (w / 2 + 0.03), y, 0), h, rr, rr * 0.85, col)
        m.O(h, (rr * 1.1, rr * 1.1, rr * 1.1), hand, 3, 5)

def head(m, skin, y=1.52, hair=None, beard=None, eyes="#1a1410"):
    m.O((0, y, 0.01), (0.11, 0.13, 0.12), skin)
    for sx in (-1, 1): m.B((sx * 0.04, y + 0.02, 0.115), (0.025, 0.02, 0.01), eyes)
    if hair: m.O((0, y + 0.05, -0.02), (0.12, 0.1, 0.12), hair)
    if beard: m.C((0, y - 0.04, 0.08), (0, y - 0.24, 0.1), 0.08, 0.01, beard)

def skull(m, y=1.52, bone="#e4dcc6", eyes="#1a1010"):
    m.O((0, y, 0.0), (0.1, 0.12, 0.11), bone)
    m.B((0, y - 0.1, 0.04), (0.12, 0.05, 0.1), bone)                       # jaw
    for sx in (-1, 1): m.B((sx * 0.04, y + 0.01, 0.1), (0.035, 0.035, 0.02), eyes)

def robe(m, col, top=1.08, r_top=0.2, r_bot=0.33, bot=0.02):
    m.C((0, top, 0), (0, bot, 0), r_top, r_bot, col, seg=8)

def hood(m, col, y=1.54):
    m.O((0, y + 0.02, -0.03), (0.15, 0.16, 0.16), col)
    m.C((0, y + 0.1, -0.08), (0, y + 0.3, -0.18), 0.08, 0.0, col, seg=5)

def cloak(m, col, top=1.36, bot=0.12, w=0.44):
    m.B((0, (top + bot) / 2, -0.14), (w, top - bot, 0.04), col, rot_x=-0.08)

def skeleton(m, bone="#e4dcc6", dark="#2a2420"):
    for sx in (-1, 1):                                                       # legs
        m.C((sx * 0.08, 0.86, 0), (sx * 0.085, 0.45, 0.02), 0.032, 0.03, bone)
        m.C((sx * 0.085, 0.45, 0.02), (sx * 0.09, 0.06, 0.0), 0.03, 0.026, bone)
        m.B((sx * 0.09, 0.03, 0.05), (0.07, 0.04, 0.14), bone)
    m.B((0, 0.88, 0), (0.24, 0.08, 0.12), bone)                              # pelvis
    m.C((0, 0.9, -0.03), (0, 1.38, -0.03), 0.03, 0.03, bone)                 # spine
    for k in range(4):                                                       # ribs
        y = 1.08 + k * 0.08
        m.C((-0.14, y, 0.0), (0.14, y, 0.0), 0.022, 0.022, bone, seg=4)
        for sx in (-1, 1): m.C((sx * 0.14, y, 0.0), (sx * 0.06, y - 0.02, 0.1), 0.02, 0.02, bone, seg=4)
    m.B((0, 1.4, -0.02), (0.36, 0.05, 0.1), bone)                            # shoulders
    skull(m, 1.53, bone, dark)

def ghost_body(m, col, top=1.36, w=0.24):
    m.O((0, top - 0.12, 0), (w, 0.22, 0.17), col)
    m.C((0, top - 0.2, 0), (0, 0.25, -0.05), w * 0.95, 0.03, col, seg=8)    # tapering tail
    for k, (x, z) in enumerate(((0.12, 0.05), (-0.12, 0.05), (0.0, -0.12))):
        m.C((x, 0.62, z), (x * 1.3, 0.3, z * 1.2 - 0.05), 0.06, 0.0, col, seg=4)   # ragged trails

def wisp(m, glow, core, y=0.9, r=0.22):
    m.O((0, y, 0), (r, r * 1.15, r), glow, 5, 10)
    m.O((0, y, 0), (r * 0.5, r * 0.55, r * 0.5), core, 4, 8)
    for a in range(5):
        ang = a * 2 * math.pi / 5
        m.C((math.cos(ang) * r * 0.6, y + r * 0.6, math.sin(ang) * r * 0.6), (math.cos(ang) * r * 0.3, y + r * 1.8, math.sin(ang) * r * 0.3), r * 0.18, 0.0, glow, seg=4)

# ---------------------------------------------------------------- gear
def spear(m, hand=R_HAND, wood="#6a4a2a", tip="#b8b8b8", length=2.1):
    x, y, z = hand
    m.C((x, 0.05, z), (x, 0.05 + length, z), 0.022, 0.02, wood, seg=5)
    m.C((x, 0.05 + length, z), (x, 0.05 + length + 0.22, z), 0.05, 0.0, tip, seg=4)

def staff(m, hand=R_HAND, wood="#4a3420", orb=None, top_skull=False, length=1.9):
    x, y, z = hand
    m.C((x, 0.03, z), (x, length, z), 0.028, 0.024, wood, seg=5)
    if orb: m.O((x, length + 0.08, z), (0.08, 0.08, 0.08), orb, 4, 6)
    if top_skull: skull(m, length + 0.07, "#e4dcc6")  if False else m.O((x, length + 0.08, z), (0.07, 0.08, 0.07), "#e4dcc6", 4, 6)

def sword(m, hand=R_HAND, blade="#c0c0c8", hilt="#5a4a2a", length=0.85, up=True):
    x, y, z = hand
    m.B((x, y, z + 0.02), (0.18, 0.03, 0.04), hilt)
    if up: m.B((x, y + 0.04 + length / 2, z + 0.02), (0.05, length, 0.015), blade)
    else: m.B((x, y - 0.04 - length / 2, z + 0.12), (0.05, length, 0.015), blade, rot_x=0.4)

def shield(m, hand=L_HAND, face="#7a2a2a", rim="#8a8a8a", round_=True, r=0.24):
    x, y, z = hand
    if round_:
        m.C((x - 0.03, y + 0.05, z + 0.02), (x - 0.03, y + 0.05, z + 0.08), r, r, rim, seg=10)
        m.C((x - 0.03, y + 0.05, z + 0.08), (x - 0.03, y + 0.05, z + 0.1), r * 0.85, r * 0.85, face, seg=10)
    else:
        m.B((x - 0.03, y + 0.02, z + 0.06), (0.06, 0.5, 0.34), face)
        m.B((x - 0.06, y + 0.02, z + 0.06), (0.02, 0.52, 0.36), rim)

def bow(m, hand=L_HAND, wood="#7a5a30"):
    x, y, z = hand
    for a, b in ((0.0, 0.5), (0.0, -0.5)):
        m.C((x, y, z + 0.05), (x, y + b, z - 0.12), 0.02, 0.014, wood, seg=4)
    m.C((x, y + 0.5, z - 0.12), (x, y - 0.5, z - 0.12), 0.006, 0.006, "#d8d0b8", seg=3)

def crossbow(m, wood="#6a4a2a", steel="#9a9aa0"):
    m.B((0.0, 1.02, 0.3), (0.06, 0.06, 0.5), wood)
    m.B((0.0, 1.04, 0.5), (0.6, 0.03, 0.04), steel)

def hammer(m, hand=R_HAND, wood="#5a3a20", head_="#8a8a90", length=1.0):
    x, y, z = hand
    m.C((x, y - 0.3, z), (x, y + length - 0.3, z), 0.03, 0.03, wood, seg=5)
    m.B((x, y + length - 0.28, z), (0.24, 0.14, 0.14), head_)

def pitchfork(m, hand=R_HAND):
    x, y, z = hand
    m.C((x, 0.05, z), (x, 1.75, z), 0.022, 0.022, "#7a5a30", seg=5)
    m.B((x, 1.77, z), (0.18, 0.03, 0.03), "#6a6a6a")
    for dx in (-0.08, 0.0, 0.08): m.C((x + dx, 1.77, z), (x + dx, 1.98, z), 0.012, 0.004, "#6a6a6a", seg=3)

def helmet_kettle(m, col="#8a8a90", y=1.6):
    m.C((0, y, 0), (0, y + 0.02, 0), 0.22, 0.22, col, seg=10)
    m.O((0, y + 0.04, 0), (0.13, 0.1, 0.13), col)

def helmet_great(m, col="#a0a0a8", y=1.52, slit="#1a1a1a"):
    m.B((0, y + 0.02, 0.0), (0.24, 0.3, 0.26), col)
    m.B((0, y + 0.04, 0.131), (0.18, 0.025, 0.005), slit)

def crown(m, col="#c9a227", y=1.66, r=0.11, spikes=5):
    m.C((0, y, 0), (0, y + 0.06, 0), r, r, col, seg=10)
    for k in range(spikes):
        a = k * 2 * math.pi / spikes
        m.C((math.cos(a) * r, y + 0.06, math.sin(a) * r), (math.cos(a) * r, y + 0.14, math.sin(a) * r), 0.025, 0.0, col, seg=3)

def witch_hat(m, col="#2a2030", y=1.64):
    m.C((0, y, 0), (0, y + 0.02, 0), 0.26, 0.26, col, seg=12)
    m.C((0, y + 0.02, 0), (0.02, y + 0.5, -0.08), 0.13, 0.0, col, seg=8)

def horns(m, col="#d8ccb0", y=1.62):
    for sx in (-1, 1): m.C((sx * 0.08, y, 0), (sx * 0.22, y + 0.2, -0.05), 0.04, 0.0, col, seg=5)

def antlers(m, col="#8a6a40", y=1.64):
    for sx in (-1, 1):
        m.C((sx * 0.07, y, 0), (sx * 0.24, y + 0.32, -0.02), 0.025, 0.012, col, seg=4)
        m.C((sx * 0.17, y + 0.2, -0.01), (sx * 0.12, y + 0.36, 0.06), 0.015, 0.0, col, seg=3)
        m.C((sx * 0.21, y + 0.27, -0.02), (sx * 0.3, y + 0.4, -0.06), 0.013, 0.0, col, seg=3)

def mitre(m, col="#e8e0c8", y=1.62):
    m.C((0, y, 0), (0, y + 0.3, 0), 0.11, 0.03, col, seg=6)

def cross(m, col="#c9a227", at=(0, 1.2, 0.12)):
    x, y, z = at
    m.B((x, y, z), (0.03, 0.18, 0.02), col); m.B((x, y + 0.03, z), (0.12, 0.03, 0.02), col)

# ---------------------------------------------------------------- archetypes
def human(skin="#c89a78", shirt="#6a5a40", pants="#4a3a2a", boots="#3a2a1a", **kw):
    m = Mesh()
    legs(m, pants, boots); torso(m, shirt, belt=kw.get("belt")); arms(m, shirt, skin, r=kw.get("r", R_HAND), l=kw.get("l", L_HAND))
    head(m, skin, hair=kw.get("hair"), beard=kw.get("beard"))
    return m

def robed(robe_col, skin="#c89a78", sleeve=None, **kw):
    m = Mesh()
    robe(m, robe_col, r_bot=kw.get("r_bot", 0.33))
    torso(m, robe_col, w=0.34, h=0.42, y0=1.0, belt=kw.get("belt"))
    arms(m, sleeve or robe_col, skin, r=kw.get("r", R_HAND), l=kw.get("l", L_HAND), y=1.34)
    head(m, skin, hair=kw.get("hair"), beard=kw.get("beard"), eyes=kw.get("eyes", "#1a1410"))
    return m

def build(unit):
    U = {}
    # --- undead -------------------------------------------------------
    if unit == "lich":
        m = robed("#3a1e52", skin="#cfc4a8", sleeve="#2a1440", eyes="#7aff9a", belt="#c9a227")
        cloak(m, "#2a1440", w=0.5); crown(m, "#c9a227", y=1.62); staff(m, orb="#7aff9a", length=2.0)
        m.B((0, 1.5, 0.115), (0.08, 0.03, 0.01), "#2a1414")                    # gaunt mouth
        return m
    if unit == "skelett":
        m = Mesh(); skeleton(m); arms(m, "#e4dcc6", "#e4dcc6", rr=0.03); spear(m); shield(m, face="#5a4a3a", rim="#7a6a50", r=0.2); return m
    if unit == "bogner":
        m = Mesh(); skeleton(m); arms(m, "#e4dcc6", "#e4dcc6", rr=0.03, l=(-0.25, 1.15, 0.2)); bow(m, (-0.25, 1.15, 0.2)); return m
    if unit == "knochenschuetze":
        m = Mesh(); skeleton(m, bone="#d0c8a8"); arms(m, "#d0c8a8", "#d0c8a8", rr=0.03, l=(-0.25, 1.15, 0.2)); bow(m, (-0.25, 1.15, 0.2), "#3a2a1a")
        hood(m, "#4a4038", 1.55); cloak(m, "#4a4038"); return m
    if unit == "schleuderer":
        m = Mesh(); skeleton(m); arms(m, "#e4dcc6", "#e4dcc6", rr=0.03, r=(0.3, 1.6, -0.05))
        m.C((0.3, 1.6, -0.05), (0.32, 1.3, -0.15), 0.008, 0.008, "#6a5030", seg=3); m.O((0.32, 1.28, -0.15), (0.05, 0.05, 0.05), "#e4dcc6", 3, 5); return m
    if unit == "ghul":
        m = Mesh()
        for sx in (-1, 1):
            m.C((sx * 0.1, 0.62, -0.05), (sx * 0.12, 0.3, 0.12), 0.06, 0.05, "#7a8a6a"); m.C((sx * 0.12, 0.3, 0.12), (sx * 0.12, 0.04, -0.02), 0.05, 0.04, "#7a8a6a")
        m.O((0, 0.9, 0.12), (0.2, 0.26, 0.16), "#6b7d5a")                     # hunched torso
        m.O((0, 1.12, 0.3), (0.1, 0.11, 0.12), "#7a8a6a")
        for sx in (-1, 1): m.B((sx * 0.04, 1.14, 0.41), (0.03, 0.02, 0.01), "#e0e050")
        m.B((0, 1.06, 0.39), (0.1, 0.03, 0.04), "#3a1414")
        for sx in (-1, 1):
            m.C((sx * 0.2, 1.05, 0.15), (sx * 0.28, 0.5, 0.35), 0.045, 0.035, "#7a8a6a")
            for k in (-0.03, 0.0, 0.03): m.C((sx * 0.28 + k, 0.5, 0.35), (sx * 0.3 + k, 0.4, 0.42), 0.012, 0.0, "#d8d0b8", seg=3)
        m.B((0, 0.6, 0.02), (0.3, 0.14, 0.2), "#5a2a2a")                      # rags
        return m
    if unit == "zombie":
        m = human(skin="#8a9a72", shirt="#5a4a3a", pants="#3a3428", boots="#2a241e", r=(0.24, 1.2, 0.42), l=(-0.24, 1.2, 0.42), hair="#2a2a20")
        m.B((0.1, 1.05, 0.12), (0.12, 0.1, 0.01), "#6a2a2a"); return m
    if unit == "leichenhund": return hound("#6f6f5a", "#4a4a3c", "#9be05a", bone="#d8d0b8", gaunt=True)
    if unit == "geist":
        m = Mesh(); ghost_body(m, "#b8d4e0"); hood(m, "#a8c4d4", 1.46)
        arms(m, "#b8d4e0", "#c8e0ea", y=1.3, r=(0.25, 1.25, 0.32), l=(-0.25, 1.25, 0.32)); m.B((0, 1.47, 0.14), (0.1, 0.03, 0.01), "#2a4a6a"); return m
    if unit == "moorleiche":
        m = human(skin="#5a4630", shirt="#4a3a24", pants="#3a2c1c", boots="#2a2014", hair="#3a2a18")
        m.O((0, 1.3, 0.12), (0.2, 0.12, 0.08), "#3a5a2a"); m.B((0, 1.0, 0.0), (0.4, 0.06, 0.24), "#2a4a20"); return m   # moss
    if unit == "todesritter":
        m = human(skin="#cfc4a8", shirt="#2a2a32", pants="#1e1e24", boots="#14141a"); helmet_great(m, "#3a3a44", slit="#ff4a2a")
        m.B((0, 1.41, 0), (0.46, 0.08, 0.26), "#3a3a44"); cloak(m, "#4a1414"); sword(m, blade="#5a6a5a", length=1.0); shield(m, face="#1e1e24", rim="#5a5a64", round_=False); return m
    if unit == "totenlicht":
        m = Mesh(); wisp(m, "#7fd04a", "#e8ffb0"); return m
    if unit == "gefallene_schwester":
        m = robed("#2a2a34", skin="#b8b0a0", eyes="#9a2a2a"); hood(m, "#1a1a22", 1.53); m.B((0, 1.36, 0.115), (0.2, 0.18, 0.01), "#d8d0c0")
        cross(m, "#5a5a5a", (0, 1.18, 0.12)); staff(m, length=1.5, orb="#6a3a8a"); return m
    if unit == "grabdruidin":
        m = robed("#3a4a2a", skin="#a89880", hair="#d8d8c8", eyes="#9be05a"); antlers(m, "#e4dcc6", 1.6); staff(m, orb="#9be05a", length=1.85)
        m.C((0, 1.42, 0.1), (0, 1.42, 0.12), 0.12, 0.12, "#c9a227", seg=8); return m
    if unit == "nekromant":
        m = robed("#1e1428", skin="#b8b0a0", sleeve="#140e1c", eyes="#9be05a"); hood(m, "#140e1c", 1.53); cloak(m, "#140e1c")
        staff(m, length=1.95); m.O((R_HAND[0], 2.03, R_HAND[2]), (0.08, 0.09, 0.08), "#e4dcc6", 4, 6)
        m.B((L_HAND[0], L_HAND[1] + 0.02, L_HAND[2] + 0.06), (0.16, 0.2, 0.05), "#4a1a1a"); return m       # tome
    if unit == "knochenballiste":
        return ballista("#d0c8a8", "#a89a7a", "#e4dcc6", skulls=True)
    if unit == "fleischriese":
        m = Mesh()
        for sx in (-1, 1): m.C((sx * 0.22, 1.1, 0), (sx * 0.25, 0.1, 0.03), 0.16, 0.13, "#b07a6a"); m.B((sx * 0.25, 0.06, 0.06), (0.24, 0.12, 0.32), "#6a4a3a")
        m.O((0, 1.55, 0.05), (0.5, 0.55, 0.38), "#b88070")
        for k in range(4): m.B((0.05 * k - 0.1, 1.5 + 0.12 * k - 0.15, 0.4), (0.3, 0.015, 0.01), "#4a2a2a")      # stitches
        m.O((0, 2.15, 0.15), (0.17, 0.17, 0.16), "#a87060")
        for sx in (-1, 1): m.B((sx * 0.06, 2.18, 0.31), (0.04, 0.03, 0.01), "#e0e050")
        for sx in (-1, 1):
            m.C((sx * 0.5, 1.85, 0.0), (sx * 0.62, 1.0, 0.25), 0.13, 0.11, "#b07a6a"); m.O((sx * 0.62, 0.92, 0.27), (0.13, 0.13, 0.13), "#a07060", 3, 6)
        hammer(m, (0.62, 0.92, 0.27), head_="#6a6a6a", length=1.3); return m
    if unit == "totenjaeger":
        m = Mesh(); skeleton(m, bone="#cfc4a8"); arms(m, "#cfc4a8", "#cfc4a8", rr=0.03); cloak(m, "#2a3a2a"); antlers(m, "#6a4a2a", 1.62)
        spear(m, wood="#3a2a1a", tip="#7a8a7a"); m.O((0, 1.4, -0.02), (0.22, 0.08, 0.14), "#2a3a2a"); return m
    # --- people -------------------------------------------------------
    if unit == "bauer":
        m = human(shirt="#8a7a5a", pants="#5a4a32", hair="#6a4a2a", belt="#4a3a22"); pitchfork(m)
        m.C((0, 1.63, 0), (0, 1.65, 0), 0.22, 0.22, "#d8c070", seg=10); m.C((0, 1.65, 0), (0, 1.74, 0), 0.12, 0.08, "#d8c070", seg=8); return m
    if unit == "stadtwache":
        m = human(shirt="#8a2f2f", pants="#3a3a3a", boots="#2a2a2a", belt="#3a2a1a"); helmet_kettle(m)
        m.B((0, 1.12, 0.0), (0.38, 0.54, 0.24), "#8a8a90"); m.B((0, 1.1, 0.125), (0.26, 0.5, 0.01), "#8a2f2f"); spear(m); return m
    if unit == "armbrust":
        m = human(shirt="#9a5a2a", pants="#4a3a2a", r=(0.12, 1.02, 0.5), l=(-0.12, 1.02, 0.3), belt="#3a2a1a"); helmet_kettle(m, "#7a7a80")
        crossbow(m); m.B((-0.24, 1.0, -0.12), (0.1, 0.36, 0.1), "#5a3a20"); return m
    if unit == "ritter":
        m = human(skin="#c89a78", shirt="#c2c2c8", pants="#a0a0a8", boots="#7a7a80"); helmet_great(m)
        m.B((0, 1.4, 0), (0.48, 0.08, 0.28), "#b0b0b8"); m.B((0, 1.12, 0.125), (0.3, 0.5, 0.01), "#c9a227")
        sword(m); shield(m, face="#c9a227", rim="#7a7a80", round_=False); return m
    if unit == "balliste":
        return ballista("#6e5536", "#4a3a24", "#9a9aa0")
    if unit == "moench":
        m = robed("#5b4632", belt="#c8b890", hair="#6a5030"); hood(m, "#4b3a28", 1.53)
        m.B((L_HAND[0], L_HAND[1] + 0.02, L_HAND[2] + 0.06), (0.15, 0.2, 0.05), "#7a2a2a"); cross(m, "#c9a227"); return m
    if unit == "priester":
        m = robed("#e6e0cc", belt="#c9a227", hair="#8a8070"); mitre(m); staff(m, wood="#c9a227", orb="#f0e8c0", length=1.9); cross(m, "#c9a227", (0, 1.25, 0.12)); return m
    if unit == "kleriker":
        m = robed("#d8d0b8", sleeve="#b8b0a0", hair="#5a4030", belt="#7a5a30"); cross(m, "#9a2a2a", (0, 1.25, 0.12))
        hammer(m, head_="#b8b0a0", length=0.8); m.B((0, 1.22, 0.115), (0.08, 0.4, 0.01), "#9a2a2a"); return m
    if unit == "heideschwester":
        m = robed("#8a6478", hair="#3a2a20", belt="#e0d0b0"); hood(m, "#7a5468", 1.53); m.B((0, 1.36, 0.115), (0.2, 0.16, 0.01), "#e8e0d0")
        m.O((L_HAND[0], L_HAND[1] + 0.05, L_HAND[2] + 0.05), (0.08, 0.06, 0.08), "#b07a9a", 3, 6); cross(m, "#c9a227", (0, 1.15, 0.12)); return m
    if unit == "rattenfaenger":
        m = human(shirt="#b0422e", pants="#d0a030", boots="#3a2a1a", hair="#6a4a2a", r=(0.1, 1.48, 0.2), l=(-0.1, 1.48, 0.2))
        m.B((-0.09, 1.0, 0.0), (0.18, 0.3, 0.23), "#d0a030"); m.C((0.12, 1.48, 0.2), (-0.08, 1.48, 0.42), 0.02, 0.02, "#d8d0b8", seg=5)
        m.C((0, 1.63, 0), (0, 1.66, 0), 0.2, 0.2, "#3a6a3a", seg=10); m.O((0, 1.7, 0), (0.12, 0.08, 0.12), "#3a6a3a")
        m.C((0.08, 1.72, -0.05), (0.22, 2.0, -0.2), 0.02, 0.0, "#e0d040", seg=4)
        for x, z in ((0.3, 0.2), (-0.32, 0.1), (0.2, -0.3)): m.O((x, 0.06, z), (0.05, 0.05, 0.1), "#4a4a44", 3, 5); m.C((x, 0.05, z - 0.1), (x, 0.04, z - 0.25), 0.01, 0.0, "#6a5a5a", seg=3)
        return m
    # --- witches and mythic -----------------------------------------------
    if unit == "hexe":
        m = robed("#43364f", skin="#b8a888", hair="#2a2a2a"); witch_hat(m, "#2a2030"); staff(m, wood="#5a4a3a", orb="#8a5bb0", length=1.6)
        m.B((0, 1.08, 0.0), (0.36, 0.05, 0.24), "#8a5bb0"); return m
    if unit == "brockenhexe":
        m = robed("#1d1d1d", skin="#a89880", sleeve="#141414", eyes="#ff4a2a", r_bot=0.4); cloak(m, "#3a1414", w=0.6); horns(m, "#1d1d1d", 1.62)
        crown(m, "#8a1a1a", 1.64, 0.12, 7); staff(m, wood="#1d1d1d", orb="#ff4a2a", length=2.1); return m
    if unit == "irrlicht":
        m = Mesh(); wisp(m, "#e0e870", "#ffffd0"); return m
    if unit == "moorgeist":
        m = Mesh(); ghost_body(m, "#3a4a3a", top=1.4, w=0.28); m.O((0, 1.44, 0.02), (0.12, 0.13, 0.12), "#4a5a44")
        for sx in (-1, 1): m.B((sx * 0.04, 1.46, 0.13), (0.03, 0.02, 0.01), "#d0e060")
        arms(m, "#3a4a3a", "#4a5a44", y=1.3, r=(0.3, 0.9, 0.25), l=(-0.3, 0.9, 0.25))
        m.O((0, 1.2, 0.1), (0.26, 0.08, 0.12), "#2a4a20"); return m
    if unit == "druide":
        m = robed("#4f6a3a", hair="#d8d8d0", beard="#d8d8d0", belt="#8a6a3a"); staff(m, orb="#9ad06a", length=1.85)
        m.C((0, 1.62, 0), (0, 1.65, 0), 0.12, 0.12, "#5a8a3a", seg=8); return m
    if unit == "druidin":
        m = robed("#6a8a4a", hair="#c88a4a", belt="#c9a227"); staff(m, wood="#6a4a2a", orb="#c9e07a", length=1.8)
        m.C((0, 1.62, 0), (0, 1.66, 0), 0.12, 0.12, "#c9a227", seg=8); cloak(m, "#4a6a3a"); return m
    if unit == "heidekoenigin":
        m = robed("#a0607a", hair="#5a3a2a", r_bot=0.42, belt="#c9a227"); cloak(m, "#7a4a5a", w=0.6); crown(m, "#c9a227", 1.62, 0.12, 6)
        for k in range(6):
            a = k * math.pi / 3; m.O((math.cos(a) * 0.12, 1.75, math.sin(a) * 0.12), (0.04, 0.04, 0.04), "#c06a9a", 2, 4)
        staff(m, wood="#6a4a2a", orb="#e07ab0", length=1.9); return m
    if unit == "wode":
        m = human(skin="#b08a6a", shirt="#3a4a6a", pants="#2a2a3a", boots="#1e1e24", hair="#8a8a8a", beard="#9a9a9a", belt="#5a3a20")
        m.B((0, 1.12, 0.0), (0.4, 0.56, 0.25), "#4a5a7a"); cloak(m, "#2a2a3a", w=0.56); antlers(m, "#5a4a3a", 1.62); spear(m, length=2.3)
        m.B((0.05, 1.62, 0.1), (0.2, 0.06, 0.04), "#2a2a2a"); return m                         # eye patch band
    if unit == "zwergenkoenig":
        m = Mesh()
        for sx in (-1, 1): m.C((sx * 0.1, 0.48, 0), (sx * 0.11, 0.06, 0.02), 0.08, 0.07, "#4a3a2a"); m.B((sx * 0.11, 0.04, 0.05), (0.12, 0.08, 0.18), "#2a2018")
        m.B((0, 0.75, 0), (0.46, 0.55, 0.3), "#7a5a3a"); m.B((0, 0.52, 0.0), (0.48, 0.07, 0.32), "#c9a227")
        arms(m, "#7a5a3a", "#c89a78", w=0.46, y=0.95, r=(0.3, 0.62, 0.14), l=(-0.3, 0.62, 0.14), rr=0.07)
        head(m, "#c89a78", y=1.13, beard="#c87a3a"); m.C((0, 1.07, 0.1), (0, 0.6, 0.15), 0.13, 0.03, "#c87a3a")
        crown(m, "#c9a227", 1.22, 0.12, 5); hammer(m, (0.3, 0.62, 0.14), length=0.8); return m
    if unit == "schwarzer_hund": return hound("#1e1c1c", "#0e0d0d", "#ff3a1a")
    raise KeyError(unit)

def ballista(wood, dark, metal, skulls=False):
    m = Mesh()
    m.B((0, 0.35, 0), (0.7, 0.12, 1.6), wood)                                  # frame
    for sx in (-1, 1):
        for z in (-0.55, 0.55): m.C((sx * 0.38, 0.3, z), (sx * 0.46, 0.3, z), 0.2, 0.2, dark, seg=8)   # wheels
    m.C((0, 0.42, -0.1), (0, 0.9, 0.0), 0.05, 0.05, dark, seg=5)               # post
    m.B((0, 0.95, 0.05), (0.14, 0.12, 1.5), wood)                              # stock
    for sx in (-1, 1): m.C((0, 0.98, 0.65), (sx * 0.75, 1.05, 0.35), 0.04, 0.025, dark, seg=5)   # arms
    for sx in (-1, 1): m.C((sx * 0.75, 1.05, 0.35), (0, 1.0, -0.6), 0.006, 0.006, "#d8d0b8", seg=3)  # string
    m.C((0, 1.04, -0.5), (0, 1.04, 0.9), 0.02, 0.02, metal, seg=4); m.C((0, 1.04, 0.9), (0, 1.04, 1.05), 0.04, 0.0, metal, seg=4)
    if skulls:
        for z in (-0.6, -0.2, 0.2, 0.6): m.O((0.0, 0.48, z), (0.07, 0.08, 0.07), "#e4dcc6", 3, 6)
    return m

UNITS = ["lich", "ghul", "skelett", "bogner", "leichenhund", "zombie", "schleuderer", "geist", "bauer", "stadtwache", "armbrust",
         "ritter", "balliste", "moench", "priester", "hexe", "irrlicht", "moorgeist", "rattenfaenger", "brockenhexe", "kleriker",
         "heideschwester", "druide", "druidin", "schwarzer_hund", "wode", "zwergenkoenig", "heidekoenigin", "knochenschuetze",
         "moorleiche", "todesritter", "totenlicht", "gefallene_schwester", "grabdruidin", "nekromant", "knochenballiste",
         "fleischriese", "totenjaeger"]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for u in UNITS:
        m = build(u)
        p = os.path.join(OUT, u + ".glb"); t = write_glb(m, p)
        print(f"{u:20s} {t:5d} Dreiecke {os.path.getsize(p) // 1024:3d} KB")
