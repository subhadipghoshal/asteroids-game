import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def run():
    # Game loop and logic would go here
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        pygame.display.flip()


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen dimensions: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    run()


if __name__ == "__main__":
    main()
