"""Basis-Gebäude, Wissens-Freischaltungen, Begegnungen der Heide (Quelle für CSV + Doku)."""

def B(row, name, lvl, l, k, s, e, days, req_b="", req_k="", produces=(), cmd=0, effect=""):
    return dict(Name=row, BuildingName=name, Level=lvl, CostCorpses=l, CostBones=k, CostSouls=s, CostEnergy=e,
                BuildDays=days, RequiresBuilding=req_b, RequiresKnowledge=req_k, Produces=list(produces),
                CommandBonus=cmd, EffectText=effect)

buildings = [
 B("Phylactery_1","Phylakterium",1,0,0,0,0,0, effect="Start. Lager 50 L / 50 K / 10 S. Lich-Rückkehr nach Tod: 3 Tage"),
 B("Phylactery_2","Phylakterium",2,20,20,5,0,3,"Phylactery_1", effect="Lager 100/100/20. Rückkehr 2 Tage"),
 B("Phylactery_3","Phylakterium",3,40,40,10,10,5,"Phylactery_2", effect="Lager 200/200/40. Rückkehr 1 Tag. Zweite Expedition möglich"),
 B("BoneWorkshop_1","Knochenwerkstatt",1,0,0,0,0,0, produces=("Skeleton","SkeletonArcher","BoneSlinger"), effect="Start. Auskochen: 1 Leiche → 2 Knochen. Schleuderer erst mit Spielwissen 2"),
 B("BoneWorkshop_2","Knochenwerkstatt",2,10,10,0,0,2,"BoneWorkshop_1","Know_Crossbow",("BoneArcher",), effect="Knochenschützen"),
 B("BoneWorkshop_3","Knochenwerkstatt",3,20,30,2,0,4,"BoneWorkshop_2", produces=("Ballista",), effect="Belagerung"),
 B("CorpsePit_1","Leichengrube",1,0,0,0,0,0, produces=("Zombie","Ghoul","CorpseHound"), effect="Start"),
 B("CorpsePit_2","Leichengrube",2,15,10,0,0,2,"CorpsePit_1","Know_Bog",("BogCorpse",), effect="Moorleichen"),
 B("CorpsePit_3","Leichengrube",3,30,20,5,0,4,"CorpsePit_2", produces=("FleshGiant",), effect="Fleischriesen"),
 B("SoulKennel_1","Seelenzwinger",1,10,10,3,0,2, produces=("Ghost",), cmd=5, effect="Kommando-Limit 15 → 20"),
 B("SoulKennel_2","Seelenzwinger",2,20,20,6,0,3,"SoulKennel_1","Know_Wisp",("DeathLight",), cmd=5, effect="Limit 25, Totenlichter"),
 B("SoulKennel_3","Seelenzwinger",3,40,40,12,10,5,"SoulKennel_2", cmd=5, effect="Limit 30"),
 B("DeadHall_1","Totenhalle",1,15,20,3,0,3, produces=("DeathKnight","Necromancer"), effect="Kommandeure. 1 Ahne pro Expedition"),
 B("DeadHall_2","Totenhalle",2,25,30,6,0,4,"DeadHall_1", produces=("FallenSister","GraveDruidess","DeathHunter"),
   effect="Untote Heide-Varianten (jeweils mit Wissen). 2 Ahnen pro Expedition"),
 B("KnowledgeAltar_1","Wissensaltar",1,5,5,0,0,1, effect="Wandelt erbeutetes Wissen in Freischaltungen. Voraussetzung für alle untoten Varianten"),
 B("BoneForge_1","Knochenschmiede",1,20,30,4,0,3,"BoneWorkshop_1","Know_DwarfForge",
   effect="Todesritter +2 SoulShield dauerhaft"),
 B("HeathAltar_1","Heidealtar",1,30,20,10,10,5,"KnowledgeAltar_1","Know_HeathQueen",
   effect="Eigene Untote heilen auf Heather-Feldern 2 HP/Runde. Pantheon-Synergien der Heide"),
]

def K(row, name, src, kills, units=(), blds=(), desc=""):
    return dict(Name=row, KnowledgeName=name, SourceUnit=src, KillsRequired=kills,
                UnlocksUnits=list(units), UnlocksBuildings=list(blds), Description=desc)

knowledge = [
 K("Know_Crossbow","Armbrust-Handwerk","Crossbowman",8,("BoneArcher",),("BoneWorkshop_2",)),
 K("Know_Bog","Moorwissen","BogSpirit",5,("BogCorpse",),("CorpsePit_2",)),
 K("Know_Wisp","Irrlicht-Bann","WillOWisp",8,("DeathLight",),("SoulKennel_2",)),
 K("Know_Sister","Verkehrte Weihe","HeathSister",5,("FallenSister",)),
 K("Know_Druidess","Grabhüter-Riten","Druidess",5,("GraveDruidess",)),
 K("Know_WildHunt","Wilde Jagd","Wode",1,("DeathHunter",), desc="Legt zusätzlich das Ahnen-Grab eines bronzezeitlichen Reiterfürsten frei"),
 K("Know_DwarfForge","Zwergenschmiede","DwarfKing",1,(),("BoneForge_1",), desc="Plus 1 heidnisches Artefakt"),
 K("Know_HeathQueen","Herz der Heide","HeathQueen",1,(),("HeathAltar_1",), desc="Region assimiliert, Ley-Knoten Wilseder Berg (nach Portalbau)"),
]

