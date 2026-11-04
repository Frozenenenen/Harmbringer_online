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


# ---------------------------------------------------------------- mythic extras (Wodan cult, Spreewald, Wattenmeer)
def scaled(m, k):
    """Scale a finished figure about the ground point (small kobolds, giants)."""
    m.P = [np.asarray(p, float) * k for p in m.P]; return m

def sickle(m, hand=R_HAND, blade="#e8e8f0", wood="#6a4a2a"):
    x, y, z = hand
    m.C((x, y - 0.12, z), (x, y + 0.22, z + 0.04), 0.022, 0.02, wood, seg=4)
    pts = [(x, y + 0.22, z + 0.04)] + [(x, y + 0.22 + 0.34 * math.sin(a), z + 0.04 + 0.34 * (1 - math.cos(a)))
                                       for a in (0.6, 1.2, 1.8, 2.4, 2.9)]
    for i, (a, b) in enumerate(zip(pts, pts[1:])): m.C(a, b, 0.035 - i * 0.005, 0.03 - i * 0.005, blade, seg=3)

def lantern(m, hand=L_HAND, frame="#3a3428", glow="#e8f0a0"):
    x, y, z = hand
    m.C((x, y, z + 0.04), (x, y - 0.12, z + 0.06), 0.006, 0.006, frame, seg=3)
    m.B((x, y - 0.2, z + 0.06), (0.1, 0.14, 0.1), frame); m.O((x, y - 0.2, z + 0.06), (0.06, 0.06, 0.06), glow, 3, 6)

def horse(m, coat, mane, hoof="#2a2420", eye="#1a1410", saddle="#4a2a1a"):
    """Horse looking along +Z, back at about 1.4."""
    m.O((0, 1.15, 0), (0.26, 0.3, 0.62), coat)
    for sx in (-1, 1):
        for z in (0.42, -0.42):
            m.C((sx * 0.14, 1.0, z), (sx * 0.15, 0.5, z + 0.03), 0.075, 0.055, coat)
            m.C((sx * 0.15, 0.5, z + 0.03), (sx * 0.15, 0.07, z), 0.05, 0.045, coat)
            m.B((sx * 0.15, 0.04, z + 0.02), (0.1, 0.08, 0.12), hoof)
    m.C((0, 1.22, 0.48), (0, 1.75, 0.8), 0.15, 0.1, coat)                     # neck
    m.O((0, 1.8, 0.9), (0.1, 0.11, 0.14), coat); m.B((0, 1.7, 1.06), (0.13, 0.13, 0.26), coat, rot_x=0.5)
    for sx in (-1, 1):
        m.C((sx * 0.05, 1.88, 0.86), (sx * 0.06, 2.0, 0.83), 0.03, 0.0, coat, seg=3)
        m.B((sx * 0.09, 1.82, 0.97), (0.01, 0.03, 0.03), eye)
    m.C((0, 1.38, 0.42), (0, 1.94, 0.84), 0.05, 0.035, mane, seg=4)
    m.C((0, 1.3, -0.6), (0, 0.55, -0.82), 0.07, 0.02, mane, seg=5)            # tail
    m.B((0, 1.44, 0.0), (0.4, 0.06, 0.42), saddle)

def rider(m, skin, shirt, pants, boots, hand_r=(0.27, 1.6, 0.25), hand_l=(-0.27, 1.6, 0.25), hair=None, beard=None, eyes="#1a1410"):
    """Seated human on a horse built with horse()."""
    for sx in (-1, 1):
        m.C((sx * 0.1, 1.5, 0.05), (sx * 0.28, 1.3, 0.2), 0.07, 0.065, pants)
        m.C((sx * 0.28, 1.3, 0.2), (sx * 0.28, 0.9, 0.12), 0.06, 0.05, pants)
        m.B((sx * 0.28, 0.86, 0.16), (0.1, 0.08, 0.18), boots)
    torso(m, shirt, w=0.36, h=0.5, y0=1.47)
    arms(m, shirt, skin, y=1.93, r=hand_r, l=hand_l)
    head(m, skin, y=2.13, hair=hair, beard=beard, eyes=eyes)

