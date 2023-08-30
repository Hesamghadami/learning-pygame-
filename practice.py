import pygame, sys 
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()
windowW=800
windowH=500


window = pygame.display.set_mode((windowW,windowH))
pygame.display.set_caption('Game')

playerSize=20
playerX=(windowW/2)-(playerSize/2)
playery=windowH-playerSize
playerVX=0.1
playerVY=0.0
moveSpeed=0.1
maxSpeed=10.0
jumpH=25.0
gravity=1.0  

moveVY = 0.1
movespeedy = 0.1 
upDown = False
down = False
leftDown=False
rightDown=False
Jump = False

def move():
    global playerX,playery,playerVX,playerVY,Jump,gravity, moveVY, movespeedy

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


    if upDown:
        if moveVY > 0.0:
            moveVY = movespeedy
            moveVY = -moveVY
        if playery > 0:
            playery += moveVY

    if down:

        if moveVY < 0.0:
            moveVY = movespeedy
        if playery + playerSize < windowH:
            playery += moveVY


    #if (playerVX > 0.0 and playerVX < maxSpeed) or (playerVX < 0.0 and playerVX > -maxSpeed):
        #if not Jump and (leftDown or rightDown):
            #playerVX = playerVX * 1.1

    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else:
        playerVY = 0.0
        Jump=False

    if Jump:
        if playery < windowH - playerSize:
            playery += gravity

        else:
            playery = windowH - playerSize
            gravity = 1.0

    playery -= playerVY

while True:
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(playerX,playery,playerSize,playerSize))
    
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                leftDown = True
            if event.key == pygame.K_d:
                rightDown = True
            if event.key == pygame.K_w:
                upDown = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_SPACE:
                if not Jump:
                    Jump = True
                    playerVY += jumpH

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_d:
                rightDown = False
                playerVX = moveSpeed

            if event.key == pygame.K_w:
                upDown = False
            if event.key == pygame.K_s:
                down = False

        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    move()
    pygame.display.update()