import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        super().__init__(x, y, radius)  # Invisible circle for collision detection
        self.velocity = pygame.Vector2(1, 1)

    def draw(self, screen):
        if screen is None:
            raise ValueError("Screen cannot be None")
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2,
        )
    def update(self, dt):
        if dt is None:
            raise ValueError("dt cannot be None")
        self.position += self.velocity * dt
# Update the rect position for collision detection
