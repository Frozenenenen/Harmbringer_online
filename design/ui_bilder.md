# Harmbringer – Bilder für das UI

Stand und Prompts für alle Bilder der Oberfläche. Kevin erzeugt die Bilder, Claude baut sie ein.

- **Offene Bilder stehen oben**, erledigte unten. Neue Bilder kommen in die offene Liste.
- **Ablage:** Kevin gibt die Bilder an Claude; Claude legt sie unter `assets/ui/<Dateiname>` ab, verkleinert sie und baut sie ein.
- **Format:** PNG oder JPG, so groß wie möglich. Auflösung egal, das Verhältnis zählt. Claude verkleinert.
- **Symbole:** schwarze Linien auf hellem Papier. Claude legt sie im Spiel per „Multiplizieren“ über den Papiergrund, ein freigestellter Hintergrund ist nicht nötig.
- **Texturen** (Papier): sollten sich kacheln lassen. Wenn nicht ganz, macht Claude sie nahtlos.
- **Prompts auf Englisch**, weil die meisten Bildmodelle damit am besten arbeiten. Der Stilteil ist in jedem Prompt gleich, damit alles zusammenpasst.
- Erzeugt das Programm Schrift, Signaturen oder Dürers Monogramm „AD“ mit, bitte neu erzeugen oder Claude sagen, er entfernt es.

## Stil

Vorbild Albrecht Dürer: Holzschnitt und Kupferstich um 1500, feine Kreuzschraffur, schwarz auf vergilbtem Papier, düster, Totentanz, Memento mori.

**Negativ-Prompt (für alle Bilder, falls das Programm einen hat):**

```
color, colorful, photo, 3d render, glossy, modern, anime, cartoon, text, letters, numbers, watermark, signature, monogram, logo, blurry
```

## Offen

164 Bilder. Reihenfolge = Priorität (Abschnitt 1–4 machen das UI schon spürbar schöner).

### 1 Grundlagen (Rahmen, Papier, Titel)

#### `ui/papier.jpg` · 1:1
Verwendung: Hintergrund aller Fenster und Leisten (wird gekachelt)

```
blank aged rag paper with faint fibres, foxing stains and a few tiny ink specks, seamless tileable texture, even lighting, no motif, no text, flat top-down view, like the paper of an Albrecht Dürer print from around 1500, realistic high-resolution scan
```

#### `ui/papier_dunkel.jpg` · 1:1
Verwendung: Seitenleiste und untere Leiste (dunkler Grund, gekachelt)

```
dark smoke-stained parchment, almost black-brown, scorched and worn, with faint hatching, seamless tileable texture, even lighting, no motif, no text, flat top-down view, like the paper of an Albrecht Dürer print from around 1500, realistic high-resolution scan
```

#### `ui/rahmen.png` · 1:1
Verwendung: Zierrahmen für Fenster (wird in 9 Teile zerschnitten)

```
ornamental rectangular frame border of twisted thorn branches, bones and small skulls in the four corners, completely empty plain paper in the middle, symmetric, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `ui/ecke.png` · 1:1
Verwendung: Eckzier für Panels (oben links, wird gespiegelt)

```
corner ornament: a small skull with crossed bones entwined by a dry thorn vine, filling the top-left corner only, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `ui/trenner.png` · 21:9
Verwendung: Trennlinie zwischen Abschnitten

```
long thin horizontal ornament: a femur bone with a thorn vine wound around it, ending in tiny skulls at both ends, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `titel.jpg` · 16:9
Verwendung: Ladebildschirm und Titel

```
a crowned lich in a tattered robe rises from an opened bronze-age burial mound on a heath hill at night, ravens circling, bare twisted trees, distant church tower, mist over the heather, dead lie around, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `erwachen.jpg` · 16:9
Verwendung: Fenster beim Spielstart (Erwachen)

