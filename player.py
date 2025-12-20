import pygame
from constants import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    COLOR_WHITE,
    PLAYER_SHOOT_SPEED,
)
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, COLOR_WHITE, self.triangle(), LINE_WIDTH)

    def rotate(self, direction, dt):
        self.rotation += direction * dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, direction, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * direction * dt * PLAYER_SPEED

    def shoot(self):
        if self.shoot_cooldown > 0:
            return None
        else:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
