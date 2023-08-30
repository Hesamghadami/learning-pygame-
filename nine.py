import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

windowW=800
windowH=600
window = pygame.display.set_mode((windowW,windowH))
pygame.display.set_caption('car')

myPic = pygame.image.load('car.png')

s=pygame.time.Clock()

def car(x,y):
    window.blit(myPic,(x,y))

x = windowW * 0.3
y = windowH * 0.7
speedX = 0
speedY = 0


while True:
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -3
            if event.key == pygame.K_RIGHT:
                speedX = 3
            if event.key == pygame.K_UP:
                speedY = -3
            if event.key == pygame.K_DOWN:
                speedY = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedX = 0
                speedY = 0

        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    x += speedX
    y += speedY

    window.fill((255,255,255))
    car(x,y)
    pygame.display.update()
    s.tick(10)
