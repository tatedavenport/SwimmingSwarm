#socket_echo_client.py

import socket
import sys

import pygame


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
server_address = ('192.168.43.54', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)


pygame.init()
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
    #print("yaw: ", yaw1)
    #print("forward1: ",forward1)
    send_data(str(round(yaw1,3)) + "," + str(round(forward1,3)) + "|")


print('closing socket')
sock.close()

