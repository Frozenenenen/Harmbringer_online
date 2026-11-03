# Fehlerliste

Gefundene Fehler im Spiel (`index.html`). Neueste oben. Status: offen, behoben (ungetestet), bestätigt.

| Datum | Fehler | Status |
|-|-|-|
| 2026-11-03 | **Nach dem Angriff nicht mehr ziehen:** Eine Einheit konnte nur ziehen und dann angreifen, nicht umgekehrt – nach einem Angriff endete der Zug sofort. **Behebung:** Hat die Einheit noch nicht gezogen, bleibt der Zug nach dem Angriff offen und die erreichbaren Felder werden angezeigt. | behoben (ungetestet) |
| 2026-11-03 | **Welt grau, keine Orte:** Nach dem Wechsel auf die 16-Bit-Höhenkarte waren Welt und Minimap grau, Orte unsichtbar. **Ursache (vermutet):** Der Browser hatte die alte `heightmap.js` zwischengespeichert (GitHub Pages: 10 Minuten), die neue `index.html` las sie als Meter → ungültige Höhen. **Behebung:** Daten-Skripte mit `?v=…` laden; passen Daten und Spiel nicht zusammen, erscheint ein Hinweis „Strg + F5“. | behoben (ungetestet) |
| 2026-11-03 | **Kamera läuft weiter:** Rechte Maustaste (Drehen) und W/A/S/D gleichzeitig, dann die rechte Maustaste außerhalb des Fensters loslassen → die Kamera bewegt sich weiter, auch nach Loslassen von W. Erst erneutes Drücken und Loslassen im Fenster stoppt sie. **Ursache:** Loslassen und Kontextmenü landeten außerhalb des Spiels, die Tasten-Loslass-Ereignisse gingen verloren. **Behebung:** Pointer-Capture beim Drehen; Kontextmenü, Fokusverlust, Tab-Wechsel und fehlende Maustaste in `pointermove` setzen Tasten und Drehung zurück. | behoben (ungetestet) |
