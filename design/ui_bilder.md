# Harmbringer – Bilder für das UI

Stand und Prompts für alle Bilder der Oberfläche. Kevin erzeugt die Bilder, Claude baut sie ein.

- **Offene Bilder stehen oben**, erledigte unten. Neue Bilder kommen in die offene Liste.
- **Ablage:** Kevin gibt die Bilder an Claude; Claude legt sie unter `assets/ui/<Dateiname>` ab, verkleinert sie und baut sie ein.
- **Format:** PNG oder JPG, so groß wie möglich. Auflösung egal, das Verhältnis zählt. Claude verkleinert.
- **Nummern** (Kevin, 18.11.2026): Jedes Bild hat eine feste Nummer (Nr. 001 bis Nr. 412), zum Wiederfinden per Suche, z. B. „Nr. 042“. Die Nummer bleibt, auch wenn ein Bild nach „Erledigt“ wandert oder umsortiert wird. Neue Bilder bekommen die nächste freie Nummer – zuletzt vergeben: **Nr. 412**.
- **Später überarbeiten:** Bilder, die nicht ganz passen, bleiben drin und stehen in der Liste „Später überarbeiten“ (vor „Erledigt“).
- **Seitenverhältnis nie im Prompt** (Kevin, 18.11.2026): Das Verhältnis wird im Bildprogramm vor dem Erzeugen eingestellt, der Prompt kann es nicht mehr ändern. Es steht deshalb nur in der Überschrift hinter dem Dateinamen (z. B. „· 21:9“) – dort ablesen und im Programm einstellen. Prompts beschreiben nur Motiv, Standpunkt und Stil.
- **Symbole:** schwarze Linien auf hellem Papier. Claude legt sie im Spiel per „Multiplizieren“ über den Papiergrund, ein freigestellter Hintergrund ist nicht nötig.
- **Texturen** (Papier): sollten sich kacheln lassen. Wenn nicht ganz, macht Claude sie nahtlos.
- **Prompts auf Englisch**, weil die meisten Bildmodelle damit am besten arbeiten. Der Stilteil ist in jedem Prompt gleich, damit alles zusammenpasst.
- **Bildkomposition muss stimmen** (Kevin, 18.11.2026): Jeder Prompt für eine Szene nennt Standpunkt und Blickwinkel und zeigt nur, was von dort aus sichtbar ist – z. B. nichts hinter einer Mauer, wenn man davor steht; Innen und Außen zugleich nur als bewusster Schnitt.
- Erzeugt das Programm Schrift, Signaturen oder Dürers Monogramm „AD“ mit, bitte neu erzeugen oder Claude sagen, er entfernt es.

## Stil

Vorbild Albrecht Dürer: Holzschnitt und Kupferstich um 1500, feine Kreuzschraffur, schwarz auf vergilbtem Papier, düster, Totentanz, Memento mori.

**Negativ-Prompt (für alle Bilder, falls das Programm einen hat):**

```
color, colorful, photo, 3d render, glossy, modern, anime, cartoon, text, letters, numbers, watermark, signature, monogram, logo, blurry
```

### Stil je Epoche (New Game+, festgelegt 18.11.2026)

Jede Epoche des New Game+ (Design-Dokument „New Game+“, Abschnitt 7) bekommt den Bildstil ihrer Zeit, damit man schon an den Bildern sieht, in welchem Jahrhundert man spielt. Vorbilder sind Druckgrafiken aus Norddeutschland und Mitteleuropa, die es in dieser Zeit wirklich gab. Gleich bleibt in allen Epochen: Druckgrafik auf altem Papier, düster, Totentanz, Standpunkt und Blickwinkel im Prompt. Der Stilteil ersetzt im Prompt den Dürer-Teil, alles andere bleibt.

| Epoche | Vorbild | Technik und Wirkung | Farbe |
|-|-|-|-|
| **1371** (Grundspiel) | Albrecht Dürer, um 1500 | Holzschnitt und Kupferstich, feine Kreuzschraffur, hoher Kontrast | schwarz auf vergilbtem Papier |
| **1471** | Schedelsche Weltchronik (Michael Wolgemut, 1493), Martin Schongauer; Lübecker Totentanz (Bernt Notke, 1463) | kräftiger, etwas derber Holzschnitt mit dicken Konturen, einfache Schraffur, Städte als Stadtansicht | sparsam handkoloriert: Rot, Ocker, Grün in dünnen Wasserfarben, Linien bleiben schwarz |
| **1571** | Pieter Bruegel d. Ä. (Stiche bei Hieronymus Cock, 1550er–60er), Braun & Hogenberg, „Civitates Orbis Terrarum“ (1572); Holbeins Totentanz (1538) | feiner Kupferstich, Wimmelszenen mit vielen kleinen Figuren, Städte in Vogelschau | handkoloriert in gedeckten Wasserfarben: Ziegelrot, Ocker, Grün, Blaugrau |
| **1671** | Matthäus Merian, „Topographia Germaniae“ (1640er–50er); Jacques Callot, „Die großen Schrecken des Krieges“ (1633) | barocke Radierung, feine geätzte Linien, weite Landschaften, dramatischer Himmel, Grauen des Krieges | Sepia und Schwarz auf cremefarbenem Papier, keine Farbe |
| **1771** (Idee) | Daniel Chodowiecki (Berlin); Francisco de Goya, „Los Caprichos“ (1799) | Radierung mit Aquatinta: weiche Grauflächen, Nacht und Schatten als Flächen, unheimliche Figuren | Grau- und Brauntöne, keine Farbe |
| *1871* (falls es so weit kommt) | Gustave Doré, Adolph Menzel | Holzstich (Xylografie) des 19. Jahrhunderts, feinste Linien, Licht und Nebel sehr plastisch | schwarz-weiß |

**Stilteil der Prompts (Englisch, ans Ende jedes Prompts):**

- **1371:** `in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371`
- **1471:** `in the style of the woodcuts of the Nuremberg Chronicle (1493) and the prints of Martin Schongauer, late 15th-century German woodcut with bold black outlines and simple parallel hatching, sparsely hand-coloured with thin washes of red, ochre and green, aged rag paper, grim, macabre, Danse Macabre mood, northern Germany around 1471`
- **1571:** `in the style of 16th-century Netherlandish and German copper engravings after Pieter Bruegel the Elder and the city views of Braun and Hogenberg's Civitates Orbis Terrarum, fine engraved lines, many small figures, hand-coloured with muted watercolour in brick red, ochre, green and blue-grey, aged paper, grim, macabre, northern Germany around 1571`
- **1671:** `in the style of 17th-century Baroque etchings by Matthäus Merian and Jacques Callot's Miseries of War, fine etched lines, wide landscape, dramatic sky, sepia and black ink on cream paper, no colour, grim, macabre, the horrors of war, northern Germany around 1671`
- **1771:** `in the style of late 18th-century etching and aquatint after Daniel Chodowiecki and Francisco de Goya's Los Caprichos, soft tonal grey aquatint areas, deep shadows, uncanny figures, brown-grey ink on cream paper, no colour, grim, macabre, northern Germany around 1771`

**Negativ-Prompt je Epoche:** 1371, 1671, 1771 wie oben (ohne Farbe). Für 1471 und 1571 `color, colorful` weglassen, dafür `saturated colors, bright colors` nehmen:

```
saturated colors, bright colors, photo, 3d render, glossy, modern, anime, cartoon, text, letters, numbers, watermark, signature, monogram, logo, blurry
```

**Oberfläche:** Papier und Rahmen des UI folgen der Epoche (1471/1571 wärmeres Papier mit Farbspuren, 1671 cremefarben mit Sepia, 1771 kühleres Grau). Eigene Papier- und Rahmenbilder je Epoche kommen in die Liste, wenn die Epoche gebaut wird.

## Offen

341 Bilder. Reihenfolge = Priorität (Abschnitt 1–4 machen das UI schon spürbar schöner). Abschnitt 0 sind die neuesten.

### 0 Neu am 18.11.2026 (abends): Story-Bilder für jeden Ort, jedes Artefakt und jeden Kommandeur

Kevins Wunsch: Jeder Ort, jedes Artefakt und jeder Kommandeur bekommt ein Story-Bild. 204 Bilder, alle **21:9** wie die fertigen Story-Bilder (unten bei „Erledigt“), Ablage `assets/story/<Dateiname>`. Fehlt ein Bild, zeigt das Spiel den gezeichneten Platzhalter mit dem Titel – man kann also nach und nach liefern. Texte und Auslöser: `story` in `data/world_data.js` (`on: "battle"` + `at: <Ort>` vor dem ersten Angriff, `on: "artifact"` beim Fund, `on: "commander"` beim Erwecken oder ersten Rekrutieren). Jeder Prompt nennt Standpunkt und Blickwinkel; das untere Drittel bleibt ruhig für den Text.

**Orte (noch 152 offen, sortiert nach Entfernung vom Hügelgrab – die ersten braucht man zuerst; Kommandeure, Artefakte und die ersten 33 Orte sind fertig, siehe „Erledigt“)**

#### Nr. 053 · `story/ort_achim.jpg` · 21:9
Verwendung: Erster Angriff auf Achim (Dorf, 16×16)

```
grey day, viewpoint: standing on top of a river dike at eye level, looking along the dike toward a village with a church on a slope. Below, on the river side, high water; undead dig into the dike with their bare bones and pull out the earth. Farmers on the land side stare up at them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 054 · `story/ort_hoya.jpg` · 21:9
Verwendung: Erster Angriff auf Hoya (Dorf, 16×16)

```
evening, viewpoint: on the Weser bank at eye level, looking toward a castle. The ferry lies abandoned; undead cross the river on its rope, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 055 · `story/ort_teufelsmoor.jpg` · 21:9
Verwendung: Erster Angriff auf Teufelsmoor (mythischer Ort, 16×16)

```
night, viewpoint: standing on a narrow plank path across a dark moor, looking ahead. Black pools of water and peat banks, a few crooked birches. Will-o'-the-wisps hover over the water as small glowing orbs and lead toward deeper water. In a pool to the left a bog body with leathery skin rises, a rope around its neck. Low mist, the moon behind clouds, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 056 · `story/ort_wittingen.jpg` · 21:9
Verwendung: Erster Angriff auf Wittingen (Dorf, 16×16)

```
grey day, viewpoint: in front of a small walled town, at eye level, looking at a fieldstone gate tower in a low wall. Burghers on the wall look outward at a crowd of undead on the road in the foreground; one burgher crosses himself, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 057 · `story/ort_moelln.jpg` · 21:9
Verwendung: Erster Angriff auf Mölln (Dorf, 16×16)

```
night, viewpoint: in a small churchyard at eye level, looking at a gravestone with a carved owl and mirror. The grave has opened; a skeletal jester in a ragged fool's cap with bells sits on the edge and grins at the crowned lich standing before him, seen from behind. A brick church tower behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 058 · `story/ort_burgdorf.jpg` · 21:9
Verwendung: Erster Angriff auf Burgdorf (Dorf, 16×16)

```
dusk, viewpoint: on a road at eye level, looking toward a small town gate and a modest castle tower behind. A messenger on a horse lies fallen on the road, his horse fleeing. Undead step from the roadside ditches onto the road in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 059 · `story/ort_syke.jpg` · 21:9
Verwendung: Erster Angriff auf Syke (Dorf, 16×16)

```
morning, viewpoint: in an oak forest near a small castle, at eye level. A herd of red deer bursts through the trees past the viewer in panic. Behind the deer, at the far end of the forest aisle, undead advance; through a gap in the trees a small castle tower is visible, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 060 · `story/ort_hitzacker.jpg` · 21:9
Verwendung: Erster Angriff auf Hitzacker (Dorf, 16×16)

```
autumn, viewpoint: on a vineyard slope above a small town on an island where two rivers meet, looking down over the rows of vines. Harvesters with baskets flee down the slope. In the foreground undead pick grapes with bony fingers and crush them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 061 · `story/ort_nienburg.jpg` · 21:9
Verwendung: Erster Angriff auf Nienburg (Dorf, 16×16)

```
grey day, viewpoint: on the Weser bank opposite a town with a castle, at eye level. A river boat lies at the landing; soldiers of the count stand on the bank in formation. Undead climb out of the river behind the soldiers' backs, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 062 · `story/ort_bremen.jpg` · 21:9
Verwendung: Erster Angriff auf Bremen (Stadt, 32×32)

```
foggy morning, viewpoint: on the Weser river bank at a wooden landing stage, looking toward a Hanseatic town: a large cathedral with two towers, gabled houses, and in the market place a tall wooden statue of a knight with a sword and shield. Cogs at anchor. Undead wade out of the river onto the landing stage in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 063 · `story/ort_oldesloe.jpg` · 21:9
Verwendung: Erster Angriff auf Oldesloe (Dorf, 16×16)

```
viewpoint: inside a small salt-boiling house at eye level. Steam rises from large flat iron pans over fires; salt boilers with rakes turn toward the open door, where undead stand against the daylight, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 064 · `story/ort_dannenberg.jpg` · 21:9
Verwendung: Erster Angriff auf Dannenberg (Dorf, 16×16)

```
evening, viewpoint: on the low marshy bank of a slow river, at eye level, looking toward a round stone castle tower rising over a small town. Cattle on the pasture run away. Undead come through the reeds along the river toward the tower, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 065 · `story/ort_ratzeburg.jpg` · 21:9
Verwendung: Erster Angriff auf Ratzeburg (Kloster/Kirche, 16×16)

```
dusk, viewpoint: at the land end of a long causeway across a lake, at eye level, looking along it toward an island with a large Romanesque brick cathedral. On the causeway undead march toward the island; others wade through the lake on both sides, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 066 · `story/ort_neustadt.jpg` · 21:9
Verwendung: Erster Angriff auf Neustadt am Rübenberge (Dorf, 16×16)

```
dusk, viewpoint: on a meadow by the Leine river, at eye level, looking at a small castle beside a town. Its garrison rides out over the bridge with lances. In the foreground undead stand in a line between the willows and wait, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 067 · `story/ort_hannover.jpg` · 21:9
Verwendung: Erster Angriff auf Hannover (Stadt, 32×32)

```
evening, viewpoint: outside the town wall on the Leine river meadows, at eye level, looking at a brick town wall with a gate and, behind it, an unfinished brick church tower surrounded by wooden scaffolding. Workers flee from the scaffolding. In the foreground, on the meadows, undead advance in a loose line, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 068 · `story/ort_salzwedel.jpg` · 21:9
Verwendung: Erster Angriff auf Salzwedel (Dorf, 16×16)

```
evening, viewpoint: inside a brick town hall at the end of a council table, looking down its length. Merchants in fur-trimmed robes sit along the table and turn toward the door at the far end, where the crowned lich enters with undead behind him, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 069 · `story/ort_hagenow.jpg` · 21:9
Verwendung: Erster Angriff auf Hagenow (Dorf, 16×16)

```
evening, viewpoint: on a sandy road through a pine heath, looking toward a modest town with a church tower. Villagers stand together at the town gate with flails; undead walk toward them across the heath, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 070 · `story/ort_segeberg.jpg` · 21:9
Verwendung: Erster Angriff auf Segeberg (Stadt, 16×16)

```
viewpoint: inside a white limestone cave below a hill, standing deep in a passage and looking toward the cave mouth, which shows daylight. Undead with torches walk through the passage toward the exit; beyond the cave mouth, high above, a castle wall is just visible on the hilltop, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 071 · `story/ort_gifhorn.jpg` · 21:9
Verwendung: Erster Angriff auf Gifhorn (Dorf, 16×16)

```
grey day, viewpoint: on the salt road at eye level, looking toward a small castle at the meeting of two rivers. Undead lead a captured salt caravan away from the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 072 · `story/ort_delmenhorst.jpg` · 21:9
Verwendung: Erster Angriff auf Delmenhorst (Dorf, 16×16)

```
night, viewpoint: on a narrow wooden bridge over a swamp, looking toward a small castle. A single guard with a lantern stands at the far end; undead come across the bridge toward him, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 073 · `story/ort_itzehoe.jpg` · 21:9
Verwendung: Erster Angriff auf Itzehoe (Dorf, 16×16)

