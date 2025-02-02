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

    # Create a clock object to manage fps
    clock = pygame.time.Clock()

    # Set the window title (optional, but helpful)
    pygame.display.set_caption("Asteroids Game")

     # a group where all objects can be updated
    updatable = pygame.sprite.Group()

    # a group where all objects can be drawn
    drawable = pygame.sprite.Group()

    # set the Player.containers
    Player.containers = (updatable, drawable)

    # create player instance here (before the loop)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Initialize delta time (dt) variable
    dt = 0

    # Start the game loop
    running = True
    while running:
        # Process events (such as closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the loop and close the game


        # Update game state
        updatable.update(dt) # change from player.update(dt) to updatable - group

        # Fill the screen with black color, RGB or "color"
        screen.fill("black")

        #  change from draw player here (inside loop) to draw all sprites
        # change from player.draw(dt) to drawable - group

        # Draw all sprites using their custom draw methods
        for obj in drawable:
            obj.draw(screen)

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
