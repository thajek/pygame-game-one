# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Define some constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define some color constants
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set up the drawing window with out defined width and height
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

# Start out main loop running
running = True
while running:

    # Check to see if the user clicked the close button on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with a color
    screen.fill(BLUE)

    # Draw a circle in the center
    pygame.draw.circle(screen, RED, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2), 75)

    # Flip the display, nothing displays above until this is called
    pygame.display.flip()


