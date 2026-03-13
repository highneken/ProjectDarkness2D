#!/usr/bin/env python3
"""Project Darkness - Throne Room Pixel Art Assets Generator"""
from PIL import Image, ImageDraw
import random

random.seed(42)  # Reproducible

# Gothicvania-compatible palette
PAL = {
    'outline':    (30, 27, 46),    # #1e1b2e
    'deep_shadow':(45, 39, 65),    # #2d2741
    'dark_mid':   (74, 62, 94),    # #4a3e5e
    'mid_stone':  (107, 93, 128),  # #6b5d80
    'light_mid':  (138, 123, 160), # #8a7ba0
    'highlight':  (168, 152, 190), # #a898be
    'bright_hi':  (196, 184, 216), # #c4b8d8
    'flame_dark': (160, 80, 32),   # #a05020
    'flame_mid':  (212, 136, 48),  # #d48830
    'flame_hot':  (248, 224, 112), # #f8e070
    'blood_dark': (120, 30, 25),   # #781e19
    'blood_mid':  (160, 45, 35),   # #a02d23
    'blood_light':(200, 60, 50),   # #c83c32
    'red_glow':   (140, 30, 40),   # #8c1e28
    'trans':      (0, 0, 0, 0),
}

def noise_pixel(base, lighter, darker, density=0.1):
    """Return base color with random texture noise"""
    r = random.random()
    if r < density / 2:
        return lighter
    elif r < density:
        return darker
    return base

def draw_stone_block(img, x, y, w, h, pal=PAL):
    """Draw a single stone block with top-left lighting"""
    d = ImageDraw.Draw(img)
    # Fill base
    for py in range(y, y+h):
        for px in range(x, x+w):
            c = noise_pixel(pal['mid_stone'], pal['light_mid'], pal['dark_mid'], 0.1)
            img.putpixel((px, py), c)
    # Top highlight (1px)
    for px in range(x, x+w):
        img.putpixel((px, y), pal['highlight'])
    # Left highlight (1px)
    for py in range(y, y+h):
        img.putpixel((x, py), pal['light_mid'])
    # Bottom shadow (1px)
    for px in range(x, x+w):
        img.putpixel((px, y+h-1), pal['dark_mid'])
    # Right shadow (1px)
    for py in range(y, y+h):
        img.putpixel((x+w-1, py), pal['dark_mid'])
    # Random chip on corners (~20%)
    if random.random() < 0.2 and w > 4 and h > 4:
        img.putpixel((x+w-2, y), pal['deep_shadow'])
        img.putpixel((x+w-1, y), pal['deep_shadow'])

