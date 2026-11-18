# Balance-Bericht (16.–18.11.2026)

Auftrag Kevin: „bitte teste du das Balancing so weit wie möglich“, „richte 3 Schwierigkeitsstufen ein“, „Du musst im Balance-Test natürlich auch verschiedene Spielstile austesten.“

Alle Kämpfe spielt die Automatik des Spiels auf beiden Seiten (wie nach dem Tod des Lichs). Sie schleicht nicht und nutzt kein Geschick – echte Spieler schneiden eher besser ab.

## Werkzeuge

| Werkzeug | Was es misst |
|-|-|
| `tools/test/matrix.js` | Reihenkämpfe: je Fraktion 3 Orte × 7 Armee-Typen, mit/ohne Doktrin, wählbare Stufe. Modus `fair`: Armee so stark wie die Besatzung mit Doktrin |
| `tools/test/campaign.js` | Kampagnen-Bot je Spielstil und Stufe: baut, forscht, lernt Pfade, rekrutiert, sammelt Verwaiste, greift das nächste Ziel an, das er laut Gefahrenschätzung schafft |
| `tools/test/sneak.js` | Einzelkämpfe mit Schleich- oder Sturm-Bot, Armee `start`/`big`/`schatten`, wählbare Stufe |
| `tools/balance_styles.py` | Faustregel: Wert je Kommando-Punkt und je Kosten |

## 1. Gefundene Probleme und Korrekturen

| Befund | Korrektur | Version |
|-|-|-|
| Gegner-KI stürzte sich mit festem Bonus auf den Lich, der durch Eroberungen fast unverwundbar wird – die übrige Armee verlor fast nichts | Bonus fürs Anführer-Jagen zählt nur, wenn der Schlag mindestens ein Zehntel seiner LP nimmt (`hurt` in `EnemyAI`) | 146 |
| Doktrin-Ausreißer (Siegquote mit/ohne Doktrin bei 0,7-facher Stärke): Askanier 19/100 %, Wodan 14/71 %, Mecklenburg 48/71 %, Spreewald 57/100 %, Heidegeister 29/52 % | Askanier Bauern ×1,3 (statt 1,8); Wodan Sturmangriff nur Sachsenkrieger und Wilde Jäger; Mecklenburg +1 Initiative nur Ritter; Spreewald Lutki ×1,25 (statt 1,5); Heidegeister Hinterhalt 25 % (statt 35 %) | 146 |
| Gefahrenfarbe unterschätzte Geisterwesen und schnelle Einheiten (Irrlichter, Schwarze Hunde, Hexen); Trennschärfe 0,69 | Neue Formel `Campaign.unitStrength` (an 420 Kämpfen ausgerichtet, Trennschärfe 0,84), Lich mit echten Werten (`ownStrength`), Besatzung mit Doktrin und Stufe (`foeStrength`). Grün ≥ 1,3-fach, gelb ≥ 1, rot darunter | 146/147 |
| **Fehler:** Fiel der Lich und endete der Kampf danach mit Rückzug, verschwand er für immer aus der Armee | Überlebende warten als Verwaiste, Lich erwacht im Hügelgrab (`BUGS.md`) | 150 |
| Schwer war im offenen Kampf kaum schwerer als Mittel (90 % gegen 92 % Siege) | Lebende auf Schwer +20 % LP, +15 % Schaden (statt +10/+5) | 153 |

## 2. Fraktionen (Reihenkämpfe nach Korrektur)

Armee genau so stark wie die Besatzung samt Doktrin (Modus `fair`, Mittel, 210 Kämpfe): **98 % Siege, alle Fraktionen 81–100 %.** Keine Doktrin fällt mehr heraus; dass Askanier-Orte mit Doktrin mehr Truppen haben, zeigt jetzt die Gefahrenfarbe an.

## 3. Schwierigkeitsstufen (gleiche Armeen, Verhältnis 1,0, je 420 Kämpfe)

| | Leicht | Mittel | Schwer (alt) | Schwer (neu) |
|-|-|-|-|-|
| Siege | 98 % | 92 % | 90 % | **80 %** |
| Rest der Armee nach Sieg (mit Doktrin) | 0,64 | 0,55 | 0,55 | 0,46 |

