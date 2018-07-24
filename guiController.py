#socket_echo_client.py

import socket
import sys

import pygame
import math

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

def drawJoystick(x, y, xv, yv, screen):
    radius = 100
    pygame.draw.circle(screen, BLACK, (x, y), radius, 2)

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


def drawThrottle(x, y, value, screen):
    height = 200
    pygame.draw.rect(screen, BLACK, [x, y, 20, 2*height], 2)
    pygame.draw.line(screen, BLACK, [x, y+height], [x+20, y+height], 3)
    ty = int(height*value)
    pygame.draw.rect(screen, GREEN, [x, y+height, 20, ty])

    
def drawSteering(x, y, value, screen):
    width = 200
    pygame.draw.rect(screen, BLACK, [x, y, 2*width, 20], 2)
    pygame.draw.line(screen, BLACK, [x+width, y], [x+width, y+20], 3)
    tx = int(width*value)
    pygame.draw.rect(screen, BLUE, [x+width, y, tx, 20])


def send_data(message):
    # Send data
    print('sending {!r}'.format(message))
    sock.sendall(str.encode(message))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        if data:
            print('received {!r}'.format(data))


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)


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
    forward2 = joystick.get_axis(3)
    #print("yaw: ", yaw1)
    #print("forward1: ",forward1)
    send_data(str(round(yaw1,3)) + "," + str(round(forward1,3)) + "|")

    screen.fill(WHITE)
    drawJoystick(215, 210, yaw1, forward1, screen)
    drawJoystick(425, 210, yaw2, forward2, screen)
    drawThrottle(5, 40, forward1,screen)
    drawSteering(120, 400, yaw1, screen)

    pygame.display.flip()

    clock.tick(60)


print('closing socket')
sock.close()
pygame.quit()
