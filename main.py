import pygame
import neat
import time
import os
import random
import pickle
from Bird import Bird
from Base import Base
from Pipe import Pipe
pygame.font.init()

# Screen dimensions
WIDTH = 550
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

GENERATION = 0

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

# Draw all objects/text onto the screen
def draw_screen(screen, birds, pipes, base, score, generation):
    SCREEN.blit(BG_IMG, (0,0))
    base.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    for bird in birds:
        bird.draw(screen)

    text = SCORE_FONT.render("Score: "+str(score), 1, (255, 255, 255))
    SCREEN.blit(text,(WIDTH - 10 - text.get_width(), 10))

    text = SCORE_FONT.render("Generation: "+str(generation), 1, (255, 255, 255))
    SCREEN.blit(text,(0, 10))

    pygame.display.update()

def main(genomes, config):
    global GENERATION
    GENERATION += 1
    nets = []
    ge = []
    birds = []

    # Loop through genomes (id, object)
    # Create population of birds
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g,config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)


    running = True
    clock = pygame.time.Clock()

    score = 0
    base = Base(730)
    pipes = [Pipe(600)]

    # Quit condition
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
                

        pipe_ind = 0
        # If pipe passed, then look at next pipe
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1 
        else:
            running = False
            break

        # For every second bird is alive, gets above clock.tick * 0.1
        for x,bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            # Should the bird jump?
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            if output[0] > 0.5:
                bird.jump()
        
        add_pipe = False
        removed_pipes = []
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    # If hit a pipe, then reduce fitness score
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x) 

                # Passed a pipe
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            # Pipe off screen, remove pipe
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                removed_pipes.append(pipe)
            pipe.move()

        # Passed a pipe so increase score and make a new pipe
        # and increase fitness a lot
        if add_pipe:
            score+=1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        # Remove all pipes off screen
        for r in removed_pipes:
            pipes.remove(r)

        # Remove bird if it touches the ground or goes above the screen
        for x,bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        # Store winning bird
        if score > 20:
            pickle.dump(nets[0],open("best.p", "wb"))
            break

        base.move()
        draw_screen(SCREEN, birds, pipes, base, score, GENERATION)

# Run using NEAT
def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run(main,50)

# Get config file path and pass to run(config_file)
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)

