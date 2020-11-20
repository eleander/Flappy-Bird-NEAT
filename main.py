import pygame
import neat
import time
import os
import random
from Bird import Bird
from Base import Base
from Pipe import Pipe
pygame.font.init()


# Screen dimensions
WIDTH = 550
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

def draw_screen(screen, bird, pipes, base, score):
    SCREEN.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(screen)
    bird.draw(screen)
    base.draw(screen)
    text = SCORE_FONT.render("Score: "+str(score), 1, (255, 255, 255))
    SCREEN.blit(text,(WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()



running = True
clock = pygame.time.Clock()

score = 0
bird = Bird(230,350)
base = Base(730)
pipes = [Pipe(600)]

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
            break
    # bird.move()
    add_pipe = False
    removed_pipes = []
    for pipe in pipes:
        if pipe.collide(bird):
            pass

        # Pipe off screen
        if pipe.x + pipe.PIPE_TOP.get_width() < 0:
            removed_pipes.append(pipe)

        # Passed a pipe
        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            add_pipe = True
        pipe.move()

    # Passed a pipe so increase score and make a new pipe
    if add_pipe:
        score+=1
        pipes.append(Pipe(600))

    # Remove all pipes off screen
    for r in removed_pipes:
        pipes.remove(r)

    if bird.y + bird.img.get_height() >= 730:
        pass

    base.move()
    draw_screen(SCREEN, bird, pipes, base, score)