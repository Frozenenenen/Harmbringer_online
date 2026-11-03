import csv, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # Repo-Wurzel
OUT = os.path.join(ROOT, "design", "data")
os.makedirs(OUT, exist_ok=True)

# ---------- Units ----------
UF = ["UnitName","Rank","Role","Faction","DescriptionText","HP","MaxEnergy","Initiative","MoveRange",
      "AttackDamage","AttackRange","PowerType","AttacksPerTurn","CanCounter","DefenseType","MagicResist",
      "SoulShield","SightRange","HearRadius","SmellRadius","NoiseLevel","ScentLevel","Size","IsSpectral",
      "IsFlying","CommandPoints","CorpsesCost","BonesCost","SoulsCost","Abilities"]

def U(row, name, rank, role, fac, desc, hp, en, ini, mv, dmg, rng, pt, apt, cc, dt, mr, ss,
      sight, hear, smell, noise, scent, size, spec, fly, cp, l=0, k=0, s=0, ab=()):
    return dict(Name=row, UnitName=name, Rank=rank, Role=role, Faction=fac, DescriptionText=desc,
                HP=hp, MaxEnergy=en, Initiative=ini, MoveRange=mv, AttackDamage=dmg, AttackRange=rng,
                PowerType=pt, AttacksPerTurn=apt, CanCounter=cc, DefenseType=dt, MagicResist=mr,
                SoulShield=ss, SightRange=sight, HearRadius=hear, SmellRadius=smell, NoiseLevel=noise,
                ScentLevel=scent, Size=size, IsSpectral=spec, IsFlying=fly, CommandPoints=cp,
                CorpsesCost=l, BonesCost=k, SoulsCost=s, Abilities=list(ab))