```
dusk, viewpoint: in green marshland with drainage ditches, at eye level, looking toward a small town on a river with a convent church. A cattle herd stands alone in a field without its herdsman; undead walk among the cattle, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 074 · `story/ort_neumuenster.jpg` · 21:9
Verwendung: Erster Angriff auf Neumünster (Dorf, 16×16)

```
night, viewpoint: in an overgrown monastery cemetery at eye level, looking toward a small church. Weathered grave slabs have been pushed aside; skeletal monks in rotten habits rise and walk toward the church door, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 075 · `story/ort_gadebusch.jpg` · 21:9
Verwendung: Erster Angriff auf Gadebusch (Dorf, 16×16)

```
dusk, viewpoint: on a road at eye level, looking toward a small town with a squat brick church. Farmers with carts full of grain stand frozen on the road; undead lead their horses away, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 076 · `story/ort_peine.jpg` · 21:9
Verwendung: Erster Angriff auf Peine (Dorf, 16×16)

```
grey day, viewpoint: in front of a small fortified castle with an earthen rampart, at eye level. Soldiers with crossbows shoot from the rampart; the bolts stick in the skeletons in the foreground, which keep walking, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 077 · `story/ort_luebeck.jpg` · 21:9
Verwendung: Erster Angriff auf Lübeck (Stadt, 64×64)

```
dawn, viewpoint: on the bank of the Trave river opposite the town, at eye level, looking across the water at a Hanseatic town on its island hill: a skyline of tall green-roofed brick church spires, high gabled warehouses along the quay, cogs at anchor. In the foreground undead stand in the shallow water among the reeds, seen from behind, facing the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 078 · `story/ort_kloetze.jpg` · 21:9
Verwendung: Erster Angriff auf Klötze (Dorf, 16×16)

```
dusk, viewpoint: in a forest clearing at eye level, looking at a small castle. Guards play dice at the gate; undead step out of the forest behind them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 079 · `story/ort_otterndorf.jpg` · 21:9
Verwendung: Erster Angriff auf Otterndorf (Dorf, 16×16)

```
storm, viewpoint: on a dike at eye level, looking along it. Waves crash over the dike; undead break the dike from the sea side; farmers on the land side run with spades, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 080 · `story/ort_schwerin.jpg` · 21:9
Verwendung: Erster Angriff auf Schwerin (Stadt, 64×64)

```
dusk, viewpoint: on the shore of a large lake, at eye level, looking across the water to a castle on an island and a town with a cathedral on the opposite shore. On the lake a boat with a ducal banner; undead stand on the shore in the foreground and watch it, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 081 · `story/ort_fallersleben.jpg` · 21:9
Verwendung: Erster Angriff auf Fallersleben (Dorf, 16×16)

```
evening, viewpoint: in a village street at eye level. Villagers peer out of their doors; the crowned lich walks down the middle of the street toward the viewer with his undead behind him, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 082 · `story/ort_pestrup.jpg` · 21:9
Verwendung: Erster Angriff auf Pestruper Gräberfeld (mythischer Ort, 16×16)

```
dusk, viewpoint: on the top of a low burial mound at eye level, looking out over a heath covered with hundreds of round grave mounds to the horizon. Pale lights hover over the mounds; heath spirits in the shape of mist figures stand between them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 083 · `story/ort_hildesheim.jpg` · 21:9
Verwendung: Erster Angriff auf Hildesheim (Kloster/Kirche, 32×32)

```
dusk, viewpoint: in a small cathedral cloister courtyard at eye level, looking at an old rose bush climbing up the apse wall of a Romanesque cathedral. The crowned lich stands beside it with his bony hand on the trunk; where he touches it, the roses wither, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 084 · `story/ort_wildeshausen.jpg` · 21:9
Verwendung: Erster Angriff auf Wildeshausen (Dorf, 16×16)

```
dusk, viewpoint: in a heath with megalithic stone graves, at eye level, looking toward a town with a large church. Undead rise from between the boulders of the stone graves and walk toward the church, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 085 · `story/ort_arendsee.jpg` · 21:9
Verwendung: Erster Angriff auf Arendsee (mythischer Ort, 16×16)

```
dusk, viewpoint: on the shore of a round lake at water level, looking out over the water. Bubbles rise in the middle of the lake; drowned knights in rusty armour rise slowly from the water, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 086 · `story/ort_stadthagen.jpg` · 21:9
Verwendung: Erster Angriff auf Stadthagen (Dorf, 16×16)

```
dusk, viewpoint: at the edge of a forest at eye level, looking toward a small walled town. A hunting party flees out of the forest past the viewer toward the town; undead follow among the trees, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 087 · `story/ort_braunschweig.jpg` · 21:9
Verwendung: Erster Angriff auf Braunschweig (Stadt, 64×64)

```
night, viewpoint: on a cobbled castle square at eye level, standing behind a crowd of undead who face a large bronze lion statue on a tall stone pedestal. Behind the lion the Romanesque cathedral and the hall of a castle palace. Townsmen with torches and halberds form a line at the far side of the square, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 088 · `story/ort_diepholz.jpg` · 21:9
Verwendung: Erster Angriff auf Diepholz (Dorf, 16×16)

```
morning mist, viewpoint: on a wooden plank road across a bog, at eye level, looking toward a castle. Undead walk beside the plank road through the bog without sinking, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 089 · `story/ort_gardelegen.jpg` · 21:9
Verwendung: Erster Angriff auf Gardelegen (Dorf, 16×16)

```
night, viewpoint: in a brewery yard at eye level, looking through an open gate into the street. Copper brew kettles steam; brewers with ladles run away. Undead walk in through the gate toward the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 090 · `story/ort_vechta.jpg` · 21:9
Verwendung: Erster Angriff auf Vechta (Dorf, 16×16)

```
dusk, viewpoint: on a moor road at eye level, looking toward a small castle. Peat fires smoke along the road; undead walk through the smoke toward the castle, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 091 · `story/ort_ploen.jpg` · 21:9
Verwendung: Erster Angriff auf Plön (Dorf, 16×16)

```
early morning, viewpoint: on a lake shore at water level, looking across a calm lake toward a small castle on a peninsula. Mist lies on the water; a fisherman in a rowing boat pulls in a net from which pale hands reach up, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 092 · `story/ort_oldenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Oldenburg (Stadt, 64×64)

```
grey day, viewpoint: on a moor at eye level, looking toward a moated castle and town on a river. The counts' banner flies; defenders stand on the walls. Undead walk out of the moor in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 093 · `story/ort_alfeld.jpg` · 21:9
Verwendung: Erster Angriff auf Alfeld (Dorf, 16×16)

```
dusk, viewpoint: at the edge of a forest on a hillside, at eye level, looking down into a valley with a small town and church on the river. Undead emerge from the forest next to the viewer and walk down toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 094 · `story/ort_duemmer.jpg` · 21:9
Verwendung: Erster Angriff auf Dümmer-Moor (mythischer Ort, 16×16)

```
dusk, viewpoint: on the shore of a shallow lake at the edge of a bog, at eye level. The crowned lich stands at the edge of the bog with his hand raised; out of the black peat, leathery bog bodies rise with ropes around their necks, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 095 · `story/ort_wolfenbuettel.jpg` · 21:9
Verwendung: Erster Angriff auf Wolfenbüttel (Dorf, 16×16)

```
foggy morning, viewpoint: at the edge of a marsh at water level, looking toward a moated castle with towers rising from the fog. Undead walk through the swamp water toward the castle, up to their chests in the water; a sentry on the tower raises a horn, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 096 · `story/ort_kiel.jpg` · 21:9
Verwendung: Erster Angriff auf Kiel (Stadt, 16×16)

```
foggy morning, viewpoint: on a wooden pier on a long narrow inlet of the Baltic Sea, looking toward a small town with a castle and a church. Fog drifts over the water; from the fog a rowing boat with undead oarsmen glides toward the pier. A dockhand on the pier drops his rope, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 097 · `story/ort_koenigslutter.jpg` · 21:9
Verwendung: Erster Angriff auf Königslutter (Kloster/Kirche, 16×16)

```
night, viewpoint: inside a Romanesque imperial cathedral at eye level, looking toward the imperial tomb in the nave. The lid of the emperor's tomb lies broken; the skeletal emperor in a crown sits up. Above, a stone frieze shows hunters and hares, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 098 · `story/ort_minden.jpg` · 21:9
Verwendung: Erster Angriff auf Minden (Kloster/Kirche, 32×32)

```
dusk, viewpoint: on the riverbank at eye level, looking at a stone bridge over the Weser leading to a town with a cathedral; two forested mountains rise behind. Undead march across the bridge; defenders on the far side lower a chain, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 099 · `story/ort_rendsburg.jpg` · 21:9
Verwendung: Erster Angriff auf Rendsburg (Dorf, 16×16)

```
grey day, viewpoint: on the bank of a river opposite a castle on a river island, at eye level. A drawbridge leads to the island; guards hold their spears crossed in front of it. Undead walk straight across the river bottom toward the island, only their skulls above the water, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 100 · `story/ort_hameln.jpg` · 21:9
Verwendung: Erster Angriff auf Hameln (mythischer Ort, 16×16)

```
dusk, viewpoint: at the foot of a hill outside a medieval town on the Weser, at eye level, looking up the slope. A piper in a pied, parti-coloured costume with a long flute walks up the hill toward a dark opening in the hillside; behind him a long line of rats, and behind the rats small shadowy figures of children. In the background the town walls and a church tower by the river, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 101 · `story/ort_wismar.jpg` · 21:9
Verwendung: Erster Angriff auf Wismar (Stadt, 32×32)

```
storm at dusk, viewpoint: on a wooden harbour pier, looking toward a Hanseatic town with tall brick churches. Out of the storm a ghost cog with torn sails approaches the harbour, its deck crowded with undead; harbour men on the pier draw their knives, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 102 · `story/ort_rinteln.jpg` · 21:9
Verwendung: Erster Angriff auf Rinteln (Dorf, 16×16)

```
grey morning, viewpoint: on the river at water level, looking toward a small town with ramparts. Undead float down the river on rafts made of coffins toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 103 · `story/ort_osterburg.jpg` · 21:9
Verwendung: Erster Angriff auf Osterburg (Dorf, 16×16)

```
evening, viewpoint: on a riverbank at eye level, looking at a watermill near a small town. A farmer's cart stands abandoned at the mill; undead stand in the mill doorway, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 104 · `story/ort_helmstedt.jpg` · 21:9
Verwendung: Erster Angriff auf Helmstedt (Kloster/Kirche, 16×16)

```
dusk, viewpoint: in front of a Romanesque monastery church at eye level. Monks carry a saint's reliquary out of the church in procession; undead block the procession's way in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 105 · `story/ort_parchim.jpg` · 21:9
Verwendung: Erster Angriff auf Parchim (Dorf, 16×16)

```
grey morning, viewpoint: on a bridge over a river, looking toward a town with two church towers. Townsmen from both ends of the town run together onto the bridge with pitchforks and spears; undead approach from the viewer's side, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 106 · `story/ort_cloppenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Cloppenburg (Dorf, 16×16)

```
grey day, viewpoint: in front of a small castle with an earthen rampart, at eye level. A rider gallops away from the castle to fetch help; undead block his way in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 107 · `story/ort_gandersheim.jpg` · 21:9
Verwendung: Erster Angriff auf Stift Gandersheim (Kloster/Kirche, 16×16)

```
dusk, viewpoint: in front of a Romanesque convent church at eye level. Canonesses in robes stand in the doorway and look at the undead in the foreground; one holds a book to her chest, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 108 · `story/ort_perleberg.jpg` · 21:9
Verwendung: Erster Angriff auf Perleberg (Dorf, 16×16)

```
grey day, viewpoint: on a market square at eye level, looking at a stone statue of a knight with a sword in front of a town hall. Undead stand in front of the statue; the townsfolk have fled into the houses and peer from the windows, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 109 · `story/ort_einbeck.jpg` · 21:9
Verwendung: Erster Angriff auf Einbeck (Stadt, 16×16)

```
viewpoint: in a vaulted brewery cellar at eye level, looking along rows of barrels. Undead smash barrels; beer runs over the floor; a brewer with a candle stands frozen at the stairs, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 110 · `story/ort_stendal.jpg` · 21:9
Verwendung: Erster Angriff auf Stendal (Stadt, 16×16)

```
dusk, viewpoint: on a road at eye level, looking at a tall ornate brick town gate. Merchants close the gate; undead press against it from outside in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 111 · `story/ort_seesen.jpg` · 21:9
Verwendung: Erster Angriff auf Seesen (Dorf, 16×16)

```
evening, viewpoint: on a road at eye level, looking toward a small town with a castle. Merchants with packhorses hurry toward the town gate, looking back; undead follow them on the road in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 112 · `story/ort_haldensleben.jpg` · 21:9
Verwendung: Erster Angriff auf Haldensleben (Dorf, 16×16)

```
dusk, viewpoint: in front of a town wall with a brick gate tower, at eye level. Burghers with spears and shields stand bravely in front of the gate; facing them, in the foreground, a dense mass of undead seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 113 · `story/ort_jever.jpg` · 21:9
Verwendung: Erster Angriff auf Jever (Dorf, 16×16)

```
grey day, viewpoint: on a dike at eye level, looking inland toward a small castle in the marsh. Frisian peasants with spears stand on the dike; undead come from the seaward side across the mudflats behind the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 114 · `story/ort_goslar.jpg` · 21:9
Verwendung: Erster Angriff auf Goslar (Stadt, 32×32)

```
dusk, viewpoint: on the slope of a mining mountain at eye level, looking down onto a town with many church towers and a long Romanesque imperial palace. Mine entrances and spoil heaps on the slope; undead come out of a mine adit right in front of the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 115 · `story/ort_tangermuende.jpg` · 21:9
Verwendung: Erster Angriff auf Tangermünde (Dorf, 16×16)

```
dusk, viewpoint: on the low opposite bank of a wide river, looking across to a high bank with a large brick castle and a town. Undead wade out into the river toward the castle; a boatman pushes off in panic, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 116 · `story/ort_hackelberg.jpg` · 21:9
Verwendung: Erster Angriff auf Hackelbergs Grab (mythischer Ort, 32×32)

```
stormy night, viewpoint: in a forest clearing at eye level, looking toward an old grave slab under an oak. Above the treetops the Wild Hunt rushes through the clouds: a rider with a hunting horn, hounds and horses drawn in fine light lines. Undead approach the grave in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 117 · `story/ort_schleswig.jpg` · 21:9
Verwendung: Erster Angriff auf Schleswig (Kloster/Kirche, 32×32)

```
dusk, viewpoint: on the top of an old grass-covered semicircular earth rampart beside a long inlet, looking across the water toward a town with a large brick cathedral. Out of the rampart below the viewer, Viking skeletons with round shields and axes climb, turning toward the cathedral, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 118 · `story/ort_northeim.jpg` · 21:9
Verwendung: Erster Angriff auf Northeim (Dorf, 16×16)

```
night, viewpoint: in a monastery crypt at eye level, looking at stone tombs of counts. The tomb lids slide aside; skeletal counts in rotting robes sit up, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 119 · `story/ort_herford.jpg` · 21:9
Verwendung: Erster Angriff auf Herford (Kloster/Kirche, 16×16)

```
evening, viewpoint: in the courtyard of a convent at eye level, looking toward a Romanesque church. Canonesses in fine robes flee across the courtyard; undead enter through the gate, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 120 · `story/ort_lemgo.jpg` · 21:9
Verwendung: Erster Angriff auf Lemgo (Dorf, 16×16)

```
night, viewpoint: in a weaver's workshop at eye level, looking at looms and spinning wheels. A spinning wheel turns by itself; through the window undead pass in the street, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 121 · `story/ort_havelberg.jpg` · 21:9
Verwendung: Erster Angriff auf Havelberg (Kloster/Kirche, 16×16)

```
dusk, viewpoint: on the river below a hill, at eye level, looking up at a large cathedral on the hilltop. Its bells swing wildly in the tower; undead climb the slope toward the cathedral, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 122 · `story/ort_harzburg.jpg` · 21:9
Verwendung: Erster Angriff auf Harzburg (Dorf, 16×16)

