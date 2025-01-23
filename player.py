import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.shots = shots_group


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = shot_velocity
        self.shots.add(new_shot)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:   
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
            

