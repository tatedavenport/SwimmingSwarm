# Setup
## Topside Computer
1. Make sure you have installed `pygame` as shown in the [Topside Computer documentation][1].
2. Install Vizier
   1. Clone or download the [repository][2].
   2. Run the setup script from the vizier/python folder by running
    `sudo python3 setup.py install`
   3. Install Mosquitto by running `sudo apt-get install Mosquitto`

## Raspberry Pi
1. Install Vizier the same way it was installed on the Topside Computer
2. Make sure that Dronekit and PyMavLink are installed as showin in the [Raspberry Pi documentation][3]

# Running the code
1. Make sure that the address the node is connecting to is correct correct address for where Mosquitto will be running
in the `vizier_node.Node()` call.
   * Found [here][4] on the Raspberry Pi
   * Found [here][5] on the Topside Computer for the guiController
2. Launch Mosquitto by running `Mosquitto -p 1884`
3. Start the Nodes. They will need to be started at about the same time as the nodes will timeout if they do not recieve a response
quickly enough.
   * Topside Computer: `python3 guiController.py`
   * Raspberry Pi: `python3 robot.py`

[1]: https://github.com/chachmu/SwimmingSwarm/blob/master/Documentation/Software/TopsideComputer.md#other-required-software
[2]: https://github.com/robotarium/vizier
[3]: https://github.com/chachmu/SwimmingSwarm/blob/master/Documentation/Software/RaspberryPi.md#installing-dependencies-for-joystick-control-over-wifi
[4]: https://github.com/chachmu/SwimmingSwarm/blob/04b4c606ec923ecefc45c05d37f08ebd242f9115/robot.py#L34
[5]: https://github.com/chachmu/SwimmingSwarm/blob/04b4c606ec923ecefc45c05d37f08ebd242f9115/guiController.py#L72
