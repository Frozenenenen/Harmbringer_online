# Harmbringer – Hinweise für Claude

Fantasy-Taktikspiel mit norddeutscher Mythologie: Ein Lich erwacht 1371 im Hügelgrab am Wilseder Berg und zieht bis zum Brocken.

## Plattform und Orte

- **Browser, ohne Engine.** Keine Unreal-, Unity- oder Godot-Lösungen vorschlagen.
- **GitHub:** `Frozenenenen/Harmbringer_online` (dieses Repo), veröffentlicht über GitHub Pages: https://frozenenenen.github.io/Harmbringer_online/
- **Claude-Projekt „Hambringer-Browser“** enthält Kopien von Design-Dokument und Daten. Quelle der Wahrheit ist dieses Repo.
- **Altes Godot-Projekt** (lokal `C:\Projekte\Godot\HarmbringerGodot`, GitHub `Frozenenenen/HarmbringerGodot`): **nur lesen, nie schreiben.** Es dient als Quelle für Texturen (`Textures/Tiles`, `Textures/World`) und die alte Höhenkarte (`Maps/Heightmap.png`).

## Aufbau

| Pfad | Inhalt |
|-|-|
| `index.html`, `data/` | Spielbares Spiel (Three.js r160, eine Datei, muss per Doppelklick über file:// laufen – kein `fetch` auf lokale Dateien) |
| `design/design_notes.md` | Design-Dokument (Deutsch) |
| `design/data/*.csv` | Spielwerte, Planungsstand und Quelle der Wahrheit fürs Balancing |
| `tools/` | Python-Werkzeuge: Generator, Balancing- und Schlacht-Simulation, Karten-Pipeline |
| `prototypes/worldmap/` | Weltkarte in WebGL2 (lädt per `fetch`, läuft nur über Webserver/Pages) |
| `prototypes/einheitenbuch/` | Einheitenbuch (Lesbarkeit der Einheiten) |
| `assets/figures/` | Figuren aus dem Godot-Projekt, verkleinert mit `tools/slim_figures.py` (Betrachter: `prototypes/figuren/`) |
| `assets/figures/Generated/` | **Eigene Low-Poly-Figuren aller Einheiten** aus `tools/build_units.py` (einheitlicher Stil, echte Größenverhältnisse: Mensch 1,8) – das sind die Figuren im Spiel |
| `data/portraits.js` | Einheitenbilder (Rekrutieren, Einheitenkarte), gerendert mit `tools/render_portraits.py` aus den Generated-Figuren |
| `data/figures/<einheit>.js` | Figuren fürs Kampffeld (Base64-GLB, beim Kampfstart per `<script>` nachgeladen), erzeugt mit `tools/build_game_figures.py` |
| `BUGS.md` | Fehlerliste (von Kevin gemeldete Fehler und ihr Status) |
| `design/ui_bilder.md` | Bilder fürs UI (Dürer-Stil): Prompts, Dateinamen, Verhältnisse, Stand offen/erledigt. Kevin erzeugt, Claude baut ein und pflegt die Liste (offene oben). |

## Arbeitsregeln

- **Generierte Bereiche** im Design-Dokument (`<!--GEN:…:BEGIN/END-->`, Inhaltsverzeichnis) nicht von Hand ändern. Werte in `tools/gen_data.py` bzw. `tools/campaign_data.py` ändern, dann `python tools/gen_data.py` ausführen.
- Nach Änderungen an Einheiten: `python tools/build_gallery.py`. Neue Einheit: Figur in `tools/build_units.py` (`build()` + `UNITS`), dann `build_units.py`, `render_portraits.py`, `build_game_figures.py`. Karten-Daten: `python tools/build_webmap.py --assets <Ordner mit Textures/ und Maps/>`. Danach `python tools/build_game_textures.py` (Bodentexturen fürs Spiel).
- `data/world_data.js`: Einheiten und Kampfregeln (Bereiche `// <GEN:UNITS>`, `// <GEN:RULES>`) erzeugt `gen_data.py` aus den CSVs – dort nicht von Hand ändern. Fraktionen, Orte, Gebäude, Wirtschaft sind Handarbeit.
- Spieltexte und Dokumentation auf Deutsch, Code-Kommentare auf Englisch.
- **Vor jedem Commit** `python tools/make_version.py "<Commit-Nachricht>"` ausführen: schreibt Versionsnummer und letzte Änderungen in `index.html` (Debug-Fenster F3, Tooltip).
- Änderungen **direkt auf `main` committen und pushen** – ohne Branch und Pull Request. Das Spiel spielt aktuell nur Kevin, GitHub Pages darf sofort den neuen Stand zeigen.

## Getroffene Entscheidungen (Auszug)

- Phylakterium im Hügelgrab in der Lüneburger Heide; der Kalkberg ist nur Erzählmotiv.
- Kampagnenkarte als durchgehende Landschaft (Projektion ETRS89/UTM 32N, 2017 × 1828 Höhenpunkte à ~247 m); Hex-Felder nur in instanzierten Schlachtfeldern. Spiel-Raster: 2017 × 1583 Hex-Felder (Spalten ~247 m, Zeilen ~285 m, `tools/build_game_map.py`; Position eines Orts: `--tile <lat> <lon>`). Im Spiel zeichnet `TerrainRenderer` die Oberwelt als Landschaft, `TileRenderer` nur das Kampffeld.
- Initiative linear: Tick-Kosten `2520 / Initiative`. MagicResist prozentual (5 %/Punkt, max. 50 %).
- Kampf mit Stapeln wie Heroes of Might and Magic: gleiche Einheiten = eine Figur, Schaden × Anzahl, nur die vorderste angeschlagen. Einheitenmengen und Materialien ×4 gegenüber dem Einzelfiguren-Stand; Gegner bis 3 Stapel pro Typ, max. 8 (erst ab 4 Typen); Lich bekommt Bonus pro belegtem Kommando-Punkt.
- 193 Orte über die ganze Karte; besondere Orte (`specials`: Einkommen, Vorteil oder Artefakt), Artefakte mit 3 Inventarplätzen (`artifacts`, `artifactSlots`). Neue Orte haben `lat`/`lon`, Feld über `tools/build_game_map.py --tile`.
- Totes Land (`Blight`, Werte `BLIGHT` in `index.html`) wächst um Hügelgrab und eroberte Orte; Gegnertrupps (`Raids`, Werte `raids` in `world_data.js`) erobern Orte zurück, wenn die Armee weit weg ist (> 250 Felder).
- Pantheons (`pantheons` in `world_data.js`): Region assimiliert, wenn alle Mitglieder erobert sind → keine Rückeroberung, Sitz wird Ley-Knoten (Ley-Sprung), Fraktion geschwächt. Lebende Mitglieder schicken Trupps in ihre Region.
