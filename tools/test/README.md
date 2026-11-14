# Testwerkzeuge

Brauchen Node und Playwright mit Chromium (`npm i playwright` bzw. die vorinstallierte Fassung).

- `sneak.js` – spielt ganze Kämpfe mit einem einfachen Bot und meldet Sieg, Runden, Rufe, Glocke, lautlose Siege, Verluste.
  `node tools/test/sneak.js <sneak|rush> [Stunde] [Anzahl] [Ortstypen oder id:<ort>] [start|big]`
  Beispiel: `node tools/test/sneak.js sneak 0 10 VILLAGE` (nachts, 10 Dörfer). Mit `id:<ort>` wird das Kampfprotokoll mit ausgegeben.
- `three.js`, `css2d.js`, `gltf.js` – Attrappen für Three.js (keine echte Grafik, dafür schnell). `sneak.js` leitet die jsDelivr-Adressen darauf um und macht Animationen sofort fertig.

Fehler erkennt man an Zeilen mit `pageerror`, `TypeError`, `is not defined` am Ende der Ausgabe.