T, F = True, False
units = [
 # --- Lich-Armee ---
 U("Lich","Lich","Unique","Commander","Undead","Der Spieler. Unsterblich durch das Phylakterium.",
   40,10,6,3,8,3,"Soul",1,F,"Unarmored",8,10, 5,4,2,1,3,2,F,F,0, ab=("LichSoulDrain","LichRetreat")),
 U("Skeleton","Skelett","CannonFodder","Melee","Undead","Speer und Rundschild. Billig, leise, zerbrechlich.",
   10,0,5,3,5,1,"Pierce",1,T,"Light",0,0, 3,2,0,2,1,1,F,F,-1, k=2, ab=("SkeletonReassemble",)),
 U("Zombie","Zombie","CannonFodder","Melee","Undead","Langsam, zäh, stinkt.",
   20,0,3,2,6,1,"Blunt",1,T,"Unarmored",0,0, 2,2,3,2,4,2,F,F,-1, l=1, ab=("ZombieInfect",)),
 U("Ghoul","Ghul","CannonFodder","Melee","Undead","Vierbeiniger Aasfresser mit Krallen.",
   18,0,5,3,6,1,"Rend",1,T,"Unarmored",1,0, 3,2,4,2,4,2,F,F,-2, l=1, ab=("GhoulCorpseEater",)),
 U("DeathKnight","Todesritter","Warrior","Tank","Undead","Plattenrüstung, Turmschild, Bidenhänder.",
   35,3,4,3,10,1,"Pierce",1,T,"Heavy",3,3, 3,3,1,3,2,2,F,F,-4, l=1, k=3, s=1, ab=("DeathKnightShieldWall",)),
 U("Ghost","Geist","Warrior","Scout","Undead","Lautloser Seelenfresser.",
   10,0,8,5,8,1,"Soul",1,F,"Unarmored",4,6, 5,4,0,0,0,1,T,T,-3, s=2),
 U("Ballista","Balliste","Machine","Siege","Undead","Knochen-Belagerungsgeschütz.",
   25,0,2,1,20,6,"Siege",1,F,"Fortified",0,0, 6,3,1,4,1,3,F,F,-5, l=3, k=5),
 U("Necromancer","Nekromant","Commander","Caster","Undead","Generischer Kommandeur, ruft Tote.",
   18,8,5,3,6,4,"Soul",1,F,"Light",5,4, 4,3,2,1,2,2,F,F,4, l=2, s=2, ab=("NecroRaiseDead",)),
 U("FleshGiant","Fleischriese","Warrior","Tank","Undead","Aus 15 Leichen vernäht.",
   70,3,2,2,14,1,"Blunt",1,T,"Medium",1,0, 3,2,2,4,4,4,F,F,-8, l=15, ab=("FleshGiantCrush",)),
 U("BoneDragon","Knochendrache","Warrior","Tank","Undead","Aus den Gebeinen eines Lindwurms gefügt. Fliegt, sein Totenhauch trifft zwei Felder weit.",
   120,4,5,6,18,2,"Soul",1,T,"Heavy",4,4, 6,4,3,4,2,4,F,T,-16, k=30, s=6),
 # --- Gegner Basis ---
 U("Peasant","Bauer","CannonFodder","Melee","Hanse","Mistgabel, rot-weißer Wappenrock.",
   10,0,4,3,4,1,"Pierce",1,T,"Unarmored",0,0, 4,3,2,2,2,2,F,F,0, ab=("PeasantMob",)),
 U("Crossbowman","Lüneburger Armbrustschütze","CannonFodder","Ranged","Hanse","Armbrust mit Setzschild.",
   15,0,4,3,9,5,"Pierce",1,F,"Medium",1,0, 6,3,2,2,2,2,F,F,0, ab=("CrossbowPavise",)),
 U("Cleric","Kleriker","Warrior","Support","Clergy","Weihrauchfass und Buch.",
   14,4,5,3,4,2,"Holy",1,F,"Light",4,6, 4,3,2,1,1,2,F,F,0, ab=("ClericCenser",)),
 U("HeathSister","Heideschwester","Warrior","Support","Clergy","Nonne mit Laterne und Kräuterkorb.",
   14,4,5,3,4,2,"Holy",1,F,"Light",4,6, 4,3,2,1,1,2,F,F,0, ab=("SisterHolyWater","SisterConsecrate")),
 U("Witch","Hexe","Warrior","Caster","Witches","Kräuterbündel-Stab, violettes Licht.",
   14,6,5,3,7,4,"Arcane",1,F,"Light",5,2, 4,3,3,1,2,2,F,F,0, ab=("WitchHex",)),
 U("Druid","Druide","Warrior","Support","Witches","Geweih-Kopfschmuck, Mistelkranz.",
   16,5,4,3,5,3,"Arcane",1,F,"Light",5,3, 4,3,3,1,2,2,F,F,0, ab=("DruidMistletoe",)),
 U("Druidess","Hügelgrab-Druidin","Warrior","Caster","Witches","Rentiergeweih-Haube, Mooreichenstab.",
   16,5,6,3,7,4,"Arcane",1,F,"Light",5,3, 4,3,4,1,2,2,F,F,0, ab=("DruidessGraveRest","DruidessEarthBind")),
 U("BogSpirit","Moorgeist","Warrior","Tank","HeathSpirits","Torfkörper, wächst aus dem Boden.",
   30,2,3,2,8,1,"Blunt",1,T,"Unarmored",3,2, 3,4,2,2,3,3,F,F,0, ab=("MoorGrip","FromThePeat")),
 U("WillOWisp","Irrlicht","CannonFodder","Scout","HeathSpirits","Schwebende Lichtkugel.",
   6,0,9,5,3,1,"Arcane",1,F,"Unarmored",6,4, 6,3,0,0,0,1,T,T,0, ab=("WispConfusion","WispFalseLight")),
 U("BlackHound","Schwarzer Hund","CannonFodder","Scout","HeathSpirits","Hund der Wilden Jagd. Nur beschworen.",
   8,0,7,5,4,1,"Rend",1,F,"Unarmored",3,2, 4,4,6,1,1,2,T,F,0, ab=("HoundPack",)),
 # --- Heide-Pantheon ---
 U("Wode","Der Wode","Unique","Melee","HeathSpirits","Anführer der Wilden Jagd. Pantheon der Heide.",
   55,8,8,6,12,1,"Pierce",1,T,"Divine",5,6, 6,5,5,4,2,3,F,F,0, ab=("WodeWildHunt","WodeRideThrough","WodeHorn")),
 U("DwarfKing","Hügelgrab-Zwergenkönig","Unique","Tank","HeathSpirits","Hüter der Gräber. Pantheon der Heide.",
   50,6,3,2,11,1,"Blunt",1,T,"Divine",6,4, 4,6,4,2,1,2,F,F,0, ab=("DwarfKingForge","DwarfKingTreasureCurse","DwarfKingStoneSkin")),
 U("HeathQueen","Die Heidekönigin","Unique","Caster","Witches","Herrin des Wilseder Bergs. Pantheon der Heide.",
   60,10,6,2,10,4,"Arcane",1,F,"Divine",8,10, 6,5,5,1,2,3,F,F,0, ab=("HeathQueenLeyBond","HeathQueenBloom","HeathQueenThorns")),
 # --- Untote Freischaltungen (Mythologie-Wissen Heide) ---
 U("BogCorpse","Moorleiche","Warrior","Tank","Undead","Untote Version des Moorgeists. Freigeschaltet durch Moorgeist-Kills.",
   28,2,3,2,8,1,"Blunt",1,T,"Unarmored",2,0, 3,3,2,2,4,3,F,F,-3, l=3, ab=("MoorGrip","BogCorpseMire")),
 U("DeathLight","Totenlicht","CannonFodder","Scout","Undead","Untote Version des Irrlichts. Grünes Licht, verwirrt Lebende.",
   6,0,9,5,3,1,"Arcane",1,F,"Unarmored",6,2, 6,3,0,0,0,1,T,T,-1, s=1, ab=("DeathLightConfusion",)),
 U("FallenSister","Gefallene Schwester","Warrior","Support","Undead","Untote Heideschwester mit erloschener Laterne.",
   14,4,5,3,4,2,"Soul",1,F,"Light",4,2, 4,3,2,1,2,2,F,F,-2, l=1, s=1, ab=("FallenSisterGraveWater",)),
 U("GraveDruidess","Grabdruidin","Warrior","Caster","Undead","Mumifizierte Hügelgrab-Druidin.",
   14,5,6,3,7,4,"Arcane",1,F,"Light",5,2, 4,3,4,1,3,2,F,F,-3, l=1, k=1, s=1, ab=("GraveDruidessBind","DruidessEarthBind")),
 U("BoneArcher","Knochenschütze","CannonFodder","Ranged","Undead","Skelett-Armbrustschütze. Wird nie führerlos (kein Leaderless).",
   10,0,4,3,8,5,"Pierce",1,F,"Light",0,0, 5,2,0,2,1,2,F,F,-2, k=3, ab=("CrossbowPavise",)),
 U("DeathHunter","Totenjäger","Warrior","Scout","Undead","Untoter Reiter der Wilden Jagd. Freigeschaltet durch den Sieg über den Wode.",
   22,3,7,6,9,1,"Pierce",1,T,"Light",2,0, 5,4,3,3,3,3,F,F,-4, l=3, k=2, s=1, ab=("DeathHunterCharge",)),
 # --- Aus dem spielbaren Prototyp übernommen (Werte unverändert aus data/world_data.js) ---
 U("SkeletonArcher","Skelett-Bogenschütze","CannonFodder","Ranged","Undead","Fernkampf ohne Wissen. Schwach, trifft aus der Deckung.",
   9,0,4,3,4,4,"Pierce",1,F,"Light",0,0, 5,2,1,1,1,1,F,F,-2, k=3),
 U("CorpseHound","Leichenhund","CannonFodder","Scout","Undead","Schnell und früh am Zug. Erreicht Schützen hinter der Front.",
   10,0,7,5,4,1,"Rend",1,F,"Unarmored",0,0, 4,4,6,1,3,1,F,F,-1, l=1),
 U("BoneSlinger","Knochenschleuderer","Warrior","Ranged","Undead","Fernkampf. Wirft Knochensplitter.",
   10,0,4,3,6,4,"Blunt",1,F,"Light",0,0, 5,2,1,1,1,1,F,F,-2, k=3),
 U("TownGuard","Stadtwache","Warrior","Melee","Hanse","Spieß und Kettenhemd, bewacht Tore und Märkte.",
   18,0,5,3,6,1,"Pierce",1,T,"Medium",0,0, 5,3,2,2,2,2,F,F,0),
 U("Knight","Ritter","Warrior","Tank","Guelphs","Gepanzerter Vasall der Welfen.",
   30,0,6,4,9,1,"Pierce",1,T,"Heavy",1,1, 5,2,2,3,2,2,F,F,0),
 U("CityBallista","Stadtballiste","Machine","Siege","Hanse","Geschütz auf Mauern und Türmen der Städte.",
   25,0,2,1,20,6,"Siege",1,F,"Fortified",0,0, 6,3,1,4,1,3,F,F,0),
 U("Monk","Mönch","Warrior","Caster","Clergy","Wirft heilige Worte wie Steine.",
   12,0,5,3,6,3,"Holy",1,F,"Unarmored",3,3, 5,4,3,1,1,1,F,F,0),
 U("Priest","Priester","Warrior","Support","Clergy","Heilt Verbündete. Ohne Verwundete greift er mit 3 Heilig-Schaden an.",
   16,0,4,3,6,3,"Heal",1,F,"Unarmored",4,4, 5,4,3,1,1,1,F,F,0),
 U("PiedPiper","Rattenfänger","Unique","Caster","Witches","Der Rattenfänger von Hameln. Seine Flöte lenkt Ratten und Kinder.",
   35,0,8,4,9,4,"Arcane",1,F,"Light",5,3, 7,7,3,2,1,2,F,F,0),
 U("BrockenQueen","Hexenkönigin vom Brocken","Unique","Caster","Witches","Herrin der Walpurgisnacht, Finale der Kampagne.",
   90,0,8,4,14,4,"Chaos",1,T,"Divine",6,6, 8,8,8,2,2,3,F,T,0),
]

