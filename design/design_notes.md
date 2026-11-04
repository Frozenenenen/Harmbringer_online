# MythosTactics – Design Notizen

*Arbeitsdokument. Ideen, Entscheidungen, offene Fragen. Wird im Laufe des Projekts erweitert.*

---

## Inhaltsverzeichnis

1. [Erweiterungsplan (Stand 31.10.2026)](#erweiterungsplan-stand-31102026)
2. [Kern-Konzept](#kern-konzept)
3. [Gameplay-Schichten](#gameplay-schichten)
4. [Lich-Mechanik & Permadeath](#lich-mechanik--permadeath)
5. [Zeitliches Setting](#zeitliches-setting)
6. [Machtknoten-Typologie](#machtknoten-typologie)
7. [Fraktionsdynamik: Patchwork vs. Zentralmacht](#fraktionsdynamik-patchwork-vs-zentralmacht)
8. [Bedrohungs-Mechanik](#bedrohungs-mechanik)
9. [Pantheon-System](#pantheon-system)
10. [Knotentypen mit klarem Profil](#knotentypen-mit-klarem-profil)
11. [Gebietseffekte als eigenes System](#gebietseffekte-als-eigenes-system)
12. [Tageszeit-System](#tageszeit-system)
13. [Variable Schlachtfeldgrößen](#variable-schlachtfeldgrößen)
14. [Schlachtfeld-Bausteine](#schlachtfeld-bausteine)
15. [Blender Asset-Liste](#blender-asset-liste)
16. [Hintergrund / Lore](#hintergrund--lore)
17. [Einheiten-Rang-System](#einheiten-rang-system)
18. [Einheiten-Datenstruktur](#einheiten-datenstruktur)
19. [Einheiten-Visualisierung](#einheiten-visualisierung)
20. [Weltkarte (Landschaft)](#weltkarte-landschaft)
21. [Tile-System (Schlachtfelder)](#tile-system-schlachtfelder)
22. [Schlachtfeld-Ankunft & Stealth-Phase](#schlachtfeld-ankunft--stealth-phase)
23. [Mythologie-Wissen als Belohnung](#mythologie-wissen-als-belohnung)
24. [Ressourcen – "Verbrannte Erde"-Prinzip](#ressourcen--verbrannte-erde-prinzip)
25. [Gräber als Rekrutierung von Kommandeuren](#gräber-als-rekrutierung-von-kommandeuren)
26. [Leichen-Ressourcen & Schadenstypen](#leichen-ressourcen--schadenstypen)
27. [Armee-Limit](#armee-limit)
28. [Kampagnen-Struktur (Idee)](#kampagnen-struktur-idee)
29. [Heide-Kampagne: Basis, Wissen, Begegnungen](#heide-kampagne-basis-wissen-begegnungen)
30. [Startort der ersten Kampagne](#startort-der-ersten-kampagne)
31. [Offene Fragen / Später entscheiden](#offene-fragen--später-entscheiden)
32. [TODO (Implementierung)](#todo-implementierung)
33. [Sicht- und Sinne-System](#sicht--und-sinne-system)
34. [Technik (Browser)](#technik-browser)
35. [Story- und UI-Konzept](#story--und-ui-konzept)
36. [Schnittstellen zwischen Systemen](#schnittstellen-zwischen-systemen)
37. [Entwicklungs-Roadmap](#entwicklungs-roadmap)

---

## Erweiterungsplan (Stand 31.10.2026)

Ziel dieser Überarbeitung: Lücken und Widersprüche im Dokument schließen und die **Einheiten so gestalten, dass sie auf dem Hex-Feld auf einen Blick lesbar sind** (Fraktion, Rolle, Zustand, Bedrohung).

### A) Konsistenz-Fixes (umgesetzt)

| Problem | Lösung |
|-|-|
| Ghul nutzt `PowerType = Physical`, den es im Enum nicht gibt | Neuer PowerType **`Rend`** (Zerfleischen: Biss, Klaue). Ghul → `Rend` |
| Leichen-Tabelle ("Zerfleischend", "Sauber") nicht an PowerType gekoppelt | Leichen-Tabelle hat jetzt eine PowerType-Spalte – eine Quelle der Wahrheit |
| `MaxEnergy` wird zur Laufzeit gelesen, fehlt aber in `S_UnitData` | Feld ergänzt |
| Stealth nennt "Lautstärke" und "Geruchsbildung", Datenstruktur hat nur Wahrnehmungs-Radien | Neue Felder `NoiseLevel` / `ScentLevel` (was die Einheit *abgibt*) getrennt von `HearRadius` / `SmellRadius` (was sie *wahrnimmt*) |
| `Rang – E_UnitRang` vs. Enum `UnitRank` | Einheitlich `Rank – E_UnitRank` |
| Rang-System kennt "Kommandeur", Enum nicht | `UnitRank` um `Commander` ergänzt |
| Inhaltsverzeichnis: Eintrag "Zeit-System" ohne Kapitel, TODO fehlte, Reihenfolge falsch | Inhaltsverzeichnis neu, folgt der Dokument-Reihenfolge |

### B) Einheiten-Visualisierung (umgesetzt, neues Kapitel)

Siehe [Einheiten-Visualisierung](#einheiten-visualisierung). Kernpunkte:

1. **Drei-Ebenen-Lesbarkeit:** Silhouette = Rolle, Farbe = Fraktion, Sockel/Overhead = Zustand
2. **Rollen-Enum** `UnitRole` als neues Datenfeld, steuert Silhouette und Icon
3. **Größen-Skalierung** aus `Size` (1–4) mit festen Höhen
4. **Fraktions-Paletten** mit Primär-, Akzent- und Leuchtfarbe
5. **Hex-Sockel** unter jeder Einheit: Freund/Feind farbenblind-sicher über Form
6. **Rang-Abzeichen**, **Overhead-UI** (HP-Segmente, Schild, Status) und **Schadensvorschau** aus der Power-Defense-Matrix
7. **VFX-Farbcode pro PowerType** – Spieler lernt Schadenstypen über Farbe
8. **Zustands-Darstellung** (Stealth, Spektral, Fliegend, führerlos, angeschlagen)
9. **Leichen zeigen ihre Qualität** – verbindet Kampf-Optik mit Ökonomie
10. **Token-Modus** beim Herauszoomen (Zinnfiguren-Look)
11. **Datenmodell `S_UnitVisual`** getrennt von Spielwerten
12. **Lesbare Platzhalter** schon in Phase 1 (Kapsel + Rollen-Icon + Fraktionsfarbe)
13. **Einheiten-Steckbriefe** für die 10 ersten Modelle

### C) Roadmap-Einordnung (umgesetzt)

Visualisierung wird nicht ans Ende (Phase 8) geschoben, sondern **wächst mit**:

| Phase | Visualisierungs-Schritt |
|-|-|
| 1 | Lesbare Platzhalter, Hex-Sockel, HP-Segmente, aktive Einheit hervorgehoben |
| 2 | Fraktionsfarben, Rollen-Icons, Initiative-Leiste mit Platzhalter-Portraits |
| 3 | Schadensvorschau, VFX-Farbcode, Status-Icons, Stealth-Darstellung, Sichtkegel |
| 5 | Leichen-Qualität sichtbar, Anführer-Aura |
| 6 | Echte Modelle der Heide-Einheiten nach Steckbrief |
| 8 | Token-Modus, Animations-Polish, Portraits final |

### D) Spätere Erweiterungen (nur geplant)

- ~~Steckbriefe für alle Heide-Gegner~~ → umgesetzt 01.11.2026 (Moorgeist, Irrlicht, Heideschwester, Hügelgrab-Druidin, Armbrustschütze inkl. Werte, Fähigkeiten, untote Versionen). Dafür neue Fraktion `HeathSpirits`.
- ~~Steckbriefe für Pantheon der Heide und Lich-Armee-Erweiterung~~ → umgesetzt (siehe E)
- Lesbarkeits-Test als festes Ritual pro neuer Einheit (siehe Checkliste im Visualisierungs-Kapitel)
- ~~Visuelle Variation untoter Freischaltungen~~ → für Heide-Gegner umgesetzt

### E) Arbeitspaket 01.11.2026 abends (umgesetzt)

| Paket | Wo im Dokument |
|-|-|
| Heide-Pantheon: Wode, Hügelgrab-Zwergenkönig, Heidekönigin inkl. Ley-Bund-Synergie, Kampfplätzen, Belohnungen | Pantheon-System → Heide-Pantheon |
| Werte für alle 22 Einheiten, neue Lich-Einheiten (Zombie, Nekromant, Fleischriese), Schwarzer Hund | Einheiten-Datenstruktur → Gesamtübersicht |
| Fähigkeiten als Daten (`S_AbilityData`, 31 Fähigkeiten), Enums ergänzt (`StatusEffect.None/Confused`, `EffectType.ModifyTerrain`) | Einheiten-Datenstruktur → Fähigkeiten |
| Status-Effekte mit Symbol, Farbe, Standardwirkung | Einheiten-Visualisierung |
| Vorschläge für 5 offene Fragen | Offene Fragen |
| Import-fertige CSVs `DT_Units`, `DT_Abilities`, `DT_FactionPalettes` | Ordner `design/data/`, Technik → Spielwerte |
| Visual-Verknüpfung vereinfacht: gleiche Row-Names statt `VisualRow`-Feld | Einheiten-Datenstruktur |

### F) Arbeitspaket 01.11.2026 nachts (umgesetzt)

| Paket | Wo im Dokument |
|-|-|
| Balancing-Simulation (`sim.py`): Treffer-bis-Tod-Tabellen, Kosten-Nutzen pro KP | Einheiten-Datenstruktur → Balancing-Check |
| Regeln präzisiert: MagicResist prozentual, SoulShield als Schild-Pool, neue lineare Initiative-Formel | Einheiten-Datenstruktur |
| Korrekturen: Fleischriese 15 → 8 KP, Zombie Initiative 3 | Gesamtübersicht, Armee-Limit |
| 6 untote Freischaltungen als Daten (Moorleiche, Totenlicht, Gefallene Schwester, Grabdruidin, Knochenschütze, Totenjäger) | Gesamtübersicht, Steckbriefe |
| Basis-Gebäude (17 Stufen), Wissens-Freischaltungen, 6 Begegnungen der Heide, Ressourcen-Kreislauf | Heide-Kampagne |
| Schlacht-Simulation: Siegchance, Dauer, Verluste, Netto-Beute pro Begegnung und Armee-Stufe | Heide-Kampagne → Simulierte Schwierigkeitskurve |
| Einheitenbuch: interaktive Galerie aller Einheiten mit Lesbarkeits-Schaltern (Artifact „MythosTactics Einheitenbuch“, Quelle `prototypes/einheitenbuch/`) | Einheiten-Visualisierung |
| Befund aus dem Einheitenbuch: Hexen-Palette zu dunkel → korrigiert, Mindest-Helligkeit als Regel | Fraktions-Paletten |
| Inhaltsverzeichnis wird automatisch erzeugt | – |

### G) Weltkarte als Landschaft (02.11.2026, umgesetzt)

| Paket | Wo im Dokument |
|-|-|
| Entscheidung: Phylakterium im Hügelgrab, Kalkberg nur Erzählmotiv | Startort, Offene Fragen |
| Kampagnenkarte als Landschaft statt Hex-Welt; Hex nur noch in Schlachtfeldern | Weltkarte, Tile-System |
| Projektion UTM 32N behebt die 1,65-fache Breitenverzerrung der alten Pixelkarte | Weltkarte |
| `geo.py` (Projektion ohne Zusatzpakete), `worldmap.py` (Kennwerte, GDAL-Befehle) | Weltkarte |
| Orte und Begegnungen auf Breite/Länge umgestellt, Kartenpositionen berechnet; `DT_Encounters` mit `Lat`, `Lon`, `MapX`, `MapY` | Kartenkoordinaten der Orte, Heide-Kampagne |
| Plattform Browser, ohne Engine; Hinweise auf andere Engines entfernt, neues Kapitel „Technik (Browser)“ | Kern-Konzept, Technik |
| Browser-Weltkarte: ein Vertex pro Höhenpunkt, Gitter nur im Sichtbereich + Rand, Zoom-abhängige Auflösung, Bodentextur je Höhenpunkt mit radialer Überblendung (Texturen aus der bestehenden Textur-Sammlung) | Weltkarte |
| `build_webmap.py` – Browser-Daten aus Höhenmodell (oder Übergangsweise aus der alten 8-Bit-Karte) | Weltkarte → Daten-Pipeline |

---

## Kern-Konzept

Rundenbasiertes Taktikspiel im Stil von Heroes of Might & Magic, kombiniert mit Deckbuilder-Elementen à la Wildfrost. Der Spieler ist ein **untoter Lich-Overlord**, der regional begrenzte Kreuzzüge führt und dabei auf verschiedene lokale Mythologien trifft.

**Setting-Fokus:** Deutsche Mythologie und Sagen. Erste Kampagne: Norddeutschland – von der Nordseeküste bis zum Harz. Brocken als thematisches Herz/Finale (Walpurgisnacht, Hexen).

**USP:** Deutsche Mythologie ist in Games kaum repräsentiert – hohe Eigenständigkeit.

**Plattform:** Browser, ohne Engine. Repo `Frozenenenen/Harmbringer_online`, spielbar über GitHub Pages (siehe Technik).

---

## Gameplay-Schichten

### 1. Taktisches Kampfsystem (Priorität 1 – wird zuerst gebaut)
- **Hex-Felder** (nicht quadratisch)
- Hindernisse, Deckung, Höhenunterschiede auf dem Feld
- **Deckung als Kanten-Eigenschaft:** Jede Hex-Kante kann Eigenschaften haben (z.B. "Wand")
  - Wand auf einer Seite = Deckung, man kann raus schießen
  - Wände auf beiden aneinandergrenzenden Feldern = echtes Hindernis
- Einheiten werden produziert und in Armee aufgenommen (Deckbuilder-Mechanik erstmal verworfen)
- Rundenbasiert (mit vorgeschalteter Stealth-Phase, siehe unten)
- 3D-Szene mit drehbarer Kamera
- **Kampfdauer-Ziel:** 15–20 Minuten pro Schlacht, damit Kampagnen-Sessions tragfähig bleiben

### 2. Kampagne / Kreuzzug (Priorität 2)
- **"Alle Wege führen nach Rom"-Karte:** Grabhügel im Zentrum, Wege in alle Richtungen
- **Landschaftskarte statt Hex-Welt:** Die Kampagne spielt auf einer durchgehenden 3D-Landschaft aus echten Höhendaten; Kämpfe laden instanzierte Hex-Schlachtfelder (siehe Weltkarte)
- Spieler wählt eine Richtung, weiß nicht was ihn erwartet (Fog of War)
- Natürliche Barrieren (Flüsse, Gebirge, Sümpfe) können Wege blockieren
- Umgehung oder Überwindung durch Spezial-Einheiten (z.B. "Untote, die über Wasser gehen")
- Besiegte Knoten werden "freigeschaltet" mit Infos (Name, Gegner-Typ, Thumbnail)

### Einfluss auf Regionen

- Eroberte Gebiete sind nur so lange sicher, bis das **komplette Pantheon** (Gruppe von Wesen) einer Region besiegt ist
- Halb-erobert = regeneriert bei Abwesenheit (übrige Pantheon-Mitglieder erstarken)
- Komplett-erobert = permanent assimiliert
- **Strategische Konsequenz:** Spieler muss wählen zwischen "eine Richtung komplett durchziehen" (sicher, aber einseitig) oder "viele Richtungen antasten" (flexibel, aber instabil)
- Hält Spielfluss dynamisch, bestraft stures Vorrücken
- Alternative/Ergänzung (später): Garnisonen – Einheiten zurücklassen als Halte-Mechanik, mit Opportunitätskosten

### Warum nicht direkt zur Hauptstadt?

Die Antwort liegt im **Fog of War** – keine komplexe Regel-Mechanik nötig.

- Spieler kennt die Region anfangs nicht
- Späher klären nur die nähere Umgebung auf
- Hauptstadt wird erst spät entdeckt, oft tief in der Region
- Unterwegs liegende Ortschaften sind nötig für Ressourcen-Nachschub
- Hauptstadt ist schlicht *stärker* als jede andere Ortschaft (höhere Gegnerwerte) – frontal ohne Vorbereitung = Tod

**Lokale Regeneration durch Pantheon-Mitglieder:** Wenn ein Dorf getilgt wird und ein Pantheon-Gott noch lebt, kann dieser es wieder aufbauen. Das ist ein lokales, sichtbares Event (im Fog of War sogar: "beim nächsten Besuch steht das Dorf wieder"), keine globale Rechnerei.

**Pantheon komplett besiegt → Region dauerhaft assimiliert.** Keine weitere Regeneration möglich.

### Ley-Linien-Teleportation

Bei wachsender Karte entsteht ein Reiseproblem (Late-Game-Logistik). Lösung: **Assimilierte Regionen werden Teil eines Teleportnetzes.**

**Ley-Knoten = Pantheon-Hauptsitz.** Das ist kein Zufall:
- Menschen und mythologische Wesen siedeln dort, wo die Erde magisch stark ist
- Kultstätten entstehen an Ley-Knoten, Dörfer um Kultstätten, Pantheon-Zentren aus Siedlungen
- **→ Jede Region hat einen klaren Hauptsitz am Ley-Knoten, wo das Pantheon residiert**

**Mechanik:**
- Ley-Knoten sind mystische Orte (Hünengräber, Steinkreise, heilige Berge)
- Sobald das Pantheon einer Region geschlagen und der Knoten erobert ist, wird er für den Lich aktiv
- Reise zwischen aktiven Knoten: direkt, ohne Weg über das Wegenetz der Karte
- **Optional:** Kosten (nekrotische Energie) zur Dosierung
- Wenn ein Pantheon regeneriert, könnte der Knoten wieder blockiert werden → macht Regeneration logistisch spürbar

**Konsequenz für Kampagnen-Struktur:**
- Jede Region hat einen **dramatischen Ziel-Kampf am Ley-Knoten** – der Boss-Fight der Region
- Kleinere Pantheon-Mitglieder sitzen vorgelagert (Außenposten, Haine, Außensiedlungen)
- Das Zentrum ist Belohnungs-Gipfel: Pantheon besiegt + Knoten erobert + Artefakte + Ahnen-Gräber + Einheiten-Freischaltung auf einmal
- Spieler hat immer ein klares strategisches Ziel pro Region

**Beispiele:**
- Lüneburger Heide → Ley-Knoten auf altem Kultplatz (Wilseder Berg?), Urmutter-Kult-Priesterin / heidnische Ratsversammlung
- Nordseeküste → Ley-Knoten in alter Küstenzitadelle (Rungholt-Ruinen, heidnische Opferinsel), Blanker Hans / Meerkönig
- **Harz (Finale):** Brocken selbst – der **mächtigste Ley-Knoten Norddeutschlands**, Sitz des Hexenrats / der Walpurgisnacht

**Späterer Ausbau / offene Ideen:**
- Pantheon ist am Ley-Knoten gebufft (Heimvorteil) – Finale wird härter
- Knoten fällt → Pantheon bricht zusammen (andere Mitglieder geschwächt) – Boss-Mechanik-Pattern
- Randmitglieder halten Verteidigung aufrecht → man muss sie trotzdem schlagen, um zum Zentrum zu kommen
- Schlachten auf Ley-Knoten haben besondere Kampf-Effekte (Magie verstärkt, Schutzrituale)

### Gothic-Prinzip: Freiheit mit Gefahr

- Spieler kann in jede Richtung expandieren, aber manche Regionen sind tödlich für frühe Armeen
- **Späher-Einheiten** (gestaffelt nach Qualität) können Regionen vorab erkunden:
  - **Rabenspäher (billig):** zeigt Silhouetten/grobe Menge, leicht zu täuschen
  - **Schattenhund (mittel):** riecht Lebenskraft, erkennt Stärke-Differenzen, mittelschwer zu täuschen
  - **Geisterspäher (teuer):** sieht durch Illusionen, zeigt echte Bedrohungslage
- Späher-Ergebnisse liefern **Gefahrenindikatoren:** geschätzte Gegner-Menge, Pantheon-Typ, grobe Stärke
- Späher können sterben, nicht alles sehen → Rest-Unsicherheit bleibt
- **Visuelle Gefahrenskala auf der Karte:** grau (unbekannt) → grün (machbar) → gelb (riskant) → rot (tödlich)
- Spieler darf rot betreten – auf eigene Gefahr. Hohes Risiko, hohe Belohnung.

### Kloster-Mechanik: Verhüllte Gefahr

- **Klöster stören Späher-Magie** – umliegende Regionen werden "verhüllt"
- In verhüllten Gebieten sind Späher-Informationen **gezielt verfälscht** (zu stark/zu schwach dargestellt, falsche Gegner-Typen)
- Bessere Späher durchdringen die Verhüllung teilweise
- Komplette Wahrheit erst nach Entweihung des Klosters
- **Klöster werden zu strategischen Zielen:** nicht wegen ihrer Ressourcen, sondern wegen der **Informationsüberlegenheit der Kirche**, die gebrochen werden muss

### Irrlicht-Gefahr für Späher

- In Gebieten mit **Irrlichtern, Moorgeistern oder ähnlichen Wegverwirrungs-Wesen** können Späher vom Weg abkommen
- Mögliche Konsequenzen: Späher kommt **verspätet** zurück, kommt mit **falschen Informationen** zurück, oder kommt **gar nicht** zurück (verloren oder tot)
- Betroffene Gebiete (Beispiele): Teufelsmoor, andere Moorregionen, Spreewald, nebelige Heide-Stellen
- **Höherwertige Späher** (Geisterspäher) sind weniger anfällig
- Macht Moor- und Sumpfregionen mechanisch zu eigenen Gefahrenzonen, nicht nur thematisch

### 3. Basenbau (Priorität 3)
- Zwischen Kreuzzügen Ressourcen in Gebäude investieren
- Gebäude produzieren Einheiten (wie Heroes) oder verstärken sie (wie Warcraft 3 Schmiede)
- Keine Verteidigung – nur ein Weg

---

## Lich-Mechanik & Permadeath

- **Einheiten kehren nie zurück.** Tote Einheit = weg.
- **Der Lich ist unsterblich** durch sein Phylakterium in der Basis. Wenn er fällt, kehrt er zurück.
- Phylakterium-Rückkehr hat vermutlich Kosten (Ressourcen? Zeit?) – noch offen.
- Dadurch: Basenbau wird zwingend zentral, weil Einheiten permanent nachproduziert werden müssen.

### Niederlagen & Lich-Rückzug

- **Eigene Einheiten überleben Niederlagen nicht.** Was reingeht, kommt nicht lebend raus, wenn der Kampf verloren geht.
- **Aktiver Lich-Rückzug als Spieler-Entscheidung:** Statt einen verlorenen Kampf bis zum bitteren Ende auszuspielen, kann der Spieler den Lich vorzeitig zurückziehen.
  - **Dauer: mindestens eine Runde** – kein sofortiger Abbruch
  - In der Rückzugs-Runde ist der Lich **verwundbar** (konzentriert sich auf Teleport)
  - Wenn er in dieser Runde fällt, kippt der Rückzug in eine erzwungene Niederlage
  - Eigene Einheiten verteidigen währenddessen
- **Aktiver Rückzug** kostet **weniger Mana** als ein erzwungener Lich-Tod
- **Niederlage = keine Ressourcen mit:** Bei Lich-Tod oder Rückzug funktioniert die Teleport-Magie nicht – Leichen, Seelen, Wissen bleiben auf dem Schlachtfeld
- Verhindert Cheesing: Spieler kann nicht "ein bisschen kämpfen, dann fliehen, Verluste mitnehmen"

### Teleportations-Magie für Leichen
- Der Lich kann **nur wirklich Tote** teleportieren – sich selbst nicht (er ist nur "un-tot")
- Erklärt die logistische Rückführung der Leichen ins Phylakterium/Basis
- Vermutlich als großes Ritual am Ende der Schlacht (nicht kontinuierlich mitten im Kampf)
- Wenn der Lich selbst fällt, zählt er in dem Moment als "wirklich tot" und die eigene Magie reißt ihn mit zurück ins Phylakterium

## Zeitliches Setting

Die Kampagne spielt im **Hochmittelalter, ca. 1350–1400**. Kein "Deutschland" – stattdessen ein Flickenteppich aus Fürstentümern, Herzogtümern, Bistümern, freien Hansestädten und Grafschaften.

- **Welfen** (Braunschweig-Lüneburg), **Askanier** (Sachsen-Wittenberg), **Erzbistum Bremen**, **Bistum Verden**, **Mark Brandenburg** usw. sind reale politische Entitäten
- Hansestädte (Lüneburg, Hamburg, Bremen) als freie weltliche Mächte
- Hexenkulte und heidnische Reste leben im Volksglauben weiter, offiziell christianisiert
- **Mythen sind Baumaterial, keine historische Dokumentation** – Mythen aus verschiedenen Epochen (Irminsul, Walpurgisnacht, Moorleichen) werden als "gleichzeitig existierend" behandelt

**Mögliche lokale Flavors (optional, nicht Hauptplot):**
- Lüneburger Erbfolgekrieg (1370–1388) erklärt mechanisch, warum Lüneburg schwächer ist als Hamburg – Burg auf dem Kalkberg wurde von den eigenen Bürgern zerstört
- Große Mandränke 1362 (Untergang Rungholts) als beobachtbares Ereignis

---

## Machtknoten-Typologie

Die Karte zeigt **drei Arten von Machtknoten**, alle gleichberechtigt als Ziele. Der Lich hat keine Sonderbeziehung zu einer Fraktion – sein Hass gilt allem Leben.

### Typen

**Mythologisch-magische Knoten:**
Hexenzirkel, Nöckenbrunnen, heidnische Hünengräber, Moor-Irrlichter-Sippen, Hexentanzplätze.

**Menschlich-weltliche Knoten:**
Hansestädte, Herzogsburgen, Ritterorden-Komtureien, Handelssiedlungen.

**Christlich-geistliche Knoten:**
Klöster, Bischofssitze, Wallfahrtsorte.

Pantheons können **gemischt** sein – eine Region kann aus heidnischem Moorzirkel, Heideklosterschwester, Herzogsvasall und Dorfpriester bestehen. Thematische Vielfalt innerhalb einer Region.

### Geografische Logik: Ley-Linien vs. Flüsse

Jeder Knotentyp hat seine eigene Infrastruktur:

- **Mythische und christliche Knoten** liegen an **Ley-Linien** – mystischer Kraftlinien, die magische Machtzentren verbinden. Klöster wurden oft bewusst auf heidnische Ley-Knoten gebaut, um sie zu überschreiben.
- **Weltliche Knoten** liegen an **Flüssen und Handelswegen** – Lüneburg an der Ilmenau, Hamburg an der Elbe, Bremen an der Weser.

**Doppelknoten:** Orte, die beides sind (z.B. Hamburg mit seiner Kathedrale an der Elbe). Strategisch doppelt wertvoll, doppelt verteidigt – ideale Bossfight-Ziele.

### Zwei parallele Mechaniken

- **Ley-Netz:** Pantheon-besiegte Regionen verbinden sich zum Teleportnetz des Lichs (siehe Ley-Linien-Sektion). Mystische Gegner regenerieren bis zum Pantheon-Ende.
- **Flussnetz:** Wirtschaftliche Adern der Menschenwelt. Wenn der Lich eine Stadt flussaufwärts einnimmt, werden flussabwärts liegende Städte über Zeit geschwächt (kein Nachschub, weniger Söldner, schwächere Verteidigung). Intuitives Schwächungs-Prinzip ohne abstrakte Prozentzahlen.

---

## Fraktionsdynamik: Patchwork vs. Zentralmacht

Grundprinzip: **Zersplitterte Regionen sind leichter, geeinte Regionen sind schwerer.** Kehrt klassische RPG-Logik um.

### Drei Region-Archetypen

**Leichte Region (Patchwork):**
- Mehrere kleine Fraktionen nebeneinander, alle mit wenig Reichweite
- Gegenseitige Rivalitäten binden Kräfte (Heideschwestern bannen Moorhexen, Kloster misstraut Herzog usw.)
- Niemand koordiniert gegen den Lich
- Spieler kann Gegner nacheinander abarbeiten
- *Beispiel:* Lüneburger Heide – Moor-Irrlichter, Hügelgrab-Druidinnen, sechs Heideklöster, Lüneburger Bürger, kleine Herzogsvasallen

**Mittelschwere Region (lose Allianz):**
- Eine dominante Fraktion mit Vasallen und Verbündeten
- Reagieren koordinierter, aber mit interner Reibung
- *Beispiel:* Hansestadt mit abhängigen Dörfern, oder Pantheon-Führer mit rivalisierenden Unterlingen

**Schwere Region (zentrale Macht):**
- Eine einzige starke Macht kontrolliert alles
- Alle Ressourcen, Wachen, Magier gebündelt
- Keine interne Reibung, volle Schlagkraft
- *Beispiel:* Harz unter dem Hexenrat auf dem Brocken – Wilde Jagd, Teufel, Zwerge, Berggeister alle unter Brocken-Einfluss

### Natürliche Difficulty-Ramp

Die Schwierigkeitskurve ergibt sich aus der politischen Struktur, nicht aus Zahlenbalancing. Die Heide als Startgebiet ist intrinsisch leichter als der Harz als Endkampf – nicht weil die Gegner schwächer sind, sondern weil sie sich gegenseitig behindern.

### Spätphase: Konsolidierung gegen den Lich

Wenn der Lich zu mächtig wird, können verbleibende Fraktionen ihre Streitigkeiten beilegen und sich verbünden. Organisches Endgame-Element:
- Nach X besiegten Pantheons (oder Bedrohungs-Schwelle) fusionieren benachbarte Fraktionen
- Spürbar im Kampf: "Der Hexenzirkel hat jetzt Ritter des Herzogs als Verstärkung?"
- Welt passt sich an den Lich an, statt nur mit höheren Zahlen zu reagieren
- **Visuell:** Verbündete Fremdeinheiten tragen ihre eigene Fraktionspalette, aber den Sockel-Rand der führenden Fraktion (siehe Einheiten-Visualisierung) – der Spieler sieht sofort, wer mit wem kämpft

---

## Bedrohungs-Mechanik

Jede Fraktion hat einen sichtbaren **Bedrohungswert** (0–100 %), der ausdrückt, wie sehr sie den Lich als Gefahr wahrnimmt.

### Anstieg

Bedrohung steigt durch konkrete Aktionen des Lichs:
- Direkter Angriff auf einen Knoten der Fraktion (großer Sprung)
- Tötung eines Anführers (sehr großer Sprung, kann Panik-Allianzen auslösen)
- Entweihung von Kultstätten (großer Sprung, symbolisch)
- Indirekt durch Angriffe auf Nachbarfraktionen (kleiner Sprung)

**Anstieg in normalem Tempo, nicht sprunghaft** – Information braucht Zeit, sich zu verbreiten (siehe Wellen-Mechanik unten).

### Senkung durch Zeit

Bedrohung sinkt **exponentiell** mit Inaktivität:

- **5 % des aktuellen Wertes pro Tag** verloren
- Halbwertszeit: ~14 Tage
- Hohe Bedrohung sinkt schneller, niedrige langsamer
- Mathematisch nähert sich asymptotisch 0, ohne sie zu erreichen → "Trauma vergeht nicht ganz"

| Tag | Bedrohung | Verlust |
|-|-|-|
| 0 | 100 % | 5,0 % |
| 5 | 77 % | 3,9 % |
| 10 | 60 % | 3,0 % |
| 20 | 36 % | 1,8 % |
| 30 | 21 % | 1,1 % |
| 50 | 7,7 % | 0,4 % |
| 100 | 0,6 % | 0,03 % |

**Praktische Untergrenze:** unter ~0,5 % wird auf 0 gerundet, sonst rechnerisches Restrauschen.

### Senkung durch Niederlagen

Wenn der Lich gegen eine Fraktion **verliert**, sinkt deren Bedrohung – die Verteidiger gewinnen Selbstvertrauen.

- Maximalwert (z.B. 90 %) wird durch Niederlagen nicht überschritten
- Niederlagen bei Maximum machen Bedrohung **nicht** weiter höher (Cap-Mechanik)
- Niederlagen können sogar genutzt werden, um Maximum-Bedrohung zu senken
- Ermöglicht **Köder-Taktik:** Schwachen Trupp opfern, damit Fraktion ihre Garde lockert

### Bedrohungs-Wellen über die Karte

Ein Angriff schlägt **Wellen** durch die Karte. Bedrohung breitet sich von Knoten zu Knoten aus:

- **Innerhalb der eigenen Fraktion:** volles Tempo
- **Zu anderen Fraktionen:** halbes Tempo (nur Hörensagen)
- **Mit Distanz nimmt das Tempo ab**, läuft irgendwann komplett aus
- Vorschlag Distanz-Verfall: pro Knoten-Distanz ~30 % schwächer

Erzeugt:
- **Räumliche Strategie:** Randangriffe haben weniger Welleneffekt als Zentrumsangriffe
- **Politische Karte wird lebendig:** dichte Knotengebiete = gefährlicher für leise Operationen
- **Realistische Informationsverbreitung:** Hörensagen mit halber Intensität, später eintreffend
- **Späher werden taktisch wichtiger:** Spieler will politische Zugehörigkeiten kennen

### Vier Bedrohungs-Zonen (Verhalten)

| Zone | Wert | Verhalten der Fraktion |
|-|-|-|
| Latente Erinnerung | 0–19 % | Sinkt langsam; latente Erinnerung an den Lich |
| Aktive Wachsamkeit | 20–59 % | Verstärkte Wachen, Späher unterwegs |
| Hohe Alarmstufe | 60–84 % | Kräfte konzentrieren sich, lokale Fehden ruhen |
| Maximale Alarmstufe | 85–100 % | Bündnisse mit anderen Fraktionen möglich |

**Unter 20 %** sinkt die Bedrohung deutlich langsamer als die Tabelle nahelegt – die Fraktion vergisst nicht ganz.

---

## Pantheon-System

Jede Region hat ein **Pantheon** – eine Gruppe übernatürlicher Wesen (Götter, Geister, Naturkräfte), die an bestimmten Ley-Knoten gebunden sind. Der Lich muss diese Wesen besiegen, um die Region zu kontrollieren.

### Grundregeln

- **Alle Pantheon-Mitglieder müssen besiegt werden** – Gegner kapitulieren nicht, kämpfen bis zur Vernichtung
- Sieg über einzelne Bosse gibt **Forschungsfortschritt** für die Region (kollektiver Wissensgewinn, kein individuelles Recycling)
- Pantheon-Größe variiert nach Schwierigkeit: Heide klein (3 Mitglieder), Brocken als Finale groß (7+ Hexenmeisterinnen)

### Heide-Pantheon (Region 1)

Drei Mitglieder, passend zum Patchwork der Heide: Sie sind lose verbündet, aber keine Einheit. Zwei Randmitglieder sitzen vorgelagert, die Heidekönigin am Ley-Knoten.

| Mitglied | Ort | Fraktion | Rolle | Kampfplatz |
|-|-|-|-|-|
| **Der Wode** | Offene Heide zwischen Soltau und Walsrode | HeathSpirits | Melee (beritten), Size 3 | Lange offene Heidefläche ~14x8, kaum Deckung. **Kampf beginnt immer nachts** (die Wilde Jagd reitet nur bei Nacht) |
| **Hügelgrab-Zwergenkönig** | Hügelgräberfeld bei Soltau | HeathSpirits | Tank, Size 2 | Grab-Innenraum ~10x10, StoneFloor/CellarFloor, enge Gänge. **Keine Stealth-Phase** – Zwerge hören jeden Schritt |
| **Die Heidekönigin** | Wilseder Berg | Witches | Caster, Size 3 | Hügel ~12x12, Height bis 2, Steinkreis im Zentrum, Heather-Boden, 2 Hügelgräber am Rand |

#### Ley-Bund (Pantheon-Synergie)

- Die Heidekönigin erhält zu Kampfbeginn **+10 SoulShield pro lebendem Randmitglied** (max. +20).
- Fällt ein Randmitglied, wird das am Wilseder Berg sichtbar: Einer von drei Lichtsäulen über dem Steinkreis erlischt (Kampagnenkarte und Schlachtfeld).
- Lebt ein Randmitglied noch und wurde die Region verlassen, baut es nach den Regeln der Pantheon-Regeneration zerstörte Heide-Dörfer wieder auf.
- **Konsequenz:** Direkt zur Königin ist möglich (Gothic-Prinzip), aber gegen 30 statt 10 SoulShield.

#### Der Wode

- **Optik:** Hagerer Reiter auf einem schwarzen, zu großen Pferd, Schlapphut, Mantel weht immer gegen den Wind. Speer als höchster Punkt. Leuchten: fahles Mondweiß in Augen und Pferdenüstern. Begleitet von Nebel am Boden.
- **Rolle im Kampf:** Schnell, beschwört Hunde, durchbricht Linien. Lehrt den Spieler, Engstellen und Formationen zu nutzen.
- **Fähigkeiten:** Wilde Jagd (2 Schwarze Hunde beschwören), Durchreiten (Linienangriff), Jagdhorn (Verbündete beschleunigt).
- **Belohnung:** Wissen „Wilde Jagd" → Einheit **Totenjäger** (untoter Reiter, Scout/Melee) produzierbar. Ahnen-Grab freigelegt: ein bronzezeitlicher Reiterfürst.

#### Hügelgrab-Zwergenkönig

- **Optik:** Klein, breit, Bart bis zum Boden mit eingeflochtenen Bronzeringen, Steinhammer, Krone aus Grabbeigaben. Leuchten: glimmende Bernstein-Runen auf dem Hammer. Steht auf einem Schatzhaufen-Sockel.
- **Rolle im Kampf:** Schwer zu knacken, bestraft Angreifer. Lehrt Schadenstypen (Blunt gegen Heavy wirkt, Pierce kaum).
- **Fähigkeiten:** Runenschmiede (Verbündeten schützen), Schatzfluch (Angreifer verflucht), Steinhaut (auf Steinboden zusätzlicher Schutz).
- **Belohnung:** Wissen „Zwergenschmiede" → Gebäude **Knochenschmiede** (Todesritter dauerhaft +2 SoulShield). Fund: 1 heidnisches Artefakt.
- **Thematischer Reiz:** Der Zwergenkönig bewacht Gräber – genau das, was der Lich plündern will. Er ist der natürliche Gegenspieler des Phylakteriums.

#### Die Heidekönigin

- **Optik:** Hochgewachsen, Kleid aus Heidekraut und Moos, Krone aus Dornenzweigen und Birkenrinde. Stab mit lebender Heideblüte. Leuchten: Mondviolett. Um sie herum blüht der Boden, wo sie steht (Decal).
- **Rolle im Kampf:** Heilt ihre Getreuen, verwandelt Gelände in Dornen. Endkampf der Region, mehrphasig:
  - **Phase 1 (100–50 % HP):** Kämpft vom Steinkreis aus, ruft Irrlichter und Moorgeister als Wachen.
  - **Phase 2 (< 50 % HP):** Steinkreis zerbricht, Dornenkrone wird auf das ganze Feld gesprochen, Tageszeit springt auf Abend.
- **Fähigkeiten:** Ley-Bund (passiv), Heideblüte (Flächenheilung), Dornenkrone (Dornen-Gelände).
- **Belohnung:** Region assimiliert, Ley-Knoten Wilseder Berg aktiv (nach Portalbau). Gebäude **Heidealtar** (eigene Untote heilen auf Heather-Feldern 2 HP/Runde). Pantheon-Stufe Mythologie-Wissen der Heide komplett.

### Assimilation und Portale

Nach dem letzten Pantheon-Mitglied beginnt die **Assimilation-Phase**:
- Lich baut **Portal** auf (kostet Zeit und Ressourcen)
- Erst nach fertigem Portal: Ley-Knoten nutzbar
- Nutzen: **Teleport-Netz** (Lich kann zwischen assimilierten Knoten springen) und **passiver Ressourcenfluss** aus der ehemaligen Hauptbasis

### Pantheon-Fall = Fraktions-Schwächung

Wenn das gesamte Pantheon einer Fraktion fällt:
- Alle anderen Knoten derselben Fraktion werden geschwächt
- Innerhalb weniger Runden bauen diese Knoten ab – sie kämpfen weiter, aber auf reduziertem Niveau
- Macht den finalen Assault auf eine Region realistischer: erst Pantheon zerstören, dann aufgeweichte Knoten abräumen

### Fraktions-Verhalten

- **Alle Fraktionen sind defensiv** – verteidigen ihre Knoten, greifen nicht aktiv an
- Spieler bestimmt immer das Tempo
- Vereinfacht KI-Komplexität erheblich, ist aber für Phase 7+ als Erweiterung möglich

---

## Knotentypen mit klarem Profil

Die drei Knotentypen haben unterschiedliche Belohnungsprofile, was eine natürliche Reihenfolge-Strategie erzeugt:

| Knotentyp | Ressourcen | Forschung | Besondere Funktion |
|-|-|-|-|
| Mythisch | wenig | viel | Pantheon, mythologisches Wissen |
| Weltlich | viel | wenig | – |
| Christlich | wenig | keine | Verhüllen Späher-Sicht |

### Strategische Konsequenz

Daraus entsteht eine organische **Drei-Akt-Struktur** ohne explizite Vorgabe:

1. **Frühphase:** Mythische Knoten zuerst → Forschung pumpen → bessere Untote, neue Schadenstypen, regionale Boni
2. **Mittelphase:** Mit der erforschten Stärke weltliche Knoten überrennen → Ressourcen-Berg
3. **Spätphase:** Mit Ressourcen die Hauptbasis ausbauen, finale Großoffensive

Christliche Knoten werden bei Bedarf zwischen den anderen genommen – sie geben nichts, aber blockieren die Späher-Sicht (siehe Kloster-Mechanik).

---

## Gebietseffekte als eigenes System

Statt prozentualer Mali auf Werte – konkrete Effekte mit klarer Wirkung:

### Effekt-Typen

- **Schaden pro Runde** (heiliger Boden lässt Untote langsam zerfallen)
- **Heilung pro Runde** (Friedhöfe, verfaulter Boden regenerieren Untote)
- **Sichtweiten-Modifikatoren** (Nebel, Dunkelheit reduzieren, Höhe erhöht)
- **Bewegungsmodifikatoren** (Schlamm verlangsamt, Pfade beschleunigen)

### Beispiele für Gebietseffekt-Quellen

- **Wind** – hat Richtung, beeinflusst Geruchs-basierte Stealth-Mechanik
- **Nebel** – häufig morgens, reduziert Sichtweiten
- **Schlammboden** – verlangsamt Bewegung, besonders schwere Einheiten
- **Heilige/geweihte Erde** – Schaden für Untote pro Runde (rund um Klöster, Kirchen)
- **Friedhöfe / alte Schlachtfelder** – Heilung für Untote pro Runde

**Visuell an der Einheit:** Steht eine Einheit auf einem Effekt-Feld, zeigt ihr Sockel einen kleinen Effekt-Pip (Gold = heiliger Schaden, Grün = Heilung, Grau = verlangsamt). So ist sichtbar, *wen* das Feld betrifft, nicht nur *wo* es liegt.

### Höhenunterschiede

- **Tiefebene:** maximal 1 Stufe Unterschied von Feld zu Feld (Ausnahme: Befestigungswälle)
- **Harz und andere Mittelgebirge:** echte Höhenunterschiede möglich
- Höhe ist seltener, dadurch besonderer taktischer Faktor – wo es Höhe gibt, hat sie Bedeutung

---

## Tageszeit-System

### Vier Tageszeiten

- **0 Uhr (Nacht)**, **6 Uhr (Morgen)**, **12 Uhr (Tag)**, **18 Uhr (Abend)**
- Beeinflusst Sichtweiten und bestimmte Einheitentypen
- Untote nachts stärker (oder zumindest weniger geschwächt)
- Lebende-Einheiten tagsüber stärker
- Morgens oft Nebel als zusätzlicher Effekt

**Lesbarkeit bei Nacht:** Szene wird dunkler, Einheiten nicht. Fraktions-Leuchtfarbe (Emissive) und Sockel bleiben bei jeder Tageszeit gleich hell, damit Taktik nie an schlechter Sicht des *Spielers* scheitert – nur an schlechter Sicht der *Einheiten*.

### Zeitfortschritt im Kampf

- **Tageszeit ändert sich alle 3 Runden um 6 Stunden** (Hybrid-Variante)
- Eine kleine Schlacht (5 Runden ≈ 30 Stunden) erlebt einen Tag/Nacht-Wechsel
- Eine Belagerung (15+ Runden) kann mehrere Zyklen erleben
- Genaue Rundendauer wird später festgelegt

### Strategische Tiefe in Belagerungen

- Verteidiger sind tagsüber stärker → Lich nutzt Nächte für Hauptangriffe
- Untote werden tagsüber konservativer eingesetzt, nachts offensiv
- Belagerung könnte sich gezielt darauf konzentrieren, "die nächste Nacht zu erleben"

---

## Variable Schlachtfeldgrößen

Das ursprüngliche 8x8 war nur ein Prototyp-Wert. Das endgültige System ist flexibel.

### Größenstaffelung nach Knotentyp

| Knotentyp | Schlachtfeld | Kampfdauer |
|-|-|-|
| Standard-Dorf | klein (~8x8) | 5 Runden, ~30h |
| Befestigtes Kloster | mittel (~12x12) | 8–10 Runden, ~2 Tage |
| Hansestadt / Belagerung | groß (~16x16) | 15+ Runden, mehrere Tage |
| Pantheon-Bosskampf | mittel-groß | variabel |

### Konsequenz für die Schnittstelle

Die Schnittstelle Kampagne → Kampf wird um zwei Werte erweitert:
- **Schlachtfeld-Größe** (klein/mittel/groß)
- **Zeitskala** (Stunden pro Runde – kann je nach Knotentyp variieren)

---

## Schlachtfeld-Bausteine

Schlachtfelder sind nicht starr nxn, sondern **Container mit beliebiger Form** (Rechteck, L-förmig, mit Lücken). Sie werden aus **vorgefertigten Bausteinen** komponiert: Häuser, Türme, Mauern, Kultstätten.

### Prinzip

- Ein Baustein wird einmal designt, dann beliebig oft platziert
- Karten = Listen von Platzierungen ("Bauernhaus an Position X, Kapelle an Position Y")
- Editor-fähig: später leicht erweiterbar
- Konsistent: eine Kapelle in der Heide sieht aus wie eine Kapelle im Spreewald

### Hex-Bausteine technisch

Bausteine bestehen aus mehreren verbundenen Hexes. **Wände sind Kanten-Eigenschaften** (passt zur früheren Wand-Mechanik). Ein Haus = Gruppe von Hexes mit Wand-Kanten ringsum, mit einer Lücke als Tür.

### Implementierungs-Hinweis

Architektur ab Phase 1 vorbereiten – Tile-Eigenschaften nicht hartcoden, sondern als Werte ablegen, die Bausteine setzen können. Tatsächliche Implementierung der Bausteine erst Phase 3 (Kampfsystem-Tiefe).

**Abgrenzung zu Einheiten:** Gebäude und Deko bleiben farblich entsättigt (Erd-, Holz-, Steintöne). Gesättigte Farben und Leuchten sind **für Einheiten reserviert** – sonst konkurriert eine rote Hanse-Markise mit einem roten Hanse-Soldaten.

### Baustein-Katalog

Größen sind erste Vorschläge und werden beim Bauen verfeinert (Hex-Grids zählen Felder anders als Quadrate).

**Belegung pro Baustein:** Hex-Felder zählen als belegt, wenn sie zu **50% oder mehr** vom Baustein-Rechteck überdeckt sind. Felder mit weniger als 50% Überdeckung bleiben begehbar.

**Orientierung:** Hex-Grids haben keine echte 90°-Symmetrie. Daher gibt es **pro Baustein zwei feste Varianten** (gerade und gedreht), nicht eine drehbare Form. Verdoppelt den Asset-Aufwand, vermeidet aber Balancing-Chaos und Form-Inkonsistenzen.

**Stütz-Elemente / Deko in Halbbereichen:** Hex-Felder, die zu weniger als 50% überdeckt sind und damit begehbar bleiben, werden mit **Dekorations-Elementen** belegt – Brunnen, Mistgabeln, Karren, Heiligenstatuen etc. Diese Deko-Elemente klären visuell, welcher Bereich zum Gebäude gehört, ohne die Hex-Begehbarkeit zu blockieren. Atmosphärisch wertvoll: macht aus sterilen Rechtecken lebendige Orte.

Pro Gebäude-Variante (gerade/gedreht) wird eine **Auswahl aus dem Deko-Pool** verwendet, sodass beide Varianten visuell unterscheidbar sind. 1x1-Bausteine brauchen keine Deko.

#### Neutrale Bausteine (alle Fraktionen)

- **Bauernhaus** 2x3 – Standard-Wohngebäude, Holzwände
  - *Deko-Pool:* Mistgabel im Boden, Holzscheit-Stapel, Hühnerstall, Wassertrog, Karren, Pflug, Wäscheleine, Sense an der Wand, Strohballen, Hund an Kette, Schwein im Pferch, Beil im Hackklotz
- **Turm groß** 2x2 – Wachturm, Sichtbonus oben, Bogenschützen-Plattform
  - *Deko-Pool:* Sandsäcke am Fuß, eiserne Lanzen-Halterung, Pechfass, Pferdetränke, Wachfeuer in Schale, Bogenschützen-Köcher, Ersatz-Schilde gestapelt
- **Turm klein** 1x1 – einfacher Beobachtungsposten
- **Brücke** 1x4 – verbindet über Flüsse, Engpass
  - *Deko-Pool:* Steinpoller, Geländer-Pfosten, Kistenstapel, Fischerkorb, Zollschranke, Laternen-Pfahl
- **Wegkreuz** 1x1 – einzelnes Element, Marker

#### Hansestädte (weltlich, Handel)

- **Kontorhaus** 3x3 – großes Lagerhaus mit Innenhof, viele Eingänge
  - *Deko-Pool:* Lade-Rampe mit Kisten, Waagen, Tonnen-Stapel, Garbenballen, Geldwaage, Kontorbuch auf Pult, Tintenfass, Schreibtisch im Hof, Karren mit Tuchballen
- **Stadttor** 1x4 – schmaler Durchgang in Mauer, sehr verteidigbar
  - *Deko-Pool:* Eiserne Stachelroste, Pechpfanne, Wappenschild, Wachposten-Hocker, Fackelhalter, Glocken-Strang, Steinhaufen für Verteidigung
- **Hafenkran** 2x2 – am Wasserrand mit Anlegestelle, freie Sichtlinie
  - *Deko-Pool:* Aufgewickelte Taue, Anker am Boden, Fischfass, Netze zum Trocknen, Pollerkette, Holzplanken-Stapel

#### Welfen-Adel / Burgen (weltlich, Macht)

- **Bergfried** 3x3 – zentraler Burgturm, dicke Mauern, hohe Stufe
  - *Deko-Pool:* Banner-Stange, Wappen über Tür, eiserne Lanzen-Halterung, Trainings-Holzpuppe, Schmiede-Amboss, Pferdeställe, Brunnen, Übungs-Strohziele, Helm auf Stange
- **Ringmauer** 1x6 (linear, biegbar) – Festungsmauer mit Wehrgang oben
  - *Deko-Pool:* Wehrgang-Treppe, Pechpfanne, Wachposten-Schild, Bogenschützen-Köcher, Brennholzhaufen, Glockenstrang, Steinmunition-Stapel
- **Burgkapelle** 2x2 – kleine Andachtsstätte im Burghof, leicht geweiht
  - *Deko-Pool:* Steinkreuz, Kerzenständer, Grabplatte im Boden, Weihwasserbecken, Heiligenstatue in Nische, kleines Beet mit Heilkräutern

#### Heideklöster (christlich, Heide-typisch)

- **Klosterhof** 3x4 – zentraler Kreuzgang, geweihter Boden
  - *Deko-Pool:* Brunnen mit Eimer, Kräuterbeet, Heiligen-Statue, Bank, Schreibpult unter Vordach, Bibel-Pult, Wäscheleine mit Kutten, Kompostgrube, Bienenstöcke, Friedhofs-Kreuze, Glockenstrang, Steinkreuz im Hof
- **Schwesternzelle** 2x2 – einfaches Wohngebäude, Holzwände
  - *Deko-Pool:* Holzbank, Bibel auf Pult, einfaches Holzkreuz, Steinkrug, kleine Beet-Einfassung, Birkenbesen, Wassereimer
- **Bibliothek** 2x3 – Wissensspeicher (Forschungs-Bonus beim Plündern), stark geweiht
  - *Deko-Pool:* Schreibpult, Tintenfass, gestapelte Buchrollen, Lesepult mit Buch, Steinbank, Pergamentrollen-Korb, Fenster-Glasmalerei am Boden (Splitter), brennende Kerze in Halter

#### Bistümer / Erzbistümer (christlich, mächtiger)

- **Kathedrale** 4x4 – riesiges Kirchengebäude, stark geweihter Boden, mehrere Eingänge
  - *Deko-Pool:* Steinkreuz, Banner mit Heiligenbild, Reliquienschrein klein, Weihwasserbecken, Kerzenständer hoch, Grabplatten im Boden, Weihrauchfass, Heiligenstatuen-Nische, Glasfenster-Spuren, Klingel-Strang, Beichtstuhl-Sitz draußen
- **Bischofspalast** 3x3 – weltliche Macht des Klerus, Hof, Wachen
  - *Deko-Pool:* Eiserner Zaun, Wappen mit Bischofsstab, Banner, Kelchgefäß auf Sockel, Hund am Eingang, Heiligenstatue, Bank, Brunnen, schmiedeeiserne Laterne
- **Reliquienschrein** 1x1 – kleines aber besonders heiliges Objekt, starker Effekt im Umkreis

#### Hexenkulte / Druidenhaine (mythisch)

- **Steinkreis** 3x3 – ringförmig angeordnete Megalithen, ritueller Mittelpunkt, zentrales Hex frei
  - *Deko-Pool:* Verwitterte Runensteine, Schädelhaufen, alte Knochen, Aschehaufen, Opferschale, getrocknete Kräuter-Bündel, Tier-Schädel an Pfahl, blutige Steinplatten, Mondsichel-Symbol im Boden geritzt
- **Druidenhütte** 2x2 – versteckte Behausung, im Wald getarnt
  - *Deko-Pool:* Hängende Kräuter-Bündel, Mörser am Boden, Tonkrüge, Schädelreihen, Holzschalen, Räucherwerk-Bündel, Blutspuren, Knochenfetisch an Stange
- **Opferaltar** 1x1 – zentraler Kultplatz, mythologischer Effekt

#### Mecklenburger Wodan-Kult (mythisch, organisierter)

- **Hain mit Götterbild** 3x3 – heiliger Wald mit zentraler Holzstatue
  - *Deko-Pool:* Holz-Götzen, Trommeln, Met-Krüge, Aschehaufen, geopferte Tier-Knochen, Speerhalter, Trinkhorn, Schwert im Stein, Wolfsschädel an Pfahl, Eichenkranz
- **Met-Halle** 3x4 – Versammlungsort, Festhalle mit langem Innenraum
  - *Deko-Pool:* Lange Holzbank, Met-Fässer, Trinkhörner, Lagerfeuer-Stelle, Banner mit Runen, Hirschgeweih-Trophäe, Schwerter an Wand, Schildwand-Stapel, Holzhauklotz, Wolfsfell
- **Runenstein** 1x1 – einzelner Megalith, Magie-Verstärker

#### Mythische Heide (Hügelgräber, niedere Mythologie)

- **Hügelgrab** 2x2 – kreisrunder Erdhügel, untoter Friedhof, Heilung für Lich-Einheiten
  - *Deko-Pool:* Verwitterte Knochen, Grabbeigaben (Gefäße), Steinplatten verschoben, Eingangsstein, Erd-Verfärbung, kleine Knochenhaufen, alte Speerspitzen rostig, Aschegrube
- **Moor-Insel** 3x3 (unregelmäßig) – feste Stelle im Sumpf, schwer erreichbar
  - *Deko-Pool:* Schilfbüschel, halb-versunkenes Boot, Pfähle im Wasser, Nebelschwaden im Boden, treibende Holzbohlen, Moor-Tümpel, Knochen halb-versunken
- **Heiliger Born** 1x1 – Quellfassung, mythologischer Ort

#### Spreewald (mythisch, slawisch, Wasser)

- **Stelzenhaus** 2x2 – auf Pfählen über Wasser, Bewegung drumherum besonders
  - *Deko-Pool:* Reusen-Korb, Fischernetze, Boot vertäut, Ruder, Fischfass, Schilfbündel, getrocknete Fische auf Schnur, hölzerner Steg
- **Schilfdickicht** 3x3 (unregelmäßig) – Sicht-Blockade, langsame Bewegung
  - *Deko-Pool:* Schilf-Büschel, Tümpel-Wasser, Gnadenbild im Schilf, Pfähle, Treibgut-Holz, halb-versunkene Steine
- **Schlangenkönig-Höhle** 2x3 – versteckter Eingang in Erdhügel
  - *Deko-Pool:* Schlangen-Häute, Geweih-Stange, Eingangs-Steine, Knochenhaufen, geritzte Runen-Steine, alte Münzen verstreut

### Spezielle Einzelobjekte (1x1-Bausteine)

- **Wegkreuz / Bildstock** – kleine christliche Markierung
- **Galgen** – Hinrichtungsstätte (psychologischer Effekt)
- **Brunnen** – zentraler Dorfpunkt
- **Heilige Eiche** – einzelner Baum mit Bedeutung

### Komposition zu Schlachtfeldern

Beispiele für komplexere Karten aus Bausteinen:

- **Christliche Stadt:** 3x Stadthaus + 1x Kapelle + Wegnetz + Mauerring drumherum
- **Hexen-Klause:** 1x Druidenhütte + Steinkreis + Schilfdickicht-Cluster
- **Heidekloster:** Klosterhof + 2x Schwesternzelle + Bibliothek + Friedhof

Pantheon-Bosskämpfe können einzigartige Wahrzeichen-Bausteine bekommen (z.B. Hexenkanzel auf dem Brocken).

---

## Blender Asset-Liste

Diese Liste ist redundant zum Bausteinkatalog, aber **nach Asset-Kategorien sortiert** für die praktische Modellierungs-Arbeit. Reihenfolge nach Priorität: erstmal Standard-Sets bauen, dann fraktionsspezifisch.

### Priorität 1: Hex-Grundlagen (Phase 1)

Diese sind die Mindestmenge für ein spielbares Schlachtfeld:

- **Hex-Tile gerade Erde** – Standard-Boden, etwas struktur
- **Hex-Tile Wiese** – grasiger Boden, leichte Variation
- **Hex-Tile Schlamm** – Bewegungsmodifikator
- **Hex-Tile Wasser** – flach, transparent
- **Hex-Tile Stein/Pflaster** – feste Wege
- **Hex-Tile Wald** (mit eingebetteten Bäumen) – Sichtblockade
- **Wand-Element** (für Hex-Kanten) – generisch, austauschbar mit Material
- **Hex-Sockel für Einheiten** – flacher Ring, zwei Randformen (Freund glatt, Feind gezackt), Material per Fraktionsfarbe (siehe Einheiten-Visualisierung)

### Priorität 2: Spielfiguren-Platzhalter (Phase 1-2)

**Vorgehen:** Erst lesbarer Platzhalter (Rollen-Silhouette aus Grundkörpern + Fraktionsfarbe + Rollen-Icon), dann Modell nach [Steckbrief](#einheiten-steckbriefe-erste-10-modelle).

- **Lich-Modell** – zentrale Spielfigur
- **Skelett** – Standard-Untot, mass-produziert
- **Ghul** – mittelschwerer Untot
- **Todesritter** – schwerer Untot
- **Geist** – spektraler Untot (Shader-Test für Spektral-Look)
- **Balliste** – Belagerung (Test für Machine-Silhouette)
- **Mensch generisch** (Bauer/Soldat) – Standard-Gegner
- **Bischof / Kleriker** – christliche Einheit
- **Hexe** – mythische Einheit
- **Druide** – mythische Einheit

### Priorität 3: Neutrale Gebäude

Die werden auf jedem Schlachtfeld vorkommen – am häufigsten gebrauchte Assets.

- **Bauernhaus 2x3** – gerade Variante + 90°-gedrehte Variante
- **Turm groß 2x2** – gerade + gedreht
- **Turm klein 1x1** – nur eine Variante
- **Brücke 1x4** – gerade + gedreht
- **Wegkreuz 1x1** – nur eine Variante

### Priorität 4: Heideklöster (für erste Region)

Die Heide ist Startgebiet, also als nächstes priorisieren.

- **Klosterhof 3x4** – gerade + gedreht
- **Schwesternzelle 2x2** – gerade + gedreht
- **Bibliothek 2x3** – gerade + gedreht

### Priorität 5: Mythische Heide (für erste Region)

- **Hügelgrab 2x2** – gerade + gedreht
- **Moor-Insel 3x3** – nur eine Variante (unregelmäßige Form)
- **Heiliger Born 1x1** – nur eine Variante

### Priorität 6: Hansestädte (für erste Region: Lüneburg)

- **Kontorhaus 3x3** – gerade + gedreht
- **Stadttor 1x4** – gerade + gedreht
- **Hafenkran 2x2** – gerade + gedreht

### Priorität 7: Hexenkulte / Druidenhaine (für erste Region)

- **Steinkreis 3x3** – nur eine Variante (rotationssymmetrisch)
- **Druidenhütte 2x2** – gerade + gedreht
- **Opferaltar 1x1** – nur eine Variante

### Priorität 8: Welfen-Adel / Burgen (Lüneburger Welfenburg)

- **Bergfried 3x3** – gerade + gedreht
- **Ringmauer 1x6** – gerade + gedreht (eventuell mehrere Biegungen als separate Bausteine)
- **Burgkapelle 2x2** – gerade + gedreht

### Priorität 9: Bistümer / Erzbistümer (für spätere Regionen)

- **Kathedrale 4x4** – gerade + gedreht
- **Bischofspalast 3x3** – gerade + gedreht
- **Reliquienschrein 1x1** – nur eine Variante

### Priorität 10: Mecklenburger Wodan-Kult (für spätere Regionen)

- **Hain mit Götterbild 3x3** – nur eine Variante
- **Met-Halle 3x4** – gerade + gedreht
- **Runenstein 1x1** – nur eine Variante

### Priorität 11: Spreewald (für spätere Regionen)

- **Stelzenhaus 2x2** – gerade + gedreht
- **Schilfdickicht 3x3** – nur eine Variante (unregelmäßig)
- **Schlangenkönig-Höhle 2x3** – gerade + gedreht

### Priorität 12: Spezielle Einzelobjekte (verteilt einsetzbar)

- **Galgen 1x1**
- **Brunnen 1x1**
- **Heilige Eiche 1x1**

### Deko-Objekte (Sets pro Fraktion)

Diese werden als Set gebaut und später in den Halbbereichen der Gebäude platziert. Reihenfolge nach Fraktion-Priorität.

#### Bauernhof-Set (neutral, höchste Priorität)
- Mistgabel
- Holzscheit-Stapel
- Hühnerstall
- Wassertrog
- Karren
- Pflug
- Wäscheleine mit Tüchern
- Sense
- Strohballen
- Hund (statisch)
- Schwein im Pferch
- Hackklotz mit Beil

#### Turm/Wachposten-Set (neutral)
- Sandsäcke
- Pechfass
- Wachfeuer in Schale
- Bogenschützen-Köcher
- Schild-Stapel
- Lanzen-Halterung

#### Brücken-Set (neutral)
- Steinpoller
- Geländer-Pfosten
- Kistenstapel
- Fischerkorb
- Zollschranke
- Laternen-Pfahl

#### Hanse-Handels-Set
- Kistenstapel
- Tonnen-Stapel
- Garbenballen
- Waagen
- Tuchballen
- Schreibpult
- Tintenfass
- Aufgewickelte Taue
- Fischfass
- Netze
- Anker

#### Burg-Set
- Banner-Stange mit Welfenwappen
- Trainings-Holzpuppe
- Schmiede-Amboss
- Übungs-Strohziele
- Helm auf Stange
- Pechpfanne
- Glockenstrang

#### Heidekloster-Set
- Heiligen-Statue (Maria)
- Steinkreuz
- Brunnen mit Eimer
- Kräuterbeet
- Bibel-Pult
- Kerzenhalter
- Wäscheleine mit Kutten
- Bienenstöcke
- Kompostgrube
- Friedhofs-Kreuze
- Schreibpult
- Lesepult mit Buch
- Pergamentrollen-Korb

#### Bistum/Kathedrale-Set
- Großes Steinkreuz
- Banner mit Heiligenbild
- Reliquienschrein klein
- Weihwasserbecken
- Kerzenständer hoch
- Grabplatten
- Weihrauchfass
- Heiligenstatuen-Nische
- Kelchgefäß auf Sockel
- Beichtstuhl

#### Hexenkult/Druiden-Set
- Verwitterte Runensteine
- Schädelhaufen
- Tier-Schädel an Pfahl
- Aschehaufen
- Opferschale
- Hängende Kräuter-Bündel
- Mörser
- Tonkrüge
- Knochenfetisch
- Räucherwerk-Bündel
- Mondsichel-Symbol (geritzt)

#### Wodan-Kult-Set
- Holz-Götzen
- Trommeln
- Met-Krüge / Met-Fässer
- Trinkhörner
- Tier-Knochen
- Speerhalter
- Schwert im Stein
- Wolfsschädel an Pfahl
- Eichenkranz
- Hirschgeweih-Trophäe
- Wolfsfell

#### Hügelgrab-Set
- Verwitterte Knochen
- Grabbeigaben (Tongefäße)
- Steinplatten verschoben
- Eingangsstein
- Alte Speerspitzen rostig
- Aschegrube

#### Spreewald/Wasser-Set
- Reusen-Korb
- Fischernetze
- Boot vertäut
- Ruder
- Schilfbündel
- Getrocknete Fische auf Schnur
- Hölzerner Steg
- Halb-versunkene Pfähle
- Treibgut-Holz

#### Leichen-Set (neu, für Leichen-Qualität)
- Leiche intakt (Basis-Pose, liegend)
- Leiche zerschmettert (Variante mit Verformung)
- Leiche zerrissen (Teile verstreut)
- Leiche verkohlt (dunkles Material, Glut-Partikel)
- Leiche verdorben (grünliche Verfärbung)
- Seelen-Funke (schwebende Partikel über Leiche, für Seelenschaden)

### Schätzung Gesamt-Asset-Menge

- **Hex-Tiles:** ~7 Varianten (+ 1 Einheiten-Sockel)
- **Spielfiguren:** ~10 Modelle (erstmal Platzhalter, später detaillierter)
- **Gebäude (mit beiden Orientierungen):** ~35 einzelne Modelle
- **Deko-Objekte:** ~80 Einzelteile
- **Leichen-Varianten:** 5 + 1 Partikeleffekt

**Gesamt für vollständige erste Region (Heide):** ca. 65-75 Modelle. Davon sind viele klein und einfach (Deko-Objekte), nur ~15 sind aufwändigere Hauptassets (Gebäude).

**Tipp:** Erstmal mit grauen Würfel-Platzhaltern bauen, alles funktional zum Laufen bringen, dann iterativ durch Blender-Modelle ersetzen. **Ausnahme Einheiten:** Hier nie graue Würfel, sondern von Anfang an lesbare Platzhalter (siehe Einheiten-Visualisierung) – sonst lässt sich die Taktik im Prototyp nicht beurteilen.

---

## Hintergrund / Lore

- Der Lich ist ein uralter untoter Overlord – die konkrete Vorgeschichte ist offen, aber nicht zwingend Rache-getrieben
- **Motivation: Hass auf das Leben selbst.** Keine Tragödie nötig, keine nachvollziehbare Motivation. Pure Bosheit.
  - Rechtfertigt unbegrenzte Expansion über mehrere Kampagnen/Regionen
  - Vermeidet moralische Ambiguität – der Spieler *ist* das Böse
- Phylakterium im Hügelgrab (Lüneburger Heide) – Erwachen aus langem Schlaf
- **Möglicher Erzfeind:** Die Kirche / christliche Ordnung als zivilisatorische Gegenkraft

## Einheiten-Rang-System

Abgestimmt mit `UnitRank` (siehe Datenstruktur):

| Rang | Beispiele | Bedeutung |
|-|-|-|
| `CannonFodder` | Skelette, Ghule, Zombies | Mass-produzierbar, Verlust tut nicht weh |
| `Warrior` | Geist, Todesritter-Krieger | Selten, teurer, wertvoller |
| `Machine` | Balliste, Katapult | Belagerung, nicht organisch |
| `Commander` | Todesritter-Anführer, Nekromant, Geisterfürst | Erweitert Kommando-Limit, generisch produzierbar |
| `Unique` | Ahnen aus Gräbern (Brunhild, Theobald der Stumme) | Benannt, unersetzbar, kehren evtl. zurück |

---

## Einheiten-Datenstruktur

### Enums

*(Pseudo-Code.)*

**UnitRank:**
```
enum UnitRank { CannonFodder, Warrior, Machine, Commander, Unique }
```
Machine = Belagerungswaffen, nicht organisch – kein Gift, keine Seele.
Commander = generischer Anführer (erweitert Kommando-Limit). Unique = benannter Ahne.

**UnitRole** (neu – steuert Silhouette, Rollen-Icon und KI-Grundverhalten):
```
enum UnitRole { Melee, Tank, Ranged, Caster, Support, Siege, Scout, Commander }
```
Rolle ist **unabhängig vom Rang**: Ein Ghul ist `CannonFodder` + `Melee`, eine Hexe `Warrior` + `Caster`.

**PowerType** (Angriffs-/Kraftarten, inkl. Heal):
```
enum PowerType { Pierce, Blunt, Rend, Siege, Fire, Poison, Arcane, Soul, Holy, Chaos, Heal }
```
*(Ein früher separater DamageType wurde gestrichen – war redundant zu PowerType.)*
*`Rend` (neu) = Zerfleischen durch Biss/Klaue. Schließt die Lücke zur Leichen-Tabelle.*

**DefenseType:**
```
enum DefenseType {
    Unarmored,
    Light,      // Leder, einfache Kleidung
    Medium,     // Kettenhemd
    Heavy,      // Platte
    Fortified,  // Gebäude, Mauern, Maschinen
    Divine      // göttliche Wesen, Pantheon-Mitglieder
}
```

### Power-Defense-Matrix

Prozentwert = wie viel des Schadens tatsächlich ankommt.

| Angriff \ Rüstung | Unarmored | Light | Medium | Heavy | Fortified | Divine |
|-|-|-|-|-|-|-|
| Pierce | 100% | 100% | 100% | 75% | 50% | 50% |
| Blunt | 100% | 100% | 75% | 100% | 75% | 50% |
| Rend | 125% | 100% | 75% | 50% | 25% | 50% |
| Siege | 100% | 75% | 75% | 100% | 150% | 50% |
| Fire | 100% | 125% | 100% | 75% | 50% | 75% |
| Poison | 100% | 100% | 100% | 75% | 0% | 50% |
| Arcane | 100% | 100% | 100% | 100% | 75% | 75% |
| Soul | 150% | 125% | 100% | 75% | 25% | 50% |
| Holy | 150% | 125% | 100% | 75% | 50% | 100% |
| Chaos | 100% | 100% | 100% | 100% | 100% | 100% |

- **über 100%** = Schwäche
- **unter 100%** = Resistenz
- **0%** = Immunität
- **Chaos** = immer 100%, universell aber nie optimal
- **Rend** = stark gegen Ungerüstete, fällt gegen Rüstung schnell ab (Zähne gegen Platte)
- **Soul gegen Fortified 25 %** = Maschinen und Mauern haben keine Seele, aber ihre Bedienmannschaft (vorher 0 %, Geister waren gegen Ballisten nutzlos)

### Basis-Klasse S_UnitData

**Identität:**
- `UnitName` – String
- `Rank` – E_UnitRank
- `Role` – E_UnitRole *(neu)*
- `Faction` – E_Faction *(neu – bisher nur implizit)*
- `DescriptionText` – String
- *Visuals: Zeile mit gleichem Row-Name in `DT_UnitVisuals` – kein Referenzfeld nötig (siehe Einheiten-Visualisierung)*

**Kampf-Stats:**
- `HP` – Integer
- `MaxEnergy` – Integer *(neu – wurde zur Laufzeit schon gelesen)*
- `Initiative` – Integer (1–10)
- `MoveRange` – Integer
- `AttackDamage` – Integer
- `AttackRange` – Integer (1 = Nahkampf, >1 = Fernkampf)
- `PowerType` – E_PowerType
- `AttacksPerTurn` – Integer
- `CanCounter` – Boolean

**Schutz:**
- `DefenseType` – E_DefenseType
- `MagicResist` – Integer (0–10). Reduziert **magischen** Schaden (Arcane, Soul, Holy, Chaos) um 5 % pro Punkt, max. 50 %
- `SoulShield` – Integer. Schild-Pool, der **jeden** Schaden zuerst absorbiert; regeneriert nicht im Kampf

**Sinne (was die Einheit wahrnimmt):**
- `SightRange` – Integer (Hex-Felder)
- `HearRadius` – Integer
- `SmellRadius` – Integer

**Signatur (was die Einheit abgibt – für Stealth):** *(neu)*
- `NoiseLevel` – Integer (0–4, Geräusch bei Bewegung)
- `ScentLevel` – Integer (0–4, untoter Gestank / Lebensgeruch)

**Eigenschaften:**
- `Size` – Integer (1–4)
- `IsSpectral` – Boolean
- `IsFlying` – Boolean
- `CommandPoints` – Integer (negativ = kostet Punkte, positiv = gibt Punkte frei, netto)
- `Abilities` – Array<Name> (Row-Names aus `DT_Abilities`) *(neu)*

**Produktion:**
- `CorpsesCost` – Integer
- `BonesCost` – Integer
- `SoulsCost` – Integer

*Visuals & Animationen liegen nicht mehr hier, sondern in `S_UnitVisual` (siehe nächstes Kapitel). Grund: Balancing-Tabelle bleibt frei von Asset-Referenzen; Visuals können ohne Neustart der Werte getauscht werden.*

### Beispiel-Einheiten

#### Ghul
| Stat | Wert |
|-|-|
| Rank | CannonFodder |
| Role | Melee |
| Faction | Undead |
| HP | 18 |
| Initiative | 5 |
| MoveRange | 3 |
| AttackDamage | 6 |
| AttackRange | 1 |
| PowerType | Rend |
| AttacksPerTurn | 1 |
| CanCounter | true |
| DefenseType | Unarmored |
| MagicResist | 1 |
| SoulShield | 0 |
| SightRange | 3 |
| HearRadius | 2 |
| SmellRadius | 4 |
| NoiseLevel | 2 |
| ScentLevel | 4 |
| Size | 2 |
| IsSpectral | false |
| IsFlying | false |
| CommandPoints | -2 |
| CorpsesCost | 1 |

#### Geist
| Stat | Wert |
|-|-|
| Rank | Warrior |
| Role | Scout |
| Faction | Undead |
| HP | 10 |
| Initiative | 8 |
| MoveRange | 5 |
| AttackDamage | 8 |
| AttackRange | 1 |
| PowerType | Soul |
| AttacksPerTurn | 1 |
| CanCounter | false |
| DefenseType | Unarmored |
| MagicResist | 4 |
| SoulShield | 6 |
| SightRange | 5 |
| HearRadius | 4 |
| SmellRadius | 0 |
| NoiseLevel | 0 |
| ScentLevel | 0 |
| Size | 1 |
| IsSpectral | true |
| IsFlying | true |
| CommandPoints | -3 |
| SoulsCost | 2 |

#### Balliste
| Stat | Wert |
|-|-|
| Rank | Machine |
| Role | Siege |
| Faction | Undead |
| HP | 25 |
| Initiative | 2 |
| MoveRange | 1 |
| AttackDamage | 20 |
| AttackRange | 6 |
| PowerType | Siege |
| AttacksPerTurn | 1 |
| CanCounter | false |
| DefenseType | Fortified |
| MagicResist | 0 |
| SoulShield | 0 |
| SightRange | 6 |
| HearRadius | 3 |
| SmellRadius | 1 |
| NoiseLevel | 4 |
| ScentLevel | 1 |
| Size | 3 |
| IsSpectral | false |
| IsFlying | false |
| CommandPoints | -5 |
| CorpsesCost | 3 |
| BonesCost | 5 |

### Gesamtübersicht aller Einheiten

*Erster Balancing-Vorschlag. Quelle der Wahrheit ist `design/data/DT_Units.csv`; diese Tabelle ist daraus generiert. Kosten: L = Leichen, K = Knochen, S = Seelen. Sinne = Sicht/Gehör/Geruch, Signatur = Geräusch/Geruch.*

<!--GEN:UNITS:BEGIN-->
| Einheit | Fraktion | Rang / Rolle | Size | HP | En | Ini | Bew | Schaden | Reichw. | Typ | Rüstung | MR / SS | Sinne | Signatur | Spektral/Flug | KP | Kosten |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Lich | Undead | Unique / Commander | 2 | 60 | 10 | 6 | 3 | 12 | 3 | Soul | Unarmored | 8 / 20 | 5/4/2 | 1/3 | – | +0 | – |
| Skelett | Undead | CannonFodder / Melee | 1 | 10 | 0 | 5 | 3 | 5 | 1 | Pierce | Light | 0 / 0 | 3/2/0 | 2/1 | – | -1 | 2K |
| Zombie | Undead | CannonFodder / Melee | 2 | 20 | 0 | 3 | 2 | 6 | 1 | Blunt | Unarmored | 0 / 0 | 2/2/3 | 2/4 | – | -1 | 1L |
| Ghul | Undead | CannonFodder / Melee | 2 | 18 | 0 | 5 | 3 | 6 | 1 | Rend | Unarmored | 1 / 0 | 3/2/4 | 2/4 | – | -2 | 1L |
| Todesritter | Undead | Warrior / Tank | 2 | 35 | 3 | 4 | 3 | 10 | 1 | Pierce | Heavy | 3 / 3 | 3/3/1 | 3/2 | – | -4 | 1L 3K 1S |
| Geist | Undead | Warrior / Scout | 1 | 10 | 0 | 8 | 5 | 8 | 1 | Soul | Unarmored | 4 / 6 | 5/4/0 | 0/0 | Spektral/Flug | -3 | 2S |
| Balliste | Undead | Machine / Siege | 3 | 25 | 0 | 2 | 1 | 20 | 6 | Siege | Fortified | 0 / 0 | 6/3/1 | 4/1 | – | -5 | 3L 5K |
| Nekromant | Undead | Commander / Caster | 2 | 18 | 8 | 5 | 3 | 6 | 4 | Soul | Light | 5 / 4 | 4/3/2 | 1/2 | – | +4 | 2L 2S |
| Fleischriese | Undead | Warrior / Tank | 4 | 70 | 3 | 2 | 2 | 14 | 1 | Blunt | Medium | 1 / 0 | 3/2/2 | 4/4 | – | -8 | 15L |
| Knochendrache | Undead | Warrior / Tank | 4 | 120 | 4 | 5 | 6 | 18 | 2 | Soul | Heavy | 4 / 4 | 6/4/3 | 4/2 | Flug | -16 | 30K 6S |
| Bronzezeitlicher Reiterfürst | Undead | Unique / Commander | 3 | 45 | 6 | 7 | 6 | 12 | 1 | Pierce | Medium | 3 / 4 | 6/4/3 | 3/2 | – | +6 | – |
| Hünenkönig | Undead | Unique / Commander | 3 | 60 | 5 | 4 | 3 | 14 | 1 | Blunt | Heavy | 4 / 4 | 4/3/2 | 4/2 | – | +6 | – |
| Widukinds Schatten | Undead | Unique / Commander | 2 | 50 | 6 | 6 | 4 | 12 | 1 | Pierce | Medium | 4 / 6 | 5/4/3 | 2/2 | – | +8 | – |
| Ratsherr von Rungholt | Undead | Unique / Commander | 2 | 35 | 8 | 5 | 3 | 9 | 3 | Soul | Light | 6 / 6 | 5/4/3 | 1/3 | – | +6 | – |
| Bauer | Hanse | CannonFodder / Melee | 2 | 10 | 0 | 4 | 3 | 4 | 1 | Pierce | Unarmored | 0 / 0 | 4/3/2 | 2/2 | – | +0 | – |
| Lüneburger Armbrustschütze | Hanse | CannonFodder / Ranged | 2 | 15 | 0 | 4 | 3 | 9 | 5 | Pierce | Medium | 1 / 0 | 6/3/2 | 2/2 | – | +0 | – |
| Kleriker | Clergy | Warrior / Support | 2 | 14 | 4 | 5 | 3 | 4 | 2 | Holy | Light | 4 / 6 | 4/3/2 | 1/1 | – | +0 | – |
| Heideschwester | Clergy | Warrior / Support | 2 | 14 | 4 | 5 | 3 | 4 | 2 | Holy | Light | 4 / 6 | 4/3/2 | 1/1 | – | +0 | – |
| Hexe | Witches | Warrior / Caster | 2 | 14 | 6 | 5 | 3 | 7 | 4 | Arcane | Light | 5 / 2 | 4/3/3 | 1/2 | – | +0 | – |
| Druide | Witches | Warrior / Support | 2 | 16 | 5 | 4 | 3 | 5 | 3 | Arcane | Light | 5 / 3 | 4/3/3 | 1/2 | – | +0 | – |
| Hügelgrab-Druidin | Witches | Warrior / Caster | 2 | 16 | 5 | 6 | 3 | 7 | 4 | Arcane | Light | 5 / 3 | 4/3/4 | 1/2 | – | +0 | – |
| Moorgeist | HeathSpirits | Warrior / Tank | 3 | 30 | 2 | 3 | 2 | 8 | 1 | Blunt | Unarmored | 3 / 2 | 3/4/2 | 2/3 | – | +0 | – |
| Irrlicht | HeathSpirits | CannonFodder / Scout | 1 | 6 | 0 | 9 | 5 | 3 | 1 | Arcane | Unarmored | 6 / 4 | 6/3/0 | 0/0 | Spektral/Flug | +0 | – |
| Schwarzer Hund | HeathSpirits | CannonFodder / Scout | 2 | 8 | 0 | 7 | 5 | 4 | 1 | Rend | Unarmored | 3 / 2 | 4/4/6 | 1/1 | Spektral | +0 | – |
| Der Wode | HeathSpirits | Unique / Melee | 3 | 55 | 8 | 8 | 6 | 12 | 1 | Pierce | Divine | 5 / 6 | 6/5/5 | 4/2 | – | +0 | – |
| Hügelgrab-Zwergenkönig | HeathSpirits | Unique / Tank | 2 | 50 | 6 | 3 | 2 | 11 | 1 | Blunt | Divine | 6 / 4 | 4/6/4 | 2/1 | – | +0 | – |
| Die Heidekönigin | Witches | Unique / Caster | 3 | 60 | 10 | 6 | 2 | 10 | 4 | Arcane | Divine | 8 / 10 | 6/5/5 | 1/2 | – | +0 | – |
| Moorleiche | Undead | Warrior / Tank | 3 | 28 | 2 | 3 | 2 | 8 | 1 | Blunt | Unarmored | 2 / 0 | 3/3/2 | 2/4 | – | -3 | 3L |
| Totenlicht | Undead | CannonFodder / Scout | 1 | 6 | 0 | 9 | 5 | 3 | 1 | Arcane | Unarmored | 6 / 2 | 6/3/0 | 0/0 | Spektral/Flug | -1 | 1S |
| Gefallene Schwester | Undead | Warrior / Support | 2 | 14 | 4 | 5 | 3 | 4 | 2 | Soul | Light | 4 / 2 | 4/3/2 | 1/2 | – | -2 | 1L 1S |
| Grabdruidin | Undead | Warrior / Caster | 2 | 14 | 5 | 6 | 3 | 7 | 4 | Arcane | Light | 5 / 2 | 4/3/4 | 1/3 | – | -3 | 1L 1K 1S |
| Wasserleiche | Undead | Warrior / Tank | 2 | 26 | 3 | 3 | 3 | 8 | 1 | Blunt | Unarmored | 3 / 2 | 3/2/4 | 2/4 | – | -3 | 2L 1S |
| Knochenschütze | Undead | CannonFodder / Ranged | 2 | 10 | 0 | 4 | 3 | 8 | 5 | Pierce | Light | 0 / 0 | 5/2/0 | 2/1 | – | -2 | 3K |
| Totenjäger | Undead | Warrior / Scout | 3 | 22 | 3 | 7 | 6 | 9 | 1 | Pierce | Light | 2 / 0 | 5/4/3 | 3/3 | – | -4 | 3L 2K 1S |
| Skelett-Bogenschütze | Undead | CannonFodder / Ranged | 1 | 9 | 0 | 4 | 3 | 4 | 4 | Pierce | Light | 0 / 0 | 5/2/1 | 1/1 | – | -2 | 3K |
| Leichenhund | Undead | CannonFodder / Scout | 1 | 10 | 0 | 7 | 5 | 4 | 1 | Rend | Unarmored | 0 / 0 | 4/4/6 | 1/3 | – | -1 | 1L |
| Knochenschleuderer | Undead | Warrior / Ranged | 1 | 10 | 0 | 4 | 3 | 6 | 4 | Blunt | Light | 0 / 0 | 5/2/1 | 1/1 | – | -2 | 3K |
| Stadtwache | Hanse | Warrior / Melee | 2 | 18 | 0 | 5 | 3 | 6 | 1 | Pierce | Medium | 0 / 0 | 5/3/2 | 2/2 | – | +0 | – |
| Ritter | Guelphs | Warrior / Tank | 2 | 30 | 0 | 6 | 4 | 9 | 1 | Pierce | Heavy | 1 / 1 | 5/2/2 | 3/2 | – | +0 | – |
| Stadtballiste | Hanse | Machine / Siege | 3 | 25 | 0 | 2 | 1 | 20 | 6 | Siege | Fortified | 0 / 0 | 6/3/1 | 4/1 | – | +0 | – |
| Mönch | Clergy | Warrior / Caster | 1 | 12 | 0 | 5 | 3 | 6 | 3 | Holy | Unarmored | 3 / 3 | 5/4/3 | 1/1 | – | +0 | – |
| Priester | Clergy | Warrior / Support | 1 | 16 | 0 | 4 | 3 | 6 | 3 | Heal | Unarmored | 4 / 4 | 5/4/3 | 1/1 | – | +0 | – |
| Rattenfänger | Witches | Unique / Caster | 2 | 35 | 0 | 8 | 4 | 9 | 4 | Arcane | Light | 5 / 3 | 7/7/3 | 2/1 | – | +0 | – |
| Hexenkönigin vom Brocken | Witches | Unique / Caster | 3 | 90 | 0 | 8 | 4 | 14 | 4 | Chaos | Divine | 6 / 6 | 8/8/8 | 2/2 | Flug | +0 | – |
| Sachsenkrieger | WodanCult | Warrior / Melee | 2 | 20 | 0 | 5 | 3 | 7 | 1 | Pierce | Medium | 2 / 0 | 5/3/2 | 2/2 | – | +0 | – |
| Wodansrabe | WodanCult | CannonFodder / Scout | 1 | 6 | 0 | 9 | 6 | 3 | 1 | Rend | Unarmored | 3 / 2 | 7/4/2 | 1/1 | Flug | +0 | – |
| Wilder Jäger | WodanCult | Warrior / Scout | 3 | 26 | 4 | 7 | 6 | 9 | 1 | Pierce | Light | 3 / 2 | 6/5/4 | 3/2 | Spektral | +0 | – |
| Hackelberg | WodanCult | Unique / Melee | 3 | 60 | 8 | 7 | 6 | 13 | 1 | Pierce | Divine | 5 / 6 | 7/6/5 | 4/2 | – | +0 | – |
| Lutki | Spreewald | CannonFodder / Melee | 1 | 7 | 0 | 7 | 3 | 3 | 1 | Blunt | Unarmored | 3 / 0 | 4/4/3 | 1/1 | – | +0 | – |
| Wassermann | Spreewald | Warrior / Tank | 2 | 32 | 4 | 4 | 3 | 8 | 1 | Blunt | Unarmored | 3 / 2 | 4/4/3 | 2/2 | – | +0 | – |
| Rusalka | Spreewald | Warrior / Caster | 2 | 14 | 5 | 6 | 3 | 7 | 3 | Arcane | Light | 5 / 3 | 5/4/2 | 0/1 | Spektral | +0 | – |
| Mittagsfrau | Spreewald | Warrior / Melee | 2 | 22 | 4 | 6 | 4 | 11 | 1 | Rend | Unarmored | 4 / 2 | 5/4/3 | 1/1 | Spektral | +0 | – |
| Schlangenkönig | Spreewald | Unique / Caster | 3 | 65 | 8 | 6 | 3 | 12 | 3 | Poison | Divine | 6 / 6 | 6/5/6 | 2/2 | – | +0 | – |
| Ertrunkener | Wattenmeer | CannonFodder / Melee | 2 | 16 | 0 | 3 | 2 | 6 | 1 | Blunt | Unarmored | 1 / 0 | 3/2/3 | 2/3 | – | +0 | – |
| Wattjungfrau | Wattenmeer | Warrior / Caster | 2 | 14 | 4 | 6 | 3 | 6 | 3 | Arcane | Light | 5 / 3 | 6/4/2 | 0/1 | Spektral | +0 | – |
| Klabautermann | Wattenmeer | Warrior / Support | 1 | 12 | 4 | 7 | 3 | 6 | 1 | Blunt | Light | 4 / 2 | 5/5/3 | 2/1 | – | +0 | – |
| Blanker Hans | Wattenmeer | Unique / Caster | 4 | 80 | 10 | 5 | 4 | 14 | 3 | Blunt | Divine | 6 / 8 | 7/6/4 | 4/1 | – | +0 | – |
<!--GEN:UNITS:END-->

**Neue Lich-Einheiten in Kürze:**
- **Zombie** – billig, langsam, zäh. Seuchenbiss vergiftet. Der Gegenpol zum Skelett: mehr HP, viel schlechter in Stealth.
- **Nekromant** – generischer Kommandeur (+4 Kommandopunkte netto). Totenruf verwandelt Leichen auf dem Feld in Skelette – kostet aber Beute.
- **Fleischriese** – 15 Leichen, 8 Kommandopunkte. Zermalmen trifft drei Felder im Kegel. Stealth praktisch unmöglich.
- **Schwarzer Hund** – nur beschworen (vom Wode), nicht produzierbar.

### Fähigkeiten (S_AbilityData / DT_Abilities)

Fähigkeiten sind Daten, kein Code pro Einheit. Eine Fähigkeit = eine Zeile. Einheiten verweisen über `Abilities` darauf.

```
struct S_AbilityData {
    AbilityName     : string
    Trigger         : E_TriggerType
    Target          : E_TargetType
    Pattern         : E_AreaPattern
    AreaSize        : int            // Radius, Länge der Linie/des Kegels
    Range           : int            // 0 = am eigenen Feld
    Effect          : E_EffectType
    PowerType       : E_PowerType    // Schadens-/Heilart, bestimmt auch VFX-Farbe
    Value           : int            // Schaden, Heilung, Schildwert, Anzahl Beschwörungen
    Status          : E_StatusEffect // None = kein Status
    Duration        : int            // Züge
    EnergyCost      : int
    Cooldown        : int            // Züge
    RequiresCorpse  : bool           // braucht Leiche auf Zielfeld, verbraucht sie
    ConditionFloors : Array<E_FloorType>  // leer = überall
    Description     : string
}
```

Sonderfälle, die die Tabelle nicht ausdrückt (Zweit-Effekte, Bedingungen wie „nicht bewegt"), stehen in `Description` und werden einzeln im Code der Fähigkeit umgesetzt. Ziel: ≥ 80 % der Fähigkeiten laufen rein über die Tabelle.

<!--GEN:ABILITIES:BEGIN-->
| ID | Name | Einheit | Auslöser | Ziel / Muster | Reichw. | Effekt | Wert | Status (Züge) | Energie / CD | Beschreibung |
|-|-|-|-|-|-|-|-|-|-|-|
| `LichSoulDrain` | Seelenentzug | Lich | Active | Enemy / SinglePoint | 3 | Damage (Soul) | 8 | – | 3 / 1 | 8 Seelenschaden; Lich heilt sich um den angerichteten Schaden |
| `LichRetreat` | Rückzug | Lich | Active | Self / SinglePoint | 0 | Teleport (Arcane) | 0 | Marked (1) | 0 / 0 | Lich verlässt nach 1 Runde das Feld; in der Rückzugsrunde Marked |
| `SkeletonReassemble` | Wiederzusammensetzen | Skelett | OnDeath | Self / SinglePoint | 0 | Heal (Heal) | 5 | – | 0 / 0 | Einmal pro Kampf mit 5 HP wieder aufstehen; nicht nach Blunt- oder Holy-Tod |
| `ZombieInfect` | Seuchenbiss | Zombie, Schlangenkönig, Ertrunkener | OnDamageDealt | Enemy / SinglePoint | 1 | ApplyStatus (Poison) | 2 | Poisoned (2) | 0 / 0 | Getroffenes Ziel wird vergiftet |
| `GhoulCorpseEater` | Leichenfresser | Ghul | Active | Ground / SinglePoint | 1 | Heal (Heal) | 8 | – | 0 / 2 | Frisst angrenzende Leiche: +8 HP, die Leiche ist als Beute verloren *(braucht Leiche)* |
| `DeathKnightShieldWall` | Schildwall | Todesritter, Hünenkönig | Active | Ally / Radius 1 | 0 | ApplyStatus (Blunt) | 5 | Shielded (1) | 2 / 2 | Todesritter und Nachbarn erhalten Schild 5 bis zum nächsten Zug |
| `NecroRaiseDead` | Totenruf | Nekromant, Ratsherr von Rungholt | Active | Ground / SinglePoint | 3 | Summon (Soul) | 1 | – | 4 / 2 | Verbraucht Leiche auf Zielfeld, erzeugt 1 Skelett *(braucht Leiche)* |
| `FleshGiantCrush` | Zermalmen | Fleischriese, Hünenkönig, Schlangenkönig, Blanker Hans | Active | Enemy / Cone 1 | 1 | Damage (Blunt) | 10 | Stunned (1) | 3 / 2 | Trifft 3 Felder im Kegel, betäubt |
| `PeasantMob` | Rottenmut | Widukinds Schatten, Bauer, Sachsenkrieger, Lutki | OnTurnStart | Self / SinglePoint | 0 | ApplyStatus (Pierce) | 0 | Enhanced (1) | 0 / 0 | Enhanced, wenn mind. 2 Bauern angrenzen |
| `CrossbowPavise` | Setzschild | Lüneburger Armbrustschütze, Knochenschütze | Passive | Self / SinglePoint | 0 | ModifyTerrain (Pierce) | 0 | – | 0 / 0 | Wenn nicht bewegt: Kante zur Angriffsrichtung zählt als Cover |
| `ClericCenser` | Weihrauch | Kleriker | Active | AllEnemies / Radius 1 | 0 | Damage (Holy) | 4 | – | 2 / 1 | 4 Holy-Schaden an alle angrenzenden Feinde |
| `SisterHolyWater` | Weihwasser | Heideschwester | Active | Ally / SinglePoint | 2 | Heal (Heal) | 6 | – | 2 / 0 | Heilt Verbündeten um 6 HP |
| `SisterConsecrate` | Geweihter Boden | Heideschwester | Active | Ground / Radius 1 | 2 | ModifyTerrain (Holy) | 2 | – (3) | 3 / 3 | Felder werden 3 Runden HolyGround: 2 Holy-Schaden pro Runde an Untote |
| `WitchHex` | Hexenschuss | Hexe, Mittagsfrau, Wattjungfrau | Active | Enemy / SinglePoint | 4 | ApplyStatus (Arcane) | 0 | Marked (2) | 2 / 1 | Ziel nimmt 2 Züge lang +25 % Schaden |
| `DruidMistletoe` | Mistelsegen | Druide, Schlangenkönig | Active | Ally / SinglePoint | 3 | ApplyStatus (Heal) | 3 | Regeneration (3) | 2 / 1 | Verbündeter regeneriert 3 HP pro Zug |
| `DruidessGraveRest` | Grabesruhe | Hügelgrab-Druidin, Rusalka | Active | Enemy / SinglePoint | 4 | ApplyStatus (Arcane) | 0 | Cursed (2) | 3 / 2 | Nur gegen Untote: -25 % Schaden |
| `DruidessEarthBind` | Erdbindung | Hügelgrab-Druidin, Grabdruidin | Active | Ground / SinglePoint | 3 | ModifyTerrain (Arcane) | 0 | – (2) | 2 / 3 | Feld wird 2 Runden unpassierbar, Kanten ringsum Cover |
| `MoorGrip` | Moorgriff | Ratsherr von Rungholt, Moorgeist, Moorleiche, Wasserleiche, Wassermann | Active | Enemy / SinglePoint | 1 | ApplyStatus (Blunt) | 0 | Slowed (2) | 2 / 1 | Slowed 2 Züge; auf Mud/Swamp/Bog zusätzlich Stunned 1 Zug |
| `FromThePeat` | Aus dem Torf | Moorgeist, Wassermann | OnTurnStart | Self / SinglePoint | 0 | ApplyStatus (Blunt) | 4 | Shielded (1) | 0 / 0 | Auf Moorboden zu Zugbeginn Schild 4 *(nur auf Mud, Swamp, Bog)* |
| `WispConfusion` | Verwirrung | Irrlicht, Wattjungfrau | Passive | AllEnemies / Ring 1 | 0 | ApplyStatus (Arcane) | 0 | Confused (1) | 0 / 0 | Feinde auf Nachbarfeldern bewegen sich zufällig |
| `WispFalseLight` | Falsches Licht | Irrlicht | OnDeath | Ground / SinglePoint | 0 | Summon (Arcane) | 1 | – (1) | 0 / 0 | Trugbild für 1 Runde, zieht Angriffe auf sich |
| `HoundPack` | Meute | Schwarzer Hund, Wodansrabe | OnTurnStart | Self / SinglePoint | 0 | ApplyStatus (Rend) | 0 | Enhanced (1) | 0 / 0 | Enhanced, wenn ein anderer Schwarzer Hund angrenzt |
| `WodeWildHunt` | Wilde Jagd | Der Wode, Hackelberg | Active | Ground / SinglePoint | 2 | Summon (Soul) | 2 | – | 5 / 4 | Beschwört 2 Schwarze Hunde |
| `WodeRideThrough` | Durchreiten | Der Wode, Hackelberg | Active | Enemy / Line 3 | 3 | Damage (Pierce) | 12 | – | 3 / 2 | Reitet 3 Felder in Linie, trifft alle darauf, endet am Linienende |
| `WodeHorn` | Jagdhorn | Bronzezeitlicher Reiterfürst, Widukinds Schatten, Der Wode, Hackelberg, Blanker Hans | Active | AllAllies / Radius 3 | 0 | ApplyStatus (Arcane) | 0 | Hasted (2) | 2 / 3 | Verbündete im Radius 3 werden beschleunigt |
| `DwarfKingForge` | Runenschmiede | Hügelgrab-Zwergenkönig, Klabautermann | Active | Ally / SinglePoint | 1 | ApplyStatus (Blunt) | 8 | Shielded (2) | 2 / 1 | Verbündeter erhält Schild 8 |
| `DwarfKingTreasureCurse` | Schatzfluch | Hügelgrab-Zwergenkönig | OnDamageTaken | Enemy / SinglePoint | 0 | ApplyStatus (Arcane) | 0 | Cursed (2) | 0 / 0 | Wer den Zwergenkönig trifft, wird verflucht |
| `DwarfKingStoneSkin` | Steinhaut | Hügelgrab-Zwergenkönig | OnTurnStart | Self / SinglePoint | 0 | ApplyStatus (Blunt) | 4 | Shielded (1) | 0 / 0 | Auf Steinboden zu Zugbeginn Schild 4 *(nur auf StoneFloor, CellarFloor, RawStone)* |
| `HeathQueenLeyBond` | Ley-Bund | Die Heidekönigin | Passive | Self / SinglePoint | 0 | ApplyStatus (Arcane) | 10 | Shielded (0) | 0 / 0 | Kampfbeginn: +10 SoulShield pro lebendem Randmitglied des Heide-Pantheons |
| `HeathQueenBloom` | Heideblüte | Die Heidekönigin | Active | AllAllies / Radius 2 | 0 | Heal (Heal) | 6 | – | 4 / 2 | Heilt alle Verbündeten im Radius 2 um 6 HP |
| `HeathQueenThorns` | Dornenkrone | Die Heidekönigin, Blanker Hans | Active | Ground / Radius 1 | 4 | ModifyTerrain (Pierce) | 3 | Slowed (3) | 4 / 3 | Dornen-Gelände 3 Runden: Slowed und 3 Pierce-Schaden pro Runde für Feinde darauf |
| `BogCorpseMire` | Moorheilung | Moorleiche, Wasserleiche | OnTurnStart | Self / SinglePoint | 0 | Heal (Heal) | 3 | – | 0 / 0 | Heilt sich auf Moorboden zu Zugbeginn um 3 HP *(nur auf Mud, Swamp, Bog)* |
| `DeathLightConfusion` | Totenirrlicht | Totenlicht | Passive | AllEnemies / Ring 2 | 0 | ApplyStatus (Arcane) | 0 | Confused (1) | 0 / 0 | Lebende Feinde im Umkreis 2 bewegen sich zufällig |
| `FallenSisterGraveWater` | Grabwasser | Gefallene Schwester | Active | Ally / SinglePoint | 2 | Heal (Soul) | 6 | – | 2 / 0 | Heilt verbündeten Untoten um 6 HP |
| `GraveDruidessBind` | Lebensbann | Grabdruidin | Active | Enemy / SinglePoint | 4 | ApplyStatus (Arcane) | 0 | Cursed (2) | 3 / 2 | Nur gegen Lebende: -25 % Schaden |
| `DeathHunterCharge` | Todesritt | Bronzezeitlicher Reiterfürst, Totenjäger, Wilder Jäger | Active | Enemy / Line 2 | 2 | Damage (Pierce) | 9 | – | 3 / 2 | Reitet 2 Felder in Linie, trifft alle darauf |
<!--GEN:ABILITIES:END-->

### Balancing-Check (automatisch)

`sim.py` rechnet aus `DT_Units.csv` und der Power-Defense-Matrix, wie viele Grundangriffe eine Einheit braucht, um eine andere zu töten (ohne Fähigkeiten, Gelände, Konter). Läuft bei jedem Generator-Lauf mit; die Tabellen hier sind generiert.

**Schadensformel:**
```
Schaden = AttackDamage × Matrix[PowerType][DefenseType]
falls magisch (Arcane, Soul, Holy, Chaos): × (1 − min(50 %, MagicResist × 5 %))
gerundet, mindestens 1 (außer Matrix = 0 → immun)
Treffer bis Tod = aufrunden((HP + SoulShield) / Schaden)
```

**Eigene Einheiten greifen Heide-Gegner an:**

<!--GEN:BAL_HITS_P:BEGIN-->
| Angreifer ↓ / Ziel → | Bauer | Lüneburger Armbrustschütze | Heideschwester | Hügelgrab-Druidin | Moorgeist | Irrlicht |
|-|-|-|-|-|-|-|
| Skelett | 2 | 3 | 4 | 4 | 7 | 2 |
| Zombie | 2 | 4 | 4 | 4 | 6 | 2 |
| Ghul | 2 | 4 | 4 | 4 | 4 | 2 |
| Todesritter | 1 | 2 | 2 | 2 | 4 | 1 |
| Geist | 1 | 2 | 3 | 3 | 4 | 2 |
| Nekromant | 2 | 3 | 4 | 4 | 4 | 2 |
| Fleischriese | 1 | 2 | 2 | 2 | 3 | 1 |
| Lich | 1 | 2 | 2 | 2 | 3 | 1 |
<!--GEN:BAL_HITS_P:END-->

**Heide-Gegner greifen eigene Einheiten an:**

<!--GEN:BAL_HITS_E:BEGIN-->
| Angreifer ↓ / Ziel → | Skelett | Zombie | Ghul | Todesritter | Geist | Nekromant | Fleischriese | Lich |
|-|-|-|-|-|-|-|-|-|
| Bauer | 3 | 5 | 5 | 13 | 4 | 6 | 18 | 20 |
| Lüneburger Armbrustschütze | 2 | 3 | 2 | 6 | 2 | 3 | 8 | 9 |
| Heideschwester | 2 | 4 | 3 | 13 | 4 | 6 | 18 | 20 |
| Hügelgrab-Druidin | 2 | 3 | 3 | 7 | 3 | 5 | 10 | 20 |
| Moorgeist | 2 | 3 | 3 | 5 | 2 | 3 | 12 | 10 |
| Irrlicht | 4 | 7 | 6 | 13 | 8 | 11 | 24 | 40 |
<!--GEN:BAL_HITS_E:END-->

**Kosten-Nutzen eigener Einheiten** (gegen den Durchschnitt der 6 Heide-Gegner). Zähigkeit = Treffer, die Gegner im Schnitt brauchen. Schlagkraft = Initiative × Angriffe ÷ benötigte Treffer. Kampfwert = Zähigkeit × Schlagkraft.

<!--GEN:BAL_VALUE:BEGIN-->
| Einheit | Zähigkeit | Schlagkraft | Kampfwert | KP | Kampfwert/KP |
|-|-|-|-|-|-|
| Skelett | 2.5 | 1.65 | 4.1 | 1 | 4.12 |
| Zombie | 4.2 | 0.96 | 4.0 | 1 | 3.99 |
| Ghul | 3.7 | 1.67 | 6.1 | 2 | 3.06 |
| Todesritter | 9.5 | 2.50 | 23.8 | 4 | 5.94 |
| Geist | 3.8 | 3.89 | 14.9 | 3 | 4.97 |
| Fleischriese | 15.0 | 1.28 | 19.2 | 8 | 2.40 |
| Balliste | 9.3 | 1.50 | 14.0 | 5 | 2.80 |
| Moorleiche | 6.0 | 1.12 | 6.8 | 3 | 2.25 |
| Totenlicht | 2.0 | 1.41 | 2.8 | 1 | 2.82 |
| Gefallene Schwester | 3.8 | 1.36 | 5.2 | 2 | 2.60 |
| Grabdruidin | 4.0 | 2.00 | 8.0 | 3 | 2.67 |
| Knochenschütze | 2.5 | 1.61 | 4.0 | 2 | 2.01 |
| Totenjäger | 5.0 | 2.82 | 14.1 | 4 | 3.52 |
<!--GEN:BAL_VALUE:END-->

**Zielkorridor:** Kampfwert/KP etwa 3–6. Darunter nur mit klarer Spezialrolle (Balliste: Belagerung, ×1,5 gegen Fortified; Fleischriese: Flächenangriff auf 3 Felder).

**Befunde und Korrekturen (01.11.2026):**

| Befund | Korrektur |
|-|-|
| MagicResist als fester Abzug machte magischen Schaden gegen MR ≥ 5 fast wirkungslos: Heideschwester brauchte 50 Treffer für den Lich, 38 für den Todesritter. Heilig soll aber *die* Waffe gegen Untote sein | MagicResist wirkt prozentual (5 %/Punkt, max. 50 %). Jetzt 13 Treffer |
| Fleischriese: Kampfwert/KP 0,64 – klar schlechter als jede Alternative | 15 → **8 KP**, Initiative 1 → **2**. Jetzt 2,4 (mit Flächenangriff effektiv ~4,8) |
| Zombie: zu selten am Zug (Initiative 2) | Initiative 2 → **3** |
| Initiative-Formel nicht linear (siehe unten) | Neue Formel `2520 / Initiative` |
| Todesritter liegt mit ~5,9 am oberen Rand | Bleibt vorerst – er kostet als einzige Grundeinheit Seelen. Im Spieltest beobachten |

### Initiative-System: Tick-basiert

`nächster_Zug = 2520 / Initiative` zu Beginn, danach `+= 2520 / Initiative` nach jedem Zug. Niedrigster Tick = nächste dran. Einheit A (Initiative 8) ist doppelt so oft dran wie Einheit B (Initiative 4). 2520 ist das kleinste gemeinsame Vielfache von 1–10 – jede Initiative ergibt ganze Ticks.

*Geändert 01.11.2026:* Die alte Formel `+= 10 - Initiative` widersprach dem eigenen Beispiel (8 gegen 4 ergab 2 gegen 6 Ticks = **dreimal** so oft) und eskaliert nahe 10: Initiative 9 war doppelt so schnell wie 8 und neunmal so schnell wie 1. Die neue Formel ist linear – doppelte Initiative = doppelt so viele Züge.

Gleichstand bei Ticks: höhere Initiative zuerst, dann Spieler vor Gegner.

### Trennung Stammdaten vs. Laufzeit-Werte

`S_UnitData` enthält nur die Maximalwerte (Schablone). Die Einheit im Spiel trägt die akuten Werte zur Laufzeit.

**S_UnitData (Stammdaten, unveränderlich):**
- HP, MaxEnergy, Initiative, etc. = Maximalwerte

**Einheit zur Laufzeit:**
- `CurrentHP` – aktueller HP-Stand
- `CurrentEnergy` – aktuelle Energy
- `ActiveStatuses` – Array aktiver Status-Effekte
- `NextTurnTick` – für Initiative-System
- `Facing` – Blickrichtung 0–5 (Hex-Richtung, für Stealth-Sichtkegel)
- `VisualState` – E_UnitVisualState (siehe Einheiten-Visualisierung)

Beim Erzeugen liest die Einheit die Stammdaten aus DT_Units und initialisiert die akuten Werte (`CurrentHP = data.HP`, `CurrentEnergy = data.MaxEnergy`). Danach lädt sie über denselben Zeilennamen Modell, Material und Icons aus `DT_UnitVisuals`.

Effektive Stats werden über Getter-Funktionen berechnet, die Basiswert + alle Status-Modifikatoren summieren.

---

## Einheiten-Visualisierung

**Leitsatz:** Ein Spieler muss jede Einheit auf Standard-Zoom **in unter einer Sekunde** einordnen können – *wem gehört sie, was tut sie, wie geht es ihr.* Dark-Fantasy-Atmosphäre darf Lesbarkeit nie kosten.

### Drei Lese-Ebenen

| Ebene | Frage | Transportiert durch |
|-|-|-|
| 1. Silhouette | Was tut die Einheit? | Form, Größe, Waffenlinie (`Role`, `Size`) |
| 2. Farbe | Wem gehört sie? | Fraktions-Palette, Leuchtfarbe, Sockel |
| 3. Overlay | Wie geht es ihr? | HP-Segmente, Status-Icons, Rang-Abzeichen, Zustands-Shader |

Regel: **Jede Ebene muss allein funktionieren.** Test: Bild in Graustufen → Rolle noch erkennbar? Bild unscharf → Fraktion noch erkennbar?

### Silhouetten-Sprache nach Rolle

| Rolle | Silhouette | Merkmal aus der Kamera-Schräge |
|-|-|-|
| `Melee` | breit, nach vorn geneigt | Waffe kurz, nah am Körper |
| `Tank` | massiv, rechteckig, aufrecht | großer Schild oder Panzerplatten, breite Schultern |
| `Ranged` | schlank, aufrecht | lange diagonale Linie (Bogen, Speer, Armbrust) |
| `Caster` | vertikal, schmal unten | Stab/Fetisch überragt den Kopf, Leuchtpunkt an der Spitze |
| `Support` | rundlich, gebeugt | Gefäß, Buch oder Laterne in der Hand |
| `Siege` | horizontal, kantig | mechanische Teile, kein menschlicher Umriss |
| `Scout` | klein, schräg, „in Bewegung" | asymmetrisch, oft vierbeinig oder schwebend |
| `Commander` | wie Grundrolle, aber erhöht | Banner, Umhang oder Krone als höchster Punkt |

**Regel „höchster Punkt":** Das Element, das die Rolle verrät (Stab, Banner, Bogen), ist der höchste oder am weitesten herausragende Punkt der Figur. Aus der Schräg-Kamera wird er zuerst gesehen.

### Größen-Skalierung

`Size` steuert die Figurenhöhe relativ zum Hex (HexSize = 300 cm):

| Size | Höhe | Beispiele | Sockel |
|-|-|-|-|
| 1 | ~140 cm | Skelett, Geist, Irrlicht, Kobold | Ring 60 % des Hex |
| 2 | ~190 cm | Ghul, Mensch, Todesritter | Ring 75 % |
| 3 | ~280 cm | Balliste, Oger, Reiter | Ring 90 % |
| 4 | ~420 cm | Fleischriese, Pantheon-Boss | voller Hex + Bodenschatten über Nachbarfelder |

Größe ist auch **Stealth-Information** (größer = auffälliger). Der Spieler soll Größe also *sehen*, nicht nachlesen müssen.

### Fraktions-Paletten

Jede Fraktion hat drei Farben: **Primär** (Stoff, große Flächen), **Akzent** (Wappen, Ränder), **Leuchten** (Emissive: Augen, Runen, Magie). Gebäude nutzen diese Farben nicht (siehe Schlachtfeld-Bausteine).

| Fraktion | Primär | Akzent | Leuchten | Motiv |
|-|-|-|-|-|
| `Undead` | Knochenweiß / Grabgrau | Rostbraun | Nekrotisches Grün | Leere Augenhöhlen mit grünem Glimmen |
| `Hanse` | Rot | Weiß | – (kein Leuchten) | Rot-weiß geteilte Wappen, Koggen-Symbol |
| `Guelphs` | Rot | Gold | – | Goldener Löwe auf Rot |
| `Clergy` | Weiß / Wollgrau | Gold | Warmes Kerzengold | Kreuz, Heiligenschein-Schimmer |
| `Witches` | Dunkles Aubergine | Violett | Mondviolett | Mondsichel, Kräuterbündel |
| `WodanCult` | Eisengrau | Blutrot | Runen-Bernstein | Wolf, Rabe, Speer |
| `Spreewald` | Moosgrün | Schilfgelb | Wassertürkis | Schlange mit Krone, Schilf |
| `Wattenmeer` | Schlickgrau | Sturmblau | Meerleuchten (Cyan) | Muscheln, Tang, Wellen |
| `HeathSpirits` | Torfbraun | Heidelila | Irrlicht-Blassgelb | Wurzeln, Sumpfgas, Heidekraut |

**Im Spiel (Nov. 2026):** Die mythischen Fraktionen der Palette sind jetzt eigene Fraktionen mit Bedrohung: **Wodan-Kult** (Hackelbergs Grab, Kyffhäuser★, Externsteine), **Spreewald** (Spreewald★, Kap Arkona), **Wattenmeer** (Rungholt★, Vineta), **Heidegeister** (`HeathSpirits`: Teufelsmoor, Dümmer-Moor, Arendsee, Pestruper Gräberfeld, Sieben Steinhäuser, Iberg, Oldendorfer Totenstatt★ mit der Heidekönigin). **Hexen und Haine** behalten Brocken★, Hameln, Hexentanzplatz, Teufelsmauer, Schierke. Dazu die weltlichen Fraktionen Hanse, Welfen, Askanier, Klerus, Grafen, Mecklenburg, Wettiner. ★ = große Stadt bzw. Hauptort (Kampffeld 64); jede Fraktion hat mindestens einen. Eigene Einheiten für Wodan-Kult, Spreewald und Wattenmeer fehlen noch (sie nutzen vorerst Hexen-, Heide- und Geister-Einheiten).

**Mindest-Helligkeit:** Keine Primärfarbe dunkler als das dunkelste Gelände bei Nacht. *Befund 01.11.2026 aus dem Einheitenbuch:* Die Hexen-Primärfarbe war Schwarz – Hexe, Druide, Druidin und Heidekönigin verschwanden auf dunklem Grund, nachts blieb nur die Stabspitze sichtbar. Geändert zu dunklem Aubergine (#43364F), Akzent heller (#8A5BB0). Zusätzlich empfohlen: ein schwacher Rim-Light-/Fresnel-Anteil im Einheiten-Material, damit dunkle Silhouetten sich immer vom Boden lösen.

**Regel:** Lebende Menschenfraktionen leuchten nicht. Leuchten = übernatürlich. Damit erkennt man Magie-Einheiten auch in gemischten Pantheons sofort.

**Untote Versionen besiegter Gegner** (Mythologie-Wissen): behalten Silhouette und Akzentfarbe des Originals, Primär wird zu Knochenweiß/Grabgrau, Leuchten wird Nekrotisch-Grün. Der Spieler erkennt „das war mal eine Hexe, jetzt ist sie meine".

### Hex-Sockel (Freund/Feind)

Jede Einheit steht auf einem flachen Sockel-Ring auf dem Hex.

| Seite | Randform | Farbe |
|-|-|-|
| Spieler | glatter, durchgehender Ring | Nekrotisches Grün |
| Feind | gezackter Ring (6 Zacken, an Hex-Kanten) | Fraktions-Akzent |
| Neutral / Zivilist | gestrichelter Ring | Grau |
| Verbündeter Fremdtrupp (Spätphase) | gezackt, Innenfarbe eigene Fraktion, Außenrand führende Fraktion | zweifarbig |

**Farbenblind-sicher:** Freund/Feind wird über die **Form** getragen, Farbe ist Zusatz.

**Sockel-Zustände** (überlagert, in dieser Priorität):
1. **Aktiv** (am Zug) – Sockel pulsiert, Lichtsäule nach oben
2. **Ausgewählt** – heller Rand
3. **Anvisiert** (Hover bei Angriff) – roter Zielkreis
4. **Bereits gezogen** – Sockel 50 % abgedunkelt
5. **Blickrichtung** – kleiner Pfeil am Sockelrand (nur Stealth-Phase und für Konter relevant)

### Rang-Abzeichen

Kleines Symbol rechts über dem HP-Balken:

| Rang | Abzeichen |
|-|-|
| `CannonFodder` | keins (Masse soll ruhig wirken) |
| `Warrior` | eine Kerbe |
| `Machine` | Zahnrad |
| `Commander` | Banner + **Befehls-Aura** am Boden (Radius, in dem das Kommando-Limit wirkt) |
| `Unique` | Krone, goldener Rand am HP-Balken, **Namensschild** bei Hover |

### Overhead-UI

- **HP als Segmente:** 1 Segment = 5 HP. Ghul (18 HP) = 4 Segmente, Balliste (25) = 5. Segmente lesen sich schneller als ein glatter Balken.
- **SoulShield:** blaue Überlagerung über den Segmenten, verbraucht sich zuerst.
- **Status-Icons:** max. 3 sichtbar, danach „+n". Reihenfolge: Kontrollverlust (Stunned) > Schaden über Zeit (Burning, Poisoned, Bleeding) > Buffs.
- **Sichtbarkeit:** Standard nur bei verwundeten, aktiven oder anvisierten Einheiten. **Alt halten** = alle Overheads einblenden.
- **Initiative-Vorschau:** Bei Hover über eine Einheit leuchtet ihr Portrait in der Initiative-Leiste auf (und umgekehrt).

### Status-Effekte: Symbole und Standardwerte

Jeder Status hat Farbe, Symbol und einen kleinen Effekt am Modell. Farben folgen dem PowerType-Farbcode, wo es einen gibt.

| Status | Symbol | Farbe | Am Modell | Standardwirkung |
|-|-|-|-|-|
| Poisoned | Tropfen | Gelbgrün | grüne Blasen steigen auf | 2 Schaden/Zug, 3 Züge |
| Burning | Flamme | Orange | Flammen an den Füßen | 3 Schaden/Zug, 2 Züge; Untote nehmen +1 |
| Bleeding | Blutstropfen | Dunkelrot | Tropfspur bei Bewegung | 2 Schaden/Zug bis geheilt; Skelette, Geister, Maschinen immun |
| Stunned | Spirale | Weiß | Figur schwankt, kein Idle | nächster Zug entfällt |
| Slowed | Kette | Grau | Schlamm/Ranken an den Füßen | MoveRange halbiert (abgerundet, min. 1) |
| Hasted | Flügel | Hellblau | Bewegungsschlieren | Initiative +3 |
| Shielded | Schild | Blau | durchscheinende Kuppel | absorbiert Wert, bevor HP sinken |
| Enhanced | Pfeil hoch | Rot | Waffe glüht | +25 % Schaden |
| Cursed | Auge | Violett | dunkler Schleier | −25 % Schaden |
| Regeneration | Blatt | Hellgrün | aufsteigende Partikel | +Wert HP zu Zugbeginn |
| Marked | Fadenkreuz | Rot | Zielkreis am Boden | nimmt +25 % Schaden |
| Confused | Fragezeichen-Spirale | Gelb | Kopf dreht sich | nächste Bewegung zufällige Richtung |

**Gegensätze heben sich auf:** Hasted ↔ Slowed, Enhanced ↔ Cursed. Neu angewendeter Gegen-Status entfernt den alten, statt sich zu stapeln – vermeidet Rechen-Chaos und Icon-Wust.

### Schadensvorschau

Bei Hover über ein Ziel im Angriffsmodus:

1. **Ghost-Segmente:** HP-Segmente, die verloren gehen, blinken. Wird die Einheit sterben → Totenkopf-Icon.
2. **Effektivitäts-Pfeil** zwischen Angreifer und Ziel, gefärbt nach Power-Defense-Matrix:

| Multiplikator | Darstellung |
|-|-|
| ≥ 125 % | Grün, doppelter Pfeil („effektiv") |
| 100 % | Weiß, einfacher Pfeil |
| 50–75 % | Gelb, gestrichelt („resistent") |
| ≤ 25 % | Orange, gestrichelt |
| 0 % | Durchgestrichenes Schild („immun") |

3. **Konter-Hinweis:** Wenn das Ziel `CanCounter` hat und überlebt → kleines Gegenpfeil-Icon mit erwartetem Rückschaden.
4. **Leichen-Hinweis:** Würde der Angriff töten → Icon der resultierenden Leichen-Qualität (siehe unten). Macht die ökonomische Entscheidung „wer tötet wen" sichtbar.

### VFX-Farbcode nach PowerType

Spieler lernen Schadenstypen über Farbe und Form. Gilt für Treffer-Effekte, Projektile und Schadenszahlen.

| PowerType | Farbe | Effekt-Form |
|-|-|-|
| Pierce | Stahlweiß | kurze Funkenlinie |
| Blunt | Staubbraun | runde Schockwelle am Boden |
| Rend | Dunkelrot | drei Kratzlinien |
| Siege | Steingrau | Splitter + Staubwolke |
| Fire | Orange | Flammenzungen, Glut |
| Poison | Gelbgrün | blubbernde Tropfen |
| Arcane | Violett | geometrische Runenkreise |
| Soul | Kaltes Blauweiß | gesogene Partikel *zum Angreifer hin* |
| Holy | Gold | Lichtstrahl von oben |
| Chaos | Magenta, flackernd | wechselnde Farben, Glitch |
| Heal | Hellgrün | aufsteigende Partikel |

Schadenszahlen erscheinen in derselben Farbe; Schwäche-Treffer größer, Resistenz-Treffer kleiner.

### Zustands-Darstellung

`E_UnitVisualState` an der Einheit:
```
enum UnitVisualState { Normal, Hidden, Suspicious, Detected, Spectral, Leaderless, Wounded, Dying }
```

| Zustand | Darstellung |
|-|-|
| **Hidden** (Stealth, unentdeckt) | Eigene Einheiten: leicht transparent, dunkler Rauchsaum am Sockel. Feinde sehen sie nicht. |
| **Suspicious** (Stealth, Geräusch/Geruch bemerkt) | Gelbes **„?"** über dem *bemerkenden* Gegner, Linie zur Quelle |
| **Detected** | Rotes **„!"** über dem Gegner, kurzer Kamera-Zoom → Kampfbeginn |
| **Sichtkegel** (Stealth-Phase) | Bodendecal vor jedem Gegner: 90°-Kegel in SightRange, halbtransparent. Hör-/Geruchsradius als gestrichelte Kreise bei Hover |
| **Spectral** (`IsSpectral`) | Fresnel-Rand, halbtransparent, kein Schattenwurf, leichtes Flimmern |
| **Fliegend** (`IsFlying`) | Figur schwebt ~80 cm über dem Hex, runder Bodenschatten markiert das belegte Feld |
| **Leaderless** (Anführer gefallen) | Gebrochenes-Banner-Icon, Idle-Animation unruhig |
| **Wounded** (< 50 % HP) | Humpel-/Schwanke-Idle, Untote verlieren Knochensplitter-Partikel, Lebende bluten |
| **Dying** (< 20 % HP) | zusätzlich Sockel flackert |

### Tod und Leichen-Qualität

Tote Gegner bleiben als **Leichen-Objekt** auf dem Hex liegen (bis zum Ernte-Ritual am Kampfende). Das Modell richtet sich nach dem tödlichen PowerType:

| PowerType des Todesstoßes | Leichen-Look | Icon |
|-|-|-|
| Pierce | intakt | volle Knochenhand |
| Blunt | zerschmettert | angeknackste Hand |
| Rend | zerrissen, Teile verstreut | halbe Hand |
| Fire | verkohlt, glimmend | schwarze Hand |
| Poison | grünlich verdorben | grüne Hand |
| Soul | intakt + Seelen-Funke schwebt darüber | Hand + Flamme |

Bei Hover über eine Leiche: Qualität in Prozent. **Ergebnis:** Der Spieler sieht während des Kampfes, wie viel Beute er gerade „verdirbt".

### Animations-Lesbarkeit

- **Antizipation:** Jeder Angriff hat 0,2–0,3 s Ausholbewegung. Fernkämpfer zielen sichtbar.
- **Treffer-Reaktion:** HitAnim + kurzer Weiß-Blitz am Mesh (0,1 s).
- **Idle mit Charakter:** Skelette klappern, Ghule schnüffeln, Geister driften. Idle zeigt Rolle und Wesen.
- **WalkAnim:** Kippel-Bewegung (bestehend) bleibt; Hex-zu-Hex-Bewegung mit kurzem Stopp pro Feld, damit Weglänge zählbar ist.
- **Aktive Fähigkeit:** Vor Ausführung 0,5 s Einblendung des Fähigkeitsnamens über der Einheit.

### Token-Modus (Strategie-Zoom)

Ab einer Kamera-Distanz (z.B. wenn ein Hex < 40 px auf dem Bildschirm groß ist) werden Modelle durch **aufrechte Tokens** ersetzt: Wappenschild in Fraktionsfarbe mit Rollen-Icon, Größe nach `Size`. Look: bemalte Zinnfigur / Spielmarke. Vorteile: Übersicht bei 16x16-Belagerungen, Performance, und es passt zur „Kriegsrat"-Fantasie des Lichs.

### Datenmodell: S_UnitVisual / DT_UnitVisuals

Eigene Tabelle mit **denselben Zeilennamen wie `DT_Units`** (Zeile „Ghoul" in beiden Tabellen):

```
struct S_UnitVisual {
    // Modell
    Model             : string   // Pfad zur .glb; leer = Platzhalter-Grundform nach Rolle
    MaterialOverride  : string?  // leer = Fraktions-Standard
    ScaleOverride     : float    // 0 = aus Size berechnen

    // Lesbarkeit
    RoleIcon          : string   // Bild, auch für Token-Modus
    Portrait          : string   // Initiative-Leiste, Dialog
    TokenTexture      : string
    HoverHeightCm     : float    // > 0 bei Fliegern

    // Animationen (Namen im glTF)
    IdleAnim, WalkAnim, AttackAnim, HitAnim, DeathAnim : string
    IdleWoundedAnim   : string?

    // Effekte & Sound
    ImpactVFXOverride : string?  // leer = Standard des PowerType
    SoundSet          : string
}
```

Fraktions-Paletten liegen zentral in `DT_FactionPalettes` (Faction → Primär, Akzent, Leuchten). Ein gemeinsames Einheiten-Material liest diese als Parameter – neue Fraktion = eine Tabellenzeile, kein neues Material.

### Lesbare Platzhalter (Phase 1–2)

Statt grauer Würfel:
- **Körper** aus Grundformen nach Rollen-Silhouette (Kapsel = Melee, Zylinder hoch = Caster, Quader flach = Siege, Kegel = Scout)
- **Höhe** nach `Size`-Tabelle
- **Material:** Einheiten-Material mit Fraktions-Primärfarbe
- **Rollen-Icon** als Billboard über dem Kopf
- **Sockel** bereits final

Aufwand: < 1 Tag. Nutzen: Taktik ist ab dem ersten Prototyp beurteilbar.

### Lesbarkeits-Checkliste (pro neuer Einheit)

Das **Einheitenbuch** (Artifact, Quelle `prototypes/einheitenbuch/template.html` + `tools/build_gallery.py`) macht die Prüfungen 1, 2, 4 und 5 per Schalter direkt auf einem Hex-Feld mit echten Begegnungen sichtbar. Figuren dort sind Regel-Platzhalter: gezeichnet nur aus Rolle, Größe, Fraktion und Rang.

1. Graustufen-Screenshot auf Standard-Zoom: Rolle erkennbar?
2. Unscharf-Filter (Gauss 4 px): Fraktion erkennbar?
3. Neben 3 anderen Einheiten derselben Fraktion: unterscheidbar?
4. Nachts und im Nebel: Sockel und Leuchten sichtbar?
5. Token-Modus: Icon eindeutig?
6. Höchster Punkt = Rollen-Merkmal?

### Einheiten-Steckbriefe (erste 10 Modelle)

| Einheit | Fraktion / Rolle / Size | Silhouette & Erkennungsmerkmal | Leuchten / VFX | Idle |
|-|-|-|-|-|
| **Lich** | Undead / Commander / 2 | Hager, hoher Kragen, Knochenkrone, Stab mit Phylakterium-Splitter als höchster Punkt | Grüne Augen + Stab-Kristall, Soul-Partikel | Schwebt minimal, Umhang weht ohne Wind |
| **Skelett** | Undead / Melee / 1 | Schmal, Rundschild, kurzer Speer, gebückt | Schwaches Augenglimmen | Kiefer klappert, Kopf ruckt |
| **Ghul** | Undead / Melee / 2 | Vierbeinig-geduckt, lange Krallen nach vorn, Buckel | Kein Leuchten (fleischlich), Rend-Kratzer | Schnüffelt am Boden |
| **Todesritter** | Undead / Tank / 2 | Massive Platte, Turmschild, Bidenhänder über Schulter | Grüne Visierschlitze | Steht stoisch, Rauch aus Rüstungsfugen |
| **Geist** | Undead / Scout / 1 | Verwehtes Leichentuch, keine Beine, nach vorn geneigt | Blauweiß, Fresnel, kein Schatten | Driftet, Saum löst sich auf |
| **Balliste** | Undead / Siege / 3 | Horizontaler Bogenarm, Knochen-Sehnen, Schädel als Gegengewicht | Grüne Sehnen glimmen beim Spannen | Knarrt, Arm zuckt |
| **Bauer / Bürgerwehr** | Hanse / Melee / 2 | Mistgabel oder Dreschflegel über Kopf, rot-weißer Wappenrock | – | Tritt unruhig auf der Stelle |
| **Kleriker** | Clergy / Support / 2 | Kutte, Weihrauchfass an Kette, Buch | Goldener Schimmer, Holy-Strahlen | Schwenkt Weihrauchfass |
| **Hexe** | Witches / Caster / 2 | Gebeugt, Kräuterbündel-Stab überragt Kopf, Kapuze | Violettes Licht an Stabspitze | Murmelt, Hand kreist |
| **Druide** | Witches / Support / 2 | Lang, Geweih-Kopfschmuck als höchster Punkt, Mistelkranz | Bernsteinfarbene Runen | Stützt sich auf Stab, Raben-Partikel |

### Einheiten-Steckbriefe: Heide-Gegner (Region 1)

Die ersten Gegner der Kampagne. Decken alle vier Fraktionen der Heide ab und zusammen alle Rollen, die der Spieler früh lesen lernen muss.

#### Optik und Rolle

| Einheit | Fraktion / Rolle / Size | Silhouette & Erkennungsmerkmal | Leuchten / VFX | Idle |
|-|-|-|-|-|
| **Moorgeist** | HeathSpirits / Tank / 3 | Breiter, tropfender Torfkörper ohne Beine, wächst aus dem Boden; überlange Arme mit Wurzelfingern | Fahle Augen, Sumpfgas-Blasen am Sockel | Sinkt leicht ein und steigt wieder auf, Schlamm tropft |
| **Irrlicht** | HeathSpirits / Scout / 1 | Kein Körper: schwebende Lichtkugel mit kurzem Schweif | Blassgelb, pulsiert, wirft als einzige Einheit eigenes Licht auf den Boden | Zieht kleine Kreise, flackert aus und wieder an |
| **Heideschwester** | Clergy / Support / 2 | Schlanke Nonne, Weidenkorb mit Kräutern, Laterne an Stange als höchster Punkt | Warmes Kerzengold aus Laterne, Holy-Strahl beim Heilen | Gießt Weihwasser, betet |
| **Hügelgrab-Druidin** | Witches / Caster / 2 | Gebeugt, Rentiergeweih-Haube, Stab aus Mooreiche mit Bronzescheibe an der Spitze | Bernstein-Runen an der Scheibe, Erd-Partikel | Klopft mit Stab, Runen glimmen nacheinander auf |
| **Lüneburger Armbrustschütze** | Hanse / Ranged / 2 | Gerader Rücken, Setzschild (Pavese) mit rot-weißem Wappen hinter sich, Armbrust waagrecht | – (lebend, kein Leuchten) | Spannt Armbrust mit Kurbel, späht |

#### Werte (erster Vorschlag)

| Stat | Moorgeist | Irrlicht | Heideschwester | Hügelgrab-Druidin | Armbrustschütze |
|-|-|-|-|-|-|
| Rank | Warrior | CannonFodder | Warrior | Warrior | CannonFodder |
| HP | 30 | 6 | 14 | 16 | 15 |
| MaxEnergy | 2 | 0 | 4 | 5 | 0 |
| Initiative | 3 | 9 | 5 | 6 | 4 |
| MoveRange | 2 | 5 | 3 | 3 | 3 |
| AttackDamage | 8 | 3 | 4 | 7 | 9 |
| AttackRange | 1 | 1 | 2 | 4 | 5 |
| PowerType | Blunt | Arcane | Holy | Arcane | Pierce |
| AttacksPerTurn | 1 | 1 | 1 | 1 | 1 |
| CanCounter | true | false | false | false | false |
| DefenseType | Unarmored | Unarmored | Light | Light | Medium |
| MagicResist | 3 | 6 | 4 | 5 | 1 |
| SoulShield | 2 | 4 | 6 | 3 | 0 |
| SightRange | 3 | 6 | 4 | 4 | 6 |
| HearRadius | 4 | 3 | 3 | 3 | 3 |
| SmellRadius | 2 | 0 | 2 | 4 | 2 |
| NoiseLevel | 2 | 0 | 1 | 1 | 2 |
| ScentLevel | 3 | 0 | 1 | 2 | 2 |
| Size | 3 | 1 | 2 | 2 | 2 |
| IsSpectral | false | true | false | false | false |
| IsFlying | false | true | false | false | false |

#### Fähigkeiten

| Einheit | Fähigkeit | Typ | Wirkung |
|-|-|-|-|
| Moorgeist | **Moorgriff** | Active, 2 Energie | Ziel im Nahkampf erhält `Slowed` (2 Züge); auf Mud/Swamp/Bog zusätzlich `Stunned` (1 Zug) |
| Moorgeist | **Aus dem Torf** | Passive | Auf Mud/Swamp/Bog zu Zugbeginn `Shielded` (absorbiert 4 Schaden) |
| Irrlicht | **Verwirrung** | Passive | Feinde auf Nachbarfeldern bewegen sich in zufällige Richtung (bestehende Idee) |
| Irrlicht | **Falsches Licht** | OnDeath | Erzeugt 1 Runde lang ein Trugbild auf dem Feld, das Angriffe auf sich zieht |
| Heideschwester | **Weihwasser** | Active, 2 Energie | Heilt Verbündeten in Reichweite 2 um 6 HP |
| Heideschwester | **Geweihter Boden** | Active, 3 Energie | Macht Radius 1 für 3 Runden zu `HolyGround` (Schaden pro Runde für Untote) |
| Hügelgrab-Druidin | **Grabesruhe** | Active, 3 Energie | Ziel-Untoter erhält `Cursed` (−25 % Schaden, 2 Züge). Thematisch: Sie bindet die Toten, die *sie* bewacht |
| Hügelgrab-Druidin | **Erdbindung** | Active, 2 Energie | Ein Feld wird für 2 Runden unpassierbar (Erdwall, Kante `Cover` ringsum) |
| Armbrustschütze | **Setzschild** | Passive | Wenn nicht bewegt: Kante zur Angriffsrichtung zählt als `Cover` |

#### Taktische Rolle in der Heide

- **Moorgeist + Irrlicht** = Moor-Kombi: Irrlicht verwirrt, Moorgeist hält fest. Spieler lernt: erst die schnelle Lichtkugel ausschalten.
- **Heideschwester** = erstes Prioritätsziel. Heilt und erzeugt heiligen Boden – zeigt früh, warum christliche Knoten gefährlich für Untote sind.
- **Hügelgrab-Druidin** = Gelände-Manipulatorin. Lehrt, dass Felder sich während des Kampfes ändern.
- **Armbrustschütze** = einfacher, ehrlicher Fernkämpfer. Lehrt Deckung und Annäherung.

#### Untote Versionen (Mythologie-Wissen)

| Original | Untote Version | Optik-Änderung | Fähigkeits-Änderung |
|-|-|-|-|
| Moorgeist | **Moorleiche** | Torf wird zu gegerbter Haut, grüne Augen | Moorgriff bleibt, heilt sich auf Bog |
| Irrlicht | **Totenlicht** | Gelb → nekrotisches Grün | Verwirrung trifft jetzt Lebende stärker (+1 Feld Radius) |
| Heideschwester | **Gefallene Schwester** | Kutte zerrissen, Laterne erloschen, grünes Glimmen darin | Holy → Soul; Weihwasser wird „Grabwasser" (heilt Untote) |
| Hügelgrab-Druidin | **Grabdruidin** | Geweih bleibt, Haut mumifiziert | Grabesruhe trifft jetzt Lebende (−25 % Schaden) |
| Armbrustschütze | **Knochenschütze** | Skelett mit zerbrochenem Wappen-Setzschild | Unverändert, aber kein Moralverlust bei Anführer-Tod |

Alle fünf plus der **Totenjäger** (Belohnung des Wode) stehen mit Werten in der Gesamtübersicht und in `DT_Units.csv`; wo sie produziert werden, steht im Kapitel Heide-Kampagne. Ihre Kampfwerte liegen unter denen der Grundeinheiten, weil die Rechnung ihre Fähigkeiten (Heilung, Verwirrung) nicht mitzählt.

### Portrait-Prompts

Basis-Prompt bleibt (siehe Story- und UI-Konzept). Zusatz pro Rolle, damit Portrait und Modell dieselbe Sprache sprechen:

| Rolle | Prompt-Zusatz |
|-|-|
| Melee | `aggressive forward pose, close-up weapon, low camera angle` |
| Tank | `frontal stance, large shield, heavy armor filling the frame` |
| Ranged | `profile view, drawn bow or spear, long diagonal line` |
| Caster | `glowing staff tip above head, hands casting, upward light` |
| Support | `holding vessel or book, soft rim light, calm expression` |
| Commander | `banner or crown in frame, slightly from below, regal` |

Fraktions-Leuchtfarbe im Prompt nennen (z.B. `sickly green glowing eyes` für Undead), damit Portraits zur Spielfigur passen.

---

## Weltkarte (Landschaft)

**Entscheidungen 02.11.2026:**
- Die Kampagnenkarte ist keine Hex-Welt mehr, sondern eine durchgehende 3D-Landschaft. Kämpfe laufen in **instanzierten Hex-Schlachtfeldern** – die Hex-Welt war nur nötig, solange Kämpfe auf der Weltkarte selbst stattfinden sollten.
- Umsetzung **im Browser mit WebGL2, ohne Engine**. Prototyp: Artifact „MythosTactics Weltkarte“ (Quelle `prototypes/worldmap/index.html`).

### Was sich gegenüber der bisherigen Hex-Welt ändert

| Bisherige Hex-Welt | Neue Weltkarte |
|-|-|
| Ein Hex-Tile pro Pixel der Höhenkarte, 257 × 257 Tiles um die Kamera | **Ein Vertex pro Höhenpunkt** in einem Gitter, das der Kamera folgt |
| Feste Größe (`stream_radius` 128) – bei maximalem Zoom sieht man über den Rand | Gittergröße aus dem **tatsächlich sichtbaren Boden** (Bildschirmecken auf den Boden projiziert) plus 15 % Rand |
| Feste Auflösung | **Vertex-Abstand passt sich dem Zoom an:** 1, 2, 4 … 256 Höhenpunkte |
| Pixel in Grad: Karte ~1,65-fach in die Breite gezogen | Projektion ETRS89 / UTM 32N – Längen und Flächen stimmen |
| 8 Bit, ab 450 m gekappt (Harz als Plateau) | 16 Bit, −100 bis 1200 m |
| Ein Material pro Tile | **Bodentyp pro Höhenpunkt**, Textur strahlt kreisförmig aus und wird zum Rand durchsichtig – Überlappungen ergeben die Übergänge |
| Orte als Tile (Q, R) | Orte als Breite/Länge, Kartenposition berechnet |

### Kennwerte

Generiert aus `worldmap.py`. Welt-Einheit im Browser = **1 Höhenpunkt** (≈ 247 m); Höhe = Meter ÷ 247 × Überhöhung.

<!--GEN:WORLDMAP:BEGIN-->
| Kennwert | Wert |
|-|-|
| Projektion | ETRS89 / UTM 32N (EPSG:25832) |
| Ausdehnung real | 498 × 452 km |
| Höhenkarte | 2017 × 1828 Höhenpunkte, 16 Bit, -100 bis 1200 m |
| Gelände pro Höhenpunkt | 247.1 m |
| Meeresspiegel | 0 m (16-Bit-Wert 5041) |
| Gitter im Browser | 257 × 257 Vertices, Abstand 1–256 Höhenpunkte je nach Zoom |
<!--GEN:WORLDMAP:END-->

### Wie das Gelände entsteht (Renderer)

1. **Ein Gitter** aus 257 × 257 Vertices wird einmal angelegt und nie neu gebaut. Pro Bild bekommt es nur zwei Werte: Ursprung und Vertex-Abstand.
2. **Sichtbereich:** Die vier Bildschirmecken (und Kantenmitten) werden als Strahlen auf die Bodenebene geworfen. Der weiteste Treffer bestimmt den Radius; ×1,15 + Rand ergibt die halbe Gitterbreite. Strahlen über dem Horizont werden bei 6 × Kameraabstand gekappt, dort deckt Dunst ab.
3. **Vertex-Abstand** = kleinste Zweierpotenz, bei der 256 Quads die Breite abdecken. Nah: 1 Höhenpunkt (247 m), ganze Karte: 32 (7,9 km).
4. **Einrasten:** Der Ursprung rastet auf Vielfache des doppelten Abstands ein – das Gitter springt nur in ganzen Schritten, das Gelände „schwimmt“ beim Verschieben nicht.
5. **Höhen** liest der Vertex-Shader aus einer Float-Textur mit eigener Mittelwert-Mip-Kette. Bei Abstand 8 liest er Mip-Stufe 3 – grobe Gitter mitteln, statt einzelne Spitzen zu treffen oder zu verfehlen.
6. **Außerhalb der Karte** wird die Randhöhe fortgesetzt und dunkel eingefärbt (keine Abbruchkante). Bereiche ohne Höhendaten sind markiert und werden ebenso dunkel gezeigt statt erfunden.

### Bodentexturen und Übergänge

- **Bodentyp pro Höhenpunkt** (8 Bit, gleiches Raster wie die Höhe). Typen und Texturen kommen aus der Textur-Sammlung (`Textures/Tiles`, dieselben wie für die Schlachtfeld-Tiles), auf 512 px verkleinert:

| ID | Textur | Bedeutung auf der Karte |
|-|-|-|
| 0 | Sand | Küste, Dünen, Watt, Meeresgrund |
| 1 | WetEarth | Marsch, Flussauen |
| 2 | GrassShort | Wiese, Weide |
| 3 | DryEarth | Acker (Börde) |
| 4 | Heather | Heide |
| 5 | Bog | Hochmoor |
| 6 | Swamp | Bruch, Niedermoor |
| 7 | GrassTall | Wald, Dickicht (Platzhalter – eigene Waldtextur fehlt) |
| 8 | RawStone | Fels; zusätzlich automatisch an Steilhängen |
| 9 | Mud | Schlick im Flachwasser |
| 255 | – | keine Daten (Kartenrand) |

- **Überblendung (Fragment-Shader):** Für jeden Bildpunkt werden die 3 × 3 nächsten Höhenpunkte betrachtet. Jeder trägt seine Textur mit einem Gewicht bei, das vom Mittelpunkt zum Rand des Radius weich auf 0 fällt. Die Summe wird normiert. Wo sich Kreise verschiedener Typen überlagern, entsteht der Übergang.
- **Unregelmäßige Ränder:** Rauschen verschiebt die Abtastposition leicht – sonst sieht man die runden Kreise der Höhenpunkte.
- **Ferne:** Werden Höhenpunkte kleiner als ein Bildschirmpixel, wird statt der Texturen eine Farbkarte (Durchschnittsfarbe je Typ, mit Mipmaps) gezeigt – kein Flimmern, weniger Rechenaufwand.
- **Stil:** Gelände leicht entsättigt; gesättigte Farben gehören Einheiten und Markern.
- **Wasser:** eigene Fläche auf Meereshöhe, Tiefe aus der Höhenkarte (bilinear → weiche Küstenlinie), Transparenz nach Tiefe, Wasser- und Normal-Textur aus der Textur-Sammlung.

### Daten-Pipeline

| Schritt | Werkzeug | Ergebnis |
|-|-|-|
| 1. Höhenmodell (WGS84, GeoTIFF, mit Rand) besorgen | z. B. SRTM15+ über OpenTopography | `dem_wgs84.tif` |
| 2. Ins Kartenraster bringen | `python worldmap.py` → `build_heightmap.bat` in der OSGeo4W-Shell von QGIS | `dem_utm32.tif` (2017 × 1828, Float32) |
| 3. Browser-Daten bauen | `python build_webmap.py --dem dem_utm32.tif` (liest die Textur-Sammlung nur, schreibt nichts hinein) | `prototypes/worldmap/worldmap/terrain.png` (R/G = Höhe 16 Bit, B = Bodentyp), Texturen, `map.json` |

**Aktueller Stand des Prototyps:** Ohne `--dem` rechnet `build_webmap.py` die alte 8-Bit-Höhenkarte (`Maps/Heightmap.png`) ins neue Raster um – deshalb ist der Harz noch ein Plateau bei 450 m, und die Ecken ohne alte Daten sind dunkel. Die **Bodentypen sind eine Platzhalter-Heuristik** (Höhe, Hangneigung, Rauschen, Heide um Wilsede, Börde im Süden).

**Echte Bodentypen später:** CORINE Land Cover in QGIS auf die IDs oben umklassifizieren, mit demselben `gdalwarp`-Ausschnitt (Resampling `mode`) ins Raster bringen, historisch anpassen (moderne Städte, Forste, entwässerte Moore zurück zu Heide und Moor; Vorlage: Kurhannoversche Landesaufnahme, 18. Jh.). `build_webmap.py` bekommt dafür einen Eingang `--landcover`.

### Bewegung auf der Karte

- **Knoten** = Orte und Begegnungen, gesetzt über ihre Kartenposition (`DT_Encounters`: `Lat`, `Lon` → Pixel).
- **Wege** = Graph aus Linien zwischen Knoten. Reisedauer = Weglänge × Geländefaktor des überwiegenden Bodentyps (Moor langsam, Heide normal, Wege schnell).
- **Ley-Teleport** springt zwischen aktivierten Ley-Knoten, ohne den Wege-Graphen.

### Verbindung zum Schlachtfeld

Schlachtfelder sind instanziert, aber **ortsgebunden**: Beim Kampfstart zählt die Kampagne die Bodentypen im Umkreis des Knotens (z. B. 60 % Moor, 30 % Heide, 10 % Wald) und übergibt sie als Bodenmix an den Schlachtfeld-Generator. Ein Kampf im Pietzmoor ist so auch auf dem Hex-Feld ein Moor. Die Zuordnung Kartentyp → FloorType ist naheliegend (Heather → Heather, Bog → Bog usw.), weil beide dieselben Texturen nutzen.

**Schnittstelle Kampagne → Kampf** bekommt dafür `GroundMix` (Bodentyp → Anteil) und `TimeOfDay`.

### Nächste Schritte

1. Echtes Höhenmodell einspielen (Schritte 1–3) – behebt Harz-Plateau und dunkle Ecken
2. Landbedeckung statt Heuristik; eigene Waldtextur
3. Wege-Graph und Reise, Knoten anklickbar
4. Fog of War und Gefahrenskala als Maske im Gelände-Shader
5. Flüsse als Linien (Gewässerdaten) – das Flussnetz ist auch Spielmechanik
6. Optional: zweiter, gröberer Gitterring für sehr flache Kamerawinkel (Clipmap), falls der Horizont zu grob wirkt

---

## Tile-System (Schlachtfelder)

*Seit 02.11.2026 gilt das Hex-Tile-System **nur noch für die instanzierten Schlachtfelder**. Die Kampagnenkarte ist eine Landschaft (siehe Weltkarte).*

### Hex-Grid Koordinatensystem

- **Axial-Koordinaten** (Q, R) für Flat-Top Hexagone
- Ursprung bei (0,0) unten links, alle Koordinaten positiv (0 bis Width-1, 0 bis Height-1)
- Distanzformel: `max(|ΔQ|, |ΔR|, |ΔQ+ΔR|)`
- Effiziente Reichweiten-Eingrenzung: erst rechteckiger Bereich (max Q±range, R±range), dann Hex-Distanz, dann ggf. Kegelfilter
- Schlachtfeldgrößen variabel je nach Knotentyp (12x12 Dorf, 16x16 Hansestadt, 20x20+ Belagerung)

### HexToWorld Formel (Flat-Top)

```
X = Q * HexSize * 1.5
Y = R * HexSize * sqrt(3) + (Q ungerade ? HexSize * sqrt(3) * 0.5 : 0)
```

**Wichtig:** Q-Offset (0.866) wird nur in Y addiert wenn Q ungerade ist (per Modulo 2). Nicht in X.

### Enums

*(Pseudo-Code.)*

**FloorType** (28 Werte):

```
enum FloorType {
    // Natural
    DryEarth, WetEarth, GrassShort, GrassTall, Heather,
    Sand, Mud, Swamp, Bog, Ice, RawStone, Gravel,
    // Water
    ShallowWater, DeepWater, PoisonousSwamp,
    // Fortified / paved
    Cobblestone, Sandstone, WoodDeck, ClayFloor, Straw,
    // Sacred
    HolyGround, DesecratedGround, PaganGround, RuneGround, GraveyardGround,
    // Interior
    StoneFloor, WoodFloor, CellarFloor
}
```

*Entfernt gegenüber früherem Entwurf: Snow, WoodPlanks, Ash, BloodSoakedEarth, SealedGround.*

**EdgeType:**

```
enum EdgeType {
    Open,             // passable, free sight
    Cover,            // blocks movement, partial sight (shoot over)
    Wall,             // blocks movement and sight
    WallDestructible, // like Wall, but can be torn down by special units
    WallTransparent   // blocks movement, free sight (e.g. window)
}
```

**Zerstörbare Wände (WallDestructible):**
- Effektiv 1 HP, aber durch Fähigkeits-Gate geschützt: nur Einheiten mit passender Fähigkeit (Riese, Katapult o.ä.) können sie einreißen, dann sofort.
- Kein HP-Zähler nötig – nur der Enum-Typ plus ein temporärer "zerstört"-Zustand.
- **Heilung über Zeit:** Zerstörung wird in einer dynamischen Schicht gespeichert (z.B. `{ Koordinate+Kante: Zerstörungstag }`). Nach einem (noch zu definierenden) Zeitraum gilt die Wand wieder als heil, der Eintrag wird verworfen. Lazy-Auswertung beim Laden statt aktivem Reparatur-Timer.
- Statische Karte sagt "hier ist eine zerstörbare Wand" (Enum), dynamische Schicht sagt "gerade kaputt seit Tag Y". Beide Schichten getrennt halten.

**TriggerType** (wann eine Fähigkeit auslöst):
```
enum TriggerType {
    Active, OnDamageTaken, OnDamageDealt, OnDeath,
    OnAllyDeath, OnTurnStart, OnTurnEnd, Passive
}
```

**StatusEffect:**
```
enum StatusEffect {
    None,
    Poisoned, Burning, Bleeding, Stunned, Slowed, Hasted,
    Shielded, Enhanced, Cursed, Regeneration, Marked,
    Confused     // neu: Bewegung in zufällige Richtung (Irrlicht)
}
```

**Ability:** Kein Enum mehr – Fähigkeiten sind Zeilen in `DT_Abilities` (siehe Einheiten-Datenstruktur → Fähigkeiten).

**AreaPattern** (Form des Wirkungsbereichs auf dem Hex-Grid):
```
enum AreaPattern { SinglePoint, Radius, Ring, Cone, Line, VShape }
```

**EffectType** (was eine Fähigkeit/ein Effekt bewirkt):
```
enum EffectType { Damage, Heal, ApplyStatus, Stun, Push, Teleport, Summon, ModifyTerrain }
```

**TargetType:**
```
enum TargetType { Self, Ally, Enemy, AllAllies, AllEnemies, Ground }
```

**Faction:**
```
enum Faction {
    Undead,      // der Lich (Spieler)
    Hanse,       // freie Handelsstädte (weltlich)
    Guelphs,     // Welfen-Dynastie (weltlich)
    Clergy,      // Klöster, Bischöfe (geistlich)
    Witches,     // Hexenzirkel (heidnisch-magisch)
    WodanCult,   // heidnischer Wodan-Kult (heidnisch-magisch)
    Spreewald,   // Spreewald-Geister (heidnisch-magisch)
    Wattenmeer,  // Wattenmeer-/Küstenmächte (heidnisch-magisch)
    HeathSpirits // Moor- und Heidegeister: Irrlichter, Moorgeister (Naturwesen, Heide)
    // Zukunft: Askanier (Dynastie Brandenburg/Sachsen – weltlich)
}
```
*Paletten pro Fraktion: siehe Einheiten-Visualisierung → Fraktions-Paletten.*

### TileInformation

```
class TileInformation {
    Q, R            : int          // hex coordinates (axial)
    Height          : int          // 0-3 elevation
    FloorType       : FloorType
    Object          : ref MapObject?   // null = empty
    OccupyingUnit   : ref Unit?        // null = empty
    Corpse          : ref Corpse?      // null = keine Leiche (neu, für Leichen-Qualität)
    Highlight       : HighlightState   // UI feedback, one per tile
    Edges           : Array<EdgeType>  // fixed order: 0=N,1=NE,2=SE,3=S,4=SW,5=NW
}
```

**Highlight** ist UI-Feedback (HighlightState-Enum: None/Movement/Attack/Selected/Path), kein bool. Konkrete Farben erst beim Rendern, nicht im Datenmodell.

**Corpse** belegt das Tile nicht (begehbar), wird aber für Ernte und Hover-Info gebraucht.

**Wahrnehmung (Sicht/Hören/Geruch) NICHT am Tile speichern.** Eine Einheit erzeugt Wahrnehmung (Blickrichtung + Sichtkegel + Sinnesradien); welche Tiles sie wahrnimmt, wird aus Position + Richtung + SightRange/HearRadius/SmellRadius berechnet. Liegt an der Einheit, nicht am Tile – löst Überlappung mehrerer Einheiten automatisch und vermeidet ständiges Zurücksetzen von Tile-Zuständen.

**Edges als Array** (statt 6 benannte Felder) mit fester Richtungsreihenfolge – Index passt zu Nachbar-Offset gleicher Richtung, gut für Pathfinding-Iteration.

### Asymmetrische Kanten

Jedes Tile definiert seine 6 Kanten unabhängig. Eine Kante kann von zwei Seiten unterschiedliche Eigenschaften haben (z.B. Schießscharte: innen Open, außen Wall). Beim Auslesen beide Kanten prüfen, restriktivere gewinnt für Bewegung.

### MapObject

Geländebelegende Objekte wie Häuser, Türme, Ruinen.

```
class MapObject {
    ObjectName : string
    Footprint  : Array<TileModification>
    VisualMesh : Mesh           // pivot at anchor tile (bottom-left)
}
```

**Wichtig:** Wenn `Object != null` auf einem Tile, überschreibt das Object die FloorType-Werte (MoveCost, Edges etc.). Man tritt nicht in den Sumpf, wenn man im Haus läuft.

### TileModification

Pro Tile, das ein MapObject belegt:

```
struct TileModification {
    RelativeOffset    : (int, int)   // (deltaQ, deltaR) from anchor tile
    OverrideFloorType : FloorType?   // null = leave unchanged
    Height            : int
    MoveCost          : float
    AreaEffectType    : PowerType
    AreaEffectValue   : int
    EdgeN, EdgeNE, EdgeSE,
    EdgeS, EdgeSW, EdgeNW : EdgeType
}
```

Objekte tragen ihren Footprint selbst. Beim Platzieren werden alle betroffenen Tiles automatisch modifiziert. Notwendig für prozedurale Karten-Generierung. Anker = untere linke belegte Hex (x00). Offsets werden axial auf die Anker-Koordinate addiert; bei axialen Koordinaten gibt es keine Versatz-Asymmetrie zwischen geraden/ungeraden Spalten.

**Hinweis Hex-Layout:** Ein "2x3" Haus belegt auf einem Hex-Grid 7 Tiles, nicht 6, wegen versetzter Spalten.

### Tile-Bauplan (Visuals)

Pro FloorType zwei Meshes:
- **Basis-Mesh:** Bodenplatte (Stein, Erde, Gras-Textur)
- **Deko-Mesh:** Vegetation, Steine, Halme

Wenn ein MapObject auf dem Tile steht, wird nur Basis-Mesh gespawnt, Deko weggelassen.

**Deko-Höhe begrenzen:** Gras/Heidekraut-Deko max. 30 cm hoch, damit Sockel und Füße von Size-1-Einheiten nicht verdeckt werden. Ausnahme: GrassTall und Schilf (gewollte Sichtblockade, dann Sockel-Rand über die Deko gerendert).

### Rendering: Instanzierung

Bei 256+ Tiles ist ein eigenes Objekt pro Tile zu teuer. Stattdessen **ein instanziertes Mesh pro FloorType** (Basis) und eines pro Deko-Art; jedes Tile ist eine Instanz mit eigener Position und Drehung. Im Spiel erledigt das `TileRenderer`.

---

## Schlachtfeld-Ankunft & Stealth-Phase

Schlachten beginnen nicht mit "Spieler rechts, Gegner links, kämpft". Der **Ankunftsmodus** prägt die Ausgangslage und ist das Herz des taktischen Beginns.

### Ankunftszustände

| Zustand | Bedeutung |
|-|-|
| **Standard** | Eigene Einheiten kommen am Kartenrand (Weg-Ende), Gegner verteilt auf Positionen |
| **Überraschung (Spieler überrascht Feind)** | Einheiten kommen tiefer ins Feld, Gegner passiv/stehend bis zur Entdeckung |
| **Hinterhalt (Feind überrascht Spieler)** | Gegner in besserer Position, teilweise verdeckt, Spieler mit Einschränkungen im ersten Zug |
| **Vorwarnung** | Gegner alarmiert, in Stellung (Schanzen, Formation), aber Spieler nähert sich regulär |

### Was den Zustand bestimmt

- **Wind-Richtung:** Untote stinken. Gegen den Wind = erkannt, mit dem Wind = versteckt.
- **Armee-Zusammensetzung:** Geister lautlos, Fleischriesen laut/auffällig
- **Tageszeit:** Nacht gibt Stealth-Bonus
- **Anführer-Skills:** z.B. "Schattenmantel" → Stealth-Bonus
- **Gegner-Typ:** Elfen/Waldwesen sensibel, schlafende Bauern einfach zu überraschen
- **Gelände:** offenes Feld vs. dichter Wald / Nebel

Wird **vor dem Kampf** automatisch berechnet. Spieler bekommt Info-Meldung ("Der Wind steht günstig. Bauern schlafen. Überraschung möglich!") und sieht dann das Ergebnis auf dem Feld.

**Windrichtung sichtbar:** Wehender Partikel-Nebel über dem Feld und ein Wind-Pfeil am Bildschirmrand, damit die Geruchs-Mechanik nachvollziehbar bleibt.

### Stealth-relevante Einheiten-Werte

Jede Einheit hat neben Kampf-Werten (HP, Angriff, Bewegung, Initiative) auch **Stealth-Dimensionen**:

- **Größe (`Size`, 1–4):** Skelett = 1, Ghul/Todesritter = 2, Fleischriese = 4 – beeinflusst Sichtbarkeit
- **Lautstärke (`NoiseLevel`, 0–4):** Geräusch-Radius bei Bewegung
- **Geruchsbildung (`ScentLevel`, 0–4):** Wie stark die untote Aura ausströmt (Entdeckungsradius gegen Lebewesen)

Geister sind in allen drei Werten extrem niedrig → Stealth-König. **Ausgleich durch Nachteile an anderer Stelle:** weniger HP, teuer in Seelen (selten), ineffektiv gegen Klöster/geweihte Gegner, viele Terrain-Boni nicht nutzbar.

### Stealth-Phase

Wenn der Zustand es erlaubt, beginnt der Kampf im **Schleich-Modus**:

- Gegner stehen still (keine Patrouillen – bewusste Design-Entscheidung gegen Micromanagement)
- Sichtlinien-basiert: Solange kein Gegner dich sieht, bleibt Stealth aktiv
- **Deckung** blockiert Sicht (Wand-Kanten-Mechanik greift hier direkt)
- **Höhenunterschiede** beeinflussen Sicht (höher = besser sehen, aber auch selbst besser sichtbar)
- **Einheitengröße:** Fleischriese kann sich schwer verstecken → Größensystem bekommt Bedeutung
- **Geräusch-Radien:** Rennen/Nahkampf alarmiert Umgebung, Schleichen nicht

**Darstellung:** siehe Einheiten-Visualisierung → Zustands-Darstellung (Sichtkegel-Decals, „?" / „!"-Stufen, Hidden-Look). Beim Planen eines Zugs zeigt die Pfad-Vorschau Felder, auf denen die Einheit entdeckt würde, rot gestrichelt.

### Übergang zum Rundenkampf: Überraschungsangriff

**Auslöser:** Eine eigene Einheit ist in Angriffsreichweite eines Gegners **und** noch unentdeckt → Spieler kann zuschlagen. Der Angriff selbst startet den Kampf.

Zwei gleichzeitige Effekte bei erfolgreicher Überraschung:

1. **Surprise-Schlag:** Die auslösende Einheit greift an, *bevor* irgendwer anders handelt (Freiangriff)
2. **Initiative-Bonus für alle eigenen Einheiten:** Die Reihenfolge der ersten Kampfrunde ist nach oben verschoben – aber Initiative-Werte einzelner Einheiten zählen weiter mit. Zombies (langsam) profitieren begrenzt, Irrwische (schnell) sind sowieso zuerst dran.

**Taktische Konsequenz:**
- Positionierung in der Stealth-Phase ist entscheidend – möglichst viele Einheiten in Reichweite bringen
- Wahl des Auslösers: schneller Burst-Angriff vs. schwacher Anfangs-Angreifer?
- Langsame Masseneinheiten wie Zombies hinten lassen ist okay – sie kommen später dran, aber sie kommen
- Thematisch stimmig: Schnelle fiese Einheiten nutzen Überraschung, träge Masse schleicht nicht

### Kampfszenen-Beispiele

- **Bauernhof:** Freies Feld, Haus/Scheune als Deckung, Zaun. Bauern am Ochsenkarren. Leicht zu überraschen.
- **Dorf:** Häuser, Gassen, Brunnen. Verstreut. Stealth möglich, aber viele Sichtlinien.
- **Burg/Turm:** Definierte Verteidigungsanlagen, Wachen an festen Positionen. Schwer zu überraschen, später evtl. Belagerung.
- **Hexenzirkel auf Lichtung:** Mystische Gegner, evtl. immun gegen Stealth (*spüren* Untote). Keine Deckung.
- **Moor:** Unsichtbar für beide, aber gefährlich (versinken). Heimspiel für Irrlichter/Moorgeister.
- **Hügelgrab-Ruine:** Innenräume, enge Gänge, Höhenunterschiede, dichte Deckung.

---

## Mythologie-Wissen als Belohnung

- Besiegte Mythologie-Gegner liefern **Wissen/Erkenntnisse**, die in die Basis zurückgebracht werden
- Wissen schaltet neue Gebäude, Einheitentypen oder Upgrades frei
- Das Phylakterium "lernt" die Mythologie – deine Skelette lernen neue Tricks
- Bleibt thematisch kohärent: Deine Armee ist und bleibt untot, aber bereichert durch gelernte Magien/Techniken

### Gestaffelte Freischaltung

| Stufe | Anforderung | Belohnung |
|-|-|-|
| Grund | 1 Exemplar getötet | Schwache untote Version der Einheit produzierbar |
| Voll | 5–10 Exemplare getötet | Voll-Version + Spezialfähigkeit |
| Elite | Boss/Anführer besiegt | Elite-Variante oder Gebäude-Freischaltung |
| Pantheon | Komplettes Mythen-Set besiegt | Synergien, Spezialgebäude (z.B. "Nordische Halle") |

**Visuell:** Untote Versionen nutzen das Original-Mesh mit Undead-Palette (siehe Fraktions-Paletten). Stufen sichtbar machen: Grund = stark verwest, Voll = vollständig, Elite = zusätzliche Knochen-Rüstung / Krone. Spart Modellierungsaufwand und erzählt die Eroberung.

### Magien als Einheiten-Fähigkeiten

- **Passive Fähigkeiten:** Grundeigenschaften (Bewegung, Angriff, HP, Schadenstyp)
- **Aktive Fähigkeiten:** Einmal pro Kampf, mit Cooldown oder Mana-Kosten
- **Pantheon-Magien:** Globale Effekte, wenn Einheiten einer Mythologie zusammen kämpfen

Beispiele:
- *Nöck (aktiv):* "Sog ins Moor" – feindliche Einheit wird auf Wasserfeld gezogen, verliert HP
- *Irrlicht (passiv):* Feinde auf Nachbarfeldern bewegen sich in zufällige Richtung
- *Valkyre (aktiv):* "Letzter Atemzug" – gefallene eigene Einheit gibt noch einen Angriff ab

Die untoten Versionen **erben die Magien**, werden aber kälter/böser in der Ausführung.

### Lich gestärkt (04.11.2026)

- Grundwerte: 60 LP, 12 Seelenschaden, 20 Seelenschild (vorher 40 / 8 / 10).
- Pro belegtem Kommando-Punkt: +4 LP, +0,5 Schaden, +1 Seelenschild (vorher 2 / 0,25 / 0,25). Neu pro erobertem Ort: +4 LP, +0,5 Schaden, +1 Seelenschild – der Lich wächst mit dem Feldzug.
- Seelenentzug trifft mit dem 1,5-fachen Schaden des Lichs (statt fest 8) und heilt ihn um den Schaden.
- Startarmee (32 Kommando): 188 LP, 28 Schaden, 52 Seelenschild.

### Ahnen, Portale, Marsch-Hinterhalte, Gelände-Fähigkeiten (umgesetzt 04.11.2026)

- **Ahnen:** Vier einzigartige untote Anführer erheben sich, wenn ihr Grab erobert wird, und schließen sich der siegreichen Armee an: Bronzezeitlicher Reiterfürst (Pestruper Gräberfeld), Hünenkönig (Sieben Steinhäuser), Widukinds Schatten (Externsteine), Ratsherr von Rungholt (Rungholt). Nicht rekrutierbar, geben Kommando, können auch ohne Totenhalle einen eigenen Zug führen. Werte: Zeilen `BronzeRider`, `BarrowKing`, `WidukindShade`, `RungholtAlderman` in `gen_data.py`; Gräber in `ancestors` (`world_data.js`).
- **Portalbau:** Nach dem Sturz eines Pantheons wird sein Sitz erst zum Ley-Knoten, wenn der Lich dort ein Portal errichtet (20 Leichen, 10 Seelen, 3 Tage).
- **Lichtsäulen:** Über jedem Pantheon-Sitz steht eine violette Lichtsäule pro lebendem Mitglied; sie erlöschen, wenn Mitglieder fallen.
- **Heimvorteil:** Am Sitz eines Pantheons erhalten die Verteidiger +2 Seelenschild je Kreatur (zusätzlich zum Ley-Bund).
- **Gemeinsamer Marsch:** Bei „Los“ kann jede Armee unterwegs in einen Hinterhalt geraten; alle halten an, der Kampf wird geschlagen, danach geht der Marsch weiter („Weiterziehen“ setzt auch nach dem Laden fort). Fällt eine Armee, scheidet sie aus dem Marsch aus.
- **Gelände-Fähigkeiten** verändern den Boden für ihre Dauer: Geweihter Boden (Heideschwester) macht Felder zu geweihtem Boden, Erdbindung und Dornenkrone zu Schlamm.

### Kampfsystem-Tiefe (umgesetzt 04.11.2026)

- **Fähigkeiten** aus `DT_Abilities` wirken im Kampf (`DATA.abilities`, erzeugt von `gen_data.py`): aktive Fähigkeiten mit Energie (+1 pro eigenem Zug) und Abklingzeit (Knöpfe über „Zug beenden“, Tasten 1–4, Ziel anklicken, Esc bricht ab), Auslöser zu Zugbeginn, bei Treffer, bei erlittenem Schaden und beim Tod (Skelette setzen sich einmal neu zusammen, Irrlichter hinterlassen falsches Licht), Auren (Verwirrung). Die Gegner-KI nutzt sie ebenfalls. Werte skalieren mit der Stapelgröße. Die neuen Mythen-Einheiten nutzen den vorhandenen Fähigkeiten-Satz.
- **Zustände:** Vergiftet, Brennt, Blutet (Schaden zu Zugbeginn), Betäubt (Zug fällt aus), Verlangsamt/Beschleunigt (±2 Bewegung), Geschützt (Seelenschild), Gestärkt (+25 %), Verflucht (−25 %), Gezeichnet (+25 % erlittener Schaden), Verwirrt (−50 %), Regeneration. Dauer in eigenen Zügen der Einheit.
- **Leichen** bleiben auf dem Feld (Totenruf des Nekromanten, Leichenfresser des Ghuls).
- **Schadensvorschau** beim Überfahren eines Ziels: erwarteter Schaden, Schild, wie viele fallen, Wirksamkeit laut Schadensmatrix, Konter.
- **Tageszeit** (Nacht, Morgen, Tag, Abend; Wechsel alle 3 Runden): Nacht Untote +15 %, Gegner −2 Sicht; Tag Lebende +15 %; Morgen Nebel (Sicht −3, Fernkampf −1 Reichweite). Licht und Nebel der Szene folgen der Tageszeit. Die Wilde Jagd kämpft immer nachts.
- **Wind:** Gegner riechen die Untoten mit dem Wind 1,5× so weit, gegen den Wind nur halb so weit.
- **Ankunft:** Hinterhalt (Begegnung unterwegs: Gegner zuerst, eigene Einheiten im ersten Zug verlangsamt), Vorwarnung (Bedrohung ≥ 50 %, Trupps derselben Fraktion unterwegs, oder Gegner, die Tote spüren: Hexen, Druidinnen, Priester, Zwergenkönig), Überraschung (unbemerkt; leise Armee bei Nacht oder Nebel bleibt immer unbemerkt), sonst entdeckt.
- **Token-Modus:** Taste K (automatisch / an / aus); automatisch ab weitem Zoom. Scheiben in Einheitenfarbe mit Namen statt Figuren.

### Expeditionen und Kommandeure (umgesetzt 04.11.2026)

- Mit der **Totenhalle** kann ein Nekromant oder Todesritter aus der Lich-Armee einen eigenen Zug führen (bis 30 Kommando): „Expedition aufstellen“ an einem Rekrutierungsort.
- **Befehlsphase:** Sobald es mehr als eine Armee gibt, wählt man die Armee in der Liste unten rechts, gibt ihr per Ortsinfo ein Ziel und startet mit **„Los“** (Taste G). Dann läuft die Zeit für alle gleichzeitig; Angriffe danach über die Ortsinfo („Angreifen (Nekromant-Zug)“).
- Fällt der Kommandeur, ist der Zug verloren (der Lich lebt weiter). Rückzug: der Kommandeur flieht ins Hügelgrab. „Vereinen“ führt einen Zug zurück in die Lich-Armee.
- Trupps meiden auch die Orte, an denen Expeditionen stehen; Expeditionen decken die Karte auf.
- Noch offen: Begegnungen unterwegs für Expeditionen, einzigartige Ahnen aus Gräbern, Führerlos-Regel.

### Kampagne: Späher, Gefahr, Bedrohung, verbrannte Erde (umgesetzt 04.11.2026)

- **Späher:** Leichenhunde in der Armee decken 40 Felder weiter auf, Geister oder Totenlichter 60 Felder – und sehen durch die Verhüllung der Klöster.
- **Gefahrenfarbe** an den Ortsnamen (links): grün = deutlich schwächer als die Armee, gelb = ebenbürtig, rot = stärker; verhüllte Klöster ohne Farbe.
- **Bedrohung:** Der Tod eines Anführers (Unique) hebt die Bedrohung seiner Fraktion um 15, aller anderen um 5. Bei 90 % schließen die Lebenden ein **Bündnis**: doppelt so viele Trupps (bis 5 gleichzeitig), 1,5× so stark.
- **Verbrannte Erde:** Jede weitere Eroberung desselben Orts bringt nur die halbe feste Beute der vorigen.
- **Chronist:** kurze Erzählzeilen bei ersten Eroberungen, Trupps, Bündnis und Pantheon-Fall.

### Reisen auf der Karte (umgesetzt 04.11.2026)

- Reisen laufen Tag für Tag: 1,6 Sekunden pro Reisetag (Leertaste halten: 4× schneller). Ein großes Datum mit Tageszähler zeigt, wie die Zeit vergeht; Trupps ziehen, Bauten wachsen, Bedrohung sinkt währenddessen.
- **Reisetempo nach der langsamsten marschierenden Einheit** (Lich, Kommandeure und Anführer zählen nicht): Felder pro Tag = 39 × (2 + Bewegung) / 5. Bewegung 3 = normal, Balliste (1) = 60 %, schnelle Armeen bis 160 %.
- **Geplant für mehrere Kommandeure:** Befehlsphase – jedem Kommandeur ein Ziel geben, dann „Los“; erst dann läuft die Zeit für alle gleichzeitig (Ereignisse unterwegs unterbrechen für alle).

### Wissen und Gebäude (umgesetzt 04.11.2026)

- **Wissen** wird nicht verbraucht. Einheiten sind entweder nur an eine Wissensmenge gebunden oder zusätzlich an den Sturz eines Pantheons. **Unbekannte Einheiten bleiben verborgen** – Rekrutieren und Bauen zeigen nur „Nächste Erkenntnis bei X Wissen“ und ob noch Geheimnisse bei ungestürzten Pantheons liegen. Erreicht man die Schwelle, meldet das Spiel die neue Einheit.
- Nur Wissen: Schleuderer 2, Geist 3, Knochenschütze 4, Fleischriese 5, Gefallene Schwester 6, Todesritter 7, Nekromant 9, Knochenballiste 10.
- Pantheon + Wissen: Moorleiche (Heide, 3), Totenlicht (Heide, 5), Grabdruidin (Heide, 8), Wasserleiche (Versunkene Städte, 6), Totenjäger (Wilde Jagd, 10), Knochendrache (Wendische Geister, 16). Diese brauchen zusätzlich den **Wissensaltar**.
- **Gebäude im Hügelgrab** (`buildings` in `world_data.js`, aus `DT_Buildings` auf die Spielwirtschaft umgerechnet): Phylakterium (kürzere Rückkehr nach dem Tod), Knochenwerkstatt, Leichengrube, Seelenzwinger (+12 Kommando je Stufe), Totenhalle, Wissensaltar, Knochenschmiede (nach Eroberung Iberg: Todesritter +2 Seelenschild), Heidealtar (nach Sturz des Heide-Pantheons: Heilung auf Heide). Jede Einheit braucht die Gebäudestufe, die sie erhebt. Ein Bau zur Zeit, er läuft während der Reise weiter.

### Pantheons, Ley-Knoten und Trupps (umgesetzt 04.11.2026)

Erste spielbare Fassung von „Einfluss auf Regionen“, Ley-Linien-Teleportation und Pantheon-Fall:

| Pantheon | Sitz (Ley-Knoten) | Mitglieder |
|-|-|-|
| Heide-Pantheon | Oldendorfer Totenstatt | + Pestrup, Iberg, Sieben Steinhäuser, Teufelsmoor, Dümmer, Arendsee |
| Wilde Jagd | Kyffhäuser | + Hackelbergs Grab, Externsteine |
| Wendische Geister | Spreewald | + Kap Arkona |
| Versunkene Städte | Rungholt | + Vineta |
| Walpurgis-Zirkel | Brocken | + Hexentanzplatz, Teufelsmauer, Hameln |

- **Region:** jeder Ort gehört zum Pantheon mit dem nächsten Mitglied (höchstens 260 Felder).
- **Halb erobert:** Lebende Mitglieder schicken Trupps in ihre eigene Region (0,8 % pro Tag und Mitglied) und stärken den Sitz (Ley-Bund: +4 Einheiten pro lebendem Mitglied).
- **Assimiliert** (alle Mitglieder erobert): Trupps erobern in der Region nichts mehr zurück; der Sitz wird Ley-Knoten. Zwischen aktiven Ley-Knoten und dem Hügelgrab: **Ley-Sprung** (1 Tag, 4 Seelen). Minimap zeigt die Ley-Linien violett, Karte markiert Knoten mit ✦.
- **Pantheon-Fall:** Die Fraktionen des Pantheons schicken keine Trupps mehr, ihre übrigen Orte haben nur noch 60 % Besatzung (Anführer bleiben).
- Noch offen: Portalbau als eigener Schritt, Lichtsäulen am Sitz, Heimvorteil im Kampf.
- Werte: `pantheons`, `ley`, `raids.mythicChance` in `data/world_data.js`.

### Gegnertrupps (umgesetzt 04.11.2026)

Die Lebenden schlagen zurück, aber nur dort, wo der Lich nicht ist:

- **Auszug:** Ab Tag 20 schicken Städte und große Klöster (Größe ≥ 32, noch in eigener Hand) Trupps aus. Chance pro Ort und Tag 0,2 % + 0,02 % je Prozent Bedrohung der Fraktion; höchstens 2 Trupps gleichzeitig, auf der ganzen Karte höchstens ein neuer Trupp alle 10 Tage, dieselbe Fraktion höchstens alle 25 Tage (angepasst 04.11.: vorher viel zu schnell). Stärke: die Hälfte der Besatzung des Ausgangsorts (ohne Anführer), mindestens 6 Einheiten.
- **Ziel:** der nächste eroberte Ort im Umkreis von 450 Feldern, den die Armee nicht deckt. Marsch: 14 Felder pro Tag (die Armee schafft 39).
- **Kartenseite:** Steht die Armee höchstens 250 Felder vom Trupp oder von dessen Ziel entfernt, wartet der Trupp. So fallen Orte nur, wenn der Lich anderswo unterwegs ist.
- **Rückeroberung:** Erreicht ein Trupp sein Ziel, gehört der Ort wieder seiner alten Fraktion; das tote Land dort verschwindet.
- **Erholung:** Ein zurückeroberter Ort startet mit 25 % seiner Besatzung und wächst in 20 + 1,5 × Größe Tagen wieder auf volle Stärke (Dorf ~6 Wochen, große Stadt ~4 Monate; `recovery` in `world_data.js`). **Anführer (Bosse) kehren nie zurück**, sobald ihr Ort einmal gefallen ist.
- **Abfangen:** Trupps erscheinen auf Karte und Minimap (Dreieck, gestrichelte Linie zum Ziel). Anklicken → „Abfangen“: Kampf gegen den Trupp, danach steht die Armee wieder an ihrem Ort.
- Werte: `raids` in `data/world_data.js`.

### Totes Land (umgesetzt 04.11.2026)

Um das Hügelgrab und um jeden eroberten Ort stirbt die Landschaft – sichtbare Spur des Raubzugs:

- **Ausbreitung:** Das Hügelgrab beginnt mit ~8 Feldern Radius und wächst mit jedem eroberten Ort (+1,6) und langsam mit der Zeit. Jeder eroberte Ort wächst ab der Eroberung um 0,35 Felder pro Tag bis zu einem Höchstradius nach Ortsgröße (4 + 2,6 · √Größe).
- **Alter:** Je länger ein Feld tot ist, desto stärker der Effekt (voll nach ~30 Tagen). Boden: trockene graue Erde, schwarze Moorflecken, schwache grünliche „unheilige Adern“.
- **Pflanzen:** Bäume werden zu grauen, kahlen Stämmen und fallen mit der Zeit um (liegende Stämme), Heide und Gras verdorren, im Kern stehen schiefe Grabsteine. Die Minimap zeigt das tote Land als graue Schicht.
- Werte: `BLIGHT` in `index.html`. Spielmechanische Folgen (z. B. „verbrannte Erde“, keine Beute mehr) sind noch offen.

## Ressourcen – "Verbrannte Erde"-Prinzip

Klassische RTS-Ressourcen (Gold, Holz, Eisen, Nahrung) passen nicht zur untoten Fantasie. Das Spiel ist **kein Aufbauspiel**, sondern ein **Raubzug**. Der Lich pflegt nichts – er verschlingt.

Zwei Arten von Ressourcen-Quellen:

### Permanente Quellen (nach Assimilation dauerhaft)

- **Heidnische Kultstätten** – entweiht = dauerhafte Ley-Line-Anzapfung (nekrotische Energie)
- **Mystische Orte (Steinkreise, Hünengräber, Opferstätten)** – permanente Mana-Quelle
- **Klöster** (entweiht) – *entfernt eine Blockade* (siehe unten), kein direkter Ressourcen-Ertrag

### Endliche Quellen (Raubgut, dann tot)

- **Dörfer/Bauernhöfe** – Leichen, bis alles geschlachtet ist, dann verbrannte Erde
- **Friedhöfe/Gräberfelder** – Knochen + **Rekrutierungs-Chance für besondere Untote** → potentielle Anführer (siehe unten)
- **Alte Schlachtfelder** – einmalige Ausbeute erfahrener Kriegerleichen
- **Heidnische Artefakte** – einmaliger Fund an Kultstätten; verbrauchbar für mächtige Effekte

### Ressourcen-Typen

- **Leichen** – Grundmaterial (Qualität abhängig von Todesart, siehe Schadenstyp-Tabelle)
- **Seelen** – Sonderressource durch Geist-Kills
- **Knochen / Rohmaterialien** – aus Friedhöfen, Beinhäusern
- **Nekrotische Energie / Ley-Line-Kraft** – treibt aktive Fähigkeiten an
- **Wissen (Mythologie)** – schaltet Einheiten, Gebäude, Upgrades frei

### Design-Konsequenz

- **Druck nach vorne:** Ausgebeutete Gebiete sind tot, der Lich *muss* weiter
- **Kein passives Farmen:** Keine langweiligen Warterunden, jede Expansion ist Entscheidung
- **Finite Kampagne:** Eine Region (z.B. Norddeutschland) wird irgendwann leer. Das ist OK – Kampagne endet am Brocken, nächste Kampagne = neue Region.
- **Tempo-Balancing als Schlüssel:** Zu schnell = Nachschub fehlt später; zu langsam = Pantheons regenerieren. Push-Dilemma.

---

## Gräber als Rekrutierung von Kommandeuren

In alten Gräbern ruhen besondere Untote, die der Lich erweckt. Diese werden zu seinen **Anführer-Einheiten** (siehe Armee-Limit-Sektion).

- Nicht aus Leichen *gebaut*, sondern **erweckt** – sind "Seinesgleichen" aus früheren Zeiten
- Benannte Individuen mit Geschichte – emotionales Gewicht, anders als austauschbare Masseneinheiten
- Regional unterschiedliche Pools:
  - Heide → bronzezeitliche Kriegerhäuptlinge, Hügelgrab-Druidinnen
  - Harz → bergmännische Urahnen, alte Berggeister
  - Küste → Meerleute-Schamanen, ertrunkene Anführer
- Mögliche Archetypen:
  - **Bronzezeit-Krieger-Häuptling** – militärisch, buffs Nahkampf
  - **Eisenzeit-Druide/Schamanin** – Magie-Anführer, nekrotische Energie-Regen
  - **Vergessener Priesterkönig** – Allrounder, besonders stark gegen christliche Einheiten
  - **Wikingerzeit-Seher** – Stealth-Bonus, prophetische Fähigkeiten

**Visuell:** Ahnen tragen **epochen-typische Grabbeigaben** als Erkennungsmerkmal (Bronzezeit: Bronzehelm, Spiralfibeln; Eisenzeit: Torques, Mistelkranz; Wikingerzeit: Kettenhemd, Runenamulett). Das unterscheidet sie sofort von mittelalterlichen Gegnern und von generischen Kommandeuren.

### Zwei Klassen von Kommandeuren

**Produzierbare Kommandeure (generisch):**
- Aus Basis-Gebäuden rekrutierbar (Todesritter, Nekromant, Geisterfürst)
- Kosten Leichen, Knochen, nekrotische Energie
- Standard-Statistiken, Standard-Fähigkeiten
- Ersetzbar – fällt einer, produziert man einen neuen
- Idealer Kanonenfutter-Kommandeur für Aufklärungs-Trupps in unbekannte Regionen

**Einzigartige Kommandeure (Ahnen):**
- Aus Gräbern erweckt, nicht reproduzierbar (Brunhild, Theobald der Stumme, Wulf die Kralle)
- Bessere/ungewöhnlichere Stats, eigene Spezialfähigkeiten
- Benannt, mit minimaler Hintergrundgeschichte
- **Unersetzbar** – sollen für wichtige Kämpfe aufgespart werden

**Design-Konsequenz:**
- Spieler hat echte taktische Wahl: Generische als Kanonenfutter, Uniques für Endkämpfe
- Mechanik bleibt einsteigerfreundlich (Uniques nicht Voraussetzung, sondern Upgrade)
- Erzählerisch entsteht Hierarchie: Lich → Ahnen → produzierte Offiziere → Massen-Einheiten

**Verbindung der Klassen:**
Einzigartige Ahnen können Vorbilder für generische Varianten werden. Beispiel: Eine bronzezeitliche Kriegerin wird erweckt → ab dann ist "Bronzezeit-Kriegerin" als generischer Todesritter-Typ produzierbar (schwächer, namenlos). Uniques lehren den Lich ihre Art. Passt zum Mythologie-Wissen-System.

### Sterblichkeit von Kommandeuren – unterschiedlich für beide Klassen

**Generische Kommandeure:** Sterben dauerhaft (Option A). Kein Drama, neuer wird produziert.

**Einzigartige Kommandeure:** Hier sind Optionen B oder C sinnvoller (Teleportation zurück ins Phylakterium oder Wiedererweckung mit Kosten), weil dauerhafter Verlust durch Zufall zu frustrierend wäre.

**Verbleibende Optionen für Uniques (Entscheidung beim Spieltest):**

- **Option B:** Teleport zurück ins Phylakterium bei "Tod", einfache Rückkehr nach Zeit/Runden
- **Option C (Mittelweg):** Wiedererweckbar mit Kosten (Leichen, nekrotische Energie, Kampagnen-Zeit, Artefakte). Kann Narben-Debuffs oder Nahtod-Boni geben → narrative Charakterentwicklung. Narben werden am Modell sichtbar (Material-Layer).

---

## Leichen-Ressourcen & Schadenstypen

| Schadenstyp | PowerType | Verursacher | Leichen-Qualität | Notiz |
|-|-|-|-|-|
| Sauber (Stich, Schnitt) | Pierce | Skelett-Speerträger, Valkyre | ~100% | Idealzustand |
| Stumpf (Keule, Faust) | Blunt | Zombie, Knochenriese | ~70% | Zerschmettert |
| Zerfleischend (Biss, Klaue) | Rend | Ghul, Wolfsbestie | ~40% | Zerrissen |
| Belagerung | Siege | Balliste, Katapult | ~30% | Zertrümmert |
| Feuer | Fire | Feuerdämon | ~20% | Verkohlt |
| Seelenschaden | Soul | Geist, Banshee | ~100% Körper + **Seelen-Ressource** | Besonderer Bonus |
| Gift / Säure | Poison | Kultist, Giftkröte | ~50% (verdorben) | *Verdorben ≠ schlecht: Gift-Zombies möglich (Spätgame-Feature)* |
| Arkan / Chaos | Arcane, Chaos | Magier-Einheiten | ~80% | Kaum Körperschaden |
| Heilig | Holy | (nur Gegner) | – | Eigene Untote zerfallen zu Staub, keine Leiche |

**Design-Konsequenz:** Taktische Entscheidungen bekommen eine ökonomische Ebene. Einheit X killt schnell, aber zerstückelt; Einheit Y ist langsamer, aber erhält den Wert des Kadavers. **Sichtbar gemacht** über Leichen-Look und Schadensvorschau (siehe Einheiten-Visualisierung).

**Keine Ressourcen aus verlorener Schlacht:** Wenn der Lich fällt, ist der Teleportzauber weg – Leichen und Einheiten bleiben auf dem Schlachtfeld.

**Geordneter Rückzug möglich:** Wenn eigene Einheiten übrig sind, können Ressourcen auch bei Nicht-Gewinn gesichert werden.

**Offene Frage:** Werden eigene gefallene Einheiten auch als Leichen "geerntet"? (Thematisch: ein Lich wirft nichts weg. Mechanisch: mildert Verlust-Schmerz.)

---

## Armee-Limit

Ohne Limit würde die Armee unaufhaltsam wachsen und das Spiel zerfallen. Mechanik: **Kombination aus Kommandopunkten, Basis-Upgrades, Anführer-Einheiten und parallelen Expeditionen.**

### Grundsystem
- Jede Einheit hat Kommando-Kosten (schwaches Skelett = 1, Elite = 3–4, Fleischriese = 8)
- Armee-Budget fest pro Expedition (z.B. 15 Punkte Grund-Limit) – das ist das Budget des Lichs selbst; er kostet keine und gibt keine zusätzlichen Punkte (`CommandPoints = 0`)
- Basis-Gebäude können das Limit erweitern ("Seelenzwinger" Stufe 1 → 2 → 3)
- **Rechtfertigt große Einheiten mechanisch:** Fleischriese kostet 15 Leichen zum Bau *und* 8 Kommandopunkte im Feld → echte Investition (ursprünglich 15 KP; die Balancing-Rechnung zeigte, dass er dann klar schlechter als jede Alternative wäre)

### Anführer-Einheiten

Anführer sind selbst Kampfeinheiten, die aber **das Kommando-Limit ihrer Gruppe erweitern**.

- Anführer kostet z.B. 4 Kommandopunkte, erhöht Limit um 8 → netto +4 Budget
- Je höher die Anführer-Stufe, desto größere Erweiterung
- **Solange der Anführer lebt.** Fällt er, schrumpft das Budget, übrige Einheiten werden "führerlos" (Debuff? Moralverlust? Desertion?)
- **Sichtbar:** Befehls-Aura am Boden; Einheiten, die am Anführer hängen, haben eine feine Linie zum Banner bei Hover über den Anführer

Mögliche Anführer-Arten:
- **Totenfürst / Death Knight** – Skelett-Krieger, +Angriff für Gruppe
- **Nekromant** – Zombies/Beschwörungen, kann in Schlacht nachbeschwören
- **Geisterkönig** – Geister/Wraiths, bessere Bewegung durch Hindernisse
- **Valkyren-Königin** (nach Pantheon-Assimilation) – untote Einheiten mit nordischen Magien

Taktische Konsequenz: Gegner priorisiert Anführer, große Armeen sind durch wenige Stützen verletzlicher.

### Parallele Expeditionen (Spätgame)

- Jede Expedition braucht einen **Kommandanten** an der Spitze
- Am Anfang immer der Lich selbst
- Sobald ein Anführer stark genug entwickelt ist, kann er eine Expedition selbstständig führen
- Ermöglicht 2 (oder später mehr) gleichzeitige Kreuzzüge → Anführer sind Voraussetzung fürs Endgame

---

## Kampagnen-Struktur (Idee)

- Mauern/Befestigungen blockieren frühen Zugriff → brauchen Belagerung
- Belagerungseinheiten mitzunehmen kostet Kommandopunkte → schwächt andere Kämpfe
- Spieler erschafft seine eigene Schwierigkeitskurve durch Wahl der Mitnahme

## Heide-Kampagne: Basis, Wissen, Begegnungen

Konkreter Inhalt für **Phase 2 (Mini-Kampagne)** und **Phase 6 (Vertical Slice Heide)**. Alle Tabellen sind aus `campaign_data.py` generiert; Quelle der Wahrheit sind die CSVs in `design/data/` (`DT_Buildings`, `DT_Knowledge`, `DT_Encounters`).

### Ressourcen-Kreislauf

- **Leichen (L)** sind die Leitwährung. Kämpfe liefern sie – Menge nach Größe der Getöteten (Size 1–2: 1, Size 3: 2, Size 4: 3), Qualität nach Todesart (siehe Leichen-Tabelle). Spektrale Wesen hinterlassen keine Leiche.
- **Knochen (K)** entstehen durch **Auskochen in der Knochenwerkstatt (1 L → 2 K)** und als Bonus an Orten mit Friedhof oder Grabbeigaben. Grund: Die Simulation zeigte, dass Skelett-Verluste sonst nicht nachproduzierbar sind – Kämpfe liefern keine Knochen.
- **Seelen (S)** entstehen bei Kills durch Seelenschaden (vor allem Lich und Geister) und als Bonus an Kultorten.
- **Nekrotische Energie (E)** erst ab Phase 6 (Ley-Knoten, entweihte Kultstätten) – nur für Stufe-3-Gebäude und Pantheon-Gebäude.
- **Startvorrat:** 10 L, 10 K, 2 S. **Eigene Gefallene** geben nach einem Sieg 50 % ihrer L/K-Kosten zurück (Vorschlag aus den offenen Fragen, in der Rechnung bereits angewendet).

### Basis-Gebäude

Beantwortet die offene Frage „Welche Gebäude-Typen in der Basis konkret?". Start-Gebäude: Phylakterium 1, Knochenwerkstatt 1, Leichengrube 1.

<!--GEN:BUILDINGS:BEGIN-->
| Gebäude | Stufe | Kosten | Bautage | Voraussetzung | Produziert | Wirkung |
|-|-|-|-|-|-|-|
| Phylakterium | 1 | Start | – | – | – | Start. Lager 50 L / 50 K / 10 S. Lich-Rückkehr nach Tod: 3 Tage |
| Phylakterium | 2 | 20L 20K 5S | 3 | Phylakterium 1 | – | Lager 100/100/20. Rückkehr 2 Tage |
| Phylakterium | 3 | 40L 40K 10S 10E | 5 | Phylakterium 2 | – | Lager 200/200/40. Rückkehr 1 Tag. Zweite Expedition möglich |
| Knochenwerkstatt | 1 | Start | – | – | Skelett, Skelett-Bogenschütze, Knochenschleuderer | Start. Auskochen: 1 Leiche → 2 Knochen. Schleuderer erst mit Spielwissen 2 |
| Knochenwerkstatt | 2 | 10L 10K | 2 | Knochenwerkstatt 1 + Armbrust-Handwerk | Knochenschütze | Knochenschützen |
| Knochenwerkstatt | 3 | 20L 30K 2S | 4 | Knochenwerkstatt 2 | Balliste, Knochendrache | Belagerung, Knochendrache |
| Leichengrube | 1 | Start | – | – | Zombie, Ghul, Leichenhund | Start |
| Leichengrube | 2 | 15L 10K | 2 | Leichengrube 1 + Moorwissen | Moorleiche, Wasserleiche | Moorleichen, Wasserleichen |
| Leichengrube | 3 | 30L 20K 5S | 4 | Leichengrube 2 | Fleischriese | Fleischriesen |
| Seelenzwinger | 1 | 10L 10K 3S | 2 | – | Geist | Kommando-Limit 15 → 20 |
| Seelenzwinger | 2 | 20L 20K 6S | 3 | Seelenzwinger 1 + Irrlicht-Bann | Totenlicht | Limit 25, Totenlichter |
| Seelenzwinger | 3 | 40L 40K 12S 10E | 5 | Seelenzwinger 2 | – | Limit 30 |
| Totenhalle | 1 | 15L 20K 3S | 3 | – | Todesritter, Nekromant | Kommandeure. 1 Ahne pro Expedition |
| Totenhalle | 2 | 25L 30K 6S | 4 | Totenhalle 1 | Gefallene Schwester, Grabdruidin, Totenjäger | Untote Heide-Varianten (jeweils mit Wissen). 2 Ahnen pro Expedition |
| Wissensaltar | 1 | 5L 5K | 1 | – | – | Wandelt erbeutetes Wissen in Freischaltungen. Voraussetzung für alle untoten Varianten |
| Knochenschmiede | 1 | 20L 30K 4S | 3 | Knochenwerkstatt 1 + Zwergenschmiede | – | Todesritter +2 SoulShield dauerhaft |
| Heidealtar | 1 | 30L 20K 10S 10E | 5 | Wissensaltar 1 + Herz der Heide | – | Eigene Untote heilen auf Heather-Feldern 2 HP/Runde. Pantheon-Synergien der Heide |
<!--GEN:BUILDINGS:END-->

**Logik dahinter:** Jedes Produktionsgebäude steht für eine Art Untoter (Knochen, Fleisch, Seele, Kommandeur). Stufe 2 öffnet die untoten Varianten besiegter Gegner – aber nur mit dem passenden Wissen. So entsteht ein Baum, in dem Kampf-Erfolg (Wissen) und Wirtschaft (Ressourcen) beide nötig sind.

### Wissen (Mythologie-Freischaltungen)

Vereinfachung gegenüber der 4-stufigen Freischaltung im Kapitel Mythologie-Wissen: Für den Vertical Slice gibt es nur **eine Stufe pro Gegnertyp** (= „Voll"). Grund- und Elite-Stufe kommen in Phase 7.

<!--GEN:KNOWLEDGE:BEGIN-->
| Wissen | Quelle | Kills nötig | Schaltet frei | Hinweis |
|-|-|-|-|-|
| Armbrust-Handwerk | Lüneburger Armbrustschütze | 8 | Knochenschütze, Knochenwerkstatt | – |
| Moorwissen | Moorgeist | 5 | Moorleiche, Leichengrube | – |
| Irrlicht-Bann | Irrlicht | 8 | Totenlicht, Seelenzwinger | – |
| Verkehrte Weihe | Heideschwester | 5 | Gefallene Schwester | – |
| Grabhüter-Riten | Hügelgrab-Druidin | 5 | Grabdruidin | – |
| Wilde Jagd | Der Wode | 1 | Totenjäger | Legt zusätzlich das Ahnen-Grab eines bronzezeitlichen Reiterfürsten frei |
| Zwergenschmiede | Hügelgrab-Zwergenkönig | 1 | Knochenschmiede | Plus 1 heidnisches Artefakt |
| Herz der Heide | Die Heidekönigin | 1 | Heidealtar | Region assimiliert, Ley-Knoten Wilseder Berg (nach Portalbau) |
<!--GEN:KNOWLEDGE:END-->

### Begegnungen

Phase 2 nutzt die ersten drei als lineare Mini-Kampagne (Hof → Kirche → Moor). Die drei Pantheon-Kämpfe gehören zu Phase 6.

<!--GEN:ENCOUNTERS:BEGIN-->
| Begegnung | Phase | Typ | Karte (km O / km S) | Feld | Gegner | Zeit | Stealth | Bonus-Beute | Besonderheit |
|-|-|-|-|-|-|-|-|-|-|
| Einzelhof bei Wilsede | 2 | Weltlich | 191.1 / 201.1 | 8×8 | 4× Bauer, Lüneburger Armbrustschütze | Nacht | ja | +2L | Tutorial-Kampf. Bauern schlafen: Überraschung fast sicher |
| Alte Kirche Bispingen | 2 | Christlich | 196.5 / 211.7 | 12×10 | 3× Bauer, 2× Lüneburger Armbrustschütze, 2× Heideschwester | Abend | ja | +6K | Feldsteinkirche, erbaut 1353. Kirchhof liefert Bonus-Knochen. Geweihter Boden um die Kirche |
| Pietzmoor bei Schneverdingen | 2 | Mythisch | 185.3 / 207.7 | 10×10 | Moorgeist, 3× Irrlicht, Hügelgrab-Druidin | Morgen | nein | +3L | Morgennebel, Moorboden. Keine Stealth-Phase: Irrlichter sehen alles. Moorleichen im Torf: +3 Leichen |
| Die Wilde Jagd (Pantheon) | 6 | Mythisch | 177.7 / 229.6 | 14×8 | Der Wode, 4× Schwarzer Hund | Nacht | nein | +6L +3S | Pantheon. Immer nachts. Offene Heide ohne Deckung. 4 Hunde = 2 Start + 2 beschworen (Simulation kennt keine Beschwörung). Gefallene Jagdpferde: +6 Leichen |
| Hügelgrab des Zwergenkönigs (Pantheon) | 6 | Mythisch | 186.3 / 222.5 | 10×10 | Hügelgrab-Zwergenkönig, 2× Hügelgrab-Druidin, 3× Irrlicht | Nacht | nein | +15K | Pantheon. Grabkammern, StoneFloor. Keine Stealth-Phase. Grabbeigaben: +15 Knochen |
| Wilseder Berg (Pantheon) | 6 | Mythisch | 192.0 / 202.5 | 12×12 | Die Heidekönigin, 2× Moorgeist, 3× Irrlicht, Hügelgrab-Druidin | Tag | nein | +5S | Pantheon-Finale der Region. Ley-Bund: +10 SoulShield pro lebendem Randmitglied. Phase 2 ab 50 % HP |
<!--GEN:ENCOUNTERS:END-->

### Simulierte Schwierigkeitskurve

`encounter_check.py` lässt drei Armee-Stufen je 300-mal gegen jede Begegnung antreten (Grundangriffe und Konter, Anmarsch nach Feldgröße; **ohne** Fähigkeiten, Gelände, Stealth und Beschwörungen). Dauer geschätzt mit 20 s pro eigenem Zug, 6 s pro Gegnerzug, 2 min Aufstellung.

<!--GEN:ARMIES:BEGIN-->
| Armee | Zusammensetzung | KP / Limit |
|-|-|-|
| Start | Lich, 6× Skelett, 2× Ghul, 3× Zombie | 13 / 15 |
| Ausgebaut | Lich, Nekromant, 2× Todesritter, 2× Geist, 4× Skelett, 2× Knochenschütze | 22 / 24 (Seelenzwinger 1 + Nekromant) |
| Stark | Lich, Nekromant, 3× Todesritter, 2× Geist, 2× Totenjäger, 4× Knochenschütze | 34 / 34 (Seelenzwinger 3 + Nekromant) |
<!--GEN:ARMIES:END-->

<!--GEN:ENC_RESULTS:BEGIN-->
| Begegnung | Armee | Siegchance | Dauer | Verluste | Netto Leichen | Netto Seelen |
|-|-|-|-|-|-|-|
| Einzelhof bei Wilsede | Start | 100% | 10 min | 0.0 | +6.6 | +1.9 |
| Einzelhof bei Wilsede | Ausgebaut | 100% | 9 min | 0.0 | +7.0 | +4.0 |
| Einzelhof bei Wilsede | Stark | 100% | 9 min | 0.0 | +7.0 | +4.2 |
| Alte Kirche Bispingen | Start | 100% | 17 min | 5.4 | +6.6 | +3.3 |
| Alte Kirche Bispingen | Ausgebaut | 100% | 14 min | 1.0 | +9.8 | +3.9 |
| Alte Kirche Bispingen | Stark | 100% | 12 min | 0.5 | +9.9 | +4.1 |
| Pietzmoor bei Schneverdingen | Start | 100% | 12 min | 2.4 | +4.2 | +1.0 |
| Pietzmoor bei Schneverdingen | Ausgebaut | 100% | 11 min | 0.8 | +5.7 | +3.0 |
| Pietzmoor bei Schneverdingen | Stark | 100% | 10 min | 0.4 | +5.8 | +2.6 |
| Die Wilde Jagd | Start | 100% | 15 min | 10.9 | +2.3 | +4.3 |
| Die Wilde Jagd | Ausgebaut | 100% | 14 min | 7.7 | +4.6 | +2.1 |
| Die Wilde Jagd | Stark | 100% | 14 min | 4.8 | +3.9 | +0.6 |
| Hügelgrab des Zwergenkönigs | Start | 100% | 19 min | 10.7 | +4.7 | +1.5 |
| Hügelgrab des Zwergenkönigs | Ausgebaut | 100% | 17 min | 6.2 | +8.4 | +0.2 |
| Hügelgrab des Zwergenkönigs | Stark | 100% | 16 min | 4.6 | +6.0 | -3.1 |
| Wilseder Berg | Start | 95% | 24 min | 11.0 | +0.9 | +7.5 |
| Wilseder Berg | Ausgebaut | 100% | 21 min | 8.2 | +3.2 | +4.3 |
| Wilseder Berg | Stark | 100% | 20 min | 6.4 | +1.3 | +2.1 |
| Wilseder Berg **mit vollem Ley-Bund** | Start | 0% | 25 min | alle | – (Niederlage) | – |
| Wilseder Berg **mit vollem Ley-Bund** | Ausgebaut | 100% | 23 min | 9.6 | +1.5 | +3.0 |
| Wilseder Berg **mit vollem Ley-Bund** | Stark | 100% | 21 min | 6.7 | +0.9 | +2.2 |
<!--GEN:ENC_RESULTS:END-->

**Was die Zahlen sagen:**
- **Phase 2 trägt:** Alle drei Knoten sind mit der Startarmee in 10–18 Minuten schaffbar und bringen netto Leichen. Die Kirche ist der Kostentreiber (Heilig gegen Skelette) – sie lehrt früh, warum geweihte Orte gefährlich sind.
- **Kampfdauer-Ziel 15–20 min** wird von normalen Knoten eingehalten oder leicht unterschritten. Pantheon-Kämpfe liegen bei 14–26 min – für Bosskämpfe akzeptabel.
- **Pantheon-Randmitglieder** sind mit der Startarmee Pyrrhussiege (fast alle Einheiten verloren) – gewollt, Gothic-Prinzip.
- **Ley-Bund wirkt:** Gegen die Heidekönigin mit beiden lebenden Randmitgliedern sinkt die Siegchance einer ausgebauten Armee spürbar und die Verluste steigen. Erst die Randmitglieder zu schlagen lohnt sich – genau die gewünschte Entscheidung.
- **Pantheon-Kämpfe bringen kaum Beute.** Ihr Lohn ist Wissen – passt zum Knotentyp-Profil („Mythisch: wenig Ressourcen, viel Forschung"). Ohne Bonus-Beute war die Wilde Jagd sogar ein Verlustgeschäft (Geisterhunde hinterlassen keine Leichen); deshalb +6 Leichen durch gefallene Jagdpferde.
- **Grenzen:** Fähigkeiten fehlen (Heilung der Gegner, Flächenschaden des Fleischriesen, Beschwörungen). Echte Kämpfe gegen Heilerinnen werden länger; die Zahlen sind ein Vergleichsmaß, kein Ersatz für den Spieltest.

---

## Startort der ersten Kampagne

**Lüneburger Heide** – ein vergessenes bronzezeitliches Hügelgrab.

- Der Lich erwacht darin, das Phylakterium bleibt zurück als Basis
- **Geografisch zentral** – Hub-and-Spoke-Karte: Wege in alle Richtungen
- Thematisch: Moore und Hügelgräber sind Untoten-Heimat schlechthin
- Erste Gegner: Bauern, Dorfpriester, Moorgeister, Irrlichter – "niedrige" Mythologie zum Aufbauen
- **Politisch leichtes Gebiet:** klassisches Patchwork aus rivalisierenden kleinen Fraktionen (siehe Fraktionsdynamik)

**Entschieden (02.11.2026): Das Phylakterium liegt im Hügelgrab in der Heide**, nicht am Kalkberg.

**Kalkberg als Erzählmotiv (optional):** 1371 haben die Lüneburger Bürger die Welfenburg auf dem Kalkberg zerstört. Darunter lag ein alter Ley-Knoten, der dadurch freigelegt wurde – die Erschütterung reicht bis ins Hügelgrab und weckt den Lich. Der Kalkberg ist damit Auslöser, nicht Ort der Basis.

### Kartengrenzen der ersten Kampagne

- **West:** Ems (Ostfriesland/Emsland liegt noch drin)
- **Nord:** Nordsee
- **Ost:** Spree/Oder-Linie (Spreewald als östlichster Knoten)
- **Süd:** Harz-Südrand (dahinter beginnen andere Regionen → spätere Kampagnen)

### Knoten auf der Karte

**Mythologische Knoten (an Ley-Linien):**
- Wilseder Berg (Heide-Zentrum, nah am Phylakterium)
- Teufelsmoor (Moorgeister, westlich)
- Externsteine (Teutoburger Wald, westlich vom Harz)
- Wodan-Kult in Mecklenburg (Fru Gode, nördlich)
- Harz-Mitte (Teufelsmauer, Ilsetal, Thale)
- **Brocken** (mächtigster Ley-Knoten, Finale der Kampagne)
- Kyffhäuser (Barbarossa, südlich am Harzrand)
- Spreewald (Irrlichter, Schlangenkönig, östlich)

**Christliche Knoten (an Ley-Linien):**
- Kloster Ebstorf (Heide, mit Ebstorfer Weltkarte)

**Weltliche Knoten (an Flüssen):**
- Lüneburg (Ilmenau/Elbe – erste Menschenhauptstadt, mechanisch geschwächt)
- Hamburg (Elbe – reiche Hansestadt)
- Bremen (Weser – Erzbistum, Handelsstadt)
- Hameln (Weser – Rattenfänger-Sage)
- Magdeburg (Elbe – Erzbistum)
- Berlin (Spree – Mark Brandenburg)

**Küsten-Knoten (Nordsee):**
- Rungholt (versunkene Stadt)
- Klabautermann (Ostfriesische Küste)

### Kartenkoordinaten der Orte

Quelle der Wahrheit sind **Breite/Länge** (`PLACES` in `campaign_data.py`). Kartenposition und Pixel der neuen Höhenkarte werden daraus berechnet (`geo.py`, `worldmap.py`) – nie von Hand eintragen. Generierte Tabelle:

<!--GEN:PLACES:BEGIN-->
| Ort | Breite | Länge | Karte km O / km S | Kartenposition (Höhenpunkte) | Bedeutung |
|-|-|-|-|-|-|
| Hamburg | 53.5523 | 9.9946 | 195.5 / 159.4 | (791, 645) | Hansestadt, Elbe |
| Lüneburg | 53.2523 | 10.4154 | 224.1 / 192.3 | (907, 778) | Erste Menschenhauptstadt |
| Teufelsmoor | 53.2315 | 8.9321 | 125.1 / 195.5 | (506, 791) | Moorgeister |
| Wilseder Berg | 53.1648 | 9.9321 | 192.0 / 202.5 | (777, 819) | Ley-Knoten Heide, Pantheon-Finale der Region |
| Kloster Medingen | 53.0898 | 10.5321 | 232.2 / 210.2 | (940, 850) | Heidekloster |
| Bremen | 53.0773 | 8.8029 | 116.4 / 212.6 | (471, 860) | Erzbistum, Weser |
| Kloster Ebstorf | 53.0315 | 10.4196 | 224.8 / 216.8 | (910, 877) | Heidekloster |
| Soltau | 52.9857 | 9.8446 | 186.3 / 222.5 | (754, 900) | Heide-Dorf |
| Uelzen | 52.9648 | 10.5571 | 234.2 / 224.0 | (948, 907) | Hansestadt |
| Verden | 52.9232 | 9.2362 | 145.5 / 229.8 | (589, 930) | Bistum |
| Kloster Walsrode | 52.8607 | 9.5946 | 169.7 / 236.6 | (687, 957) | Heidekloster |
| Celle | 52.6232 | 10.0821 | 202.9 / 262.6 | (821, 1063) | Welfen-Residenz |
| Berlin | 52.5190 | 13.4071 | 428.6 / 265.6 | (1734, 1075) | Mark Brandenburg |
| Hannover | 52.3773 | 9.7321 | 179.5 / 290.3 | (726, 1175) | – |
| Braunschweig | 52.2690 | 10.5279 | 233.9 / 301.5 | (946, 1220) | Welfen |
| Magdeburg | 52.1190 | 11.6279 | 309.6 / 316.0 | (1253, 1279) | Erzbistum, Elbe |
| Hameln | 52.1023 | 9.3571 | 154.1 / 321.1 | (624, 1299) | Rattenfänger, Weser |
| Wittenberg | 51.8648 | 12.6487 | 380.8 / 341.2 | (1541, 1381) | Askanier |
| Brocken | 51.7982 | 10.6154 | 241.0 / 353.7 | (975, 1431) | Finale, Walpurgisnacht |
<!--GEN:PLACES:END-->

*Km O / km S* = Abstand von der Nordwest-Ecke der Karte. *Kartenposition* = Welt-Koordinate im Browser in Höhenpunkten (X nach Osten, Z nach Süden, Ursprung in der NW-Ecke).

**Herkunft der Werte:** Aus den am 31.10.2026 kalibrierten Tiles der alten Pixelkarte zurückgerechnet (`lat = 54,8190 − R/240`, `lon = 7,1529 + Q/240`; Restfehler der Kalibrierung ≤ 6 Tiles ≈ 1–2 km). Die alte Karte (`output_SRTM15Plus.png`, 1704 × 920, 8 Bit, ab 450 m gekappt) wird nicht mehr verwendet.

### Nordseeküste
- Klabautermann (Schiffskobold)
- Wattenmeer-Sagen, Rungholt (untergegangene Stadt)
- Der Blanke Hans (personifizierte Sturmflut)
- Wattjungfrauen (verführen Wanderer ins Watt)

### Norddeutsche Tiefebene / Heide
- Moorleichen, Moorgeister
- Irrlichter / Dwersknarren
- Hügelgräber, Heidnische Kultplätze
- Teufelsstein, Hexentanzplätze
- **Wode / Wilde Jagd** (geisterhafte Schar mit schwarzen Hunden)
- **Heidekönigin** (heidnische Priesterinnen-Figur)
- **Zwerge** in Hügelgräbern (klassisch germanisch: Schmiede, Schatzhüter, unterirdisch)

### Weserbergland
- Rattenfänger von Hameln (130 Kinder, 1284)
- Sachsenherzog-Sagen, Widukind-Motive
- Lindwurm-Sagen (Drache-Echos)
- Münchhausen-Region (Bodenwerder)

### Teutoburger Wald
- Externsteine (vorchristlicher Kultort, Sonnwende-Markierung)
- Irminsul (heiliger Pfahl der Sachsen, von Karl dem Großen zerstört)
- Widukind-Widerstand (heidnische Bastion)

### Mecklenburg / Vorpommern
- **Wode / Wod / Fru Gode** (auch weibliche Form als Anführerin der Wilden Jagd)
- **Vineta** (versunkene Hafenstadt, slawisches Atlantis-Pendant)
- Hexen-Sagen (Wismar, Schwerin)
- Herrgottsfuß (Felsspuren als Heiligen-Eindrücke)

### Spreewald / Lausitz (slawisch geprägt)
- **Schlangenkönig** mit goldener Krone
- **Mittagsfrau / Pšezpólnica** (Rätselgeist, gefährlich auf Feldern)
- **Wassermann / Vodnik** (lockt ins Wasser, grüner Anzug)
- **Lutka** (Hauskobolde)
- Irrlichter (Seelen Ertrunkener)
- **Rusalka** (Wassergeister junger Frauen)

### Harz (thematisches Finale)
- **Brocken:** Hexen, Walpurgisnacht
- Wilde Jagd (Wodan / Hackelberg)
- Teufelsmauer (Teufel als Baumeister)
- Roßtrappe und Hexentanzplatz (Brunhilde, Bodo)
- Frau Holle / Holda (Winter, Spinnerinnen)
- Bergmännchen, Berggeister (Bergbau-Folklore)
- Zwerge, Schatzhüter
- Roland-Sagen

### Wassergeister an Flüssen (regionsübergreifend)

Nixen und verwandte Wassergeister können an allen größeren Flüssen vorkommen:
- **Nixen** (germanisch) – Wassergeister in Frauengestalt, locken Menschen ins Wasser
- An Elbe, Weser, Spree, Aller etc.
- **Rusalka** speziell im slawischen Spreewald-Raum
- Nicht zu verwechseln mit **Sirenen** (griechisch, kulturell fremd – nicht im Spiel)
- Atmosphärisch: Schiffer-Sagen, ertrunkene Frauen kehren als Wassergeister zurück
- Mechanisch könnten sie als Knoten-Wesen oder als Gefahrenfeld an Flussüberquerungen funktionieren

---

## Offene Fragen / Später entscheiden

- **Basis-Bedrohung:** Kann die Basis angegriffen werden? (In Heroes-Kampagnen war sie auch nicht sicher) – noch offen
- Mana/Ressourcen-System im Kampf: Wie werden aktive Fähigkeiten ausgelöst?
- ~~Welche Gebäude-Typen in der Basis konkret?~~ → Vorschlag im Kapitel Heide-Kampagne
- ~~Ort des Phylakteriums~~ → **entschieden 02.11.2026: Hügelgrab in der Lüneburger Heide.** Der Kalkberg bleibt nur Erzählmotiv (siehe Startort)
- Wie wird eine Armee zwischen Expeditionen rekonfiguriert?
- Wände einreißbar / durch große Einheiten überwindbar? *(Erstmal: nein)*
- Werden eigene Tote als Ressource recycled?
- Wie genau verhalten sich "führerlose" Einheiten, wenn ein Anführer fällt?
- **Size 4 auf dem Hex-Grid:** Belegt ein Fleischriese ein Feld oder mehrere? (Visuell ragt er über Nachbarfelder; Regel muss das klar zeigen)
- **Werte von `Rend`** in der Power-Defense-Matrix sind ein erster Vorschlag – im Spieltest prüfen
- **Token-Modus:** automatisch per Zoom oder nur per Taste?
- **HeathSpirits als eigene Fraktion** oder Teil von `Witches`? (Aktuell eigene: Naturgeister haben keinen Zirkel und rivalisieren mit den Druidinnen – passt zum Patchwork der Heide)
- Werte der Heide-Gegner sind erste Vorschläge – im Phase-3-Prototyp gegen Ghul/Skelett testen

**Vorschläge zu offenen Fragen (01.11.2026 – zur Bestätigung):**

| Frage | Vorschlag | Begründung |
|-|-|-|
| Size 4 auf dem Grid | Belegt **1 Feld**, aber **Nachbarfelder kosten Gegner +1 Bewegung** („Masse"). Sockel ragt sichtbar über die Nachbarfelder | Keine Sonderregeln fürs Pathfinding, trotzdem fühlt sich der Riese groß an – und die Optik passt zur Regel |
| Führerlose Einheiten | Fällt ein Anführer und das Budget wird überschritten, erhalten die **zuletzt rekrutierten** Einheiten über dem Limit `Leaderless`: −2 Initiative, kein Konter, verlieren 2 HP/Zug („Zerfall") bis Budget wieder passt oder Kampfende | Spürbar, aber kein sofortiger Verlust; sichtbar über gebrochenes Banner |
| Eigene Tote recyceln | **Ja, bei Sieg**: eigene Gefallene liefern 50 % ihrer Leichen-/Knochenkosten zurück. Geister und Maschinen nichts | Thematisch („ein Lich wirft nichts weg"), mildert Permadeath ohne ihn aufzuheben |
| Token-Modus | **Automatisch** ab Zoom-Schwelle, zusätzlich Taste **T** zum Umschalten | Übersicht ohne Pflicht-Taste, Profis behalten Kontrolle |
| HeathSpirits eigene Fraktion | **Ja, bleibt eigen** | Zwergenkönig und Wode gehören dazu; Witches bleiben die menschlichen Zirkel |

**Bereits entschieden (war ursprünglich offen):**
- Initiative-System → tick-basiert (Wildfrost-artig), `nächster_Zug += 10 - Initiative` (siehe Einheiten-Datenstruktur)
- Sichtberechnung in Stealth-Phase → Raycast statt Höhenmathematik, 90°-Kegel (siehe Sicht- und Sinne-System)
- Freund/Feind-Kennung → über Sockel-Form (glatt/gezackt), nicht nur Farbe

---

## TODO (Implementierung)

**Kamera:**
- Maus-Drehung mit gehaltener Taste
- Maus am Bildschirmrand für Bewegung
- Pivot ans Spielfeld klemmen (kann nicht aus der Welt rausfahren)
- Bewegungsgeschwindigkeit von Zoom-Stufe abhängig machen (rausgezoomt = schneller bewegen)
- Zoom-Schwelle für Token-Modus festlegen

**Weltkarte (Browser):**
- ✅ Prototyp `prototypes/worldmap/index.html`: Gitter folgt Kamera, Zoom-abhängiger Vertex-Abstand, Bodentypen mit weichen Übergängen, Wasser, Orte
- Echtes Höhenmodell (GeoTIFF) → `worldmap.py` → `build_webmap.py --dem`
- Landbedeckung statt Heuristik (`--landcover`), Waldtextur
- Wege-Graph, Reise, anklickbare Knoten
- Fog-of-War- und Gefahren-Maske im Shader
- Flüsse als Linien + Flussnetz als Daten

**Schlachtfeld-Tiles:**
- 28 FloorType-Materialien (eines pro Typ)
- Instanziertes Mesh pro FloorType
- Per-Tile zufällige Y-Rotation in 60°-Schritten (Variation gegen Kachel-Look)
- Tile-Mesh nach unten verlängern, damit zwischen Höhenstufen keine Lücken klaffen
- Optional später: verschiedene Meshes pro FloorType statt nur Material-Varianten

**Gebäude / Objekte:**
- Prozedurale Karten-Generierung mit Footprints (Häuser, Türme, Ruinen)
- Validierung beim Platzieren (Tile frei? Türen zeigen auf begehbares Tile?)
- Zerstörte Wände temporär speichern (Dictionary mit Zerstörungstag, lazy Heilung nach n Tagen)

**Einheiten-Visualisierung (neu):**
- ~~`world_data.js` aus den CSVs erzeugen~~ erledigt (Einheiten, Schadensmatrix, Leichenqualität, Regeln). Offen: Fähigkeiten und Paletten im Spiel nutzen
- `DT_UnitVisuals` anlegen (Modell, Icons, Animationen je Einheit)
- Einheiten-Material mit Primär/Akzent/Leucht-Parametern aus `DT_FactionPalettes`
- Sockel-Mesh (glatt / gezackt / gestrichelt) + Sockel-Zustände (aktiv, ausgewählt, gezogen)
- Lesbare Platzhalter nach Rollen-Grundform, Höhe nach Size
- Overhead-Widget: HP-Segmente, SoulShield-Überlagerung, Status-Icons (max 3), Rang-Abzeichen
- Schadensvorschau: Ghost-Segmente + Effektivitäts-Pfeil aus Power-Defense-Matrix
- Standard-Treffereffekt pro PowerType (11 Stück, zuerst als farbige Platzhalter-Partikel)
- Leichen-Objekt pro Todesart + Hover-Info

**Interaktion:**
- Klick-Detection auf Tiles (über unsichtbares Collision-Mesh, da instanzierte Meshes keine einzelnen Objekte haben)
- Wand-Platzhalter spawnen (rote Rechtecke = Wall, gelbe Dreiecke = Cover, etc.)
- Mouse-Over-Anzeige der Wandtypen bei Tastendruck/Haken
- Alt halten = alle Overheads einblenden

**Wahrnehmung (Stealth-Phase):**
- Sicht/Hören/Geruch an der Einheit speichern (nicht am Tile)
- Sichtkegel 90°, Geruch/Gehör 360° als berechnete Reichweite
- Sichtkegel als Bodendecal, „?" / „!"-Indikatoren über Gegnern

**VR (langfristig):**
- Weltkarte als Tischmodell (Kriegsrat-Fantasie); Streaming entfällt durch die Landschaftskarte

---

## Sicht- und Sinne-System

### Phasen-Aufteilung

- **Stealth-Phase (vor Kampf):** Sicht relevant, Sinne werden geprüft (Sicht 90° Kegel, Geruch/Gehör 360°)
- **Kampf-Phase:** Alle Einheiten gegenseitig sichtbar. Nur Reichweite und Höhe relevant für Angriffe

Sichtberechnung läuft also nur in der Stealth-Phase. Im Kampf entfällt der Aufwand komplett.

### Sichtberechnung

**Berechnungsmodell:** Option 2 (in der Diskussion) – nach jedem Zug alle Einheiten neu berechnen. Bei 8x8 bis 16x16 Feldern und 10-20 Einheiten ist das performance-technisch trivial (Mikrosekunden).

**Algorithmus (90° Kegel, SightRange als Reichweite):**

1. **Blickrichtung:** Eine von 6 Hex-Richtungen
2. **Kegel:** 3 von 6 Richtungen (Blickrichtung + je eine links/rechts)
3. **Eingrenzung:** Rechteckiger Bereich Q±SightRange, R±SightRange
4. **Hex-Distanz:** `max(|ΔQ|, |ΔR|, |ΔQ+ΔR|) ≤ SightRange`
5. **Kegelfilter:** Tile im 90° Sektor?
6. **Sichtlinie:** Visueller Raycast (Line Trace) statt Höhenberechnung

**Wichtig:** Raycast statt Höhenmathematik, weil visuelle Darstellung und berechnete Sichtlinie sonst auseinanderlaufen können. Spieler sieht was das System sieht.

Berechnung läuft parallel zur Bewegungsanimation – synchron nach Animation reicht völlig (Berechnung dauert Mikrosekunden, Animation 0.5-1 Sekunde).

**Raycast-Ziel:** Kopfhöhe der Zieleinheit nach `Size`-Tabelle. Dadurch ist ein Fleischriese hinter einer Mauer sichtbar, ein Skelett nicht – exakt so, wie es auf dem Bildschirm aussieht.

### Einheiten sind stationär in Stealth-Phase

Einheiten haben feste Blickrichtung. Keine Patrouillen, kein automatisches Drehen. Spieler bewegt sich um sie herum.

### Geruch und Gehör

- 360° Radius (kein Kegel)
- HearRadius = wie weit eine Einheit hört
- SmellRadius = wie weit eine Einheit riecht
- Entdeckung durch Gehör: `NoiseLevel` des Eindringlings gegen `HearRadius` des Wächters
- Entdeckung durch Geruch: `ScentLevel` des Eindringlings gegen `SmellRadius` des Wächters
- Geruch wahrscheinlich durch Windrichtung modifiziert (noch nicht implementiert)

### Mechanik: Späher verlieren sich

In Gebieten mit Irrlichtern, Moorgeistern können Späher vom Weg abkommen. Mögliche Konsequenzen:
- Späher kommt verspätet zurück
- Späher kommt mit falschen Informationen zurück
- Späher kommt nicht zurück (verloren/tot)

Gebiete: Teufelsmoor, andere Moore, Spreewald, nebelige Heide-Stellen. Höherwertige Späher (z.B. Geisterspäher) sind weniger anfällig.

---

## Technik (Browser)

**Plattform:** Browser, ohne Engine. Repo: `Frozenenenen/Harmbringer_online`, veröffentlicht über GitHub Pages.

| Teil | Ort im Repo | Technik | Start |
|-|-|-|-|
| Spielbares Spiel | `index.html`, `data/world_data.js`, `data/heightmap.js` | Three.js r160, eine Datei, kein Build-Schritt | Doppelklick (file://) oder GitHub Pages |
| Weltkarte (Prototyp) | `prototypes/worldmap/` | WebGL2 direkt, keine Bibliothek | nur über Webserver / GitHub Pages (lädt Daten per `fetch`) |
| Einheitenbuch | `prototypes/einheitenbuch/` | HTML + SVG | Doppelklick oder GitHub Pages |
| Design und Daten | `design/` (dieses Dokument, CSV-Tabellen) | – | – |
| Werkzeuge | `tools/` | Python 3 (numpy, Pillow nur für die Karten-Pipeline) | Kommandozeile |

### Bausteine

Im Spiel als Klassen in `index.html`:

| Baustein | Aufgabe | Nicht zuständig für |
|-|-|-|
| `WorldData` | Spielwerte aus `world_data.js` bereitstellen | – |
| `Battlefield` | Hex-Gitter des Kampfes: Tiles, `hexToWorld`, Nachbarn, Distanz | Spielregeln, Einheiten |
| `TerrainRenderer` | Weltkarte als Landschaft: Gitter folgt der Kamera, Höhen und Bodentypen aus Datentexturen, Bodentexturen mit weichen Übergängen | – |
| `VegetationRenderer` | Bäume, Büsche, Steine, Gras, Schilf auf der Weltkarte: Low-Poly, instanziert, nach Bodentyp (`VEG_RULES`), 6 % der Felder nehmen den Bodentyp eines Nachbarn für natürliche Ränder | – |
| `TileRenderer` | Hex-Tiles im Kampf zeichnen, ein instanziertes Mesh pro FloorType | – |
| `CameraController` | Bewegen, Drehen, Zoomen | – |

Globale Werte (z. B. Hex-Größe) liegen an einer Stelle. Breite und Höhe des Schlachtfelds gehören dagegen zum jeweiligen Kampf, nicht in die globale Konfiguration.

### Spielwerte

Die CSV-Tabellen in `design/data/` sind die Quelle der Wahrheit. Das Spiel liest `data/world_data.js`; `gen_data.py` schreibt dort die Bereiche zwischen `// <GEN:UNITS>` und `// <GEN:RULES>`:

- **Einheiten:** Die Liste `GAME_UNITS` ordnet jeder Spiel-Kennung (`ghul`, `ritter` …) eine Design-Zeile zu und ergänzt Platzhalter-Form, Farbe und Wissens-Voraussetzung. Knochenkosten zählt das Spiel 60-fach.
- **Regeln:** Schadensmatrix (inkl. Reißen), Leichenqualität je Schadensart, Initiative `2520 / Ini` (eine Runde = 1008 Ticks), MagicResist prozentual, SoulShield als Pool, der jeden Schaden zuerst schluckt und sich im Kampf nicht erneuert.
- **Stapel (wie Heroes of Might and Magic):** Gleiche Einheiten einer Seite stehen im Kampf als *eine* Figur mit Anzahl (×3). Schaden des Stapels = Einzelschaden × Anzahl (Konter ebenso). Erlittener Schaden wird vom Gesamt-LP abgezogen; es sterben so viele, wie der Schaden hergibt, nur die vorderste Einheit ist angeschlagen (3 × 8 LP, 12 Schaden → 1 tot, 1 mit 4 LP, 1 unversehrt). Heilung flickt nur die vorderste, erweckt keine Toten. SoulShield-Pool = Wert × Anzahl. Jede gefallene Einheit bringt Beute. Auf der Weltkarte bleibt die Armee eine Liste einzelner Untoter (Rekrutierung, Kommando-Punkte).
- **Mengen ×4 (Stapel-System):** Startarmee Lich + 12 Ghule + 8 Skelette, Besatzungen ×4 (Unikate bleiben einzeln), Startressourcen und Eroberungsbeute ×4 (Wissen unverändert), Kommando-Limit 60 (+12 je mythischem Ort), Bedrohung +4 Einheiten je 25 %. Beute pro Kill bleibt gleich – bei viermal so vielen Gegnern ergibt das von selbst ×4.
- **Gegner-Stapel aufteilen:** Eine Einheitenart darf auf bis zu 3 Stapel verteilt werden, jeder Teil behält mindestens 4 Einheiten. Höchstens 8 Stapel, und die nur ab 4 verschiedenen Einheitentypen; darunter höchstens 2 Stapel pro Typ (Dorf: 2 × 8 Bauern statt 1 × 16). Regeln in `world_data.js` → `stacks`. Spieler-Stapel teilen kommt später.
- **Ziehen und Angreifen in beliebiger Reihenfolge:** Jede Einheit darf pro Zug einmal ziehen und einmal angreifen. Greift sie zuerst an, bleiben danach nur 2/3 ihrer Bewegung (abgerundet, mindestens 1 Feld) – Fernkämpfer können so zurückweichen, aber nicht weit.
- **Lich wächst mit der Armee:** Zu Kampfbeginn pro belegtem Kommando-Punkt +2 LP, +0,25 Schaden, +0,25 Seelenschild (Startarmee mit 32 Punkten: 104 LP, 16 Schaden, 18 Seelenschild). Der Bonus gilt nur im Kampf; Wunden werden anteilig auf die Kampagnen-LP umgerechnet.
- **Weitere Orte (Nov. 2026):** 126 neue Orte füllen die ganze Karte – Holstein, Lübeck und Schleswig im Norden, Mecklenburg und Pommern mit Rügen, Uckermark, Havelland und Lausitz im Osten, Anhalt, Saale und Leipzig im Südosten, der Harzrand mit Goslar, Halberstadt und Quedlinburg, Weserbergland und Westfalen, Oldenburg und Ostfriesland im Westen. Neue Fraktionen: **Grafen** (Holstein, Oldenburg, Hoya, Mansfeld, Hessen), **Mecklenburg**, **Wettiner**. Mythische Orte nutzen die Heide- und Druiden-Einheiten aus den Design-Daten (Kleriker, Heideschwester, Druide, Hügelgrab-Druidin, Schwarzer Hund, Wode, Zwergenkönig, Heidekönigin).
- **Besondere Orte (★):** 26 Orte bringen etwas Besonderes (`world_data.js` → `specials`):
  - *Einkommen pro Tag*, solange sie den Untoten gehören: Salinen Lüneburg und Halle (Leichen), Rammelsberg, Kalkberg Segeberg, Mansfelder Kupfer (Knochen), Vineta und Externsteine (Seelen), Dümmer-Moor (Leichen).
  - *Dauerhafte Vorteile:* Kontor in Lübeck und Hexentanzplatz (Reisetempo), Teufelsmauer (Schaden), Pestruper Gräberfeld und Arendsee (Beute), Kloster Doberan (Heilung), Externsteine (Magieresistenz).
  - *Artefakte* beim Erobern: Reichsschwert (Kyffhäuser), Glocke von Rungholt, Trinkhorn des Svantevit (Arkona), Krone des Schlangenkönigs (Spreewald), Lehniner Weissagung, Merseburger Zaubersprüche, Reliquienkasten (Quedlinburg), Zwergenhammer (Iberg), Horn der Wilden Jagd (Hackelbergs Grab), Codex von Corvey, Hünenknochen (Sieben Steinhäuser), Herz der Heide (Oldendorfer Totenstatt).
- **Zufallsbegegnungen unterwegs:** Jeder unbesiegte Ort, an dem die Reise vorbeiführt (bis 30 Felder neben dem Weg), erhöht die Gefahr: Dorf 0,5, kleiner Ort 1, mittlerer 2, großer 3. Pro Reisetag wird gewürfelt: 3 % + 4 % je Gefahrenpunkt (höchstens 60 %), höchstens ein Hinterhalt pro Reise. Die Gegner stammen aus dem gefährlichsten passierten Ort (ohne Unikate), ihre Zahl wächst mit der Gefahr (8 + 6 je Punkt, höchstens 64) plus Bedrohungs-Verstärkung der Fraktion. Gekämpft wird auf einem 16er-Feld am Weg; nach einem Sieg geht die Reise weiter, es gibt nur die Beute der Gefallenen (kein Ort, keine Bedrohung). Die Ortsinfo zeigt vor der Reise die Zahl der Orte am Weg und die Hinterhalt-Wahrscheinlichkeit. Werte: `world_data.js` → `encounters`.
- **Rekrutieren in eroberten Orten:** Im Hügelgrab alle Einheiten. In eroberten Städten Ghul, Zombie, Leichenhund, Skelett, Bogenschütze, Knochenschleuderer; in Klöstern Zombie und Knochen-Einheiten (Friedhof); an mythischen Orten Ghul, Leichenhund und Geist. Dörfer nicht. Heilen weiterhin nur im Hügelgrab. Tabelle `RECRUIT_AT` in `index.html`. Seit Nov. 2026 zusätzlich die fortgeschrittenen Untoten aus den Design-Daten, freigeschaltet über Wissen: Knochenschütze und Moorleiche (4), Todesritter und Totenlicht (5), Gefallene Schwester, Grabdruidin und Nekromant (6, Anführer: +4 Kommando), Fleischriese (3), Knochenballiste (7), Totenjäger und Knochendrache (10). Der **Knochendrache** (neu): 120 LP, fliegt, Bewegung 6, Totenhauch (Seele, Reichweite 2, 18 Schaden), schwere Knochenrüstung, 16 Kommando, 1800 Knochen und 6 Seelen; im Hügelgrab und an mythischen Orten. Fleischriese zusätzlich in Klöstern. Städte: Knochenschütze, Todesritter, Knochenballiste, Fleischriese; Klöster: Knochenschütze, Gefallene Schwester, Nekromant; mythische Orte: Moorleiche, Totenlicht, Grabdruidin, Nekromant, Totenjäger.
- **Inventar:** Taste I oder Knopf „Inventar“. Artefakte sammeln sich dort; **3 Plätze** zum Anlegen, nur angelegte wirken. Das Inventar zeigt auch die eroberten besonderen Orte, die Summe aller Vorteile und das Tageseinkommen. Vorteile für Untote gelten nur im Kampf (kopierte Werte), nach dem Kampf werden die LP auf die normalen Werte zurückgerechnet.

Fraktionen, Orte, Gebäude und Wirtschaft in `world_data.js` sind weiterhin von Hand gepflegt. Die zehn Einheiten, die es bisher nur im Spiel gab (z. B. Ritter, Stadtwache, Priester, Hexenkönigin), stehen jetzt mit ihren bisherigen Werten in den CSVs.

| Datei | Inhalt |
|-|-|
| `DT_Units.csv` | 28 Einheiten |
| `DT_Abilities.csv` | 36 Fähigkeiten |
| `DT_FactionPalettes.csv` | 9 Fraktionen; Farben als Hex und in Linear-Space |
| `DT_DamageMatrix.csv` | Power-Defense-Matrix, Zeile = PowerType |
| `DT_Buildings.csv` | 17 Gebäude-Stufen |
| `DT_Knowledge.csv` | 8 Wissens-Freischaltungen |
| `DT_Encounters.csv` | 6 Begegnungen der Heide (NodeType: Mythic, Secular, Christian; TimeOfDay: Night, Morning, Day, Evening) |

Erste Spalte `Name` = Zeilenname, über den Tabellen aufeinander verweisen (z. B. `Abilities` in `DT_Units`). Enum-Werte stehen als Namen (`Rend`, `Warrior`).

**Werkzeuge** in `tools/`:
- `gen_data.py` – Quelle der Wahrheit für Einheiten und Fähigkeiten; schreibt alle CSVs und erneuert die generierten Tabellen in diesem Dokument (inkl. Inhaltsverzeichnis)
- `campaign_data.py` – Gebäude, Wissen, Begegnungen, Orte
- `rules.py` – Schadensformel, Matrix, Initiative
- `sim.py` / `encounter_check.py` – Balancing- und Schlacht-Simulation
- `geo.py`, `worldmap.py`, `build_webmap.py` – Projektion und Daten der Weltkarte
- `build_gallery.py` – baut das Einheitenbuch aus den CSVs
- `build_game_map.py` – rechnet die alte Höhenkarte ins UTM-Kampagnenraster des Spiels um (`data/heightmap.js`, 2017 × 1583 Hex-Felder, gleich groß in beide Richtungen, 16 Bit in Metern). Die alte Karte endet bei 450 m; darüber wird der Harz aus bekannten Gipfel- und Ortshöhen genähert (Thin-Plate-Spline plus Rauschen), bis ein echtes Höhenmodell vorliegt; `--tile <lat> <lon>` gibt das Feld eines Orts
- `build_units.py` – baut **alle Einheiten** als eigene Low-Poly-Figuren in einheitlichem Stil (Bauteile: Beine, Rumpf, Robe, Skelett, Geisterkörper, Irrlicht; Ausrüstung: Speer, Schwert, Schild, Bogen, Armbrust, Stab, Hammer, Kronen, Hüte, Geweihe). Echte Größen: Mensch 1,8, Zwerg kleiner, Fleischriese größer, Hunde und Irrlichter klein. Diese Figuren nutzt das Spiel; die Godot-Figuren bleiben als Vorlage
- `slim_figures.py` – verkleinert die Figuren aus dem Godot-Projekt (`models/Figures`, nur lesend) für den Browser: Geometrie quantisiert, nur Farbtextur 512 px; 90 Figuren von 1,08 GB auf 42 MB (`assets/figures/`, Betrachter `prototypes/figuren/`)
- `build_game_textures.py` – bettet die Bodentexturen als Data-URIs in `data/ground_textures.js` ein (nötig für file://)

Generierte Bereiche sind mit `<!--GEN:…:BEGIN/END-->` markiert – dort nicht von Hand editieren. **Workflow:** Werte im Generator ändern, `python tools/gen_data.py` ausführen, dann sind CSV, Dokument und `data/world_data.js` synchron.

### Ereignisse (geplant)

Ein zentraler Ereignis-Verteiler (`on` / `emit`) mit:
- `unitDied`, `unitTookDamage`, `unitMoved`
- `turnStarted`, `turnEnded`
- `damageDealt` (für Trigger wie Gift bei Treffer)

Jede Einheit mit Trigger-Fähigkeit meldet sich beim Erzeugen für die passenden Ereignisse an (OnDeath, OnAllyDeath usw.). Die Darstellung hängt sich an dieselben Ereignisse – keine eigene Logik in der Darstellung.

### Einheiten-Darstellung

- **Modell:** Platzhalter-Grundform nach Rolle, später glTF-Modell; Material mit Fraktionsfarben aus `DT_FactionPalettes`
- **Sockel-Ring:** Form nach Seite, Farbe nach Fraktion
- **Anzeige über der Einheit:** HP-Segmente, Status, Rang (HTML-Overlay oder Sprite)
- **Blickrichtungs-Pfeil** und **Sichtkegel** als Boden-Overlay, nur in der Stealth-Phase
- `setVisualState(state)` – eine zentrale Funktion schaltet Material-Werte, Overlays und Idle-Animation um. Aufgerufen über Ereignisse (`unitTookDamage` → Wounded/Dying prüfen)

### Assets bei Bedarf laden

Effekte, Sounds und Animationen werden erst geladen, wenn sie gebraucht werden. Ausnahme: Beim Kampfstart werden die Treffer-Effekte der PowerTypes vorgeladen, die auf dem Feld vorkommen – keine Verzögerung beim ersten Treffer.

### Modelle (Blender / Meshy)

1. Als glTF (`.glb`) exportieren
2. Eine zweite, vereinfachte Stufe mit ca. 15 % der Dreiecke für weite Zoomstufen
3. Gegen die Lesbarkeits-Checkliste prüfen. Häufige Korrektur: Rollen-Merkmal (Stab, Banner) vergrößern, Fraktionsfarben über das Einheiten-Material statt über die Original-Textur

---

## Story- und UI-Konzept

### Initiative-Anzeige im Kampf

Horizontale Leiste am unteren Bildschirmrand mit 10-12 Avataren der nächsten Einheiten:
- Aktive Einheit ganz links, **50-100% größer** dargestellt
- Avatar = Portrait der Einheit (Dark Fantasy Oil Painting Stil)
- Fraktionsfarbe als Rahmen; **Rahmenform** wie Sockel (glatt = Spieler, gezackt = Feind)
- Rollen-Icon klein unten links am Portrait
- HP-Balken klein darunter (segmentiert wie Overhead), Energy-Anzeige bei aktiver Einheit
- Status-Icons am Rand (vergiftet, gestärkt etc.)
- Opazitäts-Verlauf nach hinten
- Hover über Portrait hebt die Einheit auf dem Feld hervor (und umgekehrt)

Tick-basiertes System: Nicht jede Einheit hat einen Zug pro Runde, Häufigkeit ergibt sich aus Initiative.

### Dialog-Leiste (Story-Modus)

Untere Dialog-Leiste:
- **Charakter-Dialog:** Avatar links mit Fraktionsfarben-Rahmen, Charaktername in Kapitälchen, Sans-Serif Text
- **Erzähler-Eintrag:** Buch-Icon statt Avatar, pergamentfarbener Akzent (Bordeaux-Linie links), kursiver Serif-Text

Klare visuelle Unterscheidung zwischen Charakter-Dialog und Erzähler-Chronist.

### Vollbild-Untermalung

Für dramatische Story-Momente: Mauer stürzt ein, Haus in Flammen, Lich steigt aus Grab. Mittig im Bildschirm, parallel zum Dialog.

### Erzähler-Konzept

Ein Erzähler als ergänzende Stimme zum Charakter-Dialog. Vorteile:
- Andere Stimme als die hetzerische Lich-Perspektive
- Erklärt Hintergründe, Geschichte, Zusammenhänge
- Märchenhaft-düstere Atmosphäre passend zu deutscher Mythologie
- Tradition der Sagensammlungen (Brüder Grimm)

Beispiel-Ton: "Es war im Jahre des Herrn 1370, als sich die Erde über einem alten Hügelgrab in der Heide regte..."

Eine konsistente Erzählerstimme durchgehend (keine regionalen Dialekte – nicht verfügbar). Wortwahl kann regional färben (sorbische Begriffe im Spreewald-Kapitel).

### KI-Bilder Stil-Konsistenz

Basis-Prompt für alle Einheiten-Portraits:
```
Dark fantasy illustration style, inspired by 1980s fantasy book cover art, oil painting aesthetic, dramatic chiaroscuro lighting, muted earth tones with deep shadows, highly detailed, Germanic medieval setting, gritty and atmospheric, no modern elements
```

Für Spreewald-Fraktion zusätzlich:
```
Slavic folklore creature, Sorbian mythology, swamp dwelling, waterlogged appearance, pale skin, reeds and mist
```

Für Wode/Wodan: Im Prompt **Odin** verwenden (mehr Trainingsdaten), im Spiel selbst **Wode** behalten.

Rollen-Zusätze und Fraktions-Leuchtfarben: siehe Einheiten-Visualisierung → Portrait-Prompts.

### Engel-Konzept (Clergy)

Biblisch-korrekte Engel statt romantisierter Flügelwesen:
- **Seraph:** 6 Flügel, feurig, blendend (Jesaja 6)
- **Cherub:** 4 Gesichter (Mensch/Löwe/Stier/Adler), Körper voller Augen (Ezechiel)
- **Ophanim:** Brennende Räder voller Augen, keine humanoide Form (Ezechiel)

Sehr alien-artig, passt zu düster-mythologischem Setting. **Lesbarkeit:** Engel sind die einzigen Clergy-Einheiten mit starkem Leuchten (Kerzengold) – sofort als übernatürliche Bedrohung erkennbar. Ophanim als `Size 3`, Seraph/Cherub als `Size 3–4`.

---

## Schnittstellen zwischen Systemen

Bewusstes Festlegen früh, weil falsche Interfaces später teuer in der Korrektur sind. Implementierungen unter stabilem Interface können jederzeit ausgetauscht werden.

### Kampf ↔ Kampagne

**Was IN den Kampf reingeht:**
- Region (für Optik/Atmosphäre)
- Knoten-Typ (Dorf, Kloster, Hexenzirkel, Hauptsitz)
- Gegner (Liste von Gegnertypen + Mengen)
- Eigene Einheiten (Liste der mitgenommenen)
- Anführer dabei
- Stealth-Bedingungen (Wind, Tageszeit)
- Schlachtfeld-Layout (Hindernisse, Höhenkarte)

**Was AUS dem Kampf rauskommt – nur zwei Zustände:**

**A) Sieg:**
- Überlebende Einheiten kommen zurück
- Geerntete Leichen mit Qualitätsstufen je Schadenstyp
- Seelen
- Wissen (aus besiegtem Pantheon-Mitglied)
- Eventuell neue Einheiten/Anführer aus Gräbern erweckt
- Welche besonderen Gegner besiegt (Pantheon-Tracking)

**B) Lich-Rückzug oder erzwungene Niederlage:**
- Alle eingesetzten Einheiten verloren
- Keine Ressourcen mit (Teleport-Magie nicht aktivierbar)
- Mana-Strafe (Rückzug billiger als erzwungen)
- Bedrohungsstufe der Fraktion sinkt (sie haben gewonnen)
- Lich braucht Wartezeit zur Rückkehr

### Einheiten-Datenstruktur

**EinheitenTyp** (die Klasse): Skelett-Speerträger als Konzept
- Stats (HP, Angriff, Bewegung, Initiative)
- Stealth-Werte (Größe, Lautstärke, Geruch)
- Schadenstyp
- Aktive Fähigkeiten
- Rolle und Visual-Zeile (`DT_UnitVisuals`)

**EinheitenInstanz** (konkretes Exemplar):
- Nur für Anführer und einzigartige Einheiten
- Massen-Einheiten haben **keine** individuelle Identität – sind nur Mengen pro Typ
- Keine individuelle Erfahrung, kein Leveln pro Einheit
- Verstärkung passiert auf Klassen-Ebene durch Basis-Forschung

### Daten ↔ Visualisierung

- Spiellogik schreibt nur Zustände (HP, Status, VisualState) und sendet Ereignisse
- Visual-Komponenten lesen nur, entscheiden nie über Regeln
- Folge: Platzhalter, finale Modelle und Token-Modus sind austauschbar, ohne Spiellogik anzufassen

### Weitere Schnittstellen (zu definieren)

- Kampagne ↔ Basis: Wechsel zwischen Karte und Basis, Ressourcen-Übergabe
- Basis ↔ Armee-Komposition: Auswahl der Einheiten für nächste Expedition
- Späher ↔ Kampagne: Welche Information liefern Späher?
- Pantheon ↔ Region/Welt: Verbindung von Pantheon-Mitgliedern, Knoten und Regionsstatus

---

## Entwicklungs-Roadmap

**Strategie: Vertikal arbeiten, nicht horizontal.** Erst eine dünne Säule durch alle Systeme bauen (Mini-Versionen), dann jedes System verbreitern. Das hält die Motivation hoch und testet früh, ob das Spielkonzept tatsächlich Spaß macht.

### Phase 1: Kampfsystem-Prototyp

Ziel: Ein einzelner Kampf mit Bewegung, Angriff, Sieg/Niederlage – funktional, hässlich, **aber lesbar**.

- ✅ Hex-Grid generieren
- ✅ Spielfigur platzieren
- Kacheln anklickbar machen
- Figur per Klick bewegen
- Mehrere Einheiten verwalten (Spieler-Truppe vs. Feinde)
- Rundensystem (wer ist dran)
- Initiative-Reihenfolge
- Angriff-Mechanik (Reichweite, Schaden, HP)
- Sieg-/Niederlage-Bedingung
- **Lesbare Platzhalter** (Rollen-Grundform, Höhe nach Size)
- **Hex-Sockel** Freund/Feind + aktive Einheit hervorgehoben
- **HP-Segmente** über den Einheiten

### Phase 2: Mini-Kampagne (Vertical Slice First)

Ziel: Den kompletten Spielloop erstmals schließen, alles auf primitivstem Niveau.

- Mini-Kampagnen-Karte (3 Knoten in einer Linie, Klick = Kampf laden)
- Mini-Basis (ein Raum mit einem Gebäude, das eine Einheit produziert)
- Übergang Kampf → Karte → Basis → Karte → Kampf funktional
- Leichen als einfache Ressource (eine Zahl)
- Sieg über alle 3 Knoten = Spiel "gewonnen"
- **Fraktionsfarben** über `DT_FactionPalettes` + Einheiten-Material
- **Rollen-Icons** und Initiative-Leiste mit Platzhalter-Portraits

**An diesem Punkt ist das Spiel zum ersten Mal SPIELBAR.** Hier kann beurteilt werden, ob der Loop trägt.

### Phase 3: Kampfsystem-Tiefe

Ziel: Aus simplem Kampf wird taktischer Kampf.

- Bewegungsreichweite mit Pathfinding (Dijkstra oder A*)
- Hindernisse auf Kacheln
- Wand-Kanten-System (Deckung)
- Höhenunterschiede
- Sichtlinien
- Schadenstypen (Stich, Stumpf, Zerfleischen, Feuer, etc.)
- Aktive Fähigkeiten (eine erste Beispielfähigkeit)
- Verschiedene Einheitentypen (3–4 verschiedene)
- Stealth-Phase (Annäherung vor Kampfbeginn)
- Überraschungsangriff
- **Schadensvorschau** (Ghost-Segmente, Effektivitäts-Pfeil, Konter-Hinweis)
- **VFX-Farbcode** pro PowerType (Platzhalter-Partikel)
- **Status-Icons** und Rang-Abzeichen
- **Stealth-Darstellung:** Sichtkegel, „?"/„!", Hidden-Look

### Phase 4: Kampagnen-Schicht

Ziel: Mehrere Kämpfe hintereinander, mit echter Verbindung und Tiefe.

- Vollständige Kampagnen-Karte als Landschaft aus der Höhenkarte (Hub-and-Spoke vom Phylakterium)
- Späher-System & Fog of War
- Reise zwischen Knoten
- Verschiedene Kampf-Szenen (nicht jedes Mal dasselbe Brett)
- Pantheon-Konzept als Datenstruktur
- Pantheon-Komplettierung als Region-Sieg
- Erste Bedrohungsstufe-Mechanik

### Phase 5: Basis & Wirtschaft

Ziel: Zwischen den Kämpfen hat der Spieler echte Entscheidungen.

- Basis-Ansicht (Phylakterium im Hügelgrab in der Heide)
- Leichen-Ressource mit Qualitätsstufen
- Mehrere Gebäude (Knochenwerkstatt, Seelenzwinger, Wissensaltar)
- Einheiten-Produktion mit Kosten
- Anführer-System
- Gräber als Rekrutierungsorte für einzigartige Anführer
- Verbrannte-Erde-Logik (endliche Quellen)
- **Leichen-Qualität sichtbar** auf dem Schlachtfeld (Leichen-Set)
- **Befehls-Aura** und Leaderless-Zustand

### Phase 6: Erste vollständige Region

Ziel: **Vertical Slice "Lüneburger Heide"** – diese eine Region komplett ausgespielt.

- Alle Mythen-Knoten der Heide implementieren
- Christliche Knoten (Heideklöster) implementieren
- Weltliche Knoten (Lüneburg) implementieren
- Konkrete Einheiten der Heide-Mythologie
- Konkrete Einheiten der Lich-Armee
- Story-Elemente und Atmosphäre
- Erste Ley-Knoten-Mechanik
- Pantheon-Komplettierung mit Belohnungen
- **Echte Modelle der 10 Steckbrief-Einheiten**, jede durch die Lesbarkeits-Checkliste
- **Untote Versionen** besiegter Heide-Gegner (Palette-Tausch)

### Phase 7: Inhalts-Erweiterung

Ziel: Vom Vertical Slice zum vollen Spiel.

- Nordsee-Region (Klabautermann, Rungholt)
- Weserbergland (Rattenfänger)
- Mecklenburg (Wodan-Kult)
- Spreewald (Irrlichter, Schlangenkönig)
- Teutoburger Wald (Externsteine)
- Harz als Finale (Brocken, Walpurgisnacht)
- Weitere Anführer-Klassen
- Erweiterte Schadens- und Magie-Systeme
- Späher-Stufen
- Parallele Kreuzzüge

### Phase 8: Polish & Veröffentlichung

Ziel: Aus "es funktioniert" wird "es ist gut".

- Echte 3D-Modelle statt Platzhalter (restliche Einheiten und Gebäude)
- UI-Design
- Sound und Musik
- Animationen (Antizipation, Wounded-Idles, Fähigkeits-Einblendungen)
- **Token-Modus** für Strategie-Zoom
- Finale Portraits
- Tutorial / Onboarding
- Hauptmenü, Speichern/Laden
- Lokalisierung
- Bugfixing
- Performance-Optimierung
- Release-Vorbereitung

---

### Strategie-Hinweise zum Vertical-Slice-Ansatz

**Bewusst akzeptieren:** Manche Dinge werden zweimal gebaut, weil die primitive Version später ersetzt wird. Das ist die Bezahlung für frühe Spielbarkeit.

**Klare Schnittstellen:** Mini-Systeme melden Ergebnisse einfach (z.B. "Sieg" oder "Niederlage" an die Kampagne), egal wie sie intern arbeiten. Das macht spätere Austausche einfach.

**Daten-Trennung:** Einheiten-Werte als Tabellen (CSV), nicht fest im Code. Werte können dann ohne Code-Änderung balanciert werden. Visuals in eigener Tabelle (`DT_UnitVisuals`), damit Balancing und Optik unabhängig iterieren.

**Lesbarkeit vor Schönheit:** Ein hässlicher, aber eindeutig lesbarer Platzhalter ist im Prototyp mehr wert als ein schönes Modell, das man nicht einordnen kann.

**Bewusstes Wegwerfen:** Manchmal ist es besser, ein System neu zu schreiben, als ein primitives weiterzuwurschteln. Die erste Version war zum Lernen.

**Phasen-Disziplin:** Eine Phase auf einmal. Während Phase X läuft, keine Features für Phase Y einbauen, auch wenn die Idee gerade kommt – stattdessen in dieses Dokument notieren.
