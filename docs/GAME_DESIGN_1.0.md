# Project Darkness – Game Design 1.0 (Noob-Friendly)

## 1) High Concept
Ein düsteres 2D-Action-Adventure in einer gigantischen Kathedrale.
Der Spieler wacht ohne Erinnerung auf einem Thron zwischen Leichen auf, kämpft sich durch Abschnitte, stirbt, respawnt am Thron und sammelt nach Bosskämpfen Erinnerungsschnipsel.
Großer Twist: Der Protagonist ist selbst das uralte Böse, das aus einer anderen Dimension in die Moderne zurückkehrt.

---

## 2) Vertical Slice (erste spielbare Mini-Version)
Ziel: In 1-2 Wochen als Anfänger spielbar bekommen.

### Enthalten
1. Startszene: Thronsaal
2. 1 kurzer Wegabschnitt (Kathedrale-Korridor)
3. 1-2 kleine Gegnertypen
4. 1 Mini-Boss
5. Tod -> Respawn im Thronsaal
6. Nach Boss: erster Story-Schnipsel (Vision)

### Nicht enthalten (später)
- Große Skill-Trees
- Viele Waffen
- Komplettes Endgame
- Aufwändige Cutscenes

---

## 3) Story in 5 Akten

## Akt I – Erwachen
- Protagonist erwacht auf einem Thron.
- Umgebung: Leichen in ähnlicher Kleidung wie der Held.
- Zielgefühl: „Raus hier.“

## Akt II – Der Käfig
- Kathedrale wirkt wie lebendiger Kerker.
- Erste Visionen ohne Kontext.
- Kleine Gegner greifen an.

## Akt III – Die Wächter
- Jeder Abschnitt endet mit heiliger Bossfigur.
- Bosse bewachen den Fluch.
- Mit jedem Sieg: mehr Vergangenheit wird sichtbar.

## Akt IV – Die Wahrheit
- Der Held ist nicht Opfer, sondern Ursprung des Unheils.
- Fluch wurde von heiligen Instanzen verhängt.

## Akt V – Ausbruch
- Kathedrale ist eine andere Dimension, nicht die Vergangenheit.
- Nach Ausbruch: Moderne Zeit.
- Anhänger haben über Jahrtausende Kraft zurückgeführt.
- Neue Weltordnung droht.

---

## 4) Gameplay-Kern

## Core Loop
Erkunden -> Kampf -> Sterben/Lernen -> Respawn -> stärker/zielsicherer -> Boss -> Story-Schnipsel.

## Player Basics (Start)
- Laufen (links/rechts)
- Springen
- Leichter Angriff
- Ausweichen (optional für Slice, sonst später)

## Kampf für Anfänger
- Maximal 1-2 Attacken am Anfang
- Deutlich sichtbare Gegner-Telegraphen
- Kurze Bossphasen

---

## 5) Bosse (erste Entwürfe)

1. **Der Stille Diakon** (Mini-Boss im Slice)
   - Thema: Schweigen / Schuld
   - Mechanik: langsame, harte Schläge + kurzer Dash
   - Story-Schnipsel: erste Andeutung, dass der Held gefürchtet war

2. **Die Geblendete Priorin**
3. **Der Aschene Richter**
4. **Die Kettenstimme**
5. **Der Letzte Hüter**

(Hinweis: Nur Boss 1 jetzt umsetzen.)

---

## 6) Environmental Storytelling (einfach umsetzbar)
- Leichen-Pose variieren (betend, fliehend, kniend)
- Wandinschriften/Symbole wiederholen
- Zerbrochene Statuen des Protagonisten
- Glocken-/Wind-/Flüster-SFX für Atmosphäre
- Nach Boss: Raum leicht verändern (z. B. neue Risse/rote Lichter)

---

## 7) Technischer Umsetzungsplan (Godot 4, noob)

## Ordnerstruktur
- `scenes/` -> Main, Player, Enemy, Boss, ThroneRoom
- `scripts/` -> movement, combat, respawn, vision
- `assets/` -> sprites, tiles, sfx, music
- `docs/` -> Design/ToDo

## Reihenfolge (praktisch)
1. Main-Scene + Kamera
2. Player-Movement
3. Kleine Gegner (patrol + hit)
4. Lebenssystem + Tod
5. Respawn auf Thron
6. Mini-Boss mit 2 Attacken
7. Vision-Popup nach Boss

---

## 8) Aufgabenaufteilung im Team

## Tegi (Creative/World)
- Lore-Schnipsel schreiben
- Boss-Namen/Design-Ideen
- Atmosphäre-Texte (Wände, Visionen)

## Iwan (Direction/Build)
- Entscheidungen treffen (was bleibt, was fliegt)
- Testen, Prioritäten setzen
- Fortschritt validieren („spielbar > perfekt“)

## Agent Smith (Umsetzung/Support)
- Schritt-für-Schritt Anleitung
- Scripts & Szenenstruktur vorbereiten
- Fehler debuggen
- Milestones planen

---

## 9) Milestone M1 (Definition of Done)
M1 ist fertig, wenn:
- Man im Thronsaal startet
- Zum Korridor laufen kann
- Kleine Gegner besiegen kann
- Mini-Boss erreichbar und besiegbar ist
- Bei Tod Respawn im Thronsaal funktioniert
- Nach Boss ein erster Vision-Text erscheint

---

## 10) Nächster Schritt
Direkt mit **M1 / Schritt 1** starten:
- `Main.tscn`
- `Player.tscn`
- Basisbewegung + Kamera + Respawn-Punkt
