import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PIXELS_PER_METER = 50  # 100 pixels = 1 meter
BACKGROUND_COLOR = (0, 0, 0)  # Black background
OBJECT_COLOR = (255, 255, 255)  # White object
AXIS_COLOR = (128, 128, 128)  # Gray axis color
SQUARE_COLOR = (255, 0, 0)  # Red square color
SQUARE_SIZE = 20  # Size of the red square
FALLING_BOX_COLOR = (0, 0, 255)  # Blue falling box color
FALLING_BOX_SIZE = 20  # Size of the falling box

# User-defined speed (in meters per second)
speed = float(input("Enter the speed (in meters per second): "))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Coordinate System")

# Calculate the center of the screen
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Main object coordinates (center of the screen)
main_object_x, main_object_y = center_x, center_y

# Variables for the red square
show_square = False
square_pos = (0, 0)
square_timer = 0

# Variables for the falling box
falling_box_pos = (0, 0)
falling_box_speed = speed * PIXELS_PER_METER  # Convert user speed to pixels per second
falling_box_falling = False

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
                relative_x = (click_x - main_object_x) / PIXELS_PER_METER
                relative_y = (main_object_y - click_y) / PIXELS_PER_METER
                distance = math.hypot(relative_x, relative_y)
                time_to_reach = distance / speed
                print(f"Relative to main object: ({relative_x:.2f} meters, {relative_y:.2f} meters), "
                      f"Distance: {distance:.2f} meters, Time to reach: {time_to_reach:.2f} seconds")

                if abs(relative_y) >= 5.0:  # Check if the click is 5000 pixels above or below the axis
                    falling_box_pos = (click_x, click_y)
                    falling_box_falling = True

                square_pos = (click_x, click_y)
                show_square = True
                square_timer = pygame.time.get_ticks()

    pygame.draw.line(screen, AXIS_COLOR, (0, main_object_y), (WIDTH, main_object_y), 2)  # X-axis
    pygame.draw.line(screen, AXIS_COLOR, (main_object_x, 0), (main_object_x, HEIGHT), 2)  # Y-axis
    pygame.draw.circle(screen, OBJECT_COLOR, (main_object_x, main_object_y), 10)

    if show_square:
        pygame.draw.rect(screen, SQUARE_COLOR, (square_pos[0] - SQUARE_SIZE // 2, square_pos[1] - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))
        current_time = pygame.time.get_ticks()
        if current_time - square_timer >= 5000:
            show_square = False

    if falling_box_falling:
        falling_box_pos = (falling_box_pos[0], falling_box_pos[1] + falling_box_speed / 30)  # Move the box down
        pygame.draw.rect(screen, FALLING_BOX_COLOR, (falling_box_pos[0] - FALLING_BOX_SIZE // 2, falling_box_pos[1] - FALLING_BOX_SIZE // 2, FALLING_BOX_SIZE, FALLING_BOX_SIZE))

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