```
dusk, viewpoint: on a forested mountain top among ruined castle walls, at eye level. Scattered bones lie among the stones of a broken burial vault; undead servants gather them carefully into baskets. A small village at the foot of the mountain far below, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 123 · `story/ort_iberg.jpg` · 21:9
Verwendung: Erster Angriff auf Zwergenlöcher am Iberg (mythischer Ort, 16×16)

```
viewpoint: at the mouth of a limestone cave in a forested mountain slope, looking into the cave. Deep inside, small lights and the silhouettes of dwarfs with hammers; undead with torches step into the cave from behind the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 124 · `story/ort_guestrow.jpg` · 21:9
Verwendung: Erster Angriff auf Güstrow (Stadt, 16×16)

```
night, viewpoint: inside the nave of a brick cathedral at eye level, looking toward the choir. The lid of a stone tomb with the effigy of a prince has shifted; a skeletal hand with a signet ring pushes it aside. Candles flicker, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 125 · `story/ort_osnabrueck.jpg` · 21:9
Verwendung: Erster Angriff auf Osnabrück (Kloster/Kirche, 32×32)

```
night, viewpoint: in a cathedral crypt at eye level, looking at a saint's shrine on an altar. Around the shrine, old graves open; skeletons rise and kneel mockingly before the shrine, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 126 · `story/ort_burg.jpg` · 21:9
Verwendung: Erster Angriff auf Burg (Dorf, 16×16)

```
windy day, viewpoint: in a field outside a town where long lengths of cloth hang on wooden drying frames, at eye level, looking along a row of frames. Between the billowing cloths undead walk toward the viewer; a cloth maker runs away, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 127 · `story/ort_osterode.jpg` · 21:9
Verwendung: Erster Angriff auf Osterode (Dorf, 16×16)

```
winter, viewpoint: on a snowy riverbank at eye level, looking toward a small town with a church. The mill wheel is frozen; undead walk across the frozen river toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 128 · `story/ort_corvey.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Corvey (Kloster/Kirche, 16×16)

```
evening, viewpoint: on the bank of the Weser at eye level, looking at a Carolingian abbey church with a massive westwork of two towers. Monks carry books out of the church into a boat; undead approach along the riverbank, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 129 · `story/ort_ilsenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Ilsenburg (Dorf, 16×16)

```
morning, viewpoint: in a monastery garden at eye level, looking past a Romanesque church toward a high bare mountain on the horizon. Monks stand in the garden and look toward the mountain; on the path along the river in the foreground undead approach the monastery wall, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 130 · `story/ort_genthin.jpg` · 21:9
Verwendung: Erster Angriff auf Genthin (Dorf, 16×16)

```
morning, viewpoint: in a flat-bottomed boat in a reed marsh, looking ahead. A reed cutter with a sickle stands in a boat in front; the reeds part, and pale faces of undead rise from the water between the stalks, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 131 · `story/ort_oschersleben.jpg` · 21:9
Verwendung: Erster Angriff auf Oschersleben (Dorf, 16×16)

```
grey day, viewpoint: standing at the near end of a narrow earth causeway through a swamp, looking along it toward a small castle and town. Undead march single file along the causeway; reeds and black water on both sides, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 132 · `story/ort_husum.jpg` · 21:9
Verwendung: Erster Angriff auf Husum (Dorf, 16×16)

```
low tide at dusk, viewpoint: on a dike above a small harbour village, at eye level, looking out over the mudflats. Out on the flats a procession of drowned dead in rags walks toward the dike; a few fishermen's boats lie on the mud. Gulls, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 133 · `story/ort_doberan.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Doberan (Kloster/Kirche, 16×16)

```
dusk, viewpoint: in a monastery herb garden at eye level, looking toward a tall brick abbey church. Monks in white habits hurry from the garden; through the open church door, tombs inside are visible, and undead walk among the herb beds in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 134 · `story/ort_wernigerode.jpg` · 21:9
Verwendung: Erster Angriff auf Wernigerode (Dorf, 16×16)

```
evening, viewpoint: in a narrow street of half-timbered houses at eye level, looking up the street toward a castle on a forested hill. Undead walk down the street toward the viewer; residents close their shutters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 135 · `story/ort_bielefeld.jpg` · 21:9
Verwendung: Erster Angriff auf Bielefeld (Dorf, 16×16)

```
morning, viewpoint: in a meadow where long strips of white linen are laid out to bleach, at eye level, looking up at a castle on a forested ridge. Undead walk across the linen and leave grey footprints, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 136 · `story/ort_goettingen.jpg` · 21:9
Verwendung: Erster Angriff auf Göttingen (Stadt, 32×32)

```
grey day, viewpoint: on a field outside a town wall at eye level, looking at a gate with a tower. Burghers on the wall shoot crossbows; undead with ladders approach the wall in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 137 · `story/ort_externsteine.jpg` · 21:9
Verwendung: Erster Angriff auf Externsteine (mythischer Ort, 32×32)

```
night, viewpoint: on the forest floor at the foot of tall weathered sandstone rock pillars, at eye level, looking up. A large relief of the Descent from the Cross is carved into one rock; glowing lines of light run up the rock like veins. Druids and Saxon spirits stand around the pillars; undead approach through the trees, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 138 · `story/ort_halberstadt.jpg` · 21:9
Verwendung: Erster Angriff auf Halberstadt (Kloster/Kirche, 32×32)

```
night, viewpoint: on the cathedral square at eye level, looking at the Gothic cathedral under construction. The cathedral windows glow with a holy light; undead stand at the square's edge and shield their eyes, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 139 · `story/ort_schierke.jpg` · 21:9
Verwendung: Erster Angriff auf Schierke (Dorf, 16×16)

```
night, viewpoint: at the end of a steep village lane at the forest edge, at eye level. Wooden houses with herbs and horseshoes over the doors, shutters closed. A witch with a besom stands in the lane and looks at undead coming out of the spruce forest in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 140 · `story/ort_aurich.jpg` · 21:9
Verwendung: Erster Angriff auf Aurich (Dorf, 16×16)

```
grey day, viewpoint: on a heath plain at eye level, looking toward a fortified brick tower house of a Frisian chieftain. The chieftain stands in the doorway with a sword; undead approach across the heath, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 141 · `story/ort_rathenow.jpg` · 21:9
Verwendung: Erster Angriff auf Rathenow (Dorf, 16×16)

```
morning, viewpoint: in a fishing boat on a river at water level, looking at two fishermen pulling up a fish trap. In the net hangs a skeletal arm that grasps the edge of the boat. A small town with a church on the far bank, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 142 · `story/ort_rostock.jpg` · 21:9
Verwendung: Erster Angriff auf Rostock (Stadt, 32×32)

```
evening, viewpoint: on a river bank among smoking huts where fish are smoked, at eye level, looking toward a town with tall church towers. Thick smoke drifts across the scene; out of the smoke step undead, while the fishwives flee, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 143 · `story/ort_teufelsmauer.jpg` · 21:9
Verwendung: Erster Angriff auf Teufelsmauer (mythischer Ort, 16×16)

```
dusk, viewpoint: in a field at eye level, looking at a long jagged ridge of sandstone rocks that runs across the landscape like a broken wall. On top of the rocks horned shadows sit; undead walk along the foot of the wall toward the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 144 · `story/ort_wittstock.jpg` · 21:9
Verwendung: Erster Angriff auf Wittstock (Dorf, 16×16)

```
night, viewpoint: in front of a castle with a tall round keep, at eye level. A bishop on horseback with a small escort gallops in through the gate; behind him, in the foreground, undead follow at a run, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 145 · `story/ort_quedlinburg.jpg` · 21:9
Verwendung: Erster Angriff auf Quedlinburg (Kloster/Kirche, 16×16)

```
dusk, viewpoint: in the lane at the foot of a sandstone castle hill, at eye level, looking up at a Romanesque abbey church on the rock. An abbess with a crozier stands at the top of the stairs; undead climb the stairs toward her, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 146 · `story/ort_hexentanzplatz.jpg` · 21:9
Verwendung: Erster Angriff auf Hexentanzplatz (mythischer Ort, 32×32)

```
night, viewpoint: on the edge of a rocky plateau high above a deep gorge, at eye level. Witches dance around a fire; one stops and points at the crowned lich, who steps onto the plateau from the forest. Across the gorge another rock with a hoofprint visible in moonlight, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 147 · `story/ort_muenden.jpg` · 21:9
Verwendung: Erster Angriff auf Münden (Dorf, 16×16)

```
morning, viewpoint: on a riverbank at the point where two rivers meet, at eye level, looking toward a town of half-timbered houses and a church. Cargo boats lie at the landing; undead pull them ashore and unload barrels, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 148 · `story/ort_brandenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Brandenburg (Stadt, 32×32)

```
dusk, viewpoint: on a riverbank among willows, at eye level, looking across the water at an island with a cathedral and a town behind it. Undead wade into the river toward the island; a ferry boat turns back, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 149 · `story/ort_paderborn.jpg` · 21:9
Verwendung: Erster Angriff auf Paderborn (Kloster/Kirche, 32×32)

```
morning, viewpoint: at a spring pool under a large cathedral, at eye level. Clear water bubbles up from the ground; undead wade through the spring and the water turns cloudy around them. Townsfolk at the well step back, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 150 · `story/ort_waren.jpg` · 21:9
Verwendung: Erster Angriff auf Waren (Dorf, 16×16)

```
dusk, viewpoint: on a lake shore at water level, looking across a vast lake with no visible far shore. Fishing boats drift empty on the water; one of them comes back to shore with undead at the oars, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 151 · `story/ort_emden.jpg` · 21:9
Verwendung: Erster Angriff auf Emden (Stadt, 16×16)

```
stormy dusk, viewpoint: on a harbour quay at eye level, looking out to sea. Ships of pirates and merchants lie in the harbour; a ghost ship with tattered sails approaches the harbour mouth, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 152 · `story/ort_belzig.jpg` · 21:9
Verwendung: Erster Angriff auf Belzig (Dorf, 16×16)

```
dusk, viewpoint: on a castle tower behind a sentry, looking out over a wide flat landscape of heath and forest. Far away a long column of undead crosses the plain toward the castle; the sentry raises a horn to his mouth, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 153 · `story/ort_zerbst.jpg` · 21:9
Verwendung: Erster Angriff auf Zerbst (Dorf, 16×16)

```
night, viewpoint: on a market square during a feast, at eye level. Townsfolk dance around a stone Roland statue with torches and music; at the edge of the square undead in tattered clothes join the dance, and the nearest dancers notice and scream, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 154 · `story/ort_nordhausen.jpg` · 21:9
Verwendung: Erster Angriff auf Nordhausen (Stadt, 16×16)

```
dusk, viewpoint: in front of a town hall with a Roland statue, at eye level. Councillors in robes stand defiantly on the steps; the crowned lich stands before them in the foreground, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 155 · `story/ort_kassel.jpg` · 21:9
Verwendung: Erster Angriff auf Kassel (Stadt, 32×32)

```
grey day, viewpoint: on a hill above a river valley, at eye level, looking down at a castle and town. Knights in armour with the lion banner ride out of the castle in a column; on the hillside below the viewer undead form ranks, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 156 · `story/ort_bernburg.jpg` · 21:9
Verwendung: Erster Angriff auf Bernburg (Dorf, 16×16)

```
evening, viewpoint: on the Saale river bank below a steep sandstone cliff, at eye level, looking up at a castle with a round tower on top. Undead climb the cliff path toward the castle; a boat on the river turns away, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 157 · `story/ort_lehnin.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Lehnin (Kloster/Kirche, 16×16)

```
evening, viewpoint: in a cloister walk of a brick monastery at eye level, looking along the arcade. Monks carry a lead box toward a hiding place in the wall; at the far end of the walk the crowned lich appears in the arcade, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 158 · `story/ort_neuruppin.jpg` · 21:9
Verwendung: Erster Angriff auf Neuruppin (Dorf, 16×16)

```
evening, viewpoint: inside a monastery church at the back of the nave, looking toward a pulpit where a Dominican friar preaches to a congregation. The friar has stopped and points to the open door at the back, where the crowned lich enters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 159 · `story/ort_muenster.jpg` · 21:9
Verwendung: Erster Angriff auf Münster (Kloster/Kirche, 32×32)

```
dusk, viewpoint: on a cathedral square at eye level, looking at a large Gothic cathedral with two towers. Mounted knights with crosses on their shields gather in front; undead fill the square in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 160 · `story/ort_nauen.jpg` · 21:9
Verwendung: Erster Angriff auf Nauen (Dorf, 16×16)

```
grey day, viewpoint: on a field dike in a vast flat moorland, at eye level. Farmers in a field look toward the horizon, where a long line of undead approaches across the moor. A small town with a church tower in the background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 161 · `story/ort_treuenbrietzen.jpg` · 21:9
Verwendung: Erster Angriff auf Treuenbrietzen (Dorf, 16×16)

```
dusk, viewpoint: on a market square at eye level, looking at townsfolk gathered in front of a church. A town elder in front holds out the key to the town gate toward the crowned lich, who stands in the foreground, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 162 · `story/ort_mansfeld.jpg` · 21:9
Verwendung: Erster Angriff auf Mansfeld (Stadt, 16×16)

```
dusk, viewpoint: on a slag heap at eye level, looking toward a castle on a hill and a mining town with smoking smelting huts. Undead dig bones out of the slag heap in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 163 · `story/ort_demmin.jpg` · 21:9
Verwendung: Erster Angriff auf Demmin (Dorf, 16×16)

```
dusk, viewpoint: on a hill above a town surrounded by three rivers, looking down at it. Below, the rivers glint; undead gather on the only land approach in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 164 · `story/ort_koethen.jpg` · 21:9
Verwendung: Erster Angriff auf Köthen (Dorf, 16×16)

```
summer evening, viewpoint: in a wheat field at eye level, looking toward a small castle and town on the flat plain. Reapers with scythes stand still in the field; on the far side of the field undead walk through the wheat toward them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 165 · `story/ort_dessau.jpg` · 21:9
Verwendung: Erster Angriff auf Dessau (Dorf, 16×16)

```
dusk, viewpoint: in a floodplain forest of huge old oaks at eye level, looking along a path toward a small town. Undead walk between the oak trunks; a stag flees across the path, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 166 · `story/ort_muehlhausen.jpg` · 21:9
Verwendung: Erster Angriff auf Mühlhausen (Stadt, 16×16)

```
dusk, viewpoint: between two town walls with a moat in front, at eye level, looking up at a gate tower. Burghers defend the inner wall; undead have already climbed the outer wall and drop down into the space between, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 167 · `story/ort_sangerhausen.jpg` · 21:9
Verwendung: Erster Angriff auf Sangerhausen (Dorf, 16×16)

```
evening, viewpoint: on a field in a fertile valley at eye level, looking toward a small town with a church. Behind the town on the horizon a forested mountain with a castle ruin on top. Undead walk across the field toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 168 · `story/ort_barth.jpg` · 21:9
Verwendung: Erster Angriff auf Barth (Dorf, 16×16)

```
early morning, viewpoint: at water level in a reed lagoon, looking toward a small town with a tall brick church tower. Flat boats with undead glide through the reeds toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 169 · `story/ort_eisleben.jpg` · 21:9
Verwendung: Erster Angriff auf Eisleben (Dorf, 16×16)

```
viewpoint: in a low mining tunnel, standing behind a miner with a lamp, looking deeper into the tunnel. The miner raises his lamp; at the end of the tunnel pale undead faces appear in the darkness, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 170 · `story/ort_potsdam.jpg` · 21:9
Verwendung: Erster Angriff auf Potsdam (Dorf, 16×16)

```
morning, viewpoint: on a lake shore among reeds, at eye level, looking toward a small fishing village with a modest castle. Fishermen mend nets on the shore; undead step out of the water behind them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 171 · `story/ort_wittenberg.jpg` · 21:9
Verwendung: Erster Angriff auf Wittenberg (Stadt, 16×16)

