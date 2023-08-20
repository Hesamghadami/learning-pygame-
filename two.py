import pygame, sys 
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Game')
window.fill((255,255,255))



# pygame.draw.rect(window, (0,0,0), (20,20,60,90))
# pygame.draw.circle(window, (0,0,0), (300, 300),70, 1)
# pygame.draw.ellipse(window, (0,0,0), (80,80,200,120), 0)
# pygame.draw.polygon(window, (0,0,0), ((70,20),(290,400),(470, 360),(523,289)),1)
# pygame.draw.line(window, (0,0,0), (5,5),(250,342),1)
# pygame.draw.lines(window, (0,0,0), True,((70,20),(290,400),(470, 360),(1,1)), 1)





while True:
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

