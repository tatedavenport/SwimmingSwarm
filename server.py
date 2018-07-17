#socket_echo_server.py

from __future__ import print_function
from dronekit import connect

import socket
import sys


def joystickToChannel(value):
    #Channels range from 1148 to 1832 with 1500 being the center value
    center = (1148 + 1832)/2
    diff = (1832 - 1148)/2
    return center + (diff * value)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

connection_string = "/dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0-if00"
vehicle = connect(connection_string, wait_ready=True) #connect over mavlink


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                #data in format:
                #  yaw,forward|
                values = data.decode().split(",")
                values[1] = values[1].split("|")
                yaw = values[0]
                forward = values[0][0]

                
                vehicle.channels.overrides = {'4': joystickToChannel(yaw), '5': joystickToChannel(forward)}

                #repeat data back to client
                connection.sendall(data)
                
            else:
                print('no data from', client_address)
                
                vehicle.channels.overrides = {}
                break

    finally:
        # Clean up the connection
        connection.close()
        vehicle.channels.overrides = {}

