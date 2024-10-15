from constants import *
from circleshape import CircleShape
import pygame

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.velocity = pygame.Vector2(0, 0)

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
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def update(self, dt):
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
      self.rotate(dt)
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
      self.rotate(-dt)

    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
      self.move(dt)
    elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
      self.move(-dt)

    self.position += self.velocity

