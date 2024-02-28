import pygame

WIDTH = 800
HEIGHT = 1600

pygame.init()

SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))

count = 0
playing = True
while playing:
    count = count + 1
    pygame.draw.rect(SURFACE, "blue", (200, 100, 50, 100))
    pygame.draw.circle(SURFACE, "red", (10, 10), 5)
    pygame.draw.polygon(SURFACE, "yellow", [(0, 300), (0, 450), (200, 375)])
    pygame.display.flip()


