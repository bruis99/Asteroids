import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) #2 is width of asteroid lines aka thickness
    
    def update(self, dt):
        self.position += self.velocity * dt