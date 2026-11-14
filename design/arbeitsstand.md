# Arbeitsstand (Übergabe-Notiz)

Diese Datei hält fest, woran gerade gearbeitet wird, damit eine andere Sitzung (auch ein anderes Modell) nahtlos weitermachen kann. Sie wird nach jeder Etappe aktualisiert. Erledigtes wandert ins Design-Dokument (`design/design_notes.md`) und fliegt hier raus.

Stand: 15.11.2026, 01:30 Uhr · letzte veröffentlichte Version: 138 (Spielstile)

## Auftrag (Kevin, 14.11.2026)

> Das Spielprinzip mit dem Anschleichen funktioniert noch fast gar nicht. Entwickle eine Lösung für ein ausgetüfteltes System und implementiere es danach. Allgemein verschiedene Spielstile, die durch verschiedene Einheiten ausgedrückt werden, sollten implementiert werden. Will man mobile Einheiten, will man lieber schwer aber untötbar sein oder auf aktive Fähigkeiten setzen? Was könnten noch interessante Spielmethoden sein: Masse statt Klasse, Klasse statt Masse? Mehr Kommandeure, ein Skillbaum für den Lich... Das Bausystem könnte auch noch eine Überarbeitung gebrauchen, sodass es übersichtlicher wird und die Forschung interessanter wird. Falls es dafür neue Einheiten und Kommandeure braucht, diese auch einfügen.

Drei Etappen, jede wird einzeln getestet, dokumentiert, mit `make_version.py` versioniert und auf `main` gepusht:

| Etappe | Inhalt | Stand |
|-|-|-|
| A | Schleichen 2.0 | **fertig, Version 137** (beschrieben im Design-Dokument, Abschnitt „Schleichen 2.0“). Rest: Lock- und Nebel-Fähigkeit, kommen mit Etappe B |
| B | Spielstile: Einheiten-Merkmale, neue Einheiten, Kommandeure mit Auren, Skillbaum des Lichs | **Regeln und Daten fertig, Version 138** (Design-Dokument „Spielstile“). Der Skillbaum hat noch **kein Fenster** – das kommt mit Etappe C |
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

## Etappe B – Spielstile (Regeln fertig)

Beschrieben im Design-Dokument, Abschnitt „Spielstile: Merkmale, neue Einheiten, Auren“. Für die Weiterarbeit:

- Daten: `tools/gen_data.py` (Zeilen unter „Spielstile (14.11.2026)“, `GAME_UNITS`-Extras `traits`, `aura`, `commander`; Fähigkeiten `LichGraveWhisper`, `DeathLightLure`, `HexerGraveFog`, `HexerMarrowBolt`; Effekte `Lure`, `Fog`), `tools/campaign_data.py` (Produktion), `data/world_data.js` (`baseBuildings.produces`, `unitGroups`, **`skills`**).
- Figuren: `tools/build_units.py` (Block „playstyle units“), Bilder-Prompts in `design/ui_bilder.md` Abschnitt 0.
- Code in `index.html`: `TRAITS`, `TRAIT_INFO`, `AURAS`, `hasTrait`, `isFodder`, `isElite`, `traitHtml`; `Abilities.damageMul` (Schwarm, Sturmangriff, Trommler, Schildwache, Nebel), `Abilities.drummed`, `moveOf`, `Abilities.fog`, `Alarm.lure`, `Battle.applyAuras`, `Battle.applyArmyEffects` (liest `b.fx`), `Skills` (Punkte, `blocker`, `learn`), `Campaign.effects()` zählt gelernte Skills mit.
- Neue Effekt-Schlüssel in `b.fx`: `noise`, `scentPct`, `sneakMove`, `surprisePct`, `sightCut`, `fodderDamagePct`, `fodderHpPct`, `eliteHpPct`, `eliteDamagePct`, `eliteShield`, `move`, `energy`, `energyRegen`, `abilityPct`, `cooldown`, `chargePct`, `damageTakenPct`, `regenPct`, `leaderGuard`.
- Test: `scratchpad/t/style.js` (nur in der Sitzung) prüft Merkmale, Auren, Locken, Nebel, Skills in einem echten Kampf – alles grün.

**Offen:** Fenster für den Skillbaum (`Skills.learn(id)` ist fertig, es fehlt nur die Oberfläche) → Etappe C. Balance der neuen Einheiten ist geschätzt, nicht simuliert.

## Etappe C – Hügelgrab-Fenster (Entwurf, noch nichts eingebaut)

Ein Fenster mit drei Reitern: **Gebäude** (Karten mit Stufenpunkten und den Einheiten, die sie freischalten) · **Forschung** · **Lich** (Skillbaum). Forschung: die 13 vorhandenen Verbesserungen (`upgrades` in `world_data.js`) werden zu Plätzen mit je zwei sich ausschließenden Optionen; Forschen dauert Tage (`c.research = { id, daysLeft }`, läuft in `Base.day()` weiter); Optionen können Merkmale verleihen. Alte Spielstände behalten, was sie haben; Umentscheiden kostet erneut.

## Werkzeuge zum Testen

- Im Repo: `tools/test/` (`sneak.js` spielt ganze Kämpfe mit Attrappen statt echter Grafik, siehe `tools/test/README.md`).
- Nur im flüchtigen Arbeitsordner der Sitzung: Bildschirmfotos mit echter Grafik (`real.js`) und ältere Einzeltests. Prinzip zum Nachbauen: Playwright lädt `index.html` über `file://`, leitet die Three.js-Adressen von jsDelivr auf eine lokale Kopie von three@0.160.0 um (Chromium mit `--use-angle=swiftshader`) und hängt vor dem letzten `</script>` eine Zeile an, die `Battle, game, newGame, DATA, UI, …` als `window.__T` herausgibt.
- **Nicht** Kevins Browser im Claude-Desktop zum Testen benutzen.