def raven(m, at=(0, 1.0, 0), k=1.0, body="#141418", eye="#ff3a1a", beak="#2a2a2a"):
    x, y, z = at
    m.O((x, y, z), (0.1 * k, 0.09 * k, 0.2 * k), body)
    m.O((x, y + 0.07 * k, z + 0.18 * k), (0.07 * k, 0.07 * k, 0.08 * k), body)
    m.C((x, y + 0.06 * k, z + 0.25 * k), (x, y + 0.03 * k, z + 0.38 * k), 0.03 * k, 0.0, beak, seg=4)
    for sx in (-1, 1):
        m.B((x + sx * 0.04 * k, y + 0.09 * k, z + 0.24 * k), (0.015 * k, 0.015 * k, 0.01 * k), eye)
        sh = np.array((x + sx * 0.08 * k, y + 0.03 * k, z + 0.05 * k))
        for t, b in (((x + sx * 0.6 * k, y + 0.25 * k, z - 0.05 * k), (x + sx * 0.3 * k, y + 0.12 * k, z - 0.15 * k)),
                     ((x + sx * 0.3 * k, y + 0.12 * k, z - 0.15 * k), (x + sx * 0.08 * k, y, z - 0.12 * k))):
            m.tri(sh, np.array(t), np.array(b), m.slot(body)); m.tri(np.array(b), np.array(t), sh, m.slot(body))
    m.C((x, y, z - 0.15 * k), (x, y - 0.02 * k, z - 0.36 * k), 0.07 * k, 0.01 * k, body, seg=4)

