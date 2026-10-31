# Harmbringer – One-Shot-Auftrag

Baue in einem Durchgang einen spielbaren Prototyp des Strategiespiels „Harmbringer“ als Browser-Spiel. Lies diesen Auftrag vollständig, bevor du Code schreibst. Halte dich an die Prioritäten in Abschnitt 12: Was als MUSS markiert ist, muss funktionieren; SOLL und KANN nur, wenn das MUSS steht.

---

## 1. Lieferumfang und Technik

- Liefere **genau eine Datei `index.html`**. Sie liegt neben dem Ordner `data/` mit zwei mitgelieferten Dateien:
  - `data/heightmap.js` setzt `window.HARMBRINGER_HEIGHTMAP` (Höhendaten, ca. 2 MB). **Nicht inline einbetten, nur per `<script src>` laden.**
  - `data/world_data.js` setzt `window.HARMBRINGER_DATA` (alle Spielwerte). Diese Datei liegt dir vor.
- Lade beide Dateien mit klassischen `<script src="data/...">`-Tags **vor** dem Spiel-Modul.
- Three.js **r160** per Import-Map, keine anderen Bibliotheken, kein Build-Schritt:
  ```html
  <script type="importmap">
  { "imports": {
      "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
      "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/" } }
  </script>
  ```
