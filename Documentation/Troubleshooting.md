# Raspberry Pi
		The Raspberry pi won't connect to the pixhawk when the pi is showing the low voltage indicator
    ([a lightning bolt in the top right corner of the screen][1]). This can be caused by a variety of reasons but is usually due to
    either low power input or high power draw from the usb ports.
    
# Pixhawk
		Sometimes the Pixhawk won't connect to MavLink if not backup powered through the ESC's. This is because the Pixhawk treats being powered
    over USB as being on a testbed and won't arm without a seperate backup power source. This can be resolved by powering the Pixhawk
    through Telemetry2 or by hooking the ESC's up to a power supply/battery.
    
    
    [1]: https://lowpowerlab.com/wp-content/uploads/2016/09/Pi3LoadTest_LowVoltage.jpg