def create_throne():
    """Schritt 1: Gothic stone throne 48x64"""
    img = Image.new('RGBA', (48, 64), (0,0,0,0))
    d = ImageDraw.Draw(img)
    P = PAL
    
    # Back panel (tall part) - centered, narrower
    for y in range(0, 40):
        for x in range(10, 38):
            c = noise_pixel(P['dark_mid'], P['mid_stone'], P['deep_shadow'], 0.08)
            img.putpixel((x, y), c + (255,))
    
    # Back panel outline
    d.rectangle([10, 0, 37, 39], outline=P['outline']+(255,))
    
    # Gothic arch top (pointed)
    for i in range(8):
        x1 = 14 + i
        x2 = 33 - i
        y_pos = 8 - i
        if y_pos >= 0:
            img.putpixel((x1, y_pos), P['outline']+(255,))
            img.putpixel((x2, y_pos), P['outline']+(255,))
            # Fill between
            for fx in range(x1+1, x2):
                c = noise_pixel(P['deep_shadow'], P['dark_mid'], P['outline'], 0.05)
                img.putpixel((fx, y_pos), c + (255,))
    
    # Pointed top
    for i in range(3):
        img.putpixel((23+i, 0), P['outline']+(255,))
        img.putpixel((24-i, 0), P['outline']+(255,))
    img.putpixel((24, 0), P['highlight']+(255,))
    
    # Side armrests
    for y in range(30, 48):
        for x in range(4, 14):
            c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.1)
            img.putpixel((x, y), c + (255,))
        for x in range(34, 44):
            c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.1)
            img.putpixel((x, y), c + (255,))
    
    # Armrest outlines
    d.rectangle([4, 30, 13, 47], outline=P['outline']+(255,))
    d.rectangle([34, 30, 43, 47], outline=P['outline']+(255,))
    
    # Armrest top highlights
    for x in range(5, 13):
        img.putpixel((x, 30), P['highlight']+(255,))
    for x in range(35, 43):
        img.putpixel((x, 30), P['highlight']+(255,))
    
    # Seat
    for y in range(40, 48):
        for x in range(10, 38):
            c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.1)
            img.putpixel((x, y), c + (255,))
    d.rectangle([10, 40, 37, 47], outline=P['outline']+(255,))
    # Seat top highlight
    for x in range(11, 37):
        img.putpixel((x, 40), P['highlight']+(255,))
    
    # Legs/base
    for y in range(48, 62):
        # Left leg
        for x in range(8, 16):
            c = noise_pixel(P['dark_mid'], P['mid_stone'], P['deep_shadow'], 0.08)
            img.putpixel((x, y), c + (255,))
        # Right leg
        for x in range(32, 40):
            c = noise_pixel(P['dark_mid'], P['mid_stone'], P['deep_shadow'], 0.08)
            img.putpixel((x, y), c + (255,))
        # Center support
        for x in range(18, 30):
            c = noise_pixel(P['deep_shadow'], P['dark_mid'], P['outline'], 0.06)
            img.putpixel((x, y), c + (255,))
    
    # Leg outlines
    d.rectangle([8, 48, 15, 61], outline=P['outline']+(255,))
    d.rectangle([32, 48, 39, 61], outline=P['outline']+(255,))
    
    # Base/floor bar
    for x in range(6, 42):
        for y in range(62, 64):
            img.putpixel((x, y), P['outline']+(255,))
    for x in range(7, 41):
        img.putpixel((x, 62), P['dark_mid']+(255,))
    
    # Rune symbols on back panel
    rune_positions = [(18, 15), (26, 15), (22, 22)]
    for rx, ry in rune_positions:
        # Simple cross/circle rune
        img.putpixel((rx, ry), P['red_glow']+(255,))
        img.putpixel((rx+1, ry), P['red_glow']+(255,))
        img.putpixel((rx, ry+1), P['red_glow']+(255,))
        img.putpixel((rx+1, ry+1), P['red_glow']+(255,))
        img.putpixel((rx-1, ry), P['blood_dark']+(180,))
        img.putpixel((rx+2, ry), P['blood_dark']+(180,))
        img.putpixel((rx, ry-1), P['blood_dark']+(180,))
        img.putpixel((rx, ry+2), P['blood_dark']+(180,))
    
    # Red glow at base (subtle)
    for x in range(12, 36):
        for y in range(58, 62):
            if random.random() < 0.3:
                img.putpixel((x, y), P['red_glow']+(60,))
    
    return img

