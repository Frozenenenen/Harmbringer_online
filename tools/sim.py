"""Balancing-Check: Treffer bis zum Tod, Duell-Sieger, Kosten-Effizienz."""
import csv, math, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # Repo-Wurzel
from rules import hit_damage, tick_cost, MATRIX, DEFENSES

INT = {"HP","MaxEnergy","Initiative","MoveRange","AttackDamage","AttackRange","AttacksPerTurn","MagicResist",
       "SoulShield","Size","CommandPoints","CorpsesCost","BonesCost","SoulsCost"}
def load(path=os.path.join(ROOT, "design", "data", "DT_Units.csv")):
    out = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        for k in INT: r[k] = int(r[k])
        out[r["Name"]] = r
    return out

def ehp(u): return u["HP"] + u["SoulShield"]

def hits_to_kill(a, d):
    dmg = hit_damage(a, d)
    return math.inf if dmg == 0 else math.ceil(ehp(d) / dmg)

def time_to_kill(a, d):
    """Ticks bis a die Einheit d getötet hat (nur Grundangriff)."""
    h = hits_to_kill(a, d)
    return math.inf if h == math.inf else math.ceil(h / a["AttacksPerTurn"]) * tick_cost(a["Initiative"])

def duel(a, b):
    ta, tb = time_to_kill(a, b), time_to_kill(b, a)
    return "A" if ta < tb else "B" if tb < ta else "="

if __name__ == "__main__":
    U = load()
    player = ["Skeleton","Zombie","Ghoul","DeathKnight","Ghost","Necromancer","FleshGiant","Lich"]
    heide = ["Peasant","Crossbowman","HeathSister","Druidess","BogSpirit","WillOWisp"]
    print("Treffer bis Tod (Zeile greift an, Spalte verteidigt):")
    print(f"{'':14}" + "".join(f"{h[:10]:>11}" for h in heide))
    for p in player:
        print(f"{p:14}" + "".join(f"{hits_to_kill(U[p],U[h]):>11}" for h in heide))
    print("\nGegenrichtung:")
    print(f"{'':14}" + "".join(f"{p[:10]:>11}" for p in player))
    for h in heide:
        print(f"{h:14}" + "".join(f"{hits_to_kill(U[h],U[p]):>11}" for p in player))

def value_report(U, player, enemies):
    rows = []
    for p in player:
        u = U[p]
        tough = sum(hits_to_kill(U[e], u) for e in enemies) / len(enemies)
        punch = sum(u["AttacksPerTurn"] * u["Initiative"] / hits_to_kill(u, U[e]) for e in enemies) / len(enemies)
        cp = -u["CommandPoints"]
        rows.append((p, tough, punch, tough * punch, cp, tough * punch / cp if cp > 0 else None))
    return rows

if __name__ == "__main__" and "--value" in sys.argv:
    U = load()
    rows = value_report(U, ["Skeleton","Zombie","Ghoul","DeathKnight","Ghost","FleshGiant","Ballista"],
                        ["Peasant","Crossbowman","HeathSister","Druidess","BogSpirit","WillOWisp"])
    print(f"\n{'Einheit':12}{'Zähigk.':>9}{'Schlagkr.':>10}{'Kampfwert':>10}{'KP':>4}{'Wert/KP':>9}")
    for p,t,s,v,cp,vc in rows:
        print(f"{p:12}{t:9.1f}{s:10.2f}{v:10.1f}{cp:4}{vc:9.2f}")

# ---------------- Schlacht-Simulation (grob) ----------------
import random, heapq
SEC_PLAYER_TURN, SEC_ENEMY_TURN, SEC_SETUP = 20, 6, 120

