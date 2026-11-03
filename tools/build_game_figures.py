"""Embeds the unit figures for the game as scripts: data/figures/<unit>.js (base64 GLB).

The game runs from file://, where fetch() of local files is blocked, so every figure is a
small script that the battle loads on demand (<script> tags work under file://).
Mapping unit -> figure: GAME_FIGURES in render_portraits.py.
"""
import base64, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_portraits import GAME_FIGURES, FIG, ROOT

out_dir = os.path.join(ROOT, "data", "figures")
os.makedirs(out_dir, exist_ok=True)
total = 0
for unit, f in GAME_FIGURES.items():
    b64 = base64.b64encode(open(os.path.join(FIG, f), "rb").read()).decode()
    p = os.path.join(out_dir, unit + ".js")
    with open(p, "w") as fh:
        fh.write(f"// {f} (tools/build_game_figures.py)\n(window.HARMBRINGER_FIGURES = window.HARMBRINGER_FIGURES || {{}})[{unit!r}] = \"{b64}\";\n")
    total += os.path.getsize(p)
print(len(GAME_FIGURES), "Figuren,", total // 1024, "KB in", out_dir)
