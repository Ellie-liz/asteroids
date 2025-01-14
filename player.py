#import pygame
from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.cooldown_timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        foward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += foward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            #rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:
            #move foward
            self.move(dt)
        if keys[pygame.K_s]:
            #move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer == 0:
                self.shoot(dt)
        
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
        elif self.cooldown_timer < 0:
            self.cooldown_timer = 0

    
    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt