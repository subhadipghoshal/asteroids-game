import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS_TO_SPLIT, LINE_WIDTH, COLOR_WHITE
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        log_event("asteroid_split")
        self.kill()
        if (
            self.radius > ASTEROID_MIN_RADIUS_TO_SPLIT
        ):  # Minimum size to split # Minimum size to split
            new_radius = self.radius - ASTEROID_MIN_RADIUS_TO_SPLIT
            rotation_angle = random.uniform(20, 50)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            # Assign random velocities to the new asteroids
            asteroid1.velocity = self.velocity.rotate(rotation_angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(-rotation_angle) * 1.2
