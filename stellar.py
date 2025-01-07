import pygame
import assets.python
import assets.python.player
import assets.python.prefabs

rect_prefab = assets.python.prefabs.rectangles
player_data = assets.python.player.Player()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.draw.rect(screen, (255,255,255),(200,50,200,100))
        pygame.draw.rect(screen, (255,0,0), (player_data.location,rect_prefab[0]))
    pygame.display.flip()
clock.tick(60)  # limits FPS to 60
pygame.quit()