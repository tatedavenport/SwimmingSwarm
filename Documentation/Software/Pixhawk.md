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
3. Use QGroundControl to set the FRAME_CONFIG parameter to `custom`

More information can be found [here][3] but this page is specifically for the Blue Robotics version of ArduSub which is significantly
behind the ArduPilot version.


# Build ArduSub and upload it to the Pixhawk
First, follow the setup instructions [here][4]. Then, follow instructions [here][5] to build the firmware. the The Pixhawk will most likely work best using the px4-v3 board.

We had issues with the setup script given by ArduPilot not working because there was a repository that failed to install halfway through. Because of this we had to download the gcc-arm cross compiler from [here][6] and follow the instructions [here][7] to get the compiler to work. Make sure to download the exact version referenced in the instructions. After that we had to install genromfs and empy by running 

`sudo apt-get install genromfs python-empy`

If you already failed to build the firmware before make sure to run `./waf clean` before trying again because sometimes the previously cached build will cause problems.

[1]: https://docs.qgroundcontrol.com/en/SetupView/Firmware.html
[2]: https://www.ardusub.com/developers/developers.html#making-a-custom-configuration
[3]: https://www.ardusub.com/developers/developers.html#developers
[4]: http://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux
[5]: https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md
[6]: http://ardupilot.org/dev/docs/building-setup-linux.html#setup-for-other-distributions
[7]: http://ardupilot.org/dev/docs/building-setup-linux.html#compiler
