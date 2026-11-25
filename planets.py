import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1000, 1000))
SCREEN.fill((0, 0, 0))

count = 0

running = True
while running:
    count = count + 1
    pygame.draw.circle(SCREEN, (155, 155, 0), (200, 500), 100)

    pygame.display.update()
    
    if count > 100000:
        print("done")
        running = False