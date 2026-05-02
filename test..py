import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Test")

font = pygame.font.SysFont('Arial', 30, bold=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    text = font.render("Hello Kwenda!", True, (255, 215, 0))
    screen.blit(text, (50, 80))
    pygame.display.flip()

pygame.quit()