```
viewpoint: on the sandy bank of a wide river at eye level, looking across the water to a small town with a castle and a brick church tower on the far bank. A ferry is halfway across; the ferryman stares at the near bank, where undead step out of the willows into the shallow water, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 172 · `story/ort_jueterbog.jpg` · 21:9
Verwendung: Erster Angriff auf Jüterbog (Dorf, 16×16)

```
grey morning, viewpoint: on a road at eye level, looking at a tall brick town gate tower. Burghers drop stones from the top of the gate onto undead below; more undead stand on the road in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 173 · `story/ort_stralsund.jpg` · 21:9
Verwendung: Erster Angriff auf Stralsund (Stadt, 32×32)

```
dusk, viewpoint: on a boat on the sea strait opposite the town, at water level, looking toward a Hanseatic town surrounded by ponds, with tall brick churches and town gates. A parchment treaty with seals drifts in the water in the foreground; undead in boats row toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 174 · `story/ort_neubrandenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Neubrandenburg (Stadt, 16×16)

```
grey day, viewpoint: on a field outside a round town wall with a tall, ornate brick gate with pointed gables, at eye level. Small half-timbered watch houses sit on the wall; guards with crossbows look out. A mass of undead stands before the gate, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 175 · `story/ort_spandau.jpg` · 21:9
Verwendung: Erster Angriff auf Spandau (Dorf, 16×16)

```
dusk, viewpoint: on the riverbank opposite a castle with a massive round tower at the meeting of two rivers, at eye level. Undead carry barrels and sacks out of the castle gate; the guards lie on the ground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 176 · `story/ort_greifswald.jpg` · 21:9
Verwendung: Erster Angriff auf Greifswald (Stadt, 16×16)

```
grey day, viewpoint: on the meadow by a small river, at eye level, looking toward a brick town with a large church. On the river a barge drifts unmanned; undead walk along the towpath toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 177 · `story/ort_halle.jpg` · 21:9
Verwendung: Erster Angriff auf Halle (Stadt, 32×32)

```
viewpoint: on a crowded salt-works yard at eye level, looking across it toward a town with church towers. Brine wells with wooden wheels, boiling huts with steam, salt workers in their traditional dress with salt baskets. Undead enter the yard from the left and carry off sacks of salt, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 178 · `story/ort_berlin.jpg` · 21:9
Verwendung: Erster Angriff auf Berlin (Stadt, 64×64)

```
dawn, viewpoint: on a wooden causeway bridge over a river, looking toward two small brick towns on either bank with church towers. Fishermen in boats on the river look up in alarm. In the foreground, on the bridge, undead march toward the town gate, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 179 · `story/ort_delitzsch.jpg` · 21:9
Verwendung: Erster Angriff auf Delitzsch (Dorf, 16×16)

```
grey day, viewpoint: on a road between fields, at eye level, looking toward a small town with a castle. A line of grain carts waits at the town gate; undead approach the carts from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 180 · `story/ort_templin.jpg` · 21:9
Verwendung: Erster Angriff auf Templin (Dorf, 16×16)

```
grey morning, viewpoint: outside a long fieldstone town wall with small half-timbered watch houses, at eye level. Guards look out from the watch houses; skeletons climb the wall with their bony fingers in the cracks, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 181 · `story/ort_bergen_ruegen.jpg` · 21:9
Verwendung: Erster Angriff auf Bergen auf Rügen (Dorf, 16×16)

```
dusk, viewpoint: on a hilltop at the edge of an old earthen fortification, looking toward a brick church of a convent. In the earth wall below the viewer, an old carved wooden idol with several faces has been uncovered; undead kneel before it, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 182 · `story/ort_merseburg.jpg` · 21:9
Verwendung: Erster Angriff auf Merseburg (Kloster/Kirche, 16×16)

```
dusk, viewpoint: on the bank of the Saale river at eye level, looking up at a Romanesque cathedral and a castle on the hill above. Undead climb the stairs from the river toward the cathedral door; a raven flies over the towers, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 183 · `story/ort_anklam.jpg` · 21:9
Verwendung: Erster Angriff auf Anklam (Dorf, 16×16)

```
night, viewpoint: in front of a brick town gate tower at eye level. A watchman with a lantern peers through the small window in the gate; in the darkness right in front of the gate, in the foreground, the crowned lich stands still and waits, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 184 · `story/ort_bernau.jpg` · 21:9
Verwendung: Erster Angriff auf Bernau (Dorf, 16×16)

```
evening, viewpoint: outside a fieldstone town wall at eye level, looking at a gate tower. Townsmen pour hot water from the gate; undead under the gate in the foreground raise their shields, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 185 · `story/ort_wolgast.jpg` · 21:9
Verwendung: Erster Angriff auf Wolgast (Dorf, 16×16)

```
evening, viewpoint: on the shore of a wide river estuary, at eye level, looking toward a castle on an island. Far out on the water, faint church spires of a drowned city shimmer as a ghostly reflection; undead walk out of the water toward the castle, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 186 · `story/ort_herzberg.jpg` · 21:9
Verwendung: Erster Angriff auf Herzberg (Dorf, 16×16)

```
dusk, viewpoint: on the bank of a dark, slow river at water level, looking toward a small town with a brick church. The water is black as ink; pale skulls rise just under its surface and drift toward the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 187 · `story/ort_koenigswusterhausen.jpg` · 21:9
Verwendung: Erster Angriff auf Wusterhausen (Dorf, 16×16)

```
dusk, viewpoint: at a lake shore in a pine forest, at eye level. A hunting party on horseback with hounds rides along the shore; from the reeds and forest on both sides undead close in on them. A small castle tower in the background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 188 · `story/ort_torgau.jpg` · 21:9
Verwendung: Erster Angriff auf Torgau (Dorf, 16×16)

```
evening, viewpoint: on a large river ferry in midstream, standing behind the ferryman, looking toward a castle on the far bank. The passengers on the ferry are undead in cloaks; the ferryman, pole in hand, looks back over his shoulder in horror, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 189 · `story/ort_leipzig.jpg` · 21:9
Verwendung: Erster Angriff auf Leipzig (Stadt, 64×64)

```
noon, viewpoint: in the middle of a crowded market square at eye level, among wooden stalls with cloth, furs and barrels. Merchants and buyers turn toward the street entrance at the far side of the square, where undead enter in a dense column, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 190 · `story/ort_naumburg.jpg` · 21:9
Verwendung: Erster Angriff auf Naumburg (Kloster/Kirche, 16×16)

```
viewpoint: inside the west choir of a Gothic cathedral at eye level, looking at life-size stone figures of medieval founders on the walls. One noblewoman figure holds her cloak collar up to her face. Through the choir screen the shadows of undead are visible in the nave, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 191 · `story/ort_weissenfels.jpg` · 21:9
Verwendung: Erster Angriff auf Weißenfels (Dorf, 16×16)

```
dusk, viewpoint: on the Saale bank at eye level, looking at a white cliff with a castle on top. The white rock turns grey where undead climb it, as if withering, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 192 · `story/ort_vineta.jpg` · 21:9
Verwendung: Erster Angriff auf Vineta (mythischer Ort, 16×16)

```
calm evening, viewpoint: in a small boat on the sea, at water level, looking down through clear water at the towers and roofs of a sunken city on the seabed. Above the water, at the horizon, a faint mirage of the city's towers. Pale drowned faces look up from the deep, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 193 · `story/ort_prenzlau.jpg` · 21:9
Verwendung: Erster Angriff auf Prenzlau (Stadt, 16×16)

```
dusk, viewpoint: on a market square at eye level, looking up at the richly decorated brick gable of a large Gothic church, with lacelike tracery. In front of the church townsfolk stare at the undead in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 194 · `story/ort_luckau.jpg` · 21:9
Verwendung: Erster Angriff auf Luckau (Dorf, 16×16)

```
evening, viewpoint: on a field at eye level, looking toward a small town with a very large brick church. A herald on horseback rides out of the town with a banner; undead surround him on the road, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 195 · `story/ort_eberswalde.jpg` · 21:9
Verwendung: Erster Angriff auf Eberswalde (Dorf, 16×16)

```
morning, viewpoint: on a riverbank beside a row of water mills and a forge, at eye level. One mill wheel stands still, blocked by bodies; a smith in an apron stares at undead coming along the bank, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 196 · `story/ort_arkona.jpg` · 21:9
Verwendung: Erster Angriff auf Kap Arkona (mythischer Ort, 32×32)

```
night, viewpoint: on a grassy clifftop near the edge of a white chalk cliff, at eye level, looking at the ruins of an old earthen rampart and a burnt temple enclosure. Pagan islanders in cloaks stand in a ring with torches around a toppled four-headed wooden idol; the sea glimmers below the cliff. Undead approach along the cliff edge in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 197 · `story/ort_chorin.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Chorin (Kloster/Kirche, 16×16)

```
dusk, viewpoint: on a forest path at eye level, looking toward the tall red-brick west front of a Gothic Cistercian abbey church, rising above beech trees. Undead walk along the path toward the church; a monk at the door raises a crucifix, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 198 · `story/ort_pasewalk.jpg` · 21:9
Verwendung: Erster Angriff auf Pasewalk (Dorf, 16×16)

```
grey morning, viewpoint: on a battlefield outside a small town, at eye level. Old dead knights and foot soldiers in rusted armour rise from the grass; a small town with a church on the river behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 199 · `story/ort_strausberg.jpg` · 21:9
Verwendung: Erster Angriff auf Strausberg (Dorf, 16×16)

```
early evening, viewpoint: in a rowing boat on a long lake surrounded by forest, at water level, looking toward a small town on the shore. Undead stand along the shore under the trees, motionless, watching the town, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 200 · `story/ort_angermuende.jpg` · 21:9
Verwendung: Erster Angriff auf Angermünde (Dorf, 16×16)

```
dusk, viewpoint: at the edge of a lake at eye level, looking toward a small town with a castle and a monastery church. A Franciscan monk with a begging bowl walks along the shore and stops: undead come toward him out of the reeds, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 201 · `story/ort_luebben.jpg` · 21:9
Verwendung: Erster Angriff auf Lübben (Dorf, 16×16)

```
morning, viewpoint: in a punt on a narrow channel at the edge of a small town, at water level. Townsfolk on the bank throw bread into the water as offerings to the water spirits; behind them, undead come down the lane, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 202 · `story/ort_fuerstenwalde.jpg` · 21:9
Verwendung: Erster Angriff auf Fürstenwalde (Kloster/Kirche, 16×16)

```
dusk, viewpoint: on a road beside a river, at eye level, looking at a bishop's carriage with outriders entering a small town with a brick church. Undead pursue the carriage along the road in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 203 · `story/ort_meissen.jpg` · 21:9
Verwendung: Erster Angriff auf Meißen (Stadt, 32×32)

```
dusk, viewpoint: on the Elbe river bank below a steep rock, at eye level, looking up at a castle and an unfinished Gothic cathedral with scaffolding on the hilltop above a town. Undead climb the steep vineyards toward the castle, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 204 · `story/ort_dresden.jpg` · 21:9
Verwendung: Erster Angriff auf Dresden (Stadt, 16×16)

```
foggy morning, viewpoint: at the town end of a long stone arch bridge over a wide river, at eye level, looking across the bridge. Out of the fog on the bridge a column of undead marches toward the town; a toll keeper's booth stands empty, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```


### 0 Neu am 15.11.2026: Spielstile, Skillbaum, Schleichen

#### Nr. 205 · `einheiten/nachzehrer.jpg` · 3:4
Verwendung: Nachzehrer (Meuchler)

```
half-length portrait of a gaunt revenant wrapped in a burial shroud, chewing on the end of the shroud, long clawed fingers, glowing eyes, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 206 · `einheiten/gruftwaechter.jpg` · 3:4
Verwendung: Gruftwächter (Schildwache)

```
half-length portrait of an armoured skeleton guard in a kettle helmet holding a coffin lid with an iron cross as a tower shield, a hammer in the other hand, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 207 · `einheiten/knochentrommler.jpg` · 3:4
Verwendung: Knochentrommler

```
half-length portrait of a skeleton drummer in a pointed cap beating a drum with two thigh bones, a skull tied to the drum, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 208 · `einheiten/knochenhexer.jpg` · 3:4
Verwendung: Knochenhexer

```
half-length portrait of a skeleton sorcerer in a hooded robe with a bone staff, a ball of fog swirling in his open hand, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 209 · `einheiten/knochenreiter.jpg` · 3:4
Verwendung: Knochenreiter

```
portrait of a skeleton rider in a kettle helmet with lance and round shield on a skeletal horse, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 210 · `einheiten/nachtvogt.jpg` · 3:4
Verwendung: Nachtvogt (Kommandeur, Aura Schatten)

```
half-length portrait of a medieval executioner in a black hood and mask with a long two-handed executioner's sword, standing in deep shadow, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 211 · `einheiten/seuchenvogt.jpg` · 3:4
Verwendung: Seuchenvogt (Kommandeur, Aura Horde)

```
half-length portrait of a plague-year grave digger in a wide-brimmed hat and a beaked mask, a spade over his shoulder and a lantern in his hand, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 212 · `einheiten/gruftfuerst.jpg` · 3:4
Verwendung: Gruftfürst (Kommandeur, Aura Bollwerk)

```
half-length portrait of a crowned skeleton prince in heavy plate armour with a great shield and a war hammer, in front of a megalithic stone chamber, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 213 · `icons/pfad_schatten.png` · 1:1
Verwendung: Lich-Pfad Schatten (Schleichen)

```
a hooded figure melting into its own long shadow, a sleeping watchman's lantern on the ground, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 214 · `icons/pfad_flut.png` · 1:1
Verwendung: Lich-Pfad Flut (Masse statt Klasse)

```
an endless crowd of skeletons pouring out of open graves like a wave, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 215 · `icons/pfad_auslese.png` · 1:1
Verwendung: Lich-Pfad Auslese (Klasse statt Masse)

```
a single crowned skeleton knight standing on a heap of broken weapons, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 216 · `icons/pfad_hexerei.png` · 1:1
Verwendung: Lich-Pfad Hexerei (aktive Fähigkeiten)

```
a skeletal hand holding a burning soul flame above an open book of spells, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 217 · `icons/pfad_eile.png` · 1:1
Verwendung: Lich-Pfad Eile (Beweglichkeit)

```
a skeleton horse in full gallop with flying mane, seen from the side, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 218 · `icons/pfad_bollwerk.png` · 1:1
Verwendung: Lich-Pfad Bollwerk (schwer, untötbar)

```
a wall of overlapping coffin-lid shields with a skull looking over the rim, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 219 · `icons/merkmal_meuchler.png` · 1:1
Verwendung: Merkmal Meuchler

```
a dagger held behind a back in a bony hand, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 220 · `icons/merkmal_schwarm.png` · 1:1
Verwendung: Merkmal Schwarm

```
a tight cluster of many small skulls, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 221 · `icons/merkmal_sturmangriff.png` · 1:1
Verwendung: Merkmal Sturmangriff

```
a lowered lance with a fluttering pennon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 222 · `icons/merkmal_schildwache.png` · 1:1
Verwendung: Merkmal Schildwache

```
a tower shield planted in the ground, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 223 · `icons/merkmal_zaeh.png` · 1:1
Verwendung: Merkmal Zäh

```
a cracked bone bound with a growing vine of stitches, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 224 · `icons/merkmal_trommler.png` · 1:1
Verwendung: Merkmal Trommler

```
a drum with two crossed thigh bones, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 225 · `icons/wache_schlaeft.png` · 1:1
Verwendung: Wache schläft (Marke über der Einheit)

```
a snuffed-out candle with a thin trail of smoke, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 226 · `icons/wache_posten.png` · 1:1
Verwendung: Wache auf Posten

```
a wide-open human eye, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 227 · `icons/wache_streife.png` · 1:1
Verwendung: Wache auf Streife

