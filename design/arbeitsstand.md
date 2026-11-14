# Arbeitsstand (Übergabe-Notiz)

Diese Datei hält fest, woran gerade gearbeitet wird, damit eine andere Sitzung (auch ein anderes Modell) nahtlos weitermachen kann. Sie wird nach jeder Etappe aktualisiert. Erledigtes wandert ins Design-Dokument (`design/design_notes.md`) und fliegt hier raus.

Stand: 14.11.2026, 23:15 Uhr · letzte veröffentlichte Version: 135 (`b02cff6`)

## Auftrag (Kevin, 14.11.2026)

> Das Spielprinzip mit dem Anschleichen funktioniert noch fast gar nicht. Entwickle eine Lösung für ein ausgetüfteltes System und implementiere es danach. Allgemein verschiedene Spielstile, die durch verschiedene Einheiten ausgedrückt werden, sollten implementiert werden. Will man mobile Einheiten, will man lieber schwer aber untötbar sein oder auf aktive Fähigkeiten setzen? Was könnten noch interessante Spielmethoden sein: Masse statt Klasse, Klasse statt Masse? Mehr Kommandeure, ein Skillbaum für den Lich... Das Bausystem könnte auch noch eine Überarbeitung gebrauchen, sodass es übersichtlicher wird und die Forschung interessanter wird. Falls es dafür neue Einheiten und Kommandeure braucht, diese auch einfügen.

Drei Etappen, jede wird einzeln getestet, dokumentiert, mit `make_version.py` versioniert und auf `main` gepusht:

| Etappe | Inhalt | Stand |
|-|-|-|
| A | Schleichen 2.0 | **Code eingebaut, noch nicht getestet, noch nicht committet** |
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

## Etappe A – Schleichen 2.0 (Entwurf = eingebauter Stand)

Alles in `index.html`. Werte stehen gesammelt in `const STEALTH` (über `const Stealth`), Feldgröße in `const APPROACH` (über `class Battlefield`).

**Anmarschzone.** `Battlefield` hat `core` (= `node.size`, danach richtet sich die Siedlung) und ein größeres `size` (30 bei Orten bis 16, sonst mindestens 40; Begegnungen unverändert). `Battle.deploy` stellt erst die Verteidiger, ruft bei Ankunft `SURPRISE` `Alarm.assign(b)` und stellt die Untoten dann außerhalb jeder Sichtweite auf (`far + APPROACH.margin`).

**Rollen der Wachen** (`Alarm.assign`): Posten (`role: 'post'`, auf einem Ring um den Ort, Blick nach außen), Streife (`'patrol'`, läuft einen Ring aus 6 Wegpunkten, 2 Felder pro Zug), Ruhende (`'rest'`, nachts `asleep`: sehen nichts, hören und riechen halb so weit). Nachts ~30 % Posten, tags ~50 %. Einzigartige, Maschinen und Sinnes-Typen (`SENSE_TYPES`) schlafen nie. Bei Tageszeitwechsel: `Alarm.timeChanged()`.

**Argwohn 0–100** (`e.aw`) statt Schalter; 50 = misstrauisch, 100 = alarmiert; ohne Reiz −20 pro Runde (`Alarm.roundEnd`), unter 50 beruhigt sich die Wache und geht zurück (`e.away`, `Alarm.goHome`).

| Reiz | Argwohn | Regel |
|-|-|-|
| Sicht nah (≤ halbe Sichtweite) | +100 | Kegel ±1 Richtung, Sichtlinie; geprüft auf **jedem Schritt** des Wegs (`Stealth.exposure`) |
| Sicht fern | +60 | Sichtweite: Tageszeit, Deckung des Bodens (`STEALTH.cover`: hohes Gras/Sumpf/Moor −2, Heide/Matsch/Friedhof −1), Größe (klein −1, groß +1/+2), Geister −1, Nebel → 1 |
| bleibt in Sicht (Rundenende) | +30 | `Alarm.look(e, true)` |
| Gehör | +40 | Radius = Gehör × Lautstärke / 2; Lautstärke = `noise` der Einheit, +1 ab 12 Kreaturen, **−2 beim Schleichen** (höchstens halbe Bewegung, aufgerundet) |
| Geruch (einmal pro Runde) | +30 | Radius = Geruch × Wind (1,5 / 0,5) × `scent` / 3; Geister riechen nicht |
| Tote gefunden | +60 | gefallene Verteidiger (`b.bodies`) in Sicht; Ghul-Leichenfraß beseitigt sie |
| Kampflärm | +40 | im Umkreis max(3, Gehör); **nicht**, wenn ein Stapel durch einen Überraschungsschlag komplett fällt („lautlos“) |
| Krachen (Tor, Mauer, lauter Zauber) | 100 | `Alarm.crash` |

