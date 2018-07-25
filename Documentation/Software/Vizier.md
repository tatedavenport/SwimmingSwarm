# Overview
Vizier is 
"A networking framework built on top of MQTT to allow the communication and synchronization of distributed,
language-independent resources"


Basically, it allows you to send messages between devices using an MQTT Server to mediate between them. The messages are sent back and forth
between "nodes" which in our use case are the Topside Computer and the robot. Each of the nodes has a JSON file that describes
what types of messages the node can send and recieve. This allows the python script to request a certain type of message from the
server which then sends back the correct information.

# JSON Description Files
## Purpose
The JSON Description files are used to describe what types of messages a node can send and recieve as well as the name of the node.

## Format
The JSON File is formatted in this order:

1. The `end_point` (the node) is given a name
2. A List of the "links" which are the possible messages it can send.
   1. The link has its own list of links
   2. The type that the link is. This can one of two types:
      * STREAM "publishes" the data given to it over the link
      * DATA "puts" the data on the link
   3. The requests that the node can make. These ask the server to respond with the data specified.

This is the JSON description file for the robot node:
```JSON
{
  "end_point" : "robot",
  "links" :
  {
    "/state" :
    {
      "links" : {},
      "type" : "STREAM"
    }
  },
  "requests" : ["controller/input"]
}
```
`controller` is the name of the other node that it is connecting to and it can request the data labeled `input`.
