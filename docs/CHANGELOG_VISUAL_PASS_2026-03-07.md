# Visual Pass – 2026-03-07

## Ziel
Lesbarkeit + Stimmung verbessern (dunkel/gothic behalten), ohne Gameplay/Physik/Controls zu ändern.

## Geändert

### 1) Render-/Layer-Lesbarkeit (Main + Room2 + ThroneRoom)
- Hintergrund-Layer (`Bg*`, `Columns*`) dunkler und atmosphärischer moduliert.
- Nebel-/Mist-Bänder neu balanciert (weniger "grauer Schleier", mehr Tiefenstaffelung).
- Vignette im Main/ThroneRoom verstärkt für stärkeren Fokus.

### 2) Fokuspunkte & Lichtführung
- Neue Moonlight-Layer (`MoonBeam`, `MoonBeamCore`) in Main, Room2, ThroneRoom ergänzt.
- ThroneRoom: Fokus-Halo und stärkere Throne-Glow-Werte für klare Boss-Arena-Mitte.
- Boden-/Pfad-Rim-Lights ergänzt (`RimLightBand`, `PathRim`) für bessere Weglesbarkeit.

### 3) Interaktive Flächen lesbarer
- Main/Room2: dezente Plattform-Guide-Lights (`PlatformGuideA/B`) hinzugefügt.
- ThroneRoom: FloorVisual/FloorEdge/PathGuide kontrastreicher abgestimmt.

### 4) Asset-Integration/Ordnung
- Keine neuen Junk-Daten gefunden (`__MACOSX`, `._*` nicht vorhanden).
- Bestehende externen Asset-Pfade beibehalten, keine Gameplay-Assets ersetzt.

## Nicht geändert (bewusst)
- Keine Änderungen an Player-Physics, Hitboxen, Controls oder Gegner-Logik.
- Keine zusätzlichen Shader/teuren PostFX (Performance-schonend, nur leichte ColorRect/Sprite-Modulation).

## Betroffene Dateien
- `scenes/Main.tscn`
- `scenes/Room2.tscn`
- `scenes/ThroneRoom.tscn`

## Validierung
- Projektstart geprüft mit: `godot4 --headless --path /root/.openclaw/workspace/ProjectDarkness2D --quit`
- Ergebnis: lädt ohne Parse-Fehler.

## Nächste kleine High-Impact-Upgrades
1. Leichte Camera Trauma/Shake nur bei Treffer/Boss-Impact (visuell, kein Gameplay-Eingriff).
2. Simple additive Torch-Sprite (2-3 Frames) an Schlüsselstellen im Thronsaal.
3. Farb-LUT/WorldEnvironment sehr subtil pro Raum, um Main/Room2/ThroneRoom stärker zu differenzieren.
