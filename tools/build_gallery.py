"""Baut das Einheitenbuch (HTML) aus den CSVs in data/."""
import csv, json, os, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # Repo-Wurzel
sys.path.insert(0, os.path.join(ROOT, "tools"))
from campaign_data import encounters
import encounter_check as EC

D = os.path.join(ROOT, "design", "data")
abil = {r["Name"]: r["AbilityName"] for r in csv.DictReader(open(f"{D}/DT_Abilities.csv", encoding="utf-8"))}
units = []
for r in csv.DictReader(open(f"{D}/DT_Units.csv", encoding="utf-8")):
    ab = [x.strip('"') for x in r["Abilities"].strip("()").split(",") if x]
    units.append(dict(id=r["Name"], name=r["UnitName"], rank=r["Rank"], role=r["Role"], faction=r["Faction"],
                      hp=int(r["HP"]), ss=int(r["SoulShield"]), ini=int(r["Initiative"]), mv=int(r["MoveRange"]),
                      dmg=int(r["AttackDamage"]), rng=int(r["AttackRange"]), pt=r["PowerType"], defn=r["DefenseType"],
                      mr=int(r["MagicResist"]), size=int(r["Size"]), spectral=r["IsSpectral"] == "True",
                      flying=r["IsFlying"] == "True", cp=int(r["CommandPoints"]),
                      cost=[int(r["CorpsesCost"]), int(r["BonesCost"]), int(r["SoulsCost"])],
                      abilities=[abil[a] for a in ab]))
for u in units: u["def"] = u.pop("defn")
pal = {r["Name"]: dict(primary=r["PrimaryHex"], accent=r["AccentHex"], emissive=r["EmissiveHex"] or None)
       for r in csv.DictReader(open(f"{D}/DT_FactionPalettes.csv", encoding="utf-8"))}
encs = [dict(id=e["Name"], name=e["EncounterName"], w=e["Width"], h=e["Height"], q=int(e["Lon"]*1000), r=int(e["Lat"]*1000), tod=e["TimeOfDay"],
             pantheon=e["IsPantheon"], enemies=e["Enemies"], notes=e["Notes"]) for e in encounters]
armies = {k.split(" (")[0] + " (" + k.split(" (")[1]: v for k, v in EC.ARMIES.items()}
data = dict(units=units, palettes=pal, encounters=encs, armies=armies, generated=datetime.date.today().strftime("%d.%m.%Y"))
tpl = open(os.path.join(ROOT, "prototypes", "einheitenbuch", "template.html"), encoding="utf-8").read()
out = os.path.join(ROOT, "prototypes", "einheitenbuch", "index.html")
open(out, "w", encoding="utf-8").write(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
print(out, len(units), "Einheiten")