```
inside a dark burial chamber of stone slabs, a skeletal lich opening his eyes on a stone bier, a glowing phylactery jar beside him, roots hanging from the ceiling, grave goods of bronze, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `tod_lich.jpg` · 16:9
Verwendung: Fenster, wenn der Lich fällt

```
a lich collapsing on a battlefield, his crown rolling away, his spirit drawn back as smoke towards a distant burial mound, peasants with torches and pitchforks, corpses everywhere, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `sieg_brocken.jpg` · 16:9
Verwendung: Endbildschirm (Brocken erreicht)

```
the lich standing on the bare Brocken summit at Walpurgis night, a vast army of skeletons and corpses below, witches fleeing on brooms, storm clouds, lightning, granite boulders, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 2 Ressourcen-Symbole

#### `icons/res_leichen.png` · 1:1
Verwendung: Ressource Leichen (Leiste unten, Kosten)

```
a shrouded human corpse lying on a wooden plank, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/res_knochen.png` · 1:1
Verwendung: Ressource Knochen (Leiste unten, Kosten)

```
a pile of bones with a skull on top, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/res_seelen.png` · 1:1
Verwendung: Ressource Seelen (Leiste unten, Kosten)

```
a small wailing ghost-like soul flame rising from a clay urn, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/res_wissen.png` · 1:1
Verwendung: Ressource Wissen (Leiste unten, Kosten)

```
an old open grimoire with a skull resting on it, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/res_kommando.png` · 1:1
Verwendung: Ressource Kommando (Leiste unten, Kosten)

```
a tattered black war banner on a bone pole, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 3 Aktions-Symbole (Seitenleiste, Kampf)

#### `icons/act_huegelgrab.png` · 1:1
Verwendung: Hügelgrab

```
a bronze-age burial mound with a stone entrance, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_rekrutieren.png` · 1:1
Verwendung: Rekrutieren

```
a skeletal hand rising out of a grave, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_bauen.png` · 1:1
Verwendung: Bauen

```
a hammer and chisel crossed over a stone block with a skull carving, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_rasten.png` · 1:1
Verwendung: Rasten

```
a crescent moon above a smouldering campfire, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_inventar.png` · 1:1
Verwendung: Inventar

```
an iron-bound wooden chest with a crown and a horn inside, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_menue.png` · 1:1
Verwendung: Menü

```
a closed book with clasps and a ribbon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_los.png` · 1:1
Verwendung: Los (Befehle ausführen)

```
a skeleton drummer beating a war drum, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_chronik.png` · 1:1
Verwendung: Chronik

```
a rolled parchment scroll with a quill, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_bedrohung.png` · 1:1
Verwendung: Bedrohung

```
a burning torch and a pitchfork crossed, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_ley_sprung.png` · 1:1
Verwendung: Ley-Sprung

```
a standing stone with a spiral carving and a crackling beam of light, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_portal.png` · 1:1
Verwendung: Portal errichten

```
a stone arch of two menhirs and a lintel with a swirling void inside, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_zug_beenden.png` · 1:1
Verwendung: Zug beenden

```
an hourglass with the sand run out, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_rueckzug.png` · 1:1
Verwendung: Rückzug

```
a lowered torn banner and footprints leading away, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_abziehen.png` · 1:1
Verwendung: Abziehen

```
a closed city gate seen from outside, the army turning away, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_kanten.png` · 1:1
Verwendung: Feldkanten

```
a small hexagonal tiling drawn as engraved lines, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_token.png` · 1:1
Verwendung: Token-Modus

```
a round wax seal with a skull imprint, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/act_hilfe.png` · 1:1
Verwendung: Hilfe

