import pygame
import os

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))

class Base:
    WIDTH = BASE_IMG.get_width()
    VEL = 5 
    IMG = BASE_IMG


    def __init__(self, y, img):
        self.y = y 
        self.x1 = 0
        self.x2 = self.WIDTH 


    # Base continually loops right to left then returns to right and repeats
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMG, (self.x1, self.y))
        screen.blit(self.IMG, (self.x2, self.y))