# Testwerkzeuge

Brauchen Node und Playwright mit Chromium (`npm i playwright` bzw. die vorinstallierte Fassung).

- `sneak.js` – spielt ganze Kämpfe mit einem einfachen Bot und meldet Sieg, Runden, Rufe, Glocke, lautlose Siege, Verluste.
  `node tools/test/sneak.js <sneak|rush> [Stunde] [Anzahl] [Ortstypen oder id:<ort>] [start|big]`
  Beispiel: `node tools/test/sneak.js sneak 0 10 VILLAGE` (nachts, 10 Dörfer). Mit `id:<ort>` wird das Kampfprotokoll mit ausgegeben.
- `three.js`, `css2d.js`, `gltf.js` – Attrappen für Three.js (keine echte Grafik, dafür schnell). `sneak.js` leitet die jsDelivr-Adressen darauf um und macht Animationen sofort fertig.

Fehler erkennt man an Zeilen mit `pageerror`, `TypeError`, `is not defined` am Ende der Ausgabe.

- `matrix.js` – Reihenkämpfe: jede Fraktion gegen sieben Armee-Typen gleicher Stärke, mit und ohne Doktrin; die Automatik des Spiels spielt beide Seiten.
  `node tools/test/matrix.js [Verhältnis 1.3] [Stunde 12] [Orte je Fraktion 3] [Teil k/n] [Fraktionen oder -] [easy|normal|hard]` – JSON-Zeilen auf stdout, Tabelle auf stderr.
- `campaign.js` – Kampagnen-Bot: baut, forscht, lernt Pfade, rekrutiert, reist und greift an; Kämpfe spielt die Automatik (ohne Schleichen, ohne menschliches Geschick – eher zu vorsichtig als zu günstig).
  `node tools/test/campaign.js <gemischt|masse|klasse|schatten|eile|bollwerk|hexerei> [Tage 150] [Mindestverhältnis 1.0] [Saat 1] [easy|normal|hard]`