# ---------- Spiel-Export: welche Design-Einheit unter welcher Kennung in data/world_data.js steht ----------
# Extras sind Werte, die nur das Spiel braucht (Platzhalter-Form, Farbe, Beschreibung, Wissens-Voraussetzung).
# cost: optional, sonst aus den Design-Kosten (Knochen x BONE_SCALE, weil das Spiel Knochen 60-fach zählt).
BONE_SCALE = 60
GAME_UNITS = [
 # Spiel-ID, Design-Zeile, Extras
 ("lich", "Lich", dict(shape="octahedron", color="#5a2d82", desc="Untoter Herrscher. Fällt er, ist der Kampf verloren und er kehrt ins Hügelgrab zurück.")),
 ("ghul", "Ghoul", dict(shape="capsule", color="#6b7d4a", desc="Billig, zäh, zerfleischt seine Opfer (schlechte Leichen).")),
 ("skelett", "Skeleton", dict(shape="cone", color="#d8d0b8", desc="Sauberer Stich, gute Leichen.")),
 ("bogner", "SkeletonArcher", dict(shape="cylinder", color="#ece4cc", cost=dict(bones=150))),
 ("leichenhund", "CorpseHound", dict(shape="box", color="#5a4a3a")),
 ("zombie", "Zombie", dict(shape="capsule", color="#7f8f62", desc="Langsam und zäh. Hält Türen und Engstellen.")),
 ("schleuderer", "BoneSlinger", dict(shape="cylinder", color="#bfb59a", requiresKnowledge=2)),
 ("geist", "Ghost", dict(shape="sphere", color="#a9c7d6", requiresKnowledge=3, desc="Lautlos, fliegt, geht durch Wände. Seelenschaden bringt Seelen.")),
 ("bauer", "Peasant", dict(shape="cone", color="#a08a5a")),
 ("stadtwache", "TownGuard", dict(shape="box", color="#8a2f2f")),
 ("armbrust", "Crossbowman", dict(shape="cylinder", color="#9a5a2a")),
 ("ritter", "Knight", dict(shape="box", color="#c2c2c8")),
 ("balliste", "CityBallista", dict(shape="box", color="#6e5536")),
 ("moench", "Monk", dict(shape="cone", color="#5b4632")),
 ("priester", "Priest", dict(shape="cone", color="#e6e0cc")),
 ("hexe", "Witch", dict(shape="cone", color="#3e5a3a")),
 ("irrlicht", "WillOWisp", dict(shape="sphere", color="#d9e86a")),
 ("moorgeist", "BogSpirit", dict(shape="capsule", color="#3a4a3a")),
 ("rattenfaenger", "PiedPiper", dict(shape="octahedron", color="#b0422e")),
 ("brockenhexe", "BrockenQueen", dict(shape="octahedron", color="#1d1d1d")),
 # Advanced undead from the design data (unlocked by knowledge; where to recruit: RECRUIT_AT in index.html)
 ("knochenschuetze", "BoneArcher", dict(shape="cylinder", color="#e0d8c0", requiresKnowledge=4)),
 ("moorleiche", "BogCorpse", dict(shape="capsule", color="#4a4030", requiresKnowledge=4)),
 ("todesritter", "DeathKnight", dict(shape="box", color="#3a3a44", requiresKnowledge=5)),
 ("totenlicht", "DeathLight", dict(shape="sphere", color="#9be05a", requiresKnowledge=5)),
 ("gefallene_schwester", "FallenSister", dict(shape="cone", color="#6a4a5a", requiresKnowledge=6)),
 ("grabdruidin", "GraveDruidess", dict(shape="cone", color="#4a5a3a", requiresKnowledge=6)),
 ("nekromant", "Necromancer", dict(shape="octahedron", color="#2a1a3a", requiresKnowledge=6)),
 ("knochenballiste", "Ballista", dict(shape="box", color="#8a7a5a", requiresKnowledge=7)),
 ("fleischriese", "FleshGiant", dict(shape="capsule", color="#8a5a4a", requiresKnowledge=3)),
 ("knochendrache", "BoneDragon", dict(shape="octahedron", color="#d8d0b8", requiresKnowledge=10)),
 ("totenjaeger", "DeathHunter", dict(shape="box", color="#3a2a2a", requiresKnowledge=10)),
 # Heath pantheon and clergy units for the mythic places of the wider map
 ("kleriker", "Cleric", dict(shape="cone", color="#cfc6a8")),
 ("heideschwester", "HeathSister", dict(shape="cone", color="#9a7a8a")),
 ("druide", "Druid", dict(shape="cone", color="#4f6a3a")),
 ("druidin", "Druidess", dict(shape="cone", color="#6a8a4a")),
 ("schwarzer_hund", "BlackHound", dict(shape="box", color="#202020")),
 ("wode", "Wode", dict(shape="octahedron", color="#3a4a6a")),
 ("zwergenkoenig", "DwarfKing", dict(shape="octahedron", color="#8a6a3a")),
 ("heidekoenigin", "HeathQueen", dict(shape="octahedron", color="#a0607a")),
]

# ---------- Abilities ----------
AF = ["AbilityName","Trigger","Target","Pattern","AreaSize","Range","Effect","PowerType","Value","Status",
      "Duration","EnergyCost","Cooldown","RequiresCorpse","ConditionFloors","Description"]
