# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()

    # Create a surface (e.g., 1280x720 pixels)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the window title (optional, but helpful)
    pygame.display.set_caption("Asteroids Game")

    # Start the game loop
    running = True
    while running:
        # Process events (such as closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the loop and close the game

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Refresh the screen with the latest updates
        pygame.display.flip()

    # Quit Pygame when the game loop finishes
    pygame.quit()

# This ensures that main() is only called when the file is executed directly,
# and not when it is imported as a module

if __name__ == "__main__":
    main()
