import pygame
import math

pygame.init()
W, H = 860, 460
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Business Card - Kwenda Kumbirayi")
clock = pygame.time.Clock()

def draw_card():
    # ── BACKGROUND ──
    screen.fill((20, 20, 26))

    # Dot grid
    for gx in range(0, W, 40):
        for gy in range(0, H, 40):
            pygame.draw.circle(screen, (35, 35, 45), (gx, gy), 2)

    # ── CARD BODY ──
    pygame.draw.rect(screen, (33, 33, 43), pygame.Rect(40, 40, W-80, H-80), border_radius=12)

    # ── GOLD TOP BAR ──
    pygame.draw.rect(screen, (217, 173, 51), pygame.Rect(40, 40, W-80, 45), border_radius=12)

    # ── GOLD BOTTOM BAR ──
    pygame.draw.rect(screen, (217, 173, 51), pygame.Rect(40, H-85, W-80, 45), border_radius=12)

    # ── GOLD LEFT STRIPE ──
    pygame.draw.rect(screen, (217, 173, 51), pygame.Rect(40, 40, 55, H-80))
    pygame.draw.rect(screen, (33, 33, 43), pygame.Rect(52, 90, 32, H-180))

    # ── CIRCLES on left ──
    cx, cy = 68, H // 2
    for r, col in [(60,(217,173,51)), (48,(33,33,43)), (32,(217,173,51)), (18,(33,33,43)), (10,(217,173,51))]:
        pygame.draw.circle(screen, col, (cx, cy), r)

    # KK initials
    f_kk = pygame.font.SysFont('Arial', 12, bold=True)
    kk = f_kk.render("KK", True, (20, 20, 26))
    screen.blit(kk, (cx - kk.get_width()//2, cy - kk.get_height()//2))

    # ── CORNER DECORATIONS ──
    gold = (217, 173, 51)
    pygame.draw.lines(screen, gold, False, [(W-120,85),(W-52,85),(W-52,130)], 2)
    pygame.draw.lines(screen, gold, False, [(W-120,H-85),(W-52,H-85),(W-52,H-130)], 2)

    # ── DOTS top right ──
    for i in range(5):
        pygame.draw.circle(screen, gold, (W-170+i*22, 62), 5)

    # ── NAME ──
    f_name = pygame.font.SysFont('Arial', 30, bold=True)
    screen.blit(f_name.render("KWENDA KUMBIRAYI", True, (217,173,51)), (130, 100))

    # ── TITLE ──
    f_title = pygame.font.SysFont('Arial', 17)
    screen.blit(f_title.render("Student  |  Developer", True, (180,180,210)), (132, 142))

    # ── UNIVERSITY ──
    f_uni = pygame.font.SysFont('Arial', 14)
    screen.blit(f_uni.render("Great Zimbabwe University", True, (140,140,170)), (132, 168))

    # ── DIVIDER ──
    pygame.draw.line(screen, gold, (130, 202), (W-55, 202), 1)

    # ── CONTACT LABEL ──
    f_label = pygame.font.SysFont('Arial', 11, bold=True)
    screen.blit(f_label.render("C O N T A C T", True, gold), (132, 210))

    # ── CONTACT DETAILS ──
    f_info = pygame.font.SysFont('Arial', 14)

    # Email
    pygame.draw.circle(screen, gold, (143, 245), 7)
    pygame.draw.circle(screen, (33,33,43), (143, 245), 4)
    screen.blit(f_info.render("mrkkwenda@gmail.com", True, (210,210,230)), (158, 237))

    # Phone
    pygame.draw.circle(screen, gold, (143, 275), 7)
    pygame.draw.circle(screen, (33,33,43), (143, 275), 4)
    screen.blit(f_info.render("+263 772 118 491", True, (210,210,230)), (158, 267))

    # GitHub
    pygame.draw.circle(screen, gold, (143, 305), 7)
    pygame.draw.circle(screen, (33,33,43), (143, 305), 4)
    screen.blit(f_info.render("github.com/toxxy7", True, (210,210,230)), (158, 297))

    # ── MODULE TAG ──
    f_mod = pygame.font.SysFont('Arial', 11)
    screen.blit(f_mod.render("ISH407 / HCS411 — Computer Graphics  |  GZU", True, (90,90,110)), (130, H-68))

    # ── CARD BORDER ──
    pygame.draw.rect(screen, gold, pygame.Rect(40, 40, W-80, H-80), 2, border_radius=12)

# ── MAIN LOOP ──
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    draw_card()
    pygame.display.flip()
    clock.tick(60)