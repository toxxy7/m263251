import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame.font

def draw_text(x, y, text):
    font = pygame.font.SysFont('Arial', 14, bold=True)
    surface = font.render(text, True, (255, 255, 0))
    data = pygame.image.tostring(surface, 'RGBA', True)
    glWindowPos2f(x, y)
    glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)

def draw_primitives():
    # ── GL_POINTS ──
    glColor3f(1, 1, 1)
    glPointSize(6)
    glBegin(GL_POINTS)
    glVertex2f(-0.85, 0.75)
    glVertex2f(-0.75, 0.85)
    glVertex2f(-0.65, 0.75)
    glVertex2f(-0.75, 0.65)
    glEnd()

    # ── GL_LINES ──
    glColor3f(1, 0.5, 0)
    glBegin(GL_LINES)
    glVertex2f(-0.45, 0.70); glVertex2f(-0.25, 0.90)
    glVertex2f(-0.40, 0.90); glVertex2f(-0.20, 0.70)
    glEnd()

    # ── GL_LINE_STRIP ──
    glColor3f(0, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.00, 0.70)
    glVertex2f(0.10, 0.90)
    glVertex2f(0.20, 0.70)
    glVertex2f(0.30, 0.90)
    glEnd()

    # ── GL_LINE_LOOP ──
    glColor3f(1, 0, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.55, 0.70)
    glVertex2f(0.65, 0.90)
    glVertex2f(0.75, 0.70)
    glVertex2f(0.85, 0.90)
    glEnd()

    # ── GL_TRIANGLES ──
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.85, 0.20)
    glVertex2f(-0.65, 0.50)
    glVertex2f(-0.45, 0.20)
    glEnd()

    # ── GL_TRIANGLE_STRIP ──
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(-0.30, 0.20)
    glVertex2f(-0.20, 0.50)
    glVertex2f(-0.10, 0.20)
    glVertex2f(0.00, 0.50)
    glVertex2f(0.10, 0.20)
    glEnd()

    # ── GL_TRIANGLE_FAN ──
    glColor3f(0, 0.5, 1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.40, 0.35)  # center
    glVertex2f(0.30, 0.20)
    glVertex2f(0.40, 0.15)
    glVertex2f(0.55, 0.20)
    glVertex2f(0.60, 0.35)
    glVertex2f(0.55, 0.50)
    glVertex2f(0.40, 0.55)
    glEnd()

    # ── GL_QUADS ──
    glColor3f(1, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(-0.85, -0.30)
    glVertex2f(-0.85, -0.05)
    glVertex2f(-0.60, -0.05)
    glVertex2f(-0.60, -0.30)
    glEnd()

    # ── GL_QUAD_STRIP ──
    glColor3f(1, 0.4, 0.7)
    glBegin(GL_QUAD_STRIP)
    glVertex2f(-0.40, -0.30)
    glVertex2f(-0.40, -0.05)
    glVertex2f(-0.20, -0.30)
    glVertex2f(-0.20, -0.05)
    glVertex2f(0.00, -0.30)
    glVertex2f(0.00, -0.05)
    glEnd()

    # ── GL_POLYGON ──
    glColor3f(0.5, 1, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(0.30, -0.05)
    glVertex2f(0.50, -0.05)
    glVertex2f(0.65, -0.18)
    glVertex2f(0.55, -0.30)
    glVertex2f(0.30, -0.30)
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 700), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL Primitives - GZU Assignment")

    glClearColor(0.1, 0.1, 0.15, 1.0)
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
        draw_primitives()

        # Draw labels
        draw_text(55,  630, "GL_POINTS")
        draw_text(230, 630, "GL_LINES")
        draw_text(410, 630, "GL_LINE_STRIP")
        draw_text(590, 630, "GL_LINE_LOOP")
        draw_text(40,  390, "GL_TRIANGLES")
        draw_text(220, 390, "GL_TRIANGLE_STRIP")
        draw_text(430, 390, "GL_TRIANGLE_FAN")
        draw_text(40,  150, "GL_QUADS")
        draw_text(230, 150, "GL_QUAD_STRIP")
        draw_text(510, 150, "GL_POLYGON")

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()