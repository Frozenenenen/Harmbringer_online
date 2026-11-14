# Arbeitsstand (Übergabe-Notiz)

Diese Datei hält fest, woran gerade gearbeitet wird, damit eine andere Sitzung (auch ein anderes Modell) nahtlos weitermachen kann. Sie wird nach jeder Etappe aktualisiert. Erledigtes wandert ins Design-Dokument (`design/design_notes.md`) und fliegt hier raus.

Stand: 15.11.2026, 00:15 Uhr · letzte veröffentlichte Version: 136 (Schleichen 2.0)

## Auftrag (Kevin, 14.11.2026)

> Das Spielprinzip mit dem Anschleichen funktioniert noch fast gar nicht. Entwickle eine Lösung für ein ausgetüfteltes System und implementiere es danach. Allgemein verschiedene Spielstile, die durch verschiedene Einheiten ausgedrückt werden, sollten implementiert werden. Will man mobile Einheiten, will man lieber schwer aber untötbar sein oder auf aktive Fähigkeiten setzen? Was könnten noch interessante Spielmethoden sein: Masse statt Klasse, Klasse statt Masse? Mehr Kommandeure, ein Skillbaum für den Lich... Das Bausystem könnte auch noch eine Überarbeitung gebrauchen, sodass es übersichtlicher wird und die Forschung interessanter wird. Falls es dafür neue Einheiten und Kommandeure braucht, diese auch einfügen.

Drei Etappen, jede wird einzeln getestet, dokumentiert, mit `make_version.py` versioniert und auf `main` gepusht:

| Etappe | Inhalt | Stand |
|-|-|-|
| A | Schleichen 2.0 | **fertig, Version 136** (beschrieben im Design-Dokument, Abschnitt „Schleichen 2.0“). Rest: Lock- und Nebel-Fähigkeit, kommen mit Etappe B |
| B | Spielstile: Einheiten-Merkmale, neue Einheiten, Kommandeure mit Auren, Skillbaum des Lichs | offen (Entwurf unten) |
| C | Hügelgrab-Fenster neu: Gebäude / Forschung mit Entweder-oder-Wahl / Lich | offen (Entwurf unten) |

## Diagnose: Warum Anschleichen nicht ging (Messung vor dem Umbau)

Startarmee (Lich, 12 Ghule, 8 Skelette) gegen 40 Orte, Zustand direkt nach Kampfbeginn:

| Zeit | Wachgruppen | ahnungslos | misstrauisch | alarmiert | Orte ganz unbemerkt | Abstand Armee–Wache |
|-|-|-|-|-|-|-|
| Tag (12 Uhr) | 153 | 90 | 26 | 37 | 17 von 40 | 3,9 Felder |
| Nacht (0 Uhr) | 153 | 116 | 37 | 0 | 31 von 40 | 3,9 Felder |

Ursachen:

1. Auf 16×16-Feldern (156 von 193 Orten) startete die Armee 6 Felder vom Zentrum, Wachen standen bis 4 Felder davon – also sofort in Sichtweite. Alle Wachen schauten zur Armee.
2. Entdeckung war ein Schalter (gesehen = alarmiert). Die Einheitenwerte `noise` und `scent` wurden gar nicht benutzt.
3. Der Alarm breitete sich von selbst aus (4 Felder pro Runde, Glocke sofort), nach 3 Runden wurden alle „unruhig“ – langsames Schleichen wurde bestraft.
4. Misstrauische liefen schnurstracks zur nächsten Untoten-Einheit.
5. Der Spieler hatte keine Mittel: keine leise Gangart, keine Wahl der Seite, keine Ablenkung, keine Belohnung.

## Etappe A – Schleichen 2.0 (fertig)

Regeln stehen im Design-Dokument (`design/design_notes.md`, „Schleichen 2.0“). Für die Weiterarbeit wichtig:

- Code: `STEALTH`, `Stealth` (Wahrnehmung: `exposure`, `preview`, `sightRange`, `loudness`, `smellRange`), `Alarm` (`assign`, `raise`, `check`, `look`, `noise`, `crash`, `shout`, `runToBell`, `investigate`, `goHome`, `patrol`, `roundEnd`, `timeChanged`), `APPROACH` + `Battlefield.core`, `Battle.deploy`, `UI.attackPlan`, `Battle.start(node, exp, plan)`.
- Wachen-Felder: `aw`, `alert`, `role`, `asleep`, `home`, `homeFacing`, `away`, `lookAt`, `route`, `routeAt`, `shouted`, `stim`, `found`. Kampf-Felder: `b.fx` (= `Campaign.effects()` beim Kampfstart), `b.bodies`, `b.fog`, `b.shouts`, `b.bell`, `b.bellRunner`, `b.threatAdded`, `b.silent`.
- Schon vorbereitet, aber noch ohne Inhalt: `b.fog` (Felder im Nebel → Sicht 1), leise Fähigkeiten in `castAbility` (Effekte `LURE`, `FOG`, `HEAL`), `TRAITS.assassin` in `Battle.surpriseMul`, Schleich-Boni aus `b.fx`: `noise`, `scentPct`, `sneakMove`, `surprisePct`, `sightCut`.
- Gemessen mit `tools/test/sneak.js` (einfacher Bot, 10 Dörfer, Startarmee): am Tag lautlose Siege Schleichen 3 / Stürmen 1, Verluste 0,3 / 1,2; nachts beide 2 (Dörfer sind für 12 Ghule zu schwach, um Stürmen zu bestrafen). Größere Orte schafft der Bot nicht lautlos – das soll Können und passende Einheiten brauchen (Etappe B).

