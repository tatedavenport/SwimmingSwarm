# Raspberry Pi
## Raspberry Pi won't connect to Pixhawk
*If this does not fix the issue check [here][2] for another possible solution*

The Raspberry pi won't connect to the pixhawk when the pi is showing the low voltage indicator
([a lightning bolt in the top right corner of the screen][1]). This can be caused by a variety of reasons but is usually due to
either low power input or high power draw from the usb ports.

## Raspberry Pi Freezes when trying to build a program
This is usually caused by the Raspberry Pi running out of RAM. This can be resolved by temporarily setting up a swap file on the SD card
for the RAM to overflow to. 

**WARNING: Do not leave the swap file enabled when not using it to build a program as extended use can degrade the SD card**
1. Create a swap file large enough to help compile the program (usually 1 or 2 GB is plenty) (Skip this step if you already have a swap file)
   
   `dd if=/dev/zero of=~/swap bs=1M count=1024`
   `mkswap ~/swap`
   This creates a swap file of 1024 chunks of 1MB making it 1GB then makes it a valid swap file.
2. Enable the swap file
    
    `swapon ~/swap`
3. Compile your program
4. **Disable the swap file**

   `swapoff`
   
## Raspberry Pi Won't Output To Screen
Sometimes if the Raspberry Pi isn't connected to a screen when it is powered on it will not initialize the HDMI Output so there will be no video out. Try disconnecting and reconnecting the power to the Raspberry Pi while the screen is plugged in and turned on.

# Pixhawk
## Pixhawk won't connect to Raspberry Pi
Sometimes the Pixhawk won't connect to MavLink if it does not have backup power throught the ESC's. This is because the Pixhawk treats being powered over USB as being on a testbed and won't arm without a seperate backup power source. 
This can be resolved by powering the Pixhawk through Telemetry2 or by hooking the ESC's up to a power supply/battery.
    
# Ubuntu
## Wayland Issues
*TODO* Add Information about Wayland Issues


[1]: https://lowpowerlab.com/wp-content/uploads/2016/09/Pi3LoadTest_LowVoltage.jpg
[2]: https://github.com/chachmu/SwimmingSwarm/blob/master/Documentation/Troubleshooting.md#raspberry-pi-won't-connect-to-pixhawk
