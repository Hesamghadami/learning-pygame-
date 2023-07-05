import pygame, sys 
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Game')
window.fill((255,255,255))

while True:
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

