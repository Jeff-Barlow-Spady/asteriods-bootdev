import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    try:
        print("Starting asteroids!")
        print("Screen width:", SCREEN_WIDTH)
        print("Screen height:", SCREEN_HEIGHT)
        dt = 0
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x, y)
        astro = AsteroidField()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")
        clock = pygame.time.Clock()

        # Create sprite groups
        updateable_asteroids = pygame.sprite.Group()
        drawable = pygame.sprite.Group(player)
        updateable = pygame.sprite.Group(player, astro)

        # Set containers for Asteroid and AsteroidField
        Asteroid.containers = drawable, updateable_asteroids, updateable
        AsteroidField.containers = updateable_asteroids

        # Example instantiation of an Asteroid object
        asteroid = Asteroid(100, 150, 20)  # Provide x, y, and radius
        updateable_asteroids.add(asteroid)
        drawable.add(asteroid)

        running = True

        while running:
            screen.fill((0, 0, 0))
            drawable.draw(screen)
            updateable.update(dt)
            updateable_asteroids.update(dt)
            updateable_asteroids.draw(screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys:
                dt = clock.tick(60) / 1000
            else:
                dt = 0

    except Exception as e:
          print("An error occurred:", e)

if __name__ == "__main__":
    main()