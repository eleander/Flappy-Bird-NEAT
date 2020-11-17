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


# Loading all required images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
               pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
               pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))


def draw_screen(screen, bird):
    SCREEN.blit(BG_IMG, (0,0))
    bird.draw(screen)

    pygame.display.update()



running = True
clock = pygame.time.Clock()

bird = Bird(200,200, BIRD_IMGS)

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