- Das Spiel muss **per Doppelklick (file://)** und über einen einfachen Webserver laufen. Deshalb: kein `fetch` auf lokale Dateien, kein Lesen von Bildpixeln über Canvas.
- Ziel: 60 FPS auf einem normalen Desktop-PC. Bedienung mit Maus und Tastatur.
- Spieltexte auf **Deutsch**, Code-Kommentare auf **Englisch** und ausführlich.
- Alle Zahlenwerte kommen aus `HARMBRINGER_DATA`. Keine Spielwerte doppelt im Code festschreiben.

---

## 2. Das Spiel in Kürze

Mai 1371. In einem bronzezeitlichen Hügelgrab am Wilseder Berg in der Lüneburger Heide erwacht ein Lich. Von dort zieht er mit einer kleinen Untotenarmee über eine echte Höhenkarte Norddeutschlands, erobert Dörfer, Klöster, Städte und mythische Orte und rekrutiert aus den Leichen neue Truppen. Ziel ist der Brocken, der mächtigste Ley-Knoten Norddeutschlands.

**Spielschleife:**

1. **Weltkarte:** Die Armee steht an einem Ort. Der Spieler wählt ein Ziel, die Armee reist, Tage vergehen.
2. **Kampf:** Am Ziel beginnt ein rundenbasierter Hex-Kampf auf genau dem Gelände dieser Stelle der Welt.
3. **Beute:** Sieg bringt Leichen, Knochen, Seelen oder Wissen und erobert den Ort.
4. **Hügelgrab:** Dort rekrutiert der Lich neue Untote und seine Truppen heilen.
5. Wiederholen, bis der Brocken fällt.

Der Lich ist unsterblich: Fällt er, verliert der Spieler seine Armee und der Lich erwacht wieder im Hügelgrab.

---

## 3. Daten

### 3.1 Höhenkarte

```js
window.HARMBRINGER_HEIGHTMAP = { width: 1704, height: 920, seaLevel: 29, data: "<base64>" };
// Decode once: const gray = Uint8Array.from(atob(HM.data), c => c.charCodeAt(0));
// gray[r * width + q] is the gray value of tile (q, r). Row 0 is the north edge.
```

- 1 Pixel = 1 Tile. Tile (q, r) = Pixel (x = q, y = r).
- Meter über Meer: `meters = gray * map.metersPerGray + map.metersAtGrayZero` (−58 bis 450 m, darüber gekappt).
- Spielhöhe in Welteinheiten (bewusst gedämpft, damit Berge nicht absurd wirken):
  ```js
  const s = gray - map.seaLevelGray;
  const y = Math.sign(s) * Math.sqrt(Math.abs(s)) * hex.heightPerStep;  // top surface of the tile
  ```
  Unterwasser-Tiles behalten ihre negative Höhe. Darüber liegt eine Wasserebene bei `hex.waterLevel`.
- **Höhenstufe für Spielregeln:** `level = Math.round(y)`.

### 3.2 Spieldaten

`HARMBRINGER_DATA` enthält `map`, `hex`, `streaming`, `camera`, `floorTypes`, `floorRules`, `powerDefense`, `corpseQuality`, `units`, `factions`, `nodes`, `economy`, `threat`. Die Kommentare in der Datei erklären jeden Wert. Nutze die Schlüssel exakt so.

### 3.3 Vorberechnung beim Start

Berechne beim Laden **einmal für alle 1.567.680 Tiles** Höhe und Bodentyp in Typed Arrays (`Float32Array` für Höhe, `Uint8Array` für den Index des Bodentyps). Zeige währenddessen eine Ladeanzeige. Danach greift alles über `tileIndex = r * width + q` darauf zu.

---

## 4. Hex-System (verbindlich)

Flat-Top-Sechsecke im **Odd-Q-Offset**: Ungerade Spalten sind um eine halbe Zeile nach Süden (+Z) verschoben. Norden ist −Z, Osten +X. Richtungen: `0=N, 1=NE, 2=SE, 3=S, 4=SW, 5=NW`, im Uhrzeigersinn von oben gesehen. Kanten eines Tiles nutzen dieselben Indizes.

Übernimm diesen getesteten Referenzcode unverändert (er hat einen Test über Rundwege, Nachbarn und Linien bestanden):

```js
const R = HARMBRINGER_DATA.hex.circumradius;  // center to corner
const INRADIUS = R * Math.sqrt(3) / 2;        // center to edge midpoint
const COL_SPACING = 1.5 * R;
const ROW_SPACING = 2 * INRADIUS;

// Direction order: 0=N, 1=NE, 2=SE, 3=S, 4=SW, 5=NW (N = -Z, clockwise seen from above)
const OFFSETS_EVEN_Q = [[0,-1],[1,-1],[1,0],[0,1],[-1,0],[-1,-1]];
const OFFSETS_ODD_Q  = [[0,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]];
const opposite = d => (d + 3) % 6;

function neighbor(q, r, d) {
  const o = (q & 1) ? OFFSETS_ODD_Q[d] : OFFSETS_EVEN_Q[d];
  return [q + o[0], r + o[1]];
}
// Tile center on the XZ plane (y comes from the heightmap).
function hexToWorld(q, r) {
  return { x: COL_SPACING * q, z: ROW_SPACING * r + ((q & 1) ? INRADIUS : 0) };
}
function offsetToCube(q, r) { const x = q, z = r - (q - (q & 1)) / 2; return [x, -x - z, z]; }
function cubeToOffset(x, y, z) { return [x, z + (x - (x & 1)) / 2]; }
function cubeRound(fx, fy, fz) {
  let rx = Math.round(fx), ry = Math.round(fy), rz = Math.round(fz);
  const dx = Math.abs(rx - fx), dy = Math.abs(ry - fy), dz = Math.abs(rz - fz);
  if (dx > dy && dx > dz) rx = -ry - rz; else if (dy > dz) ry = -rx - rz; else rz = -rx - ry;
  return [rx, ry, rz];
}
function worldToHex(x, z) {
  const fq = (2 / 3 * x) / R;
  const fr = (-1 / 3 * x + Math.sqrt(3) / 3 * z) / R;   // axial r
  const [cx, cy, cz] = cubeRound(fq, -fq - fr, fr);
  return cubeToOffset(cx, cy, cz);
}
function hexDistance(q1, r1, q2, r2) {
  const a = offsetToCube(q1, r1), b = offsetToCube(q2, r2);
  return Math.max(Math.abs(a[0]-b[0]), Math.abs(a[1]-b[1]), Math.abs(a[2]-b[2]));
}
// Tiles on the straight line between two tiles, both ends included.
function hexLine(q1, r1, q2, r2) {
  const n = hexDistance(q1, r1, q2, r2);
  const a = offsetToCube(q1, r1), b = offsetToCube(q2, r2), out = [];
  for (let i = 0; i <= n; i++) {
    const t = n === 0 ? 0 : i / n;
    const c = cubeRound(a[0] + (b[0]-a[0])*t + 1e-6, a[1] + (b[1]-a[1])*t + 1e-6, a[2] + (b[2]-a[2])*t - 2e-6);
    out.push(cubeToOffset(c[0], c[1], c[2]));
  }
  return out;
}
// Direction index from tile A to an adjacent tile B, or -1.
function directionTo(q1, r1, q2, r2) {
  for (let d = 0; d < 6; d++) { const [nq, nr] = neighbor(q1, r1, d); if (nq === q2 && nr === r2) return d; }
  return -1;
}
// Unit vector on XZ from a tile center toward edge d.
function edgeDirection(d) { const a = d * Math.PI / 3; return { x: Math.sin(a), z: -Math.cos(a) }; }
```

**Tile-Geometrie:** `new THREE.CylinderGeometry(R * 0.98, R * 0.98, hex.tileDepth, 6)` und danach `geometry.rotateY(Math.PI / 6)`, damit die Ecken auf ±X liegen (Flat-Top). Der kleine Spalt (0,98) macht die Hex-Struktur sichtbar. Die Oberkante liegt auf Höhe `y`, also Mittelpunkt bei `y - tileDepth / 2`.

**Kanten-Platzhalter:** Mittelpunkt der Kante `d` = Tile-Mitte + `edgeDirection(d) * INRADIUS`. Ein Objekt, das an der Kante entlang liegt, bekommt `rotation.y = -d * Math.PI / 3`, wenn seine Längsachse ursprünglich auf X liegt.

---

## 5. Welt

### 5.1 Bodentypen (Regel)

Deterministisch, damit ein Tile nach dem Neuladen gleich aussieht. Verwende exakt diese Funktionen:

```js
function hash2(q, r, seed) {
  const h = Math.sin(q * 127.1 + r * 311.7 + seed * 74.7) * 43758.5453;
  return h - Math.floor(h);                         // 0..1
}
function smoothstep01(t) { return t * t * (3 - 2 * t); }
function valueNoise(q, r, cell, seed) {             // 0..1, smooth patches of about `cell` tiles
  const x = q / cell, y = r / cell, gx = Math.floor(x), gy = Math.floor(y);
  const fx = smoothstep01(x - gx), fy = smoothstep01(y - gy);
  const a = hash2(gx, gy, seed), b = hash2(gx + 1, gy, seed);
  const c = hash2(gx, gy + 1, seed), d = hash2(gx + 1, gy + 1, seed);
  return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy;
}
```

Ablauf pro Tile mit `meters` aus 3.1:

1. Nimm das erste Band in `floorRules.bands`, dessen `maxMeters >= meters`.
2. Hat das Band `floor`, ist das der Bodentyp.
3. Sonst: Prüfe, ob das Tile in der Heide liegt (`floorRules.heathRegion`): `d = Abstand(q, r zu Mittelpunkt) / radius`; `t = clamp((fadeOut - d) / (fadeOut - fullUntil), 0, 1)`; `weight = smoothstep01(t)`; Heide, wenn `valueNoise(q, r, edgeNoiseCellSize, 4) < weight`. In der Heide gilt `heathMix`, falls vorhanden, sonst `mix`.
4. `n = valueNoise(q, r, floorRules.noiseCellSize, 1)`. Wähle aus der Liste nach Gewicht: `n * Summe der Gewichte`, kumuliert in Listenreihenfolge.

`reference/floor_preview.png` zeigt das erwartete Ergebnis für die ganze Karte (eine Farbe pro Tile).

### 5.2 Darstellung

- Ein `THREE.InstancedMesh` **pro Bodentyp**, alle mit derselben Hex-Geometrie und einem eigenen `MeshStandardMaterial` in der Farbe aus `floorTypes`. Kapazität jeweils = Anzahl Tiles im Sichtfenster.
- Pro Instanz eine leichte Helligkeitsvariation (±6 %, aus `hash2(q, r, 3)`) über `setColorAt`. Pro Tile eine Drehung um Y in 60°-Schritten (`Math.floor(hash2(q, r, 2) * 6)`), damit nichts gekachelt wirkt.
- Wasserebene: großes `PlaneGeometry` über die ganze Karte bei `hex.waterLevel`, halbtransparent (Opazität 0,7), dunkles Blaugrün, leichtes Glitzern durch langsam verschobene prozedurale Normal-Map oder animierte Farbe.
- Licht: warmes `DirectionalLight` schräg von Südwesten plus `HemisphereLight`. Exponentieller Nebel in der Hintergrundfarbe, so dicht, dass der Rand des Sichtfensters im Nebel verschwindet.

### 5.3 Streaming

- Sichtbar ist nur ein Fenster von `(2 * streaming.radius + 1)²` Tiles um das Tile unter dem Kamera-Pivot (`worldToHex`).
- Wechselt der Pivot das Tile, baue die Instanz-Puffer des Fensters neu auf (bei ±1 auf einer Achse darfst du nur die Randspalte bzw. -zeile tauschen, Pflicht ist das nicht). Bei 4.225 Tiles ist ein Neuaufbau schnell genug.
- Tiles außerhalb der Karte (q < 0, r < 0, q ≥ width, r ≥ height) werden **nicht** gezeichnet.
- Für Klicks: `Raycaster` gegen die InstancedMeshes, `instanceId` über eine Slot-Tabelle auf (q, r) zurückführen.

---

## 6. Kamera und Steuerung

Orbit-Kamera um einen unsichtbaren Pivot auf dem Gelände (Werte aus `camera`):

| Eingabe | Wirkung |
| --- | --- |
| W/A/S/D, Pfeiltasten | Pivot bewegen, **relativ zur Blickrichtung**, nur in XZ. Tempo = `moveSpeed * (Abstand / minZoom)` |
| Q / E | Um die senkrechte Achse durch den Pivot drehen |
| Mausrad | Abstand Kamera–Pivot zwischen `minZoom` und `maxZoom`, Neigung bleibt `pitchDegrees` |
| Rechte Maustaste halten + ziehen | Drehen um den Pivot (KANN) |
| Linksklick | Auswählen (Ort, Einheit, Tile) |
| F3 | Debug-Overlay an/aus |

- Pivot-Höhe folgt dem Gelände unter ihm, gedämpft: `pivot.y += (targetY - pivot.y) * min(1, heightSmoothing * dt)`. Unter Wasser zählt `waterLevel` als Mindesthöhe.
- Pivot bleibt innerhalb der Karte, im Kampf innerhalb des Kampffelds.
- Start: Pivot auf dem Wilseder Berg, Abstand `startZoom`.

**Debug-Overlay (F3):** FPS, Pivot-Tile (q, r), Grauwert, Meter, Spielhöhe, Bodentyp, Anzahl gezeichneter Tiles, Modus.

---

## 7. Kampagne (Weltkarte)

### 7.1 Orte

- Jeder Eintrag in `nodes` ist ein Ort auf seinem Tile. Darstellung: eine leuchtende Säule (Höhe ca. 40, Farbe der Fraktion, Untote = Violett) plus Namensschild (CSS2DRenderer aus `three/addons/renderers/CSS2DRenderer.js`). Orte sind auch außerhalb des Streaming-Fensters sichtbar.
- **Aufgedeckt** ist ein Ort, wenn er höchstens 120 Tiles (`hexDistance`) von der Armee, vom Hügelgrab oder von einem eroberten Ort entfernt ist. Unaufgedeckte Orte erscheinen als graue, niedrige Säule mit „?“.
- Klick auf einen aufgedeckten Ort öffnet ein Infofeld: Name, Typ (Mythisch, Weltlich, Christlich, Hügelgrab), Fraktion, Größe des Kampffelds, Reisezeit in Tagen, Bedrohung der Fraktion, Besatzung. **Christliche Orte** verhüllen ihre Besatzung („Verhüllt – Späher sehen nichts“), bis die Armee dort steht.

### 7.2 Reisen und Zeit

- Die Armee ist eine Figur (Lich-Form, Violett) auf ihrem aktuellen Ort. Knopf „Hierher ziehen“: Die Figur gleitet in 2–3 Sekunden in gerader Linie zum Ziel, die Kamera folgt. Tage += `ceil(hexDistance / economy.travelTilesPerDay)`.
- Kalender ab `map.startDate`, angezeigt als „1. Mai 1371“. Pro vergangenem Tag sinkt jede Bedrohung um `threat.dailyDecay` des aktuellen Werts.
- Steht die Armee an einem feindlichen Ort, zeigt das Infofeld „Angreifen“.

### 7.3 Bedrohung

- Jede lebende Fraktion außer Untoten hat einen Bedrohungswert 0–100 %, angezeigt als kleiner Balken im Kopfbereich.
- Angriff auf einen Ort: dessen Fraktion `+attackOwnNode`, alle anderen `+attackOtherFaction` (maximal 100).
- Beim Kampfbeginn erhält die Besatzung **+1 Einheit pro volle `reinforcementPer` % Bedrohung** ihrer Fraktion (Typ: die häufigste Einheit der Besatzung).

### 7.4 Hügelgrab (Phylakterium)

- Steht die Armee am Wilseder Berg: alle Untoten heilen voll, und das Menü „Rekrutieren“ ist verfügbar.
- Rekrutieren zeigt jede Untoten-Einheit außer dem Lich mit Kosten (`cost`), Kommandopunkten und ggf. benötigtem Wissen (`requiresKnowledge`, wird nicht verbraucht). Gesperrte Einheiten sind sichtbar, aber ausgegraut.
- Kommandolimit = `commandLimitBase + commandLimitPerMythicNode * eroberte mythische Orte`. Summe der `commandPoints` der Armee darf es nicht überschreiten.
- Kopfbereich zeigt immer: Datum, Leichen, Knochen, Seelen, Wissen, Kommando (genutzt / Limit).

---

## 8. Kampf (Kern des Spiels)

### 8.1 Kampffeld

- Kampffeld = Quadrat aus `size × size` Tiles, zentriert auf dem Orts-Tile, aus der echten Welt: gleiche Höhen, gleiche Bodentypen. Das Streaming-Fenster wird auf den Ort fixiert. Tiles außerhalb des Felds werden abgedunkelt (50 % Helligkeit) und sind nicht begehbar.
- Für jedes Tile im Feld gibt es ein Datenobjekt `{ q, r, floor, y, level, edges: [6 × EdgeType], unit, building }`. EdgeTypes: `OPEN`, `COVER`, `WALL`, `WALL_DESTRUCTIBLE`, `WALL_TRANSPARENT`.
- **Ausbau des Felds** (deterministisch, Zufall aus `hash2` mit einem Seed aus der Orts-ID):
  - **Weltliche und christliche Orte:** `3 * size / 16` Gebäude (16 → 3, 32 → 6, 64 → 12) im inneren Bereich (Radius `size / 3`). Ein Gebäude = Anker-Tile + Nachbar in Richtung `d` + Nachbar in Richtung `d+1` (drei Tiles, die sich gegenseitig berühren). Boden `STONE_FLOOR`. Jede Kante zu einem Tile außerhalb des Gebäudes wird auf **beiden Seiten** `WALL`, außer genau einer Tür-Kante (`OPEN`), die auf ein begehbares Tile zeigt. Ein Gebäude wird verworfen, wenn eines seiner Tiles Wasser ist, die Höhenstufen innerhalb um ≥ 2 abweichen oder es ein anderes Gebäude berührt.
  - Dazu `size / 8` Zäune: Linie aus 4–6 Tiles in einer Richtung `d`; auf jedem Tile wird Kante `(d + 1) % 6` beidseitig `COVER`.
  - **Weltliche Orte:** Rund um die Mitte (Radius 3) wird der Boden `COBBLESTONE`.
  - **Christliche Orte:** Ein Gebäude ist die Kirche; Tiles im Radius 2 um sie werden `HOLY_GROUND`. Daneben ein Friedhof mit Radius 2 aus `GRAVEYARD_GROUND`.
  - **Mythische Orte:** Keine Gebäude. Radius 2 um die Mitte wird `PAGAN_GROUND`, dazu 6–10 einzelne `COVER`-Kanten als Hünensteine. Teufelsmoor: Radius 4 wird `BOG`.
- Kantentypen sind sichtbar, wenn die Kantenanzeige (Taste T) an ist und immer an Gebäuden: `WALL` = rotes flaches Rechteck (Länge ≈ R, Höhe 1,5), `COVER` = gelbes Dreiecksprisma (Höhe 0,8), `WALL_DESTRUCTIBLE` = orangefarbenes Rechteck, `WALL_TRANSPARENT` = halbtransparentes blaues Rechteck. Mouse-over über eine Kante zeigt ihren Typ als Tooltip.
- Gebäude bekommen zusätzlich einfache Klötze als Dach (KANN), aber Wände dürfen die Sicht auf Einheiten nicht verdecken.

### 8.2 Aufstellung

- Die Armee kommt von der Seite des Felds, die zu ihrem Herkunftsort zeigt. Spieler-Einheiten stehen in den äußersten zwei Reihen dieser Seite, aber höchstens `min(size / 2 - 2, 12)` Tiles von der Mitte entfernt (bei großen Feldern rücken sie also näher heran).
- Gegner stehen im Radius `min(size / 4, 8)` um die Mitte auf begehbaren Tiles, gern in Gebäuden.

### 8.3 Initiative und Runden

- Jede Einheit hat `nextTick`, anfangs `10 - initiative`. Dran ist die Einheit mit dem kleinsten `nextTick`; bei Gleichstand höhere Initiative, dann Spieler vor Gegner. Nach ihrem Zug: `nextTick += max(1, 10 - initiative)`.
- Eine **Runde** endet jedes Mal, wenn der aktuelle Tick ein Vielfaches von 10 überschreitet. Zum Rundenende wirken Bodeneffekte: Untote auf `HOLY_GROUND` erleiden `damageUndeadPerRound`, Untote auf `GRAVEYARD_GROUND` heilen `healUndeadPerRound`.
- Oben im Bild: Initiativeleiste mit den nächsten 10 Zügen (Symbol, Name, Lebensbalken).

### 8.4 Zug einer Einheit

Ein Zug besteht aus **Bewegen, dann Angreifen** (beides optional). Wer angreift, kann sich danach nicht mehr bewegen. Leertaste beendet den Zug.

**Bewegung** (Dijkstra bis zu `move` Bewegungspunkten):

- Kosten des Ziel-Tiles = `moveCost` seines Bodentyps. `null` = nicht betretbar. Fliegende Einheiten zahlen überall 1 und dürfen auch tiefes Wasser überqueren.
- Übergang von A nach B in Richtung `d` ist gesperrt, wenn `A.edges[d] !== 'OPEN'` oder `B.edges[opposite(d)] !== 'OPEN'`. Die restriktivere Seite gewinnt. Ausnahme: `spectral` ignoriert Kanten.
- Höhenstufen-Differenz ≥ 2 zwischen A und B ist nicht begehbar, außer für Fliegende.
- Tiles mit Einheiten sind nicht betretbar; Fliegende dürfen über sie hinweg, aber nicht darauf enden.
- Anzeige: erreichbare Tiles als blaue Hex-Overlays, Pfadvorschau beim Hovern, Bewegung animiert Tile für Tile (ca. 0,15 s pro Tile).

**Angriff:**

- Reichweite: `hexDistance ≤ range`. Fernkämpfer (`range > 1`) erhalten +1 Reichweite, wenn sie mindestens 2 Stufen höher stehen als das Ziel.
- Nahkampf (Distanz 1) ist über `WALL`, `WALL_DESTRUCTIBLE` und `WALL_TRANSPARENT` hinweg nicht möglich, über `COVER` schon.
- Fernkampf braucht Sichtlinie: Gehe `hexLine` entlang. Blockiert, wenn zwischen zwei aufeinanderfolgenden Tiles eine Seite `WALL` oder `WALL_DESTRUCTIBLE` ist, oder wenn ein Tile dazwischen eine Stufe höher als `max(Angreifer, Ziel) + 1` hat. Einheiten blockieren nicht.
- **Deckung:** Führt der letzte Schritt der Linie über eine `COVER`-Kante ins Ziel-Tile, erhält das Ziel nur halben Schaden.
- Angreifbare Ziele werden rot markiert. Klick auf ein Ziel greift an.

**Schadensformel:**

```js
let dmg = attacker.damage * powerDefense[attacker.power][target.defense] / 100;
if (attacker.level > target.level) dmg *= 1.25;      // high ground
if (attacker.level < target.level) dmg *= 0.85;
if (targetInCover) dmg *= 0.5;
if (attacker.power === 'ARCANE' || attacker.power === 'CHAOS') dmg -= target.magicResist;
if (attacker.power === 'SOUL') dmg -= target.soulShield;
dmg = Math.round(dmg);
dmg = (powerDefense[attacker.power][target.defense] === 0) ? 0 : Math.max(1, dmg);
```

- `HEAL` zielt auf verwundete Verbündete und stellt `damage` HP wieder her (bis zum Maximum).
- **Konter:** Überlebt das Ziel einen Nahkampfangriff, hat `counter: true` und könnte selbst angreifen, schlägt es einmal mit 50 % seines berechneten Schadens zurück.
- Darstellung: kurzer Ausfallschritt bzw. Projektil, schwebende Schadenszahl, Lebensbalken über jeder Einheit, Kampflog am Rand.

### 8.5 Gegner-KI

Pro Zug einer gegnerischen Einheit:

1. Priester (`HEAL`): Ist ein verwundeter Verbündeter erreichbar (bewegen, dann in Reichweite), heile den mit dem größten Fehlbetrag. Sonst Angriff mit 3 `HOLY`-Schaden, falls möglich.
2. Alle anderen: Bewerte jedes erreichbare Tile mit dem besten Angriff von dort: `erwarteter Schaden + 30 bei Tötung + 15 wenn das Ziel der Lich ist − 0,5 × Abstand zum aktuellen Standort`. Fernkämpfer bevorzugen Tiles auf maximaler Reichweite und in Deckung. Nimm die beste Option.
3. Kein Angriff möglich: Gehe den Pfad zur nächsten Untoten-Einheit entlang, so weit es geht. Ballisten bewegen sich nur, wenn sie seit zwei Zügen nichts angreifen konnten.
4. Kurze Pause (ca. 0,4 s) zwischen Bewegen und Angreifen, damit der Spieler folgen kann. Die KI darf den Browser nicht einfrieren.

### 8.6 Sieg, Niederlage, Rückzug

- **Sieg:** Alle Gegner tot. Beuteschirm: Leichen (Summe über getötete Gegner: `corpsesPerKill × Leichenqualität`, abgerundet), Knochen (`bonesPerKill` pro Gegner, abgerundet), Seelen (+`soulsPerSoulKill` pro Todesstoß mit `SOUL`), plus `nodeRewards[type][size]`. Der Ort wird erobert (Fraktion Untote, Säule violett). Überlebende behalten ihre aktuellen HP.
- Leichenqualität = `unit.corpseQuality` des Töters, falls gesetzt, sonst `corpseQuality[power]`.
- **Niederlage:** Der Lich fällt. Alle anderen Einheiten der Armee sind verloren, keine Beute. Der Lich erwacht im Hügelgrab, `lichDeathDays` Tage vergehen.
- **Rückzug (Taste R, SOLL):** Wirkt zu Beginn des nächsten Zugs des Lichs. Stirbt er vorher, ist es eine Niederlage. Gelingt er: Der Lich kehrt mit einem Tag Verlust ins Hügelgrab zurück, die übrigen Einheiten sind verloren, keine Beute.
- **Spielsieg:** Der Brocken (`finale: true`) wird erobert. Abschlussbildschirm mit Tagen, Kämpfen, eroberten Orten.

---

## 9. Stealth-Phase (SOLL)

Vor dem Kampf wird geprüft, ob die Armee unentdeckt ankommt:

- Gegner stehen still und blicken in eine von 6 Richtungen (zur Ankunftsseite, ±1 per Zufall).
- Ein Gegner **entdeckt** eine Untoten-Einheit, wenn mindestens eines gilt:
  - **Sicht:** Abstand ≤ `sight`, Ziel liegt im 90°-Kegel (Richtung vom Gegner zum Ziel, gerundet auf die nächste Hex-Richtung, ist Blickrichtung oder ±1) und die Sichtlinie (wie Fernkampf) ist frei.
  - **Gehör:** Abstand ≤ `hear` und das Ziel hat `size ≥ 2` und hat sich in diesem Zug bewegt.
  - **Geruch:** Abstand ≤ `smell` und das Ziel ist nicht `spectral`.
- Ist bei Ankunft niemand entdeckt, beginnt der Schleich-Modus: Nur Spieler-Einheiten ziehen (Initiative wie oben), Gegner tun nichts. Sichtkegel der Gegner werden als halbtransparente Fächer angezeigt.
- Wird eine Einheit entdeckt: normaler Kampf, alle Gegner starten mit `nextTick - 3`.
- Greift eine unentdeckte Einheit an: **Überraschungsangriff**. Der Angriff wird sofort ausgeführt, danach normaler Kampf, alle Spieler-Einheiten starten mit `nextTick - 5`.
- Meldung beim Start, z.B. „Der Wind steht günstig. Die Wachen haben euch nicht bemerkt.“

---

## 10. Oberfläche und Stil

- Stil: mittelalterlicher Holzschnitt (Dürer). UI-Flächen wie Pergament (`#e9dfc4`), dunkelbraune Tinte (`#2b2116`), dünne Rahmen, Serifenschrift (Google Font „IM Fell English“, Ersatz Georgia). Hintergrund und Nebel in gedecktem Sepia-Grau.
- Weltkarte: Kopfleiste (Datum, Ressourcen, Kommando, Bedrohungsbalken), Infofeld rechts, Hinweiszeile unten mit den Tasten.
- Kampf: Initiativeleiste oben, Einheitenkarte unten links (Name, HP, Werte, Schadens- und Rüstungstyp), Kampflog rechts, Knöpfe „Zug beenden“, „Rückzug“, „Kanten anzeigen“.
- Einheiten als einfache Formen (`shape` und `color` aus den Daten), Größe nach `size`, auf ihrem Tile stehend. Aktive Einheit mit goldenem Ring. Spieler-Einheiten mit violettem Sockel, Gegner mit Sockel in Fraktionsfarbe.
- Kurze Einleitung beim Start (3–4 Sätze, Pergamentfenster, Knopf „Erwachen“).

---

## 11. Speichern (SOLL)

Automatisch nach jedem Kampf und jeder Reise in `localStorage` (Schlüssel `harmbringer_save_v1`): Datum, Ressourcen, Armee (Typ + HP), Armeeposition, eroberte Orte, Bedrohungen. Lese- und Schreibzugriffe in `try/catch`. Knopf „Neues Spiel“ löscht den Stand.

---

## 12. Prioritäten

**MUSS**

1. Laden der Daten, Vorberechnung, Ladeanzeige.
2. Hex-Welt mit Höhen, Bodentypen, Wasser, Streaming und Kamera.
3. Orte mit Säulen und Namen, Infofeld, Reisen, Kalender.
4. Kampf: Feld aus der Welt, Gebäude mit Wänden, Initiative, Bewegung mit Kanten- und Höhenregeln, Angriff mit Schadensformel, Konter, KI, Sieg und Niederlage.
5. Beute, Eroberung, Hügelgrab mit Rekrutieren und Kommandolimit, Spielsieg am Brocken.
6. Debug-Overlay (F3).

**SOLL**

7. Bedrohung mit Verstärkung.
8. Stealth-Phase mit Überraschungsangriff.
9. Rückzug.
10. Speichern.
11. Kantenanzeige mit Tooltip.

**KANN**

12. Tageszeit: alle 3 Runden +6 Stunden; nachts verursachen Untote +20 % Schaden und Gegner haben −2 Sicht.
13. Drehen mit rechter Maustaste, Dächer auf Gebäuden, Partikel an Orten.

---

## 13. Code-Aufbau

Eine Datei, aber klar in Abschnitte gegliedert, jeder mit Kopfkommentar:

`CONFIG` (liest `HARMBRINGER_DATA`) · `HexMath` (Referenzcode oben) · `WorldData` (Typed Arrays, Höhe, Bodentyp) · `TileRenderer` (InstancedMeshes, Streaming, Picking) · `CameraController` · `Campaign` (Orte, Reisen, Zeit, Bedrohung, Ressourcen) · `Recruitment` · `Battlefield` (Feldaufbau, Kanten) · `Battle` (Initiative, Züge, Regeln) · `Pathfinding` · `EnemyAI` · `Stealth` · `UI` · `SaveGame` · `Debug`.

- Daten und Darstellung trennen: Spielregeln arbeiten nur mit Datenobjekten, Three.js-Objekte sind Ansicht.
- Keine globalen Variablen außer den beiden Daten-Objekten und einem `game`-Objekt.
- Keine Platzhalter-Funktionen ohne Inhalt, keine „TODO“-Lücken im MUSS-Teil.

---

## 14. Abnahmetests

Prüfe deinen Code gedanklich gegen diese Werte, bevor du antwortest. Sie stammen aus den echten Daten.

| Prüfung | Erwartung |
| --- | --- |
| Grauwert Tile (667, 397), Wilseder Berg | 90 → 121,3 m → Spielhöhe 7,810 → Bodentyp `HEATHER` |
| Grauwert Tile (682, 304), Hamburg | 34 → 9,7 m → Spielhöhe 2,236 |
| Grauwert Tile (831, 725), Brocken | 255 → 450 m (gekappt) → Spielhöhe 15,033 → `RAW_STONE` |
| Grauwert Tile (100, 100), Nordsee | 15 → −28,1 m → Spielhöhe −3,742 → `DEEP_WATER` |
| `hexToWorld(682, 304)` | x = 3069, z ≈ 1579,63 |
| `hexDistance(667, 397, 682, 304)` | 101 → Reise Wilseder Berg → Hamburg = 4 Tage |
| Nachbarn von (4, 10) | N (4, 9), NE (5, 9), SE (5, 10), S (4, 11), SW (3, 10), NW (3, 9) |
| Nachbarn von (5, 10) | N (5, 9), NE (6, 10), SE (6, 11), S (5, 11), SW (4, 11), NW (4, 10) |
| Kamera beim Start | Pivot über dem Wilseder Berg, Heide-Farben ringsum, Elbe-Niederung im Norden sichtbar beim Rauszoomen |
| Ghul (BLUNT, 6) gegen Stadtwache (MEDIUM) auf gleicher Höhe | 6 × 75 % = 4,5 → 5 Schaden |
| Geist (SOUL, 8) gegen Bauer (UNARMORED, soulShield 0) | 8 × 150 % = 12 Schaden |
| Balliste (SIEGE, 20) gegen Lich (MEDIUM) | 20 × 75 % = 15 Schaden |
| Lich (ARCANE, 10) gegen Hexe (LIGHT, magicResist 4) | 10 − 4 = 6 Schaden |

**Selbstprüfung vor der Antwort:** Läuft das Spiel per file:// ohne Konsolenfehler? Funktioniert der komplette Ablauf Start → Reise nach Soltau → Kampf gewinnen → zurück zum Hügelgrab → Ghul rekrutieren? Werden Wände bei Bewegung und Sichtlinie beachtet? Bleibt der Pivot in den Kartengrenzen? Wird nichts außerhalb der Karte gezeichnet?

---

## 15. Antwortformat

1. Zwei bis drei Sätze, was gebaut wurde und was aus SOLL/KANN fehlt.
2. Die vollständige `index.html` in einem Codeblock. Keine Auslassungen wie „… Rest wie oben“.
3. Eine kurze Liste bekannter Einschränkungen.
