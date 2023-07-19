import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

window=pygame.display.set_mode((500,500))
window.fill((0,0,0))

x=0
y=0
pygame.draw.rect(window,(255,255,255),(x,y,50,50),0)

while True:
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        x += 40
        pygame.draw.rect(window,(0,255,255),(x,y,50,50),0)

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()