def A(row, name, trig, tgt, pat, area, rng, eff, pt, val, st="None", dur=0, en=0, cd=0, corpse=False, floors=(), desc=""):
    return dict(Name=row, AbilityName=name, Trigger=trig, Target=tgt, Pattern=pat, AreaSize=area, Range=rng,
                Effect=eff, PowerType=pt, Value=val, Status=st, Duration=dur, EnergyCost=en, Cooldown=cd,
                RequiresCorpse=corpse, ConditionFloors=list(floors), Description=desc)

abilities = [
 A("LichSoulDrain","Seelenentzug","Active","Enemy","SinglePoint",0,3,"Damage","Soul",8,en=3,cd=1,
   desc="8 Seelenschaden; Lich heilt sich um den angerichteten Schaden"),
 A("LichRetreat","Rückzug","Active","Self","SinglePoint",0,0,"Teleport","Arcane",0,"Marked",1,
   desc="Lich verlässt nach 1 Runde das Feld; in der Rückzugsrunde Marked"),
 A("SkeletonReassemble","Wiederzusammensetzen","OnDeath","Self","SinglePoint",0,0,"Heal","Heal",5,
   desc="Einmal pro Kampf mit 5 HP wieder aufstehen; nicht nach Blunt- oder Holy-Tod"),
 A("ZombieInfect","Seuchenbiss","OnDamageDealt","Enemy","SinglePoint",0,1,"ApplyStatus","Poison",2,"Poisoned",2,
   desc="Getroffenes Ziel wird vergiftet"),
 A("GhoulCorpseEater","Leichenfresser","Active","Ground","SinglePoint",0,1,"Heal","Heal",8,cd=2,corpse=True,
   desc="Frisst angrenzende Leiche: +8 HP, die Leiche ist als Beute verloren"),
 A("DeathKnightShieldWall","Schildwall","Active","Ally","Radius",1,0,"ApplyStatus","Blunt",5,"Shielded",1,en=2,cd=2,
   desc="Todesritter und Nachbarn erhalten Schild 5 bis zum nächsten Zug"),
 A("NecroRaiseDead","Totenruf","Active","Ground","SinglePoint",0,3,"Summon","Soul",1,en=4,cd=2,corpse=True,
   desc="Verbraucht Leiche auf Zielfeld, erzeugt 1 Skelett"),
 A("FleshGiantCrush","Zermalmen","Active","Enemy","Cone",1,1,"Damage","Blunt",10,"Stunned",1,en=3,cd=2,
   desc="Trifft 3 Felder im Kegel, betäubt"),
 A("PeasantMob","Rottenmut","OnTurnStart","Self","SinglePoint",0,0,"ApplyStatus","Pierce",0,"Enhanced",1,
   desc="Enhanced, wenn mind. 2 Bauern angrenzen"),
 A("CrossbowPavise","Setzschild","Passive","Self","SinglePoint",0,0,"ModifyTerrain","Pierce",0,
   desc="Wenn nicht bewegt: Kante zur Angriffsrichtung zählt als Cover"),
 A("ClericCenser","Weihrauch","Active","AllEnemies","Radius",1,0,"Damage","Holy",4,en=2,cd=1,
   desc="4 Holy-Schaden an alle angrenzenden Feinde"),
 A("SisterHolyWater","Weihwasser","Active","Ally","SinglePoint",0,2,"Heal","Heal",6,en=2,
   desc="Heilt Verbündeten um 6 HP"),
 A("SisterConsecrate","Geweihter Boden","Active","Ground","Radius",1,2,"ModifyTerrain","Holy",2,"None",3,en=3,cd=3,
   desc="Felder werden 3 Runden HolyGround: 2 Holy-Schaden pro Runde an Untote"),
 A("WitchHex","Hexenschuss","Active","Enemy","SinglePoint",0,4,"ApplyStatus","Arcane",0,"Marked",2,en=2,cd=1,
   desc="Ziel nimmt 2 Züge lang +25 % Schaden"),
 A("DruidMistletoe","Mistelsegen","Active","Ally","SinglePoint",0,3,"ApplyStatus","Heal",3,"Regeneration",3,en=2,cd=1,
   desc="Verbündeter regeneriert 3 HP pro Zug"),
 A("DruidessGraveRest","Grabesruhe","Active","Enemy","SinglePoint",0,4,"ApplyStatus","Arcane",0,"Cursed",2,en=3,cd=2,
   desc="Nur gegen Untote: -25 % Schaden"),
 A("DruidessEarthBind","Erdbindung","Active","Ground","SinglePoint",0,3,"ModifyTerrain","Arcane",0,"None",2,en=2,cd=3,
   desc="Feld wird 2 Runden unpassierbar, Kanten ringsum Cover"),
 A("MoorGrip","Moorgriff","Active","Enemy","SinglePoint",0,1,"ApplyStatus","Blunt",0,"Slowed",2,en=2,cd=1,
   desc="Slowed 2 Züge; auf Mud/Swamp/Bog zusätzlich Stunned 1 Zug"),
 A("FromThePeat","Aus dem Torf","OnTurnStart","Self","SinglePoint",0,0,"ApplyStatus","Blunt",4,"Shielded",1,
   floors=("Mud","Swamp","Bog"), desc="Auf Moorboden zu Zugbeginn Schild 4"),
 A("WispConfusion","Verwirrung","Passive","AllEnemies","Ring",1,0,"ApplyStatus","Arcane",0,"Confused",1,
   desc="Feinde auf Nachbarfeldern bewegen sich zufällig"),
 A("WispFalseLight","Falsches Licht","OnDeath","Ground","SinglePoint",0,0,"Summon","Arcane",1,"None",1,
   desc="Trugbild für 1 Runde, zieht Angriffe auf sich"),
 A("HoundPack","Meute","OnTurnStart","Self","SinglePoint",0,0,"ApplyStatus","Rend",0,"Enhanced",1,
   desc="Enhanced, wenn ein anderer Schwarzer Hund angrenzt"),
 A("WodeWildHunt","Wilde Jagd","Active","Ground","SinglePoint",0,2,"Summon","Soul",2,en=5,cd=4,
   desc="Beschwört 2 Schwarze Hunde"),
 A("WodeRideThrough","Durchreiten","Active","Enemy","Line",3,3,"Damage","Pierce",12,en=3,cd=2,
   desc="Reitet 3 Felder in Linie, trifft alle darauf, endet am Linienende"),
 A("WodeHorn","Jagdhorn","Active","AllAllies","Radius",3,0,"ApplyStatus","Arcane",0,"Hasted",2,en=2,cd=3,
   desc="Verbündete im Radius 3 werden beschleunigt"),
 A("DwarfKingForge","Runenschmiede","Active","Ally","SinglePoint",0,1,"ApplyStatus","Blunt",8,"Shielded",2,en=2,cd=1,
   desc="Verbündeter erhält Schild 8"),
 A("DwarfKingTreasureCurse","Schatzfluch","OnDamageTaken","Enemy","SinglePoint",0,0,"ApplyStatus","Arcane",0,"Cursed",2,
   desc="Wer den Zwergenkönig trifft, wird verflucht"),
 A("DwarfKingStoneSkin","Steinhaut","OnTurnStart","Self","SinglePoint",0,0,"ApplyStatus","Blunt",4,"Shielded",1,
   floors=("StoneFloor","CellarFloor","RawStone"), desc="Auf Steinboden zu Zugbeginn Schild 4"),
 A("HeathQueenLeyBond","Ley-Bund","Passive","Self","SinglePoint",0,0,"ApplyStatus","Arcane",10,"Shielded",0,
   desc="Kampfbeginn: +10 SoulShield pro lebendem Randmitglied des Heide-Pantheons"),
 A("HeathQueenBloom","Heideblüte","Active","AllAllies","Radius",2,0,"Heal","Heal",6,en=4,cd=2,
   desc="Heilt alle Verbündeten im Radius 2 um 6 HP"),
 A("HeathQueenThorns","Dornenkrone","Active","Ground","Radius",1,4,"ModifyTerrain","Pierce",3,"Slowed",3,en=4,cd=3,
   desc="Dornen-Gelände 3 Runden: Slowed und 3 Pierce-Schaden pro Runde für Feinde darauf"),
 A("BogCorpseMire","Moorheilung","OnTurnStart","Self","SinglePoint",0,0,"Heal","Heal",3,
   floors=("Mud","Swamp","Bog"), desc="Heilt sich auf Moorboden zu Zugbeginn um 3 HP"),
 A("DeathLightConfusion","Totenirrlicht","Passive","AllEnemies","Ring",2,0,"ApplyStatus","Arcane",0,"Confused",1,
   desc="Lebende Feinde im Umkreis 2 bewegen sich zufällig"),
 A("FallenSisterGraveWater","Grabwasser","Active","Ally","SinglePoint",0,2,"Heal","Soul",6,en=2,
   desc="Heilt verbündeten Untoten um 6 HP"),
 A("GraveDruidessBind","Lebensbann","Active","Enemy","SinglePoint",0,4,"ApplyStatus","Arcane",0,"Cursed",2,en=3,cd=2,
   desc="Nur gegen Lebende: -25 % Schaden"),
 A("DeathHunterCharge","Todesritt","Active","Enemy","Line",2,2,"Damage","Pierce",9,en=3,cd=2,
   desc="Reitet 2 Felder in Linie, trifft alle darauf"),
]