def create_broken_statue():
    """Schritt 2: Broken statue 32x64"""
    img = Image.new('RGBA', (32, 64), (0,0,0,0))
    d = ImageDraw.Draw(img)
    P = PAL
    
    # Base/pedestal (bottom)
    for y in range(52, 64):
        for x in range(4, 28):
            c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.1)
            img.putpixel((x, y), c + (255,))
    d.rectangle([4, 52, 27, 63], outline=P['outline']+(255,))
    for x in range(5, 27):
        img.putpixel((x, 52), P['highlight']+(255,))
    
    # Legs (lower body intact)
    for y in range(32, 52):
        for x in range(10, 22):
            c = noise_pixel(P['dark_mid'], P['mid_stone'], P['deep_shadow'], 0.08)
            img.putpixel((x, y), c + (255,))
    # Left leg
    for y in range(40, 52):
        for x in range(8, 14):
            c = noise_pixel(P['dark_mid'], P['mid_stone'], P['deep_shadow'], 0.08)
            img.putpixel((x, y), c + (255,))
    # Right leg
    for y in range(40, 52):
        for x in range(18, 24):
            c = noise_pixel(P['dark_mid'], P['mid_stone'], P['deep_shadow'], 0.08)
            img.putpixel((x, y), c + (255,))
    
    # Torso (partially broken - jagged top)
    for y in range(16, 32):
        width_reduce = max(0, (20 - y) * 1) if y < 20 else 0
        for x in range(9 + width_reduce, 23 - width_reduce):
            if y < 20 and random.random() < 0.3:
                continue  # Broken chunks missing
            c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.1)
            img.putpixel((x, y), c + (255,))
    
    # Jagged break line at top
    break_y = [18, 16, 17, 14, 16, 18, 15, 17, 19, 16, 14, 17, 18, 16]
    for i, by in enumerate(break_y):
        x = 9 + i
        if x < 23:
            for y in range(by, by+2):
                if 0 <= y < 64:
                    img.putpixel((x, y), P['highlight']+(255,))
    
    # Outline the figure
    for y in range(14, 52):
        for x in range(7, 25):
            px = img.getpixel((x, y))
            if px[3] > 0:
                # Check neighbors for outline
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 32 and 0 <= ny < 64:
                        if img.getpixel((nx, ny))[3] == 0:
                            img.putpixel((nx, ny), P['outline']+(255,))
    
    # One arm stub remaining (left side)
    for y in range(22, 30):
        for x in range(5, 9):
            c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.1)
            img.putpixel((x, y), c + (255,))
    
    # Rubble pieces on ground
    rubble = [(2, 58), (3, 59), (25, 57), (26, 58), (28, 60), (1, 60)]
    for rx, ry in rubble:
        for dx in range(3):
            for dy in range(2):
                if random.random() < 0.7:
                    c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.15)
                    img.putpixel((rx+dx, ry+dy), c + (255,))
    
    return img

def create_wall_rune(variant=1):
    """Schritt 3a: Wall rune tile 16x16"""
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    P = PAL
    
    if variant == 1:
        # Circular rune with cross
        center = (8, 8)
        # Circle outline
        circle_pts = [
            (6,4),(7,3),(8,3),(9,3),(10,4),
            (11,5),(11,6),(11,7),(11,8),(11,9),(11,10),
            (10,11),(9,12),(8,12),(7,12),(6,11),
            (5,10),(5,9),(5,8),(5,7),(5,6),(5,5)
        ]
        for px, py in circle_pts:
            img.putpixel((px, py), P['red_glow']+(200,))
        # Inner cross
        for i in range(6, 11):
            img.putpixel((8, i), P['blood_mid']+(180,))
            img.putpixel((i, 8), P['blood_mid']+(180,))
        # Center bright
        img.putpixel((8, 8), P['blood_light']+(220,))
    else:
        # Angular/diamond rune
        pts = [
            (8,2),(9,3),(10,4),(11,5),(12,6),(12,7),(11,8),
            (10,9),(9,10),(8,11),(7,10),(6,9),(5,8),
            (4,7),(4,6),(5,5),(6,4),(7,3)
        ]
        for px, py in pts:
            img.putpixel((px, py), P['red_glow']+(200,))
        # Inner vertical line
        for y in range(4, 10):
            img.putpixel((8, y), P['blood_mid']+(180,))
        # Inner dots
        img.putpixel((7, 6), P['blood_dark']+(160,))
        img.putpixel((9, 6), P['blood_dark']+(160,))
    
    return img

