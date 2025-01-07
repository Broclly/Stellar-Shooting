import pygame, sys, time

##########################################################################
#                               INITIALIZER                              #
##########################################################################

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

##########################################################################
#                               METHODS                                  #
##########################################################################

def main_menu():
    screen.fill(WHITE)
    screen.blit(start_button_image, START_BUTTON_RECT)
    screen.blit(controls_button_image, CONTROLS_BUTTON_RECT)
    pygame.display.flip()

def controls():
    screen.fill(WHITE)
    title_text = Text("CONTROLS:", 60, BLACK, (400, 100), font_type="Roboto/Roboto-Black.ttf")
    KEY_W_text = Text("W = Jump", 45, BLACK, (400, 200), font_type="Roboto/Roboto-Light.ttf")
    KEY_A_text = Text("A = Move Left", 45, BLACK, (400, 250), font_type="Roboto/Roboto-Light.ttf")
    KEY_S_text = Text("S = Crouch", 45, BLACK, (400, 300), font_type="Roboto/Roboto-Light.ttf")
    KEY_D_text = Text("D = Move Right", 45, BLACK, (400, 350), font_type="Roboto/Roboto-Light.ttf")
    title_text.draw(screen)
    KEY_W_text.draw(screen)
    KEY_A_text.draw(screen)
    KEY_S_text.draw(screen)
    KEY_D_text.draw(screen)
    pygame.display.flip()

def loading_screen():
    start_time = pygame.time.get_ticks()  # Get the starting time
    count_down = 3  # Start from 3

    while count_down > 0:
        screen.fill(BLACK)
        # Display the countdown number
        Text(f"{count_down}..", 60, WHITE, (400, 300), font_type="Roboto/Roboto-Black.ttf").draw(screen)
        
        pygame.display.flip()  # Update the screen
        
        # Wait for a second (or until a second has passed since start_time)
        while pygame.time.get_ticks() - start_time < 1000:  # 1000 milliseconds = 1 second
            pygame.event.pump()  # Make sure pygame events are handled (e.g., quitting)
        
        # Decrease the countdown
        count_down -= 1
        start_time = pygame.time.get_ticks()  # Reset start time for the next countdown
    
    # After the countdown ends, clear the screen (optional)
    screen.fill(BLACK)
    pygame.display.flip()

def game():
    loading_screen()
    state = MENU
    return state

##########################################################################
#                               CLASSES                                  #
##########################################################################

class Text:
    def __init__(self, text, font_size, color, position, font_type=None):
        """Creates a text object."""
        if font_type:
            self.font = pygame.font.Font(font_type, font_size)  # Use custom font
        else:
            self.font = pygame.font.Font(None, font_size)  # Default font
        self.text = text
        self.color = color
        self.position = position
        self.text_surface = self.font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect(center=position)

    def draw(self, surface):
        """Draws the text on the given surface."""
        surface.blit(self.text_surface, self.text_rect)

##########################################################################
#                          VARIABLES & METHODS                           #
##########################################################################

# SCREEN DIMENSIONS
SCREEN_LENGTH, SCREEN_WIDTH = 800, 600
BUTTON_LENGTH, BUTTON_WIDTH = 200, 50

# LOAD BUTTON IMAGES
start_button_image = pygame.image.load("start_button.png")
start_button_image = pygame.transform.scale(start_button_image, (BUTTON_LENGTH, BUTTON_WIDTH))
controls_button_image = pygame.image.load("controls_button.png")
controls_button_image = pygame.transform.scale(controls_button_image, (BUTTON_LENGTH, BUTTON_WIDTH))

# BUTTON RECTANGLES
START_BUTTON_RECT = start_button_image.get_rect(center=(SCREEN_LENGTH // 2, 225))
CONTROLS_BUTTON_RECT = controls_button_image.get_rect(center=(SCREEN_LENGTH // 2, 325))

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# GAME STATE
MENU = "menu"
CONTROLS = "controls"
RUNNING = "running"
state = MENU

# SPRITES
player = pygame.transform.scale(pygame.image.load("player.png"), (50, 20))

##########################################################################
#                                 GAME                                   #
##########################################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if state == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON_RECT.collidepoint(event.pos):  # Correct usage
                    state = RUNNING  # Transition to game state
                elif CONTROLS_BUTTON_RECT.collidepoint(event.pos):  # Correct usage
                    state = CONTROLS  # Transition to controls screen
        if state == CONTROLS:
            controls()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = MENU  # Transition back to the menu state
    
    if state == MENU:
        main_menu()

    if state == CONTROLS:
        controls()
    
    if state == RUNNING:
        state = game()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
