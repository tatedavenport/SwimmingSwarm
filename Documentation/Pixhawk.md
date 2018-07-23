# Flash firmware through QGroundControl
QGroundControl comes packaged with the most recent stable versions of ArduPilot and can flash them to the Pixhawk. 
Instructions for flashing default firmware can be found [here][1].

# Create Custom Frame
ArduSub supports custom motor layouts called frames. In order to do this:
1. Add the frame to AP_Motors6DOF.cpp
   1. This can be found in `Ardupilot/libraries\AP_Motors\AP_Motors6DOF.cpp`
   2. Search for SUB_FRAME_CUSTOM and your motor there following [this template][2]
   3. Uncomment the break statement after the added commands
2. Compile the firmware and upload it to the Pixhawk

More information can be found [here][3] but this page is specifically for the Blue Robotics version of ArduSub which is significantly
behind the ArduPilot version.


# Build ArduSub and upload it to the Pixhawk
Follow the instructions [here][4]. The Pixhawk will most likely work best using the px4-v3 board.

*TODO* add information about arm-none-eabi-gcc

[1]: https://docs.qgroundcontrol.com/en/SetupView/Firmware.html
[2]: https://www.ardusub.com/developers/developers.html#making-a-custom-configuration
[3]: https://www.ardusub.com/developers/developers.html#developers
[4]: https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md