def battle(U, player, enemy, gap=6, seed=0):
    """player/enemy: Listen von Row-Names. gap = Hex-Abstand der Fronten zu Beginn.
    Modell: Grundangriffe + Konter, keine Fähigkeiten, kein Gelände. Melee braucht Anmarsch-Züge."""
    rnd = random.Random(seed)
    def mk(name, side, i):
        u = U[name]
        need = max(0, gap - u["AttackRange"])           # Felder bis Angriff
        approach = math.ceil(need / 2 / u["MoveRange"])  # beide Seiten laufen aufeinander zu
        return dict(n=name, u=u, side=side, hp=ehp(u), app=approach, id=(side, i))
    units = [mk(n, "P", i) for i, n in enumerate(player)] + [mk(n, "E", i) for i, n in enumerate(enemy)]
    q = [(tick_cost(x["u"]["Initiative"]), -x["u"]["Initiative"], 0 if x["side"] == "P" else 1, k) for k, x in enumerate(units)]
    heapq.heapify(q)
    turns = {"P": 0, "E": 0}
    while True:
        t, _, _, k = heapq.heappop(q)
        a = units[k]
        if a["hp"] <= 0: continue
        foes = [x for x in units if x["side"] != a["side"] and x["hp"] > 0]
        if not foes: break
        turns[a["side"]] += 1
        if a["app"] > 0:
            a["app"] -= 1
        else:
            tgt = min(foes, key=lambda x: x["hp"]) if rnd.random() < 0.5 else rnd.choice(foes)
            for _ in range(a["u"]["AttacksPerTurn"]):
                tgt["hp"] -= hit_damage(a["u"], tgt["u"])
                if tgt["hp"] <= 0: tgt["killer"] = a["u"]["PowerType"]
            if tgt["hp"] > 0 and tgt["u"]["CanCounter"] and a["u"]["AttackRange"] == 1:
                a["hp"] -= hit_damage(tgt["u"], a["u"])
        lich_dead = any(x["n"] == "Lich" and x["hp"] <= 0 for x in units)
        if lich_dead or not any(x["hp"] > 0 for x in units if x["side"] == "E") \
           or not any(x["hp"] > 0 for x in units if x["side"] == "P"):
            break
        heapq.heappush(q, (t + tick_cost(a["u"]["Initiative"]), -a["u"]["Initiative"], 0 if a["side"] == "P" else 1, k))
    win = not any(x["hp"] > 0 for x in units if x["side"] == "E") and not any(x["n"] == "Lich" and x["hp"] <= 0 for x in units)
    lost = [x["n"] for x in units if x["side"] == "P" and x["hp"] <= 0]
    killed = [x for x in units if x["side"] == "E" and x["hp"] <= 0]
    minutes = (SEC_SETUP + turns["P"] * SEC_PLAYER_TURN + turns["E"] * SEC_ENEMY_TURN) / 60
    return dict(win=win, lost=lost, killed=[(x["n"], x.get("killer", "Chaos")) for x in killed], minutes=minutes, turns=turns)

QUALITY = {"Pierce":1.0,"Blunt":0.7,"Rend":0.4,"Siege":0.3,"Fire":0.2,"Poison":0.5,"Arcane":0.8,"Chaos":0.8,"Soul":1.0,"Holy":0.0}
SIZE_CORPSES = {1:1, 2:1, 3:2, 4:3}

def loot(U, killed):
    """Leichen (Qualitäts-gewichtet), Seelen aus Seelenschaden-Kills."""
    corpses = souls = 0.0
    for n, killer in killed:
        u = U[n]
        if killer == "Soul" and u["Rank"] != "Machine": souls += 1
        if u["IsSpectral"] != "True":
            corpses += SIZE_CORPSES[u["Size"]] * QUALITY[killer]
    return corpses, souls

def replace_cost(U, lost, refund=0.5):
    """Kosten, verlorene Einheiten nachzubauen – abzüglich 50 % Rückgewinn eigener Toter (Vorschlag)."""
    c = k = s = 0.0
    for n in lost:
        u = U[n]
        r = 0 if u["IsSpectral"] == "True" or u["Rank"] == "Machine" else refund
        c += u["CorpsesCost"] * (1 - r); k += u["BonesCost"] * (1 - r); s += u["SoulsCost"]
    return c, k, s

def battle_stats(U, player, enemy, gap=6, n=400):
    rs = [battle(U, player, enemy, gap, s) for s in range(n)]
    wins = [r for r in rs if r["win"]]
    from collections import Counter
    loss = Counter(l for r in wins for l in r["lost"])
    lt = [loot(U, r["killed"]) for r in wins]
    rc = [replace_cost(U, r["lost"]) for r in wins]
    w = max(1, len(wins))
    return dict(winrate=len(wins) / n,
                corpses=sum(x[0] for x in lt) / w, souls=sum(x[1] for x in lt) / w,
                rep_corpses=sum(x[0] for x in rc) / w, rep_bones=sum(x[1] for x in rc) / w, rep_souls=sum(x[2] for x in rc) / w,
                minutes=sum(r["minutes"] for r in rs) / n,
                avg_losses=sum(len(r["lost"]) for r in wins) / max(1, len(wins)),
                loss_by_type={k: v / max(1, len(wins)) for k, v in loss.items()},
                player_turns=sum(r["turns"]["P"] for r in rs) / n)
