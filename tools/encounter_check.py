import copy, sim
from campaign_data import encounters
U = sim.load()
ARMIES = {
 "Start (13/15 KP)": ["Lich"]+["Skeleton"]*6+["Ghoul"]*2+["Zombie"]*3,
 "Ausgebaut (22/24 KP)": ["Lich","Necromancer"]+["DeathKnight"]*2+["Ghost"]*2+["Skeleton"]*4+["BoneArcher"]*2,
 "Stark (34/34 KP)": ["Lich","Necromancer"]+["DeathKnight"]*3+["Ghost"]*2+["DeathHunter"]*2+["BoneArcher"]*4,
}
def kp(a): return sum(-U[x]["CommandPoints"] for x in a if U[x]["CommandPoints"] < 0)
def net(r, e):
    L = r["corpses"] + e["BonusCorpses"] + e["BonusBones"]/2 - r["rep_corpses"] - r["rep_bones"]/2
    S = r["souls"] + e["BonusSouls"] - r["rep_souls"]
    return L, S
def run(variant_queen_bond=0):
    out = []
    for e in encounters:
        UU = U
        if e["Name"] == "Enc_HeathQueen" and variant_queen_bond:
            UU = copy.deepcopy(U); UU["HeathQueen"]["SoulShield"] += variant_queen_bond
        for an, a in ARMIES.items():
            r = sim.battle_stats(UU, a, e["Enemies"], gap=min(e["Width"], e["Height"]) - 2, n=300)
            L, S = net(r, e)
            out.append((e, an, r, L, S))
    return out
if __name__ == "__main__":
    for an,a in ARMIES.items(): print(an, kp(a))
    for e, an, r, L, S in run():
        print(f"{e['EncounterName'][:26]:26} {an[:10]:10} Sieg {r['winrate']:4.0%} {r['minutes']:5.1f}min Verl {r['avg_losses']:4.1f} netto L {L:+5.1f} S {S:+4.1f}")
    print("-- Heidekönigin mit vollem Ley-Bund (+20 SS):")
    for e, an, r, L, S in run(20):
        if e["Name"]=="Enc_HeathQueen":
            print(f"{an[:10]:10} Sieg {r['winrate']:4.0%} {r['minutes']:5.1f}min Verl {r['avg_losses']:4.1f}")
