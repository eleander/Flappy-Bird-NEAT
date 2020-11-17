import pygame
import neat
import time
import os
import random
from Bird import Bird

# Screen dimensions
WIDTH = 550
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


def draw_screen(screen, bird):
    SCREEN.blit(BG_IMG, (0,0))
    bird.draw(screen)

    pygame.display.update()



running = True
clock = pygame.time.Clock()

bird = Bird(200,200)

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
            break
    # bird.move()
    draw_screen(SCREEN, bird)