def create_wall_crack(variant=1):
    """Schritt 3b: Wall crack tile 16x16"""
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    P = PAL
    
    if variant == 1:
        # Diagonal crack
        crack_path = [(3,2),(4,3),(4,4),(5,5),(6,6),(6,7),(7,8),(8,9),(9,10),(9,11),(10,12),(11,13)]
        for px, py in crack_path:
            img.putpixel((px, py), P['outline']+(220,))
            # Highlight side
            img.putpixel((px+1, py), P['light_mid']+(120,))
            # Shadow side  
            if px > 0:
                img.putpixel((px-1, py), P['deep_shadow']+(150,))
        # Small branch
        branch = [(6,6),(7,5),(8,4)]
        for px, py in branch:
            img.putpixel((px, py), P['deep_shadow']+(180,))
    else:
        # Larger branching crack
        main = [(2,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13)]
        for px, py in main:
            img.putpixel((px, py), P['outline']+(220,))
            img.putpixel((px+1, py), P['light_mid']+(100,))
        branch1 = [(6,5),(5,6),(4,7),(3,8),(3,9)]
        for px, py in branch1:
            img.putpixel((px, py), P['deep_shadow']+(200,))
        branch2 = [(9,9),(10,8),(11,7),(12,7)]
        for px, py in branch2:
            img.putpixel((px, py), P['deep_shadow']+(180,))
    
    return img

def create_chains():
    """Schritt 3c: Hanging chains 16x32"""
    img = Image.new('RGBA', (16, 32), (0,0,0,0))
    P = PAL
    
    # Two chains hanging down
    for chain_x in [5, 11]:
        # Wall mount
        for dx in range(-1, 2):
            img.putpixel((chain_x+dx, 0), P['dark_mid']+(255,))
            img.putpixel((chain_x+dx, 1), P['mid_stone']+(255,))
        
        # Chain links alternating orientation
        y = 2
        while y < 30:
            # Vertical link
            img.putpixel((chain_x, y), P['mid_stone']+(255,))
            img.putpixel((chain_x, y+1), P['light_mid']+(255,))
            img.putpixel((chain_x, y+2), P['mid_stone']+(255,))
            # Horizontal connector
            img.putpixel((chain_x-1, y+3), P['dark_mid']+(255,))
            img.putpixel((chain_x, y+3), P['mid_stone']+(255,))
            img.putpixel((chain_x+1, y+3), P['dark_mid']+(255,))
            y += 4
        
        # Outline
        for oy in range(2, 30):
            px = img.getpixel((chain_x, oy))
            if px[3] > 0:
                for dx in [-1, 1]:
                    nx = chain_x + dx
                    if 0 <= nx < 16 and img.getpixel((nx, oy))[3] == 0:
                        img.putpixel((nx, oy), P['outline']+(140,))
    
    return img