```
an open book with a pointing hand (manicule), single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 4 Werte- und Zustands-Symbole (Einheitenkarte)

#### `icons/stat_leben.png` · 1:1
Verwendung: Lebenspunkte

```
an anatomical human heart, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_schaden.png` · 1:1
Verwendung: Schaden

```
a notched broadsword, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_nahkampf.png` · 1:1
Verwendung: Nahkampf

```
a clenched armoured gauntlet, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_reichweite.png` · 1:1
Verwendung: Reichweite

```
a crossbow bolt and a longbow, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_bewegung.png` · 1:1
Verwendung: Bewegung

```
bare skeletal feet walking, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_initiative.png` · 1:1
Verwendung: Initiative

```
a lightning bolt striking a skull, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_ruestung.png` · 1:1
Verwendung: Rüstung

```
a dented heater shield, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_magieresistenz.png` · 1:1
Verwendung: Magieresistenz

```
a pentagram drawn in a circle, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_seelenschild.png` · 1:1
Verwendung: Seelenschild

```
a shield made of swirling ghostly faces, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_energie.png` · 1:1
Verwendung: Energie

```
a burning candle stub, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_auge.png` · 1:1
Verwendung: Sicht

```
a single wide-open human eye, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_ohr.png` · 1:1
Verwendung: Gehör

```
a human ear, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_nase.png` · 1:1
Verwendung: Geruch

```
a human nose sniffing, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_ahnungslos.png` · 1:1
Verwendung: Wache ahnungslos

```
a sleeping guard's closed eye with a small Z-like curl of breath, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_misstrauisch.png` · 1:1
Verwendung: Wache misstrauisch

```
a half-open suspicious eye under a raised eyebrow, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_alarmiert.png` · 1:1
Verwendung: Wache alarmiert

```
a ringing church bell, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_fuehrerlos.png` · 1:1
Verwendung: Führerlos

```
a broken commander's staff, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/stat_ueberraschung.png` · 1:1
Verwendung: Überraschungstreffer

```
a dagger striking from a shadow, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 5 Tageszeiten (Uhr unten rechts)

#### `icons/zeit_nacht.png` · 1:1
Verwendung: Tageszeit Nacht

```
round medallion: a full moon with a skull face among stars, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/zeit_morgen.png` · 1:1
Verwendung: Tageszeit Morgen

```
round medallion: a pale sun rising through mist over heather, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/zeit_tag.png` · 1:1
Verwendung: Tageszeit Tag

```
round medallion: a blazing sun with a stern face and long rays, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `icons/zeit_abend.png` · 1:1
Verwendung: Tageszeit Abend

```
round medallion: a setting sun behind a gallows on a hill, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 6 Fenster-Banner (Kopfbild der Fenster)

#### `banner/rekrutieren.jpg` · 21:9
Verwendung: Fenster Rekrutieren

```
wide panoramic scene: necromancer raising skeletons and corpses from open graves in a churchyard, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/bauen.jpg` · 21:9
Verwendung: Fenster Bauen

```
wide panoramic scene: skeleton workers building a bone-and-stone hall inside a huge burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/chronik.jpg` · 21:9
Verwendung: Fenster Chronik

```
wide panoramic scene: an old monk-chronicler writing by candlelight, a skeleton dictating over his shoulder, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/inventar.jpg` · 21:9
Verwendung: Fenster Inventar

```
wide panoramic scene: a treasure vault with a crown, a sword, a horn and relics among bones, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/rasten.jpg` · 21:9
Verwendung: Fenster Rasten

```
wide panoramic scene: an undead army camped around fires under a crescent moon on a heath, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/ley.jpg` · 21:9
Verwendung: Fenster Ley-Sprung

```
wide panoramic scene: standing stones linked by glowing lines across a dark landscape, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/spielstaende.jpg` · 21:9
Verwendung: Fenster Spielstände

```
wide panoramic scene: a monk's desk with stacked books and an hourglass, a skull as bookend, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/sieg.jpg` · 21:9
Verwendung: Fenster Kampf gewonnen

```
wide panoramic scene: skeletons raising tattered banners over a burning village, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/niederlage.jpg` · 21:9
Verwendung: Fenster Kampf verloren

```
wide panoramic scene: a field of shattered skeletons, crows feeding, a priest blessing the ground, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/rueckzug.jpg` · 21:9
Verwendung: Fenster Rückzug

