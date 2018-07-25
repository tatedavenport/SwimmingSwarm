#socket_echo_server.py

from __future__ import print_function
from dronekit import connect

import json
import random
import vizier.node as vizier_node
import time


def joystickToChannel(value):
    #Channels range from 1200 to 1700 with 1500 being the center value
    center = (1200 + 1700)/2
    diff = (1700 - 1200)/2
    return center + (diff * value)


connection_string = "/dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0-if00"
#vehicle = connect(connection_string, wait_ready=True) #connect over mavlink


# Ensure that Node Descriptor File can be Opened
node_descriptor = None
try:
        f = open("node_desc_robot.json", 'r')
        node_descriptor = json.load(f)
        f.close()
except Exception as e:
    print(repr(e))
    print("Couldn't open given node file node_desc_robot.json")

# Start the Node
node = vizier_node.Node("localhost", 1884, node_descriptor)
node.start()

# Get the links for Publishing/Subscribing
publishable_link = list(node.publishable_links)[0]
subscribable_link = list(node.subscribable_links)[0]
msg_queue = node.subscribe(subscribable_link)


#Initialize Connection
print("Connecting to Controller")

node.publish(publishable_link,"1")
message = msg_queue.get(timeout = 10).payload.decode(encoding='UTF-8')


recieved = False

while True:
    try:
        message = msg_queue.get(timeout = 1).payload.decode(encoding='UTF-8')
    
    except KeyboardInterrupt:
        break
    
    except:
        if recieved:
            print("Connection to Controller Lost")
            node.publish(publishable_link, "0")
            break
        else:
            recieved = True

    node.publish(publishable_link,"1")

    values = message.split(",")
    yaw = values[0]
    forward = values[1]
    throttle = values[2]
    print(yaw + "," + forward + "," + throttle)
    
    #vehicle.channels.overrides = {'4': joystickToChannel(yaw), '5': joystickToChannel(forward), '3': joystickToChannel(throttle)}
 

# Clean up the connection
node.publish(publishable_link,"0")
node.stop()
#vehicle.channels.overrides = {}

