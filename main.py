import os
os.environ["SDL_VIDEODRIVER"] = "x11"
import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0,0,0)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, shots)
    asteroidfield = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000 #print(f"Delta time: {dt}")    
        screen.fill(black)
        for sprite in updatable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.collisions(player):
                print("Game over!")
                sys.exit()   
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        #pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50)) #RED SQUARE TEST ON XSERVER SCREEN
        pygame.display.flip()
        
if __name__ == "__main__":
    main()