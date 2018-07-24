#socket_echo_server.py

from __future__ import print_function
from dronekit import connect

import socket
import sys


def joystickToChannel(value):
    #Channels range from 1200 to 1700 with 1500 being the center value
    center = (1200 + 1700)/2
    diff = (1700 - 1200)/2
    return center + (diff * value)



connection_string = "/dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0-if00"
#vehicle = connect(connection_string, wait_ready=True) #connect over mavlink


while True:
    try:

                values = data.decode().split(",")
                values[1] = values[1].split("|")
                yaw = values[0]
                forward = values[0][0]

                
                #vehicle.channels.overrides = {'4': joystickToChannel(yaw), '5': joystickToChannel(forward)}
    
    finally:
        # Clean up the connection
        connection.close()
        #vehicle.channels.overrides = {}

