#!/usr/bin/env python3
"""MC Idle Animation - 4 Frames, Gothicvania-style chibi knight"""
from PIL import Image
import random

random.seed(123)

# MC Palette (from analysis)
P = {
    'outline':    (26, 21, 40),    # #1a1528
    'hair_dark':  (58, 37, 32),    # #3a2520
    'hair_mid':   (92, 61, 48),    # #5c3d30
    'hair_light': (120, 80, 60),   # #78503c
    'skin':       (232, 208, 184), # #e8d0b8
    'skin_shadow':(200, 170, 140), # #c8aa8c
    'armor_dark': (30, 25, 50),    # #1e1932
    'armor_mid':  (42, 31, 61),    # #2a1f3d
    'armor_light':(61, 40, 85),    # #3d2855
    'metal_hi':   (192, 192, 204), # #c0c0cc
    'white_hi':   (255, 255, 255), # #ffffff
    'belt':       (58, 42, 31),    # #3a2a1f
    'blade':      (200, 200, 220), # #c8c8dc
    'blade_hi':   (255, 255, 255),
    'eye_red':    (180, 40, 40),   # subtle red eyes
    'trans':      (0, 0, 0, 0),
}

FRAME_W = 32
FRAME_H = 32

def draw_mc_frame(y_offset=0, hair_offset=0, blade_shimmer=0):
    """Draw one MC idle frame. y_offset for breathing bob, hair_offset for sway."""
    img = Image.new('RGBA', (FRAME_W, FRAME_H), (0,0,0,0))
    
    yo = y_offset  # vertical breathing offset
    ho = hair_offset  # hair sway
    
    # ─── FEET / BOOTS (bottom, static) ───
    # Left boot
    for x in range(10, 15):
        for y in range(27, 30):
            img.putpixel((x, y), P['armor_dark']+(255,))
    img.putpixel((10, 27), P['outline']+(255,))
    img.putpixel((14, 27), P['outline']+(255,))
    for x in range(10, 15):
        img.putpixel((x, 29), P['outline']+(255,))
    
    # Right boot
    for x in range(17, 22):
        for y in range(27, 30):
            img.putpixel((x, y), P['armor_dark']+(255,))
    img.putpixel((17, 27), P['outline']+(255,))
    img.putpixel((21, 27), P['outline']+(255,))
    for x in range(17, 22):
        img.putpixel((x, 29), P['outline']+(255,))
    
    # ─── LEGS (with armor bands) ───
    for y in range(23+yo, 27):
        # Left leg
        for x in range(11, 14):
            img.putpixel((x, y), P['armor_mid']+(255,))
        # Right leg
        for x in range(18, 21):
            img.putpixel((x, y), P['armor_mid']+(255,))
    # White leg bands
    for x in range(11, 14):
        img.putpixel((x, 24+yo), P['metal_hi']+(255,))
    for x in range(18, 21):
        img.putpixel((x, 24+yo), P['metal_hi']+(255,))
    
    # ─── BELT ───
    for x in range(10, 22):
        img.putpixel((x, 22+yo), P['belt']+(255,))
    img.putpixel((15, 22+yo), P['metal_hi']+(255,))  # buckle
    img.putpixel((16, 22+yo), P['metal_hi']+(255,))
    
    # ─── TORSO (armor) ───
    for y in range(17+yo, 22+yo):
        for x in range(10, 22):
            img.putpixel((x, y), P['armor_mid']+(255,))
    # Chest plate segments
    for x in range(11, 21):
        img.putpixel((x, 18+yo), P['armor_light']+(255,))
        img.putpixel((x, 20+yo), P['armor_light']+(255,))
    # Outline
    for y in range(17+yo, 23+yo):
        img.putpixel((9, y), P['outline']+(255,))
        img.putpixel((22, y), P['outline']+(255,))
    for x in range(10, 22):
        img.putpixel((x, 16+yo), P['outline']+(255,))
    
    # ─── SHOULDERS (pauldrons) ───
    # Left
    for x in range(8, 12):
        for y in range(16+yo, 19+yo):
            img.putpixel((x, y), P['armor_dark']+(255,))
    img.putpixel((8, 16+yo), P['metal_hi']+(255,))
    img.putpixel((9, 16+yo), P['metal_hi']+(255,))
    # Right
    for x in range(20, 24):
        for y in range(16+yo, 19+yo):
            img.putpixel((x, y), P['armor_dark']+(255,))
    img.putpixel((22, 16+yo), P['metal_hi']+(255,))
    img.putpixel((23, 16+yo), P['metal_hi']+(255,))
    
    # ─── ARMS ───
    # Left arm
    for y in range(19+yo, 24+yo):
        for x in range(7, 10):
            img.putpixel((x, y), P['armor_mid']+(255,))
    # Right arm
    for y in range(19+yo, 24+yo):
        for x in range(22, 25):
            img.putpixel((x, y), P['armor_mid']+(255,))
    
    # ─── HEAD ───
    # Face
    for y in range(10+yo, 16+yo):
        for x in range(12, 20):
            img.putpixel((x, y), P['skin']+(255,))
    # Face shadow (lower)
    for x in range(12, 20):
        img.putpixel((x, 15+yo), P['skin_shadow']+(255,))
    # Head outline
    for x in range(12, 20):
        img.putpixel((x, 9+yo), P['outline']+(255,))
    for y in range(10+yo, 16+yo):
        img.putpixel((11, y), P['outline']+(255,))
        img.putpixel((20, y), P['outline']+(255,))
    
    # Eyes (subtle red glow under hair shadow)
    img.putpixel((14, 12+yo), P['eye_red']+(255,))
    img.putpixel((17, 12+yo), P['eye_red']+(255,))
    
    # ─── HAIR (spiky, covering forehead) ───
    # Main hair mass
    for y in range(7+yo, 12+yo):
        for x in range(10+ho, 22+ho):
            if y < 9+yo or (y == 9+yo and 12 <= x <= 19):
                img.putpixel((x, y), P['hair_mid']+(255,))
            else:
                img.putpixel((x, y), P['hair_dark']+(255,))
    # Top spikes
    spikes = [(12+ho, 6+yo), (14+ho, 5+yo), (16+ho, 6+yo), (18+ho, 5+yo), (20+ho, 6+yo)]
    for sx, sy in spikes:
        if 0 <= sx < FRAME_W and 0 <= sy < FRAME_H:
            img.putpixel((sx, sy), P['hair_dark']+(255,))
            if sy+1 < FRAME_H:
                img.putpixel((sx, sy+1), P['hair_mid']+(255,))
    # Hair highlight
    img.putpixel((13+ho, 8+yo), P['hair_light']+(255,))
    img.putpixel((14+ho, 7+yo), P['hair_light']+(255,))
    # Side hair
    for y in range(9+yo, 14+yo):
        img.putpixel((10+ho, y), P['hair_dark']+(255,))
        img.putpixel((21+ho, y), P['hair_dark']+(255,))
    
    # Hair outline
    for x in range(10+ho, 22+ho):
        if 0 <= x < FRAME_W:
            img.putpixel((x, min(6+yo, FRAME_H-1)), P['outline']+(255,))
    
    # ─── SWORD (diagonal, right side) ───
    blade_y_start = 14 + yo + blade_shimmer
    for i in range(10):
        bx = 24 + i // 2
        by = blade_y_start + i
        if 0 <= bx < FRAME_W and 0 <= by < FRAME_H:
            img.putpixel((bx, by), P['blade']+(255,))
            if i == 3 + blade_shimmer:
                img.putpixel((bx, by), P['blade_hi']+(255,))  # shimmer
    
    return img