```
a lantern on a pole with footprints around it in a circle, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 228 · `icons/glocke.png` · 1:1
Verwendung: Glöckner / Glocke läutet

```
a swinging church bell with its rope, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 229 · `banner/angriffsplan.jpg` · 3:1
Verwendung: Kopfbild des Fensters „Angriff auf …“ (Seite wählen)

```
a small medieval village at night seen from a dark heath hill, a few watch fires, skeletal figures crouching in the tall grass in the foreground, wind bending the grass, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 1 Grundlagen (Rahmen, Papier, Titel)

#### Nr. 230 · `ui/papier.jpg` · 1:1
Verwendung: Hintergrund aller Fenster und Leisten (wird gekachelt)

```
blank aged rag paper with faint fibres, foxing stains and a few tiny ink specks, seamless tileable texture, even lighting, no motif, no text, flat top-down view, like the paper of an Albrecht Dürer print from around 1500, realistic high-resolution scan
```

#### Nr. 231 · `ui/papier_dunkel.jpg` · 1:1
Verwendung: Seitenleiste und untere Leiste (dunkler Grund, gekachelt)

```
dark smoke-stained parchment, almost black-brown, scorched and worn, with faint hatching, seamless tileable texture, even lighting, no motif, no text, flat top-down view, like the paper of an Albrecht Dürer print from around 1500, realistic high-resolution scan
```

#### Nr. 232 · `ui/rahmen.png` · 1:1
Verwendung: Zierrahmen für Fenster (wird in 9 Teile zerschnitten)

```
ornamental rectangular frame border of twisted thorn branches, bones and small skulls in the four corners, completely empty plain paper in the middle, symmetric, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 233 · `ui/ecke.png` · 1:1
Verwendung: Eckzier für Panels (oben links, wird gespiegelt)

```
corner ornament: a small skull with crossed bones entwined by a dry thorn vine, filling the top-left corner only, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 234 · `ui/trenner.png` · 21:9
Verwendung: Trennlinie zwischen Abschnitten

```
horizontal ornament: a femur bone with a thorn vine wound around it, ending in tiny skulls at both ends, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 235 · `titel.jpg` · 16:9
Verwendung: Ladebildschirm und Titel

```
a crowned lich in a tattered robe rises from an opened bronze-age burial mound on a heath hill at night, ravens circling, bare twisted trees, distant church tower, mist over the heather, dead lie around, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 236 · `erwachen.jpg` · 16:9
Verwendung: Fenster beim Spielstart (Erwachen)

```
inside a dark burial chamber of stone slabs, a skeletal lich opening his eyes on a stone bier, a glowing phylactery jar beside him, roots hanging from the ceiling, grave goods of bronze, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 237 · `tod_lich.jpg` · 16:9
Verwendung: Fenster, wenn der Lich fällt

```
a lich collapsing on a battlefield, his crown rolling away, his spirit drawn back as smoke towards a distant burial mound, peasants with torches and pitchforks, corpses everywhere, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 238 · `sieg_brocken.jpg` · 16:9
Verwendung: Endbildschirm (Brocken erreicht)

```
the lich standing on the bare Brocken summit at Walpurgis night, a vast army of skeletons and corpses below, witches fleeing on brooms, storm clouds, lightning, granite boulders, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 2 Ressourcen-Symbole

#### Nr. 239 · `icons/res_leichen.png` · 1:1
Verwendung: Ressource Leichen (Leiste unten, Kosten)

```
a shrouded human corpse lying on a wooden plank, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 240 · `icons/res_knochen.png` · 1:1
Verwendung: Ressource Knochen (Leiste unten, Kosten)

```
a pile of bones with a skull on top, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 241 · `icons/res_seelen.png` · 1:1
Verwendung: Ressource Seelen (Leiste unten, Kosten)

```
a small wailing ghost-like soul flame rising from a clay urn, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 242 · `icons/res_wissen.png` · 1:1
Verwendung: Ressource Wissen (Leiste unten, Kosten)

```
an old open grimoire with a skull resting on it, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 243 · `icons/res_kommando.png` · 1:1
Verwendung: Ressource Kommando (Leiste unten, Kosten)

```
a tattered black war banner on a bone pole, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 3 Aktions-Symbole (Seitenleiste, Kampf)

#### Nr. 244 · `icons/act_huegelgrab.png` · 1:1
Verwendung: Hügelgrab

```
a bronze-age burial mound with a stone entrance, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 245 · `icons/act_rekrutieren.png` · 1:1
Verwendung: Rekrutieren

```
a skeletal hand rising out of a grave, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 246 · `icons/act_bauen.png` · 1:1
Verwendung: Bauen

```
a hammer and chisel crossed over a stone block with a skull carving, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 247 · `icons/act_rasten.png` · 1:1
Verwendung: Rasten

```
a crescent moon above a smouldering campfire, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 248 · `icons/act_inventar.png` · 1:1
Verwendung: Inventar

```
an iron-bound wooden chest with a crown and a horn inside, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 249 · `icons/act_menue.png` · 1:1
Verwendung: Menü

```
a closed book with clasps and a ribbon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 250 · `icons/act_los.png` · 1:1
Verwendung: Los (Befehle ausführen)

```
a skeleton drummer beating a war drum, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 251 · `icons/act_chronik.png` · 1:1
Verwendung: Chronik

```
a rolled parchment scroll with a quill, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 252 · `icons/act_bedrohung.png` · 1:1
Verwendung: Bedrohung

```
a burning torch and a pitchfork crossed, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 253 · `icons/act_ley_sprung.png` · 1:1
Verwendung: Ley-Sprung

```
a standing stone with a spiral carving and a crackling beam of light, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 254 · `icons/act_portal.png` · 1:1
Verwendung: Portal errichten

```
a stone arch of two menhirs and a lintel with a swirling void inside, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 255 · `icons/act_zug_beenden.png` · 1:1
Verwendung: Zug beenden

```
an hourglass with the sand run out, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 256 · `icons/act_rueckzug.png` · 1:1
Verwendung: Rückzug

```
a lowered torn banner and footprints leading away, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 257 · `icons/act_abziehen.png` · 1:1
Verwendung: Abziehen

```
a closed city gate seen from outside, the army turning away, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 258 · `icons/act_kanten.png` · 1:1
Verwendung: Feldkanten

```
a small hexagonal tiling drawn as engraved lines, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 259 · `icons/act_token.png` · 1:1
Verwendung: Token-Modus

```
a round wax seal with a skull imprint, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 260 · `icons/act_hilfe.png` · 1:1
Verwendung: Hilfe

```
an open book with a pointing hand (manicule), single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 4 Werte- und Zustands-Symbole (Einheitenkarte)

#### Nr. 261 · `icons/stat_leben.png` · 1:1
Verwendung: Lebenspunkte

```
an anatomical human heart, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 262 · `icons/stat_schaden.png` · 1:1
Verwendung: Schaden

```
a notched broadsword, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 263 · `icons/stat_nahkampf.png` · 1:1
Verwendung: Nahkampf

```
a clenched armoured gauntlet, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 264 · `icons/stat_reichweite.png` · 1:1
Verwendung: Reichweite

```
a crossbow bolt and a longbow, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 265 · `icons/stat_bewegung.png` · 1:1
Verwendung: Bewegung

```
bare skeletal feet walking, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 266 · `icons/stat_initiative.png` · 1:1
Verwendung: Initiative

```
a lightning bolt striking a skull, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 267 · `icons/stat_ruestung.png` · 1:1
Verwendung: Rüstung

```
a dented heater shield, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 268 · `icons/stat_magieresistenz.png` · 1:1
Verwendung: Magieresistenz

```
a pentagram drawn in a circle, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 269 · `icons/stat_seelenschild.png` · 1:1
Verwendung: Seelenschild

```
a shield made of swirling ghostly faces, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 270 · `icons/stat_energie.png` · 1:1
Verwendung: Energie

```
a burning candle stub, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 271 · `icons/stat_auge.png` · 1:1
Verwendung: Sicht

```
a single wide-open human eye, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 272 · `icons/stat_ohr.png` · 1:1
Verwendung: Gehör

```
a human ear, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 273 · `icons/stat_nase.png` · 1:1
Verwendung: Geruch

```
a human nose sniffing, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 274 · `icons/stat_ahnungslos.png` · 1:1
Verwendung: Wache ahnungslos

```
a sleeping guard's closed eye with a small Z-like curl of breath, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 275 · `icons/stat_misstrauisch.png` · 1:1
Verwendung: Wache misstrauisch

```
a half-open suspicious eye under a raised eyebrow, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 276 · `icons/stat_alarmiert.png` · 1:1
Verwendung: Wache alarmiert

```
a ringing church bell, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 277 · `icons/stat_fuehrerlos.png` · 1:1
Verwendung: Führerlos

```
a broken commander's staff, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 278 · `icons/stat_ueberraschung.png` · 1:1
Verwendung: Überraschungstreffer

```
a dagger striking from a shadow, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 5 Tageszeiten (Uhr unten rechts)

#### Nr. 279 · `icons/zeit_nacht.png` · 1:1
Verwendung: Tageszeit Nacht

```
round medallion: a full moon with a skull face among stars, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 280 · `icons/zeit_morgen.png` · 1:1
Verwendung: Tageszeit Morgen

```
round medallion: a pale sun rising through mist over heather, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 281 · `icons/zeit_tag.png` · 1:1
Verwendung: Tageszeit Tag

```
round medallion: a blazing sun with a stern face and long rays, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 282 · `icons/zeit_abend.png` · 1:1
Verwendung: Tageszeit Abend

```
round medallion: a setting sun behind a gallows on a hill, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 6 Fenster-Banner (Kopfbild der Fenster)

#### Nr. 283 · `banner/rekrutieren.jpg` · 21:9
Verwendung: Fenster Rekrutieren

```
necromancer raising skeletons and corpses from open graves in a churchyard, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 284 · `banner/bauen.jpg` · 21:9
Verwendung: Fenster Bauen

```
skeleton workers building a bone-and-stone hall inside a huge burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 285 · `banner/chronik.jpg` · 21:9
Verwendung: Fenster Chronik

```
an old monk-chronicler writing by candlelight, a skeleton dictating over his shoulder, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 286 · `banner/inventar.jpg` · 21:9
Verwendung: Fenster Inventar

```
a treasure vault with a crown, a sword, a horn and relics among bones, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 287 · `banner/rasten.jpg` · 21:9
Verwendung: Fenster Rasten

```
an undead army camped around fires under a crescent moon on a heath, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 288 · `banner/ley.jpg` · 21:9
Verwendung: Fenster Ley-Sprung

```
standing stones linked by glowing lines across a dark landscape, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 289 · `banner/spielstaende.jpg` · 21:9
Verwendung: Fenster Spielstände

```
a monk's desk with stacked books and an hourglass, a skull as bookend, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 290 · `banner/sieg.jpg` · 21:9
Verwendung: Fenster Kampf gewonnen

```
skeletons raising tattered banners over a burning village, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 291 · `banner/niederlage.jpg` · 21:9
Verwendung: Fenster Kampf verloren

```
a field of shattered skeletons, crows feeding, a priest blessing the ground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 292 · `banner/rueckzug.jpg` · 21:9
Verwendung: Fenster Rückzug

```
an undead column retreating through a forest in the rain, stragglers falling behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 293 · `banner/belagerung.jpg` · 21:9
Verwendung: Fenster Ummauerte Stadt / Abziehen

```
a fortified Hanseatic town wall with towers and a gate under siege by giants and a bone ballista, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 7 Erzähler

#### Nr. 294 · `portraits/chronist.png` · 1:1
Verwendung: Erzähler-Leiste (Chronist)

```
bust portrait of an old gaunt monk-chronicler with quill and spectacles, hollow eyes, cowl, in a round frame, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 295 · `portraits/hinweis.png` · 1:1
Verwendung: Hinweis-Symbol der Erzähler-Leiste

```
an oil lamp with a small flame, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 8 Fraktionswappen

#### Nr. 296 · `wappen/untote.png` · 1:1
Verwendung: Fraktion Untote (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a crowned skull over two crossed femurs, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 297 · `wappen/hanse.png` · 1:1
Verwendung: Fraktion Hanse (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a Hanseatic cog ship with a single sail, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 298 · `wappen/welfen.png` · 1:1
Verwendung: Fraktion Welfen (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a leaping lion, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 299 · `wappen/askanier.png` · 1:1
Verwendung: Fraktion Askanier (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a bear on a crenellated wall, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 300 · `wappen/klerus.png` · 1:1
Verwendung: Fraktion Klerus (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a crozier and a crucifix crossed, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 301 · `wappen/hexen.png` · 1:1
Verwendung: Fraktion Hexen und Haine (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a broom, a black cat and a sickle moon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 302 · `wappen/grafen.png` · 1:1
Verwendung: Fraktion Grafen (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a castle tower with a count's coronet, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 303 · `wappen/mecklenburg.png` · 1:1
Verwendung: Fraktion Mecklenburg (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a crowned bull's head, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 304 · `wappen/wettiner.png` · 1:1
Verwendung: Fraktion Wettiner (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a lion standing on a striped field, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 305 · `wappen/wodan.png` · 1:1
Verwendung: Fraktion Wodan-Kult (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: two ravens and an eight-legged horse, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 306 · `wappen/spreewald.png` · 1:1
Verwendung: Fraktion Spreewald (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a serpent with a small crown among reeds, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 307 · `wappen/wattenmeer.png` · 1:1
Verwendung: Fraktion Wattenmeer (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a sunken church bell among waves, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 308 · `wappen/heidegeister.png` · 1:1
Verwendung: Fraktion Heidegeister (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a will-o'-the-wisp above heather and a juniper bush, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 9 Pantheon-Siegel

#### Nr. 309 · `pantheon/heide.png` · 1:1
Verwendung: Pantheon Heide-Pantheon

```
round wax seal medallion showing a megalithic dolmen under a heath moon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 310 · `pantheon/wodan.png` · 1:1
Verwendung: Pantheon Wilde Jagd

```
round wax seal medallion showing a horned huntsman leading hounds across the sky, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 311 · `pantheon/spreewald.png` · 1:1
Verwendung: Pantheon Wendische Geister

```
round wax seal medallion showing a noon-witch with a sickle in a wheat field, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 312 · `pantheon/wattenmeer.png` · 1:1
Verwendung: Pantheon Versunkene Städte

```
round wax seal medallion showing the drowned town of Rungholt under the waves, a church spire, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 313 · `pantheon/harz.png` · 1:1
Verwendung: Pantheon Walpurgis-Zirkel

```
round wax seal medallion showing witches dancing around a fire on a mountain top, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 10 Gebäude des Hügelgrabs (Baumenü)

#### Nr. 314 · `gebaeude/phylactery.jpg` · 4:3
Verwendung: Gebäude Phylakterium

```
a glowing reliquary jar on an altar of skulls in a burial chamber, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 315 · `gebaeude/boneWorkshop.jpg` · 4:3
Verwendung: Gebäude Knochenwerkstatt

```
skeletons sawing and assembling bones at workbenches, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 316 · `gebaeude/corpsePit.jpg` · 4:3
Verwendung: Gebäude Leichengrube

```
a deep pit full of corpses, ghouls climbing out, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 317 · `gebaeude/soulKennel.jpg` · 4:3
Verwendung: Gebäude Seelenzwinger

```
iron cages holding wailing ghosts, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 318 · `gebaeude/deadHall.jpg` · 4:3
Verwendung: Gebäude Totenhalle

```
a long vaulted crypt hall lined with standing skeleton warriors, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 319 · `gebaeude/knowledgeAltar.jpg` · 4:3
Verwendung: Gebäude Wissensaltar

```
a stone altar piled with stolen books, candles and an open skull, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 320 · `gebaeude/boneForge.jpg` · 4:3
Verwendung: Gebäude Knochenschmiede

```
a forge where bones are hammered into weapons, sparks and smoke, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 321 · `gebaeude/heathAltar.jpg` · 4:3
Verwendung: Gebäude Heidealtar

```
a heather-covered megalith altar with offerings and a spirit rising, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 11 Artefakte (Inventar)

#### Nr. 322 · `artefakte/reichsschwert.png` · 1:1
Verwendung: Artefakt Reichsschwert Barbarossas

