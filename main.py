import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        starship = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        starship.draw(screen)
        pygame.display.flip()
        clock.tick(60) / 1000


if __name__ == "__main__":
    main()
