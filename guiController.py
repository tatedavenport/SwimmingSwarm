import json
import numpy as np
import vizier.node as vizier_node
import pygame
import math
import time

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
OFFWHITE = ( 235, 235, 235)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREY     = (   160, 160,  160)

def drawJoystick(x, y, xv, yv, screen):
    #Draws the Circular Joystick value indicator

    radius = 100
    pygame.draw.circle(screen, OFFWHITE, (x, y), radius)

    #Large amount of math to convert  the joystick input from a square looking map (where the top right is 1.0, 1.0)
    #to a circle where the top right is sqrt(2), sqrt(2)

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
    # Draws a vertical indicator
    height = 200
    pygame.draw.rect(screen, OFFWHITE, [x, y, 20, 2*height])
    ty = int(height*value)
    pygame.draw.rect(screen, color, [x, y+height, 20, ty])

    
def drawSteering(x, y, value, screen):
    #Draws a horizontal indicator
    width = 200
    pygame.draw.rect(screen, OFFWHITE, [x, y, 2*width, 20])
    tx = int(width*value)
    pygame.draw.rect(screen, BLUE, [x+width, y, tx, 20])


# Ensure that Node Descriptor File can be Opened
node_descriptor = None
try:
        f = open("node_desc_controller.json", 'r')
        node_descriptor = json.load(f)
        f.close()
except Exception as e:
    print(repr(e))
    print("Couldn't open given node file node_desc_controller.json")

# Start the Node
node = vizier_node.Node("localhost", 1884, node_descriptor)
node.start()

# Get the links for Publishing/Subscribing
publishable_link = list(node.publishable_links)[0]
subscribable_link = list(node.subscribable_links)[0]
msg_queue = node.subscribe(subscribable_link)

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


done = False
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#Initialize Connection
print("Connecting to Robot")

node.publish(publishable_link,"0,0,0")
state = 0

recieved = False

while not done:
    #Check for Exit Event from Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    yaw1 = joystick.get_axis(0)
    forward1 = joystick.get_axis(1)
    yaw2 = joystick.get_axis(2)
    throttle1 = joystick.get_axis(3)

    # Recieve data here
    try:
        #Recieve Vizier Messages
        message = msg_queue.get(timeout = 1).payload.decode(encoding='UTF-8')
        state = int(message)
    except:
        if recieved:
            print("Connection to robot lost")
            node.publish(publishable_link,"0,0,0")
            break
        else:
            recieved = True
            state = 1

    if state != 1:
        #Robot sent back bad status
        print("Connection to robot lost")
        node.publish(publishable_link,"0,0,0")
        break

    #Send Vizier Message
    node.publish(publishable_link, str(round(yaw1,3)) + "," + str(round(forward1, 3)) + "," + str(round(throttle1,3)))

    #Clear Screen to Background Color
    screen.fill(GREY)

    #Draw Joystick Indicators
    drawJoystick(215, 210, yaw1, forward1, screen)
    drawJoystick(425, 210, yaw2, throttle1, screen)

    #Draw Vertical Indicators
    drawThrottle(20, 40, forward1,GREEN, screen)
    drawThrottle(600, 40, throttle1,RED, screen)

    #Draw Horizontal Indicator
    drawSteering(120, 400, yaw1, screen)

    #Draw Labels
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface1 = myfont.render('Throttle', False, (0, 0, 0))
    textsurface2 = myfont.render('Yaw', False, (0,0,0))
    textsurface3 = myfont.render('Depth', False, (0,0,0))
    screen.blit(textsurface1,(5,10))
    screen.blit(textsurface2,(300,375))
    screen.blit(textsurface3,(570,10))

    #update Screen
    pygame.display.flip()

    #Limit FPS to 60
    clock.tick(60)

#Clean up Connection
node.stop()

#Quit Pygame
pygame.quit()
