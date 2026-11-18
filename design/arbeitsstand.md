# Arbeitsstand (Übergabe-Notiz)

Diese Datei hält fest, woran gerade gearbeitet wird, damit eine andere Sitzung (auch ein anderes Modell) nahtlos weitermachen kann. Sie wird nach jeder Etappe aktualisiert. Erledigtes wandert ins Design-Dokument (`design/design_notes.md`) und fliegt hier raus.

Stand: 18.11.2026 · letzte veröffentlichte Version: 173 (Anführer schwächer, stehen wieder auf; Versionsnummer zählt Commits)

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

Kevin (18.11.): Spielintro und Story als große Bilder mit Erzähltext; Wahrzeichen (Hamburger Hafen), Belagerung, Klerus mit Engel gegen Zombie. Dazu: Bildkomposition muss stimmen (Standpunkt/Blickwinkel). Eingebaut: 16 Szenen, 19 Bilder (Design-Dokument „Story-Bilder“), Prompts in `design/ui_bilder.md` Abschnitt 0 (18.11.). **Alle 19 Bilder eingebaut (18.11., Version 170)** unter `assets/story/` (2208 × 960, JPG Qualität 84). Kleinigkeiten: `lueneburg_saline` hat unten einen leeren braunen Streifen, `erste_ernte` zeigt unten links den Papierrand – beides im Textbereich. Für weitere Bilder gilt: Claude legt sie unter `assets/story/` ab (21:9 JPG im Kinoformat, auf ~2520 px Breite verkleinern; Anzeige mit schwarzen Balken). Seitenverhältnisse stehen nie im Prompt, nur in der Überschrift – Kevin stellt sie im Bildprogramm ein (18.11.). Test in der Sitzung: `story.js` (Intro, Wahrzeichen vor Kampf, einmalig, Galerie). Kevins „Nephilim“: im Spiel gibt es Ophan, Cherub und Seraph – das Bild zeigt einen Seraph.

## Koop: Beitritt nur mit Zustimmung, Prüfsummen (Version 161)

Kevin (18.11.): Bestätigung ja (mit Namen), längere Raumcodes nein, Plausibilitätsprüfung der Gast-Ergebnisse nein („Man spielt nur, mit wem man spielen will“), Prüfsummen ja.

- **Beitritt:** Jeder Spieler gibt sich im Koop-Fenster einen Namen (`harmbringer_playerName`). Der Gast schickt ihn mit `hello`; beim Gastgeber erscheint `#coopAsk` („X möchte beitreten – Zulassen/Ablehnen“). Bis zur Zustimmung erreicht nichts vom Neuen das Spiel (`Coop.receive(m, link)`: fremde Verbindungen dürfen nur anklopfen). Zugelassene bekommen ein Token (`c.coopGuest = {name, token}`, beim Gast `harmbringer_coopToken_<Code>`) und kommen nach Abbruch ohne neue Frage zurück. Ein verbundener Gast wird nur nach Zustimmung ersetzt. Lokaler Testmodus (zwei Fenster) fragt nicht. Namen erscheinen im Chat und in den Meldungen. Test: `coopask.js` in der Sitzung.
- **Prüfsummen:** PeerJS (`integrity`, sha256) und Three.js (Importmap `"integrity"`, sha384 für three.module.js, CSS2DRenderer, GLTFLoader, BufferGeometryUtils). Werte am 18.11. gegen die Dateiliste von jsDelivr geprüft (sha256 identisch mit Git-Tag r160). Neue Three-Version = neue Prüfsummen, sonst startet das Spiel nicht. Die Test-Werkzeuge in `tools/test/` entfernen den Block (sie liefern Attrappen statt three.js).
- Google Fonts (CSS) lässt sich nicht per Prüfsumme sichern (Inhalt je Browser verschieden); CSS führt keinen Code aus.

## Anführer schwächer, stehen wieder auf (18.11.2026, Version 173)

Kevin: „Mach den Lich und Kommandeure wieder schwächer. Wenn aber mindestens eine Einheit überlebt, steht er am Ende des Kampfes wieder auf. Alle Kommandeure und der Lich sollten dann aber gewisse Buffs bringen.“

- Schwächer: `lichArmyBonus` (3/0,25/1 je Kommando-Punkt, 2/0,25/0,5 je Eroberung), `COMMANDER_BONUS` ×3 / +2 / +10, `LEADER_GUARD` 0,15.
- Wieder aufstehen: `Battle.leaderDown(u)` merkt gefallene Anführer (`b.fallenLeaders`, Regel `risesAgain`: Lich, Rang COMMANDER oder UNIQUE), `Battle.risen()` / `risenText()` beim Sieg, Rückzug, Abzug; halbe LP. Kein Automatik-Kampf mehr nach dem Tod des Lichs (`b.auto` bleibt aus), Rückzug am nächsten eigenen Zug. Die Verwaisten (`Stranded`) entstehen dadurch nicht mehr, der Code bleibt für alte Spielstände.
- Buffs: neue Auren `DOMINION` (Lich, +10 % Schaden aller Untoten) und `DRILL` (Todesritter, Krieger und Maschinen +15 %), wirken über `auraDamagePct`/`auraEliteDamagePct` in `Abilities.damageMul`; fällt der Träger, zieht `leaderDown` die Aura aus `b.fx` ab.
- Test in der Sitzung: `rise.js` (Sieg, Rückzug, Niederlage, Aura erlischt).
- **Nicht nachgemessen:** Balance-Matrix und Kampagnen mit den neuen Werten.

## Story-Bilder für jeden Ort, jedes Artefakt, jeden Kommandeur (Texte fertig, Bilder offen)

Kevin (18.11. abends): mindestens ein Story-Bild je Ort, je Artefakt und je Kommandeur, den man findet (geklärt: alle 192 Orte inkl. Dörfer, alle 7 Kommandeure = 4 Ahnen + 3 rekrutierbare). Eingebaut: 204 neue Szenen in `story` (`ort_<id>` mit `on: "battle"`, `art_<id>` mit `on: "artifact"`, `cmd_<id>` mit `on: "commander"`), Code `Story.gain` (Aufrufe beim Artefaktfund, beim Erheben eines Ahnen, in `Recruitment.recruit` für `commander`), `Story.beforeBattle` spielt Ort + Regel-Szene nacheinander, Galerie zeigt nur Gesehenes. Prompts in `design/ui_bilder.md` Abschnitt 0 (Orte nach Entfernung vom Hügelgrab sortiert). **Bilder fehlen** – bis dahin Platzhalter mit Titel. Texte geschätzt nach Ortsgeschichte um 1371; Fakten bewusst vorsichtig (keine späteren Ereignisse wie Luther, Universitäten, Vitalienbrüder).

## Was als Nächstes sinnvoll wäre (nichts davon begonnen)

- **New Game+:** Entwurf im Design-Dokument („New Game+“, 18.11.2026) – Vermächtnis, die Lebenden erinnern sich (Doktrinen Stufe 2, Orden vom Grabe als Jäger), Heimsuchungen, Freischaltungen, neue Ziele. Dazu Abschnitt 7 „Epochen“ (Kevin: „finde das super“): jedes New Game+ 100 Jahre später, 1471 → 1571 → 1671 → … (keine feste Zahl, Epochen kommen nach und nach), Lebende mit Feuerwaffen, Hexenjägern, Festungen, verblassende Mythen, Schadenstyp Schießpulver, Feuerbestattung gegen die Leichen-Wirtschaft. Nicht umgesetzt; drei offene Fragen an Kevin stehen dort.

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
