import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the circle properties
circle_color = (255, 0, 0) # Red color
circle_position = (200, 200) # Center position
circle_radius = 50 # Radius size

# Draw the circle on the screen
pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

# Update the display
pygame.display.update()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