```
an imperial longsword with a cross guard and an eagle pommel, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 323 · `artefakte/glocken_rungholt.png` · 1:1
Verwendung: Artefakt Glocke von Rungholt

```
a barnacle-covered bronze church bell, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 324 · `artefakte/svantevit_horn.png` · 1:1
Verwendung: Artefakt Trinkhorn des Svantevit

```
an ornate drinking horn with silver bands, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 325 · `artefakte/schlangenkrone.png` · 1:1
Verwendung: Artefakt Krone des Schlangenkönigs

```
a tiny golden crown with a serpent coiled through it, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 326 · `artefakte/lehniner_weissagung.png` · 1:1
Verwendung: Artefakt Lehniner Weissagung

```
a sealed prophecy scroll with a broken wax seal, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 327 · `artefakte/merseburger_sprueche.png` · 1:1
Verwendung: Artefakt Merseburger Zaubersprüche

```
an old manuscript leaf with runes and knotwork, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 328 · `artefakte/reliquienkasten.png` · 1:1
Verwendung: Artefakt Reliquienkasten der Ottonen

```
a small house-shaped reliquary shrine with gems, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 329 · `artefakte/zwergenhammer.png` · 1:1
Verwendung: Artefakt Zwergenhammer

```
a heavy short hammer with runes on the head, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 330 · `artefakte/jagdhorn.png` · 1:1
Verwendung: Artefakt Horn der Wilden Jagd

```
a large hunting horn with a strap, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 331 · `artefakte/codex_corvey.png` · 1:1
Verwendung: Artefakt Codex von Corvey

```
a heavy bound codex with metal corners, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 332 · `artefakte/huenenknochen.png` · 1:1
Verwendung: Artefakt Hünenknochen

```
a gigantic thigh bone, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 333 · `artefakte/herz_der_heide.png` · 1:1
Verwendung: Artefakt Herz der Heide

```
a heart-shaped stone with heather growing from it, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 12 Einheitenbilder (Rekrutieren, Einheitenkarte, Initiativeleiste)

#### Nr. 334 · `einheiten/lich.jpg` · 3:4
Verwendung: Lich

```
half-length portrait of a crowned lich in a tattered purple robe with a staff topped by a glowing green stone, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 335 · `einheiten/ghul.jpg` · 3:4
Verwendung: Ghul

```
half-length portrait of a hunched emaciated ghoul with long claws, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 336 · `einheiten/skelett.jpg` · 3:4
Verwendung: Skelett

```
half-length portrait of a skeleton warrior with a rusty sword and round shield, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 337 · `einheiten/bogner.jpg` · 3:4
Verwendung: Skelett-Bogenschütze

```
half-length portrait of a skeleton archer drawing a longbow, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 338 · `einheiten/leichenhund.jpg` · 3:4
Verwendung: Leichenhund

```
half-length portrait of a rotting dead hound with exposed ribs, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 339 · `einheiten/zombie.jpg` · 3:4
Verwendung: Zombie

```
half-length portrait of a shambling rotting peasant corpse, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 340 · `einheiten/schleuderer.jpg` · 3:4
Verwendung: Knochenschleuderer

```
half-length portrait of a skeleton with a sling and a pouch of skull stones, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 341 · `einheiten/geist.jpg` · 3:4
Verwendung: Geist

```
half-length portrait of a translucent wailing ghost in a burial shroud, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 342 · `einheiten/knochenschuetze.jpg` · 3:4
Verwendung: Knochenschütze

```
half-length portrait of a skeleton crossbowman with a bone crossbow, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 343 · `einheiten/moorleiche.jpg` · 3:4
Verwendung: Moorleiche

```
half-length portrait of a leathery bog body with a rope around its neck, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 344 · `einheiten/todesritter.jpg` · 3:4
Verwendung: Todesritter

```
half-length portrait of a skeletal knight in black plate armour on a skeletal horse, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 345 · `einheiten/totenlicht.jpg` · 3:4
Verwendung: Totenlicht

```
half-length portrait of a floating skull with a candle flame inside, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 346 · `einheiten/gefallene_schwester.jpg` · 3:4
Verwendung: Gefallene Schwester

```
half-length portrait of a dead nun with a torn veil and a rosary of finger bones, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 347 · `einheiten/grabdruidin.jpg` · 3:4
Verwendung: Grabdruidin

```
half-length portrait of an undead druid woman with a sickle and mistletoe, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 348 · `einheiten/nekromant.jpg` · 3:4
Verwendung: Nekromant

```
half-length portrait of a gaunt necromancer in a hooded robe with a skull lantern, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 349 · `einheiten/knochenballiste.jpg` · 3:4
Verwendung: Balliste

```
half-length portrait of a siege ballista built from bones and sinew, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 350 · `einheiten/fleischriese.jpg` · 3:4
Verwendung: Fleischriese

```
half-length portrait of a huge stitched giant of many corpses, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 351 · `einheiten/knochendrache.jpg` · 3:4
Verwendung: Knochendrache

```
half-length portrait of a dragon skeleton with tattered wings, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 352 · `einheiten/wasserleiche.jpg` · 3:4
Verwendung: Wasserleiche

```
half-length portrait of a bloated drowned corpse dripping water, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 353 · `einheiten/reiterfuerst.jpg` · 3:4
Verwendung: Bronzezeitlicher Reiterfürst

```
half-length portrait of a skeletal bronze-age chieftain on horseback with a bronze sword, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 354 · `einheiten/huenenkoenig.jpg` · 3:4
Verwendung: Hünenkönig

```
half-length portrait of a giant skeletal king of the megalith builders with a stone club, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 355 · `einheiten/widukind.jpg` · 3:4
Verwendung: Widukinds Schatten

```
half-length portrait of the ghost of a Saxon duke with a winged helmet and a seax, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 356 · `einheiten/ratsherr.jpg` · 3:4
Verwendung: Ratsherr von Rungholt

```
half-length portrait of a drowned town councillor in rich robes covered in seaweed, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 357 · `einheiten/totenjaeger.jpg` · 3:4
Verwendung: Totenjäger

```
half-length portrait of an undead huntsman with a spear and a hound, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 358 · `einheiten/bauer.jpg` · 3:4
Verwendung: Bauer

```
half-length portrait of a medieval peasant with a pitchfork, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 359 · `einheiten/stadtwache.jpg` · 3:4
Verwendung: Stadtwache

```
half-length portrait of a town guard with a halberd and a kettle hat, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 360 · `einheiten/armbrust.jpg` · 3:4
Verwendung: Lüneburger Armbrustschütze

```
half-length portrait of a town crossbowman with a pavise shield, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 361 · `einheiten/ritter.jpg` · 3:4
Verwendung: Ritter

```
half-length portrait of a mounted knight in plate armour with a lance, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 362 · `einheiten/balliste.jpg` · 3:4
Verwendung: Stadtballiste

```
half-length portrait of a town siege ballista on a wall, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 363 · `einheiten/moench.jpg` · 3:4
Verwendung: Mönch

```
half-length portrait of a tonsured monk with a lantern, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 364 · `einheiten/priester.jpg` · 3:4
Verwendung: Priester

```
half-length portrait of a priest raising a crucifix, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 365 · `einheiten/kleriker.jpg` · 3:4
Verwendung: Kleriker

```
half-length portrait of a cleric with a censer and holy water, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 366 · `einheiten/heideschwester.jpg` · 3:4
Verwendung: Heideschwester

```
half-length portrait of a nun herb-healer of the heath, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 367 · `einheiten/hexe.jpg` · 3:4
Verwendung: Hexe

```
half-length portrait of a witch with a staff and herbs, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 368 · `einheiten/brockenhexe.jpg` · 3:4
Verwendung: Hexenkönigin vom Brocken

```
half-length portrait of a witch queen on the Brocken with a crown of antlers, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 369 · `einheiten/irrlicht.jpg` · 3:4
Verwendung: Irrlicht

```
half-length portrait of a will-o'-the-wisp over a bog, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 370 · `einheiten/moorgeist.jpg` · 3:4
Verwendung: Moorgeist

```
half-length portrait of a bog spirit rising from black water, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 371 · `einheiten/rattenfaenger.jpg` · 3:4
Verwendung: Rattenfänger

```
half-length portrait of the pied piper with a flute and rats, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 372 · `einheiten/druide.jpg` · 3:4
Verwendung: Druide

```
half-length portrait of an old druid with a staff and oak leaves, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 373 · `einheiten/druidin.jpg` · 3:4
Verwendung: Hügelgrab-Druidin

```
half-length portrait of a druidess guarding a burial mound, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 374 · `einheiten/schwarzer_hund.jpg` · 3:4
Verwendung: Schwarzer Hund

```
half-length portrait of a huge black hound with burning eyes, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 375 · `einheiten/wode.jpg` · 3:4
Verwendung: Der Wode

```
half-length portrait of the one-eyed god Wode with a wide hat and a spear, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 376 · `einheiten/zwergenkoenig.jpg` · 3:4
Verwendung: Hügelgrab-Zwergenkönig

```
half-length portrait of a dwarf king with a hammer under a burial mound, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 377 · `einheiten/heidekoenigin.jpg` · 3:4
Verwendung: Die Heidekönigin

```
half-length portrait of a pale queen of the heath crowned with heather, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 378 · `einheiten/sachsenkrieger.jpg` · 3:4
Verwendung: Sachsenkrieger

```
half-length portrait of an old Saxon warrior with a round shield and seax, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 379 · `einheiten/wodansrabe.jpg` · 3:4
Verwendung: Wodansrabe

```
half-length portrait of a huge raven with spread wings, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 380 · `einheiten/wilder_jaeger.jpg` · 3:4
Verwendung: Wilder Jäger

```
half-length portrait of a spectral huntsman on a horse in the storm, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 381 · `einheiten/hackelberg.jpg` · 3:4
Verwendung: Hackelberg

```
half-length portrait of the cursed huntsman Hackelberg with hounds, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 382 · `einheiten/lutki.jpg` · 3:4
Verwendung: Lutki

```
half-length portrait of tiny Wendish house spirits, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 383 · `einheiten/wassermann.jpg` · 3:4
Verwendung: Wassermann

```
half-length portrait of a water man with green skin and a net, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 384 · `einheiten/rusalka.jpg` · 3:4
Verwendung: Rusalka

```
half-length portrait of a pale water maiden with long wet hair, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 385 · `einheiten/mittagsfrau.jpg` · 3:4
Verwendung: Mittagsfrau

```
half-length portrait of the noon witch with a sickle in a white dress, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 386 · `einheiten/schlangenkoenig.jpg` · 3:4
Verwendung: Schlangenkönig

```
half-length portrait of a giant crowned serpent, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 387 · `einheiten/ertrunkener.jpg` · 3:4
Verwendung: Ertrunkener

```
half-length portrait of a drowned sailor, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 388 · `einheiten/wattjungfrau.jpg` · 3:4
Verwendung: Wattjungfrau

```
half-length portrait of a ghostly maiden of the mudflats, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 389 · `einheiten/klabautermann.jpg` · 3:4
Verwendung: Klabautermann

```
half-length portrait of a small ship goblin with a mallet and pipe, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 390 · `einheiten/blanker_hans.jpg` · 3:4
Verwendung: Blanker Hans

```
half-length portrait of the storm flood as a giant figure of waves with a white mane, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 391 · `einheiten/ophan.jpg` · 3:4
Verwendung: Ophan

```
half-length portrait of a wheel within a wheel covered with eyes, wreathed in fire, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 392 · `einheiten/cherub.jpg` · 3:4
Verwendung: Cherub

```
half-length portrait of a four-faced winged cherub with a flaming sword, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### Nr. 393 · `einheiten/seraph.jpg` · 3:4
Verwendung: Seraph

```
half-length portrait of a six-winged seraph covered in flames, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

## Später überarbeiten

Kevin (19.11.2026): Bilder, die nicht ganz zum Prompt passen, bleiben vorerst drin – wichtiger ist, dass überhaupt ein Bild da ist. Hier gesammelt, damit sie später neu erzeugt werden können. Die Nummer bleibt dieselbe, die Datei wird einfach ersetzt.

| Nr. | Bild | Was nicht passt | Hinweis für den neuen Prompt |
|-|-|-|-|
| 399 | `story/sturmleitern.jpg` | Die Verteidiger auf der Mauer sind Skelette – ergibt keinen Sinn | neuer Prompt unten |
| 033 | `story/ort_ebstorf.jpg` | Moderne Weltkarte mit Kontinenten statt der runden Ebstorfer Karte | „round medieval T-O world map, Jerusalem in the centre, Christ's head at the top, his hands left and right, his feet at the bottom“ |
| 013 | `story/artefakt_merseburger_sprueche.jpg` | Auf der Buchseite ist ein Skelett gezeichnet statt nur Schriftzeilen | „the open pages show only two short blocks of handwriting, no pictures on the pages“ |
| 022 | `story/ort_schneverdingen.jpg` | Der verdorrte graue Heidestreifen fehlt | Streifen an den Anfang des Prompts stellen |
| 014 | `story/artefakt_reliquienkasten.jpg` | Schädel im Schrein statt Hand, die einen Knochen herausnimmt | Hand und Knochen an den Anfang stellen |
| 045 | `story/ort_unterluess.jpg` | Kohlenmeiler sieht aus wie eine leuchtende Scheibe am Boden | „a tall dome-shaped charcoal kiln covered with earth, smoke rising from its top“ |

**Lehre für Prompts:** Kommen Untote und Lebende im selben Bild vor, überträgt das Bildprogramm „skeleton/undead“ gern auf alle Figuren. Die Lebenden deshalb ausdrücklich als lebende Menschen mit Gesichtern beschreiben (z. B. „living human townsmen with bearded faces“), möglichst früh im Prompt.

#### Neuer Prompt für Nr. 399 · `story/sturmleitern.jpg` · 21:9

```
viewpoint: outside the town on the ground, behind a crowd of attacking skeletons, looking up at a tall stone town wall with crenellations and a gate tower. On top of the wall stand living human defenders: townsmen and guards with bearded faces, kettle helmets and padded coats, aiming crossbows down and pushing a ladder away with a forked pole. Skeletons climb crude ladders made of bones; one ladder topples backward. In the left foreground skeletons crank a ballista made of bones. Of the town only roofs and a church spire rise above the wall, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

## Erledigt

### Story-Bilder für Kommandeure, Artefakte und die ersten Orte (eingebaut 19.11.2026, Nr. 001–052)

Aus Kevins Ordner `Desktop/Story` (`Qwen_image_2.1_00207` = Nr. 001 bis `00258` = Nr. 052), 2160 × 928, als JPG Qualität 84 abgelegt. Nr. 040 (Bergedorf): Pseudoschrift oben rechts und ein Logo-Zeichen unten rechts von Claude wegretuschiert.

#### Nr. 001 · `story/kommandeur_reiterfuerst.jpg` · 21:9
Verwendung: Bronzezeitlicher Reiterfürst – Ahne erhebt sich nach dem Sieg in Pestruper Gräberfeld

```
night, viewpoint: standing among low heather-covered burial mounds at eye level, looking toward the largest mound, whose side has broken open. Out of the opening rides a skeletal bronze-age chieftain on a skeletal horse, a bronze sword raised, a gold arm ring on the bony wrist, horse bones still wrapped in rotten leather harness. Behind him, across the sky, faint riders and hounds of the Wild Hunt race through the clouds. In the foreground the crowned lich stands with his back to the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 002 · `story/kommandeur_huenenkoenig.jpg` · 21:9
Verwendung: Hünenkönig – Ahne erhebt sich nach dem Sieg in Sieben Steinhäuser

