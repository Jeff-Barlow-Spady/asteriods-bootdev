import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PLAYER_RADIUS * 2, PLAYER_RADIUS * 2])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            direction = pygame.Vector2(0, -1).rotate(self.rotation)
            self.velocity += direction * PLAYER_SPEED * dt

        self.position += self.velocity
        self.rect.center = self.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)