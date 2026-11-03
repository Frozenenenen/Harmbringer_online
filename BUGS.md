# Fehlerliste

Gefundene Fehler im Spiel (`index.html`). Neueste oben. Status: offen, behoben (ungetestet), bestätigt.

| Datum | Fehler | Status |
|-|-|-|
| 2026-11-03 | **Kamera läuft weiter:** Rechte Maustaste (Drehen) und W/A/S/D gleichzeitig, dann die rechte Maustaste außerhalb des Fensters loslassen → die Kamera bewegt sich weiter, auch nach Loslassen von W. Erst erneutes Drücken und Loslassen im Fenster stoppt sie. **Ursache:** Loslassen und Kontextmenü landeten außerhalb des Spiels, die Tasten-Loslass-Ereignisse gingen verloren. **Behebung:** Pointer-Capture beim Drehen; Kontextmenü, Fokusverlust, Tab-Wechsel und fehlende Maustaste in `pointermove` setzen Tasten und Drehung zurück. | behoben (ungetestet) |