def create_floor_blood():
    """Schritt 4a: Blood splatter 16x16"""
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    P = PAL
    
    # Organic blood pool shape
    blood_pts = [
        (6,6),(7,5),(8,5),(9,6),(10,6),
        (5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),
        (5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(11,8),
        (6,9),(7,9),(8,9),(9,9),(10,9),
        (7,10),(8,10),(9,10),
        (8,11),
        # Splatter drops
        (4,5),(12,9),(3,8),(13,7),
    ]
    for px, py in blood_pts:
        if (px, py) in [(8,7),(8,8),(7,8),(9,7)]:
            img.putpixel((px, py), P['blood_light']+(200,))
        elif random.random() < 0.3:
            img.putpixel((px, py), P['blood_dark']+(180,))
        else:
            img.putpixel((px, py), P['blood_mid']+(190,))
    
    return img

def create_floor_debris():
    """Schritt 4b: Stone debris 16x16"""
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    P = PAL
    
    # Scattered stone chunks
    chunks = [
        (2,10,4,3), (7,9,3,2), (11,11,4,2), (5,12,2,2),
        (13,9,2,3), (1,13,3,2), (9,13,2,2)
    ]
    for cx, cy, cw, ch in chunks:
        for dx in range(cw):
            for dy in range(ch):
                c = noise_pixel(P['mid_stone'], P['light_mid'], P['dark_mid'], 0.15)
                img.putpixel((cx+dx, cy+dy), c + (255,))
        # Top highlight
        for dx in range(cw):
            img.putpixel((cx+dx, cy), P['highlight']+(255,))
        # Outline bottom
        for dx in range(cw):
            img.putpixel((cx+dx, cy+ch-1), P['outline']+(200,))
    
    return img

def create_floor_crack():
    """Schritt 4c: Floor crack 16x16"""
    img = Image.new('RGBA', (16, 16), (0,0,0,0))
    P = PAL
    
    # Horizontal-ish crack (floor perspective)
    crack = [(1,7),(2,7),(3,8),(4,8),(5,7),(6,8),(7,8),(8,9),(9,9),(10,8),(11,8),(12,9),(13,9),(14,8)]
    for px, py in crack:
        img.putpixel((px, py), P['outline']+(200,))
        img.putpixel((px, py+1), P['deep_shadow']+(160,))
        if py > 0:
            img.putpixel((px, py-1), P['light_mid']+(100,))
    # Small branches
    branch = [(5,7),(5,6),(6,5),(4,9),(4,10)]
    for px, py in branch:
        img.putpixel((px, py), P['deep_shadow']+(170,))
    
    return img

# ─── Generate all assets ───
OUT = '/root/.openclaw/workspace/ProjectDarkness2D/assets/sprites/custom/'

print("Schritt 1: Thron...")
create_throne().save(OUT + 'throne.png')

print("Schritt 2: Zerbrochene Statue...")
create_broken_statue().save(OUT + 'broken_statue.png')

print("Schritt 3: Wand-Deko...")
create_wall_rune(1).save(OUT + 'wall_rune_1.png')
create_wall_rune(2).save(OUT + 'wall_rune_2.png')
create_wall_crack(1).save(OUT + 'wall_crack_1.png')
create_wall_crack(2).save(OUT + 'wall_crack_2.png')
create_chains().save(OUT + 'chains.png')

print("Schritt 4: Boden-Overlays...")
create_floor_blood().save(OUT + 'floor_blood_1.png')
create_floor_debris().save(OUT + 'floor_debris.png')
create_floor_crack().save(OUT + 'floor_crack.png')

# ─── Schritt 5: Validation overview ───
print("Schritt 5: Validierung + Übersicht...")
assets = [
    ('throne.png', 'Thron 48x64'),
    ('broken_statue.png', 'Statue 32x64'),
    ('wall_rune_1.png', 'Rune 1'),
    ('wall_rune_2.png', 'Rune 2'),
    ('wall_crack_1.png', 'Crack 1'),
    ('wall_crack_2.png', 'Crack 2'),
    ('chains.png', 'Ketten'),
    ('floor_blood_1.png', 'Blut'),
    ('floor_debris.png', 'Trümmer'),
    ('floor_crack.png', 'Bodenriss'),
]

# Create overview image (all assets side by side)
overview_w = 400
overview_h = 80
overview = Image.new('RGBA', (overview_w, overview_h), (24, 20, 37, 255))

x_pos = 4
for fname, label in assets:
    sprite = Image.open(OUT + fname)
    # Scale 2x for visibility
    scaled = sprite.resize((sprite.width*2, sprite.height*2), Image.NEAREST)
    # Fit in overview
    if scaled.height > overview_h - 8:
        ratio = (overview_h - 8) / scaled.height
        scaled = sprite.resize((int(sprite.width*ratio*2), overview_h-8), Image.NEAREST)
    paste_y = (overview_h - scaled.height) // 2
    overview.paste(scaled, (x_pos, paste_y), scaled)
    x_pos += scaled.width + 4
    
    # Validate
    assert sprite.mode == 'RGBA', f"{fname}: Not RGBA!"
    assert sprite.width % 16 == 0, f"{fname}: Width {sprite.width} not multiple of 16!"
    assert sprite.height % 16 == 0 or sprite.height == 64 or sprite.height == 32, f"{fname}: Height check"
    print(f"  ✅ {fname} ({sprite.width}x{sprite.height}) - OK")

overview.save(OUT + 'overview_all_assets.png')
print("\n✅ Alle Assets erstellt und validiert!")
print(f"📁 Gespeichert in: {OUT}")
