# Running the code
1. Make sure that the address the node is connecting to is correct correct address for where Mosquitto will be running
in the `vizier.node.Node()` call.
   * Found [here][1] on the Raspberry Pi
   * Found [here][2] on the Topside Computer for the guiController
2. Launch Mosquitto by running `mosquitto -p 8080` (start mosquitto on topside computer listening to port 8080)
3. Start the Nodes. They will need to be started at about the same time as the nodes will timeout if they do not recieve a response
quickly enough.
   * Topside Computer: `python3 guiController.py -p 8080`
   * Raspberry Pi: `python3 robot.py (IP address of topside computer)`

[1]: ../../robot.py#L34
[2]: ../../guiController.py#L72
