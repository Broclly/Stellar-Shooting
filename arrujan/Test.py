import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
clock.tick(60)

def main_menu():
    screen.fill(WHITE)
    screen.blit(start_button_image, START_BUTTON_RECT)
    screen.blit(controls_button_image, CONTROLS_BUTTON_RECT)

    if pygame.event == []:
        print() # WIP

    pygame.display.flip()

