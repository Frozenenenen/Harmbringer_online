"""Grober Balance-Vergleich der Untoten im Spielstand von data/world_data.js (mit Seltenheitsbonus,
Merkmalen und Auren): Kampfwert je Kommando-Punkt und je Kosten.

Kampfwert = Zähigkeit x Schlagkraft gegen typische Gegner (wie tools/sim.py value_report):
  Zähigkeit  = Treffer, die ein Gegner im Mittel braucht (LP + Seelenschild)
  Schlagkraft = Initiative / Treffer bis der Gegner fällt
Merkmale gehen als Faktoren ein (Annahmen in TRAIT_FACTORS). Das ist eine Faustregel, kein Ersatz
für Spielen: Bewegung, Fähigkeiten und Gelände zählen nicht.

Aufruf: python tools/balance_styles.py
"""
import json, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rules import hit_damage
import math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENEMIES = ["bauer", "stadtwache", "armbrust", "ritter", "moench", "sachsenkrieger"]
# (Zähigkeit, Schlagkraft): was das Merkmal im Schnitt wert ist.
TRAIT_FACTORS = {
    "ASSASSIN": (1.0, 1.25),   # jeder dritte Treffer ein Überraschungsschlag mit +75 %
    "SWARM": (1.0, 1.2),       # Stapel von 20: +20 %
    "CHARGE": (1.0, 1.15),     # jeder zweite Angriff nach 3 Feldern Anlauf (+30 %)
    "HITRUN": (1.15, 1.0),     # entgeht Kontern und Gegenangriffen
    "GUARD": (1.25, 1.0),      # schützt die Nachbarn (hier der Einheit gutgeschrieben)
    "REGEN": (1.2, 1.0),       # 10 % Heilung je Zug
    "DRUM": (1.0, 1.0),        # Unterstützer: Wert steckt in den Nachbarn, siehe Spalte "Hilfe"
}
RES_VALUE = {"corpses": 100, "bones": 1, "souls": 300}   # grober Wechselkurs in Knochen

def load_units():
    s = open(os.path.join(ROOT, "data", "world_data.js"), encoding="utf-8").read()
    body = s[s.index("// <GEN:UNITS>"):s.index("// </GEN:UNITS>")]
    return {m.group(1): json.loads(m.group(2)) for m in re.finditer(r"^\s{4}(\w+): (\{.*\}),?$", body, re.M)}

def row(u):
    cap = lambda x: x[0] + x[1:].lower() if x else x
    camel = lambda x: "".join(p.capitalize() for p in x.split("_"))
    return dict(AttackDamage=u["damage"], PowerType=camel(u["power"]), DefenseType=camel(u["defense"]), MagicResist=u["magicResist"],
                HP=u["hp"], SoulShield=u["soulShield"], Initiative=u["initiative"])

def hits(a, d):
    dmg = hit_damage(a, d)
    return math.inf if dmg == 0 else math.ceil((d["HP"] + d["SoulShield"]) / dmg)

def report():
    U = load_units(); E = [row(U[e]) for e in ENEMIES]; out = []
    for k, u in U.items():
        if u["side"] != "undead" or k == "lich" or u.get("ancestor") or u["power"] == "HEAL": continue
        r = row(u); tf, pf = 1.0, 1.0
        for t in u.get("traits", []): tf *= TRAIT_FACTORS[t][0]; pf *= TRAIT_FACTORS[t][1]
        tough = sum(min(40, hits(e, r)) for e in E) / len(E) * tf
        punch = sum(u["initiative"] / hits(r, e) for e in E) / len(E) * pf * (1.3 if u["range"] > 1 else 1.0)
        cp = u.get("commandPoints", 0); cost = sum(RES_VALUE[x] * v for x, v in u.get("cost", {}).items())
        out.append(dict(id=k, name=u["name"], kn=u.get("requiresKnowledge", 0), cp=cp, cost=cost, tough=tough, punch=punch, value=tough * punch,
                        per_cp=tough * punch / cp if cp > 0 else None, per_cost=tough * punch / cost * 1000 if cost else None, traits=",".join(u.get("traits", [])), aura=u.get("aura", "")))
    return out

if __name__ == "__main__":
    rows = sorted(report(), key=lambda r: (r["kn"], r["id"]))
    troops = [r for r in rows if r["per_cp"]]
    med_cp = statistics.median(r["per_cp"] for r in troops); med_cost = statistics.median(r["per_cost"] for r in troops)
    print(f"{'Einheit':22}{'Wissen':>7}{'KP':>4}{'Kosten':>8}{'Zäh':>7}{'Schlag':>8}{'Wert':>8}{'Wert/KP':>9}{'rel.':>6}{'Wert/1000':>10}{'rel.':>6}  Merkmale")
    for r in rows:
        pc = f"{r['per_cp']:9.2f}{r['per_cp'] / med_cp:6.2f}" if r["per_cp"] else f"{'Anführer':>15}"
        print(f"{r['name']:22}{r['kn']:7}{r['cp']:4}{r['cost']:8}{r['tough']:7.1f}{r['punch']:8.2f}{r['value']:8.1f}{pc}{r['per_cost']:10.2f}{r['per_cost'] / med_cost:6.2f}  {r['traits']} {r['aura']}")
    print(f"\nMedian Wert/KP {med_cp:.2f}, Median Wert je 1000 Knochen-Gegenwert {med_cost:.2f}. rel. = Verhältnis zum Median (1,00 = Durchschnitt).")
