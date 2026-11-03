"""Embeds the ground textures of the world map prototype into data/ground_textures.js.

The game must run from file:// where WebGL cannot read images loaded from local files
(cross-origin). Data URIs are same-origin, so the textures are shipped as base64 in a script.
Source: prototypes/worldmap/worldmap/tex_<id>.jpg (built by build_webmap.py from the Godot textures).
"""
import base64, io, json, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "prototypes", "worldmap", "worldmap")
NAMES = ["Sand", "WetEarth", "GrassShort", "DryEarth", "Heather", "Bog", "Swamp", "GrassTall", "RawStone", "Mud"]
SIZE = 512

out = []
for i, name in enumerate(NAMES):
    im = Image.open(os.path.join(SRC, f"tex_{i}.jpg")).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=80)
    out.append(dict(name=name, src="data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()))
path = os.path.join(ROOT, "data", "ground_textures.js")
with open(path, "w", encoding="utf-8") as f:
    f.write("// Ground textures for the world map (from the Godot project, via tools/build_game_textures.py).\n"
            "// Embedded as data URIs so WebGL can use them when the game runs from file://.\n")
    f.write(f"window.HARMBRINGER_GROUND = {{ size: {SIZE}, textures: {json.dumps(out)} }};\n")
print(path, os.path.getsize(path) // 1024, "KB")