```
wide panoramic scene: an undead column retreating through a forest in the rain, stragglers falling behind, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `banner/belagerung.jpg` · 21:9
Verwendung: Fenster Ummauerte Stadt / Abziehen

```
wide panoramic scene: a fortified Hanseatic town wall with towers and a gate under siege by giants and a bone ballista, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 7 Erzähler

#### `portraits/chronist.png` · 1:1
Verwendung: Erzähler-Leiste (Chronist)

```
bust portrait of an old gaunt monk-chronicler with quill and spectacles, hollow eyes, cowl, in a round frame, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `portraits/hinweis.png` · 1:1
Verwendung: Hinweis-Symbol der Erzähler-Leiste

```
an oil lamp with a small flame, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 8 Fraktionswappen

#### `wappen/untote.png` · 1:1
Verwendung: Fraktion Untote (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a crowned skull over two crossed femurs, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/hanse.png` · 1:1
Verwendung: Fraktion Hanse (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a Hanseatic cog ship with a single sail, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/welfen.png` · 1:1
Verwendung: Fraktion Welfen (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a leaping lion, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/askanier.png` · 1:1
Verwendung: Fraktion Askanier (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a bear on a crenellated wall, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/klerus.png` · 1:1
Verwendung: Fraktion Klerus (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a crozier and a crucifix crossed, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/hexen.png` · 1:1
Verwendung: Fraktion Hexen und Haine (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a broom, a black cat and a sickle moon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/grafen.png` · 1:1
Verwendung: Fraktion Grafen (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a castle tower with a count's coronet, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/mecklenburg.png` · 1:1
Verwendung: Fraktion Mecklenburg (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a crowned bull's head, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/wettiner.png` · 1:1
Verwendung: Fraktion Wettiner (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a lion standing on a striped field, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/wodan.png` · 1:1
Verwendung: Fraktion Wodan-Kult (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: two ravens and an eight-legged horse, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/spreewald.png` · 1:1
Verwendung: Fraktion Spreewald (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a serpent with a small crown among reeds, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/wattenmeer.png` · 1:1
Verwendung: Fraktion Wattenmeer (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a sunken church bell among waves, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `wappen/heidegeister.png` · 1:1
Verwendung: Fraktion Heidegeister (Bedrohung, Ortsinfo, Minimap)

```
heraldic shield, coat of arms: a will-o'-the-wisp above heather and a juniper bush, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 9 Pantheon-Siegel

#### `pantheon/heide.png` · 1:1
Verwendung: Pantheon Heide-Pantheon

```
round wax seal medallion showing a megalithic dolmen under a heath moon, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `pantheon/wodan.png` · 1:1
Verwendung: Pantheon Wilde Jagd

```
round wax seal medallion showing a horned huntsman leading hounds across the sky, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `pantheon/spreewald.png` · 1:1
Verwendung: Pantheon Wendische Geister

```
round wax seal medallion showing a noon-witch with a sickle in a wheat field, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `pantheon/wattenmeer.png` · 1:1
Verwendung: Pantheon Versunkene Städte

```
round wax seal medallion showing the drowned town of Rungholt under the waves, a church spire, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `pantheon/harz.png` · 1:1
Verwendung: Pantheon Walpurgis-Zirkel

```
round wax seal medallion showing witches dancing around a fire on a mountain top, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 10 Gebäude des Hügelgrabs (Baumenü)

#### `gebaeude/phylactery.jpg` · 4:3
Verwendung: Gebäude Phylakterium

```
a glowing reliquary jar on an altar of skulls in a burial chamber, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/boneWorkshop.jpg` · 4:3
Verwendung: Gebäude Knochenwerkstatt

```
skeletons sawing and assembling bones at workbenches, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/corpsePit.jpg` · 4:3
Verwendung: Gebäude Leichengrube

```
a deep pit full of corpses, ghouls climbing out, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/soulKennel.jpg` · 4:3
Verwendung: Gebäude Seelenzwinger

```
iron cages holding wailing ghosts, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/deadHall.jpg` · 4:3
Verwendung: Gebäude Totenhalle

```
a long vaulted crypt hall lined with standing skeleton warriors, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/knowledgeAltar.jpg` · 4:3
Verwendung: Gebäude Wissensaltar

```
a stone altar piled with stolen books, candles and an open skull, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/boneForge.jpg` · 4:3
Verwendung: Gebäude Knochenschmiede

```
a forge where bones are hammered into weapons, sparks and smoke, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `gebaeude/heathAltar.jpg` · 4:3
Verwendung: Gebäude Heidealtar

```
a heather-covered megalith altar with offerings and a spirit rising, underground inside a burial mound, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 11 Artefakte (Inventar)

#### `artefakte/reichsschwert.png` · 1:1
Verwendung: Artefakt Reichsschwert Barbarossas

```
an imperial longsword with a cross guard and an eagle pommel, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/glocken_rungholt.png` · 1:1
Verwendung: Artefakt Glocke von Rungholt

```
a barnacle-covered bronze church bell, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/svantevit_horn.png` · 1:1
Verwendung: Artefakt Trinkhorn des Svantevit

```
an ornate drinking horn with silver bands, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/schlangenkrone.png` · 1:1
Verwendung: Artefakt Krone des Schlangenkönigs

```
a tiny golden crown with a serpent coiled through it, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/lehniner_weissagung.png` · 1:1
Verwendung: Artefakt Lehniner Weissagung

```
a sealed prophecy scroll with a broken wax seal, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/merseburger_sprueche.png` · 1:1
Verwendung: Artefakt Merseburger Zaubersprüche

```
an old manuscript leaf with runes and knotwork, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/reliquienkasten.png` · 1:1
Verwendung: Artefakt Reliquienkasten der Ottonen

```
a small house-shaped reliquary shrine with gems, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/zwergenhammer.png` · 1:1
Verwendung: Artefakt Zwergenhammer

```
a heavy short hammer with runes on the head, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/jagdhorn.png` · 1:1
Verwendung: Artefakt Horn der Wilden Jagd

```
a large hunting horn with a strap, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/codex_corvey.png` · 1:1
Verwendung: Artefakt Codex von Corvey

```
a heavy bound codex with metal corners, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/huenenknochen.png` · 1:1
Verwendung: Artefakt Hünenknochen

```
a gigantic thigh bone, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `artefakte/herz_der_heide.png` · 1:1
Verwendung: Artefakt Herz der Heide

```
a heart-shaped stone with heather growing from it, single isolated motif centered with a wide empty margin, plain off-white paper background, no frame, no text, no letters, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

### 12 Einheitenbilder (Rekrutieren, Einheitenkarte, Initiativeleiste)

#### `einheiten/lich.jpg` · 3:4
Verwendung: Lich

```
half-length portrait of a crowned lich in a tattered purple robe with a staff topped by a glowing green stone, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/ghul.jpg` · 3:4
Verwendung: Ghul

```
half-length portrait of a hunched emaciated ghoul with long claws, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/skelett.jpg` · 3:4
Verwendung: Skelett

```
half-length portrait of a skeleton warrior with a rusty sword and round shield, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/bogner.jpg` · 3:4
Verwendung: Skelett-Bogenschütze

```
half-length portrait of a skeleton archer drawing a longbow, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/leichenhund.jpg` · 3:4
Verwendung: Leichenhund

```
half-length portrait of a rotting dead hound with exposed ribs, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/zombie.jpg` · 3:4
Verwendung: Zombie

```
half-length portrait of a shambling rotting peasant corpse, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/schleuderer.jpg` · 3:4
Verwendung: Knochenschleuderer

```
half-length portrait of a skeleton with a sling and a pouch of skull stones, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/geist.jpg` · 3:4
Verwendung: Geist

```
half-length portrait of a translucent wailing ghost in a burial shroud, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/knochenschuetze.jpg` · 3:4
Verwendung: Knochenschütze

```
half-length portrait of a skeleton crossbowman with a bone crossbow, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/moorleiche.jpg` · 3:4
Verwendung: Moorleiche

```
half-length portrait of a leathery bog body with a rope around its neck, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/todesritter.jpg` · 3:4
Verwendung: Todesritter

```
half-length portrait of a skeletal knight in black plate armour on a skeletal horse, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/totenlicht.jpg` · 3:4
Verwendung: Totenlicht

```
half-length portrait of a floating skull with a candle flame inside, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/gefallene_schwester.jpg` · 3:4
Verwendung: Gefallene Schwester

```
half-length portrait of a dead nun with a torn veil and a rosary of finger bones, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/grabdruidin.jpg` · 3:4
Verwendung: Grabdruidin

```
half-length portrait of an undead druid woman with a sickle and mistletoe, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/nekromant.jpg` · 3:4
Verwendung: Nekromant

```
half-length portrait of a gaunt necromancer in a hooded robe with a skull lantern, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/knochenballiste.jpg` · 3:4
Verwendung: Balliste

```
half-length portrait of a siege ballista built from bones and sinew, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/fleischriese.jpg` · 3:4
Verwendung: Fleischriese

```
half-length portrait of a huge stitched giant of many corpses, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/knochendrache.jpg` · 3:4
Verwendung: Knochendrache

```
half-length portrait of a dragon skeleton with tattered wings, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/wasserleiche.jpg` · 3:4
Verwendung: Wasserleiche

```
half-length portrait of a bloated drowned corpse dripping water, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/reiterfuerst.jpg` · 3:4
Verwendung: Bronzezeitlicher Reiterfürst

```
half-length portrait of a skeletal bronze-age chieftain on horseback with a bronze sword, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/huenenkoenig.jpg` · 3:4
Verwendung: Hünenkönig

```
half-length portrait of a giant skeletal king of the megalith builders with a stone club, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/widukind.jpg` · 3:4
Verwendung: Widukinds Schatten

```
half-length portrait of the ghost of a Saxon duke with a winged helmet and a seax, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/ratsherr.jpg` · 3:4
Verwendung: Ratsherr von Rungholt

```
half-length portrait of a drowned town councillor in rich robes covered in seaweed, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/totenjaeger.jpg` · 3:4
Verwendung: Totenjäger

```
half-length portrait of an undead huntsman with a spear and a hound, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/bauer.jpg` · 3:4
Verwendung: Bauer

```
half-length portrait of a medieval peasant with a pitchfork, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/stadtwache.jpg` · 3:4
Verwendung: Stadtwache

```
half-length portrait of a town guard with a halberd and a kettle hat, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/armbrust.jpg` · 3:4
Verwendung: Lüneburger Armbrustschütze

```
half-length portrait of a town crossbowman with a pavise shield, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/ritter.jpg` · 3:4
Verwendung: Ritter

```
half-length portrait of a mounted knight in plate armour with a lance, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/balliste.jpg` · 3:4
Verwendung: Stadtballiste

```
half-length portrait of a town siege ballista on a wall, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/moench.jpg` · 3:4
Verwendung: Mönch

```
half-length portrait of a tonsured monk with a lantern, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/priester.jpg` · 3:4
Verwendung: Priester

```
half-length portrait of a priest raising a crucifix, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/kleriker.jpg` · 3:4
Verwendung: Kleriker

```
half-length portrait of a cleric with a censer and holy water, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/heideschwester.jpg` · 3:4
Verwendung: Heideschwester

```
half-length portrait of a nun herb-healer of the heath, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/hexe.jpg` · 3:4
Verwendung: Hexe

```
half-length portrait of a witch with a staff and herbs, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/brockenhexe.jpg` · 3:4
Verwendung: Hexenkönigin vom Brocken

```
half-length portrait of a witch queen on the Brocken with a crown of antlers, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/irrlicht.jpg` · 3:4
Verwendung: Irrlicht

```
half-length portrait of a will-o'-the-wisp over a bog, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/moorgeist.jpg` · 3:4
Verwendung: Moorgeist

```
half-length portrait of a bog spirit rising from black water, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/rattenfaenger.jpg` · 3:4
Verwendung: Rattenfänger

```
half-length portrait of the pied piper with a flute and rats, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/druide.jpg` · 3:4
Verwendung: Druide

```
half-length portrait of an old druid with a staff and oak leaves, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/druidin.jpg` · 3:4
Verwendung: Hügelgrab-Druidin

```
half-length portrait of a druidess guarding a burial mound, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/schwarzer_hund.jpg` · 3:4
Verwendung: Schwarzer Hund

```
half-length portrait of a huge black hound with burning eyes, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/wode.jpg` · 3:4
Verwendung: Der Wode

```
half-length portrait of the one-eyed god Wode with a wide hat and a spear, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/zwergenkoenig.jpg` · 3:4
Verwendung: Hügelgrab-Zwergenkönig

```
half-length portrait of a dwarf king with a hammer under a burial mound, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/heidekoenigin.jpg` · 3:4
Verwendung: Die Heidekönigin

```
half-length portrait of a pale queen of the heath crowned with heather, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/sachsenkrieger.jpg` · 3:4
Verwendung: Sachsenkrieger

```
half-length portrait of an old Saxon warrior with a round shield and seax, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/wodansrabe.jpg` · 3:4
Verwendung: Wodansrabe

```
half-length portrait of a huge raven with spread wings, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/wilder_jaeger.jpg` · 3:4
Verwendung: Wilder Jäger

```
half-length portrait of a spectral huntsman on a horse in the storm, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/hackelberg.jpg` · 3:4
Verwendung: Hackelberg

```
half-length portrait of the cursed huntsman Hackelberg with hounds, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/lutki.jpg` · 3:4
Verwendung: Lutki

```
half-length portrait of tiny Wendish house spirits, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/wassermann.jpg` · 3:4
Verwendung: Wassermann

```
half-length portrait of a water man with green skin and a net, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/rusalka.jpg` · 3:4
Verwendung: Rusalka

```
half-length portrait of a pale water maiden with long wet hair, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/mittagsfrau.jpg` · 3:4
Verwendung: Mittagsfrau

```
half-length portrait of the noon witch with a sickle in a white dress, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/schlangenkoenig.jpg` · 3:4
Verwendung: Schlangenkönig

```
half-length portrait of a giant crowned serpent, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/ertrunkener.jpg` · 3:4
Verwendung: Ertrunkener

```
half-length portrait of a drowned sailor, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/wattjungfrau.jpg` · 3:4
Verwendung: Wattjungfrau

```
half-length portrait of a ghostly maiden of the mudflats, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/klabautermann.jpg` · 3:4
Verwendung: Klabautermann

```
half-length portrait of a small ship goblin with a mallet and pipe, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/blanker_hans.jpg` · 3:4
Verwendung: Blanker Hans

```
half-length portrait of the storm flood as a giant figure of waves with a white mane, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/ophan.jpg` · 3:4
Verwendung: Ophan

```
half-length portrait of a wheel within a wheel covered with eyes, wreathed in fire, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/cherub.jpg` · 3:4
Verwendung: Cherub

```
half-length portrait of a four-faced winged cherub with a flaming sword, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

#### `einheiten/seraph.jpg` · 3:4
Verwendung: Seraph

```
half-length portrait of a six-winged seraph covered in flames, dark background, in the style of Albrecht Dürer, early 16th-century German Renaissance woodcut and copper engraving, dense fine cross-hatching and parallel-line shading, black ink on aged yellowed laid paper, high contrast, grim, macabre, memento mori, Danse Macabre mood, northern German heathland around 1371
```

## Erledigt

_Noch keine._