# ---------- Validation ----------
ENUMS = {
 "Rank": {"CannonFodder","Warrior","Machine","Commander","Unique"},
 "Role": {"Melee","Tank","Ranged","Caster","Support","Siege","Scout","Commander"},
 "Faction": {"Undead","Hanse","Guelphs","Clergy","Witches","WodanCult","Spreewald","Wattenmeer","HeathSpirits"},
 "PowerType": {"Pierce","Blunt","Rend","Siege","Fire","Poison","Arcane","Soul","Holy","Chaos","Heal"},
 "DefenseType": {"Unarmored","Light","Medium","Heavy","Fortified","Divine"},
 "Trigger": {"Active","OnDamageTaken","OnDamageDealt","OnDeath","OnAllyDeath","OnTurnStart","OnTurnEnd","Passive"},
 "Target": {"Self","Ally","Enemy","AllAllies","AllEnemies","Ground"},
 "Pattern": {"SinglePoint","Radius","Ring","Cone","Line","VShape"},
 "Effect": {"Damage","Heal","ApplyStatus","Stun","Push","Teleport","Summon","ModifyTerrain"},
 "Status": {"None","Poisoned","Burning","Bleeding","Stunned","Slowed","Hasted","Shielded","Enhanced","Cursed","Regeneration","Marked","Confused"},
}
ab_ids = {a["Name"] for a in abilities}
assert len(ab_ids) == len(abilities)
used = set()
for u in units:
    for k in ("Rank","Role","Faction","PowerType","DefenseType"):
        assert u[k] in ENUMS[k], (u["Name"], k, u[k])
    for a in u["Abilities"]:
        assert a in ab_ids, (u["Name"], a); used.add(a)
    assert 1 <= u["Size"] <= 4
    if u["MaxEnergy"] == 0:
        for a in u["Abilities"]:
            ab = next(x for x in abilities if x["Name"] == a)
            assert ab["EnergyCost"] == 0, (u["Name"], a)
    else:
        for a in u["Abilities"]:
            ab = next(x for x in abilities if x["Name"] == a)
            assert ab["EnergyCost"] <= u["MaxEnergy"], (u["Name"], a)
for a in abilities:
    for k in ("Trigger","Target","Pattern","Effect","PowerType","Status"):
        assert a[k] in ENUMS[k], (a["Name"], k, a[k])
assert used == ab_ids, ab_ids - used

# ---------- CSV-Ausgabe (Arrays als ("a","b"), Wahrheitswerte als True/False) ----------
def ue(v):
    if isinstance(v, bool): return "True" if v else "False"
    if isinstance(v, list): return "(" + ",".join(f'"{x}"' for x in v) + ")" if v else "()"
    return v

def write(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(["Name"] + fields)
        for r in rows:
            w.writerow([r["Name"]] + [ue(r[k]) for k in fields])

write(f"{OUT}/DT_Units.csv", UF, units)
write(f"{OUT}/DT_Abilities.csv", AF, abilities)

def lin(c):
    c /= 255
    return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
def lc(h):
    if h is None: return "(R=0.000000,G=0.000000,B=0.000000,A=1.000000)"
    r,g,b = (int(h[i:i+2],16) for i in (1,3,5))
    return f"(R={lin(r):.6f},G={lin(g):.6f},B={lin(b):.6f},A=1.000000)"

pal = [
 ("Undead","#D8D2C2","#7A4A2A","#5CFF7A",4.0),
 ("Hanse","#B3262B","#EDE8DC",None,0.0),
 ("Guelphs","#9E1B1B","#D4A537",None,0.0),
 ("Clergy","#E6E1D3","#C9A24A","#FFC766",2.0),
 ("Witches","#43364F","#8A5BB0","#B88CFF",3.0),
 ("WodanCult","#5B5F63","#8A1C1C","#FFAA33",3.0),
 ("Spreewald","#4E6B3A","#C8B568","#40E0C8",3.0),
 ("Wattenmeer","#6E6A60","#2F4C6E","#4FE8FF",3.0),
 ("HeathSpirits","#4A3626","#8E5A9B","#F2EBA0",3.0),
]
with open(f"{OUT}/DT_FactionPalettes.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Name","Primary","Accent","Emissive","EmissiveStrength","PrimaryHex","AccentHex","EmissiveHex"])
    for n,p,a,e,s in pal:
        w.writerow([n, lc(p), lc(a), lc(e), s, p, a, e or ""])
