import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes")

# Define colors
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

# Main loop
running = True
while running:
    screen.fill((0,0,0))  # Fill the screen with white background
    
    # Purple Line: Define starting and ending coordinates, and thickness
    pygame.draw.line(screen, PURPLE, (100, 100), (700, 100), 5)
    
    # Orange Square: Define position and size using pygame.Rect
    pygame.draw.rect(screen, ORANGE, pygame.Rect(500, 250, 75, 75))
    
    # Yellow Polygon: Define points for the triangle
    pygame.draw.polygon(screen, YELLOW, [(300, 500), (500, 500), (400, 350)])
    
    # Update the screen display
    pygame.display.flip()
    
    # Check for events to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
