import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    containers = ()

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20, 50)
        asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_one.velocity.x *= 1.2 
        asteroid_one.velocity.y *= 1.2
        asteroid_one.velocity = self.velocity.rotate(random_angle)
        asteroid_two.velocity = self.velocity.rotate(-random_angle)
        self.kill()
        return
        