assert {p[0] for p in pal} == ENUMS["Faction"]

# ---------- Kampagne: Gebäude, Wissen, Begegnungen ----------
from campaign_data import buildings, knowledge, encounters, NODE_TYPES, TIMES, PLACES
from worldmap import layout as wm_layout, to_map
WM = wm_layout()
for e in encounters:
    m = to_map(e["Lat"], e["Lon"], WM)
    e["MapX"], e["MapY"] = round(m["px"], 2), round(m["py"], 2)   # Kartenposition in Höhenpunkten (Browser-Welteinheit)
    assert 0 <= m["px"] <= WM["width"] - 1 and 0 <= m["py"] <= WM["height"] - 1, e["Name"]
UN = {u["Name"]: u for u in units}
BN = {b["Name"]: b for b in buildings}
KN = {k["Name"]: k for k in knowledge}
produced = {}
for b in buildings:
    assert b["RequiresBuilding"] in BN or b["RequiresBuilding"] == "", b["Name"]
    assert b["RequiresKnowledge"] in KN or b["RequiresKnowledge"] == "", b["Name"]
    for p in b["Produces"]:
        assert p in UN and UN[p]["Faction"] == "Undead", (b["Name"], p)
        produced.setdefault(p, []).append(b["Name"])
for u in units:
    if u["Faction"] == "Undead" and u["Name"] != "Lich":
        assert u["Name"] in produced, ("nicht produzierbar", u["Name"])
for k in knowledge:
    assert k["SourceUnit"] in UN, k["Name"]
    for x in k["UnlocksUnits"]: assert x in produced, (k["Name"], x)
    for x in k["UnlocksBuildings"]: assert x in BN and BN[x]["RequiresKnowledge"] == k["Name"], (k["Name"], x)
for e in encounters:
    assert e["NodeType"] in NODE_TYPES and e["TimeOfDay"] in TIMES, e["Name"]
    for x in e["Enemies"]: assert x in UN and UN[x]["Faction"] != "Undead", (e["Name"], x)

BF = ["BuildingName","Level","CostCorpses","CostBones","CostSouls","CostEnergy","BuildDays","RequiresBuilding",
      "RequiresKnowledge","Produces","CommandBonus","EffectText"]
KF = ["KnowledgeName","SourceUnit","KillsRequired","UnlocksUnits","UnlocksBuildings","Description"]
EF = ["EncounterName","Phase","NodeType","IsPantheon","Lat","Lon","MapX","MapY","Width","Height","Enemies","TimeOfDay","StealthAllowed",
      "BonusCorpses","BonusBones","BonusSouls","Notes"]
write(f"{OUT}/DT_Buildings.csv", BF, buildings)
write(f"{OUT}/DT_Knowledge.csv", KF, knowledge)
write(f"{OUT}/DT_Encounters.csv", EF, encounters)

EXTRA_TABLES = []
# ---------- Balancing-Tabellen (aus sim.py) ----------
import sim
from rules import MATRIX, DEFENSES
SU = sim.load(f"{OUT}/DT_Units.csv")
P_LIST = ["Skeleton","Zombie","Ghoul","DeathKnight","Ghost","Necromancer","FleshGiant","Lich"]
H_LIST = ["Peasant","Crossbowman","HeathSister","Druidess","BogSpirit","WillOWisp"]
nm = lambda k: SU[k]["UnitName"]
t1 = ["| Angreifer ↓ / Ziel → | " + " | ".join(nm(h) for h in H_LIST) + " |", "|-" * (len(H_LIST)+1) + "|"]
for p in P_LIST:
    t1.append(f"| {nm(p)} | " + " | ".join(str(sim.hits_to_kill(SU[p], SU[h])) for h in H_LIST) + " |")
t2 = ["| Angreifer ↓ / Ziel → | " + " | ".join(nm(p) for p in P_LIST) + " |", "|-" * (len(P_LIST)+1) + "|"]
for h in H_LIST:
    t2.append(f"| {nm(h)} | " + " | ".join(str(sim.hits_to_kill(SU[h], SU[p])) for p in P_LIST) + " |")
t3 = ["| Einheit | Zähigkeit | Schlagkraft | Kampfwert | KP | Kampfwert/KP |", "|-|-|-|-|-|-|"]
for p,t,sk,v,cp,vc in sim.value_report(SU, ["Skeleton","Zombie","Ghoul","DeathKnight","Ghost","FleshGiant","Ballista","BogCorpse","DeathLight","FallenSister","GraveDruidess","BoneArcher","DeathHunter"], H_LIST):
    t3.append(f"| {nm(p)} | {t:.1f} | {sk:.2f} | {v:.1f} | {cp} | {vc:.2f} |")
EXTRA_TABLES += [("BAL_HITS_P", t1), ("BAL_HITS_E", t2), ("BAL_VALUE", t3)]

# ---------- Kampagnen-Tabellen ----------
import encounter_check as EC
def lst(x): return ", ".join(x) if x else "–"
def cnt(names):
    from collections import Counter
    return ", ".join(f"{v}× {UN[k]['UnitName']}" if v > 1 else UN[k]["UnitName"] for k, v in Counter(names).items())
def cost_s(b):
    p = [f"{b[k]}{c}" for k, c in (("CostCorpses","L"),("CostBones","K"),("CostSouls","S"),("CostEnergy","E")) if b[k]]
    return " ".join(p) or "Start"
tb = ["| Gebäude | Stufe | Kosten | Bautage | Voraussetzung | Produziert | Wirkung |", "|-|-|-|-|-|-|-|"]
for b in buildings:
    req = " + ".join(x for x in (BN[b["RequiresBuilding"]]["BuildingName"] + f" {BN[b['RequiresBuilding']]['Level']}" if b["RequiresBuilding"] else "",
                                 KN[b["RequiresKnowledge"]]["KnowledgeName"] if b["RequiresKnowledge"] else "") if x) or "–"
    tb.append(f"| {b['BuildingName']} | {b['Level']} | {cost_s(b)} | {b['BuildDays'] or '–'} | {req} | "
              f"{lst([UN[p]['UnitName'] for p in b['Produces']])} | {b['EffectText']} |")
