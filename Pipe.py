import random
import pygame

class Pipe:
    GAP = 200
    VEL = 5 

    def __init__(self,x, pipe_img):
        self.x = x 
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_BOTTOM = pipe_img
        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP
    
    def move(self):
        self.x -= self.VEL

    def draw(self, screen):
        screen.blit(self.PIPE_TOP, (self.x, self.top))
        screen.blit(self.PIPE_BOTTOM, (self.x, self.bottom))