**Offen aus A (wandert in B):** Fähigkeits-Effekte `LURE` (Totenlicht lockt Wachen zu einem Feld: `lookAt` setzen, Argwohn auf höchstens 90) und `FOG` (Grabesnebel füllt `b.fog` für einige Runden) in `tools/gen_data.py` und `Abilities.use`.

## Etappe B – Spielstile (Entwurf, noch nichts eingebaut)

**Merkmale** (`traits` je Einheit, aus `tools/gen_data.py` exportiert; Wirkung vor allem in `Abilities.damageMul`, `moveOf`, `Battle.computeOptions`):

| Merkmal | Wirkung | Spielstil |
|-|-|-|
| ASSASSIN | Überraschungsschlag ×2 statt ×1,25 | Schleichen |
| SWARM | +2 % Schaden je Kreatur über 10 im Stapel, max. +40 % | Masse statt Klasse |
| CHARGE | +10 % Schaden je gelaufenem Feld, max. +50 % | Beweglich |
| HITRUN | volle Bewegung nach dem Angriff | Beweglich |
| GUARD | benachbarte Verbündete −25 % Schaden | Schwer, untötbar |
| REGEN | heilt jede Runde | Schwer, untötbar |
| DRUM | Aura: billige Einheiten +15 % Schaden, +1 Bewegung | Masse |

**Neue Einheiten** (je: Zeile in `gen_data.py`, Figur in `tools/build_units.py`, dann `build_units.py`, `render_portraits.py`, `build_game_figures.py`, `build_gallery.py`; Produzent in `baseBuildings`; Bild-Prompt in `design/ui_bilder.md`). Schon vorhanden und daher **nicht** doppeln: `totenjaeger` (Reiter, Wissen 10), `totenlicht` (Irrlicht – bekommt die Lockfähigkeit).

- `nachzehrer` – Meuchler (ASSASSIN, leise, geruchsarm), Wissen 2
- `gruftwaechter` – schwerer Schildträger (GUARD), Wissen 3
- `knochentrommler` – Trommler (DRUM), Wissen 2
- `knochenhexer` – Zauberer mit Grabesnebel (FOG), Wissen 3
- evtl. ein früher leichter Reiter (CHARGE/HITRUN), falls der Totenjäger zu spät kommt

**Kommandeure mit Auren** (`COMMANDER_TYPES` verallgemeinern; je Armee einer): neu `seuchenvogt` (Horde), `nachtvogt` (Schatten: Lautstärke −1, Geruch halb, Überraschung +25 %), `gruftfuerst` (Bollwerk: −20 % erlittener Schaden). Bestehende bekommen Auren: Nekromant/Ratsherr Hexerei, Todesritter Vorkämpfer, Reiterfürst Ritt, Hünenkönig Bollwerk, Widukind Horde.

**Skillbaum des Lichs** (`DATA.skills` in `data/world_data.js`, Handarbeit): 6 Pfade × 4 Stufen – Schatten, Flut (Masse), Auslese (Klasse), Hexerei, Eile, Bollwerk. Punkte = 1 + ⌊√(2 × eroberte Orte)⌋. Wirkungen laufen über `Campaign.effects()`; das Schleichen liest daraus schon `noise`, `scentPct`, `sneakMove`, `surprisePct`, `sightCut` (`Stealth.fx()` = `b.fx`).

## Etappe C – Hügelgrab-Fenster (Entwurf, noch nichts eingebaut)

Ein Fenster mit drei Reitern: **Gebäude** (Karten mit Stufenpunkten und den Einheiten, die sie freischalten) · **Forschung** · **Lich** (Skillbaum). Forschung: die 13 vorhandenen Verbesserungen (`upgrades` in `world_data.js`) werden zu Plätzen mit je zwei sich ausschließenden Optionen; Forschen dauert Tage (`c.research = { id, daysLeft }`, läuft in `Base.day()` weiter); Optionen können Merkmale verleihen. Alte Spielstände behalten, was sie haben; Umentscheiden kostet erneut.

## Werkzeuge zum Testen

- Im Repo: `tools/test/` (`sneak.js` spielt ganze Kämpfe mit Attrappen statt echter Grafik, siehe `tools/test/README.md`).
- Nur im flüchtigen Arbeitsordner der Sitzung: Bildschirmfotos mit echter Grafik (`real.js`) und ältere Einzeltests. Prinzip zum Nachbauen: Playwright lädt `index.html` über `file://`, leitet die Three.js-Adressen von jsDelivr auf eine lokale Kopie von three@0.160.0 um (Chromium mit `--use-angle=swiftshader`) und hängt vor dem letzten `</script>` eine Zeile an, die `Battle, game, newGame, DATA, UI, …` als `window.__T` herausgibt.
- **Nicht** Kevins Browser im Claude-Desktop zum Testen benutzen.
