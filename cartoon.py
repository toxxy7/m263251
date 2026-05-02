import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_circle_filled(cx, cy, r, segments=60):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex2f(cx + r * math.cos(angle), cy + r * math.sin(angle))
    glEnd()

def draw_circle_outline(cx, cy, r, segments=60):
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        glVertex2f(cx + r * math.cos(angle), cy + r * math.sin(angle))
    glEnd()

def draw_ellipse_filled(cx, cy, rx, ry, segments=60):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        glVertex2f(cx + rx * math.cos(angle), cy + ry * math.sin(angle))
    glEnd()

def draw_rect(x1, y1, x2, y2):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()

def draw_text(x, y, text, size=16, color=(255, 255, 255)):
    font = pygame.font.SysFont('Arial', size, bold=True)
    surface = font.render(text, True, color)
    data = pygame.image.tostring(surface, 'RGBA', True)
    glWindowPos2f(x, y)
    glDrawPixels(surface.get_width(), surface.get_height(),
                 GL_RGBA, GL_UNSIGNED_BYTE, data)

def draw_scene():

    # ── BACKGROUND (wooden wall - warm brown) ──
    glColor3f(0.72, 0.48, 0.28)
    draw_rect(-1, -1, 1, 1)

    # Wood grain lines
    glColor3f(0.62, 0.40, 0.22)
    glLineWidth(1.5)
    for y in [-0.6, -0.2, 0.2, 0.6]:
        glBegin(GL_LINES)
        glVertex2f(-1, y)
        glVertex2f(1, y)
        glEnd()

    # ── DESK (wooden table) ──
    glColor3f(0.60, 0.38, 0.18)
    draw_rect(-1, -1, 1, -0.40)

    # Desk top edge highlight
    glColor3f(0.75, 0.55, 0.30)
    draw_rect(-1, -0.42, 1, -0.38)

    # ── LAPTOP (gold/silver on desk) ──
    # Laptop base
    glColor3f(0.75, 0.65, 0.45)
    glBegin(GL_POLYGON)
    glVertex2f(-0.45, -0.42)
    glVertex2f( 0.35, -0.42)
    glVertex2f( 0.30, -0.58)
    glVertex2f(-0.40, -0.58)
    glEnd()

    # Laptop screen
    glColor3f(0.70, 0.60, 0.40)
    glBegin(GL_POLYGON)
    glVertex2f(-0.38, -0.42)
    glVertex2f( 0.10, -0.42)
    glVertex2f( 0.05, -0.10)
    glVertex2f(-0.42, -0.10)
    glEnd()

    # Laptop screen display (blue glow)
    glColor3f(0.50, 0.65, 0.85)
    glBegin(GL_POLYGON)
    glVertex2f(-0.34, -0.40)
    glVertex2f( 0.06, -0.40)
    glVertex2f( 0.02, -0.13)
    glVertex2f(-0.38, -0.13)
    glEnd()

    # Laptop logo
    glColor3f(0.85, 0.75, 0.50)
    draw_circle_filled(-0.16, -0.27, 0.04)

    # ── BODY - Blue dress shirt ──
    glColor3f(0.40, 0.58, 0.85)
    glBegin(GL_POLYGON)
    glVertex2f(-0.55, -0.42)
    glVertex2f( 0.55, -0.42)
    glVertex2f( 0.45,  0.10)
    glVertex2f( 0.18,  0.30)
    glVertex2f(-0.18,  0.30)
    glVertex2f(-0.45,  0.10)
    glEnd()

    # Shirt collar left
    glColor3f(0.55, 0.72, 0.95)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.18, 0.30)
    glVertex2f(-0.05, 0.18)
    glVertex2f( 0.00, 0.30)
    glEnd()

    # Shirt collar right
    glBegin(GL_TRIANGLES)
    glVertex2f( 0.18, 0.30)
    glVertex2f( 0.05, 0.18)
    glVertex2f( 0.00, 0.30)
    glEnd()

    # Shirt pocket
    glColor3f(0.35, 0.52, 0.80)
    draw_rect(0.12, 0.00, 0.28, 0.15)

    # ── DARK TIE ──
    glColor3f(0.20, 0.22, 0.28)
    glBegin(GL_POLYGON)
    glVertex2f(-0.03, 0.28)
    glVertex2f( 0.03, 0.28)
    glVertex2f( 0.06, 0.00)
    glVertex2f( 0.00, -0.15)
    glVertex2f(-0.06, 0.00)
    glEnd()

    # Tie knot
    glColor3f(0.25, 0.27, 0.33)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.03, 0.28)
    glVertex2f( 0.03, 0.28)
    glVertex2f( 0.00, 0.20)
    glEnd()

    # Tie stripe detail
    glColor3f(0.30, 0.32, 0.40)
    glBegin(GL_LINES)
    glVertex2f(0.00, 0.18)
    glVertex2f(0.03, -0.05)
    glEnd()

    # ── LEFT ARM (raised - holding phone) ──
    glColor3f(0.40, 0.58, 0.85)
    glBegin(GL_POLYGON)
    glVertex2f(-0.18, 0.25)
    glVertex2f(-0.30, 0.25)
    glVertex2f(-0.45, 0.55)
    glVertex2f(-0.35, 0.60)
    glEnd()

    # ── RIGHT ARM (on laptop) ──
    glColor3f(0.40, 0.58, 0.85)
    glBegin(GL_POLYGON)
    glVertex2f( 0.18, 0.10)
    glVertex2f( 0.45, 0.10)
    glVertex2f( 0.50, -0.10)
    glVertex2f( 0.28, -0.10)
    glEnd()

    # ── HANDS (dark skin) ──
    glColor3f(0.25, 0.17, 0.10)
    # Left hand holding phone
    draw_ellipse_filled(-0.38, 0.62, 0.06, 0.05)
    # Right hand on laptop
    draw_ellipse_filled(0.46, -0.12, 0.07, 0.04)

    # ── PHONE ──
    glColor3f(0.15, 0.15, 0.18)
    draw_rect(-0.36, 0.60, -0.28, 0.80)
    glColor3f(0.30, 0.30, 0.35)
    draw_rect(-0.35, 0.62, -0.29, 0.78)

    # ── NECK ──
    glColor3f(0.25, 0.17, 0.10)
    draw_rect(-0.06, 0.28, 0.06, 0.40)

    # ── HEAD (dark skin) ──
    glColor3f(0.25, 0.17, 0.10)
    draw_ellipse_filled(0.0, 0.60, 0.22, 0.26)

    # ── SHORT LOW CUT HAIR ──
    glColor3f(0.08, 0.05, 0.02)
    draw_ellipse_filled(0.0, 0.76, 0.22, 0.12)
    # Side hair fade
    draw_ellipse_filled(-0.20, 0.63, 0.05, 0.12)
    draw_ellipse_filled( 0.20, 0.63, 0.05, 0.12)

    # ── EARS ──
    glColor3f(0.22, 0.15, 0.09)
    draw_ellipse_filled(-0.22, 0.58, 0.04, 0.06)
    draw_ellipse_filled( 0.22, 0.58, 0.04, 0.06)

    # ── EYES (focused/serious - looking down slightly) ──
    # Eye whites
    glColor3f(0.95, 0.92, 0.88)
    draw_ellipse_filled(-0.08, 0.60, 0.05, 0.03)
    draw_ellipse_filled( 0.08, 0.60, 0.05, 0.03)

    # Pupils (looking slightly downward)
    glColor3f(0.08, 0.05, 0.02)
    draw_circle_filled(-0.08, 0.585, 0.022)
    draw_circle_filled( 0.08, 0.585, 0.022)

    # Eye shine
    glColor3f(1, 1, 1)
    draw_circle_filled(-0.075, 0.592, 0.006)
    draw_circle_filled( 0.085, 0.592, 0.006)

    # ── EYEBROWS (slightly furrowed - serious look) ──
    glColor3f(0.08, 0.05, 0.02)
    glLineWidth(3.0)
    # Left brow - slightly angled down toward center
    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.13, 0.660)
    glVertex2f(-0.08, 0.655)
    glVertex2f(-0.03, 0.658)
    glEnd()
    # Right brow
    glBegin(GL_LINE_STRIP)
    glVertex2f( 0.03, 0.658)
    glVertex2f( 0.08, 0.655)
    glVertex2f( 0.13, 0.660)
    glEnd()

    # ── NOSE (broad) ──
    glColor3f(0.20, 0.13, 0.08)
    draw_ellipse_filled( 0.00, 0.56, 0.03, 0.02)
    draw_ellipse_filled(-0.03, 0.555, 0.018, 0.015)
    draw_ellipse_filled( 0.03, 0.555, 0.018, 0.015)

    # ── MOUTH (neutral/serious - straight line) ──
    glColor3f(0.18, 0.10, 0.07)
    glLineWidth(2.5)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.05, 0.508)
    glVertex2f( 0.00, 0.505)
    glVertex2f( 0.05, 0.508)
    glEnd()

    # Slight lip definition
    glColor3f(0.22, 0.14, 0.09)
    draw_ellipse_filled(0.0, 0.515, 0.045, 0.012)

    # ── BEARD STUBBLE (subtle) ──
    glColor3f(0.12, 0.08, 0.04)
    draw_ellipse_filled(0.0, 0.505, 0.08, 0.04)

    # ── PENS ON DESK ──
    # Blue pen
    glColor3f(0.10, 0.20, 0.80)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(-0.70, -0.50)
    glVertex2f(-0.50, -0.45)
    glEnd()
    # Green pen tip
    glColor3f(0.10, 0.80, 0.20)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(-0.72, -0.50)
    glVertex2f(-0.68, -0.50)
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 800), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("2D Cartoon Kwenda K - M263251")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)
        draw_scene()

        draw_text(180, 15, "Kwenda K - M263251", 15, (255, 230, 150))
        draw_text(220, 38, "2D Cartoon Character", 15, (255, 230, 150))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()