```
dusk, viewpoint: crouching low in a pine forest clearing, looking at a megalithic dolmen of huge granite boulders. The massive capstone is being pushed up from below by enormous skeletal hands; between the support stones the skull of a giant king, twice the size of a man, with a crude stone crown, looks out. Pine trunks frame the scene, moss and roots on the stones. Small undead servants kneel in the foreground, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 003 · `story/kommandeur_widukind.jpg` · 21:9
Verwendung: Widukinds Schatten – Ahne erhebt sich nach dem Sieg in Externsteine

```
night, viewpoint: on the forest floor at the foot of tall weathered sandstone rock pillars, looking up. A carved relief of the Descent from the Cross on the rock face is cracking. From the rock steps a ghostly Saxon duke in a winged helmet and chain mail, a seax in his hand, his figure half transparent, drawn in fine light hatching. A small rock chamber high in the cliff with a round window; mist between the pillars; the crowned lich waits at the bottom edge of the picture, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 004 · `story/kommandeur_ratsherr.jpg` · 21:9
Verwendung: Ratsherr von Rungholt – Ahne erhebt sich nach dem Sieg in Rungholt

```
low tide at dusk, viewpoint: at eye level on the wet mudflats, looking toward the broken walls of a sunken church. In the middle ground a drowned town councillor rises out of a tidal creek: a rich fur-trimmed robe heavy with seaweed and mud, a heavy chain of office around his neck, a pewter beer tankard in one bony hand, his face half skull. Water runs off his sleeves. Gulls overhead, a low stormy sky; the crowned lich stands in the foreground with his back to the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 005 · `story/kommandeur_nachtvogt.jpg` · 21:9
Verwendung: Nachtvogt – Kommandeur zum ersten Mal rekrutiert

```
night, viewpoint: standing at the foot of a gallows hill at eye level, looking up the slope. At the top an old wooden gallows with an empty noose; in front of it a tall executioner in a black hood and mask climbs out of a shallow grave, the long two-handed executioner's sword in his hands. A lantern lying in the grass goes out, its smoke curling. Thin moon behind clouds, crows on the gallows beam, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 006 · `story/kommandeur_seuchenvogt.jpg` · 21:9
Verwendung: Seuchenvogt – Kommandeur zum ersten Mal rekrutiert

```
grey morning, viewpoint: at the edge of a large plague pit outside a town wall, looking down into it at a slight angle. A gravedigger in a wide-brimmed hat and a beaked plague mask stands in the pit, a spade over his shoulder and a lantern in his hand; around him shrouded corpses begin to rise and turn their heads toward him. A death cart with a wheel and a bell stands at the rim. In the background a church tower and the town wall, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 007 · `story/kommandeur_gruftfuerst.jpg` · 21:9
Verwendung: Gruftfürst – Kommandeur zum ersten Mal rekrutiert

```
viewpoint: inside a low megalithic burial chamber of stone slabs, standing at the entrance and looking in. A crowned skeleton prince in heavy, rusted plate armour rises from a stone bier; he holds a great shield made from a coffin lid with an iron cross and a war hammer. Bronze vessels and urns along the walls; dust and small stones fall from the ceiling. A faint glow from behind the viewer lights his armour, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 008 · `story/artefakt_reichsschwert.jpg` · 21:9
Verwendung: Reichsschwert Barbarossas – gefunden in Kyffhäuser

```
viewpoint: inside a hall in a mountain cave, standing next to a stone table where an old emperor sleeps with his head on his arms, his long beard grown through the table. In the foreground a skeletal hand with bronze rings lifts a long imperial sword with a cross guard and an eagle pommel from its scabbard at the emperor's side. A single torch on the wall, ravens visible through a cleft in the rock behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 009 · `story/artefakt_glocken_rungholt.jpg` · 21:9
Verwendung: Glocke von Rungholt – gefunden in Rungholt

```
low tide, viewpoint: at eye level on the mudflats, a few steps from a group of drowned undead who haul a large bronze church bell out of the silt on ropes. The bell is crusted with barnacles and seaweed, mud runs from it; faint ghostly faces swirl around its mouth like smoke. Broken church walls in the background, a low stormy sky, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 010 · `story/artefakt_svantevit_horn.jpg` · 21:9
Verwendung: Trinkhorn des Svantevit – gefunden in Kap Arkona

```
viewpoint: on the edge of a white chalk cliff high above the sea, looking along the cliff toward the ruins of a wooden temple wall. In the foreground a skeletal hand holds up an ornate drinking horn with silver bands, freshly dug out of the chalk. Behind, among the ruins, a toppled wooden statue of a four-headed god lies in the grass. Sea and sky to the right, gulls, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 011 · `story/artefakt_schlangenkrone.jpg` · 21:9
Verwendung: Krone des Schlangenkönigs – gefunden in Spreewald

```
viewpoint: very close, at water level on the bank of a narrow channel in an alder swamp. A skeletal hand holds a tiny golden crown, no bigger than a finger ring, up into a thin ray of light. Below in the black water, dead serpents drift; on a root in the background a giant serpent without a crown rears its head. Reeds and mist, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 012 · `story/artefakt_lehniner_weissagung.jpg` · 21:9
Verwendung: Lehniner Weissagung – gefunden in Kloster Lehnin

```
candlelight, viewpoint: in a monastery scriptorium at a writing desk, looking over the shoulder of the crowned lich. He unrolls a long prophecy scroll with a broken wax seal; behind it a hole in the brick wall where the scroll was hidden, loose bricks on the floor. Dead monks slumped over their desks in the background, a gothic window with moonlight, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 013 · `story/artefakt_merseburger_sprueche.jpg` · 21:9
Verwendung: Merseburger Zaubersprüche – gefunden in Merseburg

```
viewpoint: at a library table in a cathedral library, looking down onto an open manuscript. On the left page dense script in two short paragraphs, rendered only as unreadable fine wavy lines; beside the book a broken skeleton arm lies on the table, its bones knitting together again with thin glowing threads. Bookshelves with chained books in the background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 014 · `story/artefakt_reliquienkasten.jpg` · 21:9
Verwendung: Reliquienkasten der Ottonen – gefunden in Quedlinburg

```
viewpoint: in a dim treasury chamber, standing in front of an open iron-bound chest. A small house-shaped reliquary shrine of gold, set with gems and enamel, stands on a stone ledge; its lid is open and a skeletal hand takes out a small yellowed bone wrapped in silk. Other reliquaries, a crozier and a jewelled cross on shelves in the background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 015 · `story/artefakt_zwergenhammer.jpg` · 21:9
Verwendung: Zwergenhammer – gefunden in Zwergenlöcher am Iberg

```
viewpoint: deep inside a limestone cave with dripstones, standing at the entrance of a small rock chamber. In the chamber an ancient cold forge with a stone anvil; on the anvil lies a heavy short hammer with runes on its head. Skeleton miners with lamps hold back in awe; the crowned lich reaches for the hammer from the right. Stalactites hang from the ceiling, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 016 · `story/artefakt_jagdhorn.jpg` · 21:9
Verwendung: Horn der Wilden Jagd – gefunden in Hackelbergs Grab

```
stormy night, viewpoint: in a dark beech forest at eye level, looking toward a moss-covered grave slab under an old oak. The crowned lich stands beside the grave and raises a large hunting horn to his skull. Above the treetops spectral riders, horses and hounds of the Wild Hunt race through the clouds toward him, drawn in fine light lines, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 017 · `story/artefakt_codex_corvey.jpg` · 21:9
Verwendung: Codex von Corvey – gefunden in Kloster Corvey

```
viewpoint: in a vaulted monastery library, standing between tall book presses with chained books. In the centre a heavy codex with metal corners lies open on a lectern; its pages show only diagrams of army formations drawn as fine lines, no letters. The crowned lich reads it; skeleton commanders stand in a row behind him like pupils. Light falls through a round-arched window, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 018 · `story/artefakt_huenenknochen.jpg` · 21:9
Verwendung: Hünenknochen – gefunden in Sieben Steinhäuser

```
viewpoint: next to a megalithic tomb in a pine forest, at eye level. Two skeletons carry a gigantic thigh bone, as long as a man is tall, out from under the lifted capstone; a third grinds splinters of it into powder in a stone mortar in the foreground. Pine trunks and granite boulders around them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 019 · `story/artefakt_herz_der_heide.jpg` · 21:9
Verwendung: Herz der Heide – gefunden in Oldendorfer Totenstatt

```
dusk, viewpoint: kneeling in purple-flowering heather between long megalithic barrows, looking at the crowned lich who holds a heart-shaped stone in his bony hands. Small sprigs of heather grow out of the stone and spread over his fingers. In the background on a barrow the pale figure of a queen with a crown of heather fades into mist, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 020 · `story/ort_undeloh.jpg` · 21:9
Verwendung: Erster Angriff auf Undeloh (Dorf, 16×16)

```
dusk, viewpoint: on a sandy track in the heather at the edge of a tiny heath village, at eye level, looking toward a small fieldstone church with a separate wooden bell tower beside it and a few thatched farmhouses. On a hill far behind the village the dark shape of a burial mound. A shepherd and his dog stand still on the track and stare at undead coming out of the heather on the right, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 021 · `story/ort_egestorf.jpg` · 21:9
Verwendung: Erster Angriff auf Egestorf (Dorf, 16×16)

```
evening, viewpoint: on a field at the edge of a heath village, at eye level, looking toward a timber-framed wooden bell tower beside a small church; a farmer pulls on the bell rope. Women with rakes run from the field toward the village; in the foreground, at the field's edge, the first undead step out of a birch thicket, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 022 · `story/ort_schneverdingen.jpg` · 21:9
Verwendung: Erster Angriff auf Schneverdingen (Dorf, 16×16)

```
late summer, viewpoint: kneeling among flowering heather at the edge of a heath village, looking toward straw beehives on a wooden rack and a few thatched farmhouses behind. A beekeeper in a veil watches a swarm of bees fleeing from a strip of withered grey heather that runs through the purple heath toward the village, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 023 · `story/ort_bispingen.jpg` · 21:9
Verwendung: Erster Angriff auf Bispingen (Dorf, 16×16)

```
grey day, viewpoint: in a field strewn with boulders at eye level, looking at a squat church built of rough fieldstones with a low tower. Peasants gather stones from the field into a cart. Between the stones in the foreground a skeletal hand pushes up from the earth, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 024 · `story/ort_hanstedt.jpg` · 21:9
Verwendung: Erster Angriff auf Hanstedt (Dorf, 16×16)

```
dusk, viewpoint: in a dark forest at the edge of a clearing, at eye level, looking toward a village with a church tower beyond the trees. Woodcutters with axes stand at a woodpile and look into the forest, where undead move between the trunks right next to the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 025 · `story/ort_salzhausen.jpg` · 21:9
Verwendung: Erster Angriff auf Salzhausen (Dorf, 16×16)

```
early evening, viewpoint: on a hillside above a small river valley, looking down onto a quiet village with a church and a few thatched farmsteads among oaks. A woman draws water at a well, unaware; on the slope in the foreground, below the viewer, undead descend through the heather toward the village, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 026 · `story/ort_tostedt.jpg` · 21:9
Verwendung: Erster Angriff auf Tostedt (Dorf, 16×16)

```
evening, viewpoint: in front of a timber-framed roadside inn at eye level. Travellers and pilgrims with staffs sit at a bench outside; the innkeeper carries a jug. On the road behind them, coming toward the inn, a column of undead with the crowned lich at its head, lit by the evening sun from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 027 · `story/ort_amelinghausen.jpg` · 21:9
Verwendung: Erster Angriff auf Amelinghausen (Dorf, 16×16)

```
dusk, viewpoint: behind a farmer with a plough and oxen in a field, at eye level, looking past him toward a small heath village by a stream. In the middle of the field an ancient burial mound that the plough furrows go around; its top has opened and undead climb out. The oxen shy, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 028 · `story/ort_soltau.jpg` · 21:9
Verwendung: Erster Angriff auf Soltau (Stadt, 16×16)

```
dusk, viewpoint: on a sandy heath track just outside a small market town, at eye level, looking toward a watermill on a small river and a church tower behind thatched roofs. A shepherd drives a flock of horned heath sheep toward the town, glancing back over his shoulder; behind him on the heath, among junipers, a line of skeletons and ghouls follows at a distance. Juniper bushes and heather in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 029 · `story/ort_munster.jpg` · 21:9
Verwendung: Erster Angriff auf Munster (Dorf, 16×16)

```
windy day, viewpoint: on a low dune of sand in an open heathland, at eye level, looking toward a small church village by a river in the distance. Sand blows across the track. In the foreground a column of undead walks through the sand toward the village, their tattered cloaks blowing in the wind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 030 · `story/ort_oldendorf.jpg` · 21:9
Verwendung: Erster Angriff auf Oldendorfer Totenstatt (mythischer Ort, 64×64)

```
dusk, viewpoint: in a valley among long stone barrows, at eye level, looking at a pale queen with a crown of heather sitting on a stone, surrounded by heath spirits. She looks toward the crowned lich, who enters from the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 031 · `story/ort_visselhoevede.jpg` · 21:9
Verwendung: Erster Angriff auf Visselhövede (Dorf, 16×16)

```
grey day, viewpoint: standing in a peat cutting at eye level, looking along the cut toward a village church in the distance. Two peat cutters with spades step back from the peat wall, where a leathery dark hand and arm stick out of the cut and grasp at the air, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 032 · `story/ort_sieben_steinhaeuser.jpg` · 21:9
Verwendung: Erster Angriff auf Sieben Steinhäuser (mythischer Ort, 16×16)

```
dusk, viewpoint: in a pine forest at eye level, looking at several megalithic tombs made of huge granite boulders. Druids in white robes stand guard; the ground between the tombs trembles and cracks, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 033 · `story/ort_ebstorf.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Ebstorf (Kloster/Kirche, 16×16)

```
viewpoint: inside a convent cloister at eye level, looking through an open door into a hall where a huge round world map painted on joined parchment hangs on the wall, drawn as fine engraved lines without readable writing. Nuns stand in front of it with candles. In the cloister walk in the foreground the shadows of approaching undead fall across the floor from the left, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 034 · `story/ort_bergen.jpg` · 21:9
Verwendung: Erster Angriff auf Bergen (Dorf, 16×16)

```
night, viewpoint: standing at the low wall of a village churchyard, looking across the graves toward a small church and a windmill behind. Grave mounds have broken open; dead villagers in shrouds sit up and climb out. The crowned lich stands among them in the middle ground, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 035 · `story/ort_fallingbostel.jpg` · 21:9
Verwendung: Erster Angriff auf Fallingbostel (Dorf, 16×16)

```
morning, viewpoint: on the bank below a small weir where a river tumbles over stones, at eye level, looking up at a watermill and a village church behind it. The mill wheel turns; the miller stands in the doorway. In the river below the weir undead wade upstream toward the mill, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 036 · `story/ort_bienenbuettel.jpg` · 21:9
Verwendung: Erster Angriff auf Bienenbüttel (Dorf, 16×16)

```
grey day, viewpoint: on a road leading to a bridge over a small river, at eye level. A salt wagon pulled by two horses has stopped on the bridge; the driver jumps off. In front of the wagon undead block the road; behind the bridge a small village with a church, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 037 · `story/ort_hermannsburg.jpg` · 21:9
Verwendung: Erster Angriff auf Hermannsburg (Dorf, 16×16)

```
morning, viewpoint: on the bank of a clear, fast heath stream at eye level, looking across a ford toward a village with a church and farmhouses. Undead wade through the ford toward the village; a boy with a fishing rod drops it and runs. Alder trees on the banks, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 038 · `story/ort_buxtehude.jpg` · 21:9
Verwendung: Erster Angriff auf Buxtehude (Dorf, 16×16)

```
rising tide at dusk, viewpoint: on a wooden quay of a small river harbour, looking along the water toward a town gate and a brick church tower. Flat-bottomed river barges lie at the quay. Undead climb up the quay wall out of the rising water right in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 039 · `story/ort_medingen.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Medingen (Kloster/Kirche, 16×16)

```
night, viewpoint: outside the wall of a brick nunnery at eye level, standing in tall grass among birches. Over the wall rise the steep roof and the small ridge turret of the convent church, warm candlelight in its tall pointed windows. Along the foot of the wall, in the foreground, skeletons crouch and press their skulls against the bricks as if listening. Nothing behind the wall is visible except roofs and windows, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 040 · `story/ort_bergedorf.jpg` · 21:9
Verwendung: Erster Angriff auf Bergedorf (Dorf, 16×16)

