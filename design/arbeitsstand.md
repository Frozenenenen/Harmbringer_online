# Arbeitsstand (Übergabe-Notiz)

Diese Datei hält fest, woran gerade gearbeitet wird, damit eine andere Sitzung (auch ein anderes Modell) nahtlos weitermachen kann. Sie wird nach jeder Etappe aktualisiert. Erledigtes wandert ins Design-Dokument (`design/design_notes.md`) und fliegt hier raus.

Stand: 16.11.2026, nachmittags · letzte veröffentlichte Version: 156 (Story-Bilder) · Stand 18.11.2026

## Auftrag (Kevin, 14.11.2026)

> Das Spielprinzip mit dem Anschleichen funktioniert noch fast gar nicht. Entwickle eine Lösung für ein ausgetüfteltes System und implementiere es danach. Allgemein verschiedene Spielstile, die durch verschiedene Einheiten ausgedrückt werden, sollten implementiert werden. Will man mobile Einheiten, will man lieber schwer aber untötbar sein oder auf aktive Fähigkeiten setzen? Was könnten noch interessante Spielmethoden sein: Masse statt Klasse, Klasse statt Masse? Mehr Kommandeure, ein Skillbaum für den Lich... Das Bausystem könnte auch noch eine Überarbeitung gebrauchen, sodass es übersichtlicher wird und die Forschung interessanter wird. Falls es dafür neue Einheiten und Kommandeure braucht, diese auch einfügen.

Drei Etappen, jede wird einzeln getestet, dokumentiert, mit `make_version.py` versioniert und auf `main` gepusht:

| Etappe | Inhalt | Stand |
|-|-|-|
| A | Schleichen 2.0 | **fertig, Version 137** (beschrieben im Design-Dokument, Abschnitt „Schleichen 2.0“). Rest: Lock- und Nebel-Fähigkeit, kommen mit Etappe B |
| B | Spielstile: Einheiten-Merkmale, neue Einheiten, Kommandeure mit Auren, Skillbaum des Lichs | **fertig, Version 138/139** (Design-Dokument „Spielstile“) |
| C | Hügelgrab-Fenster neu: Gebäude / Forschung mit Entweder-oder-Wahl / Pfade des Lichs | **fertig, Version 139** (Design-Dokument „Hügelgrab-Fenster“) |

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

Balance der neuen Einheiten ist geschätzt, nicht simuliert.

## Etappe C – Hügelgrab-Fenster (fertig)

Beschrieben im Design-Dokument, Abschnitt „Hügelgrab-Fenster: Gebäude, Forschung, Pfade des Lichs“. Code: `Base.open(tab)`, `Base.buildHtml/researchHtml/lichHtml/chips`, `Upgrades` (jetzt Forschung: `rival`, `days`, `buy` startet, `day` schließt ab, `count`), `UI.buildBadge`, Daten `researchSlots` + `upgrades` (26 Antworten in 13 Fragen) in `data/world_data.js`.

## Nachträge vom 15.11. (fertig, Version 140)

Beschrieben im Design-Dokument, Abschnitt „Aufforderungen, Spielstil-Filter, Ton, Balance“.

- **Windlesen ist freischaltbar** (Kevins Wunsch): `UI.attack(node, exp)` öffnet den Angriffsplan nur mit dem Effekt `attackPlan` (Skill `sh1` „Windlesen“ oder Forschung `windLore` „Windkunde“); sonst direkter Angriff aus der Marschrichtung, Wind im Kampf nicht angezeigt.
- **Aufforderungen** (Kevins Wunsch, wie Civilization): `UI.todoList`, `UI.todo`, Element `#todoBar`.
- **Ton:** `Sfx` neu aufgebaut (`setup`, `makeLoop`, `ambience`, `gusts`, `step`, `bell`, `horn`, `fanfare`, `drum`, `setVolume`). Gemessen mit einem Offline-Audiokontext, **nicht gehört** – Kevins Ohr entscheidet; Stellschrauben in `SFX` und in den Zahlen von `Sfx.gusts`.
- **Spielstil-Filter** beim Rekrutieren (`STYLES` in `UI.openRecruit`).
- **Balance:** `tools/balance_styles.py`; vier neue Einheiten abgeschwächt.

## Nebel des Krieges (fertig, Version 141)

Beschrieben im Design-Dokument, Abschnitt „Nebel des Krieges auf der Weltkarte“. Code: `FOW`, `Fow` (`sources`, `note`, `stamp`, `refresh`, `explored`, `visible`, `patch`), Geländeshader (`wTex`, `fowOn`), `Campaign.isRevealed` (= erkundet), `Campaign.inSight`/`revealedAt` (= in Sicht), `WorldView.refresh` (`nv.known`), Minimap-Overlay, `c.explored` im Spielstand, Debug-Schalter `c.debugNoFog`. Test in der Sitzung: `fow.js` (Reise deckt auf, Erinnerung, Speichern, Kosten: 23 ms je Neuberechnung im Spätspiel).

Noch nicht gemacht: Expeditionen decken unterwegs nur an ihren Orten auf (nicht entlang des Wegs); kein eigener Späher-Befehl; Tooltips/Listen außerhalb der Karte (z. B. Pantheon-Mitglieder) nennen auch unbekannte Orte beim Namen.

## Doktrinen der Fraktionen (fertig, Version 142)