# ─── Generate 4 idle frames ───
# Frame 1: neutral
# Frame 2: slight up (breathe in)
# Frame 3: neutral + hair sway
# Frame 4: slight down (breathe out) + blade shimmer

frames = [
    draw_mc_frame(y_offset=0, hair_offset=0, blade_shimmer=0),   # neutral
    draw_mc_frame(y_offset=-1, hair_offset=0, blade_shimmer=0),  # breathe up
    draw_mc_frame(y_offset=0, hair_offset=1, blade_shimmer=1),   # hair sway + shimmer
    draw_mc_frame(y_offset=1, hair_offset=0, blade_shimmer=0),   # breathe down
]

OUT = '/root/.openclaw/workspace/ProjectDarkness2D/assets/sprites/custom/'

# Save individual frames
for i, frame in enumerate(frames):
    frame.save(f'{OUT}mc_idle_{i+1}.png')
    print(f"✅ mc_idle_{i+1}.png ({frame.width}x{frame.height})")

# Save as spritesheet (4 frames horizontal: 128x32)
sheet = Image.new('RGBA', (FRAME_W * 4, FRAME_H), (0,0,0,0))
for i, frame in enumerate(frames):
    sheet.paste(frame, (i * FRAME_W, 0))
sheet.save(f'{OUT}mc_idle_sheet.png')
print(f"✅ mc_idle_sheet.png ({sheet.width}x{sheet.height})")

# Save scaled preview (4x)
preview = sheet.resize((sheet.width * 4, sheet.height * 4), Image.NEAREST)
preview.save(f'{OUT}mc_idle_preview.png')
print(f"✅ mc_idle_preview.png (4x scaled preview)")

# Save as animated GIF for preview
frames_gif = []
for f in frames:
    # Convert RGBA to RGB with dark bg for GIF
    bg = Image.new('RGBA', f.size, (24, 20, 37, 255))
    bg.paste(f, (0,0), f)
    frames_gif.append(bg.convert('RGB').resize((128, 128), Image.NEAREST))

frames_gif[0].save(
    f'{OUT}mc_idle_anim.gif',
    save_all=True,
    append_images=frames_gif[1:],
    duration=200,
    loop=0
)
print(f"✅ mc_idle_anim.gif (animated preview)")

print("\nFertig! 🎮")