**Alarmkette.** Der Alarm breitet sich nicht mehr von selbst aus. Ein Alarmierter ruft in seinem nächsten Zug (`Alarm.shout`, Radius max(3, 2 × Gehör)) – stirbt er vorher, weiß es keiner. Der erste Rufer in der Nähe (≤ 10 Felder) von Kirche, Kapelle oder Wachturm wird Glöckner (`b.bellRunner`, Symbol 🔔) und läuft hin (`Alarm.runToBell`); kommt er an, sind alle wach (`b.bell`).

**Misstrauische** gehen zum Ort des Reizes (`e.lookAt`), schauen sich dort um (`Alarm.investigate`), statt zur nächsten Einheit zu laufen.

**Belohnung** (`Battle.finish`): Sieg ohne einen einzigen Ruf = „Lautlos“: die Bedrohung aus diesem Angriff wird zurückgenommen (`b.threatAdded`), +25 % Leichen und Knochen. Glocke geläutet: Bedrohung der Fraktion +10.

**Angriffsplan** (`UI.attackPlan`, vor jedem Angriff über die Knöpfe): Kompass mit 6 Seiten, Wind in der Mitte, grün = gegen den Wind, rot = mit dem Wind; Umgehen kostet 1 Std. pro Sechstel; „Bis zur Nacht warten“. `Battle.start(node, exp, plan)` mit `plan.dir`. Tests, die `Battle.start(node)` direkt rufen, laufen ohne Dialog.

**Anzeige.** Marken über den Wachen: z schläft, • wach, ↻ Streife, ? misstrauisch, ! alarmiert, 🔔 Glöckner; darunter ein Argwohn-Balken. Kegel: gelb = ferne Sicht (misstrauisch), orange = nahe Sicht (Alarm). Bewegungsfelder: grün = leise, blau = normal. Wegvorschau: hell = unbemerkt, orange = misstrauisch, rot = Alarm, dazu Text im Tooltip (`Stealth.preview`). Einheitenkarte zeigt Rolle, Sinne und Argwohn.

**Noch zu tun für A**

- [ ] Testen: `meas.js` (Start-Messung Tag/Nacht), echter Kampf im Test-Browser, Regressionstests (`test_*.js`), Koop-Tests.
- [ ] Werkzeuge: Fähigkeits-Effekte `LURE` (Totenlicht lockt Wachen zu einem Feld, höchstens bis knapp unter Alarm) und `FOG` (Grabesnebel: `b.fog`, Sicht auf Einheiten im Nebel = 1) in `tools/gen_data.py` und `Abilities.use`. `b.fog` und die Ausnahme „leise Fähigkeiten“ in `castAbility` sind schon vorbereitet.
- [ ] `const TRAITS` anlegen (wird von `Battle.surpriseMul` für das Merkmal ASSASSIN erwartet, kommt mit Etappe B).
- [ ] Design-Dokument: Abschnitt „Alarm schlagen“ durch das neue System ersetzen. `BUGS.md` bei Bedarf.

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

Liegen nur im flüchtigen Arbeitsordner der Sitzung, nicht im Repo. Prinzip zum Nachbauen: Playwright (Chromium ist vorinstalliert) lädt `index.html` über `file://`, leitet die Three.js-Adressen von jsDelivr auf eine lokale Kopie um und hängt vor dem letzten `</script>` eine Zeile an, die `Battle, game, newGame, DATA, UI, Campaign, Alarm, Stealth …` als `window.__T` herausgibt. Danach per `page.evaluate` ein neues Spiel starten und `Battle.start(node)` rufen. **Nicht** Kevins Browser im Claude-Desktop zum Testen benutzen.