def E(row, name, phase, node, pantheon, lat, lon, w, h, enemies, tod, stealth, bl=0, bk=0, bs=0, notes=""):
    return dict(Name=row, EncounterName=name, Phase=phase, NodeType=node, IsPantheon=pantheon, Lat=lat, Lon=lon,
                Width=w, Height=h, Enemies=list(enemies), TimeOfDay=tod, StealthAllowed=stealth,
                BonusCorpses=bl, BonusBones=bk, BonusSouls=bs, Notes=notes)

encounters = [
 E("Enc_WilsedeFarm","Einzelhof bei Wilsede",2,"Secular",False,53.1773,9.9196,8,8,
   ["Peasant"]*4+["Crossbowman"],"Night",True, bl=2,
   notes="Tutorial-Kampf. Bauern schlafen: Überraschung fast sicher"),
 E("Enc_BispingenChapel","Alte Kirche Bispingen",2,"Christian",False,53.0815,9.9987,12,10,
   ["Peasant"]*3+["Crossbowman"]*2+["HeathSister"]*2,"Evening",True, bk=6,
   notes="Feldsteinkirche, erbaut 1353. Kirchhof liefert Bonus-Knochen. Geweihter Boden um die Kirche"),
 E("Enc_Pietzmoor","Pietzmoor bei Schneverdingen",2,"Mythic",False,53.1190,9.8321,10,10,
   ["BogSpirit"]+["WillOWisp"]*3+["Druidess"],"Morning",False, bl=3,
   notes="Morgennebel, Moorboden. Keine Stealth-Phase: Irrlichter sehen alles. Moorleichen im Torf: +3 Leichen"),
 E("Enc_Wode","Die Wilde Jagd",6,"Mythic",True,52.9232,9.7154,14,8,
   ["Wode","BlackHound","BlackHound","BlackHound","BlackHound"],"Night",False, bl=6, bs=3,
   notes="Pantheon. Immer nachts. Offene Heide ohne Deckung. 4 Hunde = 2 Start + 2 beschworen (Simulation kennt keine Beschwörung). Gefallene Jagdpferde: +6 Leichen"),
 E("Enc_DwarfKing","Hügelgrab des Zwergenkönigs",6,"Mythic",True,52.9857,9.8446,10,10,
   ["DwarfKing","Druidess","Druidess","WillOWisp","WillOWisp","WillOWisp"],"Night",False, bk=15,
   notes="Pantheon. Grabkammern, StoneFloor. Keine Stealth-Phase. Grabbeigaben: +15 Knochen"),
 E("Enc_HeathQueen","Wilseder Berg",6,"Mythic",True,53.1648,9.9321,12,12,
   ["HeathQueen","BogSpirit","BogSpirit","WillOWisp","WillOWisp","WillOWisp","Druidess"],"Day",False, bs=5,
   notes="Pantheon-Finale der Region. Ley-Bund: +10 SoulShield pro lebendem Randmitglied. Phase 2 ab 50 % HP"),
]

# Orte der Kampagnenkarte (Breite, Länge in Grad, WGS84). Aus den am 31.10.2026 kalibrierten Tiles
# zurückgerechnet (Genauigkeit ca. 1–2 km); bei Bedarf durch exakte Koordinaten ersetzen.
def _t(q, r): return round(54.8190 - r / 240, 4), round(7.1529 + q / 240, 4)
PLACES = [
 ("Hamburg", *_t(682, 304), "Hansestadt, Elbe"),
 ("Lüneburg", *_t(783, 376), "Erste Menschenhauptstadt"),
 ("Teufelsmoor", *_t(427, 381), "Moorgeister"),
 ("Wilseder Berg", *_t(667, 397), "Ley-Knoten Heide, Pantheon-Finale der Region"),
 ("Kloster Medingen", *_t(811, 415), "Heidekloster"),
 ("Bremen", *_t(396, 418), "Erzbistum, Weser"),
 ("Kloster Ebstorf", *_t(784, 429), "Heidekloster"),
 ("Soltau", *_t(646, 440), "Heide-Dorf"),
 ("Uelzen", *_t(817, 445), "Hansestadt"),
 ("Verden", *_t(500, 455), "Bistum"),
 ("Kloster Walsrode", *_t(586, 470), "Heidekloster"),
 ("Celle", *_t(703, 527), "Welfen-Residenz"),
 ("Berlin", *_t(1501, 552), "Mark Brandenburg"),
 ("Hannover", *_t(619, 586), "–"),
 ("Braunschweig", *_t(810, 612), "Welfen"),
 ("Magdeburg", *_t(1074, 648), "Erzbistum, Elbe"),
 ("Hameln", *_t(529, 652), "Rattenfänger, Weser"),
 ("Wittenberg", *_t(1319, 709), "Askanier"),
 ("Brocken", *_t(831, 725), "Finale, Walpurgisnacht"),
]

NODE_TYPES = {"Mythic", "Secular", "Christian"}
TIMES = {"Night", "Morning", "Day", "Evening"}
