import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):

    containers = ()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        super().__init__(x, y, self.radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 