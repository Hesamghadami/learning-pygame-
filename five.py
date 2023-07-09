import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Game')


R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)


while True:
    window.fill((255,255,255))
    pygame.draw.rect(window, (R,G,B), (20,20,60,90), 0)
    if R >= 255:
        R = random.randint(0,255)
    else:
        R += 1
    if G >= 255:
        G = random.randint(0,255)
    else:
        G += 1
    if B >= 255:
        B = random.randint(0,255)
    else:
        B += 1
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()