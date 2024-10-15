import pygame
from constants import *
from player import Player

def main():
    try:
        print("Starting asteroids!")
        print("Screen width:", SCREEN_WIDTH)
        print("Screen height:", SCREEN_HEIGHT)
        dt = 0
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x, y)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")
        clock = pygame.time.Clock()

        # Create sprite groups
        updateable = pygame.sprite.Group(player)
        Player.containers = (updateable,)

        running = True

        while running:
            screen.fill((0, 0, 0))
            player.draw(screen)  # Draw the player directly
            updateable.update(dt)
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