```
morning, viewpoint: in flat marshland with drainage ditches, at eye level, looking toward a small moated brick castle. Undead walk in a long line along the ditches toward the castle; a heron takes flight in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 041 · `story/ort_walsrode.jpg` · 21:9
Verwendung: Erster Angriff auf Kloster Walsrode (Kloster/Kirche, 16×16)

```
evening, viewpoint: on a wooden bridge over a small heath river, looking toward the gate of an old convent with a Romanesque church tower. A nun hurries across the yard toward the tower to ring the bell. On the bridge in the foreground, seen from behind, undead advance toward the gate; water and reeds below them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 042 · `story/ort_lauenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Lauenburg (Dorf, 16×16)

```
dusk, viewpoint: on the river bank below a steep slope, at eye level, looking up past the half-timbered houses of boatmen to a castle on the top of the slope. Boats lie on the shore. Undead climb from the water up the steep lanes toward the castle, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 043 · `story/ort_uelzen.jpg` · 21:9
Verwendung: Erster Angriff auf Uelzen (Stadt, 16×16)

```
grey morning, viewpoint: outside a small brick town on a meadow by a moat, at eye level, looking at a town gate in an earthen rampart with a palisade and the tall brick tower of a Gothic church behind. Merchants' carts on the road to the gate stop; a horse rears. From the heath on the left undead approach along the moat, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 044 · `story/ort_suderburg.jpg` · 21:9
Verwendung: Erster Angriff auf Suderburg (Dorf, 16×16)

```
early morning, viewpoint: on a footbridge over a narrow brook, looking toward a small fieldstone church on a rise among old oaks. Mist lies over the brook. Two undead stand in the water right below the footbridge, looking up at the church, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 045 · `story/ort_unterluess.jpg` · 21:9
Verwendung: Erster Angriff auf Unterlüß (Dorf, 16×16)

```
night, viewpoint: in a forest clearing beside a smoking charcoal kiln, at eye level. A charcoal burner with a long pole stands by the kiln; its glow lights the trunks around. Between the pines at the edge of the clearing pale undead figures step out of the darkness as if they had grown out of the wood, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 046 · `story/ort_zeven.jpg` · 21:9
Verwendung: Erster Angriff auf Zeven (Dorf, 16×16)

```
dusk, viewpoint: on a path across a moor toward a small convent with a church on higher ground, at eye level. A knight on horseback gallops along the causeway toward the convent; in the moor on both sides undead rise from the black water, closer to the convent than he is, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 047 · `story/ort_verden.jpg` · 21:9
Verwendung: Erster Angriff auf Verden (Kloster/Kirche, 16×16)

```
dawn, viewpoint: on the flat meadows by a river below a cathedral town, at eye level, looking toward the large Gothic cathedral on a low rise. Mist lies on the meadows; out of the ground in the foreground rise many old skeletons of Saxon warriors with round shields and rusted seaxes, turning toward the cathedral, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 048 · `story/ort_boizenburg.jpg` · 21:9
Verwendung: Erster Angriff auf Boizenburg (Dorf, 16×16)

```
evening, viewpoint: on a riverbank landing with a toll post, at eye level, looking upstream. A river barge drifts toward the landing without a helmsman; its deck is full of undead. Toll men on the bank step back, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 049 · `story/ort_bleckede.jpg` · 21:9
Verwendung: Erster Angriff auf Bleckede (Dorf, 16×16)

```
grey morning, viewpoint: on the bank of a wide river beside a toll post, at eye level, looking toward a small castle on the bank. A toll keeper stands at a barrier pole and holds out his hand to a crowd of undead who simply walk past him, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 050 · `story/ort_stade.jpg` · 21:9
Verwendung: Erster Angriff auf Stade (Stadt, 16×16)

```
dusk, viewpoint: on a river quay with warehouses, at eye level, looking toward the town hall and church. Toll collectors stand at the quay; undead climb out of the water past them, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 051 · `story/ort_schwarmstedt.jpg` · 21:9
Verwendung: Erster Angriff auf Schwarmstedt (Dorf, 16×16)

```
spring flood, viewpoint: at water level on a flooded meadow, looking toward a church on a small sandy rise that is an island in the flood. Villagers in boats row toward the church. Undead wade through the waist-deep water toward the rise, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 052 · `story/ort_celle.jpg` · 21:9
Verwendung: Erster Angriff auf Celle (Stadt, 32×32)

```
grey day, viewpoint: on the bank of a river opposite a moated castle, at eye level. A square stone castle with corner towers stands behind a broad water ditch, a drawbridge raised; soldiers with crossbows on the battlements. Along the river bank in the foreground undead gather among willows, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

### Story-Bilder (eingebaut 18.11.2026, 19 von 19)

Ablage: `assets/story/<Dateiname>` (JPG, **21:9 Kinoformat** (Kevin, 18.11.2026), gern 2520 × 1080 oder größer). Das Spiel zeigt die Bilder wie im Kino mit schwarzen Balken oben und unten; der Text liegt unten über dem Bildrand und dem Balken – das untere Drittel soll ruhig und dunkel sein. Fehlt ein Bild, zeigt das Spiel einen gezeichneten Platzhalter mit dem Titel. Texte und Auslöser: `story` in `data/world_data.js`. Jede Szene nennt Standpunkt und Blickwinkel; zu sehen ist nur, was von dort aus sichtbar wäre.

#### Nr. 394 · `story/intro_kalkberg.jpg` · 21:9
Verwendung: Spielstart, Bild 1: Die Lüneburger reißen 1371 die Burg auf dem Kalkberg ab  
Bildaufbau: Standpunkt: auf einem Feld vor der Stadt, Augenhöhe, Blick zum Kalkberg

```
viewpoint: standing in a field outside the town at eye level, looking toward a low white chalk hill. On top of the hill, in the middle ground, townsfolk with picks, crowbars and ropes tear down the walls and the round keep of a castle; one tower collapses in a cloud of dust. Behind the hill the roofs and brick church towers of a medieval salt town. In the shadowed foreground a deep crack runs through the white chalk ground toward the viewer, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 395 · `story/intro_huegelgrab.jpg` · 21:9
Verwendung: Spielstart, Bild 2: Das Hügelgrab am Wilseder Berg bricht auf  
Bildaufbau: Standpunkt: in der Heide, Bodenhöhe, Blick über die Heide zum Grabhügel

```
night, viewpoint: crouching in the heather at ground level, looking across an open heath. In the middle distance a round bronze-age burial mound overgrown with heather, ringed by standing stones; the large capstone on top has split, and light seeps from the crack as fine radiating engraved lines. A full moon low behind the mound, wind-bent birches, a single crow on a stone. Foreground: dark heather in shadow, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 396 · `story/intro_erwachen.jpg` · 21:9
Verwendung: Spielstart, Bild 3: Der Lich steigt aus dem Grab  
Bildaufbau: Standpunkt: sehr tief, am Rand des Grablochs, Blick schräg nach oben

```
night, viewpoint: very low at the edge of a broken grave chamber, looking slightly upward. A skeletal hand with bronze rings and a corroded bronze arm ring pushes up through earth and split stone slabs; behind it rises the skull of a crowned lich, its empty eye sockets radiating faint engraved light. Soil, roots and stones fall away. Moon and night sky above the opening, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 397 · `story/erste_ernte.jpg` · 21:9
Verwendung: Nach der ersten Eroberung  
Bildaufbau: Standpunkt: auf einer leichten Anhöhe am Dorfrand, Blick auf den Weg und die Höfe

```
dawn, viewpoint: on a slight rise at the edge of a heath village, looking down a sandy track toward thatched farmhouses. Skeletons and ghouls drag lifeless villagers by the feet along the track, out of the village and past the viewer to the left. Thin smoke rises from two roofs in the background. Withered dry heather and a dead birch in the foreground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 398 · `story/heiliges_licht.jpg` · 21:9
Verwendung: Erster Angriff auf ein Kloster oder eine Kirche  
Bildaufbau: Standpunkt: im Kreuzganghof, Augenhöhe, Blick zur Kirchenfassade

```
viewpoint: inside a monastery courtyard (cloister garth) at eye level, looking toward the church facade. A six-winged seraph hovers above the church portal; from its raised hands a beam of holy light, drawn as dense radiating engraved rays, strikes a staggering zombie in the middle of the courtyard, whose flesh crumbles into dust. Other undead recoil and shield their eyes; monks pray under the arcade on the right, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 399 · `story/sturmleitern.jpg` · 21:9
Verwendung: Erster Angriff auf eine Stadt mit Mauern  
Bildaufbau: Standpunkt: außerhalb der Stadt, hinter den Angreifern am Boden, Blick die Mauer hinauf – vom Stadtinneren ist nur sichtbar, was über die Mauer ragt

```
viewpoint: outside the town on the ground, behind the attacking undead, looking up at a tall stone town wall with crenellations and a gate tower. Skeletons climb crude ladders made of bones; one ladder topples backward. In the left foreground skeletons crank a ballista made of bones. Crossbowmen lean out between the merlons and shoot down. Of the town itself only the roofs and a church spire rising above the wall are visible, nothing of the streets behind it, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 400 · `story/hamburg_hafen.jpg` · 21:9
Verwendung: Angriff auf Hamburg  
Bildaufbau: Standpunkt: vom Wasser aus, wie aus einem kleinen Boot auf der Elbe, Blick auf Kais und Stadt

```
foggy dawn, viewpoint: at water level, as if from a small boat on the river Elbe, looking toward the quays of the medieval Hanseatic town of Hamburg. Moored cogs with high sterns along wooden quays, a wooden treadwheel harbour crane, gabled brick warehouses, and behind them the tall spires of two Gothic brick churches. Undead dripping with river weed climb out of the water onto the quays and up the hulls of the cogs; a watchman with a lantern on the quay raises the alarm, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 401 · `story/lueneburg_saline.jpg` · 21:9
Verwendung: Angriff auf Lüneburg  
Bildaufbau: Standpunkt: auf dem Kalkberg zwischen den Burgruinen, Blick hinunter auf Saline und Stadt

```
dusk, viewpoint: on top of a white chalk hill among the ruined, half-demolished walls of a castle, looking down onto a medieval town. Below lie the salt works: boiling houses with steam and smoke rising from many chimneys, brick gables and a tall Gothic church tower behind. In the foreground a column of undead winds through the ruins and down the path toward the town, seen from behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 402 · `story/magdeburg_dom.jpg` · 21:9
Verwendung: Angriff auf Magdeburg  
Bildaufbau: Standpunkt: auf dem Domplatz, Bodenhöhe, Blick nach oben zur Westfassade

```
viewpoint: on the cathedral square at ground level, looking up at the west front of a Gothic cathedral whose two towers are unfinished and surrounded by wooden scaffolding. Above the towers the sky opens in a ring of engraved rays and a six-winged seraph of fire descends. On the square a crowd of undead halts; the front ranks crumble. Clerics with raised crosses stand on the cathedral steps, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 403 · `story/rungholt_ebbe.jpg` · 21:9
Verwendung: Angriff auf Rungholt  
Bildaufbau: Standpunkt: am Rand des Watts, Augenhöhe, flacher Horizont

```
low tide, viewpoint: at the edge of wide mudflats at eye level, with a very low horizon. In the middle distance the broken walls and arched windows of a sunken church rise from the mud, with rows of old wooden piles and a fallen bell half buried in the silt. Tidal creeks wind toward the viewer; drowned dead in rags rise out of the creeks. Low stormy sky, gulls, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 404 · `story/kyffhaeuser.jpg` · 21:9
Verwendung: Angriff auf den Kyffhäuser  
Bildaufbau: Bildaufbau: Schnitt durch den Berg wie in alten Stichen – oben außen, unten innen

```
the picture shows the mountain cut open like in an old engraving: in the upper part, outside, a forested mountain summit with a castle ruin and ravens circling it; in the lower part, a cut-away hall inside the mountain where an old emperor sleeps at a stone table, his long beard grown through the table, lit by a single torch. On the right, at the cave mouth, the crowned lich and his undead enter, seen in profile, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 405 · `story/spreewald.jpg` · 21:9
Verwendung: Angriff auf den Spreewald  
Bildaufbau: Standpunkt: in einem flachen Kahn auf einem schmalen Fließ, Blick nach vorn

```
viewpoint: sitting in a flat-bottomed punt on a narrow channel in a swampy alder forest, looking ahead along the water. Alder trees and reeds on both banks, mist on the water. Ahead, on a tree root, a giant serpent with a small golden crown raises its head; to the left a water man with green skin rises from the water to the waist; pale water maidens half hidden in the reeds, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 406 · `story/brocken_sabbat.jpg` · 21:9
Verwendung: Angriff auf den Brocken  
Bildaufbau: Standpunkt: am Hang unter dem Gipfel, Blick hinauf; die Untoten im Vordergrund von hinten

```
night, viewpoint: on the slope just below a bare granite summit, looking up. On the summit witches dance around a great fire among granite boulders; others ride brooms and goats across the sky; sparks and smoke. In the foreground, climbing between the rocks toward the summit with their backs to the viewer, a column of undead led by the crowned lich, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 407 · `story/phylakterium.jpg` · 21:9
Verwendung: Der Lich fällt zum ersten Mal  
Bildaufbau: Standpunkt: im Eingang der Grabkammer, Blick in die Kammer

```
viewpoint: standing in the low entrance of a burial chamber built of stone slabs, looking inside. On a stone altar in the centre a small reliquary-like phylactery radiates engraved rays; above it dust and bones swirl together and form the half-finished figure of the lich. Bronze vessels, urns and grave goods along the walls, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 408 · `story/fackeln.jpg` · 21:9
Verwendung: Der erste Trupp der Lebenden zieht aus  
Bildaufbau: Standpunkt: auf dem Dorfanger, Augenhöhe

```
evening, viewpoint: on a village green at eye level. Peasants with torches, pitchforks and flails and a knight on horseback drive undead out of the village; in the middle a pyre burns skeletons. In the background a church tower where men haul a new bell up on a rope. Strong contrast of torchlight against the dark, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 409 · `story/buendnis.jpg` · 21:9
Verwendung: Die Lebenden schließen ein Bündnis  
Bildaufbau: Standpunkt: im Kirchenschiff, Augenhöhe, Blick zum Altar

```
viewpoint: in the nave of a Gothic church at eye level, looking toward the choir. Before the altar a bishop holds up a reliquary; in front of him a duke in armour with a lion banner and a Hanseatic merchant-mayor in a fur-trimmed robe swear an oath with raised fingers. Knights and councillors stand around them; bell ropes hang in the tower arch, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 410 · `story/ley_knoten.jpg` · 21:9
Verwendung: Das erste Pantheon fällt  
Bildaufbau: Standpunkt: hinter dem Lich auf einem Hügel, Blick über das Land

```
night, viewpoint: on a hill behind the lich, who stands in a stone circle with arms raised, seen from behind. Below, a wide landscape; from the stone circle bright lines, drawn as engraved light, run like veins across the land to distant hills, other stone circles and far church towers, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 411 · `story/finale_brocken.jpg` · 21:9
Verwendung: Ende, Bild 1: Der Lich auf dem Brocken  
Bildaufbau: Standpunkt: hinter dem Lich auf dem Gipfel, Blick über das Tiefland

```
dawn, viewpoint: on the bare granite summit just behind the lich, who is seen from behind: crown, cloak and staff. Around him extinguished fires and scattered brooms among the rocks. Below, the endless lowland spreads to a far horizon with rivers, towns and forests under a low sky, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```

#### Nr. 412 · `story/finale_schatten.jpg` · 21:9
Verwendung: Ende, Bild 2: Der lange Schatten  
Bildaufbau: Standpunkt: Vogelschau über das Tiefland

```
dusk, viewpoint: high bird's-eye view over the north German plain. A huge shadow in the shape of a crowned head and an outstretched hand falls across the land: grey withered heath, silent towns, church towers without bells. Far in the south, beyond dark mountains on the horizon, a few graves open and a pale glow rises, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern Germany around 1371, cinematic composition, the lower third of the picture darker and calm with little detail (room for subtitle text), no text
```
