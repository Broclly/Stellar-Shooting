import pygame 
from pygame.locals import *
import assets
import assets.python
import assets.python.player 

pygame.init()

screen = pygame.display.set_mode((640, 480))

BLACK = [0, 0, 0]
RED = [100, 0, 0]

player_width = 10
player_height = 20

player_x = 320
player_y = 240

player_speed = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[K_w]: 
        player_y -= player_speed
    if keys[K_s]:  
        player_y += player_speed
    if keys[K_a]:  
        player_x -= player_speed
    if keys[K_d]:  
        player_x += player_speed
