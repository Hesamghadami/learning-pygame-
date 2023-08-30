import pygame,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

windowW=500
windowH=500
window = pygame.display.set_mode((windowW,windowH))
pygame.display.set_caption('Mouse')

mousePosition = None
mousePress = False

squareSize=40
squareColor=(255,0,0)
squareX=windowW/2
squareY=windowH-squareSize
gravity=0.00000000001
drag = False


def checkBounds():
    global squareColor,squareX,squareY,drag,squareSize

    if mousePress == True:
        if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:
            if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:
                drag = True
                pygame.mouse.set_visible(0)
    else:
        squareColor = (255,0,0)
        pygame.mouse.set_visible(1)
        drag = False

def checkGravity():
    global gravity,squareY,squareSize,windowW

    if squareY < windowH - squareSize and mousePress == False:
        squareY += gravity
        gravity = gravity * 1.1
    else:
        squareY = windowH - squareSize
        gravity = 0.00000000001

def drawSquare():
    global squareColor,squareX,squareY,drag

    if drag == True:
        squareColor = (0,255,0)
        squareX = mousePosition[0] - squareSize / 2
        squareY = mousePosition[1] - squareSize / 2

    pygame.draw.rect(window,squareColor,(squareX,squareY,squareSize,squareSize))





while True:
    window.fill((0,0,0))
    mousePosition = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] == True:
        mousePress = True
    else:
        mousePress = False

    checkBounds()
    checkGravity()
    drawSquare()


    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()