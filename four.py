import pygame, sys 
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()
windowheight = 500
windowwidth = 500
window = pygame.display.set_mode((windowheight, windowwidth))
pygame.display.set_caption('Game')


gameicon= pygame.image.load('photo_2023-03-05_01-55-04.jpg')
pygame.display.set_icon(gameicon)

rectprimaryx= 100.0
rectprimaryy= 100.0

speedx = 0.01
speedy = 0.01

while True:
    window.fill((255,255,255))
    pygame.draw.rect(window, (0,0,0), (rectprimaryx,rectprimaryy,40,40))
    if rectprimaryx >= windowwidth:
        rectprimaryx = 0
    else:
        rectprimaryx += speedx
    if rectprimaryy >= windowheight:
        rectprimaryy = 0
    else:
        rectprimaryy += speedy
    
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()