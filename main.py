import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import * 
from Shot import *

#global variables
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, bullets)

player_obj= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
asteroid_field_obj = AsteroidField()

def display_screen():
    global dt
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)
            
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player_obj):
                print("Game over!")
                return
            for bullet in bullets:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()

        dt = clock.tick(60) / 1000
        print(dt)
        pygame.display.flip()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    display_screen()

if __name__ == "__main__":
    main()