def serpent(m, scale_col, belly, eye="#e0c030", tongue="#c02a2a"):
    """Coiled snake with raised head (Schlangenkönig)."""
    pts = []
    for i in range(30):
        a = i * 0.55; r = 0.55 - i * 0.011; pts.append((math.cos(a) * r, 0.1 + i * 0.018, math.sin(a) * r))
    pts += [(0.05, 0.75, 0.1), (0.0, 1.05, 0.15), (0.0, 1.3, 0.25)]
    for i, (a, b) in enumerate(zip(pts, pts[1:])):
        rr = 0.13 if i < 26 else 0.11 - (i - 26) * 0.01
        m.C(a, b, rr, rr, scale_col if i % 3 else belly, seg=6)
    hx, hy, hz = 0.0, 1.36, 0.36
    m.O((hx, hy, hz), (0.13, 0.09, 0.18), scale_col)
    for sx in (-1, 1): m.B((sx * 0.08, hy + 0.04, hz + 0.08), (0.03, 0.025, 0.03), eye)
    m.C((hx, hy - 0.03, hz + 0.17), (hx, hy - 0.04, hz + 0.32), 0.012, 0.004, tongue, seg=3)
    return hx, hy, hz

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
    if unit == "knochendrache": return bone_dragon()
    # --- Wodan cult -----------------------------------------------------
    if unit == "sachsenkrieger":
        m = human(skin="#c89a78", shirt="#6a5a3a", pants="#5a4a34", boots="#3a2a1a", hair="#c8a060", beard="#c8a060", belt="#3a2a1a")
        cloak(m, "#3a4a2a"); shield(m, face="#3a5a3a", rim="#6a4a2a", r=0.26); sword(m, length=0.55, blade="#a8a8a0")
        m.O((0, 1.66, 0), (0.12, 0.06, 0.12), "#7a7a80"); m.C((0, 1.6, 0.1), (0, 1.48, 0.13), 0.015, 0.015, "#7a7a80", seg=3); return m   # spangenhelm + nasal
    if unit == "wodansrabe":
        m = Mesh(); raven(m, (0.0, 1.25, 0.0), 1.0); raven(m, (0.45, 0.85, -0.25), 0.8); raven(m, (-0.4, 1.0, -0.15), 0.85); return m
    if unit == "wilder_jaeger":
        m = Mesh(); horse(m, "#5a6270", "#2a2e36", eye="#ff3a1a", saddle="#2a2420")
        rider(m, "#9aa4ae", "#4a525e", "#3a3e48", "#22252a", hand_r=(0.27, 1.62, 0.25), eyes="#ff3a1a")
        hood(m, "#3a3e48", 2.15); cloak(m, "#2a2e36", top=2.0, bot=1.3); spear(m, (0.27, 1.62, 0.25), wood="#3a2a1a", tip="#8a9aa0", length=2.4); return m
    if unit == "hackelberg":
        m = Mesh(); horse(m, "#2a2420", "#141010", eye="#ff4a1a", saddle="#6a1a1a")
        rider(m, "#b08a6a", "#5a3a2a", "#3a2a1e", "#1e1610", hair="#4a3a2a", beard="#4a3a2a", hand_l=(-0.2, 2.08, 0.25))
        m.O((0, 1.95, -0.06), (0.26, 0.1, 0.18), "#7a7a70"); cloak(m, "#5a1a1a", top=2.0, bot=1.25, w=0.5)            # wolf pelt + cloak
        m.C((0, 2.23, 0), (0, 2.26, 0), 0.18, 0.18, "#3a4a2a", seg=10); m.C((0, 2.26, 0), (0, 2.36, -0.04), 0.11, 0.07, "#3a4a2a", seg=8)
        m.C((-0.2, 2.08, 0.25), (-0.12, 2.18, 0.45), 0.02, 0.06, "#e0d0a0", seg=6)                                       # hunting horn
        spear(m, (0.27, 1.6, 0.25), wood="#4a3020", length=2.5); return m
    # --- Spreewald --------------------------------------------------------
    if unit == "lutki":
        m = human(skin="#c8a07a", shirt="#6a4a2a", pants="#4a3a2a", boots="#2a1e14", beard="#8a6a4a", belt="#2a1e14")
        m.C((0, 1.6, 0), (0.03, 1.98, -0.1), 0.14, 0.0, "#a02a20", seg=8); hammer(m, length=0.7, head_="#6a6a6a")
        return scaled(m, 0.55)
    if unit == "wassermann":
        m = human(skin="#7a9a8a", shirt="#2e6a3a", pants="#245a30", boots="#1a3a22", hair="#3a5a3a", beard="#4a6a4a", belt="#1a3a22")
        m.B((0, 0.75, -0.05), (0.42, 0.5, 0.26), "#2e6a3a")                                                            # long coat tails
        m.C((0, 1.63, 0), (0, 1.65, 0), 0.19, 0.19, "#a02a20", seg=10); m.C((0, 1.65, 0), (0, 1.86, 0), 0.12, 0.11, "#a02a20", seg=8)
        spear(m, wood="#4a4a3a", tip="#5a7a6a", length=1.9); m.C((0.27, 2.1, 0.12), (0.4, 1.95, 0.12), 0.015, 0.0, "#5a7a6a", seg=3)   # boat hook
        for x, y, z in ((0.15, 0.55, 0.14), (-0.18, 0.62, 0.1), (0.05, 1.0, 0.13), (-0.3, 0.86, 0.14)): m.O((x, y, z), (0.025, 0.04, 0.025), "#7ab0d0", 2, 4)
        return scaled(m, 1.1)
    if unit == "rusalka":
        m = robed("#d8e4dc", skin="#b8d0c8", hair="#3a5a4a", eyes="#4ac0b0", r_bot=0.28)
        m.B((0, 1.05, -0.14), (0.3, 0.9, 0.05), "#3a5a4a")                                                             # long hair down the back
        for k in range(7):
            a = k * 2 * math.pi / 7; m.O((math.cos(a) * 0.12, 1.64, math.sin(a) * 0.12), (0.035, 0.035, 0.035), "#e8e0f0" if k % 2 else "#d0c060", 2, 4)
        m.O((R_HAND[0], R_HAND[1] + 0.05, R_HAND[2]), (0.06, 0.06, 0.06), "#6ae0d0", 3, 6); return m
    if unit == "mittagsfrau":
        m = robed("#ece6d4", skin="#d8c8b0", hair="#e8e0c8", eyes="#6a2a1a", r_bot=0.36, belt="#c8b070")
        m.B((0, 1.2, -0.14), (0.26, 0.6, 0.04), "#e8e0c8"); m.C((0, 1.64, 0), (0, 1.66, 0), 0.22, 0.22, "#d8c070", seg=10)   # sun hat
        sickle(m); return scaled(m, 1.05)
    if unit == "schlangenkoenig":
        m = Mesh(); hx, hy, hz = serpent(m, "#3a6a3a", "#a8b060"); crown(m, "#e0b020", hy + 0.07, 0.075, 5)
        return scaled(m, 1.3)
    # --- Wattenmeer -------------------------------------------------------
    if unit == "ertrunkener":
        m = human(skin="#8a9aa0", shirt="#4a5a6a", pants="#3a3e44", boots="#2a2a2e", hair="#3a3a30", r=(0.27, 1.0, 0.2), l=(-0.24, 1.2, 0.42))
        for x, y in ((0.1, 1.3), (-0.12, 1.05), (0.15, 0.9)): m.B((x, y, 0.12), (0.06, 0.22, 0.01), "#3a6a3a")         # seaweed
        spear(m, (0.27, 1.0, 0.2), wood="#5a4a3a", tip="#6a4a3a", length=1.7); m.C((0.27, 1.85, 0.2), (0.4, 1.75, 0.2), 0.015, 0.0, "#6a4a3a", seg=3)
        return m
    if unit == "wasserleiche":
        m = human(skin="#7a8a80", shirt="#3a4440", pants="#2a302c", boots="#1e2220", hair="#2a3a2a", r=(0.24, 1.2, 0.42), l=(-0.24, 1.2, 0.42))
        for x, y in ((0.1, 1.3), (-0.12, 1.05), (0.15, 0.9), (0.0, 1.45)): m.B((x, y, 0.12), (0.06, 0.24, 0.01), "#2a5a2a")
        for sx in (-1, 1): m.B((sx * 0.04, 1.54, 0.125), (0.03, 0.02, 0.01), "#9be05a")
        m.C((0.0, 0.9, -0.15), (0.1, 0.35, -0.3), 0.012, 0.012, "#5a5a50", seg=3); m.B((0.1, 0.33, -0.3), (0.16, 0.12, 0.05), "#5a5a50")   # chain + anchor stone
        return m
    if unit == "wattjungfrau":
        m = robed("#9aaab0", skin="#c8d0d0", hair="#2a4a3a", eyes="#e8f0a0", r_bot=0.3)
        m.B((0, 1.0, -0.14), (0.3, 0.8, 0.05), "#2a4a3a"); lantern(m, (-0.27, 1.05, 0.2)); return m
    if unit == "klabautermann":
        m = human(skin="#d0a080", shirt="#2a3a6a", pants="#d8d0b8", boots="#2a2018", hair="#c0502a", beard="#c0502a", belt="#2a2018")
        m.C((0, 1.63, -0.02), (0, 1.66, -0.02), 0.2, 0.22, "#d8b030", seg=10); m.O((0, 1.7, 0), (0.12, 0.08, 0.12), "#d8b030")   # sou'wester
        hammer(m, length=0.6, head_="#5a4a3a"); m.C((-0.05, 1.46, 0.12), (-0.15, 1.42, 0.28), 0.012, 0.012, "#4a3020", seg=3)
        m.O((-0.15, 1.45, 0.29), (0.025, 0.03, 0.025), "#4a3020", 2, 4); return scaled(m, 0.6)                             # pipe
    if unit == "blanker_hans":
        m = Mesh()
        m.C((0, 1.2, 0), (0, 0.02, 0), 0.25, 0.55, "#2a5a7a", seg=10)                                                  # wave body
        for k, (y, r) in enumerate(((0.25, 0.58), (0.55, 0.48), (0.85, 0.38))): m.C((0, y, 0), (0, y + 0.07, 0), r, r * 0.9, "#e8f0f0", seg=10)  # foam crests
        torso(m, "#2e6a8a", w=0.42, h=0.5, y0=1.05); m.B((0, 1.3, 0.12), (0.3, 0.4, 0.02), "#3a7a9a")
        arms(m, "#2e6a8a", "#8ab0c0", w=0.42, y=1.48, r=(0.42, 1.95, 0.1), l=(-0.42, 1.95, 0.1), rr=0.07)
        head(m, "#8ab0c0", y=1.7, hair="#e8f0f0", beard="#e8f0f0", eyes="#e0ffff"); m.C((0, 1.62, 0.1), (0, 1.1, 0.16), 0.14, 0.03, "#e8f0f0")
        crown(m, "#e8f0f0", 1.82, 0.12, 7); spear(m, (0.42, 1.95, 0.1), wood="#6a6a60", tip="#c8d8d8", length=2.3)
        for x in (-0.1, 0.0, 0.1): m.C((0.42 + x, 2.25 + 0.05, 0.1), (0.42 + x, 2.5, 0.1), 0.02, 0.0, "#c8d8d8", seg=3)     # trident tines
        return scaled(m, 1.45)
    raise KeyError(unit)

