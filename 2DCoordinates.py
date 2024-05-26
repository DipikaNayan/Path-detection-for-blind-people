import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
OBJECT_COLOR = (255, 255, 255)  # White object
AXIS_COLOR = (128, 128, 128)  # Gray axis color
SQUARE_COLOR = (255, 0, 0)  # Red square color
SQUARE_SIZE = 20  # Size of the red square

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Coordinate System")

# Calculate the center of the screen
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Main object coordinates (center of the screen)
main_object_x, main_object_y = center_x, center_y

# Variables for the red square
red_square_x, red_square_y = 0, 0  # Initialize off-screen
show_red_square = False
red_square_timer = 0

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                click_x, click_y = event.pos
                # Calculate relative coordinates from the main object's position (center)
                relative_x = click_x - main_object_x
                relative_y = main_object_y - click_y  # Invert y because pygame's y-axis is inverted
                print(f"Relative to main object: ({relative_x}, {relative_y})")

                # Set the position of the red square and show it
                red_square_x, red_square_y = click_x, click_y
                show_red_square = True
                red_square_timer = 5 * 60  # 5 seconds (assuming 60 FPS)

    # Decrement the timer and hide the red square after 5 seconds
    if red_square_timer > 0:
        red_square_timer -= 0.5
    else:
        show_red_square = False

    # Draw X and Y axes passing through the main object's center
    pygame.draw.line(screen, AXIS_COLOR, (0, main_object_y), (WIDTH, main_object_y), 2)  # X-axis
    pygame.draw.line(screen, AXIS_COLOR, (main_object_x, 0), (main_object_x, HEIGHT), 2)  # Y-axis

    # Draw the main object at the center of the screen
    pygame.draw.circle(screen, OBJECT_COLOR, (main_object_x, main_object_y), 10)

    # Draw the red square if it's visible
    if show_red_square:
        pygame.draw.rect(screen, SQUARE_COLOR, (red_square_x - SQUARE_SIZE // 2, red_square_y - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