tk = ["| Wissen | Quelle | Kills nötig | Schaltet frei | Hinweis |", "|-|-|-|-|-|"]
for k in knowledge:
    fr = [UN[x]["UnitName"] for x in k["UnlocksUnits"]] + [BN[x]["BuildingName"] for x in k["UnlocksBuildings"]]
    tk.append(f"| {k['KnowledgeName']} | {UN[k['SourceUnit']]['UnitName']} | {k['KillsRequired']} | {lst(fr)} | {k['Description'] or '–'} |")
TOD = {"Night":"Nacht","Morning":"Morgen","Day":"Tag","Evening":"Abend"}
NT = {"Mythic":"Mythisch","Secular":"Weltlich","Christian":"Christlich"}
te = ["| Begegnung | Phase | Typ | Karte (km O / km S) | Feld | Gegner | Zeit | Stealth | Bonus-Beute | Besonderheit |", "|-|-|-|-|-|-|-|-|-|-|"]
for e in encounters:
    bonus = " ".join(f"+{e[k]}{c}" for k, c in (("BonusCorpses","L"),("BonusBones","K"),("BonusSouls","S")) if e[k]) or "–"
    te.append(f"| {e['EncounterName']}{' (Pantheon)' if e['IsPantheon'] else ''} | {e['Phase']} | {NT[e['NodeType']]} | {e['MapX']*WM['res']/1000:.1f} / {e['MapY']*WM['res']/1000:.1f} | "
              f"{e['Width']}×{e['Height']} | {cnt(e['Enemies'])} | {TOD[e['TimeOfDay']]} | {'ja' if e['StealthAllowed'] else 'nein'} | {bonus} | {e['Notes']} |")
ta = ["| Armee | Zusammensetzung | KP / Limit |", "|-|-|-|"]
limits = {"Start (13/15 KP)": "13 / 15", "Ausgebaut (22/24 KP)": "22 / 24 (Seelenzwinger 1 + Nekromant)", "Stark (34/34 KP)": "34 / 34 (Seelenzwinger 3 + Nekromant)"}
for an, a in EC.ARMIES.items():
    ta.append(f"| {an.split(' (')[0]} | {cnt(a)} | {limits[an]} |")
tr = ["| Begegnung | Armee | Siegchance | Dauer | Verluste | Netto Leichen | Netto Seelen |", "|-|-|-|-|-|-|-|"]
for e, an, r, L, S in EC.run():
    tr.append(f"| {e['EncounterName']} | {an.split(' (')[0]} | {r['winrate']:.0%} | {r['minutes']:.0f} min | " +
              (f"{r['avg_losses']:.1f} | {L:+.1f} | {S:+.1f} |" if r['winrate'] else "alle | – (Niederlage) | – |"))
for e, an, r, L, S in EC.run(20):
    if e["Name"] == "Enc_HeathQueen":
        tr.append(f"| Wilseder Berg **mit vollem Ley-Bund** | {an.split(' (')[0]} | {r['winrate']:.0%} | {r['minutes']:.0f} min | " +
                  (f"{r['avg_losses']:.1f} | {L:+.1f} | {S:+.1f} |" if r['winrate'] else "alle | – (Niederlage) | – |"))
tp = ["| Ort | Breite | Länge | Karte km O / km S | Kartenposition (Höhenpunkte) | Bedeutung |", "|-|-|-|-|-|-|"]
for name, lat, lon, info in PLACES:
    m = to_map(lat, lon, WM)
    tp.append(f"| {name} | {lat:.4f} | {lon:.4f} | {m['km_e']:.1f} / {m['km_s']:.1f} | ({m['px']:.0f}, {m['py']:.0f}) | {info} |")
EXTRA_TABLES += [("PLACES", tp)]
from worldmap import sea_level_16bit, H_MIN, H_MAX
tw = ["| Kennwert | Wert |", "|-|-|",
      f"| Projektion | ETRS89 / UTM 32N (EPSG:25832) |",
      f"| Ausdehnung real | {(WM['e_max']-WM['e_min'])/1000:.0f} × {(WM['n_max']-WM['n_min'])/1000:.0f} km |",
      f"| Höhenkarte | {WM['width']} × {WM['height']} Höhenpunkte, 16 Bit, {H_MIN:g} bis {H_MAX:g} m |",
      f"| Gelände pro Höhenpunkt | {WM['res']:.1f} m |",
      f"| Meeresspiegel | 0 m (16-Bit-Wert {sea_level_16bit()}) |",
      f"| Gitter im Browser | 257 × 257 Vertices, Abstand 1–256 Höhenpunkte je nach Zoom |"]