def bone_dragon(bone="#e0d8c0", dark="#8a8070", glow="#7aff9a", membrane="#5a4a5a"):
    """Skeletal dragon: four legs, ribcage, long neck and tail, skull with horns, bone wings
    with torn membranes. About 2.6 tall at the wing tips, looks along +Z."""
    m = Mesh()
    m.C((0, 1.0, -0.6), (0, 1.15, 0.5), 0.05, 0.05, bone, seg=5)              # spine
    for k in range(6):                                                         # ribcage
        z = 0.35 - k * 0.15; r = 0.32 - abs(k - 2) * 0.04
        for sx in (-1, 1): m.C((0, 1.12, z), (sx * r, 0.82, z + 0.02), 0.03, 0.025, bone, seg=4); m.C((sx * r, 0.82, z + 0.02), (sx * r * 0.4, 0.62, z), 0.025, 0.02, bone, seg=4)
    m.B((0, 0.95, -0.62), (0.4, 0.12, 0.2), bone)                              # pelvis
    for sx in (-1, 1):                                                         # legs with claws
        for z, top in ((0.38, 1.05), (-0.62, 0.95)):
            knee = (sx * 0.34, 0.55, z + 0.12); foot = (sx * 0.36, 0.04, z + 0.05)
            m.C((sx * 0.2, top, z), knee, 0.06, 0.045, bone, seg=5); m.C(knee, foot, 0.045, 0.035, bone, seg=5)
            for dx in (-0.06, 0.0, 0.06): m.C(foot, (foot[0] + dx, 0.0, foot[2] + 0.16), 0.02, 0.0, dark, seg=3)
    pts = [(0, 1.15, 0.5), (0, 1.45, 0.75), (0, 1.75, 0.9), (0, 1.95, 1.05)]   # neck
    for a, b in zip(pts, pts[1:]): m.C(a, b, 0.06, 0.05, bone, seg=5)
    hx, hy, hz = 0, 2.0, 1.2                                                   # skull
    m.O((hx, hy, hz), (0.13, 0.12, 0.16), bone); m.B((hx, hy - 0.04, hz + 0.2), (0.14, 0.08, 0.26), bone); m.B((hx, hy - 0.11, hz + 0.18), (0.12, 0.04, 0.24), dark)
    for sx in (-1, 1):
        m.B((sx * 0.06, hy + 0.04, hz + 0.1), (0.04, 0.035, 0.03), glow)
        m.C((sx * 0.07, hy + 0.08, hz - 0.08), (sx * 0.16, hy + 0.32, hz - 0.3), 0.035, 0.0, dark, seg=4)
    tail = [(0, 0.98, -0.7), (0, 0.85, -1.1), (0, 0.6, -1.5), (0.1, 0.35, -1.85), (0.2, 0.2, -2.1)]
    for i, (a, b) in enumerate(zip(tail, tail[1:])): m.C(a, b, 0.06 - i * 0.012, 0.05 - i * 0.012, bone, seg=4)
    m.C(tail[-1], (0.26, 0.12, -2.35), 0.05, 0.0, dark, seg=4)
    for sx in (-1, 1):                                                         # wings: arm bone, fingers, membrane panels
        sh = (sx * 0.2, 1.15, 0.25); el = (sx * 0.8, 1.75, 0.0); wr = (sx * 1.3, 2.25, -0.2)
        m.C(sh, el, 0.045, 0.04, bone, seg=5); m.C(el, wr, 0.04, 0.03, bone, seg=5)
        tips = [(sx * 2.0, 1.6, -0.5), (sx * 1.75, 1.05, -0.65), (sx * 1.3, 0.75, -0.6)]
        for t in tips: m.C(wr, t, 0.025, 0.01, bone, seg=4)
        prev = el
        for t in tips:
            m.tri(np.array(wr), np.array(t), np.array(prev), m.slot(membrane)); m.tri(np.array(prev), np.array(t), np.array(wr), m.slot(membrane))
            prev = t
        m.tri(np.array(prev), np.array(sh), np.array(el), m.slot(membrane)); m.tri(np.array(el), np.array(sh), np.array(prev), m.slot(membrane))
    return m

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
         "fleischriese", "totenjaeger", "knochendrache",
         "sachsenkrieger", "wodansrabe", "wilder_jaeger", "hackelberg", "lutki", "wassermann", "rusalka", "mittagsfrau",
         "schlangenkoenig", "ertrunkener", "wattjungfrau", "klabautermann", "blanker_hans", "wasserleiche"]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for u in UNITS:
        m = build(u)
        p = os.path.join(OUT, u + ".glb"); t = write_glb(m, p)
        print(f"{u:20s} {t:5d} Dreiecke {os.path.getsize(p) // 1024:3d} KB")
