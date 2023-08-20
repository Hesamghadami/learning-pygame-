import pygame, sys 
import pygame.locals as GAME_GLOBAL
import pygame.event as GAME_EVENT


pygame.init()

windowH = 500
windowW = 800

window  = pygame.display.set_mode((windowW, windowH))


leftDown=False
rightDown=False
Jump1 = False

playerSize=20
playerX=(windowW/2)-(playerSize/2)
playery=windowH-playerSize
playerVX=0.1
playerVY=0.0
moveSpeed=0.1
jumpH=25.0
gravity=0.1
def shape1():
    global Jump1,playerX,playery,playerVX,playerVY,gravity



    if leftDown:
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX
        if playerX > 0:
            playerX += playerVX

    if rightDown:
        if playerVX < 0.0:
            playerVX = moveSpeed
        if playerX + playerSize < windowW:
            playerX += playerVX

    #if (playerVX > 0.0 and playerVX < maxSpeed) or (playerVX < 0.0 and playerVX > -maxSpeed):
        #if not Jump and (leftDown or rightDown):
            #playerVX = playerVX * 1.1

    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else:
        playerVY = 0.0
        Jump1=False
    if playery < windowH - playerSize:
        playery += gravity
        #gravity = gravity * 1.1
    else:
        playery = windowH - playerSize
        # gravity = 1.0

    playery -= playerVY


leftDown2=False
rightDown2=False
Jump2 = False

playerSize=20
circleX=210
circley=windowH-playerSize/2
circleVX=0.1
circleVY=0.0
moveSpeed=0.1
jumpH=25.0
gravity=0.1


def shape2():
    global Jump2, circleVX, circleVY, moveSpeed, gravity, circleX, circley



    if leftDown2:
        if circleVX > 0.0:
            circleVX = moveSpeed
            circleVX = -circleVX
        if circleX > 0:
            circleX += circleVX

    if rightDown2:
        if circleVX < 0.0:
           circleVX = moveSpeed
        if circleX + playerSize < windowW:
            circleX += circleVX

    #if (playerVX > 0.0 and playerVX < maxSpeed) or (playerVX < 0.0 and playerVX > -maxSpeed):
        #if not Jump and (leftDown or rightDown):
            #playerVX = playerVX * 1.1

    if circleVY > 1.0:
        circleVY = circleVY * 0.9
    else:
        circleVY = 0.0
        Jump2=False
    if circley < windowH - playerSize/2:
        circley += gravity
        #gravity = gravity * 1.1
    else:
        circley = windowH - playerSize/2
        # gravity = 1.0

    circley -= circleVY






while True:
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(playerX,playery,playerSize,playerSize))
    pygame.draw.circle(window,(0,255,0),(circleX,circley), playerSize/2)
    for event in GAME_EVENT.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not Jump1:
                    Jump1 = True
                    playerVY += jumpH

            
            if event.key == pygame.K_d:
                rightDown2 = True
            if event.key == pygame.K_a:
                leftDown2 = True
            if event.key == pygame.K_w:
                if not Jump2:
                    Jump2 = True
                    circleVY += jumpH

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed



            if event.key == pygame.K_d:
                rightDown2 = False
                circleVX = moveSpeed
            if event.key == pygame.K_a:
                leftDown2 = False
                circleVx = moveSpeed

        if event.type == GAME_GLOBAL.QUIT:
            pygame.quit()
            sys.exit()

    shape1()
    shape2()
    pygame.display.update()