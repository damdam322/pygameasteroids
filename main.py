import pygame
from constants import *
from player import *

#global variables
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

def display_screen():
    global dt
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
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