EXTRA_TABLES += [("WORLDMAP", tw)]
EXTRA_TABLES += [("BUILDINGS", tb), ("KNOWLEDGE", tk), ("ENCOUNTERS", te), ("ARMIES", ta), ("ENC_RESULTS", tr)]
# DT_DamageMatrix.csv
with open(f"{OUT}/DT_DamageMatrix.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["Name"] + DEFENSES)
    for pt, row in MATRIX.items(): w.writerow([pt] + [f"{x:.2f}" for x in row])
# ---------- Markdown ----------
def cost(u):
    parts = [f"{u[k]}{c}" for k,c in (("CorpsesCost","L"),("BonesCost","K"),("SoulsCost","S")) if u[k]]
    return " ".join(parts) or "–"
md_u = ["| Einheit | Fraktion | Rang / Rolle | Size | HP | En | Ini | Bew | Schaden | Reichw. | Typ | Rüstung | MR / SS | Sinne | Signatur | Spektral/Flug | KP | Kosten |",
        "|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"]
for u in units:
    flags = "/".join(x for x,b in (("Spektral",u["IsSpectral"]),("Flug",u["IsFlying"])) if b) or "–"
    md_u.append(f"| {u['UnitName']} | {u['Faction']} | {u['Rank']} / {u['Role']} | {u['Size']} | {u['HP']} | {u['MaxEnergy']} | "
                f"{u['Initiative']} | {u['MoveRange']} | {u['AttackDamage']} | {u['AttackRange']} | {u['PowerType']} | "
                f"{u['DefenseType']} | {u['MagicResist']} / {u['SoulShield']} | {u['SightRange']}/{u['HearRadius']}/{u['SmellRadius']} | "
                f"{u['NoiseLevel']}/{u['ScentLevel']} | {flags} | {u['CommandPoints']:+d} | {cost(u)} |")

owner = {}
for u in units:
    for a in u["Abilities"]: owner.setdefault(a, []).append(u["UnitName"])
owner = {k: ", ".join(v) for k, v in owner.items()}
md_a = ["| ID | Name | Einheit | Auslöser | Ziel / Muster | Reichw. | Effekt | Wert | Status (Züge) | Energie / CD | Beschreibung |",
        "|-|-|-|-|-|-|-|-|-|-|-|"]
for a in abilities:
    pat = a["Pattern"] + (f" {a['AreaSize']}" if a["AreaSize"] else "")
    st = f"{a['Status']} ({a['Duration']})" if a["Status"] != "None" else (f"– ({a['Duration']})" if a["Duration"] else "–")
    desc = a["Description"] + (" *(braucht Leiche)*" if a["RequiresCorpse"] else "") + \
           (f" *(nur auf {', '.join(a['ConditionFloors'])})*" if a["ConditionFloors"] else "")
    md_a.append(f"| `{a['Name']}` | {a['AbilityName']} | {owner[a['Name']]} | {a['Trigger']} | {a['Target']} / {pat} | "
                f"{a['Range']} | {a['Effect']} ({a['PowerType']}) | {a['Value']} | {st} | {a['EnergyCost']} / {a['Cooldown']} | {desc} |")

doc = os.path.join(ROOT, "design", "design_notes.md")
s = open(doc, encoding="utf-8").read()
def put(s, tag, lines):
    b, e = f"<!--GEN:{tag}:BEGIN-->", f"<!--GEN:{tag}:END-->"
    assert s.count(b) == 1 and s.count(e) == 1, tag
    i, j = s.index(b) + len(b), s.index(e)
    return s[:i] + "\n" + "\n".join(lines) + "\n" + s[j:]
for tag, table in (("UNITS", md_u), ("ABILITIES", md_a)) + tuple(EXTRA_TABLES):
    s = put(s, tag, table)
# Inhaltsverzeichnis aus den ##-Überschriften neu erzeugen
def slug(h):
    return re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")
heads = [l[3:].strip() for l in s.splitlines() if l.startswith("## ") and l.strip() != "## Inhaltsverzeichnis"]
toc = "\n".join(f"{i}. [{h}](#{slug(h)})" for i, h in enumerate(heads, 1))
i = s.index("## Inhaltsverzeichnis"); j = s.index("\n---", i)
s = s[:i] + "## Inhaltsverzeichnis\n\n" + toc + "\n" + s[j:]
open(doc, "w", encoding="utf-8").write(s)
print(len(units), "units,", len(abilities), "abilities,", len(pal), "palettes")

# ---------- Spiel: data/world_data.js zwischen den GEN-Markern aus denselben Daten schreiben ----------
import json
from rules import MATRIX, DEFENSES, MR_PER_POINT, MR_CAP, TICK_BASE, MAGIC
from sim import QUALITY

def enum(x):                       # CamelCase -> UPPER_SNAKE (CannonFodder -> CANNON_FODDER)
    return re.sub(r"(?<!^)(?=[A-Z])", "_", x).upper()

def js(v):
    return json.dumps(v, ensure_ascii=False)

def game_unit(gid, row, extra):
    u = UN[row]
    cost = extra.get("cost") or {k: v for k, v in (("corpses", u["CorpsesCost"]), ("bones", u["BonesCost"] * BONE_SCALE),
                                                     ("souls", u["SoulsCost"])) if v}
    d = dict(name=u["UnitName"], side="undead" if u["Faction"] == "Undead" else "enemy", faction=enum(u["Faction"]),
             rank=enum(u["Rank"]), role=enum(u["Role"]), hp=u["HP"], initiative=u["Initiative"], move=u["MoveRange"],
             damage=u["AttackDamage"], range=u["AttackRange"], power=enum(u["PowerType"]), counter=u["CanCounter"],
             defense=enum(u["DefenseType"]), magicResist=u["MagicResist"], soulShield=u["SoulShield"],
             sight=u["SightRange"], hear=u["HearRadius"], smell=u["SmellRadius"], size=u["Size"],
             spectral=u["IsSpectral"], flying=u["IsFlying"], abilities=u["Abilities"])
    if d["side"] == "undead":
        d["commandPoints"] = -u["CommandPoints"]; d["cost"] = cost
    if "requiresKnowledge" in extra: d["requiresKnowledge"] = extra["requiresKnowledge"]
    d["shape"], d["color"] = extra["shape"], extra["color"]
    d["desc"] = extra.get("desc") or u["DescriptionText"]
    return d

wd_path = os.path.join(ROOT, "data", "world_data.js")
wd = open(wd_path, encoding="utf-8").read()
def put_js(s, tag, body):
    b, e = f"// <GEN:{tag}>", f"// </GEN:{tag}>"
    assert s.count(b) == 1 and s.count(e) == 1, tag
    i, j = s.index(b) + len(b), s.index(e)
    return s[:i] + "\n" + body + "\n  " + s[j:]
note = "  // Generated by tools/gen_data.py from design/data/*.csv and tools/rules.py - do not edit by hand.\n"
ids = [g for g, _, _ in GAME_UNITS]
assert len(set(ids)) == len(ids)
body_u = note + "  units: {\n" + ",\n".join(f"    {g}: {js(game_unit(g, r, x))}" for g, r, x in GAME_UNITS) + "\n  },"
body_pd = note + "  // Percent of damage that arrives. HEAL is not in the matrix: it restores HP to an ally.\n  powerDefense: {\n" + ",\n".join(
    f"    {enum(p)}: {js({enum(d): round(m * 100) for d, m in zip(DEFENSES, row)})}" for p, row in MATRIX.items()) + "\n  },\n" + \
    "  // Corpse quality per killing power type (0..1)\n" + f"  corpseQuality: {js({enum(k): v for k, v in QUALITY.items()})},\n" + \
    "  // Combat rules: tick cost per turn = tickBase / initiative; one round = roundTicks (ini 2.5).\n" + \
    "  // Magic power types are reduced by magicResist * mrPerPoint (capped). soulShield is a pool that absorbs any damage first.\n" + \
    f"  rules: {js(dict(tickBase=TICK_BASE, roundTicks=1008, magicPowers=sorted(enum(m) for m in MAGIC), mrPerPoint=MR_PER_POINT, mrCap=MR_CAP))},"
wd = put_js(wd, "UNITS", body_u)
wd = put_js(wd, "RULES", body_pd)
open(wd_path, "w", encoding="utf-8").write(wd)
print("world_data.js:", len(GAME_UNITS), "Einheiten")