Die Stufen ändern mehr als Werte (siehe Design-Dokument „Schwierigkeitsstufen“): Auf Leicht zielt die KI wahllos, sucht weder Lich noch Deckung und Wachen rufen spät; auf Schwer bündelt sie Angriffe auf Angeschlagene, Schützen weichen zurück, jede Wache ruft sofort, nach der Glocke kommt Entsatz. Diese Wachen-Regeln wirken nur beim Schleichen – siehe Abschnitt 5.

## 4. Spielstile

**Offene Feldschlacht** (Siege / Rest der Armee, mit Doktrin):

| Stil | Leicht | Mittel | Schwer (neu) |
|-|-|-|-|
| Hexerei | 100 % / 0,92 | 100 % / 0,82 | 100 % / 0,77 |
| Klasse | 100 % / 0,87 | 90 % / 0,70 | 77 % / 0,56 |
| Bollwerk | 100 % / 0,86 | 93 % / 0,77 | 73 % / 0,55 |
| Masse | 97 % / 0,60 | 83 % / 0,47 | 77 % / 0,43 |
| Start | 97 % / 0,50 | 87 % / 0,46 | 77 % / 0,39 |
| Eile | 97 % / 0,38 | 90 % / 0,39 | 73 % / 0,33 |
| Schatten | 97 % / 0,32 | 67 % / 0,24 | 47 % / 0,16 |

**Kampagnen** (Bot, 100 Tage, eroberte Orte; Siege überall 93–100 %, weil der Bot nur Ziele angreift, die er laut Gefahrenschätzung schafft):

| Stufe | Ø | gemischt | Masse | Klasse | Schatten | Eile | Bollwerk | Hexerei |
|-|-|-|-|-|-|-|-|-|
| Leicht | 35 | 28 | 29 | 38 | 52 | 35 | 24 | 42 |
| Mittel | 29 | 24 | 26 | 23 | 33 | 35 | 29 | 33 |
| Schwer (alt) | 30 | 23 | 26 | 33 | 34 | 32 | 27 | 37 |

Ein Lauf je Stil, die Streuung ist groß (Klasse 23–38). Kampagnen auf Schwer mit den neuen Werten sind nicht nachgemessen.

Bewertung:

- **Hexerei** ist der stärkste Stil in der offenen Schlacht (100 % auf allen Stufen) und in den Kampagnen vorn. Vermutlich unterschätzt die Stärke-Schätzung die Fähigkeiten (Knochenhexer, Nekromant) – Kandidat für eine leichte Abschwächung, sobald Kevin selbst gespielt hat.
- **Schatten** ist in der offenen Schlacht klar am schwächsten, kommt in Kampagnen aber weit (schnell, viele Geister). Gewollt: Seine Stärke ist das Schleichen.
- **Eile** erobert am schnellsten, verliert aber viel – passt zum Stil.
- **Masse und gemischt** sind am langsamsten.

## 5. Schleichen mit dem Schatten-Stil

SCHLEICH_ERGEBNIS

## 6. Wirtschaft

- **Leichen sind bei allen Stilen der Engpass:** fast immer 0–40 auf Lager, jede Einheit kostet 3. Teure Elite (Knochenreiter 750 Knochen, Todesritter) kommt nur tröpfchenweise.
- Wer früh das Kommando mit billigen Ghulen und Zombies füllt, hat später keinen Platz für Stil-Einheiten (im ersten Bot-Lauf bestanden alle Armeen am Ende großteils aus Zombies). Mögliche Abhilfe, nicht umgesetzt: Einheiten entlassen und dabei Leichen/Knochen teilweise zurückbekommen.

## 7. Nicht getestet / Grenzen

- Schleichen nur mit einfachem Bot; echtes Spielgefühl fehlt.
- Städte mit Mauern: Die Automatik baut kein Belagerungsgerät und bleibt stecken (Kampf nach 40 Runden abgebrochen).
- Koop, Expeditionen, Pantheon-Kämpfe und das Finale am Brocken sind nicht durchgespielt.
