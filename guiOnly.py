# This file runs the Joystick GUI without connecting to the robot

import pygame
import math
import time


pygame.font.init() 

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
OFFWHITE = ( 235, 235, 235)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREY     = (   160, 160,  160)

def drawJoystick(x, y, xv, yv, screen):
    radius = 100
    pygame.draw.circle(screen, OFFWHITE, (x, y), radius)

    magnitude = radius * (xv**2 + yv**2)**.5
    angle = 0

    if xv == 0:
        if yv > 0:
            angle = math.radians(90)
        elif yv < 0:
            angle = math.radians(270)
        else:
            angle = 0
    else:
        angle = math.atan(yv/xv)
        
    if magnitude > radius:
        magnitude = radius

    if xv < 0:
        cx = int(x - magnitude*math.cos(angle))
        cy = int(y - magnitude*math.sin(angle))
    else:
        cx = int(x + magnitude*math.cos(angle))
        cy = int(y + magnitude*math.sin(angle))

    pygame.draw.circle(screen, RED, (cx, cy), 5)


def drawThrottle(x, y, value, color ,screen):
    height = 200
    pygame.draw.rect(screen, OFFWHITE, [x, y, 20, 2*height])
    ty = int(height*value)
    pygame.draw.rect(screen, color, [x, y+height, 20, ty])

    
def drawSteering(x, y, value, screen):
    width = 200
    pygame.draw.rect(screen, OFFWHITE, [x, y, 2*width, 20])
    tx = int(width*value)
    pygame.draw.rect(screen, BLUE, [x+width, y, tx, 20])


pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


done = False
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    yaw1 = joystick.get_axis(0)
    forward1 = joystick.get_axis(1)
    yaw2 = joystick.get_axis(2)
    throttle1 = joystick.get_axis(3)

    screen.fill(GREY)
    drawJoystick(215, 210, yaw1, forward1, screen)
    drawJoystick(425, 210, yaw2, throttle1, screen)
    drawThrottle(20, 40, forward1,GREEN, screen)
    drawThrottle(600, 40, throttle1,RED, screen)
    drawSteering(120, 400, yaw1, screen)

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface1 = myfont.render('Throttle', False, (0, 0, 0))
    textsurface2 = myfont.render('Yaw', False, (0,0,0))
    textsurface3 = myfont.render('Depth', False, (0,0,0))
    screen.blit(textsurface1,(5,10))
    screen.blit(textsurface2,(300,375))
    screen.blit(textsurface3,(570,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
