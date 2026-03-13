# Project Darkness 2D — SNES/GBA Pixel Scale Ruleset

Status: active baseline (Godot 4.6)
Owner: Iwan + Agent

## 1) Visual Target
- Style goal: **SNES/GBA-inspired dark fantasy**
- Quality goal: **modern-monitor sharpness** (no blur/mush)
- Rule: retro proportions + clean readability over strict nostalgia purity

## 2) Core Technical Rules

### 2.1 Display & Stretch
- Window target: `1280x720`
- Stretch mode: `canvas_items`
- Stretch aspect: `keep`
- Why: stable composition, no weird aspect stretching.

### 2.2 Pixel Clarity Rules
- Default texture filter: **Nearest** (no blur)
- 2D transform snap: ON
- 2D vertex snap: ON
- Why: avoids shimmering and muddy sprites on modern displays.

### 2.3 Placement Grid
- Main grid: **16 px**
- Sub grid: **8 px**
- Level geometry and props should snap to this grid.

## 3) Asset Baseline (current imported pack)
- Atlas: `1761x325` (`atlas.png`)
- Background: `1078x224`
- Columns: `522x224`
- Tileset: `336x224`

## 4) Canonical Scale Ratios (game world)
Reference: **Player visible body height = 1.0 unit**

- Player (MC): 1.0
- Standard enemy: 0.95–1.05
- Throne hero prop: 1.6–1.8
- Door height: 2.0–2.4
- Pillar medium prop: 1.5–1.9
- Corpse prop: 0.7–1.0

If uncertain: choose readability over realism.

## 5) Current Implementation Decisions (applied)
- Player sprite scale set to `0.53`
- Enemy sprite scale set to `0.53`
- Throne in Main reduced to closer ratio vs MC
- Pillar instances in Main/Room2 scaled to `0.58`
- HUD readability pass (high contrast panel + larger text)
- Camera framing normalized in active scenes (`zoom = 1` with limits)

## 6) Animation & Hitbox Consistency Rules
- Visual size, collision shape, and hitbox must be reviewed together.
- Never scale character visuals without sanity-checking:
  - floor contact
  - sword reach readability
  - enemy contact fairness

## 7) “Done” Criteria for Future Assets
A new asset/animation is accepted only if:
1. It respects the ratio table above.
2. It stays sharp (no filter blur).
3. It reads clearly against the scene background.
4. It does not break combat readability (hurtboxes/hitboxes still fair).

## 8) Next Standardization Pass (recommended)
1. Lock one camera framing preset for all rooms.
2. Normalize all prop instances to ratio table.
3. Add a dedicated test scene with MC + enemy + throne + door side-by-side for quick visual QA.
