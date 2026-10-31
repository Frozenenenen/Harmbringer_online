# Harmbringer – One-Shot-Paket

Mit diesem Paket baut eine KI in einem Durchgang einen spielbaren Browser-Prototyp von Harmbringer: Hex-Welt aus echten Höhendaten, Reisen zwischen 19 Orten, rundenbasierte Kämpfe auf dem Gelände des jeweiligen Orts, Rekrutieren im Hügelgrab, Ziel Brocken. Kein Godot, keine Installation: eine `index.html` plus Three.js aus dem Netz.

## Inhalt

| Datei | Zweck | An die KI geben? |
| --- | --- | --- |
| `PROMPT.md` | Der vollständige Auftrag mit Regeln, Formeln, Prioritäten und Abnahmetests | Ja |
| `data/world_data.js` | Alle Spielwerte: Karte, Bodentypen, Einheiten, Fraktionen, Orte, Wirtschaft | Ja |
| `reference/floor_preview.png` | So soll die Bodentyp-Verteilung aussehen (1 Pixel = 1 Tile) | Ja |
| `data/heightmap.js` | Höhendaten als Base64, ca. 2 MB | **Nein**, nur neben die `index.html` legen |
| `data/heightmap.png` | Dieselben Höhendaten als verlustfreies Graustufen-PNG | Nein, nur zur Ansicht |

`heightmap.js` nicht anhängen: 2 MB Base64-Text füllen den Kontext der KI, ohne dass sie daraus etwas lernt. Der Prompt beschreibt das Datenformat genau.

## So geht's

**Variante A – Chat (claude.ai, stärkstes verfügbares Modell):**

1. Neuen Chat öffnen, `PROMPT.md`, `data/world_data.js` und `reference/floor_preview.png` anhängen.
2. Schreiben: „Setze PROMPT.md vollständig um.“
3. Die gelieferte `index.html` in diesen Ordner speichern, direkt neben `data/`.
4. `index.html` doppelklicken. Läuft in Chrome, Edge und Firefox.

Bricht die Antwort mitten im Code ab: „Mach genau an der Abbruchstelle weiter“ und die Teile zusammenfügen.

**Variante B – Agent mit Dateizugriff (z.B. Claude Code oder eine Sitzung mit Ordnerzugriff):**

Den ganzen Ordner bereitstellen und schreiben: „Setze PROMPT.md um und schreibe index.html in diesen Ordner. Teste es im Browser und prüfe die Abnahmetests aus Abschnitt 14.“ Das ist zuverlässiger, weil der Agent sein Ergebnis selbst starten und korrigieren kann.

## Was getestet ist

- Hex-Referenzcode im Prompt: Rundweg Welt ↔ Hex, alle Nachbarn, Richtungen, Abstände und Linien auf 40 × 40 Tiles, 0 Fehler.
- Datendateien per file:// in Chromium: Dekodierung 134 ms, Bodentypen für alle 1,57 Mio. Tiles 388 ms, keine Konsolenfehler.
- Alle Prüfwerte in Abschnitt 14 des Prompts stammen aus diesen Daten.
- Nicht getestet: das Spiel selbst. Das baut erst die KI.

## Was neu ist gegenüber den Design Notes

Damit ein spielbarer Prototyp entsteht, habe ich Lücken mit ersten Vorschlägen gefüllt. Alles davon steht in `world_data.js` und ist frei änderbar:

- **Aus den Design Notes:** Werte von Ghul, Geist und Balliste, Power-Defense-Matrix, Leichenqualität, Initiative-System, Bedrohungsabbau 5 % pro Tag, Kampffeldgrößen 16/32/64, Ortsliste.
- **Neu vorgeschlagen:** Lich, Skelett-Speerträger, Knochenschleuderer und alle Gegner außer der Balliste; sechs weitere Orte rund um die Heide (Soltau, Uelzen, Celle, Teufelsmoor, Kloster Walsrode, Kloster Medingen); Besatzungen, Beute, Kosten, Kommandolimit, Reisegeschwindigkeit; Fraktion Askanier für Berlin und Wittenberg; Gebäude- und Zaungenerierung; Gegner-KI.
- **Ghul:** Die Design Notes nennen „Physical“, das gibt es im Enum nicht. Hier: `BLUNT` mit eigener Leichenqualität 0,4 (zerfleischend).

## Wichtige Korrekturen gegenüber dem Godot-Stand

Beim Zusammenstellen sind drei Fehler aufgefallen. Sie sind hier schon richtig und betreffen auch das Godot-Projekt:

1. **Ortskoordinaten:** Die Höhenkarte zeigt nicht den OpenTopography-Ausschnitt, sondern ein 15″-Raster von 7,15° O / 54,82° N bis 14,25° O / 50,99° N. Kalibriert an Küstenpunkten (Fehmarn, Rügen, Darß, Gedser, Bungsberg), geprüft an Brocken, Kyffhäuser, Helgoland, Steinhuder Meer und weiteren. Neue Formel: `Q = round((lon − 7.1529) · 240)`, `R = round((54.8190 − lat) · 240)`. Die alten Werte lagen 45 bis 88 Tiles daneben, im Osten am stärksten.
2. **Höhenwerte:** Grau ist linear −58 bis 450 m (ca. 2 m pro Stufe), darüber gekappt. Grau 255 ist also nicht der Brocken mit 1141 m, sondern „450 m oder höher“. Daher das Harz-Plateau.
3. **Nachbar-Tabellen:** In `hex_grid.gd` zeigen je zwei von sechs Offsets auf kein Nachbarfeld, und Norden ist dort +R statt −R. Die richtigen Tabellen stehen in `PROMPT.md`, Abschnitt 4.

## Bekannte Grenzen der Daten

- 8-Bit-Höhen, über 450 m gekappt. Ein verlustfreier 16-Bit-Export aus QGIS würde den Harz modellieren.
- Keine Flüsse. Die Höhenkarte ist dafür zu grob; eine Wassermaske wäre der nächste Schritt.