Beschrieben im Design-Dokument, Abschnitt „Doktrinen: Identität der Fraktionen“ (Tabelle aller 12). Daten `factions[*].doctrine`, Code `Doctrine`. Test in der Sitzung: `doct.js` (je Fraktion ein Kampf: Besatzung, Werte, Wache, Hinterhalt).

Nicht gemacht / offen: Zahlen sind gesetzt, nicht ausbalanciert (Welfen-Städte mit 1,5-fach Rittern und Sturmangriff dürften spürbar härter sein; Hanse-Städte sind nachts kaum noch zu beschleichen – so gewollt, aber ungeprüft im Spiel). Beschworene Gegner bekommen die Doktrin nicht. Begegnungen unterwegs haben die Doktrin ihrer Fraktion, Wachen-Regeln greifen dort nicht (alle alarmiert). Die Prompts „Bauplatz frei“ stehen jetzt unten links (überdeckten rechts die Ortsinfo).

## Balance-Test und Schwierigkeitsstufen (fertig, Version 155)

Kevins Auftrag vom 16./17.11.: Balance testen (auch je Spielstil), drei Schwierigkeitsstufen. Ergebnisse, Korrekturen und offene Punkte stehen in **`design/balance_bericht.md`**. Kurz:

- Korrigiert: Gegner-KI jagt keinen unverwundbaren Lich mehr, fünf Doktrinen entschärft, neue Stärke-Schätzung für die Gefahrenfarbe (`Campaign.unitStrength/ownStrength/foeStrength`), Fehler „Lich verschwindet nach Rückzug“ behoben, Schwer +20 % LP / +15 % Schaden.
- Stufen im offenen Kampf: Siege Leicht 98 %, Mittel 92 %, Schwer 80 %.
- Offen: Hexerei womöglich zu stark; Schleichen bringt dem Test-Bot keinen Vorteil (Kevin selbst testen lassen); Leichen sind überall der Engpass; Kampagnen auf Schwer mit neuen Werten nicht nachgemessen.
- Werkzeuge: `tools/test/matrix.js`, `campaign.js`, `sneak.js` (Aufrufe in den Dateiköpfen).

## Story-Bilder (fertig, Version 156)

Kevin (18.11.): Spielintro und Story als große Bilder mit Erzähltext; Wahrzeichen (Hamburger Hafen), Belagerung, Klerus mit Engel gegen Zombie. Dazu: Bildkomposition muss stimmen (Standpunkt/Blickwinkel). Eingebaut: 16 Szenen, 19 Bilder (Design-Dokument „Story-Bilder“), Prompts in `design/ui_bilder.md` Abschnitt 0 (18.11.). **Bilder fehlen noch** – Kevin erzeugt sie, Claude legt sie unter `assets/story/` ab (16:9 JPG, auf ~1920 px Breite verkleinern). Test in der Sitzung: `story.js` (Intro, Wahrzeichen vor Kampf, einmalig, Galerie). Kevins „Nephilim“: im Spiel gibt es Ophan, Cherub und Seraph – das Bild zeigt einen Seraph.

## Was als Nächstes sinnvoll wäre (nichts davon begonnen)

- **Kevins Rückmeldung abwarten:** Spielgefühl beim Schleichen (Kegelgröße am Tag, Tempo der Streifen, ob „Posten rufen sofort“ zu hart ist) – alle Stellschrauben stehen in `STEALTH`.
- **Balance:** Faustregel-Vergleich ist gemacht (`tools/balance_styles.py`); ganze Schlachten mit Merkmalen und Auren sind nicht simuliert. Auffällig stark im Vergleich: Balliste, Knochendrache, Todesritter (alt), Geist.
- **Koop:** Forschung und Skillbaum gehören dem Gastgeber (`c.research`, `c.skills`); der Gast sieht sie, lernt aber nicht. Eigene Pfade für den Gast-Kommandeur wären ein eigener Schritt.
- **Gegner-KI:** nutzt die neuen Merkmale nicht (kein Gegner hat welche). Wachen könnten nach einem Alarm Verstärkung aus Nachbarorten rufen.
- **Bilder:** `design/ui_bilder.md` Abschnitt 0 (8 Einheiten, 6 Pfad-Symbole, Merkmals- und Wachen-Symbole, Banner Angriffsplan).
- Weiter offen aus früheren Sitzungen: Koop Stufe 6 (gemeinsame Schlachten), Ley-Sprung/Inventar/Expeditionen für den Gast, Bedrohungswellen, Wissen durch Kills, Pantheon-Magie, Flussnetz, Rangabzeichen; Kevins offene Entscheidungen (Hügelgrab angreifbar, Lagergrenzen, Späher).

## Werkzeuge zum Testen

- Im Repo: `tools/test/` (`sneak.js` spielt ganze Kämpfe mit Attrappen statt echter Grafik, siehe `tools/test/README.md`).
- Nur im flüchtigen Arbeitsordner der Sitzung: Bildschirmfotos mit echter Grafik (`real.js`) und ältere Einzeltests. Prinzip zum Nachbauen: Playwright lädt `index.html` über `file://`, leitet die Three.js-Adressen von jsDelivr auf eine lokale Kopie von three@0.160.0 um (Chromium mit `--use-angle=swiftshader`) und hängt vor dem letzten `</script>` eine Zeile an, die `Battle, game, newGame, DATA, UI, …` als `window.__T` herausgibt.
- **Nicht** Kevins Browser im Claude-Desktop zum Testen benutzen.
