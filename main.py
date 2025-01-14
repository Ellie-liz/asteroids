import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    #set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set framerate
    time_clock = pygame.time.Clock()
    dt = 0

    #initialize groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #add Player Shot Asteroid and AsteroidField class to groups
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #initialize player and asteroidfield object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        #update all updatables
        for updatee in updatable:
            updatee.update(dt)

        #render all drawables
        for drawee in drawable:
            drawee.draw(screen)

        #check for collisions
        for roid in asteroids:
            if roid.check_collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if roid.check_collision(shot):
                    shot.kill()
                    roid.split()

        pygame.display.flip()
        dt = (time_clock.tick(60) / 1000)
        
if __name__ == "__main__":
    main()