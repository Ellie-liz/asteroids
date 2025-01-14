import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        trajectory = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(trajectory)
        vector_2 = self.velocity.rotate(-trajectory)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = vector_1 * 1.2
        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2.velocity = vector_2 * 1.2