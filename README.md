# Harmbringer

Browser-Prototyp eines rundenbasierten Taktikspiels: Mai 1371, ein Lich erwacht im Hügelgrab am Wilseder Berg und zieht über eine Hex-Karte Norddeutschlands (echte Höhendaten) bis zum Brocken.

**Online spielen:** https://frozenenenen.github.io/Harmbringer_online/

## Orte

19 größere Orte (Städte, Klöster, mythische Stätten) und 48 Dörfer dazwischen. Dörfer haben ein kleines Kampffeld mit zwei Höfen, 2–3 Verteidiger, wenig Beute und erhöhen die Bedrohung ihrer Fraktion nur um 10 % statt 25 %. Nach einem Sieg heilen die Überlebenden um 25 % ihrer Lebenspunkte; voll geheilt wird weiterhin im Hügelgrab.

## Lokal starten

Repo herunterladen, entpacken, `index.html` doppelklicken. Der Ordner `data/` muss direkt neben `index.html` liegen. Three.js r160 wird beim Start von jsDelivr geladen.

## Steuerung

- W/A/S/D oder Pfeiltasten: Kamera bewegen · Q/E oder rechte Maustaste: drehen · Mausrad: Zoom
- Linksklick: Ort, Einheit oder Feld auswählen · F3: Debug-Overlay
- Im Kampf: Leertaste Zug beenden · R Rückzug · T Kanten anzeigen

## Dateien

| Datei | Inhalt |
| --- | --- |
| `index.html` | Das komplette Spiel (eine Datei, kein Build-Schritt) |
| `data/world_data.js` | Alle Spielwerte: Einheiten, Fraktionen, Orte, Wirtschaft, Bodentypen |
| `data/heightmap.js` | Höhendaten (1704 × 920 Felder, Base64) |
| `data/heightmap.png` | Dieselben Höhendaten als Bild |
| `reference/floor_preview.png` | Erwartete Bodentyp-Verteilung |
| `PROMPT.md` | Spezifikation, nach der das Spiel gebaut wurde |
| `PAKET.md` | Beschreibung des ursprünglichen One-Shot-Pakets |

Spielstand wird im Browser gespeichert (`localStorage`, Schlüssel `harmbringer_save_v1`).
