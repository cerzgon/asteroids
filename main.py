# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *

def main():
    # Initialize Pygame
    pygame.init()

    # Create a surface (e.g., 1280x720 pixels)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the window title (optional, but helpful)
    pygame.display.set_caption("Asteroids Game")

    # Create a clock object to manage fps
    clock = pygame.time.Clock()

    # Initialize delta time (dt) variable
    dt = 0

    # create player here (before the loop)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Start the game loop
    running = True
    while running:
        # Process events (such as closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the loop and close the game


        # Update game state
        player.update(dt)

        # Fill the screen with black color, RGB or "color"
        screen.fill("black")

        # draw player here (inside loop)
        player.draw(screen)

        # Refresh the screen with the latest updates
        pygame.display.flip()


        # Call clock.tick() to limit the frame rate to 60 FPS
        # dt will store the time that passed since the last frame in seconds
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    # Quit Pygame when the game loop finishes
    pygame.quit()

# This ensures that main() is only called when the file is executed directly,
# and not when it is imported as a module

if __name__ == "__main__":
    main()
