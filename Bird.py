import pygame
import os

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

class Bird:
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5 

    def __init__(self,x,y):

        self.x = x 
        self.y = y 
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y 
        self.img_count = 0
        self.img = BIRD_IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        
        # d = displacement
        # Allows for an arch when jumping
        d = self.vel * self.tick_count + 1.5*self.tick_count**2

        # Terminal Velocity
        if d >= 16:
            d = 16

        # Height of jump
        if d < 0:
            d -= 2

        self.y = self.y + d

        # Bird moving upwards
        # Tilt up
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        # Bird moving downward
        # Tild down
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    

    # COME BACK; USE BETTER LOGIC
    def draw(self,screen):
        self.img_count += 1
        
        # Animation
        if self.img_count < self.ANIMATION_TIME:
            self.img = BIRD_IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = BIRD_IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = BIRD_IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = BIRD_IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = BIRD_IMGS[0]
            self.img_count = 0

        # Don't flap when going downwards
        # After going upwards again, bird should be flapping
        if self.tilt <= -80:
            self.img = BIRD_IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # Tilt the bird
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        screen.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)