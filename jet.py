import pygame
import math

pygame.init()
W, H = 900, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Jet Flying -KwendaK M263251")
clock = pygame.time.Clock()

# Jet position and movement
jet_x = -100
jet_y = H // 2
speed = 4
direction = 1  # 1 = left to right, -1 = right to left

# Clouds
clouds = [
    (150, 120, 1.0),
    (380, 80,  0.8),
    (620, 140, 1.2),
    (820, 90,  0.9),
    (100, 200, 0.7),
    (500, 170, 1.1),
    (750, 200, 0.8),
]

def draw_sky():
    # Sky gradient (draw horizontal bands)
    for i in range(H):
        ratio = i / H
        r = int(50  + (135 - 50)  * ratio)
        g = int(150 + (206 - 150) * ratio)
        b = int(220 + (235 - 220) * ratio)
        pygame.draw.line(screen, (r, g, b), (0, i), (W, i))

def draw_sun():
    # Sun glow
    for r in range(60, 0, -1):
        alpha = int(255 * (1 - r / 60) * 0.3)
        color = (255, 230, 100)
        pygame.draw.circle(screen, color, (820, 80), r)
    pygame.draw.circle(screen, (255, 240, 100), (820, 80), 35)
    pygame.draw.circle(screen, (255, 255, 200), (820, 80), 22)

def draw_cloud(x, y, scale):
    col = (255, 255, 255)
    cx, cy = int(x), int(y)
    s = scale
    pygame.draw.ellipse(screen, col, (cx - int(60*s), cy - int(20*s), int(120*s), int(40*s)))
    pygame.draw.circle(screen, col, (cx - int(25*s), cy - int(10*s)), int(28*s))
    pygame.draw.circle(screen, col, (cx + int(10*s), cy - int(18*s)), int(32*s))
    pygame.draw.circle(screen, col, (cx + int(38*s), cy - int(8*s)),  int(24*s))

def draw_ground():
    # Ground strip at bottom
    pygame.draw.rect(screen, (80, 160, 80),  (0, H-60, W, 60))
    pygame.draw.rect(screen, (100, 180, 90), (0, H-60, W, 15))
    # Field lines
    for x in range(0, W, 80):
        pygame.draw.line(screen, (70, 150, 70), (x, H-60), (x+40, H), 1)

def draw_jet(x, y, facing_right):
    # All coordinates are relative to jet center (x, y)
    # Flip horizontally if facing left
    def pt(dx, dy):
        if facing_right:
            return (int(x + dx), int(y + dy))
        else:
            return (int(x - dx), int(y + dy))

    # ── FUSELAGE (main body) ──
    pygame.draw.polygon(screen, (180, 190, 200), [
        pt(-60,  0),   # tail
        pt(-40, -8),
        pt( 20, -8),
        pt( 60,  0),   # nose tip
        pt( 20,  8),
        pt(-40,  8),
    ])

    # Fuselage top shine
    pygame.draw.polygon(screen, (210, 220, 230), [
        pt(-40, -8),
        pt( 20, -8),
        pt( 40, -3),
        pt(-20, -3),
    ])

    # ── NOSE CONE ──
    pygame.draw.polygon(screen, (150, 160, 175), [
        pt(20, -8),
        pt(60,  0),
        pt(20,  8),
    ])

    # ── COCKPIT ──
    pygame.draw.ellipse(screen, (100, 200, 230),
        (int(x + (5 if facing_right else -30)), int(y - 12), 25, 14))
    pygame.draw.ellipse(screen, (180, 230, 255),
        (int(x + (8 if facing_right else -27)), int(y - 11), 10, 7))

    # ── MAIN WINGS ──
    pygame.draw.polygon(screen, (140, 150, 165), [
        pt( -5, -8),
        pt( 15, -8),
        pt(  5, -40),  # wing tip top
        pt(-30, -38),
    ])
    pygame.draw.polygon(screen, (140, 150, 165), [
        pt( -5,  8),
        pt( 15,  8),
        pt(  5,  40),  # wing tip bottom
        pt(-30,  38),
    ])

    # Wing shine
    pygame.draw.polygon(screen, (170, 180, 195), [
        pt(-5, -8),
        pt(10, -8),
        pt( 0, -28),
        pt(-15,-26),
    ])

    # ── TAIL FINS ──
    pygame.draw.polygon(screen, (130, 140, 155), [
        pt(-60,  0),
        pt(-40, -8),
        pt(-45, -28),
        pt(-65, -18),
    ])
    pygame.draw.polygon(screen, (130, 140, 155), [
        pt(-60,  0),
        pt(-40,  8),
        pt(-45,  22),
        pt(-62,  14),
    ])

    # ── ENGINE POD ──
    pygame.draw.ellipse(screen, (120, 130, 145),
        (int(x + (-45 if facing_right else -45)), int(y - 5), 30, 10))

    # ── OUTLINE ──
    pygame.draw.polygon(screen, (80, 90, 100), [
        pt(-60,  0),
        pt(-40, -8),
        pt( 20, -8),
        pt( 60,  0),
        pt( 20,  8),
        pt(-40,  8),
    ], 1)

    # ── MARKINGS ──
    pygame.draw.line(screen, (200, 50, 50),
        pt(-20, -8), pt(10, -8), 3)
    pygame.draw.line(screen, (200, 50, 50),
        pt(-20,  8), pt(10,  8), 3)

def draw_hud(x, speed_val, direction):
    font = pygame.font.SysFont('Arial', 14, bold=True)
    direction_str = ">>> EASTBOUND" if direction == 1 else "<<< WESTBOUND"
    screen.blit(font.render(f"Kwenda K  — Jet Simulation", True, (255,255,255)), (10, 10))
    screen.blit(font.render(f"Position: {int(x)}px   Speed: {speed_val}px/frame   {direction_str}", True, (255, 230, 100)), (10, 30))

# ── MAIN LOOP ──
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move jet
    jet_x += speed * direction

    # Bounce at edges
    if jet_x > W + 80:
        direction = -1
        jet_y = int(H * 0.3 + (H * 0.4) * (jet_x / W))  # vary height slightly
    if jet_x < -80:
        direction = 1
        jet_y = int(H * 0.35 + (H * 0.2))

    # Keep jet within sky area
    jet_y = max(80, min(H - 100, jet_y))

    # Draw everything
    draw_sky()
    draw_sun()

    for (cx, cy, cs) in clouds:
        draw_cloud(cx, cy, cs)

    draw_ground()
    draw_jet(jet_x, jet_y, direction == 1)
    draw_hud(jet_x, speed, direction)

    pygame.display.flip()
    clock.tick(60)